/**
 * OOSD Unit 2 — Professional Master Application Script
 * Features: High-Performance Scrollspy, Study Progress Persistence, Focus Mode,
 * Live Search Filter, Interactive Recall Checklists & Theme Engine.
 */

document.addEventListener('DOMContentLoaded', () => {
  // DOM Elements
  const sections = Array.from(document.querySelectorAll('.topic-section'));
  const navItems = Array.from(document.querySelectorAll('.nav-item'));
  const searchInput = document.getElementById('sidebar-search');
  const clearSearchBtn = document.getElementById('clear-search');
  const progressBar = document.getElementById('progress-bar');
  const progressPercent = document.getElementById('progress-percent');
  const currentSecIndicator = document.getElementById('current-sec-indicator');
  const completedCountEl = document.getElementById('completed-count');
  const topActiveTitle = document.getElementById('top-active-title');
  const floatLabel = document.getElementById('float-label');
  const floatPrev = document.getElementById('float-prev');
  const floatNext = document.getElementById('float-next');
  const sidebar = document.getElementById('sidebar');
  const sidebarToggle = document.getElementById('sidebar-toggle');
  const sidebarOverlay = document.getElementById('sidebar-overlay');
  const themeToggle = document.getElementById('theme-toggle');
  const themeToggleMob = document.getElementById('theme-toggle-mob');
  const focusToggle = document.getElementById('focus-toggle');
  const expandAllBtn = document.getElementById('expand-all-btn');
  const resetProgressBtn = document.getElementById('reset-progress-btn');

  let currentActiveIndex = 0;

  // 1. Theme Management (Default: Light Mode)
  const savedTheme = localStorage.getItem('oosd_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcons(savedTheme);

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('oosd_theme', next);
    updateThemeIcons(next);
  }

  function updateThemeIcons(theme) {
    const isDark = theme === 'dark';
    if (themeToggle) {
      themeToggle.querySelector('.theme-icon').textContent = isDark ? '🌙' : '☀️';
      themeToggle.querySelector('.theme-text').textContent = isDark ? 'Dark' : 'Light';
    }
    if (themeToggleMob) {
      themeToggleMob.textContent = isDark ? '🌙' : '☀️';
    }
  }

  if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
  if (themeToggleMob) themeToggleMob.addEventListener('click', toggleTheme);

  // 2. Focus Mode Toggle (Zen Reading)
  if (focusToggle) {
    focusToggle.addEventListener('click', () => {
      document.body.classList.toggle('focus-mode');
      const isFocused = document.body.classList.contains('focus-mode');
      focusToggle.querySelector('.tool-text').textContent = isFocused ? 'Show Sidebar' : 'Focus Mode';
      focusToggle.querySelector('.tool-icon').textContent = isFocused ? '✕' : '⛶';
    });
  }

  // 3. Zoom Controls (Range: 75% to 160% with instant visual scaling)
  const zoomDec = document.getElementById('zoom-dec') || document.getElementById('font-dec');
  const zoomReset = document.getElementById('zoom-reset') || document.getElementById('font-reset') || document.getElementById('zoom-level');
  const zoomInc = document.getElementById('zoom-inc') || document.getElementById('font-inc');
  const zoomLevelEl = document.getElementById('zoom-level');

  let currentZoom = parseFloat(localStorage.getItem('oosd_zoom') || '1.0');

  function applyZoom(newZoom) {
    currentZoom = Math.min(Math.max(newZoom, 0.75), 1.6);
    currentZoom = Math.round(currentZoom * 10) / 10; // Clean 0.8, 0.9, 1.0, 1.1, etc.
    
    document.documentElement.style.setProperty('--content-zoom', currentZoom);
    document.body.style.setProperty('--content-zoom', currentZoom);
    
    // Explicitly apply zoom to hero and sections
    const zoomTargets = document.querySelectorAll('.sections-wrapper, .course-hero');
    zoomTargets.forEach(el => {
      el.style.zoom = currentZoom;
    });

    const percentString = `${Math.round(currentZoom * 100)}%`;
    if (zoomLevelEl) zoomLevelEl.textContent = percentString;
    if (zoomReset && zoomReset !== zoomLevelEl) {
      zoomReset.textContent = currentZoom === 1.0 ? '100%' : percentString;
    }
    localStorage.setItem('oosd_zoom', currentZoom.toString());
  }

  // Initialize saved zoom on load
  applyZoom(currentZoom);

  if (zoomDec) {
    zoomDec.addEventListener('click', (e) => {
      e.preventDefault();
      applyZoom(currentZoom - 0.1);
    });
  }
  if (zoomReset) {
    zoomReset.addEventListener('click', (e) => {
      e.preventDefault();
      applyZoom(1.0);
    });
  }
  if (zoomInc) {
    zoomInc.addEventListener('click', (e) => {
      e.preventDefault();
      applyZoom(currentZoom + 0.1);
    });
  }

  // 4. Study Progress Tracking (Mark as Studied)
  const unitKey = document.body.getAttribute('data-unit') || 'unit2';
  const storageKey = `oosd_completed_${unitKey}`;
  let completedSections = new Set(JSON.parse(localStorage.getItem(storageKey) || '[]'));

  function updateCompletedUI() {
    sections.forEach(sec => {
      const secId = sec.id;
      const isDone = completedSections.has(secId);
      const doneBtn = sec.querySelector('.mark-done-btn');
      const navItem = document.getElementById(`nav-${secId}`);
      
      if (doneBtn) {
        if (isDone) {
          doneBtn.classList.add('is-done');
          doneBtn.querySelector('.done-icon').textContent = '✓';
          doneBtn.querySelector('.done-text').textContent = 'Studied';
        } else {
          doneBtn.classList.remove('is-done');
          doneBtn.querySelector('.done-icon').textContent = '○';
          doneBtn.querySelector('.done-text').textContent = 'Mark as Studied';
        }
      }

      if (navItem) {
        if (isDone) {
          navItem.classList.add('done');
        } else {
          navItem.classList.remove('done');
        }
      }
    });

    if (completedCountEl) {
      completedCountEl.textContent = `${completedSections.size}/${sections.length}`;
    }
  }

  window.toggleSectionDone = function(secId, btnElem) {
    if (completedSections.has(secId)) {
      completedSections.delete(secId);
    } else {
      completedSections.add(secId);
    }
    localStorage.setItem(storageKey, JSON.stringify(Array.from(completedSections)));
    updateCompletedUI();
  };

  if (resetProgressBtn) {
    resetProgressBtn.addEventListener('click', () => {
      if (confirm('Reset all studied checkmarks for this unit?')) {
        completedSections.clear();
        localStorage.removeItem(storageKey);
        updateCompletedUI();
      }
    });
  }

  updateCompletedUI();

  // 5. Mobile Sidebar Drawer
  if (sidebarToggle && sidebar && sidebarOverlay) {
    sidebarToggle.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      sidebarOverlay.classList.toggle('active');
    });

    sidebarOverlay.addEventListener('click', () => {
      sidebar.classList.remove('open');
      sidebarOverlay.classList.remove('active');
    });

    navItems.forEach(item => {
      item.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          sidebar.classList.remove('open');
          sidebarOverlay.classList.remove('active');
        }
      });
    });
  }

  // 6. Part Group Collapsing
  window.togglePartGroup = function(headerElem) {
    const group = headerElem.closest('.part-group');
    if (group) {
      group.classList.toggle('collapsed');
    }
  };

  if (expandAllBtn) {
    let allCollapsed = false;
    expandAllBtn.addEventListener('click', () => {
      const groups = document.querySelectorAll('.part-group');
      allCollapsed = !allCollapsed;
      groups.forEach(g => {
        if (allCollapsed) {
          g.classList.add('collapsed');
        } else {
          g.classList.remove('collapsed');
        }
      });
      expandAllBtn.textContent = allCollapsed ? 'Expand All' : 'Collapse All';
    });
  }

  // 7. Interactive Quick Recall Items (Click to Strike-through/Check)
  document.querySelectorAll('.quick-recall li').forEach(li => {
    li.addEventListener('click', () => {
      li.style.textDecoration = li.style.textDecoration === 'line-through' ? 'none' : 'line-through';
      li.style.opacity = li.style.textDecoration === 'line-through' ? '0.6' : '1';
    });
  });

  // 8. Active Section & High-Performance Scrollspy
  function setActiveSection(index) {
    if (index < 0 || index >= sections.length) return;
    if (currentActiveIndex === index && navItems[index].classList.contains('active')) return;

    currentActiveIndex = index;
    const activeSec = sections[index];
    const secId = activeSec.id;
    const secNum = activeSec.getAttribute('data-num');
    const secTitle = activeSec.querySelector('.sec-title').textContent;

    // Update Sidebar Navigation highlights
    navItems.forEach(item => {
      if (item.getAttribute('data-id') === secId) {
        item.classList.add('active');
        // Ensure active item stays visible in sidebar
        item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      } else {
        item.classList.remove('active');
      }
    });

    // Update Header breadcrumbs
    if (topActiveTitle) {
      topActiveTitle.textContent = `${secNum}. ${secTitle}`;
    }

    // Update Sidebar stat
    if (currentSecIndicator) {
      currentSecIndicator.textContent = `${secNum} / ${sections.length.toString().padStart(2, '0')}`;
    }

    // Update Floating Pill
    if (floatLabel) {
      floatLabel.querySelector('.f-num').textContent = secNum;
      floatLabel.querySelector('.f-text').textContent = secTitle;
    }
  }

  // Dual Scrollspy: Scroll position check + IntersectionObserver
  let isTicking = false;
  function updateScrollSpy() {
    const scrollY = window.scrollY || document.documentElement.scrollTop;
    const windowHeight = window.innerHeight;
    const docHeight = document.documentElement.scrollHeight;

    // Check if user is near the bottom of the page -> activate last section
    if (scrollY + windowHeight >= docHeight - 80) {
      setActiveSection(sections.length - 1);
      return;
    }

    // Find section closest to top offset (e.g. 140px)
    let bestIndex = 0;
    let minDistance = Infinity;

    for (let i = 0; i < sections.length; i++) {
      const rect = sections[i].getBoundingClientRect();
      const distance = Math.abs(rect.top - 100);
      if (rect.top <= 180 && distance < minDistance) {
        minDistance = distance;
        bestIndex = i;
      }
    }

    setActiveSection(bestIndex);

    // Global Scroll Reading Progress
    const maxScroll = docHeight - windowHeight;
    const progress = maxScroll > 0 ? (scrollY / maxScroll) * 100 : 0;
    const clamped = Math.min(100, Math.max(0, Math.round(progress)));

    if (progressBar) progressBar.style.width = `${clamped}%`;
    if (progressPercent) progressPercent.textContent = `${clamped}%`;

    isTicking = false;
  }

  window.addEventListener('scroll', () => {
    if (!isTicking) {
      window.requestAnimationFrame(updateScrollSpy);
      isTicking = true;
    }
  }, { passive: true });

  // 9. Floating Nav Buttons
  if (floatPrev) {
    floatPrev.addEventListener('click', () => {
      if (currentActiveIndex > 0) {
        sections[currentActiveIndex - 1].scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  if (floatNext) {
    floatNext.addEventListener('click', () => {
      if (currentActiveIndex < sections.length - 1) {
        sections[currentActiveIndex + 1].scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  // 10. Live Search / Filter in Sidebar
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      
      if (clearSearchBtn) {
        clearSearchBtn.style.display = query.length > 0 ? 'block' : 'none';
      }

      navItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        const parentGroup = item.closest('.part-group');
        
        if (text.includes(query)) {
          item.style.display = 'flex';
          // Auto-expand group if a match is inside
          if (parentGroup) {
            parentGroup.classList.remove('collapsed');
          }
        } else {
          item.style.display = 'none';
        }
      });

      // Hide or show empty part groups
      document.querySelectorAll('.part-group').forEach(group => {
        const visibleChildren = group.querySelectorAll('.nav-item[style="display: flex;"]');
        if (query.length > 0 && visibleChildren.length === 0) {
          group.style.display = 'none';
        } else {
          group.style.display = 'block';
        }
      });
    });

    if (clearSearchBtn) {
      clearSearchBtn.addEventListener('click', () => {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.focus();
      });
    }
  }

  // 11. Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') {
      if (e.key === 'Escape') {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.blur();
      }
      return;
    }

    if (e.key === '/' || e.key === 's') {
      e.preventDefault();
      if (searchInput) {
        searchInput.focus();
        searchInput.select();
      }
    } else if (e.key === 'j' || e.key === 'ArrowDown') {
      if (currentActiveIndex < sections.length - 1) {
        sections[currentActiveIndex + 1].scrollIntoView({ behavior: 'smooth' });
      }
    } else if (e.key === 'k' || e.key === 'ArrowUp') {
      if (currentActiveIndex > 0) {
        sections[currentActiveIndex - 1].scrollIntoView({ behavior: 'smooth' });
      }
    } else if (e.key === 't' || e.key === 'T') {
      toggleTheme();
    } else if (e.key === 'f' || e.key === 'F') {
      if (focusToggle) focusToggle.click();
    }
  });

  // 12. Terminal Window Code Copy Functionality
  document.querySelectorAll('.code-example-card').forEach(card => {
    const header = card.querySelector('.code-header');
    const codeEl = card.querySelector('.code-block code') || card.querySelector('pre code');
    if (header && codeEl && !header.querySelector('.code-copy-btn')) {
      const copyBtn = document.createElement('button');
      copyBtn.className = 'code-copy-btn';
      copyBtn.type = 'button';
      copyBtn.innerHTML = '<span>📋</span> Copy';
      copyBtn.title = 'Copy code snippet';
      copyBtn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(codeEl.textContent);
          copyBtn.classList.add('copied');
          copyBtn.innerHTML = '<span>✓</span> Copied!';
          setTimeout(() => {
            copyBtn.classList.remove('copied');
            copyBtn.innerHTML = '<span>📋</span> Copy';
          }, 2000);
        } catch (err) {
          const ta = document.createElement('textarea');
          ta.value = codeEl.textContent;
          document.body.appendChild(ta);
          ta.select();
          document.execCommand('copy');
          document.body.removeChild(ta);
          copyBtn.classList.add('copied');
          copyBtn.innerHTML = '<span>✓</span> Copied!';
          setTimeout(() => {
            copyBtn.classList.remove('copied');
            copyBtn.innerHTML = '<span>📋</span> Copy';
          }, 2000);
        }
      });
      header.appendChild(copyBtn);
    }
  });

  // Initial update on page load
  updateScrollSpy();
});
