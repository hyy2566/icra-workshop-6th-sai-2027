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
    <a class="speaker-portrait" href="{e(s['url'])}" target="_blank" rel="noopener noreferrer" aria-label="{e(s['name'])}: official profile (opens in a new tab)">{photo}</a><div class="speaker-info">
    <h3><a href="{e(s['url'])}" target="_blank" rel="noopener noreferrer">{e(s['name'])}</a></h3>
    <p class="affiliation">{e(s['affiliation'])}</p><p class="country">{e(s['country'])}</p>
    <p class="talk">Invited talk with Q&amp;A<br><span>Title to be announced</span></p></div></article>'''

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

gallery = []
for item in data.get('gallery', []):
    caption = f"{item['event']} · {item['location']}"
    gallery.append(f'''<figure class="gallery-item"><a class="gallery-open" href="{e(item['image'])}" target="_blank" rel="noopener" data-caption="{e(caption)}" aria-label="View {e(item['event'])} group photograph at full size"><img src="{e(item['image'])}" width="{item['width']}" height="{item['height']}" alt="Group photograph from {e(item['event'])}" loading="lazy" decoding="async"><span class="gallery-zoom" aria-hidden="true">↗</span></a><figcaption><div class="gallery-caption-top"><h3>{e(item['event'])}</h3><span>{e(item['location'])}</span></div><p>{e(item['title'])}</p><a class="gallery-event-link" href="{e(item['url'])}" target="_blank" rel="noopener noreferrer">Workshop website ↗</a></figcaption></figure>''')

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(data['title'])} | ICRA 2027 Workshop Proposal</title>
<meta name="description" content="Proposed ICRA 2027 workshop in Seoul on evaluating adaptive robotic assistance through digital twins and human agency. Speakers, tentative programme, contribution plans and organizers.">
<meta name="theme-color" content="#081824"><link rel="canonical" href="{URL}"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:title" content="6th Sensorimotor-Augmented Interaction · ICRA 2027"><meta property="og:description" content="Evaluating Adaptive Assistance through Digital Twins and Human Agency. Proposed full-day workshop, Seoul, May 2027."><meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}assets/hero-interaction-v2.webp"><meta property="og:image:alt" content="Conceptual illustration of human and robotic hands interacting through a digital twin">
<link rel="preload" href="assets/fonts/manrope-500.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="assets/hero-interaction-v2.webp" as="image">
<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="design.css"><script src="site.js" defer></script><noscript><style>.menu-toggle{{display:none}}@media(max-width:800px){{.site-header{{height:auto;position:static}}.header-inner{{flex-wrap:wrap;padding-block:18px}}.nav{{display:flex;position:static;padding:0;border:0}}}}</style></noscript></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="#home" aria-label="6th Sensorimotor-Augmented Interaction home"><span class="brand-mark">6</span><span class="brand-text">Sensorimotor Interaction<small>ICRA 2027 · SEOUL</small></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu +</button>
<nav class="nav" id="main-nav" aria-label="Main navigation"><a href="#about">About</a><a href="#speakers">Speakers</a><a href="#programme">Programme</a><a href="#contribute">Contribute</a><a href="#organizers">Organizers</a><a href="#gallery">Gallery</a><a class="nav-contact" href="#contact">Contact ↗</a></nav></div></header>
<main id="main">
<section class="hero" id="home"><div class="hero-art"><img src="assets/hero-interaction-v2.webp" width="1672" height="941" alt="Conceptual illustration: a human hand and a robotic hand approaching a translucent digital twin" fetchpriority="high"></div><div class="wrap hero-main"><div class="hero-copy">
<span class="eyebrow hero-kicker"><span class="edition-pill">6th edition</span> ICRA 2027 · Seoul, Korea</span>
<h1><span>Sensorimotor-</span><span>Augmented</span><span class="hero-emphasis">Interaction.</span></h1>
<p class="subtitle">Evaluating Adaptive Assistance through Digital Twins and Human Agency</p>
<p class="intro">When should robotic assistance act, ask, or yield? Bringing physical performance and the operator’s experience into the same conversation.</p>
<div class="actions"><a class="button primary" href="#programme">Explore the programme <span aria-hidden="true">↗</span></a><a class="button secondary" href="#speakers">Meet the speakers <span aria-hidden="true">↗</span></a></div></div><div class="hero-caption">Physical intelligence.<br>Human agency.</div></div>
<div class="event-band"><div class="wrap event-strip"><div><span class="event-label">The setting</span><strong>Seoul, Republic of Korea</strong><small>Coex Convention &amp; Exhibition Center</small></div><div><span class="event-label">The date</span><strong>May 24 or 28, 2027</strong><small>Proposed full day · Workshop day and room to be confirmed</small></div><div class="status-cell"><span class="pill">Proposal stage</span><small>Subject to conference acceptance.<br><a href="https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/" target="_blank" rel="noopener noreferrer">Official workshop information ↗</a></small></div></div></div></section>

<section class="section" id="about"><div class="wrap"><div class="section-head"><div><span class="eyebrow">01 / The shared question</span><h2>Better assistance.<br>Meaningful human control.</h2></div><p>Adaptive assistance brings together sensing, robot control and human judgment. This edition focuses on how to evaluate the decisions between them in contact-rich teleoperation and physical human–robot interaction.</p></div>
<div class="question-panel"><div><p class="big-question">How should we evaluate assistance when model predictions, physical outcomes and the operator’s experience do not align?</p><div class="topic-tags"><span>Shared autonomy</span><span>Digital twins</span><span>Human agency</span><span>Teleoperation</span><span>Physical HRI</span></div></div>
<ol class="questions"><li><span class="num">01</span><div><strong>Recognise uncertainty.</strong><p>Separate degraded sensing, model mismatch and uncertainty about human intent.</p></div></li><li><span class="num">02</span><div><strong>Make assistance understandable.</strong><p>Define when to intervene, request clarification or return control, and what feedback the operator needs.</p></div></li><li><span class="num">03</span><div><strong>Connect claims with evidence.</strong><p>Evaluate physical outcomes alongside agency, understanding and workload, using appropriate evidence for each.</p></div></li></ol></div></div></section>

<section class="section speakers-section" id="speakers"><div class="wrap"><div class="section-head"><div><span class="eyebrow">02 / Invited speakers</span><h2>Seven perspectives.<br>One shared discussion.</h2></div><p>The following speakers have accepted invitations for the proposed workshop. Talk titles, abstracts, order and participation modes will be announced as the programme develops.</p></div>
<div class="speaker-grid">{''.join(speaker_card(s) for s in data['speakers'])}<aside class="speaker-note"><span class="eyebrow">Ideas in conversation</span><span class="large">07</span><p>Invited speakers bringing together control, learning and human–robot interaction.</p></aside></div>
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

<section class="section gallery-section" id="gallery"><div class="wrap"><div class="section-head"><div><span class="eyebrow">09 / Workshop gallery</span><h2>From our previous<br>workshops.</h2></div><p>Group photographs from our ICRA, IROS and related Humanoids workshops. Select a photograph to view it at full size.</p></div><div class="gallery-grid">{''.join(gallery)}</div></div></section>
<dialog class="photo-dialog" aria-labelledby="photo-caption"><div class="photo-viewer"><button class="photo-close" type="button" aria-label="Close photograph" autofocus>×</button><img class="photo-full" alt="Selected workshop group photograph" width="1280" height="719"><div class="photo-controls"><button class="photo-previous" type="button" aria-label="Previous photograph">←</button><div><p id="photo-caption"></p><span class="photo-count" aria-live="polite"></span></div><button class="photo-next" type="button" aria-label="Next photograph">→</button></div></div></dialog>

<section class="contact" id="contact"><div class="wrap contact-inner"><div><span class="eyebrow">Let’s keep the conversation going</span><h2>Questions about<br>the workshop?</h2></div><div><p>For programme, contribution and participation enquiries:</p><p class="contact-name">Dr Ziwei Wang · Lancaster University</p><a class="contact-email" href="mailto:z.wang82@lancaster.ac.uk">z.wang82@lancaster.ac.uk ↗</a><p>Website contact: <a href="mailto:y.he20@lancaster.ac.uk">Yiyang He</a></p></div></div></section>
</main><footer class="footer"><div class="wrap footer-inner"><p>6th Sensorimotor-Augmented Interaction · Proposed ICRA 2027 workshop</p><p><a href="https://2027.ieee-icra.org/" target="_blank" rel="noopener noreferrer">ICRA 2027 ↗</a> &nbsp; / &nbsp; Updated {data['updated']}</p></div></footer>
</body></html>'''

(ROOT / 'index.html').write_text(html, encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n', encoding='utf-8')
(ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{URL}</loc><lastmod>{data["updated"]}</lastmod></url></urlset>', encoding='utf-8')
print(f'Built {ROOT / "index.html"}: {len(data["speakers"])} speakers, {len(data["organizers"])} organizers, {len(data["programme"])} sessions.')
