# -*- coding: utf-8 -*-
"""Platform, About, Research, Contact, Privacy and 404 — EN + ZH."""
from build import page, write, sheet_head, stamp, pre, e, STAMP, SITE

# ------------------------------------------------------------------ helpers
def pagehead(lang, crumb, h1, side, size='d-xl'):
    home = 'Home' if lang == 'en' else '首頁'
    return f'''
<section class="pagehead">
  <div class="wrap">
    <nav class="crumb mono mono--sm" aria-label="Breadcrumb"><a href="index.html">{home}</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
    <div class="grid">
      <h1 class="span-8 display {size}">{h1}</h1>
      <div class="span-4" style="display:flex;flex-direction:column;gap:16px">{side}</div>
    </div>
  </div>
</section>'''


def ledger(rows, head=None):
    h = ''
    if head:
        h = '<div class="ledger__row ledger__row--head mono mono--sm muted">' + ''.join(f'<span>{x}</span>' for x in head) + '</div>'
    r = ''.join(f'<div class="ledger__row reveal"><span class="ledger__no">{n}</span><p class="ledger__t">{t}</p><p class="ledger__d">{d}</p></div>' for n, t, d in rows)
    return f'<div class="ledger">{h}{r}</div>'


def shot(P, src, alt, cap, kind, label, cls='', style=''):
    return f'''<figure class="fig {cls} reveal"{f' style="{style}"' if style else ''}>
        <div class="viewer__frame" style="border-color:var(--line)"><img src="{P}assets/img/rsa/{src}" width="1850" height="1041" loading="lazy" alt="{e(alt)}"></div>
        <figcaption class="fig__cap"><span class="mono">{cap}</span>{stamp(kind, label)}</figcaption>
      </figure>'''


# ------------------------------------------------------------------ PLATFORM
PL = {
 'en': dict(
  title='Platform — Residential Site Analyzer by RSA',
  desc='Residential Site Analyzer is RSA’s research platform for site, solar and shading, exploratory wind and UTCI-oriented analysis. RSA Studio is a concept; RSA Intelligence is planned.',
  crumb='Platform', h1='From site conditions to <span style="color:var(--mute-2)">legible evidence.</span>',
  side_lede='One working research prototype, and two directions it could grow into.',
  side_stamps=[('real', 'Site Analyzer · Real'), ('concept', 'Studio · Concept'), ('planned', 'Intelligence · Planned')],
  s1=('01', 'Residential Site Analyzer', 'Research prototype · Python + Streamlit'),
  h2='A working prototype.<br>Not a promise.',
  intro='Residential Site Analyzer is RSA’s own research platform. It brings site setup, massing, solar and shading, exploratory wind and UTCI-oriented analysis into one workspace. Everything in this section is a real capture from the development build; interfaces and results may change before further validation.',
  shots=[('site-workspace.webp', 'RSA prototype: map-based site workspace with a parcel outline and setup panels', 'C-01 — Site definition: map workspace and geographic context', 'real', 'Real screenshot · dev build'),
         ('solar-shading.webp', 'RSA prototype: time-based 3D solar and shading view of a target building among neighbouring blocks', 'C-02 — Solar &amp; shading by floor and time', 'real', 'Real'),
         ('utci.webp', 'RSA prototype: UTCI-oriented outdoor thermal comfort research view', 'C-03 — UTCI-oriented thermal-comfort view', 'explore', 'Exploratory'),
         ('massing.webp', 'RSA prototype: massing editor on a map, with Scheme A outlined in red among neighbouring buildings', 'C-04 — Massing editor: Scheme A / B on one site model', 'real', 'Real'),
         ('wind.webp', 'RSA prototype: 3D wind-direction view with streamlines passing a cluster of building masses', 'C-05 — Wind direction &amp; massing: relative ventilation potential, not CFD', 'explore', 'Exploratory')],
  s11=('01.1', 'Module register', 'Status as of 2026'),
  modules=[('M1', 'Site context', 'Spatial site setup on a map, parcel and surroundings', 'real'),
           ('M2', 'Building massing', 'Target building, neighbours and A/B schemes', 'real'),
           ('M3', 'Solar &amp; shading', 'Time-based shadow study with historical reference comparison', 'real'),
           ('M4', 'Wind', 'Directional preview — not a validated CFD solver', 'explore'),
           ('M5', 'UTCI comfort', 'Research visualisation; inputs and limits must be documented', 'explore'),
           ('M6', 'Floors, time &amp; reports', '2D/3D, floor slices, time comparison and reports — being integrated and debugged', 'planned')],
  m6_label='In progress',
  s2=('02', 'One foundation, several horizons', 'Only Site Analyzer exists today'),
  horizons=[('core', 'real', 'Real · Research prototype', 'Site<br>Analyzer', 'The working research environment: site, massing, sun and shade, wind preview and comfort in one place.', ['Python &amp; Streamlit implementation', '2D / 3D environments in active development', 'Analysis &amp; evidence workflows']),
            ('concept', 'concept', 'Concept · Not available', 'RSA<br>Studio', 'A proposed comparison environment linking environmental change to the design choices behind it.', ['Alternative massing &amp; A/B scenarios', 'Floor- and time-scale comparison', 'Report-ready summaries (concept)']),
            ('concept', 'planned', 'Planned · Not deployed', 'RSA<br>Intelligence', 'Planned research into whether AI (e.g. the Claude API) can explain results in terms people can evaluate and challenge.', ['Explanations tied to source results', 'Human review &amp; traceable assumptions', 'Explicit uncertainty and method limits'])],
  s3=('03', 'Connected by design, transparent by method'),
  stack_h='A Python and Streamlit research system linking spatial setup, visualisation and evidence-oriented design support.',
  sources='Geographic and climate sources studied or evaluated: OpenStreetMap, Taiwan NLSC, CWA, ERA5 and Open-Meteo. Listing a source does not mean every API is integrated, live or independently validated.',
  stack=[('Python / Streamlit', 'Experimental interface and analysis orchestration.'), ('Solar geometry', 'Time-aware shadow research with historical reference comparison.'),
         ('Wind exploration', 'Directional preview. Not CFD-based pressure or pedestrian-safety evidence.'), ('UTCI orientation', 'Depends on climate inputs, radiation, geometry and modelling assumptions.')],
  band='Research preview, not release certification. Screenshots do not prove validated accuracy, production readiness or commercial availability. Site Analyzer is a decision-support tool for early design; it does not replace Radiance, CFD or EnergyPlus.',
  ai=dict(
   head=('02.1', 'RSA Intelligence · How we plan to use Claude', 'Planned · not deployed'),
   h='Explain the evidence.<br><span style="color:var(--mute-2)">Never invent it.</span>',
   intro='Residential Site Analyzer already computes floor-, time- and scheme-level results. What people struggle with is reading them. RSA Intelligence is planned research into using Claude (via the Claude API) to explain those results in plain language—tied to their sources, with the limits stated, and reviewed by a person.',
   flow=[('01', 'Inputs', 'Computed results from Site Analyzer: floor × time × scheme values, the parameters used, data sources and known limits.'),
         ('02', 'Claude', 'Writes a short explanation: what differs between schemes, on which floors and at which hours, and which assumptions matter most.'),
         ('03', 'Checks', 'Every statement must point to a source result. Claims without a source are dropped; uncertainty and method limits are stated.'),
         ('04', 'Human review', 'A designer or researcher reviews and edits the text before it goes into a report or a design discussion.')],
   uses=[('Scheme summaries', 'A vs B differences in sun, shade and outdoor comfort, by floor and hour.'),
         ('Assumption prompts', 'Which inputs (date, height, climate source) most affect a result, and what to check next.'),
         ('Report drafts', 'Plain-language sections for environmental reports, with traceable references.'),
         ('Question answering', 'Answer design-team questions only from the analysed case, with sources.')],
   rules_t='Ground rules',
   rules=['Claude explains results; it never produces or alters calculation results.', 'Every claim links to a source value, parameter or method note.', 'Uncertainty, model limits and unvalidated modules are stated in the text.', 'A person reviews before anything is shared.', 'It does not replace physical simulation or professional judgement.'],
   ex_t='What an explanation could look like', ex_stamp='Concept illustration · not a live Claude response',
   ex_q='Why does Scheme B get less direct sun on the 3rd floor in winter afternoons?',
   ex_a='In this [example] case, the neighbouring block to the south-west is taller than Scheme B’s 3rd-floor façade between [14:00] and [16:00], so the façade is in shadow for most of that window [→ shadow result, 3F, 21 Dec]. Scheme A sits [2 m] further north and avoids part of that shadow. This comparison uses a clear-sky assumption and the recorded neighbour heights [→ input sources]; real cloud cover would reduce both.',
   ex_note='Bracketed values are placeholders to show the format. Arrows mark the source each statement would cite.',
   study='Whether these explanations actually help is a research question. It will be tested in the planned user study: same data, same task, with and without explanations—comparing accuracy, time and quality of reasoning.',
   study_link='Research &amp; validation'),
  b1='How we validate', b2='Get in touch'),
 'zh': dict(
  title='技術平台 — Residential Site Analyzer · RSA 見築科技',
  desc='Residential Site Analyzer 是 RSA 自主研發的住宅基地環境分析研究平台：基地、日照遮蔭、探索性風環境與 UTCI 導向熱舒適。RSA Studio 為概念，RSA Intelligence 規劃中。',
  crumb='技術平台', h1='從基地條件，<br><span style="color:var(--mute-2)">到看得懂的證據。</span>',
  side_lede='一個真實運作的研究原型，以及兩個可能的延伸方向。',
  side_stamps=[('real', 'Site Analyzer · 真實'), ('concept', 'Studio · 概念'), ('planned', 'Intelligence · 規劃中')],
  s1=('01', 'Residential Site Analyzer', '研究原型 · Python + Streamlit'),
  h2='一個真實運作的原型，<br>而不是承諾。',
  intro='Residential Site Analyzer（住宅基地環境分析）是 RSA 自主研發的研究平台，把基地設定、建築量體、日照遮蔭、探索性風環境與 UTCI 導向分析整合在同一個工作區。本節所有畫面皆擷取自開發版本；介面與結果在進一步驗證前仍可能變動。',
  shots=[('site-workspace.webp', 'RSA 原型：地圖上的基地定位與設定面板', 'C-01 — 基地設定：地圖工作區與地理脈絡', 'real', '真實截圖 · 開發版本'),
         ('solar-shading.webp', 'RSA 原型：目標建物與鄰棟的 3D 日照遮蔭畫面', 'C-02 — 依樓層與時間的日照／遮蔭', 'real', '真實'),
         ('utci.webp', 'RSA 原型：UTCI 戶外熱環境研究畫面', 'C-03 — UTCI 導向熱舒適研究畫面', 'explore', '探索中'),
         ('massing.webp', 'RSA 原型：地圖上的量體編輯，方案 A 以紅框標示', 'C-04 — 量體編輯：A／B 方案共用同一基地模型', 'real', '真實'),
         ('wind.webp', 'RSA 原型：流線通過建築群的 3D 風向畫面', 'C-05 — 風向與量體關係：相對通風潛勢，非 CFD', 'explore', '探索中')],
  s11=('01.1', '模組目錄', '2026 年狀態'),
  modules=[('M1', '基地脈絡', '地圖上的基地範圍與周邊環境設定', 'real'),
           ('M2', '建築量體', '目標建物、鄰棟與 A／B 方案', 'real'),
           ('M3', '日照／遮蔭', '時間條件下的陰影研究，含歷史參考比對', 'real'),
           ('M4', '風環境', '風向預覽 — 非已驗證之 CFD', 'explore'),
           ('M5', 'UTCI 熱舒適', '研究性視覺化；須註明輸入條件與驗證限制', 'explore'),
           ('M6', '樓層、時序與報告', '2D／3D、樓層切片、時序比較與報告 — 整合與除錯中', 'planned')],
  m6_label='進行中',
  s2=('02', '一個基礎，多個延伸', '目前只有 Site Analyzer 實際存在'),
  horizons=[('core', 'real', '真實 · 研究原型', 'Site<br>Analyzer', '真實運作的研究環境：基地、量體、日照遮蔭、風向預覽與熱舒適整合在一起。', ['Python 與 Streamlit 實作', '2D／3D 環境持續開發中', '分析與證據工作流程']),
            ('concept', 'concept', '概念 · 尚未提供', 'RSA<br>Studio', '構想中的方案比較環境，把環境差異連回背後的設計選擇。', ['替代量體與 A／B 情境', '樓層與時間尺度比較', '報告摘要（概念）']),
            ('concept', 'planned', '規劃中 · 尚未部署', 'RSA<br>Intelligence', '規劃研究：AI（例如 Claude API）能否以人可以檢驗與質疑的方式解釋分析結果。', ['解釋與來源結果綁定', '人工審查與可追溯的假設', '明確揭露不確定性與方法限制'])],
  s3=('03', '以設計連結，以方法透明'),
  stack_h='以 Python 與 Streamlit 建構的研究系統，串連空間設定、視覺化與證據導向的設計支援。',
  sources='曾研究或評估的地理與氣象資料來源：OpenStreetMap、內政部國土測繪中心（NLSC）、中央氣象署（CWA）、ERA5 與 Open-Meteo。列出來源不代表每一項皆已完成即時 API 串接或獨立驗證。',
  stack=[('Python／Streamlit', '實驗性介面與分析流程整合。'), ('太陽幾何', '時間條件下的陰影研究，含歷史參考比對。'),
         ('風環境探索', '風向預覽，非 CFD 風壓或行人安全證據。'), ('UTCI 導向', '結果取決於氣象輸入、輻射、幾何與模型假設。')],
  band='研究預覽，非正式版本認證。截圖不代表已驗證的精度、正式可用或商業上市。Site Analyzer 是設計前期的決策支援工具，不取代 Radiance、CFD 或 EnergyPlus。',
  ai=dict(
   head=('02.1', 'RSA Intelligence · 我們計畫如何使用 Claude', '規劃中 · 尚未部署'),
   h='解釋證據，<br><span style="color:var(--mute-2)">而不是捏造證據。</span>',
   intro='Residential Site Analyzer 已能計算樓層、時間與方案層級的結果；真正困難的是「讀懂」這些結果。RSA Intelligence 是規劃中的研究：透過 Claude API，以白話解釋分析結果——每句話都對應來源、說明限制，並經過人工審查。',
   flow=[('01', '輸入', 'Site Analyzer 的計算結果：樓層 × 時間 × 方案數值、使用的參數、資料來源與已知限制。'),
         ('02', 'Claude', '寫出簡短說明：方案之間哪裡不同、在哪些樓層與時段，以及哪些假設影響最大。'),
         ('03', '檢查', '每一句說明都必須指向來源結果；沒有來源的說法會被移除，並註明不確定性與方法限制。'),
         ('04', '人工審查', '由設計者或研究者審閱、修改後，才放進報告或設計討論。')],
   uses=[('方案摘要', 'A／B 方案在日照、遮蔭與戶外熱舒適上的差異，依樓層與時段整理。'),
         ('假設提示', '哪些輸入（日期、高度、氣象來源）最影響結果，下一步該檢查什麼。'),
         ('報告草稿', '環境報告中的白話段落，附可追溯的引用。'),
         ('問答', '只根據已分析的案例回答設計團隊的問題，並附來源。')],
   rules_t='基本原則',
   rules=['Claude 只解釋結果，不產生也不修改計算結果。', '每個說法都連到來源數值、參數或方法說明。', '文字中明確寫出不確定性、模型限制與未驗證模組。', '任何內容分享前都經人工審查。', '不取代物理模擬，也不取代專業判斷。'],
   ex_t='說明可能長這樣', ex_stamp='概念示意 · 非 Claude 實際回應',
   ex_q='為什麼方案 B 的 3 樓在冬季下午直射日照比較少？',
   ex_a='在這個〔示例〕案例中，西南側鄰棟在〔14:00〕到〔16:00〕之間高於方案 B 的 3 樓立面，因此該時段大部分時間立面位於陰影中〔→ 陰影結果，3F，12/21〕。方案 A 往北退縮〔2 m〕，避開了部分陰影。此比較採用晴空假設與已記錄的鄰棟高度〔→ 輸入來源〕；實際雲量會同時降低兩個方案的日照。',
   ex_note='括號內為示意用的佔位數值；箭頭標示每句話將引用的來源。',
   study='這些說明是否真的有幫助，本身就是研究問題，將在規劃中的使用者研究中檢驗：相同資料與任務，比較有無說明時的判讀正確率、任務時間與決策理由品質。',
   study_link='研究與驗證'),
  b1='我們如何驗證', b2='聯絡我們'),
}


def ai_section(a):
    flow = ''.join(f'<li class="aiflow__step reveal"><span class="loop__n">{n}</span><span class="aiflow__t">{t}</span><p>{d}</p></li>' for n, t, d in a['flow'])
    uses = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in a['uses'])
    rules = ''.join(f'<li>{r}</li>' for r in a['rules'])
    return f'''
<section class="section" style="padding-top:0" id="intelligence">
  <div class="wrap">
    {sheet_head(*a['head'])}
    <div class="grid" style="row-gap:24px;align-items:end;margin-bottom:clamp(36px,4vw,56px)">
      <h2 class="span-6 display d-l">{a['h']}</h2>
      <p class="span-6 body muted" style="max-width:none">{a['intro']}</p>
    </div>
    <ol class="aiflow">{flow}</ol>
    <div class="grid" style="row-gap:40px;margin-top:clamp(48px,6vw,88px);align-items:start">
      <div class="span-7 stack" style="grid-template-columns:repeat(2,minmax(0,1fr))">{uses}</div>
      <div class="span-4 start-9"><p class="mono muted" style="margin-bottom:10px">{a['rules_t']}</p><ul class="ticks">{rules}</ul></div>
    </div>
    <figure class="aiex reveal">
      <figcaption class="aiex__cap"><span class="mono">{a['ex_t']}</span>{stamp('concept', a['ex_stamp'])}</figcaption>
      <p class="aiex__q">{a['ex_q']}</p>
      <p class="aiex__a">{a['ex_a']}</p>
      <p class="mono mono--sm muted">{a['ex_note']}</p>
    </figure>
    <p class="body muted" style="margin-top:28px;max-width:46em">{a['study']} <a class="link" href="research.html">{a['study_link']} <span aria-hidden="true">→</span></a></p>
  </div>
</section>'''


def platform(lang):
    d = PL[lang]
    P = pre(lang)
    S = STAMP[lang]
    side = f'<p class="lede">{d["side_lede"]}</p><div style="display:flex;flex-wrap:wrap;gap:8px">' + ''.join(stamp(k, t) for k, t in d['side_stamps']) + '</div>'
    sh = d['shots']
    mods = ''.join(f'<div class="index__row index__row--mod"><span class="index__no">{n}</span><span class="index__title">{t}</span><span class="muted hide-m">{ds}</span><span>{stamp(k, d["m6_label"] if n == "M6" else S[k])}</span></div>' for n, t, ds, k in d['modules'])
    hz = ''
    for kind, sk, sl, name, desc, items in d['horizons']:
        cls = 'horizon--core' if kind == 'core' else 'horizon--concept'
        hz += f'<article class="horizon {cls}">{stamp(sk, sl).replace("<span", "<span style=\"align-self:flex-start\"", 1)}<h2 class="horizon__name">{name}</h2><p class="muted">{desc}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></article>'
    stack = ''.join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a, b in d['stack'])
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], side)}
<section class="section">
  <div class="wrap">
    {sheet_head(*d['s1'])}
    <div class="grid" style="row-gap:24px;align-items:end;margin-bottom:clamp(40px,5vw,64px)">
      <h2 class="span-7 display d-l">{d['h2']}</h2>
      <p class="span-5 body muted">{d['intro']}</p>
    </div>
    {shot(P, *sh[0])}
    <div class="grid" style="row-gap:40px;margin-top:clamp(40px,5vw,72px);align-items:start">
      {shot(P, *sh[1], cls='span-7')}
      {shot(P, *sh[2], cls='span-5', style='margin-top:clamp(0px,8vw,140px)')}
    </div>
    <div class="grid" style="row-gap:40px;margin-top:clamp(40px,5vw,72px);align-items:start">
      {shot(P, *sh[3], cls='span-5', style='margin-top:clamp(0px,6vw,100px)')}
      {shot(P, *sh[4], cls='span-7')}
    </div>
    <div style="margin-top:clamp(64px,8vw,120px)">{sheet_head(*d['s11'])}</div>
    <div class="index">{mods}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s2'])}
    <div class="horizons">{hz}</div>
  </div>
</section>
{ai_section(d['ai'])}
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s3'])}
    <div class="grid" style="row-gap:40px">
      <div class="span-5"><h2 class="h-statement">{d['stack_h']}</h2><p class="muted" style="margin-top:20px;font-size:15px">{d['sources']}</p></div>
      <div class="span-7 stack" style="grid-template-columns:repeat(2,minmax(0,1fr))">{stack}</div>
    </div>
  </div>
</section>
<section class="dark section--tight">
  <div class="wrap grid" style="row-gap:24px;align-items:center">
    <p class="span-8 h-statement" style="font-size:clamp(20px,2.2vw,30px)">{d['band']}</p>
    <div class="span-4" style="display:flex;flex-wrap:wrap;gap:12px;justify-content:flex-end">
      <a class="btn btn--primary" href="research.html">{d['b1']} <span class="arr" aria-hidden="true">→</span></a>
      <a class="btn btn--ghost" href="contact.html">{d['b2']}</a>
    </div>
  </div>
</section>
</main>
'''
    write(lang, 'platform.html', page(lang, 'platform.html', d['title'], d['desc'], body, active='platform.html', img='assets/img/rsa/solar-shading.webp'))


# ------------------------------------------------------------------ ABOUT
AB = {
 'en': dict(
  title='About — RSA · Responsive Space Architecture',
  desc='About RSA (見築科技): brand and product names, mission, vision, values, the founder’s background and the company’s current status.',
  crumb='About', h1='We understand environments.<br><span style="color:var(--mute-2)">We design the lives within them.</span>',
  side='<p class="lede">An architecture and environmental-technology brand that grew from design practice.</p>',
  s1=('01', 'Names', 'Brand / company / product'),
  names_head=['Layer', 'Name', 'Meaning', 'Status'],
  names=[('Brand &amp; logo', 'RSA', 'The one English brand and logo', 'In use'),
         ('Brand in full', 'Responsive Space Architecture', 'R = Responsive · S = Space · A = Architecture', 'Adopted brand direction'),
         ('Chinese name', '見築科技有限公司', 'Chinese company name', 'In use'),
         ('Product', 'Residential Site Analyzer', 'Research platform for residential site analysis', 'Research prototype, in development'),
         ('Future products', 'RSA Studio · RSA Intelligence', 'Scheme comparison · AI-assisted explanation', 'Concept · Planned')],
  names_note='RSA is the company brand. Residential Site Analyzer is a product name, not the company’s name.',
  s2=('02', 'Story'),
  story_h='Good architecture should not start from form. It should start from understanding where it stands.',
  story=['A site’s sun, its neighbouring buildings, the way heat builds through the day and the habits of the people who use it often decide the quality of a space earlier than any rendering. Architecture is not only form and material; it is a relationship between land, nature, city and daily life.',
         'RSA builds on the founder’s training in spatial design and years in residential development and project coordination. It turns environmental questions that come up in design—and are hard to answer—into research and software. Can a site be understood more clearly before design starts? How should differences between floors, hours and massing options be shown? Can results be explained to people without an engineering background, and do they change the design?',
         'Residential Site Analyzer came out of those questions. It is a research tool in development that combines site geometry, sun and shade, exploratory wind and UTCI-oriented outdoor comfort, and studies how that evidence can support design decisions.',
         'Design brings questions and imagination. Analysis brings evidence and limits. Technology helps them understand each other. RSA wants these three to form a loop, not just sit side by side.'],
  mission_k='Mission', mission='Make environmental knowledge easier to understand and use, so that analysis becomes a real basis for architectural design, early residential planning and environmental improvement.',
  vision_k='Vision', vision='Grow into an architecture-technology brand that connects design, environmental research, data and its own products—building a design workflow that is more sensitive to people and places and more transparent about its methods.',
  s3=('03', 'Values'),
  values=[('Human-centred', '人本', 'Design for the people who will live with the result.'),
          ('Environment-first', '環境優先', 'Understand the site and its climate before form is decided.'),
          ('Evidence-led', '證據導向', 'Every important reading has a basis and limits that can be checked.'),
          ('Clarity', '清晰', 'Translate technical data into meaning without losing accuracy.'),
          ('Integration', '整合', 'Work across architecture, construction, environmental science and software.'),
          ('Integrity', '誠信', 'Never invent validation, results, clients or team size.')],
  s4=('04', 'Founder', 'Chiu Yu-Jyun · 邱禹鈞'),
  founder_h='From spatial design and residential practice to environmental research.',
  founder=['Trained in spatial design at Da-Yeh University and Kun Shan University. Years in residential development: land assessment, early planning, design integration, construction coordination, project management and handover.',
           'Currently studying in the Department of Architecture at National University of Kaohsiung, where the Residential Site Analyzer research continues. Also works in photography and visual storytelling about light, scale and use.'],
  timeline=[('2017 — 2021', 'Spatial design studies', 'Da-Yeh University; Kun Shan University, Dept. of Spatial Design'),
            ('2020 — 2026', 'Residential development', 'Project assistant, then project manager in a construction and development group'),
            ('2026 —', 'Graduate study &amp; RSA', 'National University of Kaohsiung, Dept. of Architecture; Residential Site Analyzer research')],
  founder_note='Academic background is personal. It does not mean any university owns, endorses or partners with RSA.',
  s5=('05', 'Where RSA stands today', 'Status'),
  status=[('real', 'Is', ['An independent brand from Taiwan, led by its founder', 'A working research prototype (Residential Site Analyzer)', 'A research programme with stated questions and validation plans']),
          ('planned', 'Is not yet', ['A commercial software product with paying customers', 'A provider of statutory architect services', 'Certified engineering analysis'])],
  cta='Questions, collaboration or research exchange'),
 'zh': dict(
  title='關於 RSA — 見築科技',
  desc='關於 RSA 見築科技：品牌與產品名稱、使命、願景、核心價值、創辦人背景與目前狀態。',
  crumb='關於', h1='我們理解環境，<br><span style="color:var(--mute-2)">也設計人在其中的生活。</span>',
  side='<p class="lede">從設計實務出發的建築環境科技品牌。</p>',
  s1=('01', '名稱', '品牌 / 公司 / 產品'),
  names_head=['層級', '名稱', '意義', '狀態'],
  names=[('品牌與 Logo', 'RSA', '唯一的英文品牌與 Logo', '使用中'),
         ('品牌全稱', 'Responsive Space Architecture', 'R＝回應 · S＝空間 · A＝建築', '已採用的品牌方向'),
         ('中文名稱', '見築科技有限公司', '中文公司名稱', '使用中'),
         ('產品', 'Residential Site Analyzer', '住宅基地環境分析研究平台', '研究原型，開發中'),
         ('未來產品', 'RSA Studio · RSA Intelligence', '方案比較 · AI 輔助解釋', '概念 · 規劃中')],
  names_note='RSA 是公司品牌；Residential Site Analyzer 是產品名稱，不是公司名稱。',
  s2=('02', '品牌故事'),
  story_h='好的建築不應只從形式開始，而應從理解它所處的環境開始。',
  story=['一塊基地的日照方向、鄰棟量體、時間變化、戶外熱環境，以及人的使用習慣，往往比一張漂亮的透視圖更早決定空間的品質。建築因此不只是形體與材質的組合，更是土地、自然、城市與日常生活之間的關係。',
         'RSA 見築科技承接創辦人的空間設計訓練、住宅開發與專案整合經歷，把設計過程中常見卻難以回答的環境問題，轉化為研究與技術開發的方向。設計前期能否更清楚地理解基地？不同樓層、時間與量體的差異如何呈現？分析結果如何以非工程背景也能理解的方式傳達？這些資訊能否實際改善設計選擇？',
         '由此出發的 Residential Site Analyzer，是一項持續研發中的住宅基地環境分析工具。它研究如何整合基地幾何、日照遮蔭、探索性風環境與 UTCI 導向的戶外熱舒適資訊，並探索分析證據在設計決策中的作用。',
         '設計提供問題與想像，分析提供證據與限制，技術則幫助兩者相互理解。見築科技希望讓這三種能力形成循環，而不只是放在同一家公司裡。'],
  mission_k='使命', mission='使環境知識更容易被理解與應用，讓專業分析成為建築設計、住宅前期規劃與環境改善決策的有效依據。',
  vision_k='願景', vision='發展成能夠連結建築設計、環境研究、資料智慧與自主產品的建築科技品牌，逐步建立對人與場域更敏感、對方法更透明的設計工作流程。',
  s3=('03', '核心價值'),
  values=[('人本', 'Human-centred', '設計關注最終使用者的生活與感知。'),
          ('環境優先', 'Environment-first', '在形式決定前，先理解基地與自然條件。'),
          ('證據導向', 'Evidence-led', '每項重要判讀，都有可檢查的依據與限制。'),
          ('清晰', 'Clarity', '把專業數據轉譯為有意義的資訊，而不犧牲正確性。'),
          ('整合', 'Integration', '跨越建築、營造、環境科學與資訊工程。'),
          ('誠信', 'Integrity', '不偽造驗證、成果、客戶與團隊規模。')],
  s4=('04', '創辦人', '邱禹鈞 · Chiu Yu-Jyun'),
  founder_h='從空間設計與住宅實務，走向環境研究。',
  founder=['曾於大葉大學、崑山科技大學接受空間設計訓練；長期投入住宅開發，經歷土地評估、前期規劃、設計整合、營造協調、專案管理到交屋。',
           '目前就讀國立高雄大學建築學系研究所，並持續 Residential Site Analyzer 的研究。也以攝影與影像敘事觀察光線、尺度與使用痕跡。'],
  timeline=[('2017 — 2021', '空間設計學習', '大葉大學；崑山科技大學 空間設計系'),
            ('2020 — 2026', '住宅開發實務', '營造與建設集團 · 特助、專案經理人'),
            ('2026 —', '研究所與 RSA', '國立高雄大學 建築學系研究所；Residential Site Analyzer 研究')],
  founder_note='學術背景屬創辦人個人經歷，不代表任何大學擁有、背書或與 RSA 正式合作。',
  s5=('05', 'RSA 目前的狀態', '現況'),
  status=[('real', '是', ['由創辦人主導、來自台灣的獨立品牌', '一個真實運作的研究原型（Residential Site Analyzer）', '一個有明確研究問題與驗證計畫的研究']),
          ('planned', '尚不是', ['有付費客戶的商業軟體產品', '提供依法須由建築師執行之簽證業務', '經認證的工程分析'])],
  cta='提問、合作或研究交流'),
}


def about(lang):
    d = AB[lang]
    rows = ''.join(f'<tr><th scope="row">{a}</th><td><strong>{b}</strong></td><td>{c}</td><td class="muted">{s}</td></tr>' for a, b, c, s in d['names'])
    story = ''.join(f'<p>{x}</p>' for x in d['story'])
    values = ''.join(f'<div class="value reveal"><span class="value__n">0{i + 1}</span><h3>{a}</h3><p class="mono mono--sm muted">{b}</p><p>{c}</p></div>' for i, (a, b, c) in enumerate(d['values']))
    tl = ''.join(f'<div class="ledger__row reveal"><span class="ledger__no">{y}</span><p class="ledger__t">{t}</p><p class="ledger__d">{x}</p></div>' for y, t, x in d['timeline'])
    status = ''.join(f'<div class="board__col">{stamp(k, t)}<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for k, t, items in d['status'])
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], d['side'], 'd-l')}
<section class="section">
  <div class="wrap">
    {sheet_head(*d['s1'])}
    <div class="table-wrap"><table class="names">
      <thead><tr>{''.join(f'<th scope="col">{x}</th>' for x in d['names_head'])}</tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
    <p class="naming" style="margin-top:24px;max-width:40em">{d['names_note']}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s2'])}
    <div class="grid" style="row-gap:40px">
      <h2 class="span-6 h-statement">{d['story_h']}</h2>
      <div class="span-5 start-8 body" style="display:flex;flex-direction:column;gap:18px">{story}</div>
    </div>
    <div class="mv">
      <div class="mv__item reveal"><p class="chapter__k"><span class="chapter__l">M</span>{d['mission_k']}</p><p class="h-statement" style="font-size:clamp(22px,2.2vw,32px)">{d['mission']}</p></div>
      <div class="mv__item mv__item--dark reveal"><p class="chapter__k"><span class="chapter__l">V</span>{d['vision_k']}</p><p class="h-statement" style="font-size:clamp(22px,2.2vw,32px)">{d['vision']}</p></div>
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s3'])}
    <div class="values">{values}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s4'])}
    <div class="grid" style="row-gap:32px;margin-bottom:clamp(32px,4vw,56px)">
      <h2 class="span-7 display d-m">{d['founder_h']}</h2>
      <div class="span-5 body muted" style="display:flex;flex-direction:column;gap:14px">{''.join(f'<p>{x}</p>' for x in d['founder'])}</div>
    </div>
    <div class="ledger">{tl}</div>
    <p class="mono mono--sm muted" style="margin-top:16px">{d['founder_note']}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s5'])}
    <div class="board" style="grid-template-columns:1fr 1fr">{status}</div>
    <p style="margin-top:40px"><a class="link" href="contact.html">{d['cta']} <span aria-hidden="true">→</span></a></p>
  </div>
</section>
</main>
'''
    write(lang, 'company.html', page(lang, 'company.html', d['title'], d['desc'], body, active='company.html'))


# ------------------------------------------------------------------ RESEARCH
RS = {
 'en': dict(
  title='Research & Validation — RSA',
  desc='RSA research: how residential site evidence can be translated, understood and used in early design. Research questions, methods, validation layers, data sources, limits and roadmap.',
  crumb='Research', h1='Scientific rigour<br><span style="color:var(--mute-2)">is a design decision.</span>',
  side='<p class="lede">This research is not about building another simulation tool. It asks how residential environmental information can be translated, understood and used in early decisions.</p><p class="mono mono--sm muted">Research brief · 2026 Q4 — 2027 Q4</p>',
  s1=('01', 'Why Kaohsiung', 'Case city'),
  why=[('01', 'A clear climate', 'Long, warm summers, strong sun and humid heat make daylight, ventilation and thermal comfort decisive for housing quality.'),
       ('02', 'Local policy context', 'Kaohsiung has promoted balconies, greening and green design, with local rules still being revised—so environmental analysis could link climate to local housing design.'),
       ('03', 'The research question', 'Can these differences be identified clearly early in design? And can existing housing get traceable evidence for improvement?')],
  s2=('02', 'Research questions', 'RQ1 — RQ3'),
  rq_h='The question is not whether it can compute.<br><span style="color:var(--orange-ink)">It is whether the result can be used.</span>',
  rq_head=['No.', 'Question', 'Validation', 'How it is tested'],
  rq=[('Can environmental differences between floors, times and schemes be identified reliably?', 'Technical', '技術驗證', 'Cross-check shading and calculation error against reference tools.'),
      ('Are the integrated results understood more easily than scattered information?', 'Real cases', '真實案例驗證', 'Check real Kaohsiung sites and surrounding heights; compare A/B schemes under controlled conditions.'),
      ('Does that understanding support better early-stage decisions?', 'Users', '使用者驗證', 'Compare accuracy of reading, task time and quality of reasoning.')],
  s3=('03', 'Method'),
  method=[('Input', 'Define geometry, datasets, model boundaries and input assumptions.'),
          ('Compute', 'Run targeted analyses with methods suited to their stated limits.'),
          ('Verify', 'Compare selected outputs with reference tools and record error measures.'),
          ('Study', 'Investigate understanding through planned user evaluation.')],
  scope_h='One body of evidence, several housing situations.',
  scope=[('Core study', 'New housing', 'Compare layouts, floors and hours to reduce reliance on experience alone in early decisions.'),
         ('Extension', 'Existing housing', 'Identify where and when overheating, weak ventilation or high heat stress occur, as a basis for improvement.')],
  scope_note='Core validation focuses on early decisions for new housing. Existing housing is an application, not a second research topic.',
  s4=('04', 'User study design', 'Planned'),
  us_h='Same data, same task.<br>Only the presentation changes.',
  cond=[('Condition A', 'Scattered information', 'Sun, wind and comfort results shown separately; the participant combines floors, hours and schemes themselves.'),
        ('Condition B', 'RSA integrated evidence', 'Sun, wind and UTCI in one comparison view; floor × time × scheme differences shown directly.')],
  metrics=[('Accuracy', 'Are differences between housing situations identified correctly?'), ('Task time', 'Is comparison and judgement faster?'), ('Reasoning quality', 'Are choices better explained and supported by evidence?')],
  us_note='Planned: a 10–15 person pilot, then a formal study. No results yet.',
  s5=('05', 'Archived validation records', 'r42 / r44'),
  rec_b='These figures come from the r42 and r44 development milestones. They are not proof that newer builds or the full system meet a scientific acceptance threshold. Reproduction requires the benchmark cases, reference environment, test scripts and current code.',
  rec=[('r42', '0.9795', '', 'Shadow IoU vs. Radiance', 'Intersection-over-union against a Radiance direct-shadow reference; three archived cases recorded as pass.'),
       ('r42', '0.25', 'm', 'Hausdorff distance', 'Boundary difference in the same setup; reported area bias about −2.05%.'),
       ('r44', '321', '', 'Regression tests', 'Historically marked PASS. Coverage and applicability to later releases need independent review.')],
  historical='Historical',
  s6=('06', 'Limits &amp; safeguards', 'What we cannot claim'),
  limits=[('Shadow', 'Benchmark-specific', 'Earlier comparisons do not establish accuracy for every date, geometry or current build.'),
          ('Wind', 'Exploratory', 'Not CFD-based pressure or pedestrian-safety evidence.'),
          ('Comfort', 'Input-dependent', 'UTCI results depend on climate inputs, radiation, geometry and modelling assumptions.'),
          ('Boundary', 'In development', 'User studies, full revalidation, repeatability and source checks are ongoing or planned. Claims of certified engineering performance would be premature.')],
  sources='Data sources studied or evaluated: OpenStreetMap, Taiwan NLSC, CWA, ERA5, Open-Meteo. Listing a source does not mean every API is integrated, live or independently validated.',
  s7=('07', 'Roadmap'),
  road=[('Now', 'Integration', 'Consolidate a reproducible core: interface states, site geometry, analysis consistency and evidence records.'),
        ('Next', 'Validation', 'Rerun representative cases with documented reference tools, assumptions and error reporting.'),
        ('Future', 'Human study', 'Test whether traceable explanations and careful AI assistance improve comprehension and decisions.')],
  ext_h='In scope now, and later',
  ext=[('In scope', ['Site-data reliability: parcel, coordinates, boundary, height sources', 'Kaohsiung case completeness and version records', 'Traceable results: sources, parameters and assumptions kept with every output']),
       ('Future extension', ['Rooftop solar potential from sun evidence', 'Indicative PV generation estimates', 'Housing-environment knowledge base and AI explanation'])]),
 'zh': dict(
  title='研究與驗證 — RSA 見築科技',
  desc='RSA 研究：住宅基地環境證據如何被轉譯、理解並用於設計前期。研究問題、方法、驗證層次、資料來源、限制與路線圖。',
  crumb='研究', h1='科學嚴謹，<br><span style="color:var(--mute-2)">也是一種設計決定。</span>',
  side='<p class="lede">本研究並非僅開發另一套模擬工具，而是檢驗住宅環境資訊如何被轉譯、理解，並支援前期決策。</p><p class="mono mono--sm muted">研究簡報 · 2026 Q4 — 2027 Q4</p>',
  s1=('01', '為什麼是高雄', '案例城市'),
  why=[('01', '氣候條件鮮明', '高雄長夏暖冬、日照充足，夏季高溫潮濕；日照、通風與熱舒適因此成為影響住宅環境品質的重要因素。'),
       ('02', '在地制度脈絡', '高雄曾在景觀陽臺、綠化與綠能設計上推動，相關地方細則也持續修訂，讓環境分析有機會連結氣候條件與在地住宅設計。'),
       ('03', '形成研究問題', '這些環境差異能否在設計前期被清楚辨識？既有住宅又能否據此形成可追溯的改善依據？')],
  s2=('02', '研究問題', 'RQ1 — RQ3'),
  rq_h='研究分析系統不是「能不能算」，<br><span style="color:var(--orange-ink)">而是「算完之後能不能被使用」。</span>',
  rq_head=['編號', '研究問題', '驗證層次', '驗證方式'],
  rq=[('不同樓層、時間及方案的環境差異，能否被可靠辨識？', '技術驗證', 'Technical', '以參考工具交叉比對，檢查遮蔭與計算誤差。'),
      ('整合後的環境證據，是否比分散資訊更容易判讀？', '真實案例驗證', 'Real cases', '稽核高雄基地與周邊高度，控制條件比較 A／B 方案。'),
      ('這樣的理解，能否支援更好的前期決策？', '使用者驗證', 'Users', '比較判讀正確率、任務時間與決策理由品質。')],
  s3=('03', '研究方法'),
  method=[('輸入', '定義幾何、資料集、模型邊界與輸入假設。'),
          ('計算', '以適合其限制的方法，進行目標分析。'),
          ('驗證', '將選定結果與參考工具比對，並記錄誤差。'),
          ('研究', '透過規劃中的使用者評估，檢驗理解程度。')],
  scope_h='同一套環境證據，支援多種住宅情境。',
  scope=[('核心研究情境', '新建住宅', '比較不同配置、樓層與時段的環境表現，降低只憑經驗判斷的不確定性。'),
         ('延伸應用情境', '既有住宅', '辨識曝曬過強、通風潛勢不足或熱壓力偏高的位置與時段，作為後續改善的量化依據。')],
  scope_note='核心驗證聚焦新建住宅前期決策；既有住宅作為應用延伸，不擴張為第二個研究主題。',
  s4=('04', '使用者研究設計', '規劃中'),
  us_h='相同資料、相同任務，<br>只改變資訊呈現方式。',
  cond=[('Condition A', '傳統分散資訊', '日照、風環境與熱舒適結果分別呈現；使用者需自行整合樓層、時間與方案差異。'),
        ('Condition B', 'RSA 整合證據介面', '將日照、風環境與 UTCI 整合為一致的比較介面；直接呈現樓層 × 時間 × 方案的環境差異。')],
  metrics=[('判讀正確率', '能否正確辨識不同住宅情境的環境差異？'), ('任務完成時間', '能否更有效率地完成比較與判斷？'), ('決策理由品質', '能否提出更完整、且有環境證據支持的選擇理由？')],
  us_note='規劃：先進行 10–15 人 pilot，再進行正式研究。目前尚無結果。',
  s5=('05', '歷史驗證紀錄', 'r42 / r44'),
  rec_b='以下數據來自 r42 與 r44 開發里程碑，不代表新版或整個系統已達科學驗收標準。重現需要原始基準案例、參考環境、測試腳本與現行程式碼。',
  rec=[('r42', '0.9795', '', '陰影 IoU（對照 Radiance）', '與 Radiance 直接陰影參考之交集聯集比；三個封存案例記錄為通過。'),
       ('r42', '0.25', 'm', 'Hausdorff 距離', '同一設定下的邊界差距；記載面積偏差約 −2.05%。'),
       ('r44', '321', '', '回歸測試', '歷史版本曾記錄通過；涵蓋範圍與對新版的適用性需獨立檢視。')],
  historical='歷史',
  s6=('06', '限制與防護', '我們不能宣稱什麼'),
  limits=[('陰影', '限特定基準', '早期比較不代表每個日期、幾何或現行版本都具同等精度。'),
          ('風環境', '探索性質', '不可作為 CFD 風壓或行人安全的證據。'),
          ('熱舒適', '取決於輸入', 'UTCI 結果取決於氣象輸入、輻射、幾何與模型假設。'),
          ('研究邊界', '開發中', '使用者研究、全面再驗證、重現性與資料來源檢查仍在進行或規劃中；宣稱工程級認證言之過早。')],
  sources='曾研究或評估的資料來源：OpenStreetMap、內政部國土測繪中心（NLSC）、中央氣象署（CWA）、ERA5、Open-Meteo。列出來源不代表每一項皆已完成即時 API 串接或獨立驗證。',
  s7=('07', '路線圖'),
  road=[('現在', '整合', '整合可重現的核心：介面狀態、基地幾何、分析一致性與證據紀錄。'),
        ('下一步', '驗證', '以記錄完整的參考工具、假設與誤差報告，重跑代表性案例。'),
        ('未來', '使用者研究', '檢驗可追溯的解釋與審慎的 AI 輔助，是否能改善理解與決策。')],
  ext_h='論文範圍內，以及之後的延伸',
  ext=[('論文範圍內：必要補強', ['基地資料可靠度：地號、宗地定位、坐標、邊界、高度來源紀錄', '高雄案例完整度與版本紀錄', '結果可追溯：輸出樓層、時間、方案證據，保留來源、參數與假設']),
       ('未來延伸', ['光電設置潛勢：由日照證據找出屋頂候選區域與板面朝向', '附屬發電量估算', '住宅環境知識庫與 AI 解釋'])]),
}


def research(lang):
    d = RS[lang]
    rq = ''.join(f'<div class="rq__row reveal"><span class="rq__no">RQ{n + 1}</span><p class="rq__q">{q}</p><p class="rq__v">{v}<br><span>{v2}</span></p><p class="rq__h">{how}</p></div>' for n, (q, v, v2, how) in enumerate(d['rq']))
    method = ''.join(f'<li class="loop__step reveal"><span class="loop__n">0{i + 1}</span><span class="loop__en">{a}</span><p class="loop__d">{b}</p></li>' for i, (a, b) in enumerate(d['method']))
    scope = ''.join(f'<div class="tech reveal"><p class="mono mono--sm">{k}</p><h3 class="tech__name">{t}</h3><p>{x}</p></div>' for k, t, x in d['scope'])
    cond = ''.join(f'<div class="cond{" cond--b" if i else ""} reveal"><p class="mono mono--sm">{a}</p><h3>{b}</h3><p>{c}</p></div>' for i, (a, b, c) in enumerate(d['cond']))
    metrics = ''.join(f'<div><span class="mono mono--sm orange">0{i + 1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(d['metrics']))
    recs = ''.join(f'<div class="record reveal"><span class="record__ver">{stamp("record", v)}</span><span class="record__val">{val}{f"<small>{u}</small>" if u else ""}</span><div><p class="record__label">{lab}</p><p class="record__note">{note}</p></div><span class="mono mono--sm muted">{d["historical"]}</span></div>' for v, val, u, lab, note in d['rec'])
    limits = ''.join(f'<div><p class="mono mono--sm orange">{b}</p><h3>{a}</h3><p>{c}</p></div>' for a, b, c in d['limits'])
    road = ''.join(f'<div><p class="mono mono--sm muted">{a}</p><h3>{b}</h3><p>{c}</p></div>' for a, b, c in d['road'])
    ext = ''.join(f'<div class="board__col">{stamp("real" if i == 0 else "planned", t)}<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for i, (t, items) in enumerate(d['ext']))
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], d['side'])}
<section class="section">
  <div class="wrap">
    {sheet_head(*d['s1'])}
    {ledger(d['why'])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s2'])}
    <h2 class="display d-l" style="margin-bottom:clamp(40px,5vw,72px)">{d['rq_h']}</h2>
    <div class="rq"><div class="rq__row rq__row--head mono mono--sm muted">{''.join(f'<span>{x}</span>' for x in d['rq_head'])}</div>{rq}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s3'])}
    <ol class="loop loop--4">{method}</ol>
    <h3 class="h-statement" style="margin:clamp(56px,7vw,96px) 0 28px">{d['scope_h']}</h3>
    <div class="techs techs--2">{scope}</div>
    <p class="mono mono--sm muted" style="margin-top:16px">{d['scope_note']}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s4'])}
    <h2 class="display d-l" style="margin-bottom:clamp(36px,4vw,56px)">{d['us_h']}</h2>
    <div class="conds">{cond}<span class="conds__vs mono" aria-hidden="true">vs</span></div>
    <div class="stack" style="grid-template-columns:repeat(3,minmax(0,1fr));margin-top:32px">{metrics}</div>
    <p class="note-line" style="margin-top:20px">{stamp('planned', STAMP[lang]['planned'])}<span>{d['us_note']}</span></p>
  </div>
</section>
<section id="validation" class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s5'])}
    <p class="body muted" style="margin-bottom:32px;max-width:48em">{d['rec_b']}</p>
    <div class="records">{recs}</div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s6'])}
    <div class="limits">{limits}</div>
    <p class="muted" style="margin-top:20px;font-size:15px;max-width:52em">{d['sources']}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s7'])}
    <div class="roadmap">{road}</div>
    <h3 class="h-card" style="margin:clamp(48px,6vw,80px) 0 20px">{d['ext_h']}</h3>
    <div class="board" style="grid-template-columns:1fr 1fr">{ext}</div>
  </div>
</section>
</main>
'''
    write(lang, 'research.html', page(lang, 'research.html', d['title'], d['desc'], body, active='research.html', img='assets/img/rsa/utci.webp'))


# ------------------------------------------------------------------ CONTACT
CT = {
 'en': dict(title='Contact — RSA', desc='Contact RSA about site analysis, environmental evidence, research collaboration or early design questions: research@rsa-analyzer.com',
   crumb='Contact', h1='Better questions.<br><span style="color:var(--mute-2)">Better places.</span>',
   side='<p class="lede">Write to us about a site, a research question or a possible collaboration.</p>',
   copy='Copy address', copied='Copied',
   s1=('01', 'What to write about'),
   topics=[('01', 'Site &amp; early design questions', 'Sun, shade, neighbouring massing or outdoor comfort on a residential site you are considering.'),
           ('02', 'Research collaboration', 'Reproducibility, validation cases, user studies, or translating environmental evidence for design.'),
           ('03', 'Technology &amp; data', 'GIS, climate data and software teams interested in site-analysis workflows.'),
           ('04', 'Teaching &amp; exchange', 'Researchers, students and educators working on design and environment.')],
   s2=('02', 'Good to know'),
   notes=['RSA is an early-stage brand. Residential Site Analyzer is a research prototype, not a commercial product.',
          'RSA does not provide statutory architect services or certified engineering analysis.',
          'Include the site location, the question and any drawings you can share. We reply by email.']),
 'zh': dict(title='聯絡 — RSA 見築科技', desc='就基地分析、環境證據、研究合作或設計前期問題聯絡 RSA：research@rsa-analyzer.com',
   crumb='聯絡', h1='更好的提問，<br><span style="color:var(--mute-2)">更好的場所。</span>',
   side='<p class="lede">歡迎就基地、研究問題或合作可能與我們聯絡。</p>',
   copy='複製信箱', copied='已複製',
   s1=('01', '可以聊什麼'),
   topics=[('01', '基地與設計前期問題', '你正在評估的住宅基地：日照、遮蔭、鄰棟量體或戶外熱舒適。'),
           ('02', '研究合作', '重現性、驗證案例、使用者研究，或環境證據如何轉譯給設計使用。'),
           ('03', '技術與資料', '對基地分析流程有興趣的 GIS、氣象資料與軟體團隊。'),
           ('04', '教學與交流', '關注設計與環境的研究者、學生與教育者。')],
   s2=('02', '先說明'),
   notes=['RSA 是發展初期的品牌；Residential Site Analyzer 是研究原型，並非商業產品。',
          'RSA 不提供依法須由建築師執行之簽證業務，也不提供經認證的工程分析。',
          '來信請附上基地位置、想釐清的問題，以及可分享的圖面。我們會以電子郵件回覆。']),
}


def contact(lang):
    d = CT[lang]
    notes = ''.join(f'<li>{x}</li>' for x in d['notes'])
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], d['side'])}
<section class="section">
  <div class="wrap">
    <a class="contact__mail" href="mailto:{SITE['email']}">{SITE['email']}</a>
    <p style="margin-top:24px"><button class="btn btn--ghost" type="button" data-copy="{SITE['email']}" data-done="{d['copied']}">{d['copy']}</button></p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s1'])}
    {ledger(d['topics'])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    {sheet_head(*d['s2'])}
    <ul class="ticks" style="max-width:44em">{notes}</ul>
  </div>
</section>
</main>
'''
    write(lang, 'contact.html', page(lang, 'contact.html', d['title'], d['desc'], body, active='contact.html'))


# ------------------------------------------------------------------ PRIVACY
PV = {
 'en': dict(title='Privacy — RSA', desc='How rsa-analyzer.com handles data: no accounts, forms, cookies or analytics.',
   crumb='Privacy', h1='Privacy', side='<p class="mono mono--sm muted">Last updated: October 2026</p>',
   items=[('What this site collects', 'This is a static website. It has no accounts, no forms, no cookies and no analytics or advertising trackers.'),
          ('Hosting &amp; network', 'The site is hosted on GitHub Pages and the domain is managed through Cloudflare. These services may process technical data such as your IP address in their server logs to deliver and protect the site. See the GitHub and Cloudflare privacy statements.'),
          ('Fonts', 'Typefaces are loaded from Google Fonts, so your browser sends a request, including your IP address, to Google. See Google’s privacy policy.'),
          ('Email', 'If you write to research@rsa-analyzer.com, we use your address and message only to reply. We do not share or sell them. Ask us and we will delete your correspondence.'),
          ('Between visits', 'The site stores nothing in your browser and remembers nothing about you between visits.'),
          ('Contact', 'Questions about privacy: research@rsa-analyzer.com.')]),
 'zh': dict(title='隱私 — RSA 見築科技', desc='rsa-analyzer.com 如何處理資料：無帳號、無表單、無 Cookie、無分析追蹤。',
   crumb='隱私', h1='隱私說明', side='<p class="mono mono--sm muted">最後更新：2026 年 10 月</p>',
   items=[('本站蒐集什麼', '本站為靜態網站，沒有會員帳號、表單、Cookie，也沒有分析或廣告追蹤工具。'),
          ('主機與網路', '本站由 GitHub Pages 託管，網域經由 Cloudflare 管理。為了傳送與保護網站，這些服務可能在伺服器紀錄中處理您的 IP 位址等技術資料，詳見 GitHub 與 Cloudflare 的隱私權聲明。'),
          ('字型', '網站字型由 Google Fonts 載入，您的瀏覽器會向 Google 發出請求（包含 IP 位址），詳見 Google 隱私權政策。'),
          ('電子郵件', '若您寫信至 research@rsa-analyzer.com，我們只會使用您的信箱與內容回覆，不會分享或出售。您可要求我們刪除往來信件。'),
          ('跨次造訪', '本站不在您的瀏覽器中儲存資料，也不會在造訪之間記住任何關於您的資訊。'),
          ('聯絡', '隱私相關問題：research@rsa-analyzer.com。')]),
}


def privacy(lang):
    d = PV[lang]
    items = ''.join(f'<div class="ledger__row"><span class="ledger__no">0{i + 1}</span><p class="ledger__t">{a}</p><p class="ledger__d">{b}</p></div>' for i, (a, b) in enumerate(d['items']))
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], d['side'])}
<section class="section"><div class="wrap"><div class="ledger">{items}</div></div></section>
</main>
'''
    write(lang, 'privacy.html', page(lang, 'privacy.html', d['title'], d['desc'], body))


# ------------------------------------------------------------------ 404
def notfound(lang):
    t = ('Page not found — RSA', 'Sheet missing.', 'This page is not in the drawing set. It may have moved in the redesign.', 'Back to home') if lang == 'en' else \
        ('找不到頁面 — RSA', '圖紙遺失。', '這一頁不在圖面集中，可能已在改版時移動。', '回到首頁')
    body = f'''
<main id="main">
<section class="section">
  <div class="wrap">
    <p class="mono muted">404</p>
    <h1 class="display d-xxl" style="margin:16px 0 28px">{t[1]}</h1>
    <p class="lede">{t[2]}</p>
    <p style="margin-top:28px"><a class="btn btn--primary" href="/{"" if lang == "en" else "zh/"}">{t[3]} <span class="arr" aria-hidden="true">→</span></a></p>
  </div>
</section>
</main>
'''
    import re
    doc = page(lang, '404.html', t[0], t[2], body)
    # GitHub Pages serves /404.html for any missing path, so every local reference must be root-absolute.
    doc = doc.replace('href="zh/404.html"', 'href="/zh/"')
    doc = re.sub(r'(href|src)="(?!https?:|/|#|mailto:)([^"]+)"', r'\1="/\2"', doc)
    write(lang, '404.html', doc)


def build_all():
    for lang in ('en', 'zh'):
        platform(lang); about(lang); research(lang); contact(lang); privacy(lang)
    notfound('en')
