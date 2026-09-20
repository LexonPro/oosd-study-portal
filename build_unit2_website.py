# build_unit2_website.py: Assembles unit2.html from Parts 1 to 6 with analogies and code examples
import os
import json
import generate_unit2_part1
import generate_unit2_part2
import generate_unit2_part3
import generate_unit2_part4
import generate_unit2_part5
import generate_unit2_part6

part1 = generate_unit2_part1.get_unit2_part1_sections()
part2 = generate_unit2_part2.get_unit2_part2_sections()
part3 = generate_unit2_part3.get_unit2_part3_sections()
part4 = generate_unit2_part4.get_unit2_part4_sections()
part5 = generate_unit2_part5.get_unit2_part5_sections()
part6 = generate_unit2_part6.get_unit2_part6_sections()

all_sections = part1 + part2 + part3 + part4 + part5 + part6

print(f"Total Unit 2 sections assembled: {len(all_sections)}")
assert len(all_sections) == 36, f"Expected 36 sections, found {len(all_sections)}"

parts_meta = [
    {"num": 1, "title": "PART 1 — Basic Structural Modeling", "theme_class": "part-blue", "sections": part1},
    {"num": 2, "title": "PART 2 — Class and Object Diagram", "theme_class": "part-cyan", "sections": part2},
    {"num": 3, "title": "PART 3 — Collaboration Diagram", "theme_class": "part-purple", "sections": part3},
    {"num": 4, "title": "PART 4 — Sequence Diagram", "theme_class": "part-rose", "sections": part4},
    {"num": 5, "title": "PART 5 — Basic Behavioural Modeling", "theme_class": "part-green", "sections": part5},
    {"num": 6, "title": "PART 6 — Architectural Modeling", "theme_class": "part-amber", "sections": part6},
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
    
    prev_link = f"""<a href="#{prev_sec['id']}" class="nav-btn prev-btn">← {prev_sec['number']}. {prev_sec['title']}</a>""" if prev_sec else """<a href="unit1.html#u1-sec-23" class="nav-btn prev-btn">← Unit 1 (Sec 23)</a>"""
    next_link = f"""<a href="#{next_sec['id']}" class="nav-btn next-btn">{next_sec['number']}. {next_sec['title']} →</a>""" if next_sec else """<a href="unit3.html#u3-sec-1" class="nav-btn next-btn">Proceed to Unit 3 (Sec 01) →</a>"""
    
    content_sections_html.append(f"""
    <section id="{s['id']}" class="topic-section" data-num="{s['number']}">
      <div class="section-meta">
        <span class="part-pill">{s['part']}</span>
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
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>OOSD — UNIT 2: Complete Master Study Guide (All 36 Topics)</title>
  <meta name="description" content="Comprehensive, unrestricted interactive study portal covering all 36 topics of Object Oriented System Design Unit 2 with real-life analogies, commented C++ code implementations, vector UML diagrams, architectural comparisons, and exam questions.">
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body id="top" data-unit="unit2">

  <!-- Mobile Header & Toggle -->
  <header class="mobile-nav-header">
    <button id="sidebar-toggle" aria-label="Toggle Slidebar Navigation" class="icon-btn">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>
    <div class="mobile-logo">
      <span class="accent-text">OOSD</span> Unit 2 (36 Topics)
    </div>
    <div class="mobile-controls">
      <div class="unit-switcher">
        <a href="unit1.html" class="unit-tab" title="Go to Unit 1">U1</a>
        <a href="unit2.html" class="unit-tab active" title="Current: Unit 2">U2</a>
        <a href="unit3.html" class="unit-tab" title="Go to Unit 3">U3</a>
        <a href="unit4.html" class="unit-tab" title="Go to Unit 4">U4</a>
        <a href="unit5.html" class="unit-tab" title="Go to Unit 5">U5</a>
      </div>
      <button id="theme-toggle-mob" class="icon-btn" title="Toggle Dark/Light Mode">☀️</button>
    </div>
  </header>

  <div class="app-layout">
    <!-- SLIDEBAR / SIDEBAR (All 36 Headings) -->
    <aside id="sidebar" class="sidebar">
      <div class="sidebar-header">
        <div class="logo-row">
          <div class="logo-mark">U2</div>
          <div class="logo-text">
            <h3>OOSD Unit 2</h3>
            <span class="subtitle-tag">Complete Syllabus (36 Topics)</span>
          </div>
        </div>

        <!-- 5-Way Unit Switcher Pill -->
        <div class="unit-switcher" style="margin: 12px 0 6px 0; width: 100%; justify-content: center; gap: 4px;">
          <a href="unit1.html" class="unit-tab" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
            U1 <span class="unit-tab-count">23</span>
          </a>
          <a href="unit2.html" class="unit-tab active" style="flex: 1; justify-content: center; padding: 5px 2px; font-size: 11px;">
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
          <input type="text" id="sidebar-search" placeholder="Search 36 topics (e.g. sequence, state)..." autocomplete="off">
          <button id="clear-search" class="clear-btn" title="Clear search" style="display: none;">✕</button>
        </div>
        <div class="sidebar-stats">
          <div class="stat-item">
            <span class="stat-val" id="current-sec-indicator">01 / 36</span>
            <span class="stat-lbl">Active Topic</span>
          </div>
          <div class="stat-item">
            <span class="stat-val">36</span>
            <span class="stat-lbl">Total Topics</span>
          </div>
        </div>

        <div class="sidebar-controls-row">
          <button id="expand-all-btn" class="mini-btn" title="Expand/Collapse All Parts">Toggle All</button>
        </div>
      </div>

      <!-- Navigation Tree: All 36 Headings Grouped Under Parts -->
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

    <!-- MAIN SCROLLABLE CONTENT (1 to 36 Without Restriction) -->
    <main class="main-content">
      <!-- Top Sticky Header -->
      <div class="top-nav-bar">
        <div class="breadcrumbs">
          <span class="bc-course">OOSD</span>
          <span class="bc-sep">/</span>
          <span class="bc-unit">Unit 2 Master</span>
          <span class="bc-sep">/</span>
          <span class="bc-active" id="top-active-title">01. Basic Structural Modeling</span>
        </div>

        <div class="action-tools">
          <!-- 5-Way Unit Switcher in Desktop Top Bar -->
          <div class="unit-switcher">
            <a href="unit1.html" class="unit-tab">
              Unit 1 <span class="unit-tab-count">23</span>
            </a>
            <a href="unit2.html" class="unit-tab active">
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
          
          <div class="zoom-controls" title="Zoom In / Out">
            <button id="zoom-dec" title="Zoom Out (Ctrl -)">−</button>
            <span id="zoom-level" class="zoom-level-text" title="Click to Reset Zoom">100%</span>
            <button id="zoom-inc" title="Zoom In (Ctrl +)">+</button>
          </div>

          <button id="theme-toggle" class="theme-btn" title="Toggle Theme">
            <span class="theme-icon">☀️</span>
            <span class="theme-text">Light</span>
          </button>
        </div>
      </div>

      <!-- Course Hero Banner -->
      <header class="course-hero">
        <div class="hero-badge">Curriculum-Aligned Engineering Reference • AKTU KCS-054</div>
        <h1>Object Oriented System Design (OOSD)</h1>
        <h2>Unit 2: Basic Structural, Behavioural & Architectural Modeling</h2>
        <p class="hero-desc">
          A fully articulated study guide covering all 36 topics in continuous unrestricted flow. Features real-life analogies, commented C++ code implementations, dedicated vector UML diagrams, architectural comparison matrices, AKTU university exam questions with answers, and 30-second rapid revision checkpoints.
        </p>

        <div class="quick-stats-pills">
          <span class="q-pill">📚 6 Core Parts</span>
          <span class="q-pill">📌 36 Exhaustive Sections</span>
          <span class="q-pill">💡 Real-Life Analogies</span>
          <span class="q-pill">💻 Commented C++ Code</span>
          <span class="q-pill">📐 36 Vector UML Diagrams</span>
          <span class="q-pill">🎓 AKTU PYQs & Solutions</span>
          <span class="q-pill">⚡ Continuous Unrestricted Scroll</span>
        </div>
      </header>

      <!-- All 36 Content Sections -->
      <div class="sections-wrapper">
        {sections_html}
      </div>

      <footer class="app-footer">
        <div class="footer-content">
          <h4>OOSD Unit 2: Complete Study Master Portal</h4>
          <p>Designed for Computer Science & Engineering (B.Tech / MCA / Software Engineering) students.</p>
          <div class="footer-links">
            <a href="unit1.html">Unit 1: OO Concepts (23 Topics)</a> • 
            <a href="#sec-1">Back to Section 01</a> • 
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
      <span class="f-text">Basic Structural Modeling</span>
    </div>
    <button id="float-next" class="float-btn" title="Next Topic">❯</button>
  </div>

  <script src="app.js"></script>
</body>
</html>
"""

# Write unit2.html
with open("unit2.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"unit2.html generated successfully! Size: {os.path.getsize('unit2.html')} bytes")

# Write index.html as the primary entry point that always redirects to Unit 1 first!
index_redirect_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=unit1.html">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>OOSD Master Portal — Redirecting to Unit 1...</title>
  <link rel="canonical" href="unit1.html">
  <script>
    // If a hash like #sec-15 was provided, preserve it and route to unit2.html; otherwise always route to unit1.html!
    if (window.location.hash && window.location.hash.startsWith('#sec-')) {
      window.location.replace("unit2.html" + window.location.hash);
    } else {
      window.location.replace("unit1.html");
    }
  </script>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
      background: #f8fafc;
      color: #0f172a;
      text-align: center;
    }
    .redirect-card {
      background: #ffffff;
      padding: 36px 44px;
      border-radius: 14px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      border: 1px solid #e2e8f0;
      max-width: 460px;
    }
    h2 {
      margin-bottom: 12px;
      font-size: 1.35rem;
      color: #0f172a;
    }
    p {
      color: #64748b;
      margin-bottom: 18px;
      line-height: 1.5;
    }
    a {
      color: #2563eb;
      font-weight: 600;
      text-decoration: none;
    }
    .spinner {
      width: 32px;
      height: 32px;
      margin: 16px auto;
      border: 3px solid #e2e8f0;
      border-top-color: #2563eb;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
  </style>
</head>
<body>
  <div class="redirect-card">
    <div class="spinner"></div>
    <h2>OOSD Master Study Portal</h2>
    <p>Redirecting to <a href="unit1.html">Unit 1: Object Orientation Concepts &amp; Architecture</a>...</p>
  </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_redirect_html)

print(f"index.html router generated successfully! Size: {os.path.getsize('index.html')} bytes")

