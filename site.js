(() => {
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
  const sections = document.querySelectorAll('main > section[id]');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) {
        nav.querySelectorAll('a').forEach(link => {
          if (link.getAttribute('href') === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
    }, { rootMargin: '-15% 0px -65% 0px', threshold: 0 });
    sections.forEach(section => observer.observe(section));
  }
})();
