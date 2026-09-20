# generate_unit1_part4.py: Part 4 (UML), Part 5 (Conceptual Model) & Part 6 (Link & Association) (Sections 17 to 23)

def get_unit1_part4_sections():
    return [
        # -------------------------------------------------------------
        # Section 17: Introduction to UML
        # -------------------------------------------------------------
        {
            "id": "u1-sec-17",
            "number": "17",
            "part": "Part 4 — Unified Modeling Language (UML)",
            "title": "Introduction to UML",
            "subtitle": "Origins, The Three Amigos, OMG Standardization & The 4 Core Objectives",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Industry Standard</div>
    <h3>What is UML?</h3>
    <p>The <strong>Unified Modeling Language (UML)</strong> is a standardized, general-purpose visual modeling language used in software engineering to <strong>visualize, specify, construct, and document</strong> the artifacts of a software-intensive system.</p>
    <p>According to AKTU Quantum (Que 1.20), UML is a pictorial blueprinting language. Crucially, <em>UML is not a programming language</em>, but visual models drawn in UML can be mapped directly into object-oriented programming languages (like C++, Java, and C#) through automated forward engineering.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Universal Blueprint Standard &amp; Musical Notation</div>
  <p>In the 1800s, architects across different countries used private, incompatible drafting symbols, causing catastrophic construction errors when multinational teams collaborated. Standardized civil architectural schematics eliminated this. Similarly, in music, whether a symphony is performed by a pianist in Tokyo, a violinist in Vienna, or an orchestra in New York, all read the exact same <strong>standard musical staff notation</strong> (clefs, notes, tempos). UML serves as the universal sheet music for software engineering!</p>
</div>

<div class="subtopics-container">
  <h4>History &amp; The Four Core Goals of UML</h4>

  <div class="detail-block">
    <h5>1. The 'Method War' &amp; The Three Amigos</h5>
    <p>In the early 1990s, the software industry suffered from fragmented OO methodologies: Grady Booch (Booch Method), James Rumbaugh (OMT), and Ivar Jacobson (OOSE / Objectory). In 1994–1996, the three leaders joined forces at Rational Software (popularly nicknamed <strong>"The Three Amigos"</strong>) to unify their techniques into UML. In 1997, the <strong>Object Management Group (OMG)</strong> officially adopted UML as the international software engineering standard.</p>
  </div>

  <div class="detail-block">
    <h5>2. The Four Pillars of UML (V-S-C-D)</h5>
    <ul>
      <li><strong>Visualizing:</strong> Translates mental models and algorithms into explicit, standardized graphical diagrams.</li>
      <li><strong>Specifying:</strong> Provides unambiguous, precise structural and behavioral blueprints of what a system must execute.</li>
      <li><strong>Constructing:</strong> Directly enables Forward Engineering (generating executable class skeletons from diagrams) and Reverse Engineering (generating UML diagrams from legacy code).</li>
      <li><strong>Documenting:</strong> Captures critical architectural design decisions, constraints, and requirements across the complete software lifecycle.</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>The 4 Core Goals of UML (V-S-C-D Matrix)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Objective</th>
        <th>What It Accomplishes</th>
        <th>Engineering Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Visualizing</strong></td>
        <td>Makes abstract software logic tangible via standard visual notations</td>
        <td>Eliminates miscommunication between developers and stakeholders</td>
      </tr>
      <tr>
        <td><strong>2. Specifying</strong></td>
        <td>Defines precise requirements, classes, interfaces, and behaviors</td>
        <td>Creates unambiguous contractual specifications before coding</td>
      </tr>
      <tr>
        <td><strong>3. Constructing</strong></td>
        <td>Ties visual models directly to programming language source code</td>
        <td>Facilitates automated code generation and round-trip engineering</td>
      </tr>
      <tr>
        <td><strong>4. Documenting</strong></td>
        <td>Records architectural decisions, requirements, and system boundaries</td>
        <td>Preserves institutional knowledge surviving team turnover</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Three Amigos Unification &amp; The 4 Goals of UML</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Three Pioneers (Left) -->
      <g transform="translate(30, 25)">
        <rect width="210" height="230" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="210" height="32" rx="8" fill="#0369a1"/>
        <text x="105" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">THE THREE AMIGOS (1995)</text>

        <rect x="15" y="45" width="180" height="46" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="25" y="64" fill="#38bdf8" font-size="10" font-weight="bold">Grady Booch</text>
        <text x="25" y="80" fill="#94a3b8" font-size="8">Booch Method (Design &amp; Classes)</text>

        <rect x="15" y="102" width="180" height="46" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="25" y="121" fill="#38bdf8" font-size="10" font-weight="bold">James Rumbaugh</text>
        <text x="25" y="137" fill="#94a3b8" font-size="8">OMT (Analysis &amp; Domain)</text>

        <rect x="15" y="160" width="180" height="46" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="25" y="179" fill="#38bdf8" font-size="10" font-weight="bold">Ivar Jacobson</text>
        <text x="25" y="195" fill="#94a3b8" font-size="8">OOSE (Use Cases &amp; Actors)</text>
      </g>

      <!-- Merge Arrow -->
      <path d="M 245 140 L 305 140" stroke="#60a5fa" stroke-width="3" marker-end="url(#u1-uml-arr)"/>
      <text x="275" y="130" fill="#60a5fa" font-size="8" font-weight="bold" text-anchor="middle">UNIFIED</text>

      <!-- Central UML / OMG Standard -->
      <g transform="translate(315, 65)">
        <rect width="180" height="150" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2.5"/>
        <rect width="180" height="32" rx="10" fill="#7e22ce"/>
        <text x="90" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">UML (OMG STANDARD)</text>

        <circle cx="90" cy="85" r="30" fill="#581c87" stroke="#c084fc" stroke-width="2"/>
        <text x="90" y="90" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">UML 2.x</text>

        <text x="90" y="132" fill="#e9d5ff" font-size="9" text-anchor="middle">Universal Visual Modeling</text>
        <text x="90" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Standardized 1997</text>
      </g>

      <!-- Distribution Arrow -->
      <path d="M 500 140 L 560 140" stroke="#a855f7" stroke-width="3" marker-end="url(#u1-uml-arr-purple)"/>
      <text x="530" y="130" fill="#c084fc" font-size="8" font-weight="bold" text-anchor="middle">DELIVERS</text>

      <!-- 4 Core Goals (Right) -->
      <g transform="translate(570, 25)">
        <rect width="220" height="230" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="220" height="32" rx="8" fill="#047857"/>
        <text x="110" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">4 CORE OBJECTIVES (V-S-C-D)</text>

        <rect x="15" y="45" width="190" height="36" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
        <text x="25" y="67" fill="#6ee7b7" font-size="9" font-weight="bold">1. Visualizing</text>
        <text x="105" y="67" fill="#94a3b8" font-size="8">Graphic representations</text>

        <rect x="15" y="90" width="190" height="36" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
        <text x="25" y="112" fill="#6ee7b7" font-size="9" font-weight="bold">2. Specifying</text>
        <text x="105" y="112" fill="#94a3b8" font-size="8">Precise unambiguous logic</text>

        <rect x="15" y="135" width="190" height="36" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
        <text x="25" y="157" fill="#6ee7b7" font-size="9" font-weight="bold">3. Constructing</text>
        <text x="105" y="157" fill="#94a3b8" font-size="8">Forward/Reverse code gen</text>

        <rect x="15" y="180" width="190" height="36" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
        <text x="25" y="202" fill="#6ee7b7" font-size="9" font-weight="bold">4. Documenting</text>
        <text x="105" y="202" fill="#94a3b8" font-size="8">Architectural lifecycle trace</text>
      </g>

      <defs>
        <marker id="u1-uml-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
        <marker id="u1-uml-arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2014-15):</strong> <em>"What do you mean by UML? Discuss the goals of UML in software design."</em> [5 Marks - Que 1.20, Que 1.22]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Write that UML stands for Unified Modeling Language. Mention that it was created by Grady Booch, James Rumbaugh, and Ivar Jacobson ("The Three Amigos") and standardized by the OMG in 1997. Explain the four fundamental goals: <strong>Visualizing, Specifying, Constructing, and Documenting</strong>. Note that it is not a programming language but facilitates code generation.
  </div>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 18: Why UML is Required
        # -------------------------------------------------------------
        {
            "id": "u1-sec-18",
            "number": "18",
            "part": "Part 4 — Unified Modeling Language (UML)",
            "title": "Why UML is Required",
            "subtitle": "The 6 Software Engineering Tasks Powered by UML (Specification to Documentation)",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Engineering Justification</div>
    <h3>Why is UML Required in Modern Engineering?</h3>
    <p>Before UML, software development suffered from natural language ambiguity. Textual requirement documents written in English were interpreted completely differently by clients, architects, database administrators, and junior programmers.</p>
    <p>According to AKTU Quantum (Que 1.22), UML is required to help system and software developers accomplish <strong>six core software engineering tasks</strong>: <strong>(1) Specification, (2) Visualization, (3) Architecture Design, (4) Construction, (5) Simulation &amp; Testing, and (6) Documentation</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Tower of Babel vs The International Electrical Schematic</div>
  <p>In the ancient allegory of the Tower of Babel, construction collapsed because workers suddenly spoke different languages and could not understand each other's words. Without UML, a software company experiences the same breakdown: a business analyst writes <em>"The system shall authenticate rapidly"</em>, the security engineer expects Kerberos cryptography, and the front-end developer builds a hardcoded login popup! An electrical schematic symbol for a resistor (zigzag line) or ground (three parallel declining bars) means the exact same thing in Berlin, Bangalore, or Boston. UML prevents the Software Tower of Babel!</p>
</div>

<div class="subtopics-container">
  <h4>The 6 Tasks Accomplished with UML (AKTU Que 1.22)</h4>

  <div class="detail-block">
    <h5>1. Specification</h5>
    <p>UML provides unambiguous semantic models specifying what the system must do. It details class structures, attributes, operations, constraints, and collaborations without leaving room for subjective misinterpretation.</p>
  </div>

  <div class="detail-block">
    <h5>2. Visualization</h5>
    <p>Human cognition processes visual spatial patterns orders of magnitude faster than dense textual code. UML diagrams expose circular dependencies, inheritance depths, and architectural choke-points at a glance.</p>
  </div>

  <div class="detail-block">
    <h5>3. Architecture Design</h5>
    <p>UML facilitates organizing large systems into logical subsystems, tiers, and deployment nodes (via Package, Component, and Deployment diagrams), ensuring scalability and separation of concerns.</p>
  </div>

  <div class="detail-block">
    <h5>4. Construction (Code Generation)</h5>
    <p>UML models are formal enough to be parsed by Computer-Aided Software Engineering (CASE) tools to automatically generate boilerplate class skeletons, interfaces, getters/setters, and database DDL schemas.</p>
  </div>

  <div class="detail-block">
    <h5>5. Simulation &amp; Testing</h5>
    <p>Dynamic diagrams (Sequence diagrams, Statecharts, Activity diagrams) can be executed in simulators to verify protocol correctness, identify deadlocks, and derive test cases prior to implementation.</p>
  </div>

  <div class="detail-block">
    <h5>6. Documentation</h5>
    <p>UML diagrams serve as living institutional memory. When onboarding new engineers or undergoing architectural audits, UML documentation explains the rationale behind design choices.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Textual Requirements vs Formal UML Modeling</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Aspect</th>
        <th>Unstructured Natural Language (English Docs)</th>
        <th>Formal Visual UML Modeling</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Ambiguity</strong></td>
        <td>High; open to multiple conflicting interpretations</td>
        <td>Virtually zero; standardized OMG semantic definitions</td>
      </tr>
      <tr>
        <td><strong>Tool Processability</strong></td>
        <td>Difficult for automated tools to parse or validate</td>
        <td>Can be parsed by CASE tools for automated code generation</td>
      </tr>
      <tr>
        <td><strong>Architecture Verification</strong></td>
        <td>Impossible to mathematically verify structural correctness</td>
        <td>Formal consistency and completeness checking</td>
      </tr>
      <tr>
        <td><strong>Evolution &amp; Maintenance</strong></td>
        <td>Becomes stale and out-of-date rapidly</td>
        <td>Supports round-trip engineering synchronizing code and model</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The 6 Software Engineering Tasks Powered by UML (AKTU Que 1.22)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Task 1: Specification -->
      <g transform="translate(30, 25)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="230" height="26" rx="8" fill="#0369a1"/>
        <text x="115" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1. SPECIFICATION</text>
        <text x="15" y="48" fill="#38bdf8" font-size="9" font-weight="bold">Unambiguous Contracts</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="8">• Exact class APIs &amp; signatures</text>
        <text x="15" y="84" fill="#94a3b8" font-size="8">• Pre/post-conditions &amp; constraints</text>
      </g>

      <!-- Task 2: Visualization -->
      <g transform="translate(295, 25)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="230" height="26" rx="8" fill="#7e22ce"/>
        <text x="115" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">2. VISUALIZATION</text>
        <text x="15" y="48" fill="#c084fc" font-size="9" font-weight="bold">Cognitive Spatial Mapping</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="8">• Graphical system structure</text>
        <text x="15" y="84" fill="#94a3b8" font-size="8">• Immediate flaw detection</text>
      </g>

      <!-- Task 3: Architecture Design -->
      <g transform="translate(560, 25)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="230" height="26" rx="8" fill="#047857"/>
        <text x="115" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">3. ARCHITECTURE DESIGN</text>
        <text x="15" y="48" fill="#6ee7b7" font-size="9" font-weight="bold">System Partitioning</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="8">• Subsystems &amp; packages</text>
        <text x="15" y="84" fill="#94a3b8" font-size="8">• Hardware nodes &amp; tiers</text>
      </g>

      <!-- Task 4: Construction -->
      <g transform="translate(30, 150)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="230" height="26" rx="8" fill="#b45309"/>
        <text x="115" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">4. CONSTRUCTION</text>
        <text x="15" y="48" fill="#fcd34d" font-size="9" font-weight="bold">Automated Forward Eng.</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="8">• Generates C++/Java skeletons</text>
        <text x="15" y="84" fill="#94a3b8" font-size="8">• Database schema DDL exports</text>
      </g>

      <!-- Task 5: Simulation & Testing -->
      <g transform="translate(295, 150)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
        <rect width="230" height="26" rx="8" fill="#9f1239"/>
        <text x="115" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">5. SIMULATION &amp; TESTING</text>
        <text x="15" y="48" fill="#fca5a5" font-size="9" font-weight="bold">Behavioral Verification</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="8">• Execute state machine models</text>
        <text x="15" y="84" fill="#94a3b8" font-size="8">• Generate automated test fixtures</text>
      </g>

      <!-- Task 6: Documentation -->
      <g transform="translate(560, 150)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#60a5fa" stroke-width="2"/>
        <rect width="230" height="26" rx="8" fill="#1d4ed8"/>
        <text x="115" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">6. DOCUMENTATION</text>
        <text x="15" y="48" fill="#93c5fd" font-size="9" font-weight="bold">Living Knowledge Base</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="8">• Preserves design rationales</text>
        <text x="15" y="84" fill="#94a3b8" font-size="8">• Survives personnel turnover</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15):</strong> <em>"Why is UML required? What are the basic architecture of UML?"</em> [5 Marks - Que 1.22]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Memorize and list the six exact tasks: <strong>(i) Specification, (ii) Visualization, (iii) Architecture design, (iv) Construction, (v) Simulation and testing, and (vi) Documentation</strong>. Explain each task in 1–2 crisp sentences showing why natural language text is inadequate for enterprise systems.
  </div>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 19: Advantages and Limitations of UML
        # -------------------------------------------------------------
        {
            "id": "u1-sec-19",
            "number": "19",
            "part": "Part 4 — Unified Modeling Language (UML)",
            "title": "Advantages and Limitations of UML",
            "subtitle": "Critical Evaluation: Standardization & Visual Power vs Complexity & Sync Overhead",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Engineering Assessment</div>
    <h3>Evaluating UML: Strengths vs Trade-Offs</h3>
    <p>While UML is universally acclaimed as the gold standard for visual software modeling, pragmatic software engineering requires understanding both its <strong>immense advantages</strong> and its <strong>inherent limitations</strong>.</p>
    <p>According to AKTU Quantum (Que 1.21), UML bridges communication gaps and provides unified standards; however, it is frequently criticized for being excessively large, complex to master, and challenging to keep synchronized with rapidly evolving production source code.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Professional Swiss Army Workstation Tool</div>
  <p>Imagine purchasing an industrial <strong>Swiss Army Multi-Tool Workstation</strong> with 45 specialized blades, pliers, laser cutters, and torque wrenches. For a master mechanic building an aircraft engine, every tool serves a specific purpose (<em>UML's 14 specialized diagrams</em>). But for a hiker who just wants to peel an apple, carrying a 10-pound metallic tool is clumsy, slow, and expensive. UML is immensely powerful for complex architectures, but excessive when applied dogmatically to trivial scripts!</p>
</div>

<div class="subtopics-container">
  <h4>Pros &amp; Cons Analysis (AKTU Que 1.21)</h4>

  <div class="detail-block">
    <h5>Advantages (Pros) of UML</h5>
    <ul>
      <li><strong>Wide Industry Acceptance:</strong> Universally recognized across academia, tech giants, and defense contracting.</li>
      <li><strong>Supports OOAD Methodology:</strong> Natively models inheritance, encapsulation, polymorphism, and dynamic binding.</li>
      <li><strong>Bridges Communication Gaps:</strong> Creates a shared visual language between System Analysts, Developers, Clients, and QA engineers.</li>
      <li><strong>Easy to Understand:</strong> Even non-programmers can grasp high-level Use Case and Activity flowcharts.</li>
      <li><strong>Extensible via Profiles:</strong> Can be customized for specific domains (e.g. SysML for systems, UML-RT for real-time embedded systems) using stereotypes (<code>&lt;&lt;...&gt;&gt;</code>) and tagged values.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Limitations (Cons) of UML</h5>
    <ul>
      <li><strong>Language Bloat &amp; Complexity:</strong> With 14 official diagram types and hundreds of notational variations, mastering UML takes significant study.</li>
      <li><strong>Code Synchronization Overhead:</strong> Developers frequently modify source code directly during agile sprints, leaving UML diagrams outdated unless automated round-trip CASE tools are enforced.</li>
      <li><strong>Cannot Express All Runtime Conditions:</strong> Certain complex conditional algorithmic branches or race conditions are awkward to represent in sequence diagrams.</li>
      <li><strong>Commercial Tool Costs:</strong> Enterprise UML modeling software (Enterprise Architect, MagicDraw) requires expensive licensing.</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Comprehensive Matrix: Advantages vs Limitations (AKTU Que 1.21)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Aspect</th>
        <th>Advantages (Pros)</th>
        <th>Limitations (Cons)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Industry Standard</strong></td>
        <td>Universal OMG standard accepted worldwide</td>
        <td>Can lead to dogmatic bureaucratic over-documentation</td>
      </tr>
      <tr>
        <td><strong>Communication</strong></td>
        <td>Bridges the gap between technical coders &amp; clients</td>
        <td>Non-technical clients may still struggle with complex class diagrams</td>
      </tr>
      <tr>
        <td><strong>Expressiveness</strong></td>
        <td>Covers static, dynamic, and deployment views</td>
        <td>Awkward for expressing fine-grained loops and complex conditionals</td>
      </tr>
      <tr>
        <td><strong>Maintenance</strong></td>
        <td>Provides durable architecture blueprints</td>
        <td>High effort required to keep diagrams synchronized with code</td>
      </tr>
      <tr>
        <td><strong>Cost &amp; Tooling</strong></td>
        <td>Rich open-source and enterprise tool ecosystem</td>
        <td>Commercial CASE tools are expensive and require training</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Balance Sheet of UML (Pros vs Cons)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Pros Box (Left) -->
      <g transform="translate(30, 25)">
        <rect width="365" height="230" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="365" height="32" rx="8" fill="#065f46"/>
        <text x="182" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">ADVANTAGES (PROS) OF UML</text>

        <rect x="15" y="45" width="335" height="32" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
        <text x="25" y="65" fill="#6ee7b7" font-size="9 font-weight=bold">• Global Industry Standard (OMG Certified)</text>

        <rect x="15" y="85" width="335" height="32" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
        <text x="25" y="105" fill="#6ee7b7" font-size="9 font-weight=bold">• Bridges Technical &amp; Non-Technical Gaps</text>

        <rect x="15" y="125" width="335" height="32" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
        <text x="25" y="145" fill="#6ee7b7" font-size="9 font-weight=bold">• Native Support for Full OOAD Lifecycle</text>

        <rect x="15" y="165" width="335" height="32" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
        <text x="25" y="185" fill="#6ee7b7" font-size="9 font-weight=bold">• Supports Automated Forward &amp; Reverse Eng.</text>

        <text x="182" y="218" fill="#34d399" font-size="9" text-anchor="middle">Result: High software quality &amp; clear architectural vision</text>
      </g>

      <!-- Cons Box (Right) -->
      <g transform="translate(425, 25)">
        <rect width="365" height="230" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
        <rect width="365" height="32" rx="8" fill="#9f1239"/>
        <text x="182" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">LIMITATIONS (CONS) OF UML</text>

        <rect x="15" y="45" width="335" height="32" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
        <text x="25" y="65" fill="#fca5a5" font-size="9 font-weight=bold">• Large, Bloated &amp; Complex (14 Diagram Types)</text>

        <rect x="15" y="85" width="335" height="32" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
        <text x="25" y="105" fill="#fca5a5" font-size="9 font-weight=bold">• Code Synchronization Burden (Diagrams go stale)</text>

        <rect x="15" y="125" width="335" height="32" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
        <text x="25" y="145" fill="#fca5a5" font-size="9 font-weight=bold">• Cannot Model All Granular Dynamic Conditions</text>

        <rect x="15" y="165" width="335" height="32" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
        <text x="25" y="185" fill="#fca5a5" font-size="9 font-weight=bold">• Commercial Modeling Software Costs Money</text>

        <text x="182" y="218" fill="#fca5a5" font-size="9" text-anchor="middle">Mitigation: Use lightweight UML (draw only key views)</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13):</strong> <em>"Describe the pros and cons of Unified Modeling Language (UML)."</em> [5 Marks - Que 1.21]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Structure your answer into clear bullet points. <strong>Pros:</strong> Wide industry acceptance, supports OOAD methodology, bridges communication gap between clients and developers, easy to understand for non-programmers, standardized. <strong>Cons:</strong> Criticized as large and complex, time-consuming to keep synchronized with actual code, sequence diagrams cannot represent every branch condition, enterprise tools cost money.
  </div>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 20: Conceptual Model of UML
        # -------------------------------------------------------------
        {
            "id": "u1-sec-20",
            "number": "20",
            "part": "Part 5 — Conceptual Model of UML",
            "title": "Conceptual Model of UML",
            "subtitle": "Domain Concepts vs Software Classes & The Classic Library System Model",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational UML Model</div>
    <h3>What is the Conceptual Model of UML?</h3>
    <p>A <strong>Conceptual Model</strong> (often called a <strong>Domain Model</strong>) is an abstract, visual representation made up of <strong>concepts and their real-world relationships</strong>.</p>
    <p>According to AKTU Quantum (Que 1.20), the conceptual model is the <strong>first step before drawing formal UML diagrams</strong>. It explains the structure of the application domain rather than the internal software implementation structure. It focuses entirely on <em>domain concepts</em> (real-world business entities) rather than software entities (such as database connections, UI buttons, or threads).</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: A City Subway Map vs The Train Engine Blueprints</div>
  <p>When passengers look at a <strong>transit map</strong> of the London Tube or Delhi Metro, they see a <em>conceptual model</em> of the transit domain: Stations, Lines (Red Line, Blue Line), and Transfer Junctions. It models how passengers navigate the city. It does not show the pneumatic brake pressure, the voltage of the third rail, or the maintenance shift schedule of train drivers. The conceptual model captures the essence of the real-world domain!</p>
</div>

<div class="subtopics-container">
  <h4>Three Major Elements of the Conceptual Model of UML</h4>
  <p>According to AKTU Quantum (Que 1.20), mastering the conceptual model requires understanding three integrated pillars:</p>
  <ul>
    <li><strong>1. UML Building Blocks:</strong> The basic vocabulary (Things, Relationships, and Diagrams).</li>
    <li><strong>2. Rules to Connect the Building Blocks:</strong> Syntactic and semantic rules dictating well-formed models (scope, visibility, integrity).</li>
    <li><strong>3. Common Mechanisms:</strong> Reusable design practices (specifications, adornments, common divisions, and extensibility mechanisms).</li>
  </ul>

  <div class="detail-block">
    <h5>The Library System Conceptual Model (AKTU Fig. 1.20.1)</h5>
    <p>In AKTU examinations, the canonical example is the <strong>Library Management System</strong> conceptual model:</p>
    <ul>
      <li><strong>Library:</strong> Central entity that contains items and manages registered users. (Multiplicity: <code>1 Library has * Users</code>, <code>1 Library contains 1..* Items</code>).</li>
      <li><strong>User:</strong> A domain patron with attribute <code>name</code> who <code>reserves * Items</code>, <code>borrows * Copies</code>, and <code>consults * Items</code>.</li>
      <li><strong>Item:</strong> An abstract catalog entry with attributes <code>Kind</code> and <code>title</code>. An Item has physical copies (<code>1 Item has_copies * Copy</code>).</li>
      <li><strong>Copy:</strong> A physical book on a shelf with attributes <code>location</code> and <code>status</code> (e.g. Available, Checked Out). Users borrow physical copies, not abstract catalog entries!</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Domain Conceptual Model vs Technical Implementation Class Diagram</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Dimension</th>
        <th>Conceptual Model (Domain Model)</th>
        <th>Implementation Class Diagram</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Focus</strong></td>
        <td>Real-world concepts and vocabulary of the problem domain</td>
        <td>Software entities, data types, and design patterns in solution domain</td>
      </tr>
      <tr>
        <td><strong>Attributes</strong></td>
        <td>High-level conceptual properties (e.g., <code>name</code>, <code>title</code>)</td>
        <td>Exact language types (e.g., <code>private std::string name;</code>)</td>
      </tr>
      <tr>
        <td><strong>Methods / Operations</strong></td>
        <td>Typically omitted; focuses on relationships and domain state</td>
        <td>Complete method signatures, visibility (<code>+</code>, <code>-</code>), parameter types</td>
      </tr>
      <tr>
        <td><strong>Target Audience</strong></td>
        <td>Domain experts, business analysts, clients, architects</td>
        <td>Software developers, database engineers, compiler runtimes</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Mapping: Structural Skeletons for Library Conceptual Entities</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>
<span class="c-keyword">#include &lt;vector&gt;</span>
<span class="c-keyword">#include &lt;memory&gt;</span>

<span class="c-comment">// Forward declarations</span>
<span class="c-keyword">class</span> Copy;
<span class="c-keyword">class</span> User;

<span class="c-comment">// Domain Concept: Abstract Catalog Item</span>
<span class="c-keyword">class</span> Item {
<span class="c-keyword">public</span>:
    <span class="c-type">std::string</span> kind;  <span class="c-comment">// Book, Journal, Media</span>
    <span class="c-type">std::string</span> title;
    <span class="c-type">std::vector</span>&lt;<span class="c-type">std::shared_ptr</span>&lt;Copy&gt;&gt; copies; <span class="c-comment">// 1 Item has_copies * Copy</span>

    Item(<span class="c-type">std::string</span> k, <span class="c-type">std::string</span> t) : kind(k), title(t) {}
};

<span class="c-comment">// Domain Concept: Physical Copy on Library Shelf</span>
<span class="c-keyword">class</span> Copy {
<span class="c-keyword">public</span>:
    <span class="c-type">std::string</span> location; <span class="c-comment">// Shelf 4B</span>
    <span class="c-type">std::string</span> status;   <span class="c-comment">// Available, Borrowed</span>
    <span class="c-type">std::shared_ptr</span>&lt;Item&gt; itemRef; <span class="c-comment">// Back-pointer to parent Item</span>

    Copy(<span class="c-type">std::string</span> loc, <span class="c-type">std::string</span> st) : location(loc), status(st) {}
};

<span class="c-comment">// Domain Concept: Library User</span>
<span class="c-keyword">class</span> User {
<span class="c-keyword">public</span>:
    <span class="c-type">std::string</span> name;
    <span class="c-type">std::vector</span>&lt;<span class="c-type">std::shared_ptr</span>&lt;Copy&gt;&gt; borrowedCopies; <span class="c-comment">// borrows * Copy</span>
    <span class="c-type">std::vector</span>&lt;<span class="c-type">std::shared_ptr</span>&lt;Item&gt;&gt; reservedItems;  <span class="c-comment">// reserves * Item</span>

    User(<span class="c-type">std::string</span> n) : name(n) {}

    <span class="c-type">void</span> borrowCopy(<span class="c-type">std::shared_ptr</span>&lt;Copy&gt; c) {
        c-&gt;status = <span class="c-string">"Borrowed"</span>;
        borrowedCopies.push_back(c);
        std::cout &lt;&lt; <span class="c-string">"[Transaction]: User "</span> &lt;&lt; name &lt;&lt; <span class="c-string">" borrowed copy at "</span> &lt;&lt; c-&gt;location &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    auto bookItem = std::make_shared&lt;Item&gt;(<span class="c-string">"Book"</span>, <span class="c-string">"Object-Oriented System Design"</span>);
    auto copy1 = std::make_shared&lt;Copy&gt;(<span class="c-string">"Rack-A-Row-2"</span>, <span class="c-string">"Available"</span>);
    bookItem-&gt;copies.push_back(copy1);

    <span class="c-type">User</span> student(<span class="c-string">"Aarav Mehta"</span>);
    student.borrowCopy(copy1);

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Conceptual Model for a Library System (AKTU Fig. 1.20.1)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="320" fill="#0f172a" rx="12"/>

      <!-- Library Entity (Top Center) -->
      <g transform="translate(320, 20)">
        <rect width="180" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="180" height="24" rx="8" fill="#0369a1"/>
        <text x="90" y="17" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Library</text>
        <text x="90" y="44" fill="#94a3b8" font-size="9" text-anchor="middle">Root Domain System</text>
      </g>

      <!-- User Entity (Left) -->
      <g transform="translate(60, 130)">
        <rect width="180" height="85" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="180" height="26" rx="8" fill="#7e22ce"/>
        <text x="90" y="18" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">User</text>
        <text x="15" y="48" fill="#c084fc" font-size="10">name: String</text>
        <line x1="10" y1="56" x2="170" y2="56" stroke="#334155" stroke-width="1"/>
        <text x="90" y="72" fill="#94a3b8" font-size="8" text-anchor="middle">Patron Domain Entity</text>
      </g>

      <!-- Item Entity (Right) -->
      <g transform="translate(580, 130)">
        <rect width="180" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="180" height="26" rx="8" fill="#047857"/>
        <text x="90" y="18" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Item</text>
        <text x="15" y="48" fill="#6ee7b7" font-size="9">Kind: String</text>
        <text x="15" y="64" fill="#6ee7b7" font-size="9">title: String</text>
        <line x1="10" y1="70" x2="170" y2="70" stroke="#334155" stroke-width="1"/>
        <text x="90" y="80" fill="#94a3b8" font-size="7" text-anchor="middle">Abstract Catalog Entry</text>
      </g>

      <!-- Copy Entity (Bottom Right) -->
      <g transform="translate(580, 240)">
        <rect width="180" height="70" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="180" height="24" rx="8" fill="#b45309"/>
        <text x="90" y="17" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Copy</text>
        <text x="15" y="44" fill="#fcd34d" font-size="9">location: String</text>
        <text x="15" y="58" fill="#fcd34d" font-size="9">status: String</text>
      </g>

      <!-- Connection: Library has User -->
      <line x1="320" y1="50" x2="150" y2="130" stroke="#94a3b8" stroke-width="2"/>
      <text x="210" y="80" fill="#38bdf8" font-size="9" font-weight="bold">has</text>
      <text x="300" y="65" fill="#f8fafc" font-size="9">1</text>
      <text x="165" y="125" fill="#f8fafc" font-size="9">*</text>

      <!-- Connection: Library contains Item -->
      <line x1="500" y1="50" x2="670" y2="130" stroke="#94a3b8" stroke-width="2"/>
      <text x="590" y="80" fill="#38bdf8" font-size="9" font-weight="bold">contains</text>
      <text x="515" y="65" fill="#f8fafc" font-size="9">1</text>
      <text x="650" y="125" fill="#f8fafc" font-size="9">1..*</text>

      <!-- Connection: User reserves Item (Top Path) -->
      <path d="M 240 150 L 580 150" stroke="#a855f7" stroke-width="2"/>
      <text x="410" y="145" fill="#c084fc" font-size="9" font-weight="bold" text-anchor="middle">reserves</text>
      <text x="250" y="145" fill="#f8fafc" font-size="8">*</text>
      <text x="565" y="145" fill="#f8fafc" font-size="8">*</text>

      <!-- Connection: User consults Item (Middle Path) -->
      <path d="M 240 180 L 580 180" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="4,2"/>
      <text x="410" y="175" fill="#93c5fd" font-size="9" font-weight="bold" text-anchor="middle">consults</text>
      <text x="250" y="175" fill="#f8fafc" font-size="8">*</text>
      <text x="565" y="175" fill="#f8fafc" font-size="8">0..1</text>

      <!-- Connection: Item has_copies Copy -->
      <line x1="670" y1="215" x2="670" y2="240" stroke="#94a3b8" stroke-width="2"/>
      <text x="695" y="230" fill="#34d399" font-size="8" font-weight="bold">has_copies</text>
      <text x="660" y="228" fill="#f8fafc" font-size="8">1</text>
      <text x="660" y="238" fill="#f8fafc" font-size="8">*</text>

      <!-- Connection: User borrows Copy (Diagonal Bottom Path) -->
      <path d="M 240 205 L 580 265" stroke="#f59e0b" stroke-width="2"/>
      <text x="410" y="245" fill="#fcd34d" font-size="9" font-weight="bold" text-anchor="middle">borrows</text>
      <text x="255" y="215" fill="#f8fafc" font-size="8">*</text>
      <text x="565" y="260" fill="#f8fafc" font-size="8">*</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2012-13):</strong> <em>"What do you mean by UML? Discuss the conceptual model of UML with the help of an appropriate example (Library System)."</em> [5 Marks - Que 1.20]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Draw AKTU Fig. 1.20.1 showing the four interconnected classes: <strong>Library, User, Item, Copy</strong>. State the multiplicities clearly: <code>Library (1) has (*) User</code>, <code>Library (1) contains (1..*) Item</code>, <code>Item (1) has_copies (*) Copy</code>, <code>User (*) reserves (*) Item</code>, <code>User (*) consults (0..1) Item</code>, <code>User (*) borrows (*) Copy</code>. Highlight that users borrow physical <em>Copies</em>, not abstract catalog <em>Items</em>.
  </div>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 21: UML Building Blocks
        # -------------------------------------------------------------
        {
            "id": "u1-sec-21",
            "number": "21",
            "part": "Part 5 — Conceptual Model of UML",
            "title": "UML Building Blocks",
            "subtitle": "Things (Structural, Behavioral, Grouping, Annotational), Relationships & Diagrams",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Grammar of UML</div>
    <h3>The Three Core UML Building Blocks</h3>
    <p>To construct any valid UML model, developers combine three fundamental building blocks: <strong>(1) Things, (2) Relationships, and (3) Diagrams</strong>.</p>
    <p>According to standard UML engineering specifications and AKTU literature, <strong>Things</strong> are the abstractions that are first-class citizens in a model; <strong>Relationships</strong> tie the things together; and <strong>Diagrams</strong> group interesting collections of things and relationships into visual projections of the system.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Natural Language Grammar (Nouns, Verbs, Sentences)</div>
  <p>Building a UML diagram is directly analogous to writing a coherent essay in English: (1) <strong>Things are Nouns</strong> (<em>Student, Computer, LoginEvent</em>); (2) <strong>Relationships are Verbs &amp; Prepositions</strong> (<em>"enrolled in" [Association], "inherits from" [Generalization], "depends on" [Dependency]</em>); (3) <strong>Diagrams are Complete Sentences and Paragraphs</strong> that convey a coherent, meaningful story about the system!</p>
</div>

<div class="subtopics-container">
  <h4>1. Things (The Four Categories of UML 'Nouns')</h4>
  <ul>
    <li><strong>Structural Things:</strong> The static, physical or conceptual nouns of a model. Includes: <code>Class</code>, <code>Interface</code>, <code>Collaboration</code>, <code>Use Case</code>, <code>Component</code>, and <code>Node</code>.</li>
    <li><strong>Behavioral Things:</strong> The dynamic verbs of a model representing behavior across time and space. Includes: <code>Interaction</code> (messages exchanged between objects) and <code>State Machine</code> (series of states an object passes through in response to events).</li>
    <li><strong>Grouping Things:</strong> Organizational boxes used to structure large models into modular chunks. The primary grouping thing is the <code>Package</code>.</li>
    <li><strong>Annotational Things:</strong> Explanatory comments, remarks, and constraints attached to elements. The primary annotational thing is the <code>Note</code>.</li>
  </ul>

  <h4>2. Relationships (The Four Connectors of UML)</h4>
  <ul>
    <li><strong>Dependency (Dashed line with open arrow):</strong> A semantic relationship where a change in one entity (independent) affects another entity (dependent).</li>
    <li><strong>Association (Solid line):</strong> A structural link relating objects of classes; may include multiplicity and role names.</li>
    <li><strong>Generalization (Solid line with hollow triangle):</strong> An inheritance relationship where specialized child classes inherit features of a general parent.</li>
    <li><strong>Realization (Dashed line with hollow triangle):</strong> A semantic contract where one entity (e.g. a class) implements the operations specified by an interface.</li>
  </ul>

  <h4>3. Diagrams (The Views of the System)</h4>
  <p>UML defines two grand families of diagrams: <strong>Structural Diagrams</strong> (Class, Object, Component, Deployment, Package) and <strong>Behavioral Diagrams</strong> (Use Case, Sequence, Collaboration, Statechart, Activity).</p>
</div>

<div class="comparison-table-wrapper">
  <h4>UML Building Blocks Summary Matrix</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Category</th>
        <th>Sub-Elements</th>
        <th>Visual Notation</th>
        <th>Semantic Purpose</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Structural Things</strong></td>
        <td>Class, Interface, Component, Node</td>
        <td>Compartmented rectangles, circles, cubes</td>
        <td>Defines static building blocks and hardware infrastructure</td>
      </tr>
      <tr>
        <td><strong>Behavioral Things</strong></td>
        <td>Interaction, State Machine</td>
        <td>Arrows with message labels, rounded state lozenges</td>
        <td>Captures dynamics, state transitions, and messaging</td>
      </tr>
      <tr>
        <td><strong>Grouping Things</strong></td>
        <td>Package</td>
        <td>Tabbed folder rectangle</td>
        <td>Organizes models into hierarchical namespaces</td>
      </tr>
      <tr>
        <td><strong>Annotational Things</strong></td>
        <td>Note</td>
        <td>Dog-eared folded corner rectangle</td>
        <td>Attaches comments, design rationales, or constraints</td>
      </tr>
      <tr>
        <td><strong>Relationships</strong></td>
        <td>Dependency, Association, Generalization, Realization</td>
        <td>Solid and dashed lines with specialized arrowheads</td>
        <td>Connects things together structurally and semantically</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Hierarchy of UML Building Blocks</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Block 1: Things (Left) -->
      <g transform="translate(30, 25)">
        <rect width="230" height="230" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="230" height="30" rx="8" fill="#0369a1"/>
        <text x="115" y="20" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">1. THINGS (NOUNS)</text>

        <rect x="15" y="42" width="200" height="38" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <text x="25" y="60" fill="#38bdf8" font-size="9" font-weight="bold">Structural Things</text>
        <text x="25" y="72" fill="#94a3b8" font-size="8">Class, Interface, Component, Node</text>

        <rect x="15" y="87" width="200" height="38" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <text x="25" y="105" fill="#38bdf8" font-size="9" font-weight="bold">Behavioral Things</text>
        <text x="25" y="117" fill="#94a3b8" font-size="8">Interaction, State Machine</text>

        <rect x="15" y="132" width="200" height="38" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <text x="25" y="150" fill="#38bdf8" font-size="9" font-weight="bold">Grouping Things</text>
        <text x="25" y="162" fill="#94a3b8" font-size="8">Package (Tabbed Folders)</text>

        <rect x="15" y="177" width="200" height="38" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <text x="25" y="195" fill="#38bdf8" font-size="9" font-weight="bold">Annotational Things</text>
        <text x="25" y="207" fill="#94a3b8" font-size="8">Note (Folded Dog-ear Box)</text>
      </g>

      <!-- Block 2: Relationships (Center) -->
      <g transform="translate(295, 25)">
        <rect width="230" height="230" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="230" height="30" rx="8" fill="#7e22ce"/>
        <text x="115" y="20" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2. RELATIONSHIPS (VERBS)</text>

        <rect x="15" y="42" width="200" height="38" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
        <text x="25" y="60" fill="#c084fc" font-size="9" font-weight="bold">Dependency (- - &gt;)</text>
        <text x="25" y="72" fill="#94a3b8" font-size="8">Client depends on supplier</text>

        <rect x="15" y="87" width="200" height="38" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
        <text x="25" y="105" fill="#c084fc" font-size="9" font-weight="bold">Association ( ── )</text>
        <text x="25" y="117" fill="#94a3b8" font-size="8">Structural connection &amp; multiplicity</text>

        <rect x="15" y="132" width="200" height="38" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
        <text x="25" y="150" fill="#c084fc" font-size="9" font-weight="bold">Generalization ( ──▷ )</text>
        <text x="25" y="162" fill="#94a3b8" font-size="8">Inheritance (is-a relationship)</text>

        <rect x="15" y="177" width="200" height="38" rx="4" fill="#0f172a" stroke="#a855f7" stroke-width="1"/>
        <text x="25" y="195" fill="#c084fc" font-size="9" font-weight="bold">Realization (- - ▷)</text>
        <text x="25" y="207" fill="#94a3b8" font-size="8">Interface implementation</text>
      </g>

      <!-- Block 3: Diagrams (Right) -->
      <g transform="translate(560, 25)">
        <rect width="230" height="230" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="230" height="30" rx="8" fill="#047857"/>
        <text x="115" y="20" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. DIAGRAMS (VIEWS)</text>

        <rect x="15" y="42" width="200" height="78" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
        <text x="25" y="60" fill="#6ee7b7" font-size="9" font-weight="bold">Structural Diagrams</text>
        <text x="25" y="74" fill="#e2e8f0" font-size="8">• Class Diagram</text>
        <text x="25" y="88" fill="#e2e8f0" font-size="8">• Object Diagram</text>
        <text x="25" y="102" fill="#e2e8f0" font-size="8">• Component &amp; Deployment</text>

        <rect x="15" y="132" width="200" height="83" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1"/>
        <text x="25" y="150" fill="#6ee7b7" font-size="9" font-weight="bold">Behavioral Diagrams</text>
        <text x="25" y="164" fill="#e2e8f0" font-size="8">• Use Case Diagram</text>
        <text x="25" y="178" fill="#e2e8f0" font-size="8">• Sequence &amp; Collaboration</text>
        <text x="25" y="192" fill="#e2e8f0" font-size="8">• State Machine &amp; Activity</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Explain the building blocks of UML. Differentiate between structural things, behavioral things, and relationships."</em> [5 Marks - Que 1.20, Que 1.22]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Structure your answer into the three distinct tiers: <strong>Things, Relationships, and Diagrams</strong>. Under Things, list all 4 sub-types: Structural (Class/Node), Behavioral (Interaction/State), Grouping (Package), and Annotational (Note). Under Relationships, list Dependency, Association, Generalization, and Realization with their graphical symbols.
  </div>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 22: UML Architecture (4+1 Views)
        # -------------------------------------------------------------
        {
            "id": "u1-sec-22",
            "number": "22",
            "part": "Part 5 — Conceptual Model of UML",
            "title": "UML Architecture (4+1 Views)",
            "subtitle": "Philippe Kruchten's 4+1 Architectural View Model & Multi-Stakeholder Perspectives",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Architectural Blueprint</div>
    <h3>What is the 4+1 View Architecture?</h3>
    <p>The <strong>4+1 Architectural View Model</strong>, designed by Philippe Kruchten and adopted by UML, is an architectural framework that describes the structure of complex software systems through <strong>five concurrent, orthogonal views</strong>.</p>
    <p>According to AKTU Quantum (Que 1.22), the UML concepts are organized around architectural views to define the various diagrams. Each view addresses specific stakeholder concerns (end users, developers, system integrators, DevOps). The <strong>Use Case View</strong> sits at the center (+1), driving and validating the four surrounding architectural views.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The 5 Blueprints of a Modern Smart Home</div>
  <p>When building a luxury smart home, a single schematic is useless: (1) The <strong>Family (End-User)</strong> looks at the <em>Floor Plan</em> showing bedroom layouts and furniture flow (<em>Use Case View</em>); (2) The <strong>Architect</strong> reviews the structural room division and wall dimensions (<em>Logical View</em>); (3) The <strong>Electrician &amp; Plumber</strong> inspects the wiring conduits and water pressure pipes running concurrently behind walls (<em>Process View</em>); (4) The <strong>General Contractor</strong> examines the physical building material delivery list: drywall boards, 2x4 timber, and roof shingles (<em>Implementation View</em>); (5) The <strong>Network Engineer</strong> maps the physical Wi-Fi routers, smart thermostats, and solar inverter hardware mounted on the concrete foundation (<em>Deployment View</em>). All 5 blueprints depict the SAME house!</p>
</div>

<div class="subtopics-container">
  <h4>The 5 Views of the 4+1 Architectural Framework</h4>

  <div class="detail-block">
    <h5>1. Use Case View (+1 Central View)</h5>
    <p><strong>Stakeholder:</strong> End Users, Customers, Product Managers, QA Testers.<br/>
    <strong>Focus:</strong> Captures system functionality, actors, business goals, and operational scenarios. It is the central "+1" view because it drives the design of all other four views and serves as the ultimate acceptance test.</p>
  </div>

  <div class="detail-block">
    <h5>2. Logical View (Design View)</h5>
    <p><strong>Stakeholder:</strong> Software Architects, System Analysts, Developers.<br/>
    <strong>Focus:</strong> Captures the logical, object-oriented structural decomposition: classes, packages, interfaces, inheritance hierarchies, and domain models. Primarily documented using <strong>Class Diagrams</strong> and <strong>Object Diagrams</strong>.</p>
  </div>

  <div class="detail-block">
    <h5>3. Process View</h5>
    <p><strong>Stakeholder:</strong> System Integrators, Performance Engineers.<br/>
    <strong>Focus:</strong> Captures non-functional runtime dynamics: concurrency, threads, processes, synchronization, memory buffering, throughput, and inter-process communication (IPC). Documented using <strong>Activity, Statechart, and Sequence Diagrams</strong>.</p>
  </div>

  <div class="detail-block">
    <h5>4. Implementation View (Development View)</h5>
    <p><strong>Stakeholder:</strong> Software Engineers, Build &amp; Release Managers.<br/>
    <strong>Focus:</strong> Captures software modular packaging, source files, libraries, DLLs, and dependency configurations within the development environment. Documented using <strong>Component Diagrams</strong> and <strong>Package Diagrams</strong>.</p>
  </div>

  <div class="detail-block">
    <h5>5. Deployment View (Physical View)</h5>
    <p><strong>Stakeholder:</strong> DevOps Engineers, Network Architects, Cloud Infrastructure Admins.<br/>
    <strong>Focus:</strong> Captures the physical hardware topology: servers, edge nodes, mobile devices, load balancers, and network links where software components execute. Documented using <strong>Deployment Diagrams</strong>.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>The 4+1 View Architecture Matrix (AKTU Que 1.22)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>View</th>
        <th>Primary Stakeholder</th>
        <th>Core Engineering Focus</th>
        <th>Associated UML Diagrams</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Use Case View (+1)</strong></td>
        <td>End User / Business Analyst</td>
        <td>System requirements, user goals &amp; scenarios</td>
        <td>Use Case Diagram, Activity Diagram</td>
      </tr>
      <tr>
        <td><strong>Logical View</strong></td>
        <td>Architect / Developer</td>
        <td>Class structures, domain entities &amp; interfaces</td>
        <td>Class Diagram, Object Diagram</td>
      </tr>
      <tr>
        <td><strong>Process View</strong></td>
        <td>System Integrator</td>
        <td>Concurrency, threads, performance &amp; IPC</td>
        <td>Sequence, Collaboration, Statechart</td>
      </tr>
      <tr>
        <td><strong>Implementation View</strong></td>
        <td>Programmer / Build Manager</td>
        <td>Source files, binaries, components &amp; modules</td>
        <td>Component Diagram, Package Diagram</td>
      </tr>
      <tr>
        <td><strong>Deployment View</strong></td>
        <td>DevOps / Network Admin</td>
        <td>Physical hardware nodes &amp; network links</td>
        <td>Deployment Diagram</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Kruchten's 4+1 Architectural View Model (AKTU Que 1.22)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="300" fill="#0f172a" rx="12"/>

      <!-- Central View: Use Case View (+1) -->
      <g transform="translate(325, 90)">
        <rect width="170" height="120" rx="10" fill="#581c87" stroke="#c084fc" stroke-width="3"/>
        <rect width="170" height="28" rx="10" fill="#7e22ce"/>
        <text x="85" y="19" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">USE CASE VIEW (+1)</text>

        <circle cx="85" cy="65" r="22" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
        <text x="85" y="70" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">SCENARIOS</text>

        <text x="85" y="102" fill="#e9d5ff" font-size="8" text-anchor="middle" font-weight="bold">DRIVES &amp; VALIDATES ALL</text>
      </g>

      <!-- View 1: Logical View (Top Left) -->
      <g transform="translate(30, 20)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="210" height="26" rx="8" fill="#0369a1"/>
        <text x="105" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">LOGICAL VIEW (DESIGN)</text>
        <text x="12" y="46" fill="#38bdf8" font-size="9" font-weight="bold">End-User Functionality</text>
        <text x="12" y="64" fill="#e2e8f0" font-size="8">• Class &amp; Object Diagrams</text>
        <text x="12" y="78" fill="#94a3b8" font-size="8">• Domain structures &amp; packages</text>
      </g>

      <!-- View 2: Process View (Top Right) -->
      <g transform="translate(580, 20)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="210" height="26" rx="8" fill="#b45309"/>
        <text x="105" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">PROCESS VIEW (RUNTIME)</text>
        <text x="12" y="46" fill="#fcd34d" font-size="9" font-weight="bold">Non-Functional Dynamics</text>
        <text x="12" y="64" fill="#e2e8f0" font-size="8">• Concurrency &amp; Threads</text>
        <text x="12" y="78" fill="#94a3b8" font-size="8">• Statecharts &amp; Sequence IPC</text>
      </g>

      <!-- View 3: Implementation View (Bottom Left) -->
      <g transform="translate(30, 185)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="210" height="26" rx="8" fill="#047857"/>
        <text x="105" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">IMPLEMENTATION VIEW</text>
        <text x="12" y="46" fill="#6ee7b7" font-size="9" font-weight="bold">Development &amp; Packaging</text>
        <text x="12" y="64" fill="#e2e8f0" font-size="8">• Component Diagrams</text>
        <text x="12" y="78" fill="#94a3b8" font-size="8">• Source files, JARs &amp; DLLs</text>
      </g>

      <!-- View 4: Deployment View (Bottom Right) -->
      <g transform="translate(580, 185)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
        <rect width="210" height="26" rx="8" fill="#9f1239"/>
        <text x="105" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">DEPLOYMENT VIEW (PHYSICAL)</text>
        <text x="12" y="46" fill="#fca5a5" font-size="9" font-weight="bold">Hardware &amp; Network Nodes</text>
        <text x="12" y="64" fill="#e2e8f0" font-size="8">• Deployment Diagrams</text>
        <text x="12" y="78" fill="#94a3b8" font-size="8">• Servers, routers &amp; topologies</text>
      </g>

      <!-- Diagonal Bi-Directional Arrows Connecting to Center -->
      <!-- Center to Logical -->
      <line x1="325" y1="120" x2="240" y2="85" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
      <!-- Center to Process -->
      <line x1="495" y1="120" x2="580" y2="85" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,2"/>
      <!-- Center to Implementation -->
      <line x1="325" y1="180" x2="240" y2="215" stroke="#10b981" stroke-width="2" stroke-dasharray="4,2"/>
      <!-- Center to Deployment -->
      <line x1="495" y1="180" x2="580" y2="215" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,2"/>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15):</strong> <em>"What are the basic architecture of UML? Explain 4+1 views with suitable diagram."</em> [5 Marks - Que 1.22]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Draw the 4+1 Views diagram with Use Case View at the center. Name all five views: <strong>Use Case View (+1), Logical View, Process View, Implementation (Development) View, and Deployment (Physical) View</strong>. For each view, cite the primary stakeholder (e.g. End User, Architect, Programmer, DevOps) and associated UML diagrams.
  </div>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 23: Link and Association
        # -------------------------------------------------------------
        {
            "id": "u1-sec-23",
            "number": "23",
            "part": "Part 6 — Important Object-Modelling Connection",
            "title": "Link and Association",
            "subtitle": "Instance vs Class Relationships, Multiplicities & The Rahul 'works_for' ABC Example",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Core Modeling Connection</div>
    <h3>What are Links and Associations?</h3>
    <p>In object-oriented modeling, <strong>Links and Associations</strong> represent the fundamental relationships that connect entities:</p>
    <ul>
      <li>A <strong>Link</strong> is a physical or conceptual connection between <strong>two or more concrete objects (instances)</strong>. A link is considered an <em>instance of an association</em>.</li>
      <li>An <strong>Association</strong> is an abstract description of a <strong>group of links</strong> that share common structure and semantics between classes.</li>
    </ul>
    <p>According to AKTU Quantum (Que 1.17), in UML notation both links and associations are represented with a line connecting boxes; however, an association connects classes (with multiplicity tags), while a link connects instantiated object instances.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Legal Contract of Marriage vs A Specific Wedding</div>
  <p>Consider the concept of <strong>Marriage</strong>: The legal statute defining the rights, tax filing status, and mutual responsibilities between any two spouses is the <strong>Association</strong> (defined at the general class level: <code>Person &mdash; MarriedTo &mdash; Person</code>). When <strong>John and Mary</strong> sign their marriage license at city hall on July 14th, that specific physical connection is a <strong>Link</strong> (an instance of the general Marriage association). You can celebrate a specific Link anniversary, but the law defines the Association blueprint!</p>
</div>

<div class="subtopics-container">
  <h4>The Person 'works_for' Company Example (AKTU Que 1.17)</h4>
  <p>Consider the relationship between working professionals and corporate enterprises:</p>
  <ul>
    <li><strong>Class Diagram (Association):</strong> Class <code>Person</code> has an association <code>WorksFor</code> with class <code>Company</code>. The association carries multiplicities (e.g., <code>Person (*) &mdash; WorksFor &mdash; (1) Company</code>: a person works for one company, while a company employs zero or more people).</li>
    <li><strong>Object Diagram (Links):</strong> At runtime, concrete instances exist: <code>rahul:Person</code> has a specific Link to <code>ABC:Company</code>, and <code>sue:Person</code> has another Link to <code>ABC:Company</code>.</li>
  </ul>

  <div class="detail-block">
    <h5>Multiplicity Annotations</h5>
    <p>Multiplicity specifies how many instances of one class may relate to a single instance of an associated class:</p>
    <ul>
      <li><code>1</code>: Exactly one.</li>
      <li><code>0..1</code>: Zero or one (optional).</li>
      <li><code>*</code> or <code>0..*</code>: Zero or more (many).</li>
      <li><code>1..*</code>: One or more (at least one).</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Link vs Association Comparison Matrix (AKTU Que 1.17)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Link</th>
        <th>Association</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Abstraction Level</strong></td>
        <td><strong>Instance Level</strong> (Concrete object-to-object)</td>
        <td><strong>Class Level</strong> (Abstract class-to-class)</td>
      </tr>
      <tr>
        <td><strong>Diagram Location</strong></td>
        <td>Appears strictly in <strong>Object Diagrams</strong></td>
        <td>Appears strictly in <strong>Class Diagrams</strong></td>
      </tr>
      <tr>
        <td><strong>Multiplicity</strong></td>
        <td>No multiplicity indicators (connects exact instances)</td>
        <td>Decorated with multiplicity numbers (<code>1</code>, <code>*</code>, <code>1..*</code>)</td>
      </tr>
      <tr>
        <td><strong>UML Box Naming</strong></td>
        <td>Connects underlined object boxes (<code>name:Class</code>)</td>
        <td>Connects standard non-underlined class boxes (<code>ClassName</code>)</td>
      </tr>
      <tr>
        <td><strong>Analogy</strong></td>
        <td>A single telephone call between Rahul and Priya</td>
        <td>The global cellular telecom network protocol</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Demonstration: Implementing Associations and Dynamic Links</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>
<span class="c-keyword">#include &lt;vector&gt;</span>
<span class="c-keyword">#include &lt;memory&gt;</span>

<span class="c-keyword">class</span> Company; <span class="c-comment">// Forward declaration</span>

<span class="c-comment">// Class Level: Person</span>
<span class="c-keyword">class</span> Person {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> name;
    <span class="c-comment">// Association realization: pointer link to Company</span>
    <span class="c-type">std::shared_ptr</span>&lt;Company&gt; employer;

<span class="c-keyword">public</span>:
    Person(<span class="c-type">std::string</span> n) : name(n), employer(<span class="c-keyword">nullptr</span>) {}

    <span class="c-type">std::string</span> getName() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> name; }

    <span class="c-comment">// Forms a concrete LINK at runtime</span>
    <span class="c-type">void</span> worksFor(<span class="c-type">std::shared_ptr</span>&lt;Company&gt; comp) {
        this-&gt;employer = comp;
    }

    <span class="c-type">void</span> displayAffiliation() <span class="c-keyword">const</span>;
};

<span class="c-comment">// Class Level: Company</span>
<span class="c-keyword">class</span> Company {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> companyName;
    <span class="c-comment">// Association realization: collection of links to Persons</span>
    <span class="c-type">std::vector</span>&lt;<span class="c-type">std::shared_ptr</span>&lt;Person&gt;&gt; employees;

<span class="c-keyword">public</span>:
    Company(<span class="c-type">std::string</span> name) : companyName(name) {}

    <span class="c-type">std::string</span> getCompanyName() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> companyName; }

    <span class="c-type">void</span> addEmployee(<span class="c-type">std::shared_ptr</span>&lt;Person&gt; p) {
        employees.push_back(p);
        p-&gt;worksFor(std::make_shared&lt;Company&gt;(*this)); <span class="c-comment">// Link established!</span>
    }
};

<span class="c-type">void</span> Person::displayAffiliation() <span class="c-keyword">const</span> {
    <span class="c-keyword">if</span> (employer) {
        std::cout &lt;&lt; <span class="c-string">"[Link]: Object "</span> &lt;&lt; name &lt;&lt; <span class="c-string">":Person is linked to "</span> 
                  &lt;&lt; employer-&gt;getCompanyName() &lt;&lt; <span class="c-string">":Company\\n"</span>;
    } <span class="c-keyword">else</span> {
        std::cout &lt;&lt; <span class="c-string">"[No Link]: Object "</span> &lt;&lt; name &lt;&lt; <span class="c-string">" has no active employment link.\\n"</span>;
    }
}

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. Instantiating concrete Object Instances</span>
    auto rahul = std::make_shared&lt;Person&gt;(<span class="c-string">"Rahul"</span>);
    auto sue = std::make_shared&lt;Person&gt;(<span class="c-string">"Sue"</span>);
    auto abcCorp = std::make_shared&lt;Company&gt;(<span class="c-string">"ABC Technology Corp"</span>);

    <span class="c-comment">// 2. Establishing concrete LINKS between objects</span>
    rahul-&gt;worksFor(abcCorp);
    sue-&gt;worksFor(abcCorp);

    rahul-&gt;displayAffiliation();
    sue-&gt;displayAffiliation();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Association (Class Diagram) vs Links (Object Diagram) (AKTU Fig. 1.17.1 &amp; 1.17.2)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 310" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="310" fill="#0f172a" rx="12"/>

      <!-- SECTION A: Class Diagram (Association) (Top Half) -->
      <g transform="translate(30, 20)">
        <rect width="760" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <rect width="760" height="24" rx="8" fill="#0369a1"/>
        <text x="380" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">CLASS DIAGRAM: ASSOCIATION (ABSTRACT LEVEL)</text>

        <!-- Person Class Box -->
        <g transform="translate(50, 35)">
          <rect width="160" height="60" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
          <rect width="160" height="20" rx="4" fill="#0284c7"/>
          <text x="80" y="14" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Person</text>
          <text x="15" y="42" fill="#e2e8f0" font-size="9">name: String</text>
        </g>

        <!-- Association Line -->
        <line x1="210" y1="65" x2="550" y2="65" stroke="#38bdf8" stroke-width="2"/>
        <!-- Association Name Label -->
        <rect x="340" y="45" width="80" height="18" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
        <text x="380" y="58" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">OwnsStock ▶</text>
        
        <!-- Multiplicity Labels -->
        <text x="225" y="58" fill="#fcd34d" font-size="10" font-weight="bold">*</text>
        <text x="535" y="58" fill="#fcd34d" font-size="10" font-weight="bold">*</text>

        <!-- Company Class Box -->
        <g transform="translate(550, 35)">
          <rect width="160" height="60" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
          <rect width="160" height="20" rx="4" fill="#0284c7"/>
          <text x="80" y="14" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Company</text>
          <text x="15" y="42" fill="#e2e8f0" font-size="9">name: String</text>
        </g>
      </g>

      <!-- SECTION B: Object Diagram (Links) (Bottom Half) -->
      <g transform="translate(30, 145)">
        <rect width="760" height="150" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
        <rect width="760" height="24" rx="8" fill="#7e22ce"/>
        <text x="380" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">OBJECT DIAGRAM: CONCRETE LINKS (INSTANCE LEVEL)</text>

        <!-- Object Instance 1 (Rahul) -->
        <g transform="translate(50, 35)">
          <rect width="160" height="42" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
          <text x="80" y="20" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" text-decoration="underline">rahul : Person</text>
          <text x="80" y="34" fill="#94a3b8" font-size="8" text-anchor="middle">name = "Rahul"</text>
        </g>

        <!-- Object Instance 2 (Sue) -->
        <g transform="translate(50, 90)">
          <rect width="160" height="42" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
          <text x="80" y="20" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" text-decoration="underline">sue : Person</text>
          <text x="80" y="34" fill="#94a3b8" font-size="8" text-anchor="middle">name = "Sue"</text>
        </g>

        <!-- Concrete Link Lines -->
        <line x1="210" y1="56" x2="550" y2="56" stroke="#c084fc" stroke-width="2"/>
        <line x1="210" y1="111" x2="550" y2="111" stroke="#c084fc" stroke-width="2"/>

        <text x="380" y="50" fill="#c084fc" font-size="8" text-anchor="middle">link instance 1</text>
        <text x="380" y="105" fill="#c084fc" font-size="8" text-anchor="middle">link instance 2</text>

        <!-- Object Instance 3 (ABC Tech) -->
        <g transform="translate(550, 35)">
          <rect width="160" height="42" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
          <text x="80" y="20" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" text-decoration="underline">abcTech : Company</text>
          <text x="80" y="34" fill="#94a3b8" font-size="8" text-anchor="middle">name = "ABC Corp"</text>
        </g>

        <!-- Object Instance 4 (XYZ Global) -->
        <g transform="translate(550, 90)">
          <rect width="160" height="42" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1.5"/>
          <text x="80" y="20" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" text-decoration="underline">xyzGlobal : Company</text>
          <text x="80" y="34" fill="#94a3b8" font-size="8" text-anchor="middle">name = "XYZ Ltd"</text>
        </g>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13):</strong> <em>"Define link and association. Discuss the role of link and association in object modeling with suitable example."</em> [5 Marks - Que 1.17]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define Link as a relationship between objects (instance of an association). Define Association as a group of links relating objects from the same classes. Recreate AKTU Fig. 1.17.1 (Object Diagram with links) and Fig. 1.17.2 (Class Diagram with association). State that both use lines, but class associations include multiplicities while object links connect specific underlined instances.
  </div>
</div>
"""
        }
    ]
