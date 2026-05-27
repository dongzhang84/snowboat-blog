"""
美国 AI 创业公司关系网络图

节点 = 公司 / 机构
节点大小 ∝ degree (连接数)
节点颜色 = 所属圈层
边样式 = 关系类型 (创始团队出走 / 投资 / 人才流动)
☆ = 2024 被大厂 reverse acquihire (Adept→Amazon, Covariant→Amazon,
    Inflection→Microsoft, Character.AI→Google)
"""
from pathlib import Path
import math
import numpy as np

import matplotlib
import matplotlib.font_manager as fm
import matplotlib.patheffects as pe
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# ============ 中文字体 (跨平台 fallback) ============
_candidate_fonts = [
    '/System/Library/Fonts/PingFang.ttc',                       # macOS
    '/System/Library/Fonts/STHeiti Medium.ttc',                 # macOS
    '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',   # Linux
    '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',           # Linux
    'C:/Windows/Fonts/msyh.ttc',                                # Windows
]
font_path = next((p for p in _candidate_fonts if Path(p).exists()), None)
if font_path:
    fm.fontManager.addfont(font_path)

def _font(size, bold=False):
    if not font_path:
        return fm.FontProperties(size=size)
    return fm.FontProperties(fname=font_path, size=size,
                             weight='bold' if bold else 'normal')

cn_label  = _font(10)
cn_hub    = _font(12, bold=True)
cn_title  = _font(24, bold=True)
cn_sub    = _font(13)
cn_legend = _font(11)
cn_legend_title = _font(12, bold=True)
cn_foot   = _font(9)

matplotlib.rcParams['axes.unicode_minus'] = False

# ============ 节点定义 ============
# (name, cluster, is_hub, is_acquihired, year)
nodes_spec = [
    # 源头 / hub
    ('OpenAI',             'openai',   True,  False, '2015'),
    ('DeepMind',           'deepmind', True,  False, '2010'),
    ('Google Brain',       'deepmind', True,  False, '2011'),
    ('PayPal Mafia',       'paypal',   True,  False, '资本源头'),

    # OpenAI 血缘裂变
    ('Anthropic',          'openai',   False, False, '2021'),
    ('xAI',                'openai',   False, False, '2023'),
    ('SSI',                'openai',   False, False, '2024'),
    ('Thinking\nMachines', 'openai',   False, False, '2025'),
    ('Perplexity',         'openai',   False, False, '2022'),
    ('Eureka Labs',        'openai',   False, False, '2024'),
    ('Adept',              'openai',   False, True,  '2022'),   # → Amazon (2024.6)
    ('Covariant',          'openai',   False, True,  '2017'),   # → Amazon (2024.8)
    ('Dust',               'openai',   False, False, '2023'),
    ('Softmax',            'openai',   False, False, '2023'),
    ('Cursor',             'openai',   False, False, '2022'),  # OpenAI Startup Fund 投资

    # DeepMind / Brain 血缘裂变
    ('Mistral',            'deepmind', False, False, '2023'),
    ('Character.AI',       'deepmind', False, True,  '2021'),   # → Google (2024.8)
    ('Cohere',             'deepmind', False, False, '2019'),
    ('Inflection',         'deepmind', False, True,  '2022'),   # → Microsoft (2024.3)
    ('World Labs',         'deepmind', False, False, '2024'),
    ('Sakana AI',          'deepmind', False, False, '2023'),
    ('Reka AI',            'deepmind', False, False, '2022'),
    ('Reflection AI',      'deepmind', False, False, '2024'),
    ('Essential AI',       'deepmind', False, False, '2023'),

    # 孤立 (无血缘关系)
    ('LangChain',          'isolated', False, False, '2022'),
    ('Midjourney',         'isolated', False, False, '2021'),
    ('DeepSeek',           'isolated', False, False, '2023'),
    ('Stability AI',       'isolated', False, False, '2019'),
    ('Replicate',          'isolated', False, False, '2019'),
]

ACQUIHIRE_TARGETS = {
    'Adept':        {'target': 'Amazon',    'date': '2024.06'},
    'Covariant':    {'target': 'Amazon',    'date': '2024.08'},
    'Inflection':   {'target': 'Microsoft', 'date': '2024.03'},
    'Character.AI': {'target': 'Google',    'date': '2024.08'},
}

# ============ 边定义 ============
# (src, dst, type) where type in {'spinoff', 'investment', 'talent'}
edges_spec = [
    # PayPal Mafia → OpenAI / xAI (早期资本 + Musk 创立 xAI)
    ('PayPal Mafia', 'OpenAI', 'investment'),
    ('PayPal Mafia', 'xAI',    'spinoff'),

    # OpenAI 血缘裂变
    ('OpenAI', 'Anthropic',           'spinoff'),
    ('OpenAI', 'xAI',                 'spinoff'),
    ('OpenAI', 'SSI',                 'spinoff'),
    ('OpenAI', 'Thinking\nMachines',  'spinoff'),
    ('OpenAI', 'Perplexity',          'spinoff'),
    ('OpenAI', 'Eureka Labs',         'spinoff'),
    ('OpenAI', 'Adept',               'spinoff'),
    ('OpenAI', 'Covariant',           'spinoff'),
    ('OpenAI', 'Dust',                'spinoff'),
    ('OpenAI', 'Softmax',             'spinoff'),
    ('OpenAI', 'Cursor',              'investment'),

    # DeepMind / Brain 血缘裂变
    ('DeepMind',     'Inflection',     'spinoff'),
    ('DeepMind',     'Mistral',        'spinoff'),
    ('DeepMind',     'Reflection AI',  'spinoff'),
    ('Google Brain', 'Character.AI',   'spinoff'),
    ('Google Brain', 'Cohere',         'spinoff'),
    ('Google Brain', 'Mistral',        'spinoff'),
    ('Google Brain', 'World Labs',     'spinoff'),
    ('Google Brain', 'Sakana AI',      'spinoff'),
    ('Google Brain', 'Reka AI',        'spinoff'),
    ('Google Brain', 'Essential AI',   'spinoff'),

    # 跨圈人才流动
    ('DeepMind',     'OpenAI',     'talent'),  # Sutskever 从 Google 被挖
    ('Google Brain', 'OpenAI',     'talent'),  # Karpathy 等
    ('DeepMind',     'Anthropic',  'talent'),
]

# ============ 视觉常量 ============
PALETTE = {
    'openai':   {'fill': '#3B82F6', 'hub': '#1E40AF', 'name': 'OpenAI 系'},
    'deepmind': {'fill': '#E11D48', 'hub': '#9F1239', 'name': 'DeepMind / Google Brain 系'},
    'paypal':   {'fill': '#7C3AED', 'hub': '#5B21B6', 'name': 'PayPal Mafia (上游资本)'},
    'isolated': {'fill': '#94A3B8', 'hub': '#475569', 'name': '孤立公司 (无血缘)'},
}
EDGE_STYLES = {
    'spinoff':    {'color': '#334155', 'linestyle': '-',  'alpha': 0.38, 'width': 1.25,
                   'label': '创始团队出走'},
    'investment': {'color': '#0EA5E9', 'linestyle': ':',  'alpha': 0.72, 'width': 1.6,
                   'label': '投资关系'},
    'talent':     {'color': '#F59E0B', 'linestyle': '--', 'alpha': 0.62, 'width': 1.35,
                   'label': '关键人才流动'},
}
ACQUIHIRE_COLOR = '#FBBF24'   # 金色光环
BG_COLOR = '#FAFAF7'          # 米白底
TEXT_DARK = '#0F172A'
TEXT_MUTED = '#64748B'
GROUP_STROKE = '#CBD5E1'

# ============ 构图 ============
G = nx.Graph()
node_meta = {}
for name, cluster, is_hub, is_acq, year in nodes_spec:
    G.add_node(name)
    node_meta[name] = {'cluster': cluster, 'hub': is_hub, 'acq': is_acq, 'year': year}

for src, dst, etype in edges_spec:
    # 用权重让卫星更紧地贴向 hub
    w = {'spinoff': 3.0, 'investment': 1.5, 'talent': 0.4}[etype]
    G.add_edge(src, dst, etype=etype, weight=w)

# ============ 布局 (手工锚定) ============
# 30 个节点规模小，手工排版比 force-directed 干净得多
pos = {
    # 上游
    'PayPal Mafia':        (-4.25, -1.2),

    # OpenAI 中心
    'OpenAI':              (-2.2,  0.2),

    # OpenAI 卫星 (扇形围绕 OpenAI, 顺时针从 NE 起)
    'Anthropic':           (-0.5,  0.9),   # NE, 桥到 DeepMind (talent)
    'Eureka Labs':         (-1.4,  1.3),   # N
    'Perplexity':          (-2.5,  1.4),   # NNW
    'Dust':                (-3.55, 0.72),  # NW
    'Thinking\nMachines':  (-4.2,  0.2),   # W
    'SSI':                 (-3.8, -0.7),   # WSW
    'xAI':                 (-3.3, -1.5),   # SW (also from PayPal Mafia)
    'Cursor':              (-2.0, -1.7),   # S (investment)
    'Softmax':             (-1.35, -1.15), # SSE
    'Adept':               (-0.25, -0.45), # E
    'Covariant':           (-0.15, -1.55), # SE

    # DeepMind / Brain 中心
    'DeepMind':            ( 2.25, 0.72),
    'Google Brain':        ( 3.35, -0.55),
    'Mistral':             ( 2.55, 0.05),  # 桥接 DM + Brain

    # DeepMind 卫星
    'Inflection':          ( 1.05, 0.72),  # NW
    'Reflection AI':       ( 2.55, 1.35),  # N

    # Google Brain 卫星
    'Character.AI':        ( 1.55, -0.52), # W
    'Cohere':              ( 4.45,  0.35), # NE
    'World Labs':          ( 4.72, -0.55), # E
    'Reka AI':             ( 4.45, -1.45), # SE
    'Sakana AI':           ( 3.25, -1.62), # S
    'Essential AI':        ( 2.0, -1.45),  # SW
}

label_offsets = {
    'PayPal Mafia':        (0.0, -0.53),
    'Thinking\nMachines':  (-0.10, 0.36),
    'Dust':                (-0.28, 0.26),
    'Perplexity':          (0.00, 0.36),
    'Eureka Labs':         (0.00, 0.36),
    'Anthropic':           (0.10, 0.36),
    'Adept':               (0.28, 0.22),
    'Covariant':           (0.33, 0.15),
    'Softmax':             (0.10, 0.36),
    'Cursor':              (0.00, -0.40),
    'xAI':                 (0.00, -0.38),
    'SSI':                 (0.00, -0.38),
    'Inflection':          (-0.48, 0.24),
    'Reflection AI':       (0.12, 0.34),
    'Mistral':             (-0.22, -0.35),
    'Character.AI':        (-0.45, 0.10),
    'Cohere':              (0.35, 0.10),
    'World Labs':          (0.35, -0.03),
    'Reka AI':             (0.35, -0.20),
    'Sakana AI':           (0.00, -0.38),
    'Essential AI':        (-0.22, -0.34),
}

display_names = {
    'PayPal Mafia': 'PayPal\nMafia',
    'Google Brain': 'Google\nBrain',
}

# 孤立公司排底部一行
isolated_names = sorted(
    [n for n, m in node_meta.items() if m['cluster'] == 'isolated'],
    key=lambda n: (node_meta[n]['year'], n),
)
iso_y = -2.9
iso_xs = np.linspace(-3.8, 3.8, len(isolated_names))
for x, name in zip(iso_xs, isolated_names):
    pos[name] = (x, iso_y)

# ============ 绘图 ============
fig, ax = plt.subplots(figsize=(20, 9.2), facecolor=BG_COLOR)
ax.set_facecolor(BG_COLOR)

# 大分区背景: 先建立读者的空间记忆, 再让连线进入细节
family_panels = [
    {
        'rect': (-4.75, -1.95, 4.95, 3.70),
        'color': '#DBEAFE',
        'title': 'OpenAI 系裂变',
        'subtitle': '研究员、创始人与基金向外扩散',
        'label_xy': (-4.55, 1.52),
        'subtitle_dy': 0.32,
    },
    {
        'rect': (0.55, -1.95, 4.25, 3.70),
        'color': '#FFE4E6',
        'title': 'DeepMind / Google Brain\n系裂变',
        'subtitle': '',
        'label_xy': (0.80, 1.70),
        'subtitle_dy': 0.70,
    },
]
for panel_spec in family_panels:
    x, y, w, h = panel_spec['rect']
    panel = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.10,rounding_size=0.22",
        linewidth=1.2, edgecolor=GROUP_STROKE,
        facecolor=panel_spec['color'], alpha=0.24, zorder=-3,
    )
    ax.add_patch(panel)
    lx, ly = panel_spec['label_xy']
    ax.text(lx, ly, panel_spec['title'],
            ha='left', va='top', fontproperties=_font(12.5, bold=True),
            color=TEXT_DARK, linespacing=1.08, zorder=-2)
    if panel_spec['subtitle']:
        subtitle_dy = panel_spec.get('subtitle_dy', 0.36)
        ax.text(lx, ly - subtitle_dy, panel_spec['subtitle'],
                ha='left', va='top', fontproperties=_font(8.7),
                color=TEXT_MUTED, linespacing=1.08, zorder=-2)

# 右侧单独放"大厂回收层", 避免 reverse acquihire 只变成一个星号
acquirer_panel = FancyBboxPatch(
    (5.05, -1.75), 1.45, 3.35,
    boxstyle="round,pad=0.08,rounding_size=0.18",
    linewidth=1.2, edgecolor='#FCD34D',
    facecolor='#FFFBEB', alpha=0.82, zorder=-2,
)
ax.add_patch(acquirer_panel)
ax.text(5.18, 1.35, '大厂回收层', ha='left', va='top',
        fontproperties=_font(12, bold=True), color='#92400E', zorder=4)
ax.text(5.18, 1.08, '人才 + 技术授权', ha='left', va='top',
        fontproperties=_font(9), color='#B45309', zorder=4)

acquirer_pos = {
    'Microsoft': (5.75,  0.55),
    'Google':    (5.75, -0.25),
    'Amazon':    (5.75, -1.05),
}
for target, (x, y) in acquirer_pos.items():
    box = FancyBboxPatch(
        (x - 0.48, y - 0.18), 0.96, 0.36,
        boxstyle="round,pad=0.05,rounding_size=0.12",
        linewidth=1.0, edgecolor='#F59E0B',
        facecolor='white', alpha=0.96, zorder=3,
    )
    ax.add_patch(box)
    ax.text(x, y, target, ha='center', va='center',
            fontproperties=_font(10, bold=True), color='#78350F', zorder=4)

# 给"孤立公司"加一个浅底色色块，视觉上分组
iso_bg = FancyBboxPatch(
    (-4.6, iso_y - 0.55), 9.2, 1.0,
    boxstyle="round,pad=0.05,rounding_size=0.15",
    linewidth=0, facecolor='#F1F5F9', alpha=0.7, zorder=0,
)
ax.add_patch(iso_bg)
ax.text(-4.55, iso_y + 0.65, '孤立公司 · 无 OpenAI / DeepMind 血缘',
        ha='left', va='bottom', fontproperties=_font(10),
        color='#64748B', zorder=1)

# 边: 按类型分批画
for etype, style in EDGE_STYLES.items():
    edge_list = [(u, v) for u, v, d in G.edges(data=True) if d['etype'] == etype]
    if not edge_list:
        continue
    nx.draw_networkx_edges(
        G, pos, edgelist=edge_list,
        edge_color=style['color'], style=style['linestyle'],
        alpha=style['alpha'], width=style['width'], ax=ax,
    )

# reverse acquihire: 保留到大厂层的线, 但弱化视觉权重
for src, meta in ACQUIHIRE_TARGETS.items():
    sx, sy = pos[src]
    tx, ty = acquirer_pos[meta['target']]
    arrow = FancyArrowPatch(
        (sx + 0.28, sy), (tx - 0.52, ty),
        arrowstyle='-|>', mutation_scale=11,
        linewidth=1.05, linestyle='-',
        color='#D97706', alpha=0.34,
        connectionstyle="arc3,rad=0.12",
        zorder=1,
    )
    ax.add_patch(arrow)

# 节点大小
degrees = dict(G.degree())
def node_size(name):
    if name == 'PayPal Mafia':
        return 3600
    if name == 'Anthropic':
        return 2600
    if node_meta[name]['hub']:
        return 4800
    return max(1100, degrees[name] * 750)

# 第 1 层: acquihire 金色光环 (画在节点底下)
acq_nodes = [n for n, m in node_meta.items() if m['acq']]
if acq_nodes:
    nx.draw_networkx_nodes(
        G, pos, nodelist=acq_nodes,
        node_size=[node_size(n) * 1.85 for n in acq_nodes],
        node_color=ACQUIHIRE_COLOR, alpha=0.40,
        edgecolors='none', ax=ax,
    )

# 第 2 层: 主体节点 (先画 isolated, 再 paypal, 再两个主圈)
for cluster in ('isolated', 'paypal', 'deepmind', 'openai'):
    nlist = [n for n in G.nodes() if node_meta[n]['cluster'] == cluster]
    if not nlist:
        continue
    colors = [PALETTE[cluster]['hub'] if node_meta[n]['hub'] else PALETTE[cluster]['fill']
              for n in nlist]
    sizes = [node_size(n) for n in nlist]
    nx.draw_networkx_nodes(
        G, pos, nodelist=nlist,
        node_color=colors, node_size=sizes,
        alpha=0.93, edgecolors='white', linewidths=2.8, ax=ax,
    )

# 第 3 层: 文字标签。小节点标签放在圆外, 避免文字被圆和线切开。
for name, (x, y) in pos.items():
    is_hub = node_meta[name]['hub']
    is_acq = node_meta[name]['acq']
    display = display_names.get(name, name)
    if is_hub:
        ax.text(
            x, y, display,
            ha='center', va='center',
            color='white',
            fontproperties=cn_hub,
            linespacing=0.92,
            zorder=10,
        )
    else:
        dx, dy = label_offsets.get(name, (0.0, 0.34))
        lx, ly = x + dx, y + dy
        ax.text(
            lx, ly, f"{display}\n{node_meta[name]['year']}",
            ha='center', va='center',
            color=TEXT_DARK,
            fontproperties=_font(8.9),
            linespacing=1.05,
            bbox=dict(boxstyle='round,pad=0.12', facecolor='white',
                      edgecolor='none', alpha=0.88),
            zorder=10,
        )

# ============ 图例 ============
event_handles = [
    Line2D([0], [0], marker='o', color='w',
           markerfacecolor=ACQUIHIRE_COLOR, alpha=0.55,
           markeredgecolor='none', markersize=18,
           label='☆ 2024 被大厂 reverse acquihire')
]
event_handles.append(
    Line2D([0], [0], color='#D97706', linestyle='-',
           linewidth=2.0, alpha=0.45, marker='>', markerfacecolor='#D97706',
           markeredgecolor='#D97706', label='大厂回收 / 授权')
)
edge_handles = [
    Line2D([0], [0], color=s['color'], linestyle=s['linestyle'],
           linewidth=2.4, label=s['label'])
    for s in EDGE_STYLES.values()
]

# ============ 标题 / 副标题 / 页脚 ============
fig.text(0.5, 0.965, 'AI 创业公司关系网络 · OpenAI 与 DeepMind 系族谱',
         ha='center', va='top', fontproperties=cn_title, color=TEXT_DARK)
fig.text(0.5, 0.928,
         '节点下方为创立年份 · 颜色 = 人才来源圈层 · 右侧 = 2024 reverse acquihire 去向',
         ha='center', va='top', fontproperties=cn_sub, color='#475569')
fig_leg = fig.legend(
    handles=edge_handles + event_handles, loc='upper center',
    bbox_to_anchor=(0.5, 0.892), ncol=5,
    frameon=True, facecolor='white', edgecolor='#E2E8F0',
    prop=cn_legend, labelspacing=0.8, borderpad=0.65,
    handletextpad=0.9, columnspacing=1.6,
)
fig_leg.get_frame().set_linewidth(1.0)
fig.text(0.99, 0.012,
         f'节点 {G.number_of_nodes()} · 边 {G.number_of_edges()} · 数据截至 2026.05',
         ha='right', va='bottom', fontproperties=cn_foot, color='#94A3B8')

ax.set_xlim(-5.0, 6.65)
ax.set_ylim(-3.55, 2.15)
ax.set_aspect('equal')
ax.axis('off')

# ============ 输出 ============
out_dir = Path(__file__).resolve().parent.parent / 'diagram' / 'ai-network'
out_dir.mkdir(parents=True, exist_ok=True)
out_png = out_dir / 'ai_network_graph.png'
plt.tight_layout(rect=[0, 0.01, 1, 0.88])
plt.savefig(out_png, dpi=180, bbox_inches='tight', facecolor=BG_COLOR)
print(f'Done → {out_png}')
print(f'Nodes: {G.number_of_nodes()}  Edges: {G.number_of_edges()}')
print('Top by degree:', sorted(degrees.items(), key=lambda x: -x[1])[:5])
