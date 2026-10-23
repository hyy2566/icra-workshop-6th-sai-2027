"""Build the public workshop page from approved event metadata."""
import json
from pathlib import Path
from html import escape as e
from hashlib import sha256

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
URL = 'https://hyy2566.github.io/icra-workshop-6th-sai-2027/'

def versioned(name):
    return f"{name}?v={sha256((ROOT / name).read_bytes()).hexdigest()[:10]}"

def speaker_card(person):
    return f'''<article class="speaker" id="speaker-{person['id']}">
    <a class="speaker-portrait" href="{e(person['url'])}" target="_blank" rel="noopener noreferrer" aria-label="{e(person['name'])}: official profile (opens in a new tab)"><img class="speaker-photo" src="{e(person['image'])}" alt="{e(person['name'])}" width="180" height="180" loading="lazy"></a>
    <div class="speaker-info"><h3><a href="{e(person['url'])}" target="_blank" rel="noopener noreferrer">{e(person['name'])}</a></h3><p>{e(person['affiliation'])}</p><p class="country">{e(person['country'])}</p></div></article>'''

def schedule(sessions, title, anchor):
    rows = []
    for row in data['programme']:
        if row['session'] not in sessions:
            continue
        label = e(row['title'])
        if row.get('speaker'):
            label = f'<a href="#speaker-{e(row["speaker"])}">{label}</a>'
        detail = f'<span class="session-detail">{e(row["detail"])}</span>' if row['detail'] else ''
        rows.append(f'<tr class="{row.get("type","talk")}"><td>{row["start"]}–{row["end"]}</td><td><span class="session-title">{label}</span>{detail}</td></tr>')
    return f'<table class="schedule" id="{anchor}"><caption>{title}</caption><thead><tr><th scope="col">Time (KST)</th><th scope="col">Session</th></tr></thead><tbody>{"".join(rows)}</tbody></table>'

organizers = []
for person in data['organizers']:
    role = f'<span class="role">{e(person["role"])}</span>' if person.get('role') else ''
    organizers.append(f'<article class="organizer"><h3>{e(person["name"])}{role}</h3><p>{e(person["affiliation"])}</p><a href="mailto:{e(person["email"])}">{e(person["email"])}</a></article>')

editions = ''.join(f'<li><span class="edition-event">{e(row["conference"])} {e(row["year"])}</span><a href="{e(row["url"])}" target="_blank" rel="noopener noreferrer">{e(row["title"])}</a></li>' for row in data['editions'])
gallery = []
for item in data['gallery']:
    caption = f"{item['event']} · {item['location']}"
    gallery.append(f'''<figure class="gallery-item"><a class="gallery-open" href="{e(item['image'])}" target="_blank" rel="noopener" data-caption="{e(caption)}" aria-label="View {e(item['event'])} group photograph at full size"><img src="{e(item['image'])}" width="{item['width']}" height="{item['height']}" alt="Group photograph from {e(item['event'])}" loading="lazy" decoding="async"><span class="gallery-zoom" aria-hidden="true">↗</span></a><figcaption><div class="gallery-caption-top"><h3>{e(item['event'])}</h3><span>{e(item['location'])}</span></div><p>{e(item['title'])}</p><a class="gallery-event-link" href="{e(item['url'])}" target="_blank" rel="noopener noreferrer">Workshop website</a></figcaption></figure>''')

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(data['title'])} | ICRA 2027</title>
<meta name="description" content="Proposed ICRA 2027 full-day workshop: Human Interaction Oriented Robotics for Real World Deployment. Invited speakers, tentative programme and call for contributions.">
<meta name="theme-color" content="#193d50"><link rel="canonical" href="{URL}"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:title" content="{e(data['title'])} · ICRA 2027"><meta property="og:description" content="{e(data['subtitle'])}"><meta property="og:url" content="{URL}"><meta property="og:image" content="{URL}assets/hero-interaction-v2.webp"><meta property="og:image:alt" content="Conceptual illustration of a human hand and a robotic hand">
<link rel="preload" href="assets/fonts/manrope-400.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="assets/hero-interaction-v2.webp" as="image"><link rel="stylesheet" href="{versioned('academic.css')}"><script src="{versioned('site.js')}" defer></script>
<noscript><style>.menu-toggle{{display:none}}@media(max-width:900px){{.site-header{{height:auto;position:static}}.header-inner{{flex-wrap:wrap;padding-block:18px}}.nav{{display:flex;position:static;padding:0;border:0}}}}</style></noscript></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="#home" aria-label="6th Sensorimotor-Augmented Interaction home"><span>SAI 2027</span><small>6th workshop · ICRA</small></a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu +</button><nav class="nav" id="main-nav" aria-label="Main navigation"><a href="#about">About</a><a href="#speakers">Speakers</a><a href="#programme">Programme</a><a href="#contribute">Contributions</a><a href="#organizers">Organizers</a><a href="#gallery">Gallery</a><a href="#contact">Contact</a></nav></div></header>
<main id="main">
<section class="hero hero-with-art" id="home"><div class="hero-art"><img src="assets/hero-interaction-v2.webp" alt="Conceptual illustration of a human hand and a robotic hand" width="1672" height="941" fetchpriority="high"></div><div class="wrap hero-grid"><div class="hero-copy"><p class="conference-label">ICRA 2027 · Full-day workshop</p><h1>{e(data['title'])}</h1><p class="subtitle">{e(data['subtitle'])}</p><dl class="event-details"><div><dt>Location</dt><dd>Seoul, Republic of Korea<br><span>Coex Convention &amp; Exhibition Center</span></dd></div><div><dt>Date</dt><dd>May 24 or 28, 2027<br><span>Workshop day and room to be confirmed</span></dd></div></dl><p class="status-note"><strong>Proposal stage.</strong> The workshop is subject to conference acceptance.</p><div class="hero-links"><a class="button" href="#programme">Tentative programme</a><a href="#contribute">Contribution information</a></div></div></div></section>

<section class="section" id="about"><div class="wrap"><div class="section-heading"><h2>About the workshop</h2></div><div class="about-layout"><div class="prose"><p>This workshop examines how sensing, feedback and robot assistance work together in teleoperation, assistive robotics and physical human–robot interaction. It follows the human-interaction-oriented approach of the series, assessing assistance through its effect on both the task and the person using the robot.</p><p>The sixth edition focuses on how to evaluate assistance that improves task performance but may be difficult for users to understand or control. Topics include unreliable sensing and situations in which the robot’s estimate conflicts with the operator’s intention. Digital twins will be considered alongside physical experiments and user studies.</p><p>Invited talks and contributed work will inform a group discussion of an illustrative teleoperation task, followed by a short summary of evaluation considerations and questions for further study.</p></div><aside class="topics"><h3>Topics of interest</h3><ul><li>Multimodal sensing and feedback</li><li>Adaptive shared autonomy and interaction control</li><li>Learning and validation for real-world deployment</li><li>Evaluation of task performance and user experience</li></ul></aside></div></div></section>

<section class="section" id="speakers"><div class="wrap"><div class="section-heading"><h2>Invited speakers</h2><p>The following speakers have confirmed their participation. Talk titles and abstracts will be announced.</p></div><div class="speaker-grid">{''.join(speaker_card(person) for person in data['speakers'])}</div></div></section>

<section class="section" id="programme"><div class="wrap"><div class="section-heading"><h2>Tentative programme</h2><p>All times are local to Seoul (KST, UTC+9). The invited-speaker order is provisional.</p></div><p class="programme-note">Each 25-minute invited-talk slot includes a 20-minute presentation and up to five minutes for questions and transition.</p><nav class="programme-links" aria-label="Programme sessions"><a href="#morning">Morning</a><a href="#afternoon">Afternoon</a></nav>{schedule(['morning','break'],'Morning','morning')}{schedule(['afternoon'],'Afternoon','afternoon')}</div></section>

<section class="section" id="discussion"><div class="wrap"><div class="section-heading"><h2>Group discussion</h2></div><div class="discussion-layout"><div class="prose"><p>The afternoon discussion will use a teleoperation example in which sensing becomes unreliable or a digital twin’s prediction differs from observed contact. Organizers will prepare a short illustrated description and a one-page discussion sheet.</p><p>Participants will work in groups of five to eight to compare evaluation approaches. No specialised equipment or programming experience is required. Groups will consider task success and contact forces alongside user understanding, workload and perceived control. Participants may ask questions aloud or in writing.</p><p>The reporting session will include four five-minute reports followed by open discussion. Notes from every group will inform the plenary summary, identifying useful evaluation criteria and questions for further study. The closing panel will address broader research directions and applications.</p></div><aside class="materials" id="resources"><h3>Workshop materials</h3><p>Discussion materials and a short glossary will be available before the event.</p><p>A short discussion summary will be published afterwards. Accepted papers and presentation materials will be shared with the authors’ permission.</p></aside></div></div></section>

<section class="section" id="contribute"><div class="wrap"><div class="section-heading"><h2>Call for contributions</h2></div><p class="submission-status"><strong>Call not yet open.</strong> Submission dates and instructions will be announced after workshop acceptance.</p><div class="contribution-layout"><div class="prose"><p>We welcome nonarchival submissions, including work in progress and application reports, on the workshop topics.</p><dl class="formats"><div><dt>Papers</dt><dd>2–4 pages</dd></div><div><dt>Demo proposals</dt><dd>1 page</dd></div></dl><p>Two reviewers will assess each submission for relevance and technical clarity, with conflicts of interest avoided. Spotlight selections will represent a range of topics; questions will be taken during the poster sessions.</p></div><aside class="contribution-notes"><h3>Presentation format</h3><p>We plan for up to 24 contributions, including up to four demos. All accepted contributions will have poster or demo space.</p><p>Up to twelve contributions will receive a 2.5-minute spotlight, including the handover.</p><p>All workshop registrants may join the discussions, including those without an accepted contribution.</p></aside></div><p class="section-contact">For contribution enquiries, contact <a href="mailto:z.wang82@lancaster.ac.uk">Ziwei Wang</a>.</p></div></section>

<section class="section" id="organizers"><div class="wrap"><div class="section-heading"><h2>Organizing committee</h2></div><div class="organizer-grid">{''.join(organizers)}</div></div></section>

<section class="section" id="previous"><div class="wrap"><div class="section-heading"><h2>Previous workshops</h2><p>Recent editions have typically attracted about 80–100 participants, based on organizer estimates.</p></div><ul class="editions">{editions}</ul><p class="related-events">Members of the team also organized the related <a href="https://rwhri.github.io/Humanoids2024_workshop/" target="_blank" rel="noopener noreferrer">Humanoids 2024</a> and <a href="https://rwhri.github.io/Humanoids2025_workshop/" target="_blank" rel="noopener noreferrer">Humanoids 2025</a> workshops.</p></div></section>

<section class="section" id="gallery"><div class="wrap"><div class="section-heading"><h2>Workshop photographs</h2><p>From previous ICRA, IROS and related Humanoids workshops. Select a photograph to view the full image.</p></div><div class="gallery-grid">{''.join(gallery)}</div></div></section>
<dialog class="photo-dialog" aria-labelledby="photo-caption"><div class="photo-viewer"><button class="photo-close" type="button" aria-label="Close photograph" autofocus>×</button><img class="photo-full" alt="Selected workshop group photograph" width="1280" height="719"><div class="photo-controls"><button class="photo-previous" type="button" aria-label="Previous photograph">←</button><div><p id="photo-caption"></p><span class="photo-count" aria-live="polite"></span></div><button class="photo-next" type="button" aria-label="Next photograph">→</button></div></div></dialog>

<section class="section contact" id="contact"><div class="wrap contact-layout"><div><h2>Contact</h2><p>Programme, contributions and participation</p><p><strong>Dr Ziwei Wang</strong><br>Lancaster University, UK<br><a href="mailto:z.wang82@lancaster.ac.uk">z.wang82@lancaster.ac.uk</a></p></div><div><h3>Website enquiries</h3><p>Yiyang He<br><a href="mailto:y.he20@lancaster.ac.uk">y.he20@lancaster.ac.uk</a></p><p><a href="https://2027.ieee-icra.org/" target="_blank" rel="noopener noreferrer">ICRA 2027 conference website</a><br><a href="https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/" target="_blank" rel="noopener noreferrer">Official workshop information</a></p></div></div></section>
</main><footer class="footer"><div class="wrap"><p>{e(data['title'])} · ICRA 2027</p><p>Updated {data['updated']}</p></div></footer></body></html>'''

(ROOT / 'index.html').write_text(html, encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n', encoding='utf-8')
(ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{URL}</loc><lastmod>{data["updated"]}</lastmod></url></urlset>', encoding='utf-8')
print(f'Built index.html: {len(data["speakers"])} speakers, {len(data["organizers"])} organizers, {len(data["programme"])} sessions.')
