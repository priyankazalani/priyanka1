/* ===================================
   main.js — Beach Portfolio Interactions
   =================================== */
(() => {
  'use strict';

  // ===== Preloader =====
  window.addEventListener('load', () => {
    setTimeout(() => {
      document.getElementById('preloader').classList.add('loaded');
    }, 1200);
  });

  // ===== Custom Cursor =====
  const cursorBubble = document.getElementById('cursorBubble');
  const cursorRing = document.getElementById('cursorRing');
  let mx = 0, my = 0, rx = 0, ry = 0;

  if (window.matchMedia('(pointer: fine)').matches) {
    window.addEventListener('mousemove', (e) => {
      mx = e.clientX;
      my = e.clientY;
      cursorBubble.style.left = mx + 'px';
      cursorBubble.style.top = my + 'px';
    });

    function animateCursor() {
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      cursorRing.style.left = rx + 'px';
      cursorRing.style.top = ry + 'px';
      requestAnimationFrame(animateCursor);
    }
    animateCursor();

    document.querySelectorAll('a, button, .island-card, .shell-card, .surfboard, .channel, .easter-shell').forEach(el => {
      el.addEventListener('mouseenter', () => cursorRing.classList.add('hover'));
      el.addEventListener('mouseleave', () => cursorRing.classList.remove('hover'));
    });
  }

  // ===== Navigation =====
  const navbar = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');
  const allNavLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  });

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('open');
  });

  allNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  // Active link on scroll
  const sections = document.querySelectorAll('section[id]');
  function updateActiveLink() {
    const scrollY = window.scrollY + 120;
    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      const link = document.querySelector(`.nav-link[href="#${id}"]`);
      if (link) {
        link.classList.toggle('active', scrollY >= top && scrollY < top + height);
      }
    });
  }
  window.addEventListener('scroll', updateActiveLink);

  // ===== Typewriter =====
  const typewriterEl = document.getElementById('typewriter');
  const phrases = [
    'Aspiring Web Developer 🌊',
    'BCA Student & Dreamer',
    'Code Enthusiast ⚡',
    'Ocean-Inspired Designer',
    'Passionate Debugger 🐚'
  ];
  let pi = 0, ci = 0, deleting = false, speed = 80;

  function typeWriter() {
    const phrase = phrases[pi];
    if (!deleting) {
      typewriterEl.textContent = phrase.substring(0, ci + 1);
      ci++;
      if (ci === phrase.length) { deleting = true; speed = 1800; }
      else speed = 80;
    } else {
      typewriterEl.textContent = phrase.substring(0, ci - 1);
      ci--;
      speed = 40;
      if (ci === 0) { deleting = false; pi = (pi + 1) % phrases.length; speed = 400; }
    }
    setTimeout(typeWriter, speed);
  }
  typeWriter();

  // ===== Scroll Reveal =====
  const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => entry.target.classList.add('revealed'), parseInt(delay));
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -30px 0px' });
  revealElements.forEach(el => revealObserver.observe(el));

  // ===== Surfboard Skill Bars =====
  const surfboardWaves = document.querySelectorAll('.surfboard-wave');
  const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const width = entry.target.dataset.width;
        entry.target.style.setProperty('--fill-width', width + '%');
        entry.target.classList.add('filled');
        skillObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  surfboardWaves.forEach(el => skillObserver.observe(el));

  // ===== Contact Form =====
  const contactForm = document.getElementById('contactForm');
  const submitBtn = document.getElementById('submitBtn');

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const original = submitBtn.innerHTML;
    submitBtn.innerHTML = '<i class="fas fa-check"></i> <span>Message Cast! 🌊</span>';
    submitBtn.style.background = '#10b981';
    submitBtn.disabled = true;

    setTimeout(() => {
      submitBtn.innerHTML = original;
      submitBtn.style.background = '';
      submitBtn.disabled = false;
      contactForm.reset();
    }, 2500);
  });

  // ===== Smooth Scroll =====
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ===== Sound Toggle =====
  const soundToggle = document.getElementById('soundToggle');
  const soundIcon = document.getElementById('soundIcon');
  const oceanSound = document.getElementById('oceanSound');
  let soundOn = false;

  soundToggle.addEventListener('click', () => {
    soundOn = !soundOn;
    if (soundOn) {
      oceanSound.play().catch(() => {});
      soundIcon.className = 'fas fa-volume-up';
    } else {
      oceanSound.pause();
      soundIcon.className = 'fas fa-volume-mute';
    }
  });

  // ===== Easter Egg Shells =====
  const shellTooltip = document.getElementById('shellTooltip');
  const shells = document.querySelectorAll('.easter-shell');
  let shellTimeout;

  shells.forEach(shell => {
    shell.addEventListener('click', (e) => {
      const fact = shell.dataset.fact;
      shellTooltip.textContent = '🐚 ' + fact;
      shellTooltip.style.left = Math.min(e.clientX, window.innerWidth - 300) + 'px';
      shellTooltip.style.top = (e.clientY - 60) + 'px';
      shellTooltip.classList.add('visible');
      clearTimeout(shellTimeout);
      shellTimeout = setTimeout(() => shellTooltip.classList.remove('visible'), 3500);
    });
  });

  // ===== Footprints on Scroll =====
  const footprintsContainer = document.getElementById('footprintsContainer');
  let lastPrintY = 0;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (Math.abs(scrollY - lastPrintY) > 300) {
      lastPrintY = scrollY;
      createFootprint();
    }
  });

  function createFootprint() {
    const fp = document.createElement('span');
    fp.classList.add('footprint');
    fp.textContent = '👣';
    fp.style.left = (20 + Math.random() * 60) + '%';
    fp.style.top = (window.scrollY + window.innerHeight * 0.7 + Math.random() * 100) + 'px';
    fp.style.transform = `rotate(${Math.random() * 30 - 15}deg)`;
    footprintsContainer.appendChild(fp);

    setTimeout(() => fp.remove(), 3000);
  }

  // ===== Parallax on Hero elements =====
  window.addEventListener('scroll', () => {
    const scroll = window.scrollY;
    const sun = document.querySelector('.sun');
    const clouds = document.querySelectorAll('.cloud');
    
    if (sun && scroll < window.innerHeight) {
      sun.style.transform = `translateY(${scroll * 0.3}px) scale(${1 + scroll * 0.0003})`;
      clouds.forEach((cloud, i) => {
        cloud.style.transform = `translateX(${scroll * (0.1 + i * 0.05)}px)`;
      });
    }
  });

})();
