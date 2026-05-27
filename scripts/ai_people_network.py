"""
AI 创业人脉网络

节点 = 人物
节点大小 ∝ degree (连接数)
节点颜色 = 所属圈层
边样式 = 关系类型 (共事/共创 / 师承 / 资助)
"""
from pathlib import Path
import math
import os
import numpy as np

_mpl_cache = Path('/tmp/snowboat-matplotlib')
_mpl_cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR', str(_mpl_cache))

import matplotlib
import matplotlib.font_manager as fm
import matplotlib.patheffects as pe
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch

# ============ 中文字体 (跨平台 fallback) ============
_candidate_fonts = [
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
    '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
    'C:/Windows/Fonts/msyh.ttc',
]
font_path = next((p for p in _candidate_fonts if Path(p).exists()), None)
if font_path:
    fm.fontManager.addfont(font_path)

def _font(size, bold=False):
    if not font_path:
        return fm.FontProperties(size=size)
    return fm.FontProperties(fname=font_path, size=size,
                             weight='bold' if bold else 'normal')

cn_label  = _font(9)
cn_hub    = _font(10, bold=True)
cn_title  = _font(24, bold=True)
cn_sub    = _font(13)
cn_legend = _font(11)
cn_legend_title = _font(12, bold=True)
cn_foot   = _font(9)
cn_anno   = _font(10)

matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['svg.fonttype'] = 'none'

# ============ 节点 ============
# (name, cluster)
nodes_spec = [
    # OpenAI 系 (创始人 / 校友)
    ('Sam Altman',         'openai'),
    ('Elon Musk',          'openai'),
    ('Ilya Sutskever',     'openai'),
    ('Greg Brockman',      'openai'),
    ('Andrej Karpathy',    'openai'),
    ('John Schulman',      'openai'),
    ('Mira Murati',        'openai'),
    ('Dario Amodei',       'openai'),
    ('Daniela Amodei',     'openai'),
    ('Aravind Srinivas',   'openai'),
    ('David Luan',         'openai'),

    # 学术 (PhD 导师 / 实验室源头)
    ('Geoffrey Hinton',    'academic'),
    ('Fei-Fei Li',         'academic'),
    ('Pieter Abbeel',      'academic'),

    # 资本 (PayPal Mafia + YC)
    ('Peter Thiel',        'capital'),
    ('Reid Hoffman',       'capital'),
    ('Paul Graham',        'capital'),
    ('Jessica Livingston', 'capital'),

    # DeepMind / Brain 系
    ('Demis Hassabis',     'deepmind'),
    ('Mustafa Suleyman',   'deepmind'),
    ('Arthur Mensch',      'deepmind'),
    ('Noam Shazeer',       'deepmind'),
    ('Daniel De Freitas',  'deepmind'),
    ('Aidan Gomez',        'deepmind'),

    # 孤立 (独立创业者，无圈层血缘)
    ('David Holz',         'isolated'),    # Midjourney
    ('Harrison Chase',     'isolated'),    # LangChain
    ('Valenzuela',         'isolated'),    # Runway
    ('Amit Jain',          'isolated'),    # Luma
    ('Demi Guo',           'isolated'),    # Pika
    ('Chenlin Meng',       'isolated'),    # Pika
]

# ============ 边 ============
# (src, dst, etype)  etype ∈ {'institution', 'mentor', 'backer'}
edges_spec = [
    # —— OpenAI 联合创始人核心 clique ——
    ('Sam Altman',     'Elon Musk',        'institution'),
    ('Sam Altman',     'Greg Brockman',    'institution'),
    ('Sam Altman',     'Ilya Sutskever',   'institution'),
    ('Sam Altman',     'Andrej Karpathy',  'institution'),
    ('Sam Altman',     'John Schulman',    'institution'),
    ('Elon Musk',      'Ilya Sutskever',   'institution'),
    ('Greg Brockman',  'Ilya Sutskever',   'institution'),
    ('Greg Brockman',  'Andrej Karpathy',  'institution'),
    ('Greg Brockman',  'John Schulman',    'institution'),
    ('Ilya Sutskever', 'Andrej Karpathy',  'institution'),
    ('Ilya Sutskever', 'John Schulman',    'institution'),

    # —— OpenAI 高管 / 校友 ——
    ('Sam Altman',     'Mira Murati',      'institution'),
    ('Greg Brockman',  'Mira Murati',      'institution'),
    ('Sam Altman',     'Dario Amodei',     'institution'),
    ('Greg Brockman',  'Dario Amodei',     'institution'),
    ('Ilya Sutskever', 'Dario Amodei',     'institution'),
    ('Dario Amodei',   'John Schulman',    'institution'),
    ('Dario Amodei',   'Daniela Amodei',   'institution'),   # Anthropic 联创 + 兄妹
    ('Sam Altman',     'Aravind Srinivas', 'institution'),
    ('Sam Altman',     'David Luan',       'institution'),

    # —— 师承 (PhD 导师) ——
    ('Geoffrey Hinton', 'Ilya Sutskever',  'mentor'),   # Toronto PhD
    ('Fei-Fei Li',      'Andrej Karpathy', 'mentor'),   # Stanford PhD
    ('Pieter Abbeel',   'John Schulman',   'mentor'),   # Berkeley PhD
    ('Pieter Abbeel',   'Aravind Srinivas','mentor'),   # Berkeley PhD
    ('Paul Graham',     'Sam Altman',      'mentor'),   # YC mentor

    # —— PayPal Mafia 内部 ——
    ('Elon Musk',     'Peter Thiel',       'institution'),
    ('Elon Musk',     'Reid Hoffman',      'institution'),
    ('Peter Thiel',   'Reid Hoffman',      'institution'),

    # —— PayPal → OpenAI 资助 ——
    ('Peter Thiel',   'Sam Altman',        'backer'),
    ('Reid Hoffman',  'Sam Altman',        'backer'),

    # —— YC 内部 ——
    ('Paul Graham',        'Jessica Livingston', 'institution'),
    ('Jessica Livingston', 'Sam Altman',         'institution'),

    # —— Musk-Karpathy (Tesla 共事) ——
    ('Elon Musk', 'Andrej Karpathy', 'institution'),

    # —— DeepMind 内部 ——
    ('Demis Hassabis',   'Mustafa Suleyman', 'institution'),
    ('Demis Hassabis',   'Arthur Mensch',    'institution'),
    ('Mustafa Suleyman', 'Arthur Mensch',    'institution'),

    # —— Google Brain 内部 ——
    ('Noam Shazeer', 'Daniel De Freitas',  'institution'),
    ('Noam Shazeer', 'Aidan Gomez',        'institution'),

    # —— Hoffman ↔ Suleyman: Inflection 联创 (跨圈) ——
    ('Reid Hoffman', 'Mustafa Suleyman', 'institution'),

    # —— Pika 联创 ——
    ('Demi Guo', 'Chenlin Meng', 'institution'),
]

# ============ 视觉常量 ============
PALETTE = {
    'openai':   {'fill': '#3B82F6', 'dark': '#1E40AF', 'name': 'OpenAI 系'},
    'deepmind': {'fill': '#E11D48', 'dark': '#9F1239', 'name': 'DeepMind / Brain 系'},
    'capital':  {'fill': '#D97706', 'dark': '#92400E', 'name': '资本 (PayPal + YC)'},
    'academic': {'fill': '#7C3AED', 'dark': '#5B21B6', 'name': '学术 (PhD 导师)'},
    'isolated': {'fill': '#94A3B8', 'dark': '#475569', 'name': '孤立创业者'},
}
EDGE_STYLES = {
    'institution': {'color': '#334155', 'linestyle': '-',  'alpha': 0.30, 'width': 1.2,
                    'label': '共事 / 共同创立'},
    'mentor':      {'color': '#F59E0B', 'linestyle': '--', 'alpha': 0.85, 'width': 1.8,
                    'label': '师承 (PhD / 导师)'},
    'backer':      {'color': '#0EA5E9', 'linestyle': ':',  'alpha': 0.85, 'width': 1.9,
                    'label': '资助 (早期投资人)'},
}
BG_COLOR = '#FAFAF7'
TEXT_DARK = '#0F172A'
TEXT_MUTED = '#64748B'

# ============ 构图 ============
G = nx.Graph()
node_meta = {}
for name, cluster in nodes_spec:
    G.add_node(name)
    node_meta[name] = {'cluster': cluster}
for src, dst, etype in edges_spec:
    G.add_edge(src, dst, etype=etype)

degrees = dict(G.degree())

# ============ 布局 (手工锚定) ============
# 4 个 hub 区域 + 孤立排底部一行
pos = {
    # 学术 (最左侧 column) - 师承边的源头, 故意压低避开左上图例
    'Geoffrey Hinton':    (-4.6,  1.0),
    'Fei-Fei Li':         (-4.6,  0.1),
    'Pieter Abbeel':      (-4.6, -0.9),

    # OpenAI cluster (center)
    'Andrej Karpathy':    (-2.3,  1.9),    # 接 Fei-Fei (师承)
    'Ilya Sutskever':     (-3.3,  1.2),    # 接 Hinton (师承)
    'Greg Brockman':      (-0.9,  1.5),
    'Sam Altman':         (-0.1,  0.4),    # 中央
    'John Schulman':      (-3.4,  0.1),    # 接 Abbeel (师承)
    'Mira Murati':        ( 1.2,  1.1),
    'Dario Amodei':       ( 1.8,  1.7),
    'Daniela Amodei':     ( 2.6,  1.0),
    'Aravind Srinivas':   (-3.4, -0.9),    # 接 Abbeel (师承)
    'David Luan':         ( 1.4,  0.0),
    'Elon Musk':          (-1.7, -0.6),    # 桥到 PayPal Mafia

    # DeepMind / Brain (右侧)
    'Demis Hassabis':     ( 3.7,  1.9),
    'Mustafa Suleyman':   ( 4.7,  1.1),
    'Arthur Mensch':      ( 4.9,  0.2),
    'Noam Shazeer':       ( 3.4,  0.4),
    'Daniel De Freitas':  ( 4.5, -0.6),
    'Aidan Gomez':        ( 3.4, -0.7),

    # 资本 (底部一行, Hoffman 在右侧便于接 Suleyman)
    'Paul Graham':        (-3.7, -1.7),
    'Jessica Livingston': (-2.3, -1.7),
    'Peter Thiel':         ( 0.1, -1.7),
    'Reid Hoffman':        ( 1.7, -1.7),
}

# 孤立行: 自动均匀
isolated_names = [n for n, m in node_meta.items() if m['cluster'] == 'isolated']
iso_y = -2.9
iso_xs = np.linspace(-4.6, 4.6, len(isolated_names))
for x, name in zip(iso_xs, isolated_names):
    pos[name] = (x, iso_y)

# ============ 绘图 ============
fig, ax = plt.subplots(figsize=(20, 14), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

# 孤立行底色 + 小标题
iso_bg = FancyBboxPatch(
    (-5.4, iso_y - 0.55), 10.8, 1.0,
    boxstyle="round,pad=0.05,rounding_size=0.15",
    linewidth=0, facecolor='#F1F5F9', alpha=0.7, zorder=0,
)
ax.add_patch(iso_bg)
ax.text(-5.35, iso_y + 0.65, '孤立创业者 · 无 OpenAI / DeepMind / 资本 / 学术 圈层关联',
        ha='left', va='bottom', fontproperties=_font(10),
        color=TEXT_MUTED, zorder=1)

# 边: 按类型分批
for etype, style in EDGE_STYLES.items():
    edge_list = [(u, v) for u, v, d in G.edges(data=True) if d['etype'] == etype]
    if not edge_list:
        continue
    nx.draw_networkx_edges(
        G, pos, edgelist=edge_list,
        edge_color=style['color'], style=style['linestyle'],
        alpha=style['alpha'], width=style['width'], ax=ax,
    )

# 节点大小: 与 degree 挂钩, 但用线性 + 上限避免 Sam Altman (d=13) 完全压住其他节点
def node_size(name):
    d = degrees[name]
    return max(1000, min(4500, 1000 + d * 270))

# 节点: 高 degree 用深色填充 (视觉上更"中心"), 其余用浅色填充
HUB_DEGREE = 5
def is_hub_like(name):
    return degrees[name] >= HUB_DEGREE

for cluster in ('isolated', 'capital', 'academic', 'deepmind', 'openai'):
    nlist = [n for n in G.nodes() if node_meta[n]['cluster'] == cluster]
    if not nlist:
        continue
    colors = [PALETTE[cluster]['dark'] if is_hub_like(n) else PALETTE[cluster]['fill']
              for n in nlist]
    sizes = [node_size(n) for n in nlist]
    nx.draw_networkx_nodes(
        G, pos, nodelist=nlist,
        node_color=colors, node_size=sizes,
        alpha=0.93, edgecolors='white', linewidths=2.5, ax=ax,
    )

# 标签: 人名统一置于节点下方, 避免长英文名压在圆圈里
def label_offset(name):
    # 节点下方偏移 = 节点半径 + 间距, 单位与 ax 一致
    sz = node_size(name)
    # 800-5000 -> 半径约 0.16-0.42 数据单位 (估算)
    r = 0.045 + math.sqrt(sz) * 0.0042
    return r + 0.04

for name, (x, y) in pos.items():
    off = label_offset(name)
    txt = ax.text(x, y - off, name,
                  ha='center', va='top',
                  color=TEXT_DARK,
                  fontproperties=cn_label,
                  bbox=dict(boxstyle='round,pad=0.12',
                            facecolor=BG_COLOR,
                            edgecolor='none',
                            alpha=0.9),
                  zorder=10)
    txt.set_path_effects([pe.withStroke(linewidth=1.8, foreground='white')])

# ============ 图例 ============
cluster_handles = [
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=v['fill'], markeredgecolor='white', markeredgewidth=1.5,
           markersize=15, label=v['name'])
    for v in PALETTE.values()
]
edge_handles = [
    Line2D([0], [0], color=s['color'], linestyle=s['linestyle'],
           linewidth=2.4, label=s['label'])
    for s in EDGE_STYLES.values()
]

leg1 = ax.legend(
    handles=cluster_handles, loc='upper left',
    bbox_to_anchor=(0.005, 0.995),
    frameon=True, facecolor='white', edgecolor='#E2E8F0',
    prop=cn_legend, title='圈层',
    title_fontproperties=cn_legend_title,
    labelspacing=0.55, borderpad=0.7, handletextpad=1.0,
)
leg1.get_frame().set_linewidth(1.0)
ax.add_artist(leg1)
leg2 = ax.legend(
    handles=edge_handles, loc='upper right',
    bbox_to_anchor=(0.995, 0.995),
    frameon=True, facecolor='white', edgecolor='#E2E8F0',
    prop=cn_legend, title='关系类型',
    title_fontproperties=cn_legend_title,
    labelspacing=0.55, borderpad=0.7, handletextpad=1.0,
)
leg2.get_frame().set_linewidth(1.0)

# ============ 标题 / 副标题 / 页脚 ============
fig.text(0.5, 0.965, 'AI 创业人脉网络 · OpenAI / DeepMind 系核心人物族谱',
         ha='center', va='top', fontproperties=cn_title, color=TEXT_DARK)
fig.text(0.5, 0.928,
         '节点大小 ∝ 连接数 · 颜色 = 所属圈层 · 边样式 = 关系类型',
         ha='center', va='top', fontproperties=cn_sub, color='#475569')
fig.text(0.99, 0.012,
         f'节点 {G.number_of_nodes()} · 边 {G.number_of_edges()} · 数据截至 2026.05',
         ha='right', va='bottom', fontproperties=cn_foot, color='#94A3B8')

ax.set_xlim(-5.7, 5.7)
ax.set_ylim(-3.6, 2.6)
ax.set_aspect('equal')
ax.axis('off')

# ============ 输出 ============
out_dir = Path(__file__).resolve().parent.parent / 'diagram' / 'ai-people-network'
out_dir.mkdir(parents=True, exist_ok=True)
out_svg = out_dir / 'diagram.svg'
out_png = out_dir / 'ai_people_network.png'
plt.tight_layout(rect=[0, 0.01, 1, 0.92])
plt.savefig(out_svg, bbox_inches='tight', facecolor=BG_COLOR)
plt.savefig(out_png, dpi=180, bbox_inches='tight', facecolor=BG_COLOR)
print(f'Done → {out_svg}')
print(f'Preview → {out_png}')
print(f'Nodes: {G.number_of_nodes()}  Edges: {G.number_of_edges()}')
print('Top by degree:', sorted(degrees.items(), key=lambda x: -x[1])[:7])
