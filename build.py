"""Render the static workshop page from editable, public event metadata."""
import json
from pathlib import Path
from html import escape as e

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
URL = 'https://hyy2566.github.io/icra-workshop-6th-sai-2027/'

def speaker_card(s):
    photo = f'<img class="speaker-photo" src="{e(s["image"])}" alt="{e(s["name"])}" width="360" height="360" loading="lazy">'
    if not (ROOT / s['image']).is_file():
        initials = ''.join(n[0] for n in s['name'].split()[:2])
        photo = f'<div class="profile-placeholder" aria-hidden="true">{e(initials)}</div>'
    return f'''<article class="speaker" id="speaker-{s['id']}">
    <a href="{e(s['url'])}" target="_blank" rel="noopener noreferrer" aria-label="{e(s['name'])}: official profile (opens in a new tab)">{photo}</a>
    <h3><a href="{e(s['url'])}" target="_blank" rel="noopener noreferrer">{e(s['name'])}<span class="arrow" aria-hidden="true">↗</span></a></h3>
    <p class="affiliation">{e(s['affiliation'])}</p><p class="country">{e(s['country'])}</p>
    <p class="talk">Invited talk with Q&amp;A<br>Title to be announced</p></article>'''

def schedule(session, title, anchor):
    rows = []
    for r in data['programme']:
        if r['session'] not in session:
            continue
        rows.append(f'''<tr class="{r.get('type','talk')}"><td>{r['start']} – {r['end']}</td><td><span class="session-title">{e(r['title'])}</span><span class="session-detail">{e(r['detail'])}</span></td></tr>''')
    return f'''<table class="schedule" id="{anchor}"><caption>{title}</caption><thead><tr><th scope="col">Time (KST · UTC+9)</th><th scope="col">Session</th></tr></thead><tbody>{''.join(rows)}</tbody></table>'''

organizers = []
for person in data['organizers']:
    role = f'<span class="role">{e(person["role"])}</span>' if person.get('role') else ''
    organizers.append(f'''<article class="organizer"><h3>{e(person['name'])}{role}</h3><p>{e(person['affiliation'])}</p><a href="mailto:{e(person['email'])}">{e(person['email'])}</a></article>''')

editions = ''.join(f'''<a class="edition" href="{e(r['url'])}" target="_blank" rel="noopener noreferrer"><span class="edition-no">{r['edition']}</span><span class="year">{r['year']}<small>{r['conference']}</small></span><strong>{e(r['title'])}</strong><span class="arrow" aria-hidden="true">↗</span></a>''' for r in data['editions'])

hero_svg = '''<svg viewBox="0 0 520 450" role="img" aria-labelledby="diagram-title diagram-description" xmlns="http://www.w3.org/2000/svg">
<title id="diagram-title">Connecting robot assistance, digital twins and human agency</title>
<desc id="diagram-description">A robot arm and its dashed digital twin are connected to a human operator. Evaluation links model predictions, physical outcomes and operator experience.</desc>
<defs><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M 28 0 L 0 0 0 28" fill="none" stroke="#34505e" stroke-width=".6"/></pattern><linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#e4ece8"/><stop offset="1" stop-color="#7c9a9e"/></linearGradient></defs>
<rect x="25" y="20" width="470" height="402" fill="url(#grid)"/>
<circle cx="270" cy="224" r="155" fill="none" stroke="#46616e" stroke-dasharray="3 9"/><circle cx="270" cy="224" r="111" fill="none" stroke="#34505e"/>
<path d="M91 332 L182 176 L299 202 L344 268" fill="none" stroke="#7edbcc" stroke-width="22" stroke-linejoin="round" opacity=".12"/>
<path d="M91 332 L182 176 L299 202 L344 268" fill="none" stroke="#7edbcc" stroke-width="2" stroke-dasharray="7 6"/>
<circle cx="182" cy="176" r="20" fill="#102c3b" stroke="#7edbcc" stroke-width="1.5" stroke-dasharray="5 4"/><circle cx="299" cy="202" r="14" fill="#102c3b" stroke="#7edbcc" stroke-width="1.5" stroke-dasharray="4 3"/>
<path d="M103 337 L174 202 L278 229 L308 287" fill="none" stroke="#66838d" stroke-width="34" stroke-linejoin="round"/>
<path d="M103 337 L174 202 L278 229 L308 287" fill="none" stroke="url(#metal)" stroke-width="23" stroke-linejoin="round"/>
<circle cx="174" cy="202" r="22" fill="#193e4e" stroke="#d2e3dd" stroke-width="5"/><circle cx="174" cy="202" r="7" fill="#7edbcc"/><circle cx="278" cy="229" r="17" fill="#193e4e" stroke="#d2e3dd" stroke-width="4"/><circle cx="278" cy="229" r="5" fill="#7edbcc"/>
<path d="M297 287 L295 310 L311 322 M319 277 L334 295 L330 314" fill="none" stroke="#d5e6df" stroke-width="7" stroke-linecap="round"/>
<path d="M68 359 L139 359 L129 337 L80 337 Z" fill="url(#metal)"/><path d="M56 366 H151" stroke="#d4e5de" stroke-width="3"/>
<path d="M284 349 L313 334 L342 350 L313 367 Z M284 349 V377 L313 393 V367 M342 350 V378 L313 393" fill="none" stroke="#fa8a70" stroke-width="2"/>
<path d="M359 145 C374 126 397 120 418 131 C440 143 443 173 429 189 L426 208 M361 146 C347 165 351 181 361 194 L366 214 M356 232 C379 213 414 212 436 232" fill="none" stroke="#f4ad91" stroke-width="2.5" stroke-linecap="round"/>
<path d="M375 149 C389 137 414 141 421 155 M376 160 H401 M380 176 C389 181 400 181 410 173" fill="none" stroke="#f4ad91" stroke-width="1.3"/>
<path d="M420 276 C415 281 407 290 405 303 L397 322 C390 335 391 351 401 356 C411 361 421 352 428 341 L444 314" fill="none" stroke="#f4ad91" stroke-width="2"/>
<path d="M405 303 L401 280 C400 273 408 272 411 277 L419 296 L440 270 C445 264 452 269 448 275 L432 301 M442 290 L458 277 C464 273 469 279 463 285 L446 302 M453 299 L466 290 C471 287 475 294 470 298 L452 316" fill="none" stroke="#f4ad91" stroke-width="2" stroke-linecap="round"/>
<path d="M343 235 C355 251 360 273 357 293" fill="none" stroke="#7edbcc" stroke-width="1.5" stroke-dasharray="4 5"/>
<path d="M357 293 L353 284 M357 293 L363 286" fill="none" stroke="#7edbcc" stroke-width="1.5"/>
<circle cx="332" cy="112" r="4" fill="#7edbcc"/><path d="M328 112 H253 L228 141" fill="none" stroke="#7edbcc" stroke-width="1"/><text x="86" y="99" fill="#a7ddd1" font-family="Arial,sans-serif" font-size="11" letter-spacing="1">DIGITAL TWIN</text><path d="M94 109 H207 L220 143" stroke="#7edbcc" fill="none" stroke-width="1"/>
<text x="43" y="407" fill="#c4d7d9" font-family="Arial,sans-serif" font-size="10" letter-spacing="1">PHYSICAL OUTCOMES</text>
<text x="339" y="99" fill="#ffc5ae" font-family="Arial,sans-serif" font-size="11" letter-spacing="1">HUMAN AGENCY</text>
<rect x="36" y="139" width="108" height="29" rx="14" fill="#1d4553" stroke="#4c797c"/><text x="90" y="158" text-anchor="middle" fill="#c9ede5" font-family="Arial,sans-serif" font-size="10">Predict · Compare</text>
<rect x="348" y="376" width="138" height="29" rx="14" fill="#4a4341" stroke="#8a6659"/><text x="417" y="395" text-anchor="middle" fill="#f7d2c2" font-family="Arial,sans-serif" font-size="10">Understand · Override</text>
</svg>'''

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(data['title'])} | ICRA 2027 Workshop Proposal</title>
<meta name="description" content="Proposed ICRA 2027 workshop in Seoul on evaluating adaptive robotic assistance through digital twins and human agency. Speakers, tentative programme, contribution plans and organizers.">
<meta name="theme-color" content="#102c3b"><link rel="canonical" href="{URL}"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:title" content="6th Sensorimotor-Augmented Interaction · ICRA 2027"><meta property="og:description" content="Evaluating Adaptive Assistance through Digital Twins and Human Agency. Proposed full-day workshop, Seoul, May 2027."><meta property="og:url" content="{URL}">
<link rel="stylesheet" href="style.css"><script src="site.js" defer></script><noscript><style>.menu-toggle{{display:none}}@media(max-width:800px){{.site-header{{height:auto;position:static}}.header-inner{{flex-wrap:wrap;padding-block:18px}}.nav{{display:flex;position:static;padding:0;border:0}}}}</style></noscript></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="#home" aria-label="6th Sensorimotor-Augmented Interaction home"><span class="brand-mark">6</span><span class="brand-text">Sensorimotor Interaction<small>ICRA 2027 · SEOUL</small></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu +</button>
<nav class="nav" id="main-nav" aria-label="Main navigation"><a href="#about">About</a><a href="#speakers">Speakers</a><a href="#programme">Programme</a><a href="#contribute">Contribute</a><a href="#organizers">Organizers</a><a class="nav-contact" href="#contact">Contact ↗</a></nav></div></header>
<main id="main">
<section class="hero" id="home"><div class="wrap"><div class="hero-grid"><div>
<span class="eyebrow hero-kicker">Sixth edition · Proposed ICRA 2027 workshop</span>
<h1><span>Sensorimotor-</span><span>Augmented</span><span>Interaction.</span></h1>
<p class="subtitle">Evaluating Adaptive Assistance through Digital Twins and Human Agency</p>
<p class="intro">When should robotic assistance act, ask, or yield? Bringing physical performance and the operator’s experience into the same conversation.</p>
<div class="actions"><a class="button primary" href="#programme">Explore the programme <span aria-hidden="true">↘</span></a><a class="button secondary" href="#contribute">Contribution plans <span aria-hidden="true">↗</span></a></div></div>
<div class="hero-visual"><div class="visual-top"><span>Human ↔ Robot</span><span>Evaluation in the loop</span></div>{hero_svg}<div class="visual-bottom"><span class="visual-dot" aria-hidden="true"></span>Connecting model predictions, physical outcomes<br>and operator experience.</div></div></div>
<div class="event-strip"><div><strong>Seoul, Republic of Korea</strong><small>ICRA 2027 · Coex Convention &amp; Exhibition Center</small></div><div><strong>May 24 or 28, 2027</strong><small>Proposed full-day format · Workshop day and room to be confirmed</small></div><div class="status-cell"><span class="pill">Proposal stage</span><small>Subject to conference acceptance.<br><a href="https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/" target="_blank" rel="noopener noreferrer">Official workshop information ↗</a></small></div></div></div></section>

<section class="section" id="about"><div class="wrap"><div class="section-head"><div><span class="eyebrow">01 / The shared question</span><h2>Better assistance.<br>Meaningful human control.</h2></div><p>Adaptive assistance brings together sensing, robot control and human judgment. This edition focuses on how to evaluate the decisions between them in contact-rich teleoperation and physical human–robot interaction.</p></div>
<div class="question-panel"><div><p class="big-question">How should we evaluate assistance when model predictions, physical outcomes and the operator’s experience do not align?</p><div class="topic-tags"><span>Shared autonomy</span><span>Digital twins</span><span>Human agency</span><span>Teleoperation</span><span>Physical HRI</span></div></div>
<ol class="questions"><li><span class="num">01</span><div><strong>Recognise uncertainty.</strong><p>Separate degraded sensing, model mismatch and uncertainty about human intent.</p></div></li><li><span class="num">02</span><div><strong>Make assistance understandable.</strong><p>Define when to intervene, request clarification or return control, and what feedback the operator needs.</p></div></li><li><span class="num">03</span><div><strong>Connect claims with evidence.</strong><p>Evaluate physical outcomes alongside agency, understanding and workload, using appropriate evidence for each.</p></div></li></ol></div></div></section>

<section class="section speakers-section" id="speakers"><div class="wrap"><div class="section-head"><div><span class="eyebrow">02 / Invited speakers</span><h2>Seven perspectives.<br>One shared discussion.</h2></div><p>The following speakers have accepted invitations for the proposed workshop. Talk titles, abstracts, order and participation modes will be announced as the programme develops.</p></div>
<div class="speaker-grid">{''.join(speaker_card(s) for s in data['speakers'])}<aside class="speaker-note"><span class="large">Control.<br>Learning.<br>Interaction.</span><p>Invited talks with Q&amp;A will connect research perspectives with the workshop’s evaluation questions.</p></aside></div>
<p class="footnote">Speaker profiles open in a new tab.</p></div></section>

<section class="section" id="programme"><div class="wrap"><div class="section-head"><div><span class="eyebrow">03 / Tentative programme</span><h2>A day built<br>for participation.</h2></div><p>Invited talks and contributions set up an extended afternoon of group work. Dedicated discussion, review and synthesis sessions lead to a draft evaluation framework.</p></div>
<div class="programme-top"><p>Proposed schedule · Local time in Seoul (KST, UTC+9)<br>Final timing will follow the conference’s confirmed instructions.</p><div class="programme-links"><a href="#morning">Morning ↓</a><a href="#afternoon">Afternoon ↓</a></div></div>
{schedule(['morning','break'],'Morning / perspectives & contributions','morning')}
{schedule(['afternoon'],'Afternoon / discussion & synthesis','afternoon')}
<p class="footnote">Each invited talk is planned for 20 minutes including Q&amp;A. Highlighted sessions reserve 170 minutes for scenario discussion, group review and synthesis.</p></div></section>

<section class="section discussion" id="discussion"><div class="wrap"><div class="section-head"><div><span class="eyebrow">04 / Work through a shared scenario</span><h2>Act, ask,<br>or return control?</h2></div><p>A facilitated discussion will bring researchers with different expertise together around the same situation. No specialised hardware or programming experience is required.</p></div>
<div class="discussion-layout"><div class="scenario"><span class="eyebrow">An illustrative situation</span><p>A person is remotely guiding a robot through a contact task. The view becomes occluded. A digital twin predicts a safe contact, but the observed result differs. The robot suggests continuing; the operator asks to pause.</p><small>What should happen next? Specify the decision, its trigger, the operator’s feedback and override options, and the evidence needed to evaluate it.</small></div>
<ol class="discussion-steps"><li><span class="minutes">90<small>MINUTES</small></span><div><strong>Explore together</strong><p>Mixed-expertise groups work through sensing degradation, model mismatch and assistance decisions.</p></div></li><li><span class="minutes">35<small>MINUTES</small></span><div><strong>Compare the reasoning</strong><p>Share assumptions and critique what evidence each proposed decision would require.</p></div></li><li><span class="minutes">45<small>MINUTES</small></span><div><strong>Draft an evaluation framework</strong><p>Collect intervention rules, feedback, baselines, physical measures and human measures, preserving open questions.</p></div></li></ol></div>
<p class="participation-note">Participants may contribute by speaking, writing or completing a worksheet. The exercise compares evaluation plans; empirical claims about task performance or workload require subsequent experimental evidence.</p></div></section>

<section class="section" id="contribute"><div class="wrap"><div class="section-head"><div><span class="eyebrow">05 / Contributions</span><h2>Bring your methods.<br>Bring your open questions.</h2></div><p>Planned contribution formats welcome empirical studies, methods, negative results, replication, work in progress and application case studies across robotics, control, HCI and human factors.</p></div>
<div class="contribution-layout"><div><div class="format-list"><article><span class="eyebrow">Research &amp; work in progress</span><h3>2–4 page papers</h3><p>Nonarchival contributions describing an evaluation claim, its evidence, limitations and connection to the workshop questions.</p></article><article><span class="eyebrow">Systems &amp; demonstrations</span><h3>1 page demo proposals</h3><p>Demonstrations may use video, so participation need not depend on transporting equipment.</p></article></div><p class="review-copy">The proposed review process uses two reviewers per submission, considering relevance, methodological clarity and the match between claims and evidence. The planned capacity is 24 contributions, including up to four demos, with up to twelve short spotlights. Accepted contributions will have poster or demo space.</p><p class="review-copy">Researchers at all career stages and people new to teleoperation are welcome. General attendance will not require an accepted paper; conference registration requirements will apply.</p></div>
<aside class="call-status"><span class="pill">Call not yet open</span><h3>Submission information</h3><dl><div><dt>Submission deadline</dt><dd>To be announced</dd></div><div><dt>Author notification</dt><dd>To be announced</dd></div><div><dt>Submission portal &amp; final instructions</dt><dd>Will be published after acceptance</dd></div></dl><a class="button secondary" href="mailto:z.wang82@lancaster.ac.uk?subject=ICRA%202027%20workshop%20enquiry">Contact the organizers <span aria-hidden="true">↗</span></a></aside></div></div></section>

<section class="section speakers-section" id="resources"><div class="wrap"><div class="section-head"><div><span class="eyebrow">06 / Planned shared resources</span><h2>From discussion<br>to a reusable framework.</h2></div><p>The organizing team plans to release accessible discussion materials before the event and a versioned synthesis afterwards. Materials will appear here when available.</p></div>
<div class="resource-list"><article class="resource-item"><small>Before the workshop</small><h3>Scenario &amp; worksheet</h3><p>An illustrative situation, a short glossary and discussion prompts. Planned release: at least two weeks before the workshop.</p><span class="resource-status">In preparation · not yet available</span></article><article class="resource-item"><small>Within four weeks afterwards</small><h3>Protocol &amp; synthesis</h3><p>A draft evaluation protocol, example worksheets, research questions and unresolved disagreements.</p><span class="resource-status">Planned output</span></article><article class="resource-item"><small>After approximately three months</small><h3>Follow-up discussion</h3><p>A proposed exchange to collect revisions and explore voluntary trials of the evaluation framework.</p><span class="resource-status">Date and participation to be arranged</span></article></div></div></section>

<section class="section" id="organizers"><div class="wrap"><div class="section-head"><div><span class="eyebrow">07 / Organizing team</span><h2>Connecting disciplines<br>and communities.</h2></div><p>The proposed team brings together expertise in interaction control, teleoperation, haptics, wearable assistance, robot learning, and physical and social HRI.</p></div><div class="organizer-grid">{''.join(organizers)}</div></div></section>

<section class="section previous-section" id="previous"><div class="wrap"><div class="section-head"><div><span class="eyebrow">08 / Previous editions</span><h2>A continuing conversation.</h2></div><p>Building on five workshops across ICRA and IROS, the sixth edition focuses on connecting model uncertainty, physical performance and human agency through shared evaluation questions.</p></div><div>{editions}</div></div></section>

<section class="contact" id="contact"><div class="wrap contact-inner"><div><span class="eyebrow">Let’s keep the conversation going</span><h2>Questions about<br>the workshop?</h2></div><div><p>For programme, contribution and participation enquiries:</p><p class="contact-name">Dr Ziwei Wang · Lancaster University</p><a class="contact-email" href="mailto:z.wang82@lancaster.ac.uk">z.wang82@lancaster.ac.uk ↗</a><p>Website contact: <a href="mailto:y.he20@lancaster.ac.uk">Yiyang He</a></p></div></div></section>
</main><footer class="footer"><div class="wrap footer-inner"><p>6th Sensorimotor-Augmented Interaction · Proposed ICRA 2027 workshop</p><p><a href="https://2027.ieee-icra.org/" target="_blank" rel="noopener noreferrer">ICRA 2027 ↗</a> &nbsp; / &nbsp; Updated {data['updated']}</p></div></footer>
</body></html>'''

(ROOT / 'index.html').write_text(html, encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n', encoding='utf-8')
(ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{URL}</loc><lastmod>{data["updated"]}</lastmod></url></urlset>', encoding='utf-8')
print(f'Built {ROOT / "index.html"}: {len(data["speakers"])} speakers, {len(data["organizers"])} organizers, {len(data["programme"])} sessions.')
