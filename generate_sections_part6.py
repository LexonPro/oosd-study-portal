# generate_sections_part6.py: Part 6 - Architectural Modeling (Sections 32 to 36)

def get_part6_sections():
    return [
        {
            "id": "sec-32",
            "number": "32",
            "part": "Part 6 — Architectural Modeling",
            "title": "Architectural Modeling",
            "subtitle": "System Blueprint, Physical Architecture, Structural + Behavioral Integration",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">System Blueprint</div>
    <h3>Meaning of Architectural Modeling</h3>
    <p><strong>Architectural Modeling</strong> represents the <strong>overall high-level framework and physical blueprint of a software system</strong>. It integrates structural building blocks with dynamic runtime processes and maps them directly onto physical execution environments, hardware topologies, and network protocols.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Core Perspectives of Architectural Modeling</h4>

  <div class="detail-block">
    <h5>1. The System Blueprint</h5>
    <p>Architecture answers high-level non-functional questions that logical class diagrams cannot address:</p>
    <ul>
      <li><em>How is the software packaged into deliverable executables, libraries, and microservices?</em></li>
      <li><em>Where do these binaries physically reside at runtime across client machines, application clusters, and cloud databases?</em></li>
      <li><em>What communication protocols (HTTPS, gRPC, TCP/IP, JDBC) bridge the nodes?</em></li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. The Two Core Architectural Diagrams</h5>
    <div class="two-col-cards">
      <div class="feature-card">
        <div class="col-head blue-head">1. Component Diagram (Software View)</div>
        <p>Models the <strong>static implementation view</strong>. Shows software artifacts, executables, source files, shared libraries (.dll, .so, .jar), and the interfaces through which they wire together.</p>
      </div>

      <div class="feature-card">
        <div class="col-head green-head">2. Deployment Diagram (Hardware View)</div>
        <p>Models the <strong>runtime physical architecture</strong>. Shows physical processing nodes (servers, edge devices, virtual machines) and the network connections linking them, with software components deployed inside.</p>
      </div>
    </div>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Bridging Software Components to Physical Hardware Nodes</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="archArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#8b5cf6"/>
        </marker>
      </defs>

      <!-- Left: Software Component (Logical/Binary) -->
      <g transform="translate(60, 40)">
        <rect width="240" height="130" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect x="-12" y="25" width="24" height="18" rx="2" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
        <rect x="-12" y="65" width="24" height="18" rx="2" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
        <text x="120" y="45" text-anchor="middle" font-size="11" fill="#2563eb">&lt;&lt;component&gt;&gt;</text>
        <text x="120" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--text-primary)">BillingEngine.jar</text>
        <text x="120" y="95" text-anchor="middle" font-size="10" fill="var(--text-muted)">Packaged Software Module</text>
      </g>

      <!-- Mapping Arrow: Deployed Onto -->
      <line x1="310" y1="105" x2="430" y2="105" stroke="#8b5cf6" stroke-width="2.5" stroke-dasharray="5,4" marker-end="url(#archArr)"/>
      <text x="370" y="95" text-anchor="middle" font-size="10" font-weight="bold" fill="#7c3aed">&lt;&lt;deployed on&gt;&gt;</text>

      <!-- Right: Hardware 3D Node (Physical) -->
      <g transform="translate(440, 30)">
        <!-- 3D Node Box -->
        <polygon points="0,20 20,0 260,0 240,20" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="1.5"/>
        <polygon points="240,20 260,0 260,130 240,150" class="uml-cube-side" fill="#182335" stroke="#475569" stroke-width="1.5"/>
        <rect x="0" y="20" width="240" height="130" fill="var(--card-bg)" stroke="#475569" stroke-width="2"/>
        <text x="120" y="45" text-anchor="middle" font-size="11" fill="#059669">&lt;&lt;device&gt;&gt;</text>
        <text x="120" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--text-primary)">AppServerNode</text>
        <rect x="25" y="80" width="190" height="50" rx="4" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6"/>
        <text x="120" y="110" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Artifact: BillingEngine.jar</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2014-15):</strong> <em>"What do you understand by architectural modeling? Name the main diagrams used in architectural modeling."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Clearly emphasize that architectural modeling integrates structural and behavioral models to produce the physical blueprint of the system via <strong>Component Diagrams</strong> and <strong>Deployment Diagrams</strong>.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Architectural Modeling = Overall system framework and physical blueprint.</li>
    <li>Two primary diagrams: Component Diagram (Software) + Deployment Diagram (Hardware).</li>
    <li>Bridges high-level logical design to physical execution environments.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-33",
            "number": "33",
            "part": "Part 6 — Architectural Modeling",
            "title": "Component",
            "subtitle": "Modular Units, Replaceability, Implementation Packaging & System Evolution",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Modular Unit</div>
    <h3>Meaning of Component</h3>
    <p>A <strong>Component</strong> is a modular, deployable, and replaceable part of a software system that encapsulates implementation details and exposes a set of external interfaces. It is a physical packaging of logical elements.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Characteristics and Packaging</h4>

  <div class="detail-block">
    <h5>1. The 3 Core Tenets of a Component</h5>
    <ul>
      <li><strong>Modular & Encapsulated:</strong> Hides internal source code behind strict interface boundaries.</li>
      <li><strong>Deployable:</strong> Exists as an autonomous physical packaging (e.g. <code>.jar</code>, <code>.dll</code>, <code>.exe</code>, Docker container, or shared library).</li>
      <li><strong>Replaceable (Plug-and-Play):</strong> Can be hot-swapped or upgraded with an alternative component provided both honor the same interface contracts.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Reusability and System Evolution</h5>
    <p>Components form the foundation of <strong>Component-Based Software Engineering (CBSE)</strong>. Systems evolve by upgrading individual components without re-architecting the entire enterprise application.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Standard UML Component Notations</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
      <!-- UML 1.x Classic Tabbed Notation -->
      <g transform="translate(80, 25)">
        <rect width="240" height="120" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect x="-14" y="25" width="28" height="20" rx="2" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
        <rect x="-14" y="65" width="28" height="20" rx="2" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
        <text x="120" y="55" text-anchor="middle" font-size="11" fill="#2563eb">&lt;&lt;component&gt;&gt;</text>
        <text x="120" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--text-primary)">AuthService.dll</text>
        <text x="120" y="110" text-anchor="middle" font-size="10" fill="var(--text-muted)">Classic UML Component Icon</text>
      </g>

      <!-- UML 2.x Modern Notational Variant -->
      <g transform="translate(420, 25)">
        <rect width="240" height="120" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <!-- Mini component icon in top right -->
        <rect x="200" y="12" width="24" height="16" rx="2" fill="none" stroke="#10b981" stroke-width="1.5"/>
        <rect x="196" y="15" width="8" height="4" fill="var(--card-bg)" stroke="#10b981"/>
        <rect x="196" y="21" width="8" height="4" fill="var(--card-bg)" stroke="#10b981"/>
        <text x="120" y="55" text-anchor="middle" font-size="11" fill="#059669">&lt;&lt;component&gt;&gt;</text>
        <text x="120" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--text-primary)">PaymentProcessor</text>
        <text x="120" y="110" text-anchor="middle" font-size="10" fill="var(--text-muted)">Modern UML 2.x Box with Tag</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Define a component. What do you mean by a replaceable part of a system?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Explain that a component is a physical, deployable, and replaceable unit. It can be replaced at runtime or compile-time without affecting clients, as long as interface contracts are maintained.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Component = Modular, deployable, replaceable part of a system.</li>
    <li>Draw as a rectangle with two small protruding tabs on the left border.</li>
    <li>Communicates strictly through interfaces (loose coupling).</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-34",
            "number": "34",
            "part": "Part 6 — Architectural Modeling",
            "title": "Interface",
            "subtitle": "Operation Collections, Provided vs Required, Ball-and-Socket & Realization",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Contract Specification</div>
    <h3>Meaning of Interface</h3>
    <p>An <strong>Interface</strong> is a named collection of operations that specifies a contract for the services offered by a class or component without dictating its internal implementation. It enforces the <em>Separation of Interface and Implementation</em>.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The Two Notational Conventions in UML</h4>

  <div class="detail-block">
    <h5>1. Provided vs. Required Interfaces (Ball-and-Socket / Lollipop Notation)</h5>
    <ul>
      <li><strong>Provided Interface (Lollipop / Ball <code>—○</code>):</strong> A service that the component implements and offers to other components.</li>
      <li><strong>Required Interface (Socket / Cup <code>—)</code>):</strong> A service that the component expects or requires from external entities to function.</li>
      <li><strong>Assembly Connector:</strong> When a provided lollipop fits into a required socket, forming a complete plug-and-play connection!</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Stereotyped Classifier Notation</h5>
    <p>A standard rectangle adorned with <code>&lt;&lt;interface&gt;&gt;</code> listing the abstract operations. Classes and components realize this interface using a <strong>dashed line with a hollow triangle (<code>- - -▷</code>)</strong>.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Ball-and-Socket Assembly Connector & Realization</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Component A (Provider) -->
      <g transform="translate(60, 40)">
        <rect width="180" height="90" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="90" y="45" text-anchor="middle" font-size="11" fill="#2563eb">&lt;&lt;component&gt;&gt;</text>
        <text x="90" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">DatabaseService</text>
        <!-- Lollipop (Ball) extending right -->
        <line x1="180" y1="50" x2="260" y2="50" stroke="#3b82f6" stroke-width="2"/>
        <circle cx="270" cy="50" r="10" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
      </g>
      <text x="325" y="35" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Provided: IDatabase</text>

      <!-- Assembly Joint in Center -->
      <!-- Component B (Consumer) with Socket -->
      <g transform="translate(420, 40)">
        <!-- Socket (Cup) extending left to meet Ball -->
        <path d="M -70 38 A 14 14 0 0 0 -70 62" fill="none" stroke="#10b981" stroke-width="2.5"/>
        <line x1="-70" y1="50" x2="0" y2="50" stroke="#10b981" stroke-width="2"/>
        
        <rect width="180" height="90" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="90" y="45" text-anchor="middle" font-size="11" fill="#059669">&lt;&lt;component&gt;&gt;</text>
        <text x="90" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">BillingClient</text>
      </g>
      <text x="385" y="75" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">Required: IDatabase</text>

      <text x="370" y="165" text-anchor="middle" font-size="11" fill="var(--text-muted)">Ball (Provided) snaps into Socket (Required) forming an Assembly Connector.</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"What is an interface? Explain lollipop (ball-and-socket) notation and interface realization."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Must-Draw:</strong> Draw both the lollipop (provided) circle and the socket (required) semicircle. Show how they connect together to form an assembly connector.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Interface = Pure contract of operation signatures without implementation.</li>
    <li>Provided interface = Lollipop ball <code>—○</code>.</li>
    <li>Required interface = Socket semicircle <code>—)</code>.</li>
    <li>Interface realization = Dashed arrow with hollow triangle <code>- - -▷</code>.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-35",
            "number": "35",
            "part": "Part 6 — Architectural Modeling",
            "title": "Component Diagram",
            "subtitle": "Static Implementation View, Software Artifacts, Executables & Component Dependencies",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Implementation Architecture</div>
    <h3>Meaning and Purpose of Component Diagrams</h3>
    <p>A <strong>Component Diagram</strong> illustrates the <strong>static implementation view</strong> of a system. It visualizes how source code files, binaries, libraries, executables, scripts, and database tables are organized into deployable software components and how they depend on each other via interfaces.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Architectural Components and Adaptability</h4>

  <div class="detail-block">
    <h5>1. Core Elements of Component Diagrams</h5>
    <ul>
      <li><strong>Components:</strong> Modular code/executable blocks (e.g. <code>UI.war</code>, <code>OrderService.jar</code>, <code>InventoryDB</code>).</li>
      <li><strong>Provided & Required Interfaces:</strong> The contracts governing communication.</li>
      <li><strong>Dependencies (<code>- - - -></code>):</strong> Indicates that one component relies on another component or interface.</li>
      <li><strong>Artifacts:</strong> Physical manifest files (e.g. <code>config.xml</code>, <code>app.exe</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Adaptable Systems & Component-Based Software Engineering (CBSE)</h5>
    <p>Component diagrams enable architects to model adaptable, loosely-coupled systems. When business rules change, only the affected component is updated and swapped without recompiling the entire system.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Enterprise E-Commerce Component Diagram</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="compDep" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Component 1: Web Frontend -->
      <g transform="translate(40, 75)">
        <rect width="180" height="90" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect x="-10" y="20" width="20" height="15" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <rect x="-10" y="55" width="20" height="15" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="90" y="42" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;component&gt;&gt;</text>
        <text x="90" y="62" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">WebClient.war</text>
      </g>

      <!-- Dependency 1 -->
      <line x1="220" y1="120" x2="295" y2="120" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#compDep)"/>
      <text x="255" y="110" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;use&gt;&gt;</text>

      <!-- Component 2: Business Order Service -->
      <g transform="translate(300, 75)">
        <rect width="180" height="90" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <rect x="-10" y="20" width="20" height="15" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <rect x="-10" y="55" width="20" height="15" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <text x="90" y="42" text-anchor="middle" font-size="10" fill="#059669">&lt;&lt;component&gt;&gt;</text>
        <text x="90" y="62" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">OrderService.jar</text>
      </g>

      <!-- Dependency 2 -->
      <line x1="480" y1="120" x2="555" y2="120" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#compDep)"/>
      <text x="515" y="110" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;use&gt;&gt;</text>

      <!-- Component 3: Database Component -->
      <g transform="translate(560, 75)">
        <rect width="160" height="90" rx="4" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="2"/>
        <rect x="-10" y="20" width="20" height="15" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="1.5"/>
        <rect x="-10" y="55" width="20" height="15" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="1.5"/>
        <text x="80" y="42" text-anchor="middle" font-size="10" fill="#7c3aed">&lt;&lt;database&gt;&gt;</text>
        <text x="80" y="62" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">PostgresDB</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2015-16):</strong> <em>"Describe in brief component diagram. Draw a component diagram for an online shopping system."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Draw at least 3 components (Frontend, Service, Database). Use the standard tabbed box symbol and connect them using dashed dependency arrows.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Component Diagram = Static implementation view of software binaries and files.</li>
    <li>Shows components, interfaces, dependencies, and database schemas.</li>
    <li>Supports plug-and-play architecture and CBSE.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-36",
            "number": "36",
            "part": "Part 6 — Architectural Modeling",
            "title": "Deployment Diagram",
            "subtitle": "Runtime Hardware Nodes, Communication Paths, Network Protocols & Nodes vs Components",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Physical Architecture</div>
    <h3>Meaning and Purpose of Deployment Diagrams</h3>
    <p>A <strong>Deployment Diagram</strong> portrays the <strong>runtime physical architecture of a system</strong>. It shows the hardware configuration (nodes, servers, sensors, workstations), the network communication paths connecting them, and the concrete software artifacts deployed on those physical execution nodes.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Terminology & Node vs. Component Distinction</h4>

  <div class="detail-block">
    <h5>1. Key Architectural Elements</h5>
    <ul>
      <li><strong>Node:</strong> A physical computational resource that possesses memory and processing power. Represented as a <strong>3D box (cube)</strong>.</li>
      <li><strong>Device Node vs. Execution Environment Node:</strong> A physical hardware device (e.g., <code>&lt;&lt;device&gt;&gt; ApplicationServer</code>) vs an execution platform (e.g., <code>&lt;&lt;execution environment&gt;&gt; JVM</code> or <code>DockerEngine</code>).</li>
      <li><strong>Communication Path:</strong> A solid line connecting nodes, stereotyped with network protocols (e.g. <code>&lt;&lt;TCP/IP&gt;&gt;</code>, <code>&lt;&lt;HTTPS&gt;&gt;</code>, <code>&lt;&lt;JDBC&gt;&gt;</code>).</li>
      <li><strong>Deployed Artifact:</strong> The concrete software binary (e.g., <code>app.war</code>, <code>service.exe</code>) drawn inside the node cube.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Crucial Exam Comparison: Node vs. Component</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Criterion</th>
          <th>Node (Deployment Diagram)</th>
          <th>Component (Component Diagram)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Nature</strong></td>
          <td><strong>Hardware element</strong> or physical execution host</td>
          <td><strong>Software element</strong> (executable, binary, code artifact)</td>
        </tr>
        <tr>
          <td><strong>UML Notation</strong></td>
          <td>3-Dimensional Box / Cube</td>
          <td>Rectangle with two small protruding tabs on the left border</td>
        </tr>
        <tr>
          <td><strong>Physical Existence</strong></td>
          <td>Possesses memory, CPU, and physical spatial location</td>
          <td>Resides <em>inside</em> a node; executes on the node's processor</td>
        </tr>
        <tr>
          <td><strong>Examples</strong></td>
          <td>Database Server, Smartphone, POS Terminal, Router</td>
          <td><code>paymentService.jar</code>, <code>auth.dll</code>, <code>schema.sql</code></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: 3-Tier Enterprise Cloud Deployment Diagram</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 270" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
      <!-- Node 1: Client Machine -->
      <g transform="translate(30, 70)">
        <polygon points="0,15 15,0 170,0 155,15" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="1.5"/>
        <polygon points="155,15 170,0 170,105 155,120" class="uml-cube-side" fill="#182335" stroke="#475569" stroke-width="1.5"/>
        <rect x="0" y="15" width="155" height="105" fill="var(--card-bg)" stroke="#475569" stroke-width="2"/>
        <text x="77" y="38" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;device&gt;&gt;</text>
        <text x="77" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Client Browser</text>
        <rect x="15" y="68" width="125" height="40" rx="3" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6"/>
        <text x="77" y="92" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;artifact&gt;&gt; SPA.js</text>
      </g>

      <!-- Communication Path 1 -->
      <line x1="185" y1="130" x2="285" y2="130" stroke="#64748b" stroke-width="2"/>
      <text x="235" y="120" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;HTTPS&gt;&gt;</text>

      <!-- Node 2: App Server -->
      <g transform="translate(285, 50)">
        <polygon points="0,15 15,0 185,0 170,15" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="1.5"/>
        <polygon points="170,15 185,0 185,125 170,140" class="uml-cube-side" fill="#182335" stroke="#475569" stroke-width="1.5"/>
        <rect x="0" y="15" width="170" height="125" fill="var(--card-bg)" stroke="#475569" stroke-width="2"/>
        <text x="85" y="38" text-anchor="middle" font-size="10" fill="#059669">&lt;&lt;device&gt;&gt;</text>
        <text x="85" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">App Server</text>
        <rect x="15" y="68" width="140" height="55" rx="3" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
        <text x="85" y="88" text-anchor="middle" font-size="9" font-weight="bold" fill="#059669">&lt;&lt;artifact&gt;&gt; ApiServer.jar</text>
        <text x="85" y="105" text-anchor="middle" font-size="8" fill="var(--text-muted)">Running in JVM</text>
      </g>

      <!-- Communication Path 2 -->
      <line x1="455" y1="130" x2="550" y2="130" stroke="#64748b" stroke-width="2"/>
      <text x="502" y="120" text-anchor="middle" font-size="9" font-weight="bold" fill="#7c3aed">&lt;&lt;JDBC/SSL&gt;&gt;</text>

      <!-- Node 3: DB Server -->
      <g transform="translate(550, 70)">
        <polygon points="0,15 15,0 170,0 155,15" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="1.5"/>
        <polygon points="155,15 170,0 170,105 155,120" class="uml-cube-side" fill="#182335" stroke="#475569" stroke-width="1.5"/>
        <rect x="0" y="15" width="155" height="105" fill="var(--card-bg)" stroke="#475569" stroke-width="2"/>
        <text x="77" y="38" text-anchor="middle" font-size="10" fill="#7c3aed">&lt;&lt;device&gt;&gt;</text>
        <text x="77" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Database Cluster</text>
        <rect x="15" y="68" width="125" height="40" rx="3" fill="rgba(139, 92, 246, 0.2)" stroke="#8b5cf6"/>
        <text x="77" y="92" text-anchor="middle" font-size="9" font-weight="bold" fill="#7c3aed">&lt;&lt;artifact&gt;&gt; data.db</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15):</strong> <em>"Explain deployment diagrams with a suitable diagram. What is the difference between components and nodes?"</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Key Marking Formula:</strong> Draw the 3D cube nodes with communication path protocols (e.g. <code>&lt;&lt;TCP/IP&gt;&gt;</code>, <code>&lt;&lt;HTTPS&gt;&gt;</code>). Provide the Node vs Component comparison table given above for full marks.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Deployment Diagram = Runtime physical architecture and hardware topology.</li>
    <li>Node = 3D cube representing physical hardware or execution container.</li>
    <li>Connections = Lines between nodes labeled with network protocols.</li>
    <li>Artifacts = Software packages deployed inside the node cubes.</li>
  </ul>
</div>
"""
        }
    ]
