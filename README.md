# Object Oriented System Design (OOSD) — Interactive Master Study Portal

An exhaustive, interactive, university-curriculum-aligned web learning portal covering the complete syllabus for **Object Oriented System Design (OOSD / AKTU KCS-054)**. Designed for Computer Science & Engineering students (B.Tech / MCA / Software Engineering).

---

## 🚀 Features & Highlights

- **Complete 5-Unit Curriculum (131 Topics Total)**:
  - **Unit 1 (`unit1.html`)**: Object Orientation Concepts, Object Identity, Polymorphism, Modeling & UML Architecture (23 Topics).
  - **Unit 2 (`index.html`)**: Basic Structural, Behavioral & Architectural Modeling, Class & Object Diagrams, Advanced Relationships (36 Topics).
  - **Unit 3 (`unit3.html`)**: Object-Oriented Analysis (OOA), Object-Oriented Design (OOD), Object Design, SA/SD vs OOA/OOD, Jackson Structured Development (JSD) & Non-OO Implementation (28 Topics).
  - **Unit 4 (`unit4.html`)**: C++ Basics, Namespaces, Operators, Dynamic Memory (`new`/`delete`), Functions, References, Inline Functions, Function Overloading & Dynamic Memory Management (20 Topics).
  - **Unit 5 (`unit5.html`)**: Objects & Classes, Static Members, Constructors & Destructors, Operator Overloading, Type Conversion, Inheritance Hierarchies, Virtual Base Classes, Pointers & Dynamic Dispatch, Virtual Functions & Abstract Classes (24 Topics).
- **131 Handcrafted XML Vector SVGs**: High-contrast architecture flowcharts, UML class diagrams, inheritance diamonds, and memory layouts. Zero external raster images (`.png`/`.jpg`).
- **131 Real-Life Analogies**: Intuitive real-world scenarios for every single concept (e.g. *Blueprint vs Villa*, *Hospital Triage Dispatcher*, *ISO Wall Socket*, *Intermodal Shipping Container Hub*).
- **Extensively Commented C/C++ Code**: Practical implementations with step-by-step commentary and realistic terminal outputs.
- **Dual-Theme Engine**:
  - **Light Mode**: Crisp white terminal theme (`#ffffff`) with syntax highlighting.
  - **Dark Mode**: Deep obsidian theme (`#080c14`) with glowing accents.
  - Theme preference persists across all units via `localStorage`.
- **Interactive Reading Utilities**:
  - Unrestricted continuous vertical scroll per unit.
  - Responsive sidebar navigation with active scrollspy and progress indicator.
  - "Mark as Studied" checkmarks with progress tracking saved in browser storage.
  - Instant live search filter across all section titles and keywords.
  - Immersive Focus Mode (Zen Reading) and dynamic font sizing (`A-`, `A`, `A+`).
  - Seamless 5-way switcher tabs connecting all unit portals.

---

## 📂 Project Structure

```text
├── index.html                # Unit 2: Basic Structural, Behavioral & Architectural Modeling (36 Topics)
├── unit1.html                # Unit 1: OO Concepts, Identity & UML (23 Topics)
├── unit3.html                # Unit 3: OOA, OOD, Object Design, SA/SD & JSD (28 Topics)
├── unit4.html                # Unit 4: C++ Basics, Memory Management & Functions (20 Topics)
├── unit5.html                # Unit 5: Classes, Inheritance & Polymorphism (24 Topics)
├── style.css                 # Master modern dual-theme stylesheet
├── app.js                    # Core application engine (Scrollspy, Search, Theme, Progress)
├── build_unit1_website.py    # Unit 1 generator script
├── build_website.py          # Unit 2 generator script
├── build_unit3_website.py    # Unit 3 generator script
├── build_unit4_website.py    # Unit 4 generator script
├── build_unit5_website.py    # Unit 5 generator script
├── generate_unit*.py         # Modular section content generators for all units
├── README.md                 # Project documentation
└── .gitignore                # Git ignore rules
```

---

## 💻 Quick Start & Local Preview

Simply open any of the HTML files directly in your web browser:
```bash
# Preview Unit 1
xdg-open unit1.html

# Preview Unit 2 (Homepage)
xdg-open index.html

# Preview Unit 5
xdg-open unit5.html
```

Or start a local lightweight web server:
```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

---

## 🌐 Deploying to GitHub Pages

1. Push this repository to GitHub.
2. In your repository on GitHub, navigate to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
4. Select the `main` branch and `/ (root)` folder, then click **Save**.
5. Your interactive study portal will be live at `https://<your-username>.github.io/<repo-name>/`.
