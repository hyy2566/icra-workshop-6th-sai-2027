# ICRA 2027 · 6th Sensorimotor-Augmented Interaction

Static website for the proposed full-day workshop **Human Interaction Oriented Robotics for Real World Deployment**.

Public site: https://hyy2566.github.io/icra-workshop-6th-sai-2027/

## Status

This is a proposed workshop, subject to ICRA 2027 acceptance. The workshop day, room, contribution deadlines, submission portal and talk titles are not confirmed. Speaker order is provisional. The programme follows the revised proposal supplied on 2026-10-23: seven 25-minute invited-talk slots, lunch at 12:30–13:30 and closing at 17:30. Changyun Wen's workshop affiliation follows that proposal: Nanyang Technological University, Singapore.

## Edit and publish

- `content.json`: speaker profiles, organizers, contact emails, schedule, previous editions and group photo gallery.
- `build.py`: shared page template and editorial sections. Builds seven independent pages: Home (`index.html`), Speakers, Programme, Contributions, Organizers, Gallery and Contact.
- `academic.css`: current page design, responsive layout, print rules and locally hosted Manrope font.
- `style.css` and `design.css`: retained earlier styles; not loaded by the current page.
- `site.js`: mobile navigation, redirects from previously shared section links and an accessible full-size photograph viewer. Active-page navigation is rendered in the HTML.
- `assets/gallery/`: five historical group photographs reused from the IROS 2026 website, excluding any 2026 group photo.
- `assets/hero-interaction-v2.webp`: conceptual human–robot hand illustration, restored as the homepage hero and social preview at the organizer's request. The revised proposal text and academic typography remain in use. Authentic group photographs are available in the gallery.
- `assets/people/`: public speaker portraits; attribution in `assets/SOURCES.md`.
- `assets/organizers/`: ten organizer portraits, including the photograph supplied for Yiyang He on 2026-10-24. Portraits and names link to the corresponding university, laboratory or personal profile.

After editing `content.json` or `build.py`, run `python build.py`. Preview with `python -m http.server 8767`. No build tools or third-party JavaScript packages are required. GitHub Pages publishes `main` at the repository root. `.nojekyll` preserves the static files as authored.

All assets are local. Each page can be opened directly, refreshed or shared; page content and navigation work without JavaScript. JavaScript enhances mobile navigation and the photograph viewer, and routes old homepage links such as `#organizers` or `#speaker-sonia` to their new pages. Navigation and layout support keyboard use, reduced motion and mobile screens. The homepage retains the hand illustration and workshop overview; the full programme, portraits and gallery are on their own pages.

## Content basis

- Organizers' revised full-proposal draft supplied on 2026-10-23, including the original deployment scope, seven-speaker programme, group discussion, 10-person organizing team and a short post-workshop discussion summary.
- [ICRA 2027](https://2027.ieee-icra.org/) for conference location and dates.
- [ICRA workshop call](https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/) for possible workshop dates and acceptance status.
- Speaker links point to their university or laboratory profiles.

The website does not reproduce private invitation correspondence or reviewer comments. Prior-year submissions, meeting links and sponsors are not carried into this edition. Earlier promises of an evaluation protocol, a timed four-week release or subsequent protocol trials have been removed in accordance with the revised proposal. Photographs remain the property of their respective owners. Manrope is locally hosted under the SIL Open Font License in `assets/fonts/OFL.txt`.
