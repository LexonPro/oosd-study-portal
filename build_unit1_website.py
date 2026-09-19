# build_unit1_website.py: Assembles unit1.html from Parts 1, 2, 3, and 4
import os
import generate_unit1_part1
import generate_unit1_part2
import generate_unit1_part3
import generate_unit1_part4

part1 = generate_unit1_part1.get_unit1_part1_sections()
part2 = generate_unit1_part2.get_unit1_part2_sections()
part3 = generate_unit1_part3.get_unit1_part3_sections()
part4_all = generate_unit1_part4.get_unit1_part4_sections()

# Split part4_all into Part 4 (17-19), Part 5 (20-22), and Part 6 (23)
part4 = part4_all[0:3]
part5 = part4_all[3:6]
part6 = part4_all[6:7]

all_sections = part1 + part2 + part3 + part4 + part5 + part6

print(f"Total Unit 1 sections assembled: {len(all_sections)}")
assert len(all_sections) == 23, f"Expected 23 sections, found {len(all_sections)}"

parts_meta = [
    {"num": 1, "title": "PART 1 — Object-Oriented Concepts", "theme_class": "part-blue", "sections": part1},
    {"num": 2, "title": "PART 2 — Identity, Encapsulation & Polymorphism", "theme_class": "part-purple", "sections": part2},
    {"num": 3, "title": "PART 3 — Modelling & OMT Models", "theme_class": "part-cyan", "sections": part3},
    {"num": 4, "title": "PART 4 — Unified Modeling Language (UML)", "theme_class": "part-amber", "sections": part4},
    {"num": 5, "title": "PART 5 — Conceptual Model & Architecture", "theme_class": "part-rose", "sections": part5},
    {"num": 6, "title": "PART 6 — Link and Association", "theme_class": "part-green", "sections": part6},
]

# Generate Sidebar HTML
sidebar_items_html = []
for p in parts_meta:
    sidebar_items_html.append(f"""
    <div class="part-group {p['theme_class']}" data-part="{p['num']}">
      <div class="part-header" onclick="togglePartGroup(this)">
        <div class="part-title-row">
          <span class="part-dot"></span>
          <span class="part-title">{p['title']}</span>
        </div>
        <div class="part-meta-row">
          <span class="part-badge">{len(p['sections'])} Topics</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="part-items">
    """)
    for s in p['sections']:
        sidebar_items_html.append(f"""
        <a href="#{s['id']}" class="nav-item" data-id="{s['id']}" id="nav-{s['id']}">
          <span class="nav-num">{s['number']}</span>
          <span class="nav-text">{s['title']}</span>
          <span class="check-indicator" id="chk-nav-{s['id']}"></span>
        </a>
        """)
    sidebar_items_html.append("""
      </div>
    </div>
    """)

sidebar_html = "\n".join(sidebar_items_html)

# Generate Main Content HTML
content_sections_html = []
for idx, s in enumerate(all_sections):
    prev_sec = all_sections[idx-1] if idx > 0 else None
    next_sec = all_sections[idx+1] if idx < len(all_sections) - 1 else None
    
    prev_link = f"""<a href="#{prev_sec['id']}" class="nav-btn prev-btn">← {prev_sec['number']}. {prev_sec['title']}</a>""" if prev_sec else """<span class="nav-btn disabled">Start of Unit 1</span>"""
    next_link = f"""<a href="#{next_sec['id']}" class="nav-btn next-btn">{next_sec['number']}. {next_sec['title']} →</a>""" if next_sec else """<a href="index.html#sec-1" class="nav-btn next-btn">Proceed to Unit 2 (Sec 01) →</a>"""
    
    content_sections_html.append(f"""
    <section id="{s['id']}" class="topic-section" data-num="{s['number']}">
      <div class="section-meta">
        <span class="part-pill">{s['part']}</span>
        <div class="meta-actions">
          <button class="mark-done-btn" onclick="toggleSectionDone('{s['id']}', this)" data-id="{s['id']}">
            <span class="done-icon">○</span>
            <span class="done-text">Mark as Studied</span>
          </button>
          <span class="reading-time">⏱ 4 min study</span>
        </div>
      </div>
      
      <div class="section-header">
        <span class="sec-badge">Section {s['number']}</span>
        <h2 class="sec-title">{s['title']}</h2>
      </div>
      <p class="sec-subtitle">{s['subtitle']}</p>
      
      <div class="section-body">
        {s['content']}
      </div>

      <div class="section-nav-footer">
        {prev_link}
        <a href="#top" class="top-jump" title="Back to top">↑ Top</a>
        {next_link}
      </div>
    </section>
    """)

sections_html = "\n".join(content_sections_html)

html_template = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OOSD — UNIT 1: Complete Master Study Guide (All 23 Topics)</title>
  <meta name="description" content="Comprehensive interactive study portal covering all 23 topics of Object Oriented System Design Unit 1 (Object Concepts, Object Identity, Encapsulation, Polymorphism, Generosity, Modelling Principles, OMT Models, UML Conceptual Model & Architecture) with real-life analogies, commented code examples, and vector diagrams.">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body id="top" data-unit="unit1">

  <!-- Top Global Progress Bar -->
  <div id="progress-bar-container">
    <div id="progress-bar"></div>
  </div>

  <!-- Mobile Header & Toggle -->
  <header class="mobile-nav-header">
    <button id="sidebar-toggle" aria-label="Toggle Slidebar Navigation" class="icon-btn">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>
    <div class="mobile-logo">
      <span class="accent-text">OOSD</span> Unit 1 (23 Topics)
    </div>
    <div class="mobile-controls">
      <div class="unit-switcher">
        <a href="unit1.html" class="unit-tab active" title="Current: Unit 1">U1</a>
        <a href="index.html" class="unit-tab" title="Go to Unit 2">U2</a>
        <a href="unit3.html" class="unit-tab" title="Go to Unit 3">U3</a>
        <a href="unit4.html" class="unit-tab" title="Go to Unit 4">U4</a>
        <a href="unit5.html" class="unit-tab" title="Go to Unit 5">U5</a>
      </div>
      <button id="theme-toggle-mob" class="icon-btn" title="Toggle Dark/Light Mode">🌙</button>
    </div>
  </header>

  <div class="app-layout">
    <!-- SLIDEBAR / SIDEBAR (All 23 Headings) -->
    <aside id="sidebar" class="sidebar">
      <div class="sidebar-header">
        <div class="logo-row">
          <div class="logo-mark" style="background: linear-gradient(135deg, #0284c7, #2563eb);">U1</div>
          <div class="logo-text">
            <h3>OOSD Unit 1</h3>
            <span class="subtitle-tag">Complete Syllabus (23 Topics)</span>
          </div>
        </div>

        <!-- 5-Way Unit Switcher Pill -->
        <div class="unit-switcher" style="margin: 12px 0 6px 0; width: 100%; justify-content: center; gap: 4px;">
          <a href="unit1.html" class="unit-tab active" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
            U1 <span class="unit-tab-count">23</span>
          </a>
          <a href="index.html" class="unit-tab" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
            U2 <span class="unit-tab-count">36</span>
          </a>
          <a href="unit3.html" class="unit-tab" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
            U3 <span class="unit-tab-count">28</span>
          </a>
          <a href="unit4.html" class="unit-tab" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
            U4 <span class="unit-tab-count">20</span>
          </a>
          <a href="unit5.html" class="unit-tab" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
            U5 <span class="unit-tab-count">24</span>
          </a>
        </div>

        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" id="sidebar-search" placeholder="Search 23 topics (e.g. Identity, Polymorphism, OMT)..." autocomplete="off">
          <button id="clear-search" class="clear-btn" title="Clear search" style="display: none;">✕</button>
        </div>

        <div class="sidebar-stats">
          <div class="stat-item">
            <span class="stat-val" id="current-sec-indicator">01 / 23</span>
            <span class="stat-lbl">Active Topic</span>
          </div>
          <div class="stat-item">
            <span class="stat-val" id="progress-percent">0%</span>
            <span class="stat-lbl">Read Progress</span>
          </div>
          <div class="stat-item">
            <span class="stat-val" id="completed-count">0/23</span>
            <span class="stat-lbl">Studied</span>
          </div>
        </div>

        <div class="sidebar-controls-row">
          <button id="expand-all-btn" class="mini-btn" title="Expand/Collapse All Parts">Toggle All</button>
          <button id="reset-progress-btn" class="mini-btn" title="Reset checkmarks">Reset Checks</button>
        </div>
      </div>

      <!-- Navigation Tree: All 23 Headings Grouped Under Parts -->
      <nav class="sidebar-nav" id="sidebar-nav" aria-label="Course Topics">
        {sidebar_html}
      </nav>

      <div class="sidebar-footer">
        <div class="quick-shortcuts">
          <small>Keys: <kbd>J</kbd> Next • <kbd>K</kbd> Prev • <kbd>/</kbd> Search • <kbd>T</kbd> Theme</small>
        </div>
      </div>
    </aside>

    <!-- Sidebar Overlay for Mobile -->
    <div id="sidebar-overlay" class="sidebar-overlay"></div>

    <!-- MAIN SCROLLABLE CONTENT (1 to 23 Continuous Scroll) -->
    <main class="main-content">
      <!-- Top Sticky Header -->
      <div class="top-nav-bar">
        <div class="breadcrumbs">
          <span class="bc-course">OOSD</span>
          <span class="bc-sep">/</span>
          <span class="bc-unit">Unit 1 Master</span>
          <span class="bc-sep">/</span>
          <span class="bc-active" id="top-active-title">01. Meaning of Object Orientation</span>
        </div>

        <div class="action-tools">
          <!-- 5-Way Unit Switcher in Desktop Top Bar -->
          <div class="unit-switcher">
            <a href="unit1.html" class="unit-tab active">
              Unit 1 <span class="unit-tab-count">23</span>
            </a>
            <a href="index.html" class="unit-tab">
              Unit 2 <span class="unit-tab-count">36</span>
            </a>
            <a href="unit3.html" class="unit-tab">
              Unit 3 <span class="unit-tab-count">28</span>
            </a>
            <a href="unit4.html" class="unit-tab">
              Unit 4 <span class="unit-tab-count">20</span>
            </a>
            <a href="unit5.html" class="unit-tab">
              Unit 5 <span class="unit-tab-count">24</span>
            </a>
          </div>

          <button id="focus-toggle" class="tool-btn" title="Toggle Immersive Focus Mode">
            <span class="tool-icon">⛶</span>
            <span class="tool-text">Focus Mode</span>
          </button>
          <div class="font-sizer">
            <button id="font-dec" title="Decrease font size">A-</button>
            <button id="font-reset" title="Reset font size">A</button>
            <button id="font-inc" title="Increase font size">A+</button>
          </div>
          <button id="theme-toggle" class="theme-btn" title="Toggle Theme">
            <span class="theme-icon">🌙</span>
            <span class="theme-text">Dark</span>
          </button>
        </div>
      </div>

      <!-- Course Hero Banner -->
      <header class="course-hero">
        <div class="hero-badge">Curriculum-Aligned Engineering Reference • AKTU KCS-054</div>
        <h1>Object Oriented System Design (OOSD)</h1>
        <h2>Unit 1: Object Orientation Concepts, Identity, Polymorphism, Modelling & UML Architecture</h2>
        <p class="hero-desc">
          An exhaustive, curriculum-aligned study portal covering all 23 syllabus topics in unrestricted continuous flow. Features real-life analogies, commented C++ code implementations, high-contrast vector architecture diagrams, deep comparison matrices, and AKTU university exam questions.
        </p>

        <div class="quick-stats-pills">
          <span class="q-pill">📚 6 Core Parts</span>
          <span class="q-pill">📌 23 Exhaustive Sections</span>
          <span class="q-pill">💡 Real-Life Analogies</span>
          <span class="q-pill">💻 Commented C++ Code</span>
          <span class="q-pill">📐 23 Vector SVGs</span>
          <span class="q-pill">🎓 AKTU PYQs & Solutions</span>
          <span class="q-pill">⚡ Continuous Unrestricted Scroll</span>
        </div>
      </header>

      <!-- All 23 Content Sections -->
      <div class="sections-wrapper">
        {sections_html}
      </div>

      <footer class="app-footer">
        <div class="footer-content">
          <h4>OOSD Unit 1: Complete Study Master Portal</h4>
          <p>Designed for Computer Science & Engineering (B.Tech / MCA / Software Engineering) students.</p>
          <div class="footer-links">
            <a href="#u1-sec-1">Back to Section 01</a> • 
            <a href="index.html">Proceed to Unit 2 (36 Topics)</a> • 
            <a href="unit3.html">Proceed to Unit 3 (28 Topics)</a> • 
            <a href="unit4.html">Proceed to Unit 4 (20 Topics)</a> • 
            <a href="unit5.html">Proceed to Unit 5 (24 Topics)</a> • 
            <a href="#top">Top of Page</a>
          </div>
        </div>
      </footer>
    </main>
  </div>

  <!-- Floating Sticky Navigation Indicator Pill -->
  <div id="floating-pill" class="floating-pill">
    <button id="float-prev" class="float-btn" title="Previous Topic">❮</button>
    <div class="float-center" id="float-label">
      <span class="f-num">01</span>
      <span class="f-text">Meaning of Object Orientation</span>
    </div>
    <button id="float-next" class="float-btn" title="Next Topic">❯</button>
  </div>

  <script src="app.js"></script>
</body>
</html>
"""

with open("unit1.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"unit1.html generated successfully! File size: {os.path.getsize('unit1.html')} bytes")
