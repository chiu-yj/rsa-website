# -*- coding: utf-8 -*-
"""Build the RSA website (English at /, Traditional Chinese at /zh/) into plain static HTML.

    python3 tools/build.py

Content lives in tools/content.py (projects, UI strings) and in the page functions below.
Generated .html files are committed; GitHub Pages serves them as-is (no build on the server).
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import SITE, UI, PROJECTS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
e = html.escape
LANGS = ('en', 'zh')


def pre(lang):
    """Relative prefix from a page to the site root."""
    return '' if lang == 'en' else '../'


def out_path(lang, fname):
    return os.path.join(ROOT, fname) if lang == 'en' else os.path.join(ROOT, 'zh', fname)


def url(lang, fname):
    base = SITE['domain'] + '/' + ('' if lang == 'en' else 'zh/')
    return base + ('' if fname == 'index.html' else fname)


def write(lang, fname, doc):
    p = out_path(lang, fname)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(doc)


# ------------------------------------------------------------------ chrome
def head(lang, fname, title, desc, img='assets/img/work/960/vision-exterior.webp'):
    P = pre(lang)
    hl = 'en' if lang == 'en' else 'zh-Hant'
    fonts = 'family=Archivo:wdth,wght@62..125,300..900&amp;family=IBM+Plex+Mono:wght@400;500'
    if lang == 'zh':
        fonts += '&amp;family=Noto+Sans+TC:wght@400;500;700;900'
    return f'''<!doctype html>
<html lang="{hl}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url(lang, fname)}">
<link rel="alternate" hreflang="en" href="{url('en', fname)}">
<link rel="alternate" hreflang="zh-Hant" href="{url('zh', fname)}">
<link rel="alternate" hreflang="x-default" href="{url('en', fname)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="RSA · Responsive Space Architecture">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(lang, fname)}">
<meta property="og:image" content="{SITE['domain']}/assets/img/og/{os.path.splitext(os.path.basename(img))[0]}.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'zh_TW'}">
<meta name="theme-color" content="#111110">
<link rel="icon" href="{P}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{P}favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{P}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">{UI[lang]['skip']}</a>
'''


def header(lang, fname, active=None):
    u = UI[lang]
    other = 'zh/' + fname if lang == 'en' else '../' + fname
    links = '\n'.join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in u['nav'])
    return f'''
<div class="statusbar">
  <div class="wrap mono mono--sm">
    <span><span class="dot" aria-hidden="true"></span>{u['status_l']}</span>
    <span class="muted">{u['status_r']}</span>
  </div>
</div>

<header class="masthead">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{u['brand_aria']}">
      <span class="brand__mark">RSA<i>.</i></span>
      <span class="brand__name">{u['brand_sub']}</span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" data-open="{u['menu']}" data-close="{u['close']}"><span class="menu-btn__label">{u['menu']}</span></button>
    <nav id="site-nav" class="nav" aria-label="Main">
{links}
      <a class="nav__lang" href="{other}" lang="{u['lang_switch_lang']}" hreflang="{u['lang_switch_lang']}">{u['lang_switch']}</a>
    </nav>
  </div>
</header>
'''


def footer(lang, fname):
    u = UI[lang]
    P = pre(lang)
    cols = ''.join(
        f'<div class="footer__col"><span class="mono mono--sm muted">{t}</span>' + ''.join(f'<a href="{h}">{n}</a>' for h, n in items) + '</div>'
        for t, items in u['foot_cols'])
    en_href = 'index.html' if lang == 'en' else '../' + fname
    zh_href = 'zh/' + fname if lang == 'en' else fname
    return f'''
<footer class="footer dark">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__lead">
        <p class="h-card">{u['foot_lead']}</p>
        <p class="muted" style="max-width:34em">{u['foot_sub']}</p>
        <p class="mono mono--sm"><a class="link" href="mailto:{SITE['email']}">{SITE['email']}</a></p>
      </div>
      {cols}
      <div class="footer__col"><span class="mono mono--sm muted">{u['foot_lang']}</span><a href="{en_href}" lang="en">English</a><a href="{zh_href}" lang="zh-Hant">繁體中文</a></div>
    </div>
    <div class="footer__mark" aria-hidden="true">RSA<i>.</i></div>
    <div class="footer__brandline">
      <p><strong>RSA. · Responsive Space Architecture</strong><br><span lang="zh-Hant">見築科技有限公司</span></p>
    </div>
    <div class="footer__legal">
      <p>{u['legal']}</p>
      <p class="mono mono--sm">© 2026 RSA · Taiwan</p>
    </div>
  </div>
</footer>

<script src="{P}assets/js/site.js" defer></script>
</body>
</html>
'''


def page(lang, fname, title, desc, body, active=None, img=None):
    kw = {'img': img} if img else {}
    return head(lang, fname, title, desc, **kw) + header(lang, fname, active) + body + footer(lang, fname)


def sheet_head(no, label, aside=''):
    a = f'<span class="sheet-head__aside">{aside}</span>' if aside else ''
    return f'<div class="sheet-head"><span class="sheet-head__no">{no}</span><span class="sheet-head__label">{label}</span>{a}</div>'


STAMP = {
    'en': {'real': 'Real', 'explore': 'Exploratory', 'record': 'Record', 'planned': 'Planned', 'concept': 'Concept', 'built': 'Built', 'validating': 'In validation', 'next': 'Next'},
    'zh': {'real': '真實', 'explore': '探索中', 'record': '紀錄', 'planned': '規劃中', 'concept': '概念', 'built': '已完成', 'validating': '驗證中', 'next': '下一階段'},
}


def stamp(kind, text):
    return f'<span class="stamp stamp--{kind}">{text}</span>'


# ------------------------------------------------------------------ HOME
H = {
 'en': dict(
   title='RSA — Responsive Space Architecture',
   desc='RSA (見築科技) is an architecture and environmental-technology brand from Taiwan: design-led spatial thinking, evidence-driven site analysis, and Residential Site Analyzer, its own research platform.',
   eyebrow='RSA / Responsive Space Architecture', sheet='Sheet A-000 / Cover',
   h1='<span class="ln">Understand the <span class="g">environment</span><span class="o">.</span></span><span class="ln ln--2">Shape the future<span class="o">.</span></span>',
   alt_tag='<p class="zh muted" lang="zh-Hant">先見環境，再築未來。</p>',
   sub='Design-led spatial thinking. Evidence-driven environmental research. Technology that connects them.',
   cta1='Explore our work', cta2='Discover the technology',
   fig1='Fig. 01 — Design', fig1c='Vision Art Gallery · founder’s academic design · visualisation',
   fig2='Fig. 02 — The platform', fig2s='Residential Site Analyzer · product mark', logo_alt='Residential Site Analyzer logo: an isometric building massing on a site plane under an orange sun path, beside the letters RSA and the name 住宅基地環境分析 Residential Site Analyzer',
   legend_t='Legend — how to read this site',
   legend=[('real', 'Real', 'Exists today · real prototype screenshot'), ('explore', 'Exploratory', 'Preview, not validated'),
           ('record', 'Record', 'Historical, version-specific'), ('planned', 'Planned', 'Future direction, not built'),
           ('concept', 'Concept', 'Illustration only'), ('work', 'Founder', 'Founder’s work, credited by role')],
   s1=('01', 'What RSA stands for', 'Brand / product'),
   letters=[('R', 'Responsive', 'Respond to climate, surroundings and the people who will live there.'),
            ('S', 'Space', 'Sites, homes, public space and everyday life.'),
            ('A', 'Architecture', 'Design and analysis as one continuous way of working.')],
   intro='RSA starts from architectural and spatial design, then adds site analysis, digital simulation and its own software research. We look at how space answers to sun, wind, heat and people—and try to turn complex environmental information into evidence that can be understood and traced.',
   naming='<strong>RSA</strong> is the company brand. <strong>Residential Site Analyzer</strong> is the research platform it develops.',
   s2=('02', 'Environment first', 'Why RSA exists'),
   why='A site’s sun, its neighbours, its heat and its habits shape a space <span class="g">before any rendering does.</span>',
   why_body=['Good architecture should start from understanding where it stands. RSA grew out of the founder’s spatial-design training and residential development work, where environmental questions came up early and were hard to answer.',
             'Can a site be understood more clearly before design begins? How do floors, hours and massing options differ? Can the results be explained to people without an engineering background—and do they actually improve the design?'],
   chain=['Observe', 'Analyze', 'Design', 'Evaluate', 'Refine'], chain_on=2,
   s3=('03', 'Expertise', 'Three disciplines, one loop'),
   d_k='RSA Design', d_h='Designing buildings, and rethinking how life happens in them.',
   d_b='Spatial concepts, site layout and massing, early residential planning, façade and material strategy, and design visualisation—grounded in the founder’s academic work and residential practice.',
   d_list=['Spatial & architectural concepts', 'Site layout & massing', 'Early residential planning', 'Façade & material strategy', 'Design visualisation'],
   d_note='Founder’s experience. RSA does not offer statutory architect services.',
   d_fig='Corner Library · founder’s academic design · visualisation',
   e_k='RSA Environment', e_h='Making invisible site conditions into design evidence you can <span style="color:var(--orange)">read.</span>',
   e_note_t='▲ Note on the work above', e_note='The founder’s projects predate RSA and were not analysed with it. What follows is Residential Site Analyzer, a separately developed research prototype.',
   e_intro='What the prototype explores today. Each module is marked by how far along it really is.',
   tabs=[('solar', 'Solar &amp; shading'), ('site', 'Site'), ('massing', 'Massing A/B'), ('wind', 'Wind'), ('utci', 'Thermal comfort')],
   panels={'solar': ('solar-shading.webp', 'RSA prototype: time-based 3D solar and shading view of a target building among neighbouring blocks', 'Sun position and neighbouring obstruction, by floor and time', 'real'),
           'site': ('site-workspace.webp', 'RSA prototype: map-based site workspace with a parcel outline and setup panels', 'Site boundary, surroundings and analysis conditions', 'real'),
           'massing': ('massing.webp', 'RSA prototype: massing editor on a map, with Scheme A outlined in red among neighbouring buildings', 'Scheme A massing editor — A/B schemes share one site model', 'real'),
           'wind': ('wind.webp', 'RSA prototype: 3D wind-direction view with streamlines passing a cluster of building masses', 'Background wind and massing — relative ventilation potential, not CFD', 'explore'),
           'utci': ('utci.webp', 'RSA prototype: UTCI-oriented outdoor thermal comfort view with building massing', 'Outdoor heat stress by time and position (UTCI)', 'explore')},
   shot_real='Real screenshot · dev build', shot_explore='Real screenshot · exploratory',
   modules=[('Site context', 'real', 'Map-based parcel and surroundings'), ('Building massing', 'real', 'Target building, neighbours, A/B schemes'),
            ('Solar &amp; shading', 'real', 'Time- and floor-aware shadow study'), ('Wind', 'explore', 'Directional preview — not CFD'),
            ('UTCI comfort', 'explore', 'Research view; inputs and limits disclosed')],
   e_link='Inside the platform',
   t_k='RSA Technology', t_h='Tools that explain the environment, built from design questions.',
   t_items=[('Residential Site Analyzer', 'real', 'Exists · in development', 'Python / Streamlit research prototype for site, massing, sun and shade, wind preview and UTCI-oriented comfort.'),
            ('RSA Studio', 'concept', 'Concept', 'A/B design, cross-floor and time comparison, decision visualisation and report summaries.'),
            ('RSA Intelligence', 'planned', 'Planned · not deployed', 'Sourced explanations of results through large language models such as the Claude API, with human review.')],
   t_ai='AI may only organise and explain analysis evidence that has a source. It never invents results and never replaces physical simulation.',
   s4=('04', 'Founder’s selected work', '2020 — 2025'),
   w_h='The work comes first.',
   w_b='Academic design and residential projects are where the questions came from. Each one is credited to its real author and role. <strong style="color:var(--ink)">None were RSA commissions or analysed with RSA.</strong>',
   w_note='Light, enclosure and scale change how a place is lived in. That is the question RSA tries to make measurable.',
   w_all='All five projects',
   s5=('05', 'Method', 'Observe → Refine'),
   m_h='Five steps.<br>One loop.', m_b='How RSA intends design and analysis to feed each other. It describes the method going forward—it is not a claim about how the earlier projects were designed.',
   loop=[('Observe', 'Site, neighbours, climate, people and use.'), ('Analyze', 'Suitable models and data, with assumptions stated.'),
         ('Design', 'Bring conditions into layout, massing, space and materials.'), ('Evaluate', 'Compare options with indicators that fit the question.'),
         ('Refine', 'Keep limits and uncertainty visible; keep improving.')],
   s6=('06', 'Research &amp; integrity', 'Research brief · 2026 Q4 — 2027 Q4'),
   r_h='The question is not whether it can compute.<br><span style="color:var(--orange-ink)">It is whether the result can be used.</span>',
   r_b='The current study focuses on early decisions for new housing, with Kaohsiung as the case city. RSA does not replace Radiance, CFD or EnergyPlus; it studies how their kind of evidence can be read and used earlier.',
   rq_head=['No.', 'Research question', 'Validation layer', 'How it is tested'],
   rq=[('Can environmental differences between floors, times and schemes be identified reliably?', 'Technical', '技術驗證', 'Cross-check shading and calculation error against reference tools.'),
       ('Are the integrated results understood more easily than scattered information?', 'Real cases', '真實案例驗證', 'Check real Kaohsiung sites and surrounding heights; compare A/B schemes under controlled conditions.'),
       ('Does that understanding support better early-stage decisions?', 'Users', '使用者驗證', 'Same data, same task, only the presentation changes: compare accuracy, time and quality of reasoning.')],
   board=[('built', 'Prototype &amp; core workflow', ['Site location, boundary &amp; surrounding massing', 'Sun, shade, wind direction &amp; UTCI views', 'Floor &amp; time comparison, A/B schemes', 'Report &amp; evidence output']),
          ('validating', 'Reliability &amp; real cases', ['Sun / shade reference comparison', 'Real Kaohsiung site case', 'Consistency across views, data &amp; reports']),
          ('next', 'User research', ['Authoritative site-data integration (assessment)', 'Case-data completeness', '10–15 person user pilot', 'Formal comprehension &amp; decision study'])],
   board_note='Built features still require continued verification. Status compiled from project version records.',
   rec_t=('06.1', 'Archived records', 'r42 / r44 · not current certification'),
   rec=[('r42', '0.9795', '', 'Shadow IoU vs. Radiance', 'Intersection-over-union against a Radiance direct-shadow reference on archived cases. Version-specific.'),
        ('r42', '0.25', 'm', 'Hausdorff distance', 'Boundary difference in one recorded comparison setup; archived data also notes an area bias of about −2.05%. Version-specific.'),
        ('r44', '321', '', 'Regression tests passed', 'Historically marked PASS. Not proof that newer builds or all modules meet a scientific acceptance threshold.')],
   historical='Historical', r_link='Methods, limits &amp; provenance',
   s7=('07', 'Contact'),
   c_h='Questions about a site, environmental evidence or research collaboration are welcome.',
   c_ctas=[('mailto:' + SITE['email'], 'Discuss a project', 'primary'), ('work.html', 'Explore our work', 'ghost'), ('platform.html', 'Discover the technology', 'ghost')],
 ),
 'zh': dict(
   title='RSA 見築科技 — 先見環境，再築未來',
   desc='RSA 見築科技：結合建築與空間設計、基地環境分析與自主軟體研發的建築環境科技品牌；Residential Site Analyzer 為旗下研發中的住宅基地環境分析平台。',
   eyebrow='RSA / Responsive Space Architecture', sheet='圖號 A-000 / 封面',
   h1='<span class="ln">先見<span class="g">環境</span>，</span><span class="ln ln--2">再築未來<span class="o">。</span></span>',
   alt_tag='<p class="muted" lang="en">Understand the environment. Shape the future.</p>',
   sub='以建築設計理解場域，以環境分析建立證據，以自主科技探索更好的空間。',
   cta1='探索作品', cta2='了解 RSA 技術',
   fig1='圖 01 — 設計', fig1c='視界美術館 · 創辦人學術設計 · 設計模擬圖',
   fig2='圖 02 — 技術平台', fig2s='住宅基地環境分析 · 產品標誌', logo_alt='Residential Site Analyzer 標誌：基地平面上的等角量體與橘色太陽軌跡，旁為 RSA 字樣與「住宅基地環境分析 Residential Site Analyzer」',
   legend_t='圖例 — 如何閱讀本站',
   legend=[('real', '真實', '現有原型 · 真實系統截圖'), ('explore', '探索中', '預覽性質，未經驗證'),
           ('record', '紀錄', '歷史版本紀錄'), ('planned', '規劃中', '未來方向，尚未建置'),
           ('concept', '概念', '示意，非實際產品'), ('work', '創辦人', '創辦人作品，依實際角色標示')],
   s1=('01', 'RSA 是什麼', '品牌 / 產品'),
   letters=[('R', 'Responsive · 回應', '因地制宜，理解氣候、建築周邊環境與使用者需求。'),
            ('S', 'Space · 空間', '涵蓋基地、住宅、公共空間、生活體驗與人本設計。'),
            ('A', 'Architecture · 建築', '讓專業設計與科學分析，形成連續的工作方法。')],
   intro='RSA 以建築與空間設計思維為出發點，結合基地環境分析、數位模擬與自主軟體研發。我們關注空間如何回應日照、風、熱環境與人的需求，並嘗試把複雜的環境資訊，轉化為可理解、可追溯的設計證據。',
   naming='<strong>RSA</strong> 是公司品牌；<strong>Residential Site Analyzer</strong> 是我們研發中的住宅基地環境分析平台。',
   s2=('02', '環境優先', '為什麼有 RSA'),
   why='一塊基地的日照、鄰棟、熱環境與人的習慣，<span class="g">往往比一張透視圖更早決定空間的品質。</span>',
   why_body=['好的建築不應只從形式開始，而應從理解它所處的環境開始。RSA 承接創辦人的空間設計訓練與住宅開發經歷，把設計過程中常見、卻難以回答的環境問題，轉化為研究與技術開發的方向。',
             '設計前期能否更清楚地理解基地？不同樓層、時間與量體的差異如何呈現？分析結果能否以非工程背景也能理解的方式傳達，並實際改善設計選擇？'],
   chain=['觀察', '分析', '設計', '檢視', '改善'], chain_on=2,
   s3=('03', '專業領域', '三個主軸，一個循環'),
   d_k='RSA Design · 設計研究', d_h='不只設計建築，也重新思考空間與生活。',
   d_b='建築與空間概念、基地配置與量體、住宅前期規劃、立面與材料策略、3D 設計視覺化——以創辦人的學術作品與住宅實務為基礎。',
   d_list=['建築與空間概念', '基地配置與量體', '住宅前期規劃', '立面與材料策略', '設計視覺化'],
   d_note='創辦人經歷。RSA 不提供依法須由建築師執行之簽證業務。',
   d_fig='角落圖書館 · 創辦人學術設計 · 設計模擬圖',
   e_k='RSA Environment · 環境分析', e_h='讓看不見的環境條件，成為<span style="color:var(--orange)">看得懂</span>的設計依據。',
   e_note_t='▲ 關於上方作品', e_note='創辦人的作品早於 RSA，並未使用 RSA 分析。以下是另行研發的研究原型 Residential Site Analyzer。',
   e_intro='原型目前探索的內容。每個模組都依實際進度標示狀態。',
   tabs=[('solar', '日照／遮蔭'), ('site', '基地'), ('massing', '量體 A/B'), ('wind', '風向'), ('utci', '熱舒適')],
   panels={'solar': ('solar-shading.webp', 'RSA 原型：目標建物與鄰棟的 3D 日照遮蔭畫面', '太陽位置與鄰棟遮蔽，依樓層與時間呈現', 'real'),
           'site': ('site-workspace.webp', 'RSA 原型：地圖上的基地定位與設定面板', '基地範圍、周邊環境與分析條件', 'real'),
           'massing': ('massing.webp', 'RSA 原型：地圖上的量體編輯，方案 A 以紅框標示', '方案 A 量體編輯 — A/B 方案共用同一基地模型', 'real'),
           'wind': ('wind.webp', 'RSA 原型：流線通過建築群的 3D 風向畫面', '背景風與量體關係 — 相對通風潛勢，非 CFD', 'explore'),
           'utci': ('utci.webp', 'RSA 原型：UTCI 戶外熱環境研究畫面', '依時間與位置呈現的戶外熱壓力（UTCI）', 'explore')},
   shot_real='真實截圖 · 開發版本', shot_explore='真實截圖 · 探索性質',
   modules=[('基地脈絡', 'real', '地圖上的基地與周邊'), ('建築量體', 'real', '目標建物、鄰棟與 A/B 方案'),
            ('日照／遮蔭', 'real', '依時間與樓層的陰影研究'), ('風環境', 'explore', '風向預覽 — 非 CFD'),
            ('UTCI 熱舒適', 'explore', '研究性視覺化，揭露輸入與限制')],
   e_link='深入技術平台',
   t_k='RSA Technology · 軟體與 AI', t_h='從設計問題出發，打造能解釋環境的工具。',
   t_items=[('Residential Site Analyzer', 'real', '現有 · 開發中', 'Python／Streamlit 研究原型：基地、量體、日照遮蔭、風向預覽與 UTCI 導向熱舒適。'),
            ('RSA Studio', 'concept', '概念', 'A/B 設計、跨樓層與時序比較、決策視覺化與報告摘要。'),
            ('RSA Intelligence', 'planned', '規劃中 · 尚未部署', '以 Claude API 等大型語言模型，提供有來源依據的結果解讀，並由人工審查。')],
   t_ai='AI 只能整理與解釋有來源的分析證據；不憑空產生結果，也不取代物理模擬。',
   s4=('04', '創辦人精選作品', '2020 — 2025'),
   w_h='先有作品，才有問題。',
   w_b='學術設計與住宅專案，是這些問題的來源。每件作品都依實際作者與角色標示。<strong style="color:var(--ink)">均非 RSA 承攬案，也未使用 RSA 分析。</strong>',
   w_note='光線、包覆感與尺度，改變人如何在一個地方生活。RSA 想讓這件事變得可以被衡量。',
   w_all='全部五件作品',
   s5=('05', '工作方法', '觀察 → 改善'),
   m_h='五個步驟，<br>一個循環。', m_b='RSA 期望設計與分析如何相互回饋。這是往後的研究方法，並非宣稱早期作品曾以此方式設計。',
   loop=[('觀察', '基地、鄰棟、氣候、人與使用情境。'), ('分析', '使用適當的模型與資料，並說明假設。'),
         ('設計', '把環境條件導入配置、量體、空間與材料。'), ('檢視', '以合適的指標比較方案與環境差異。'),
         ('改善', '保留限制與不確定性，持續修正決策。')],
   s6=('06', '研究與誠信', '研究簡報 · 2026 Q4 — 2027 Q4'),
   r_h='研究分析系統不是「能不能算」，<br><span style="color:var(--orange-ink)">而是「算完之後能不能被使用」。</span>',
   r_b='目前研究聚焦新建住宅的前期決策，以高雄為案例城市。RSA 不取代 Radiance、CFD 或 EnergyPlus，而是研究這類證據如何更早被讀懂與使用。',
   rq_head=['編號', '研究問題', '驗證層次', '驗證方式'],
   rq=[('不同樓層、時間及方案的環境差異，能否被可靠辨識？', '技術驗證', 'Technical', '以參考工具交叉比對，檢查遮蔭與計算誤差。'),
       ('整合後的環境證據，是否比分散資訊更容易判讀？', '真實案例驗證', 'Real cases', '稽核高雄基地與周邊高度，控制條件比較 A/B 方案。'),
       ('這樣的理解，能否支援更好的前期決策？', '使用者驗證', 'Users', '相同資料與任務，只改變呈現方式：比較判讀正確率、任務時間與決策理由品質。')],
   board=[('built', '原型與核心分析流程', ['基地定位、範圍與周邊量體', '日照、遮蔭、風向與 UTCI', '樓層與時間、A/B 方案比較', '報告與證據輸出']),
          ('validating', '模擬可信度與真實案例', ['太陽／遮蔭參考比對', '高雄真實基地案例', '頁面、資料與報告一致性']),
          ('next', '使用者研究與正式實證', ['權威基地資料串接評估', '案例資料完整度補強', '10–15 人使用者 pilot', '正式理解與決策比較研究'])],
   board_note='已建置功能仍需持續驗證。狀態依既有系統版本紀錄整理。',
   rec_t=('06.1', '歷史紀錄', 'r42 / r44 · 非現行認證'),
   rec=[('r42', '0.9795', '', '陰影 IoU（對照 Radiance）', '與 Radiance 直接陰影參考比較之交集聯集比，限該歷史版本與封存案例。'),
        ('r42', '0.25', 'm', 'Hausdorff 距離', '同一比較設定下的邊界差距；舊資料另記載面積偏差約 −2.05%。限該版本。'),
        ('r44', '321', '', '回歸測試通過', '歷史版本曾記錄通過。不代表新版或所有模組已達科學驗收標準。')],
   historical='歷史', r_link='方法、限制與資料來源',
   s7=('07', '交流合作'),
   c_h='歡迎就基地、環境證據或研究合作與我們交流。',
   c_ctas=[('mailto:' + SITE['email'], '交流合作', 'primary'), ('work.html', '探索作品', 'ghost'), ('platform.html', '了解 RSA 技術', 'ghost')],
 ),
}

MOSAIC = [  # (slug, img in 960/, ratio, css class, meta-en, meta-zh)
    ('vision', 'vision-gallery', 'ratio-43', 'm1', '2021 · Graduation project', '2021 · 畢業設計'),
    ('corner', 'corner-shelves', 'ratio-34', 'm2', '2020', '2020'),
    ('encounter', 'encounter-front', 'ratio-34', 'm3', '2020 · TSID entry', '2020 · TSID 競圖'),
    ('futian', 'futian-exterior', 'ratio-32', 'm4', '2022–2025 · Project lead', '2022–2025 · 專案負責'),
    ('datong', 'datong-exterior', 'ratio-43', 'm5', '2024– · Early planning', '2024– · 前期規劃'),
]


def home(lang):
    h = H[lang]
    P = pre(lang)
    S = STAMP[lang]
    proj = {p['slug']: p for p in PROJECTS}

    legend = ''.join(f'<li><span class="stamp stamp--{k}">{t}</span> {d}</li>' for k, t, d in h['legend'])
    letters = ''.join(f'''
      <div class="letter reveal"><span class="letter__glyph" aria-hidden="true">{g}</span><h3 class="letter__word">{w}</h3><p>{d}</p></div>''' for g, w, d in h['letters'])
    chain = ''.join(f'<span{" class=\"on\"" if i == h["chain_on"] else ""}>{c}</span>' for i, c in enumerate(h['chain']))
    why_body = ''.join(f'<p>{x}</p>' for x in h['why_body'])
    d_list = ''.join(f'<li>{x}</li>' for x in h['d_list'])

    tabs = ''.join(
        f'<button class="viewer__tab" role="tab" id="tab-{i}" aria-selected="{"true" if k == 0 else "false"}" aria-controls="panel-{i}"{"" if k == 0 else " tabindex=\"-1\""}>{t}</button>'
        for k, (i, t) in enumerate(h['tabs']))
    panels = ''
    for k, (i, _) in enumerate(h['tabs']):
        src, alt, cap, kind = h['panels'][i]
        st = stamp('real', h['shot_real']) if kind == 'real' else stamp('explore', h['shot_explore'])
        panels += f'''
        <div class="viewer__panel" role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}"{"" if k == 0 else " hidden"}>
          <figure>
            <div class="viewer__frame"><img src="{P}assets/img/rsa/{src}" width="1850" height="1041" loading="lazy" alt="{e(alt)}"></div>
            <figcaption class="fig__cap"><span class="mono">{cap}</span>{st}</figcaption>
          </figure>
        </div>'''
    modules = ''.join(f'<li><span class="n">M{n + 1}</span><span class="t">{t}</span>{stamp(k, S[k])}<span class="d">{d}</span></li>' for n, (t, k, d) in enumerate(h['modules']))
    t_items = ''.join(f'''
        <div class="tech reveal">{stamp(k, s)}<h3 class="tech__name">{n}</h3><p>{d}</p></div>''' for n, k, s, d in h['t_items'])

    mosaic = ''
    for slug, img, ratio, cls, men, mzh in MOSAIC:
        p = proj[slug]
        mosaic += f'''
      <a class="fig {cls} reveal" href="project-{slug}.html">
        <div class="fig__img {ratio}"><img src="{P}assets/img/work/960/{img}.webp" loading="lazy" alt="{e(p['name'][lang])}"></div>
        <div class="work-cap"><span class="work-cap__no">W-{p['no']}</span><span class="work-cap__title">{e(p['name'][lang])}</span><span class="work-cap__arrow" aria-hidden="true">↗</span>
          <span class="work-cap__meta mono mono--sm"><span class="stamp stamp--work">{p['klabel'][lang]}</span>{men if lang == 'en' else mzh}</span></div>
      </a>'''

    loop = ''.join(f'''
      <li class="loop__step reveal"><span class="loop__n">0{n + 1}</span><span class="loop__en">{t}</span>{"" if lang == "en" else ""}<p class="loop__d">{d}</p></li>''' for n, (t, d) in enumerate(h['loop']))
    rq = ''.join(f'''
      <div class="rq__row reveal"><span class="rq__no">RQ{n + 1}</span><p class="rq__q">{q}</p><p class="rq__v">{v}<br><span>{v2}</span></p><p class="rq__h">{how}</p></div>''' for n, (q, v, v2, how) in enumerate(h['rq']))
    board = ''.join(f'''
      <div class="board__col reveal">{stamp({'built': 'real', 'validating': 'explore', 'next': 'planned'}[k], S[k])}<h3>{t}</h3><ul>{''.join(f'<li>{x}</li>' for x in items)}</ul></div>''' for k, t, items in h['board'])
    recs = ''.join(f'''
      <div class="record reveal"><span class="record__ver">{stamp('record', v)}</span><span class="record__val">{val}{f'<small>{u}</small>' if u else ''}</span><div><p class="record__label">{lab}</p><p class="record__note">{note}</p></div><span class="mono mono--sm muted">{h['historical']}</span></div>''' for v, val, u, lab, note in h['rec'])
    ctas = ''.join(f'<a class="btn btn--{k}" href="{href}">{t} <span class="arr" aria-hidden="true">→</span></a>' for href, t, k in h['c_ctas'])

    body = f'''
<main id="main">

<!-- COVER -->
<section class="cover" aria-labelledby="cover-title">
  <div class="cover__sun" data-sun aria-hidden="true">
    <svg viewBox="0 0 1000 420" fill="none">
      <path class="sun-path" d="M 40 418 A 470 400 0 0 1 960 418" stroke="#8c8b86" stroke-width="1" stroke-dasharray="2 6"/>
      <line class="sun-ray" x1="560" y1="418" x2="300" y2="140" stroke="#ff5a1f" stroke-width="1" stroke-dasharray="10 4 2 4"/>
      <circle class="sun-dot" cx="300" cy="140" r="11" fill="#ff5a1f"/>
    </svg>
  </div>
  <p class="cover__sunread mono mono--sm muted" aria-hidden="true">{'Scroll = time of day' if lang == 'en' else '捲動 = 一天的時間'}<br><span class="orange" data-sun-time>10:12</span></p>
  <div class="wrap">
    <div class="cover__top">
      <div class="cover__kicker">{stamp('real', h['eyebrow'])}<span class="mono muted">{h['sheet']}</span></div>
      <h1 id="cover-title" class="cover__title display d-xxl">{h['h1']}</h1>
      <div class="cover__intro">
        <p class="lede">{h['sub']}</p>
        {h['alt_tag']}
        <div class="cover__ctas">
          <a class="btn btn--primary" href="work.html">{h['cta1']} <span class="arr" aria-hidden="true">→</span></a>
          <a class="btn btn--ghost" href="platform.html">{h['cta2']} <span class="arr" aria-hidden="true">→</span></a>
        </div>
      </div>
    </div>
    <div class="cover__diptych">
      <a class="fig fig--design reveal" href="project-vision.html">
        <div class="fig__img ratio-32"><img src="{P}assets/img/work/vision-exterior.webp" width="2048" height="1298" alt="{e(proj['vision']['hero'][1][lang])}" fetchpriority="high"></div>
        <div class="fig__cap"><span class="mono">{h['fig1']}</span><span class="mono">{h['fig1c']}</span></div>
      </a>
      <span class="cover__x" aria-hidden="true">×</span>
      <a class="fig fig--env reveal" href="platform.html">
        <div class="fig__img ratio-43 fig__img--logo"><img src="{P}assets/img/rsa/analyzer-logo.webp" width="1150" height="490" alt="{h['logo_alt']}"></div>
        <div class="fig__cap"><span class="mono">{h['fig2']}</span><span class="mono">{h['fig2s']}</span></div>
      </a>
    </div>
  </div>
</section>

<aside class="legend" aria-label="{h['legend_t']}">
  <div class="wrap"><p class="legend__title">{h['legend_t']}</p><ul>{legend}</ul></div>
</aside>
<div class="cut" aria-hidden="true"><span class="cut__tag cut__tag--l">1 —</span><span class="cut__tag cut__tag--r">— 1</span></div>

<!-- 01 RSA -->
<section class="section" aria-labelledby="rsa-title">
  <div class="wrap">
    {sheet_head(*h['s1'])}
    <h2 id="rsa-title" class="sr-only">{h['s1'][1]}</h2>
    <div class="letters">{letters}
    </div>
    <div class="grid" style="margin-top:clamp(40px,5vw,72px);row-gap:20px">
      <p class="span-7 lede">{h['intro']}</p>
      <p class="span-4 start-9 naming">{h['naming']}</p>
    </div>
  </div>
</section>

<!-- 02 WHY -->
<section class="section" style="padding-top:0" aria-labelledby="why-title">
  <div class="wrap">
    {sheet_head(*h['s2'])}
    <div class="grid" style="row-gap:32px">
      <h2 id="why-title" class="span-8 h-statement why">{h['why']}</h2>
      <div class="span-4 start-9 body muted" style="display:flex;flex-direction:column;gap:16px;font-size:16px">{why_body}</div>
      <div class="span-12 chain" style="margin-top:8px">{chain}</div>
    </div>
  </div>
</section>

<!-- 03 EXPERTISE -->
<section id="expertise" class="section" style="padding-top:0" aria-labelledby="exp-title">
  <div class="wrap">
    {sheet_head(*h['s3'])}
    <h2 id="exp-title" class="sr-only">{h['s3'][1]}</h2>
    <div class="chapter">
      <figure class="fig chapter__fig reveal">
        <div class="fig__img ratio-43"><img src="{P}assets/img/work/corner-reading.webp" loading="lazy" alt="{e(proj['corner']['imgs'][1][2][lang][0])}"></div>
        <figcaption class="fig__cap"><span class="mono">{h['d_fig']}</span></figcaption>
      </figure>
      <div class="chapter__text reveal">
        <p class="chapter__k"><span class="chapter__l">D</span>{h['d_k']}</p>
        <h3 class="display d-m">{h['d_h']}</h3>
        <p class="body muted">{h['d_b']}</p>
        <ul class="ticks">{d_list}</ul>
        <p class="mono mono--sm muted">{h['d_note']}</p>
      </div>
    </div>
  </div>
</section>

<section id="environment" class="dark section" aria-labelledby="env-title">
  <div class="wrap">
    <div class="grid" style="margin-bottom:clamp(40px,5vw,72px);row-gap:28px">
      <div class="span-9"><p class="chapter__k"><span class="chapter__l">E</span>{h['e_k']}</p><h3 id="env-title" class="display d-l">{h['e_h']}</h3></div>
      <div class="bridge__note bridge__note--side reveal"><span class="mono mono--sm">{h['e_note_t']}</span><p style="font-size:15px">{h['e_note']}</p></div>
    </div>
    <div class="viewer">
      <div class="viewer__tabs" role="tablist" aria-label="Residential Site Analyzer">{tabs}</div>
      <div class="viewer__stage">{panels}
      </div>
      <div class="viewer__side">
        <p class="muted">{h['e_intro']}</p>
        <ol class="modules">{modules}</ol>
        <a class="link" href="platform.html">{h['e_link']} <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="tech-title">
  <div class="wrap">
    <div class="grid" style="row-gap:24px;margin-bottom:clamp(36px,4vw,56px);align-items:end">
      <div class="span-8"><p class="chapter__k"><span class="chapter__l">T</span>{h['t_k']}</p><h3 id="tech-title" class="display d-l">{h['t_h']}</h3></div>
      <p class="span-4 ai-rule">{h['t_ai']}</p>
    </div>
    <div class="techs">{t_items}
    </div>
  </div>
</section>

<!-- 04 WORK -->
<section class="section" style="padding-top:0" aria-labelledby="work-title">
  <div class="wrap">
    {sheet_head(*h['s4'])}
    <div class="grid" style="margin-bottom:clamp(40px,5vw,72px);row-gap:24px;align-items:end">
      <h2 id="work-title" class="span-7 display d-l">{h['w_h']}</h2>
      <p class="span-5 body muted">{h['w_b']}</p>
    </div>
    <div class="mosaic">{mosaic}
      <div class="m-note reveal">
        <p class="h-statement">{h['w_note']}</p>
        <p style="margin-top:24px"><a class="link" href="work.html">{h['w_all']} <span aria-hidden="true">→</span></a></p>
      </div>
    </div>
  </div>
</section>

<!-- 05 METHOD -->
<section class="section" style="padding-top:0" aria-labelledby="method-title">
  <div class="wrap">
    {sheet_head(*h['s5'])}
    <div class="grid" style="margin-bottom:clamp(40px,5vw,64px);row-gap:24px;align-items:end">
      <h2 id="method-title" class="span-7 display d-l">{h['m_h']}</h2>
      <p class="span-5 body muted">{h['m_b']}</p>
    </div>
    <ol class="loop">{loop}
    </ol>
    <div class="loop__return" aria-hidden="true">
      <svg viewBox="0 0 1000 72" preserveAspectRatio="none" fill="none">
        <path d="M 900 0 L 900 44 L 100 44 L 100 8" stroke="#ff5a1f" stroke-width="1.5" stroke-dasharray="14 5 3 5" vector-effect="non-scaling-stroke"/>
        <path d="M 94 16 L 100 4 L 106 16" stroke="#ff5a1f" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
      </svg>
    </div>
  </div>
</section>

<!-- 06 RESEARCH -->
<section class="section" style="padding-top:0" aria-labelledby="research-title">
  <div class="wrap">
    {sheet_head(*h['s6'])}
    <div class="grid" style="margin-bottom:clamp(48px,6vw,88px);row-gap:28px;align-items:end">
      <h2 id="research-title" class="span-9 display d-l">{h['r_h']}</h2>
      <p class="span-3 body muted" style="font-size:15px">{h['r_b']}</p>
    </div>
    <div class="rq">
      <div class="rq__row rq__row--head mono mono--sm muted">{''.join(f'<span>{x}</span>' for x in h['rq_head'])}</div>{rq}
    </div>
    <div class="board" style="margin-top:clamp(56px,7vw,104px)">{board}
    </div>
    <p class="mono mono--sm muted" style="margin-top:16px">{h['board_note']}</p>
    <div style="margin-top:clamp(72px,9vw,128px)">{sheet_head(*h['rec_t'])}</div>
    <div class="records">{recs}
    </div>
    <p style="margin-top:32px"><a class="link" href="research.html">{h['r_link']} <span aria-hidden="true">→</span></a></p>
  </div>
</section>

<!-- 07 CONTACT -->
<section class="section rule" aria-labelledby="contact-title">
  <div class="wrap">
    {sheet_head(*h['s7'])}
    <div class="grid" style="row-gap:32px">
      <h2 id="contact-title" class="span-8 h-statement">{h['c_h']}</h2>
      <div class="span-12"><a class="contact__mail" href="mailto:{SITE['email']}">{SITE['email']}</a></div>
      <div class="span-12 cover__ctas">{ctas}</div>
    </div>
  </div>
</section>
</main>
'''
    write(lang, 'index.html', page(lang, 'index.html', h['title'], h['desc'], body))


# ------------------------------------------------------------------ WORK + CASES
W = {
  'en': dict(title='Selected Work — RSA', desc='Founder’s selected work: three individual academic designs and two prior-employment residential projects, each credited to its actual author and role.',
             h1='From the work,<br><span style="color:var(--mute-2)">to the questions.</span>',
             lede='Academic design and residential project leadership—each one a source of inquiry.',
             note='Three individual academic designs and two projects from prior employment. <strong style="color:var(--ink)">None are RSA commissions, and none were analysed with RSA.</strong>',
             f_all='All', f_ac='Individual academic', f_emp='Prior employment', reg=('REG', 'Project register', 'Every project, one line')),
  'zh': dict(title='精選作品 — RSA 見築科技', desc='創辦人精選作品：三件個人學術設計與兩件過往任職住宅專案，皆依實際作者與角色標示。',
             h1='從作品，<br><span style="color:var(--mute-2)">走向問題。</span>',
             lede='學術設計與住宅專案實務——每一件都是提問的起點。',
             note='三件個人學術設計、兩件過往任職專案。<strong style="color:var(--ink)">均非 RSA 承攬案，也未使用 RSA 分析。</strong>',
             f_all='全部', f_ac='個人學術設計', f_emp='過往任職專案', reg=('REG', '作品目錄', '一件作品，一行紀錄')),
}


def work_stamp(p, lang):
    return f'<span class="stamp stamp--work">{e(p["klabel"][lang])}</span>'


def work_index(lang):
    w = W[lang]
    u = UI[lang]
    P = pre(lang)
    bands = ''
    for i, p in enumerate(PROJECTS):
        left = i % 2 == 0
        img_span = 'span-7' if left else 'span-7 start-6'
        txt_span = 'span-4 start-9' if left else 'span-4 start-1'
        ratio = 'ratio-32' if i != 2 else 'ratio-43'
        bands += f'''
    <article class="grid reveal band{"" if left else " band--flip"}" data-kind="{p['kind']}">
      <a class="fig {img_span}" href="project-{p['slug']}.html" aria-label="{e(p['name'][lang])}">
        <div class="fig__img {ratio}"><img src="{P}assets/img/work/960/{p['hero'][0]}.webp" loading="lazy" alt="{e(p['hero'][1][lang])}"></div>
      </a>
      <div class="{txt_span}">
        <p class="mono muted" style="margin-bottom:14px">W-{p['no']} · {p['year']}</p>
        <h2 class="display d-m"><a href="project-{p['slug']}.html">{e(p['name'][lang])}</a></h2>
        <p class="muted" style="margin-top:8px">{e(p['alt_name'][lang])}</p>
        <p style="margin-top:18px;font-size:18px">{e(p['tag'][lang])}</p>
        <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:20px">{work_stamp(p, lang)}<span class="mono mono--sm muted">{e(p['loc'][lang])}</span></div>
        <p style="margin-top:20px"><a class="link" href="project-{p['slug']}.html">{u['case_study']} <span aria-hidden="true">→</span></a></p>
      </div>
    </article>'''
    rows = ''.join(f'''
      <a class="index__row" href="project-{p['slug']}.html" data-kind="{p['kind']}">
        <span class="index__no">W-{p['no']}</span><span class="index__title">{e(p['name'][lang])}</span>
        <span class="mono mono--sm muted hide-m">{e(p['klabel'][lang])}</span><span class="mono mono--sm muted hide-m">{p['year']} · {e(p['loc'][lang])}</span><span aria-hidden="true">↗</span>
      </a>''' for p in PROJECTS)
    body = f'''
<main id="main">
<section class="pagehead">
  <div class="wrap">
    <nav class="crumb mono mono--sm" aria-label="Breadcrumb"><a href="index.html">{u['home']}</a><span aria-hidden="true">/</span><span>{u['work']}</span></nav>
    <div class="grid">
      <h1 class="span-8 display d-xl">{w['h1']}</h1>
      <div class="span-4" style="display:flex;flex-direction:column;gap:16px"><p class="lede">{w['lede']}</p><p class="muted" style="font-size:15px">{w['note']}</p></div>
    </div>
  </div>
</section>
<section class="section--tight">
  <div class="wrap">
    <div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:16px">
      <div class="filters" data-filters role="group" aria-label="Filter">
        <button type="button" data-filter="all" aria-pressed="true">{w['f_all']}<span class="c">05</span></button>
        <button type="button" data-filter="academic" aria-pressed="false">{w['f_ac']}<span class="c">03</span></button>
        <button type="button" data-filter="employment" aria-pressed="false">{w['f_emp']}<span class="c">02</span></button>
      </div>
      <span class="mono mono--sm muted">2020 — 2025</span>
    </div>
    <div style="margin-top:24px;border-top:2px solid var(--ink)">{bands}
    </div>
  </div>
</section>
<section class="section" style="padding-top:clamp(24px,4vw,48px)">
  <div class="wrap">
    {sheet_head(*w['reg'])}
    <div class="index">{rows}
    </div>
  </div>
</section>
</main>
'''
    write(lang, 'work.html', page(lang, 'work.html', w['title'], w['desc'], body, active='work.html'))


def case(lang, i):
    u = UI[lang]
    P = pre(lang)
    p = PROJECTS[i]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    fname = f'project-{p["slug"]}.html'
    cls = ['s1', 's2', 's3', 's4', 's5']
    figs = []
    for k, (f, ratio, t) in enumerate(p['imgs']):
        alt, cap = t[lang]
        src = f'{P}assets/img/work/960/{f}.webp' if ratio == 'ratio-34' else f'{P}assets/img/work/{f}.webp'
        figs.append(f'<figure class="fig {cls[k]} reveal"><div class="fig__img {ratio}"><img src="{src}" loading="lazy" alt="{e(alt)}"></div><figcaption class="fig__cap"><span class="mono">{"Fig." if lang == "en" else "圖"} {p["no"]}.{k + 2} — {e(cap)}</span></figcaption></figure>')
    area_or_type = (u['k_area'], p['area']) if p['area'] else (u['k_type'], p['type'][lang])
    credit = u['credit_academic'] if p['kind'] == 'academic' else u['credit_employment']
    role_block = ''
    if p.get('scope'):
        rows = ''.join(f'<div class="ledger__row"><span class="ledger__no">0{k + 1}</span><p class="ledger__t">{e(a)}</p><p class="ledger__d">{e(b)}</p></div>' for k, (a, b) in enumerate(p['scope'][lang]))
        role_block = f'''
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head('03', u['role_h'], e(p['role'][lang]))}
    <p class="mono muted" style="margin-bottom:12px">{u['role_sub']}</p>
    <div class="ledger">{rows}</div>
    <div class="grid" style="row-gap:24px;margin-top:clamp(32px,4vw,56px)">
      <div class="span-7"><p class="mono muted" style="margin-bottom:10px">{u['outcome']}</p><p class="h-statement" style="font-size:clamp(20px,2vw,28px)">{e(p['outcome'][lang])}</p></div>
      <div class="span-4 start-9 credit"><span class="mono mono--sm">▲ {u['credit_title']}</span><p style="font-size:14.5px">{u['role_note']}</p></div>
    </div>
  </div>
</section>'''
    body = f'''
<main id="main">
<section class="case-hero">
  <div class="wrap">
    <nav class="crumb mono mono--sm" aria-label="Breadcrumb"><a href="work.html">{u['work']}</a><span aria-hidden="true">/</span><span>W-{p['no']}</span></nav>
    <div class="grid" style="row-gap:24px;align-items:end">
      <div class="span-8">
        <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:20px">{work_stamp(p, lang)}<span class="mono muted" style="align-self:center">{u['case']} {p['no']} / 05</span></div>
        <h1 class="display d-xl">{e(p['name'][lang])}</h1>
        <p class="muted" style="margin-top:14px;font-size:18px">{e(p['alt_name'][lang])}</p>
      </div>
      <p class="span-4 lede">{e(p['tag'][lang])}</p>
    </div>
    <figure class="fig case-hero__img">
      <div class="fig__img"><img src="{P}assets/img/work/{p['hero'][0]}.webp" width="2048" height="1298" alt="{e(p['hero'][1][lang])}" fetchpriority="high"></div>
      <figcaption class="fig__cap"><span class="mono">{"Fig." if lang == "en" else "圖"} {p['no']}.1 — {u['fig_hero']}</span><span class="mono">{e(p['name'][lang])} · {e(p['klabel'][lang])} · {p['year']}</span></figcaption>
    </figure>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {sheet_head('01', u['behind'])}
    <div class="grid" style="row-gap:40px">
      <div class="span-7" style="display:flex;flex-direction:column;gap:32px">
        <div><p class="mono muted" style="margin-bottom:10px">{u['approach']}</p><p class="h-statement">{e(p['approach'][lang])}</p></div>
        <div><p class="mono muted" style="margin-bottom:10px">{u['connection']}</p><p class="lede">{e(p['connection'][lang])}</p></div>
      </div>
      <div class="span-4 start-9" style="display:flex;flex-direction:column;gap:20px">
        <dl class="tblock tblock--stack">
          <div class="tblock__pair"><div><dt class="k">{u['k_year']}</dt><dd class="v">{p['year']}</dd></div><div><dt class="k">{u['k_loc']}</dt><dd class="v">{e(p['loc'][lang])}</dd></div></div>
          <div><dt class="k">{u['k_role']}</dt><dd class="v">{e(p['role'][lang])}</dd></div>
          <div><dt class="k">{area_or_type[0]}</dt><dd class="v">{e(area_or_type[1])}</dd></div>
          <div><dt class="k">{u['k_context']}</dt><dd class="v">{e(p['context'][lang])}</dd></div>
        </dl>
        <div class="credit"><span class="mono mono--sm">▲ {u['credit_title']}</span><p style="font-size:14.5px">{credit}</p></div>
      </div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head('02', u['perspectives'], u['renders'])}
    <div class="spread">
      {chr(10).join(figs)}
    </div>
  </div>
</section>
{role_block}
<div class="wrap">
  <a class="next" href="project-{nxt['slug']}.html">
    <span><span class="mono muted" style="display:block;margin-bottom:12px">{u['next']} · W-{nxt['no']}</span><span class="next__t display d-l">{e(nxt['name'][lang])}</span></span>
    <span class="mono">{e(nxt['klabel'][lang])} · {nxt['year']} <span aria-hidden="true">→</span></span>
  </a>
</div>
</main>
'''
    title = f'{p["name"][lang]} — RSA'
    desc = f'{p["name"][lang]} ({p["year"]}) — {p["tag"][lang]} {p["klabel"][lang]}.'
    write(lang, fname, page(lang, fname, title, desc, body, active='work.html', img=f'assets/img/work/960/{p["hero"][0]}.webp'))


def write_sitemap():
    pages = ['index.html', 'work.html'] + [f'project-{p["slug"]}.html' for p in PROJECTS] + ['platform.html', 'research.html', 'company.html', 'contact.html', 'privacy.html']
    xs = []
    for f in pages:
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{url(l, f)}"/>' for l, h in (('en', 'en'), ('zh', 'zh-Hant')))
        for l in LANGS:
            xs.append(f'  <url><loc>{url(l, f)}</loc>{alts}</url>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(xs) + '\n</urlset>\n')
    with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8') as fh:
        fh.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE["domain"]}/sitemap.xml\n')


if __name__ == '__main__':
    for lang in LANGS:
        home(lang)
        work_index(lang)
        for i in range(len(PROJECTS)):
            case(lang, i)
    import pages2
    pages2.build_all()
    write_sitemap()
    print('built')
