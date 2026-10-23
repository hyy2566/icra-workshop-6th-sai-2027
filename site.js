(() => {
  // Preserve links shared before the site was separated into individual pages.
  const legacyPages = {
    speakers: 'speakers.html', programme: 'programme.html',
    morning: 'programme.html#morning', afternoon: 'programme.html#afternoon',
    discussion: 'programme.html#discussion', resources: 'programme.html#resources',
    contribute: 'contributions.html', contributions: 'contributions.html',
    organizers: 'organizers.html', gallery: 'gallery.html',
    previous: 'gallery.html#previous', contact: 'contact.html'
  };
  const routeLegacyLink = () => {
    const home = location.pathname.endsWith('/') || location.pathname.endsWith('/index.html');
    if (!home) return;
    const key = location.hash.slice(1);
    const speaker = /^speaker-(arash|monroe|marta|sonia|dongjun|wansoo|chenguang)$/.test(key);
    const destination = speaker ? `speakers.html#${key}` : legacyPages[key];
    if (typeof destination === 'string') location.replace(destination);
  };
  routeLegacyLink();
  window.addEventListener('hashchange', routeLegacyLink);

  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-nav');
  const closeMenu = () => {
    nav.classList.remove('open');
    button.setAttribute('aria-expanded', 'false');
    button.textContent = 'Menu +';
  };
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    nav.classList.toggle('open', open);
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? 'Close −' : 'Menu +';
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      button.focus();
    }
  });
  // Real image links remain usable when dialog support or JavaScript is absent.
  const dialog = document.querySelector('.photo-dialog');
  const photos = [...document.querySelectorAll('.gallery-open')];
  if (dialog && typeof dialog.showModal === 'function' && photos.length) {
    const fullImage = dialog.querySelector('.photo-full');
    const caption = dialog.querySelector('#photo-caption');
    const count = dialog.querySelector('.photo-count');
    let active = 0;
    let opener;
    const showPhoto = index => {
      active = (index + photos.length) % photos.length;
      const link = photos[active];
      const thumbnail = link.querySelector('img');
      fullImage.src = link.href;
      fullImage.alt = thumbnail.alt;
      fullImage.width = Number(thumbnail.getAttribute('width'));
      fullImage.height = Number(thumbnail.getAttribute('height'));
      caption.textContent = link.dataset.caption;
      count.textContent = `${active + 1} / ${photos.length}`;
    };
    photos.forEach((link, index) => link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      opener = link;
      showPhoto(index);
      dialog.showModal();
      document.body.classList.add('photo-open');
    }));
    dialog.querySelector('.photo-close').addEventListener('click', () => dialog.close());
    dialog.querySelector('.photo-previous').addEventListener('click', () => showPhoto(active - 1));
    dialog.querySelector('.photo-next').addEventListener('click', () => showPhoto(active + 1));
    dialog.addEventListener('click', event => {
      if (event.target === dialog) dialog.close();
    });
    dialog.addEventListener('keydown', event => {
      if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
        event.preventDefault();
        showPhoto(active + (event.key === 'ArrowRight' ? 1 : -1));
      }
    });
    dialog.addEventListener('close', () => {
      document.body.classList.remove('photo-open');
      opener?.focus({preventScroll:true});
    });
  }
})();
