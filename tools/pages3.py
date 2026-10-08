# -*- coding: utf-8 -*-
"""Expertise and Notes pages — EN + ZH."""
from build import page, write, sheet_head, stamp, pre, e, STAMP, SITE
from pages2 import pagehead, ledger

# ------------------------------------------------------------------ EXPERTISE
EX = {
 'en': dict(
  title='Expertise — RSA · Design, Environment, Technology',
  desc='RSA works across three connected disciplines: architectural and spatial design research, site environmental analysis and decision support, and its own software and AI research.',
  crumb='Expertise', h1='Three disciplines.<br><span style="color:var(--mute-2)">One loop.</span>',
  side='<p class="lede">Design raises the question, analysis builds the evidence, technology connects them—and the result goes back into design.</p>',
  pillars=[
   dict(l='D', k='RSA Design', name='Architecture &amp; spatial design research', img=('corner-reading', 'Corner Library: timber lattice reading structure with people seated at different heights', 'Corner Library · founder’s academic design · visualisation'),
        lead='Designing buildings, and rethinking how life happens in them.',
        value='Spatial concepts, site layout and massing, early residential planning, façade and material strategy, design visualisation and cross-team design integration.',
        scope=['Spatial &amp; architectural concepts', 'Site layout &amp; massing', 'Early residential planning', 'Façade &amp; material strategy', 'Design visualisation &amp; integration'],
        now=('real', 'Founder’s experience', 'Shown through the founder’s academic work and prior residential projects, credited by role.'),
        limit='RSA does not provide statutory architect services; work that legally requires a licensed architect stays with licensed professionals.',
        link=('work.html', 'See the work')),
   dict(l='E', k='RSA Environment', name='Site environmental analysis &amp; decision support', img=('solar-shading', 'RSA prototype: time-based 3D solar and shading view', 'Residential Site Analyzer · real screenshot'),
        lead='Making invisible site conditions into design evidence you can read.',
        value='Site and neighbouring context, sun position, sun and shade over time, differences between floors, exploratory wind, UTCI-oriented thermal comfort, traceable reports and scheme comparison.',
        scope=['Site &amp; neighbouring massing', 'Sun, shade &amp; time', 'Floor-by-floor differences', 'Exploratory wind', 'UTCI-oriented comfort', 'A/B scheme comparison'],
        now=('explore', 'Research prototype', 'Real research software and interface. Not every module is externally validated; no engineering-grade reliability is promised.'),
        limit='Analysis should return to design questions, risks and uncertainty—not end as attractive charts.',
        link=('platform.html', 'Inside the platform')),
   dict(l='T', k='RSA Technology', name='Own software &amp; AI research', img=('massing', 'RSA prototype: massing editor with Scheme A outlined', 'Residential Site Analyzer · real screenshot'),
        lead='Tools that explain the environment, built from design questions.',
        value='Residential Site Analyzer (Python / Streamlit prototype), more consistent 2D/3D views, floor and time mapping, scheme comparison, report generation, GIS and parcel data, and sourced AI explanation.',
        scope=['Residential Site Analyzer', '2D / 3D consistency', 'Floor &amp; time mapping', 'Reports &amp; evidence records', 'GIS / parcel data (assessment)', 'AI explanation (planned)'],
        now=('planned', 'In development · AI planned', 'The prototype exists; RSA Studio is a concept and RSA Intelligence (Claude API) is planned, not deployed.'),
        limit='AI may only organise and explain analysis evidence that has a source. It never invents results and never replaces physical simulation.',
        link=('research.html', 'Research &amp; validation')),
  ],
  s_scen=('04', 'Where it helps', 'Intended scenarios, not client records'),
  scen=[('01', 'Site selection', 'Understand surrounding massing and sun before a site is committed to.'),
        ('02', 'Concept &amp; layout', 'Spot sun, wind and heat questions that deserve deeper study.'),
        ('03', 'Scheme review', 'Compare evidence-backed differences floor by floor and hour by hour.'),
        ('04', 'Reporting', 'Turn technical indicators into information a team can decide with.'),
        ('05', 'Research &amp; teaching', 'Reproduce cases and test whether environmental translation helps.')],
  who='Possible collaborators: architecture and spatial design teams, residential developers, construction and early-planning teams, environmental consultants, researchers and universities, GIS / climate / software teams.',
  cta='Discuss a project'),
 'zh': dict(
  title='專業領域 — RSA 見築科技 · 設計、環境、技術',
  desc='RSA 的三個主軸：建築與空間設計研究、基地環境分析與決策支援、自主軟體與 AI 研究。',
  crumb='專業領域', h1='三個主軸，<br><span style="color:var(--mute-2)">一個循環。</span>',
  side='<p class="lede">設計提出問題，分析建立證據，技術連結兩者——結果再回到設計。</p>',
  pillars=[
   dict(l='D', k='RSA Design · 設計研究', name='建築與空間設計研究', img=('corner-reading', '角落圖書館：木格構閱讀架，人們坐在不同高度', '角落圖書館 · 創辦人學術設計 · 設計模擬圖'),
        lead='不只設計建築，也重新思考空間與生活。',
        value='建築與空間概念、基地配置與量體、住宅前期規劃、立面與材料策略、3D 設計視覺化與跨部門設計整合。',
        scope=['建築與空間概念', '基地配置與量體', '住宅前期規劃', '立面與材料策略', '設計視覺化與整合'],
        now=('real', '創辦人經歷', '以創辦人的學術作品與過往住宅專案呈現，並依實際角色標示。'),
        limit='RSA 不提供依法須由建築師執行之簽證業務；依法須由建築師辦理者，仍由具資格者執行。',
        link=('work.html', '看作品')),
   dict(l='E', k='RSA Environment · 環境分析', name='基地環境分析與決策支援', img=('solar-shading', 'RSA 原型：3D 日照遮蔭畫面', 'Residential Site Analyzer · 真實截圖'),
        lead='讓看不見的環境條件，成為看得懂的設計依據。',
        value='基地與鄰棟條件、太陽位置、日照遮蔭與時間變化、樓層差異、風環境探索、UTCI 熱舒適研究、可追溯報告與方案比較。',
        scope=['基地與鄰棟量體', '日照、遮蔭與時間', '樓層差異', '探索性風環境', 'UTCI 熱舒適', 'A／B 方案比較'],
        now=('explore', '研究原型', '有實際研究程式與介面；並非所有模組都經外部驗證，未承諾工程級可靠度。'),
        limit='分析不應只產生漂亮圖表，而要回到設計問題、風險、不確定性與具體的比較依據。',
        link=('platform.html', '深入技術平台')),
   dict(l='T', k='RSA Technology · 軟體與 AI', name='自主軟體與 AI 研究', img=('massing', 'RSA 原型：量體編輯，方案 A 以紅框標示', 'Residential Site Analyzer · 真實截圖'),
        lead='從設計問題出發，打造能解釋環境的工具。',
        value='Residential Site Analyzer（Python／Streamlit 原型）、更一致的 2D／3D 視覺、樓層與時間對應、方案比較、報告生成、GIS 與地籍資料串接、有來源的 AI 解釋。',
        scope=['Residential Site Analyzer', '2D／3D 一致性', '樓層與時間對應', '報告與證據紀錄', 'GIS／地籍資料（評估中）', 'AI 解釋（規劃中）'],
        now=('planned', '開發中 · AI 規劃中', '原型已存在；RSA Studio 為概念，RSA Intelligence（Claude API）規劃中、尚未部署。'),
        limit='AI 只能整理與解釋有來源的分析證據；不憑空產生結果，也不取代物理模擬。',
        link=('research.html', '研究與驗證')),
  ],
  s_scen=('04', '可以幫上忙的情境', '預期情境，非客戶紀錄'),
  scen=[('01', '基地挑選', '在決定基地之前，先理解周邊量體與日照條件。'),
        ('02', '概念與配置', '辨識值得深入分析的日照、風與熱舒適問題。'),
        ('03', '方案檢討', '逐層、逐時比較有資料支持的設計差異。'),
        ('04', '報告與溝通', '把技術指標轉成團隊可以據以決策的資訊。'),
        ('05', '研究與教學', '重現案例，檢驗環境資訊轉譯是否真的有幫助。')],
  who='潛在合作對象：建築／空間設計團隊、住宅開發商、營造與前期規劃團隊、建築環境顧問、研究者與大學、GIS／氣象／軟體技術團隊。',
  cta='交流合作'),
}


def expertise(lang):
    d = EX[lang]
    P = pre(lang)
    blocks = ''
    for i, x in enumerate(d['pillars']):
        src = f"{P}assets/img/work/{x['img'][0]}.webp" if x['l'] == 'D' else f"{P}assets/img/rsa/{x['img'][0]}.webp"
        frame = 'fig__img ratio-43' if x['l'] == 'D' else 'viewer__frame'
        flip = ' pillar--flip' if i % 2 else ''
        dark = ' dark' if x['l'] == 'E' else ''
        k, t, note = x['now']
        blocks += f'''
<section class="section pillar{flip}{dark}" id="{x['k'].split()[1].lower()}">
  <div class="wrap">
    {sheet_head('0' + str(i + 1), x['k'], x['name'])}
    <div class="pillar__grid">
      <figure class="fig pillar__fig reveal"><div class="{frame}"{' style="border-color:var(--line)"' if frame == 'viewer__frame' and not dark else ''}><img src="{src}" loading="lazy" alt="{e(x['img'][1])}"></div><figcaption class="fig__cap"><span class="mono">{x['img'][2]}</span></figcaption></figure>
      <div class="pillar__text reveal">
        <p class="chapter__k"><span class="chapter__l">{x['l']}</span>{x['k']}</p>
        <h2 class="display d-m">{x['lead']}</h2>
        <p class="body{' muted' if not dark else ''}" style="{'color:var(--dark-mute)' if dark else ''}">{x['value']}</p>
        <ul class="ticks">{''.join(f'<li>{s}</li>' for s in x['scope'])}</ul>
        <div class="pillar__now">{stamp(k, t)}<p>{note}</p></div>
        <p class="mono mono--sm{' muted' if not dark else ''}" style="{'color:var(--dark-mute)' if dark else ''}">{x['limit']}</p>
        <p><a class="link" href="{x['link'][0]}">{x['link'][1]} <span aria-hidden="true">→</span></a></p>
      </div>
    </div>
  </div>
</section>'''
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], d['side'])}
{blocks}
<section class="section">
  <div class="wrap">
    {sheet_head(*d['s_scen'])}
    {ledger(d['scen'])}
    <p class="muted" style="margin-top:24px;max-width:52em">{d['who']}</p>
    <p style="margin-top:32px"><a class="btn btn--primary" href="contact.html">{d['cta']} <span class="arr" aria-hidden="true">→</span></a></p>
  </div>
</section>
</main>
'''
    write(lang, 'expertise.html', page(lang, 'expertise.html', d['title'], d['desc'], body, active='expertise.html', img='assets/img/work/960/corner-exterior.webp'))


# ------------------------------------------------------------------ NOTES
NT = {
 'en': dict(
  title='Notes — RSA research log',
  desc='Short, dated notes on RSA’s research, software versions, validation and website—what changed and what it means.',
  crumb='Notes', h1='Research<br><span style="color:var(--mute-2)">notes.</span>',
  side='<p class="lede">A dated log of what changed: versions, validation, studies and this website. Newest first.</p>',
  entries=[
   ('2026-10-09', 'Website', 'A new website for RSA · Responsive Space Architecture',
    'RSA now presents itself as an architecture and environmental-technology brand, with Residential Site Analyzer as its research platform. The site is bilingual and marks every claim about the software as real, exploratory, historical, planned or concept.',
    ('index.html', 'Home')),
   ('2026-10', 'Research', 'Research brief: Kaohsiung case and a three-layer validation plan',
    'The current study asks whether integrated environmental evidence is understood and used better than scattered information. It plans technical cross-checks, a real Kaohsiung site case and a user study comparing accuracy, task time and quality of reasoning. Planned period: 2026 Q4 to 2027 Q4.',
    ('research.html', 'Research &amp; validation')),
   ('Archive', 'Record', 'r42 / r44 validation records',
    'Earlier builds recorded a shadow IoU of 0.9795 and a Hausdorff distance of 0.25 m against a Radiance direct-shadow reference (r42), and 321 passing regression tests (r44). These are version-specific records, not current certification.',
    ('research.html#validation', 'See the records')),
  ],
  more='New notes will be added as versions are released and validation results come in.'),
 'zh': dict(
  title='研究日誌 — RSA 見築科技',
  desc='RSA 研究、軟體版本、驗證與網站的短篇紀錄：改了什麼、代表什麼。',
  crumb='研究日誌', h1='研究<br><span style="color:var(--mute-2)">日誌。</span>',
  side='<p class="lede">依日期記錄的變化：版本、驗證、研究與網站。最新在前。</p>',
  entries=[
   ('2026-10-09', '網站', 'RSA 見築科技新網站上線',
    'RSA 以建築環境科技品牌的身分對外呈現，Residential Site Analyzer 為旗下研究平台。網站中英雙語，所有關於軟體的說法都標示為真實、探索中、歷史紀錄、規劃中或概念。',
    ('index.html', '首頁')),
   ('2026-10', '研究', '研究簡報：高雄案例與三層驗證計畫',
    '目前研究在問：整合後的環境證據，是否比分散資訊更容易被理解與使用？計畫包含技術交叉比對、高雄真實基地案例，以及比較判讀正確率、任務時間與決策理由品質的使用者研究。規劃期間：2026 Q4 至 2027 Q4。',
    ('research.html', '研究與驗證')),
   ('封存', '紀錄', 'r42／r44 驗證紀錄',
    '早期版本曾記錄：對照 Radiance 直接陰影參考的陰影 IoU 0.9795、Hausdorff 距離 0.25 m（r42），以及 321 項回歸測試通過（r44）。皆為特定版本紀錄，非現行認證。',
    ('research.html#validation', '查看紀錄')),
  ],
  more='之後每次版本發布與驗證結果出爐，都會在這裡新增一則。'),
}


def notes(lang):
    d = NT[lang]
    items = ''.join(f'''
      <article class="note reveal">
        <div class="note__meta"><span class="mono">{date}</span><span class="stamp stamp--{'record' if tag in ('Record', '紀錄') else 'real'}">{tag}</span></div>
        <div><h2 class="note__t">{t}</h2><p class="note__b">{b}</p><p><a class="link" href="{href}">{lab} <span aria-hidden="true">→</span></a></p></div>
      </article>''' for date, tag, t, b, (href, lab) in d['entries'])
    body = f'''
<main id="main">
{pagehead(lang, d['crumb'], d['h1'], d['side'])}
<section class="section">
  <div class="wrap">
    <div class="notes">{items}
    </div>
    <p class="mono mono--sm muted" style="margin-top:24px">{d['more']}</p>
  </div>
</section>
</main>
'''
    write(lang, 'notes.html', page(lang, 'notes.html', d['title'], d['desc'], body, active='notes.html', img='assets/img/rsa/utci.webp'))


def build_all():
    for lang in ('en', 'zh'):
        expertise(lang)
        notes(lang)
