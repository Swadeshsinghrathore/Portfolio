/* =========================================================
   ANTIGRAVITY AI — MINIMALIST PORTFOLIO  |  main.js
   ========================================================= */

/* ── 2. INTERACTIVE DOT GRID (canvas) ── */
const canvas = document.getElementById('bg-canvas');
const ctx    = canvas.getContext('2d');
let W, H, dots = [];

function buildGrid() {
  W = canvas.width  = window.innerWidth;
  H = canvas.height = window.innerHeight;
  dots = [];
  const gap  = 55;
  const cols = Math.ceil(W / gap) + 1;
  const rows = Math.ceil(H / gap) + 1;
  for (let c = 0; c < cols; c++)
    for (let r = 0; r < rows; r++)
      dots.push({ ox: c * gap, oy: r * gap, x: c * gap, y: r * gap });
}
buildGrid();
window.addEventListener('resize', buildGrid);

let pmx = 0, pmy = 0;
document.addEventListener('mousemove', e => { pmx = e.clientX; pmy = e.clientY; });

(function renderGrid() {
  ctx.clearRect(0, 0, W, H);
  for (const d of dots) {
    const dx   = pmx - d.ox;
    const dy   = pmy - d.oy;
    const dist = Math.sqrt(dx * dx + dy * dy);
    const r    = 120;

    if (dist < r) {
      const f = (1 - dist / r) * 0.5;
      d.x += (d.ox - dx * f * 0.4 - d.x) * 0.12;
      d.y += (d.oy - dy * f * 0.4 - d.y) * 0.12;
    } else {
      d.x += (d.ox - d.x) * 0.1;
      d.y += (d.oy - d.y) * 0.1;
    }

    const bright = dist < r ? (1 - dist / r) * 0.25 : 0;
    ctx.beginPath();
    ctx.arc(d.x, d.y, 0.8, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,255,255,${0.045 + bright})`;
    ctx.fill();
  }
  requestAnimationFrame(renderGrid);
})();

/* ── 3. FLOATING PARTICLES ── */
for (let i = 0; i < 60; i++) {
  const p    = document.createElement('div');
  p.className = 'particle';
  const size = 1 + Math.random() * 2;
  p.style.cssText =
    `width:${size}px;height:${size}px;` +
    `left:${Math.random() * 100}vw;` +
    `bottom:-10px;` +
    `animation-duration:${10 + Math.random() * 18}s;` +
    `animation-delay:${Math.random() * 12}s;` +
    `--dx:${(Math.random() - 0.5) * 180}px;`;
  document.body.appendChild(p);
}

/* ── 4. HERO NAME ENTRANCE ── */
window.addEventListener('load', () => {
  const hn = document.getElementById('heroName');
  if (hn) setTimeout(() => hn.classList.add('visible'), 200);
});

/* ── 5. SCROLL REVEAL ── */
const revealIO = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealIO.observe(el));

/* ── 6. SKILL BAR ANIMATION ── */
const skillIO = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    const fill  = e.target.querySelector('.skill-fill');
    const level = parseFloat(e.target.dataset.level) || 0;
    if (fill) fill.style.transform = `scaleX(${level})`;
  });
}, { threshold: 0.4 });

document.querySelectorAll('.skill-card').forEach(c => skillIO.observe(c));

/* ── 7. MAGNETIC HOVER EFFECT ── */
document.querySelectorAll('.btn, .contact-link, .project-card').forEach(el => {
  el.addEventListener('mousemove', e => {
    const b  = el.getBoundingClientRect();
    const xc = e.clientX - b.left  - b.width  / 2;
    const yc = e.clientY - b.top   - b.height / 2;
    el.style.transform = `translate(${xc * 0.1}px, ${yc * 0.15}px)`;
  });
  el.addEventListener('mouseleave', () => { el.style.transform = ''; });
});

/* ── 8. MOBILE MENU ── */
const menuBtn    = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (menuBtn && mobileMenu) {
  menuBtn.addEventListener('click', () => mobileMenu.classList.toggle('open'));
}
function closeMobile() {
  if (mobileMenu) mobileMenu.classList.remove('open');
}

/* ── 9. CONTACT FORM ── */
const form       = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');

if (form) {
  form.addEventListener('submit', async e => {
    e.preventDefault();
    const payload = {
      name:    document.getElementById('cf-name').value,
      email:   document.getElementById('cf-email').value,
      message: document.getElementById('cf-msg').value,
    };

    formStatus.textContent = 'Sending…';
    formStatus.className   = 'form-status';

    try {
      const res  = await fetch('/api/contact', {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify(payload),
      });
      const data = await res.json();
      if (data.success) {
        formStatus.textContent = '✓ ' + data.message;
        formStatus.className   = 'form-status ok';
        form.reset();
      } else {
        formStatus.textContent = '✗ ' + (data.error || 'Something went wrong.');
        formStatus.className   = 'form-status err';
      }
    } catch {
      formStatus.textContent = '✗ Network error. Please try again.';
      formStatus.className   = 'form-status err';
    }
  });
}

/* ── 10. ACTIVE NAV LINK on SCROLL ── */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 200) current = s.id;
  });
  navLinks.forEach(a => {
    a.style.color = a.getAttribute('href') === '#' + current
      ? 'var(--white)' : 'var(--g400)';
  });
}, { passive: true });

/* ── 11. PROJECT MODAL ── */
let projectsData = [];
try {
  const dataScript = document.getElementById('projectsData');
  if (dataScript) {
    projectsData = JSON.parse(dataScript.textContent);
  }
} catch (e) {
  console.error("Error parsing projects data:", e);
}

const projectModal = document.getElementById('projectModal');

// Make it available globally for inline onclick attributes
window.openProjectModal = function(index) {
  if (!projectModal || !projectsData[index]) return;
  
  const p = projectsData[index];
  
  // Title
  document.getElementById('modalTitle').textContent = p.name;
  
  // Tags
  const tagsContainer = document.getElementById('modalTags');
  tagsContainer.innerHTML = '';
  if (p.tags) {
    p.tags.forEach(tag => {
      const span = document.createElement('span');
      span.className = 'tag';
      span.textContent = tag;
      tagsContainer.appendChild(span);
    });
  }
  
  // Description
  document.getElementById('modalDesc').textContent = p.long_desc || p.desc;
  
  // Photos
  const photosContainer = document.getElementById('modalPhotos');
  const photosSection = document.getElementById('modalPhotosSection');
  photosContainer.innerHTML = '';
  if (p.photos && p.photos.length > 0) {
    p.photos.forEach(photo => {
      const img = document.createElement('img');
      // Using leading slash for absolute path from root
      img.src = '/static/' + photo; 
      photosContainer.appendChild(img);
    });
    photosSection.style.display = 'block';
  } else {
    photosSection.style.display = 'none';
  }
  
  // Contributors
  const contribContainer = document.getElementById('modalContributors');
  const contribSection = document.getElementById('modalContribSection');
  contribContainer.innerHTML = '';
  if (p.contributors && p.contributors.length > 0) {
    p.contributors.forEach(c => {
      const a = document.createElement('a');
      a.className = 'contrib-card';
      a.href = c.linkedin || '#';
      a.target = '_blank';
      
      const img = document.createElement('img');
      img.className = 'contrib-img';
      img.src = '/static/' + (c.photo || 'image/1.png');
      
      const name = document.createElement('span');
      name.className = 'contrib-name';
      name.textContent = c.name;
      
      a.appendChild(img);
      a.appendChild(name);
      contribContainer.appendChild(a);
    });
    contribSection.style.display = 'block';
  } else {
    contribSection.style.display = 'none';
  }
  
  // Link
  const modalLink = document.getElementById('modalLink');
  if (p.link && p.link !== '#') {
    modalLink.href = p.link;
    modalLink.style.display = 'inline-block';
  } else {
    modalLink.style.display = 'none';
  }
  
  // Show Modal & Disable body scroll
  projectModal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

window.closeProjectModal = function() {
  if (projectModal) {
    projectModal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

// Close modal on click outside
if (projectModal) {
  projectModal.addEventListener('click', (e) => {
    if (e.target === projectModal) {
      window.closeProjectModal();
    }
  });
}

// Close on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && projectModal && projectModal.classList.contains('active')) {
    window.closeProjectModal();
  }
});
