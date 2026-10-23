# ICRA 2027 · 6th Sensorimotor-Augmented Interaction

Static website for the proposed full-day workshop **Human Interaction Oriented Robotics for Real World Deployment**.

Public site: https://hyy2566.github.io/icra-workshop-6th-sai-2027/

## Status

This is a proposed workshop, subject to ICRA 2027 acceptance. The workshop day, room, contribution deadlines, submission portal and talk titles are not confirmed. Speaker order is provisional. The programme follows the revised proposal supplied on 2026-10-23: seven 25-minute invited-talk slots, lunch at 12:30–13:30 and closing at 17:30. Changyun Wen's workshop affiliation follows that proposal: Nanyang Technological University, Singapore.

## Edit and publish

- `content.json`: speaker profiles, organizers, contact emails, schedule, previous editions and group photo gallery.
- `build.py`: static page template and editorial text.
- `academic.css`: current page design, responsive layout, print rules and locally hosted Manrope font.
- `style.css` and `design.css`: retained earlier styles; not loaded by the current page.
- `site.js`: mobile navigation, active-section highlighting and an accessible full-size photograph viewer.
- `assets/gallery/`: five historical group photographs reused from the IROS 2026 website, excluding any 2026 group photo.
- `assets/hero-interaction-v2.webp`: retained earlier conceptual artwork; no longer displayed or used in social previews. The current introduction uses the authentic ICRA 2025 photograph, explicitly labelled as a previous edition.
- `assets/people/`: public speaker portraits; attribution in `assets/SOURCES.md`.

After editing `content.json` or `build.py`, run `python build.py`. Preview with `python -m http.server 8767`. No build tools or third-party JavaScript packages are required. GitHub Pages publishes `main` at the repository root. `.nojekyll` preserves the static files as authored.

All assets are local. Page content and links remain accessible without JavaScript; JavaScript enhances mobile navigation, active-section highlighting and the photograph viewer. Navigation and layout support keyboard use, reduced motion and mobile screens.

## Content basis

- Organizers' revised full-proposal draft supplied on 2026-10-23, including the original deployment scope, seven-speaker programme, group discussion, 10-person organizing team and a short post-workshop discussion summary.
- [ICRA 2027](https://2027.ieee-icra.org/) for conference location and dates.
- [ICRA workshop call](https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/) for possible workshop dates and acceptance status.
- Speaker links point to their university or laboratory profiles.

The website does not reproduce private invitation correspondence or reviewer comments. Prior-year submissions, meeting links and sponsors are not carried into this edition. Earlier promises of an evaluation protocol, a timed four-week release or subsequent protocol trials have been removed in accordance with the revised proposal. Photographs remain the property of their respective owners. Manrope is locally hosted under the SIL Open Font License in `assets/fonts/OFL.txt`.
