# ICRA 2027 · 6th Sensorimotor-Augmented Interaction

Static website for the proposed full-day workshop **Evaluating Adaptive Assistance through Digital Twins and Human Agency**.

Public site: https://hyy2566.github.io/icra-workshop-6th-sai-2027/

## Status

This is a proposed workshop, subject to ICRA 2027 acceptance. The workshop day, room, contribution deadlines, submission portal, talk titles and speaker order are not confirmed. Changyun Wen's affiliation for this edition awaits confirmation.

## Edit and publish

- `content.json`: speaker profiles, organizers, contact emails, schedule and previous editions.
- `build.py`: static page template and editorial text.
- `style.css` and `site.js`: presentation and navigation.
- `assets/people/`: public speaker portraits; attribution in `assets/SOURCES.md`.

After editing `content.json` or `build.py`, run `python build.py`. Preview with `python -m http.server 8767`. No build tools or third-party JavaScript packages are required. GitHub Pages publishes `main` at the repository root. `.nojekyll` preserves the static files as authored.

All assets are local. Page content and links remain accessible without JavaScript; JavaScript only enhances mobile navigation and active-section highlighting. Navigation and layout support keyboard use, reduced motion and mobile screens.

## Content basis

- Organizers' supplied full-proposal draft and its final revisions, including the seven-speaker programme, facilitated scenario discussion, 10-person organizing team and Yiyang He's corrected contact email.
- [ICRA 2027](https://2027.ieee-icra.org/) for conference location and dates.
- [ICRA workshop call](https://2027.ieee-icra.org/contribute/call-for-workshop-and-tutorial/) for possible workshop dates and acceptance status.
- Speaker links point to their university or laboratory profiles.

The website does not reproduce private invitation correspondence or reviewer comments. Prior-year submissions, meeting links and sponsors are not carried into this edition. The illustrative hero diagram was created for this site; portraits remain the property of their respective owners.
