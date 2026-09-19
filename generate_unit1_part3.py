# generate_unit1_part3.py: Part 3 - Modelling (Sections 09 to 16)

def get_unit1_part3_sections():
    return [
        # -------------------------------------------------------------
        # Section 09: Meaning of Modelling
        # -------------------------------------------------------------
        {
            "id": "u1-sec-9",
            "number": "09",
            "part": "Part 3 — Modelling",
            "title": "Meaning of Modelling",
            "subtitle": "Abstraction of Reality, Capturing Essential Features & Domain Concepts",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational Engineering Concept</div>
    <h3>What is Modelling?</h3>
    <p>A <strong>Model</strong> is an <strong>abstraction of a physical or software system</strong> created for the purpose of understanding, communicating, and evaluating the system before physically constructing it. Modelling involves extracting the essential characteristics of a domain while deliberately filtering out irrelevant, non-essential, or incidental details.</p>
    <p>According to AKTU Quantum (Que 1.12), to build complex hardware and software systems, engineers must: (1) Abstract different views of the system, (2) Build models using precise visual notations, (3) Verify that the model satisfies functional requirements, and (4) Progressively add implementation details to transform the model into executable code.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Architectural Scale Blueprint vs The Real Skyscraper</div>
  <p>Before constructing a 100-story skyscraper, civil engineers do not start pouring thousands of tons of concrete on day one. They construct architectural scale blueprints, 3D CAD stress simulations, and wind-tunnel models. The blueprint models load-bearing pillars, emergency stairwells, and electrical conduits. It intentionally ignores the color of the lobby curtains or the brand of office chairs. If an earthquake flaw exists in the model, fixing it takes an eraser stroke; in concrete, it costs hundreds of millions of dollars and human lives!</p>
</div>

<div class="subtopics-container">
  <h4>Core Characteristics of Effective Software Models</h4>

  <div class="detail-block">
    <h5>1. Abstraction (Selective Omission)</h5>
    <p>Abstraction is the deliberate suppression of irrelevant technical noise. In an e-commerce domain model, representing an <code>Order</code> requires <code>orderId</code>, <code>orderDate</code>, and <code>totalAmount</code>. The physical CPU register holding the order or the baud rate of the network card is abstracted away.</p>
  </div>

  <div class="detail-block">
    <h5>2. Domain Model of E-Commerce System</h5>
    <p>A domain conceptual model organizes business concepts into interacting entities:</p>
    <ul>
      <li><strong>Customer:</strong> Holds identity, address, and purchase history.</li>
      <li><strong>Product:</strong> Details inventory SKU, unit price, and specifications.</li>
      <li><strong>Order:</strong> Aggregates line items and tracks fulfillment state (Pending, Shipped).</li>
      <li><strong>Payment:</strong> Records transaction token, gateway authorization, and payment method.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Executable Specification</h5>
    <p>Modern visual modeling languages like UML are semantically rigorous enough to support forward engineering (generating starter code from diagrams) and reverse engineering (reconstructing models from existing source code).</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Physical Reality vs Conceptual Model</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Aspect</th>
        <th>Physical / Real System</th>
        <th>Abstract Software Model</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Cost of Mutation</strong></td>
        <td>Extremely expensive (refactoring deployed databases, servers)</td>
        <td>Virtually zero (updating diagram or blueprint before coding)</td>
      </tr>
      <tr>
        <td><strong>Detail Level</strong></td>
        <td>100% full implementation detail, hardware quirks, and noise</td>
        <td>Targeted, filtered view focusing strictly on current concerns</td>
      </tr>
      <tr>
        <td><strong>Audience</strong></td>
        <td>Compilers, runtimes, and end-users</td>
        <td>System Architects, Business Stakeholders, and Developers</td>
      </tr>
      <tr>
        <td><strong>Testability</strong></td>
        <td>Testing requires full hardware setup and real runtime conditions</td>
        <td>Simulatable logically via formal walk-throughs and model checkers</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Domain Model: E-Commerce System (Customer &rarr; Order &rarr; Product)</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>
<span class="c-keyword">#include &lt;vector&gt;</span>
<span class="c-keyword">#include &lt;memory&gt;</span>

<span class="c-comment">// Abstracting Product Entity</span>
<span class="c-keyword">class</span> Product {
<span class="c-keyword">public</span>:
    <span class="c-type">int</span> id;
    <span class="c-type">std::string</span> name;
    <span class="c-type">double</span> price;

    Product(<span class="c-type">int</span> id, <span class="c-type">std::string</span> name, <span class="c-type">double</span> price) : id(id), name(name), price(price) {}
};

<span class="c-comment">// Abstracting Order Line Item</span>
<span class="c-keyword">struct</span> OrderItem {
    <span class="c-type">std::shared_ptr</span>&lt;Product&gt; product;
    <span class="c-type">int</span> quantity;

    <span class="c-type">double</span> getSubtotal() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> product-&gt;price * quantity;
    }
};

<span class="c-comment">// Abstracting Order Entity</span>
<span class="c-keyword">class</span> Order {
<span class="c-keyword">public</span>:
    <span class="c-type">int</span> orderId;
    <span class="c-type">std::string</span> orderDate;
    <span class="c-type">std::vector</span>&lt;OrderItem&gt; items;

    Order(<span class="c-type">int</span> id, <span class="c-type">std::string</span> date) : orderId(id), orderDate(date) {}

    <span class="c-type">void</span> addItem(<span class="c-type">std::shared_ptr</span>&lt;Product&gt; p, <span class="c-type">int</span> qty) {
        items.push_back({p, qty});
    }

    <span class="c-type">double</span> calculateTotal() <span class="c-keyword">const</span> {
        <span class="c-type">double</span> total = <span class="c-number">0.0</span>;
        <span class="c-keyword">for</span> (<span class="c-keyword">const</span> auto&amp; item : items) {
            total += item.getSubtotal();
        }
        <span class="c-keyword">return</span> total;
    }
};

<span class="c-comment">// Abstracting Customer Entity</span>
<span class="c-keyword">class</span> Customer {
<span class="c-keyword">public</span>:
    <span class="c-type">int</span> customerId;
    <span class="c-type">std::string</span> name;
    <span class="c-type">std::vector</span>&lt;Order&gt; orderHistory;

    Customer(<span class="c-type">int</span> id, <span class="c-type">std::string</span> n) : customerId(id), name(n) {}

    <span class="c-type">void</span> placeOrder(<span class="c-keyword">const</span> Order&amp; order) {
        orderHistory.push_back(order);
        std::cout &lt;&lt; <span class="c-string">"[Model Action]: Customer "</span> &lt;&lt; name &lt;&lt; <span class="c-string">" placed Order #"</span> 
                  &lt;&lt; order.orderId &lt;&lt; <span class="c-string">" Totaling: $"</span> &lt;&lt; order.calculateTotal() &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    auto laptop = std::make_shared&lt;Product&gt;(<span class="c-number">101</span>, <span class="c-string">"ThinkPad X1"</span>, <span class="c-number">1200.0</span>);
    auto mouse = std::make_shared&lt;Product&gt;(<span class="c-number">102</span>, <span class="c-string">"Wireless Mouse"</span>, <span class="c-number">25.0</span>);

    <span class="c-type">Customer</span> cust(<span class="c-number">1</span>, <span class="c-string">"Ananya Roy"</span>);

    <span class="c-type">Order</span> order1(<span class="c-number">5001</span>, <span class="c-string">"2026-09-19"</span>);
    order1.addItem(laptop, <span class="c-number">1</span>);
    order1.addItem(mouse, <span class="c-number">2</span>);

    cust.placeOrder(order1);
    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Modeling Abstraction Filter (Real World to Conceptual Model)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Real World Problem Domain (Left) -->
      <g transform="translate(30, 30)">
        <rect width="210" height="220" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
        <rect width="210" height="32" rx="8" fill="#9f1239"/>
        <text x="105" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">REAL-WORLD REALITY</text>

        <text x="15" y="58" fill="#fca5a5" font-size="10" font-weight="bold">Chaotic &amp; Infinite Details:</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Physical warehouse shelves</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Cash register thermal paper</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• Courier delivery tire pressure</text>
        <text x="15" y="138" fill="#e2e8f0" font-size="9">• Customer mood / biometric pulse</text>
        <text x="15" y="158" fill="#e2e8f0" font-size="9">• CPU cache line invalidations</text>
        
        <rect x="15" y="175" width="180" height="30" rx="4" fill="#881337" opacity="0.6"/>
        <text x="105" y="195" fill="#fca5a5" font-size="9" text-anchor="middle">Too complex to build directly!</text>
      </g>

      <!-- Funnel / Abstraction Filter (Center) -->
      <g transform="translate(265, 80)">
        <polygon points="0,20 80,55 80,75 0,110" fill="#334155" stroke="#60a5fa" stroke-width="2"/>
        <text x="35" y="70" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">ABSTRACTION</text>
        <text x="35" y="82" fill="#94a3b8" font-size="8" text-anchor="middle">FILTER</text>
      </g>

      <!-- Abstract Software Model (Right) -->
      <g transform="translate(370, 30)">
        <rect width="420" height="220" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="420" height="32" rx="8" fill="#065f46"/>
        <text x="210" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CONCEPTUAL DOMAIN MODEL (ESSENTIAL ABSTRACTION)</text>

        <!-- Customer Box -->
        <g transform="translate(20, 50)">
          <rect width="170" height="70" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
          <rect width="170" height="20" rx="6" fill="#0284c7"/>
          <text x="85" y="14" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Customer</text>
          <text x="10" y="36" fill="#94a3b8" font-size="8">+ id: int, name: String</text>
          <text x="10" y="52" fill="#38bdf8" font-size="8">+ placeOrder(order)</text>
        </g>

        <!-- Order Box -->
        <g transform="translate(230, 50)">
          <rect width="170" height="70" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
          <rect width="170" height="20" rx="6" fill="#7e22ce"/>
          <text x="85" y="14" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Order</text>
          <text x="10" y="36" fill="#94a3b8" font-size="8">+ orderId: int, date: Date</text>
          <text x="10" y="52" fill="#c084fc" font-size="8">+ calculateTotal(): double</text>
        </g>

        <!-- Association Line Customer -> Order -->
        <line x1="190" y1="85" x2="230" y2="85" stroke="#94a3b8" stroke-width="2"/>
        <text x="200" y="80" fill="#f8fafc" font-size="8">1</text>
        <text x="220" y="80" fill="#f8fafc" font-size="8">*</text>

        <!-- Product Box -->
        <g transform="translate(230, 135)">
          <rect width="170" height="70" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
          <rect width="170" height="20" rx="6" fill="#047857"/>
          <text x="85" y="14" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Product</text>
          <text x="10" y="36" fill="#94a3b8" font-size="8">+ sku: int, price: double</text>
          <text x="10" y="52" fill="#34d399" font-size="8">+ getInventory(): int</text>
        </g>

        <!-- Association Line Order -> Product -->
        <line x1="315" y1="120" x2="315" y2="135" stroke="#94a3b8" stroke-width="2"/>
        <text x="320" y="130" fill="#f8fafc" font-size="8">*</text>

        <!-- Model Summary Note -->
        <g transform="translate(20, 135)">
          <rect width="170" height="70" rx="6" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2"/>
          <text x="85" y="24" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">Essential Business Logic</text>
          <text x="85" y="42" fill="#e2e8f0" font-size="8" text-anchor="middle">Clean, communicable,</text>
          <text x="85" y="56" fill="#e2e8f0" font-size="8" text-anchor="middle">testable &amp; traceable</text>
        </g>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12):</strong> <em>"What do you mean by modeling? Discuss several purposes served by models with suitable examples."</em> [5 Marks - Que 1.12]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define a model as an abstraction of a system created to understand it prior to construction. Emphasize that models deliberately eliminate non-essential details. State the 4 steps engineers perform: abstract views, build precise notations, verify requirements, and transform into code.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Model:</strong> An abstraction of reality created to understand and design a system before building it.</li>
    <li><strong>Abstraction:</strong> Filtering out irrelevant noise to highlight core structural and behavioral invariants.</li>
    <li><strong>Key Benefit:</strong> Catching design flaws on paper costs pennies; refactoring production code costs millions.</li>
    <li><strong>Domain Example:</strong> E-commerce modeled cleanly as Customer, Order, Product, and Payment.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 10: Importance of Modelling
        # -------------------------------------------------------------
        {
            "id": "u1-sec-10",
            "number": "10",
            "part": "Part 3 — Modelling",
            "title": "Importance of Modelling",
            "subtitle": "5 Strategic Purposes: Testing, Customer Communication, Visualization & Complexity Reduction",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Strategic Value</div>
    <h3>Why is Modelling Essential?</h3>
    <p>Software development without modelling is equivalent to erecting a suspension bridge without structural engineering schematics. As systems grow in scale, attempting to understand or manage them directly at the raw code level leads to architectural decay, catastrophic bugs, and budget overruns.</p>
    <p>According to AKTU Quantum (Que 1.12), modelling serves <strong>five critical engineering purposes</strong>: (1) Testing a physical/virtual entity before building it, (2) Seamless communication with customers and stakeholders, (3) Visualization of system dynamics, (4) Reduction of overwhelming complexity, and (5) Architectural documentation and traceability.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Scale Aircraft in Wind Tunnels &amp; Hollywood Storyboards</div>
  <p>Consider two vivid analogies cited in engineering literature: First, <strong>Boeing testing scale model airplanes in supersonic wind tunnels</strong>. Simulating airflow over a scaled composite model reveals turbulence and drag flaws safely. Building a full airliner immediately and discovering aerodynamic instability during its maiden flight would be catastrophic! Second, <strong>Hollywood directors creating storyboards</strong> before shooting a $200M blockbuster. Storyboards allow writers and cinematographers to spot pacing and narrative plot holes before hiring thousands of actors and renting expensive cameras.</p>
</div>

<div class="subtopics-container">
  <h4>The 5 Major Purposes Served by Models (AKTU Que 1.12)</h4>

  <div class="detail-block">
    <h5>1. Testing Before Building</h5>
    <p>Simulating a model is radically cheaper than building a complete physical or software deployment. It enables the detection of architectural bottlenecks, memory leaks, and concurrency deadlocks in the design phase when changes require only updating diagrams.</p>
  </div>

  <div class="detail-block">
    <h5>2. Communication with Customers &amp; Domain Experts</h5>
    <p>Clients and business owners rarely understand C++ pointers, database indexes, or microservice mesh configs. Visual models (Use Case diagrams, Activity diagrams, Conceptual Domain models) provide a common, ambiguity-free visual vocabulary between technical architects and non-programming domain experts.</p>
  </div>

  <div class="detail-block">
    <h5>3. System Visualization</h5>
    <p>Models translate abstract mental representations into concrete graphical depictions. Architects can instantly inspect how components interface, how messages flow across network boundaries, and how data changes state over time.</p>
  </div>

  <div class="detail-block">
    <h5>4. Reduction of Complexity</h5>
    <p>Modern enterprise platforms possess millions of variables and paths. Human working memory (Miller's Law: 7 &plusmn; 2 chunks) cannot process entire codebases at once. Models decompose colossal systems into manageable, orthogonal subsystems.</p>
  </div>

  <div class="detail-block">
    <h5>5. Architecture Documentation &amp; Forward/Reverse Engineering</h5>
    <p>Models serve as the permanent blueprinted institutional knowledge for a codebase, surviving employee turnover. They guide automated code generation tools and facilitate regression auditing.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Ad-hoc 'Code &amp; Fix' vs Model-Driven Engineering</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Engineering Dimension</th>
        <th>Ad-hoc "Code &amp; Fix" Approach</th>
        <th>Model-Driven Engineering</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Design Phase</strong></td>
        <td>Skipped; developers start coding immediately</td>
        <td>Thorough analysis, domain modeling &amp; simulation</td>
      </tr>
      <tr>
        <td><strong>Customer Alignment</strong></td>
        <td>Customer sees product only at delivery; high rejection rate</td>
        <td>Customer inspects mock-ups and use cases iteratively</td>
      </tr>
      <tr>
        <td><strong>Defect Resolution Cost</strong></td>
        <td>100x to 500x more expensive when found in production</td>
        <td>Minimal cost when detected during architectural modeling</td>
      </tr>
      <tr>
        <td><strong>Maintainability</strong></td>
        <td>Spaghetti code; fragile dependencies cause ripple failures</td>
        <td>Decoupled modular architecture with documented contracts</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The 5 Pillars of Modeling Importance</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Central Hub: Software Model -->
      <g transform="translate(335, 100)">
        <circle cx="75" cy="40" r="45" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
        <text x="75" y="37" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">SOFTWARE</text>
        <text x="75" y="52" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">MODEL</text>
      </g>

      <!-- Pillar 1: Testing & Simulation (Top Left) -->
      <g transform="translate(40, 25)">
        <rect width="210" height="65" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
        <rect width="210" height="22" rx="8" fill="#9f1239"/>
        <text x="105" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1. TESTING &amp; SIMULATION</text>
        <text x="10" y="38" fill="#fca5a5" font-size="9">• Wind-tunnel scale testing</text>
        <text x="10" y="52" fill="#94a3b8" font-size="8">• Catch architectural flaws early</text>
      </g>
      <line x1="250" y1="60" x2="340" y2="115" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,2"/>

      <!-- Pillar 2: Customer Communication (Top Right) -->
      <g transform="translate(570, 25)">
        <rect width="210" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
        <rect width="210" height="22" rx="8" fill="#065f46"/>
        <text x="105" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">2. CUSTOMER COMM</text>
        <text x="10" y="38" fill="#6ee7b7" font-size="9">• Visual mock-ups &amp; use cases</text>
        <text x="10" y="52" fill="#94a3b8" font-size="8">• Common domain vocabulary</text>
      </g>
      <line x1="570" y1="60" x2="480" y2="115" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,2"/>

      <!-- Pillar 3: Visualization (Bottom Left) -->
      <g transform="translate(40, 185)">
        <rect width="210" height="65" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
        <rect width="210" height="22" rx="8" fill="#7e22ce"/>
        <text x="105" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">3. VISUALIZATION</text>
        <text x="10" y="38" fill="#c084fc" font-size="9">• Hollywood storyboard effect</text>
        <text x="10" y="52" fill="#94a3b8" font-size="8">• Graphical clarity of flow</text>
      </g>
      <line x1="250" y1="210" x2="340" y2="165" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4,2"/>

      <!-- Pillar 4: Complexity Reduction (Bottom Right) -->
      <g transform="translate(570, 185)">
        <rect width="210" height="65" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
        <rect width="210" height="22" rx="8" fill="#b45309"/>
        <text x="105" y="16" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">4. COMPLEXITY CONTROL</text>
        <text x="10" y="38" fill="#fde68a" font-size="9">• Modular subsystem chunking</text>
        <text x="10" y="52" fill="#94a3b8" font-size="8">• Miller's 7 ± 2 cognitive limit</text>
      </g>
      <line x1="570" y1="210" x2="480" y2="165" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,2"/>

      <!-- Pillar 5: Traceability (Center Top) -->
      <g transform="translate(315, 10)">
        <rect width="190" height="35" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="95" y="22" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">5. Traceability &amp; Documentation</text>
      </g>
      <line x1="410" y1="45" x2="410" y2="95" stroke="#60a5fa" stroke-width="1.5" stroke-dasharray="4,2"/>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2013-14):</strong> <em>"Discuss several purposes served by models with suitable examples."</em> [5 Marks - Que 1.12]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> You must list and detail the four explicit points from Quantum: <strong>(a) Testing a physical entity before building it</strong> (cite airplane wind tunnel scale model), <strong>(b) Communication with customers</strong> (software mock-ups/storyboards), <strong>(c) Visualization</strong> (storyboards for movies/ads), and <strong>(d) Reduction of complexity</strong> (omitting non-essential details).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Testing:</strong> Simulating a model detects architectural defects before writing thousands of lines.</li>
    <li><strong>Communication:</strong> Provides a clear visual bridge between engineers and non-technical clients.</li>
    <li><strong>Visualization:</strong> Makes abstract code structures and control flows tangible.</li>
    <li><strong>Complexity Reduction:</strong> Modularizes massive systems into human-comprehensible views.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 11: Principles of Modelling
        # -------------------------------------------------------------
        {
            "id": "u1-sec-11",
            "number": "11",
            "part": "Part 3 — Modelling",
            "title": "Principles of Modelling",
            "subtitle": "The 4 Core Principles (C-P-R-M): Choice, Precision, Reality & Multiple Models",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Architectural Axioms</div>
    <h3>The 4 Foundational Principles of Modelling</h3>
    <p>Graddy Booch, James Rumbaugh, and Ivar Jacobson formulated <strong>Four Fundamental Principles of Modeling</strong> that govern all rigorous engineering disciplines, from aerospace to enterprise software design.</p>
    <p>According to AKTU Quantum (Que 1.15), these principles ensure that models genuinely guide the construction of successful systems rather than becoming disconnected bureaucratic documentation.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Cartographer's Maps of New York City</div>
  <p>Consider navigating New York City: If you are taking the subway, you need a <strong>schematic transit map</strong> (showing stations and transfers, ignoring street distances). If you are driving a delivery truck, you need a <strong>topological road map</strong> (showing one-way streets, bridge clearance heights, and traffic lights). If you are a civil engineer fixing water mains, you need an <strong>underground utility blueprint</strong>. No single map can serve all three! You choose the model that shapes the solution, adjust the precision, stay anchored to physical reality, and use multiple complementary views.</p>
</div>

<div class="subtopics-container">
  <h4>The 4 Core Principles Explained (AKTU Que 1.15)</h4>

  <div class="detail-block">
    <h5>Principle 1: The choice of model has a profound influence on how the problem is attacked</h5>
    <p>The choice of what models you create dictates how you view the problem and shapes your eventual solution. If you model a system with relational tables, your solution will be data-centric; if you model it using object hierarchies and polymorphism, your solution will be modular and extensible; if you model it using reactive message streams, your solution will be event-driven.</p>
  </div>

  <div class="detail-block">
    <h5>Principle 2: Every model may be expressed at different levels of precision</h5>
    <p>A model is not a one-size-fits-all zoom level. During early inception, an architect needs an executive high-level conceptual model (macro view). During implementation, a developer requires a microscopic model specifying method signatures, parameter types, exceptions, and pre/post-conditions.</p>
  </div>

  <div class="detail-block">
    <h5>Principle 3: The best models are connected to reality</h5>
    <p>A mathematical model may be theoretically elegant, but if it assumes infinite memory, zero network latency, or frictionless data serialization, it will fail in production. Successful software models mirror physical real-world boundaries, hardware topology, and actual business constraints.</p>
  </div>

  <div class="detail-block">
    <h5>Principle 4: No single model is sufficient; every non-trivial system requires multiple independent models</h5>
    <p>Attempting to capture an entire enterprise platform in a single colossal diagram results in incomprehensible noise. A complex system must be approached through a set of nearly independent, orthogonal models (such as Kruchten's 4+1 Architectural Views: Use Case, Logical, Process, Implementation, and Deployment views).</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>The 4 Principles of Modelling Matrix (CPRM Mnemonic)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Principle</th>
        <th>Mnemonic</th>
        <th>Engineering Rule</th>
        <th>Violation Consequence</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Choice of Model</strong></td>
        <td><strong>C</strong>hoice</td>
        <td>Choose the modeling paradigm that matches the problem domain</td>
        <td>Forcing square pegs into round holes (e.g. procedural code for GUI events)</td>
      </tr>
      <tr>
        <td><strong>Precision Levels</strong></td>
        <td><strong>P</strong>recision</td>
        <td>Zoom from macro architecture down to micro code contracts as phases progress</td>
        <td>Drowning in trivial details during analysis, or missing API signatures in design</td>
      </tr>
      <tr>
        <td><strong>Reality Connection</strong></td>
        <td><strong>R</strong>eality</td>
        <td>Anchor abstractions to tangible business rules, network limits, and hardware</td>
        <td>Building a fantasy system that crashes due to physical resource exhaustion</td>
      </tr>
      <tr>
        <td><strong>Multiple Models</strong></td>
        <td><strong>M</strong>ultiple</td>
        <td>Use orthogonal structural, behavioral, and deployment views</td>
        <td>Single giant unreadable diagram that stakeholders and coders both abandon</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The 4 Principles of Modelling Framework (CPRM)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Principle 1 (Top-Left) -->
      <g transform="translate(30, 25)">
        <rect width="365" height="105" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="365" height="28" rx="8" fill="#0369a1"/>
        <text x="182" y="19" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1. CHOICE OF MODEL INFLUENCES SOLUTION</text>
        <text x="15" y="48" fill="#93c5fd" font-size="10" font-weight="bold">The lens determines what you see:</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="9">• OO Model → Extensible polymorphism &amp; components</text>
        <text x="15" y="86" fill="#e2e8f0" font-size="9">• Relational Model → Normalized tables &amp; SQL joins</text>
      </g>

      <!-- Principle 2 (Top-Right) -->
      <g transform="translate(425, 25)">
        <rect width="365" height="105" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="365" height="28" rx="8" fill="#7e22ce"/>
        <text x="182" y="19" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">2. LEVELS OF PRECISION (ZOOM FACTOR)</text>
        <text x="15" y="48" fill="#c084fc" font-size="10" font-weight="bold">Varying granularities of detail:</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="9">• Inception: High-level packages &amp; conceptual boxes</text>
        <text x="15" y="86" fill="#e2e8f0" font-size="9">• Construction: Exact types, pre-conditions &amp; signatures</text>
      </g>

      <!-- Principle 3 (Bottom-Left) -->
      <g transform="translate(30, 150)">
        <rect width="365" height="105" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="365" height="28" rx="8" fill="#047857"/>
        <text x="182" y="19" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">3. CONNECTED TO REALITY</text>
        <text x="15" y="48" fill="#6ee7b7" font-size="10" font-weight="bold">Grounded in physical truth:</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="9">• Respect hardware limits, latency &amp; memory</text>
        <text x="15" y="86" fill="#e2e8f0" font-size="9">• Mirror actual business rules and legal workflows</text>
      </g>

      <!-- Principle 4 (Bottom-Right) -->
      <g transform="translate(425, 150)">
        <rect width="365" height="105" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
        <rect width="365" height="28" rx="8" fill="#b45309"/>
        <text x="182" y="19" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">4. NO SINGLE MODEL IS SUFFICIENT</text>
        <text x="15" y="48" fill="#fde68a" font-size="10" font-weight="bold">Multiple orthogonal viewpoints:</text>
        <text x="15" y="68" fill="#e2e8f0" font-size="9">• Structural (Classes) + Behavioral (States/Interactions)</text>
        <text x="15" y="86" fill="#e2e8f0" font-size="9">• Kruchten's 4+1 views (Use case, Logical, Process, etc.)</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14, 2014-15):</strong> <em>"What are the principles of modeling? What is the importance of modeling?"</em> [5 Marks - Que 1.15]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Write all four principles verbatim: <strong>(1) Choice of model influences how a problem is attacked, (2) Expressed at different levels of precision, (3) Best models are connected to reality, and (4) No single model is sufficient (small set of nearly independent models)</strong>. Connect point 4 to architectural views (Design, Process, Implementation, Deployment).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Choice:</strong> The modeling language chosen dictates how you conceptualize the solution.</li>
    <li><strong>Precision:</strong> Architects use conceptual macro views; coders use microscopic API contracts.</li>
    <li><strong>Reality:</strong> Models must reflect physical hardware and operational runtime constraints.</li>
    <li><strong>Multiple Views:</strong> Complex systems require multiple orthogonal diagrams (4+1 views).</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 12: Object-Oriented Modelling (OOM)
        # -------------------------------------------------------------
        {
            "id": "u1-sec-12",
            "number": "12",
            "part": "Part 3 — Modelling",
            "title": "Object-Oriented Modelling",
            "subtitle": "OOM Lifecycle, Abstraction & The 4-Stage OOM Pipeline",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Engineering Methodology</div>
    <h3>What is Object-Oriented Modelling (OOM)?</h3>
    <p><strong>Object-Oriented Modelling (OOM)</strong> is a disciplined software engineering approach that constructs an application as a collection of discrete, interacting objects encapsulating both data (instance variables) and behavior (methods).</p>
    <p>According to AKTU Quantum (Que 1.16), OOM is utilized at the beginning of the software lifecycle. The complete OOM process unfolds across four systematic stages: <strong>(1) System Analysis, (2) System Design, (3) Object Design, and (4) Final Implementation</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Lego Mindstorms Robotics Kit</div>
  <p>Imagine engineering an automated robotic rover with a <strong>Lego Mindstorms kit</strong>. You don't manufacture custom plastic from petroleum pellets; you work with standardized modular components: an intelligent brick (controller), servo motors (actuators), ultrasonic sensors (inputs), and sturdy gears (mechanics). Each component has known connection studs (interfaces) and specific functions. Object-Oriented Modelling builds software the exact same way—assembling modular, cohesive, pre-tested object blueprints into sophisticated automated machines.</p>
</div>

<div class="subtopics-container">
  <h4>The 4 Stages of the OOM Process (AKTU Que 1.16)</h4>

  <div class="detail-block">
    <h5>Stage 1: System Analysis (Formulating the Problem - WHAT)</h5>
    <p>In this initial phase, the analyst formulates a statement of the problem and constructs a clean abstraction of the real-world situation. The analysis model contains purely <strong>application-domain concepts</strong> (e.g., Bank Account, ATM Card, Ledger). It deliberately omits programming concepts like pointers, operating system handles, or SQL schemas so domain experts can validate requirements.</p>
  </div>

  <div class="detail-block">
    <h5>Stage 2: System Design (Structuring the Architecture)</h5>
    <p>The high-level overall system architecture is devised. The complete system is partitioned into discrete <strong>subsystems</strong> based on both analysis structure and proposed physical topology. Key decisions are made regarding client-server partitioning, database selection, concurrency/threading strategies, and resource allocations.</p>
  </div>

  <div class="detail-block">
    <h5>Stage 3: Object Design (Detailing the Mechanics - HOW)</h5>
    <p>The conceptual analysis model is augmented with <strong>computer-domain concepts</strong>. The object designer chooses concrete data structures (hash maps, binary trees, arrays) and efficient algorithms (quicksort, graph traversal) to implement each class and association while optimizing performance.</p>
  </div>

  <div class="detail-block">
    <h5>Stage 4: Final Implementation (Executable Code)</h5>
    <p>The refined classes, associations, and state machines are translated into target programming language source code (e.g., C++, Java). Rigorous software engineering practices ensure full traceability back to the original analysis requirements.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>OOM Stage Breakdown Matrix</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Stage</th>
        <th>Primary Focus</th>
        <th>Key Artifacts Produced</th>
        <th>Domain Vocabulary</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. System Analysis</strong></td>
        <td><strong>WHAT</strong> the system must do</td>
        <td>Use Case Models, Conceptual Class Diagrams</td>
        <td>Application / Business concepts</td>
      </tr>
      <tr>
        <td><strong>2. System Design</strong></td>
        <td><strong>WHERE &amp; AT WHAT SCALE</strong></td>
        <td>Package diagrams, Subsystem topology, IPC design</td>
        <td>Architectural &amp; hardware tiers</td>
      </tr>
      <tr>
        <td><strong>3. Object Design</strong></td>
        <td><strong>HOW</strong> classes compute &amp; store</td>
        <td>Detailed Class diagrams with algorithms &amp; data structures</td>
        <td>Computer / algorithmic concepts</td>
      </tr>
      <tr>
        <td><strong>4. Implementation</strong></td>
        <td><strong>CONSTRUCT</strong> executable software</td>
        <td>Source code, DB schemas, unit test suites</td>
        <td>Target programming language syntax</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The 4-Stage OOM Pipeline with Artifact Transformations</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="260" fill="#0f172a" rx="12"/>

      <!-- Stage 1 -->
      <g transform="translate(25, 35)">
        <rect width="170" height="190" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="170" height="30" rx="8" fill="#0369a1"/>
        <text x="85" y="20" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1. SYSTEM ANALYSIS</text>
        <text x="12" y="52" fill="#93c5fd" font-size="9" font-weight="bold">Focus: WHAT</text>
        <text x="12" y="74" fill="#e2e8f0" font-size="8">• Problem Statement</text>
        <text x="12" y="94" fill="#e2e8f0" font-size="8">• Real-World Model</text>
        <text x="12" y="114" fill="#e2e8f0" font-size="8">• Domain Concepts</text>
        <text x="12" y="134" fill="#e2e8f0" font-size="8">• User Understandable</text>
        <rect x="12" y="150" width="146" height="26" rx="4" fill="#0c4a6e"/>
        <text x="85" y="167" fill="#38bdf8" font-size="8" text-anchor="middle">Analysis Classes</text>
      </g>

      <!-- Arrow 1 to 2 -->
      <path d="M 200 130 L 225 130" stroke="#60a5fa" stroke-width="2" marker-end="url(#u1-oom-arr)"/>

      <!-- Stage 2 -->
      <g transform="translate(230, 35)">
        <rect width="170" height="190" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="170" height="30" rx="8" fill="#b45309"/>
        <text x="85" y="20" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">2. SYSTEM DESIGN</text>
        <text x="12" y="52" fill="#fde68a" font-size="9" font-weight="bold">Focus: ARCHITECTURE</text>
        <text x="12" y="74" fill="#e2e8f0" font-size="8">• Subsystem Partitioning</text>
        <text x="12" y="94" fill="#e2e8f0" font-size="8">• Hardware / Concurrency</text>
        <text x="12" y="114" fill="#e2e8f0" font-size="8">• Database Strategy</text>
        <text x="12" y="134" fill="#e2e8f0" font-size="8">• Resource Allocation</text>
        <rect x="12" y="150" width="146" height="26" rx="4" fill="#78350f"/>
        <text x="85" y="167" fill="#fcd34d" font-size="8" text-anchor="middle">Subsystems &amp; Tiers</text>
      </g>

      <!-- Arrow 2 to 3 -->
      <path d="M 405 130 L 430 130" stroke="#60a5fa" stroke-width="2" marker-end="url(#u1-oom-arr)"/>

      <!-- Stage 3 -->
      <g transform="translate(435, 35)">
        <rect width="170" height="190" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="170" height="30" rx="8" fill="#7e22ce"/>
        <text x="85" y="20" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">3. OBJECT DESIGN</text>
        <text x="12" y="52" fill="#c084fc" font-size="9" font-weight="bold">Focus: HOW</text>
        <text x="12" y="74" fill="#e2e8f0" font-size="8">• Data Structures (Hash/Tree)</text>
        <text x="12" y="94" fill="#e2e8f0" font-size="8">• Concrete Algorithms</text>
        <text x="12" y="114" fill="#e2e8f0" font-size="8">• Method Signatures</text>
        <text x="12" y="134" fill="#e2e8f0" font-size="8">• Association Realization</text>
        <rect x="12" y="150" width="146" height="26" rx="4" fill="#581c87"/>
        <text x="85" y="167" fill="#e9d5ff" font-size="8" text-anchor="middle">Detailed Class Specs</text>
      </g>

      <!-- Arrow 3 to 4 -->
      <path d="M 610 130 L 635 130" stroke="#60a5fa" stroke-width="2" marker-end="url(#u1-oom-arr)"/>

      <!-- Stage 4 -->
      <g transform="translate(640, 35)">
        <rect width="155" height="190" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="155" height="30" rx="8" fill="#047857"/>
        <text x="77" y="20" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">4. IMPLEMENTATION</text>
        <text x="12" y="52" fill="#6ee7b7" font-size="9" font-weight="bold">Focus: BINARY CODE</text>
        <text x="12" y="74" fill="#e2e8f0" font-size="8">• Target Syntax (C++)</text>
        <text x="12" y="94" fill="#e2e8f0" font-size="8">• Database Schemas</text>
        <text x="12" y="114" fill="#e2e8f0" font-size="8">• Unit Test Coverage</text>
        <text x="12" y="134" fill="#e2e8f0" font-size="8">• Requirement Trace</text>
        <rect x="12" y="150" width="131" height="26" rx="4" fill="#064e3b"/>
        <text x="77" y="167" fill="#a7f3d0" font-size="8" text-anchor="middle">Executable App</text>
      </g>

      <defs>
        <marker id="u1-oom-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11):</strong> <em>"Define object-oriented modeling (OOM). Describe various steps involved in OOM process. Explain."</em> [5 Marks - Que 1.16]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define OOM as constructing systems using a collection of objects that encapsulate stored values and methods. Explain the four steps clearly: <strong>System Analysis</strong> (problem formulation &amp; real-world model), <strong>System Design</strong> (subsystem partitioning &amp; architecture), <strong>Object Design</strong> (data structures &amp; algorithms), and <strong>Final Implementation</strong> (translating classes to code following SE practices).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>OOM:</strong> Constructing systems out of discrete objects containing state and operations.</li>
    <li><strong>Analysis:</strong> Focuses on the domain (WHAT); understandable to non-programmers.</li>
    <li><strong>System Design:</strong> High-level architectural partitioning into subsystems and tiers.</li>
    <li><strong>Object Design:</strong> Augmenting domain classes with concrete algorithms and data structures (HOW).</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 13: Three Models of OMT
        # -------------------------------------------------------------
        {
            "id": "u1-sec-13",
            "number": "13",
            "part": "Part 3 — Modelling",
            "title": "Three Models of OMT",
            "subtitle": "James Rumbaugh's OMT Methodology: Object Model, Dynamic Model & Functional Model",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Classic OOAD Methodology</div>
    <h3>What is the Object Modeling Technique (OMT)?</h3>
    <p>The <strong>Object Modeling Technique (OMT)</strong>, created by James Rumbaugh et al., is a seminal software engineering methodology that models a system through <strong>three orthogonal, complementary views</strong>:</p>
    <ul>
      <li><strong>1. The Object Model:</strong> Represents the static, structural framework of classes, objects, attributes, and relationships.</li>
      <li><strong>2. The Dynamic Model:</strong> Captures temporal, behavioral aspects, events, and state changes over time.</li>
      <li><strong>3. The Functional Model:</strong> Details data transformations, inputs, and algorithmic computations using Data Flow Diagrams (DFDs).</li>
    </ul>
    <p>According to AKTU Quantum (Que 1.13, Que 1.18), these three models separate a system into orthogonal views that can be represented and manipulated using uniform, precise visual notation.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: A Comprehensive Medical Examination of the Human Body</div>
  <p>To fully understand a patient's health, a doctor cannot rely on a single scan. The doctor uses three orthogonal diagnostic perspectives: (1) An <strong>X-Ray / MRI</strong> shows the static skeletal anatomy and organ structure (<em>Object Model</em>); (2) An <strong>ECG / EEG</strong> tracks heart rhythm, electrical impulses, and muscle contractions over time (<em>Dynamic Model</em>); (3) A <strong>Blood Metabolic Panel</strong> tracks biochemical transformations—how glucose is converted into glycogen and insulin (<em>Functional Model</em>). Together, they form a complete diagnostic picture!</p>
</div>

<div class="subtopics-container">
  <h4>Deep Dive: The 3 Orthogonal Models</h4>

  <div class="detail-block">
    <h5>1. The Object Model (Static Structural View)</h5>
    <p>The object model provides the foundational framework. It identifies the classes in the system, their internal data attributes, available operations, and structural associations (inheritance, aggregation, associations). It is represented graphically via <strong>Class Diagrams</strong>. It answers: <em>"What entities exist and how are they structurally connected?"</em></p>
  </div>

  <div class="detail-block">
    <h5>2. The Dynamic Model (Behavioral / Temporal View)</h5>
    <p>The dynamic model captures the functional behavior of the system over time. It models how objects react to external events, pass control signals, and transition from one discrete state to another. It is represented graphically via <strong>State Transition Diagrams</strong> and <strong>Event Trace Diagrams</strong>. It answers: <em>"When do things happen and how do states change?"</em></p>
  </div>

  <div class="detail-block">
    <h5>3. The Functional Model (Transformational View)</h5>
    <p>The functional model describes what the system does without concerning how it is implemented. It represents the flow of data values from inputs, through computational processes, into data stores and outputs. It is represented graphically via <strong>Data Flow Diagrams (DFDs)</strong>. It answers: <em>"What computations are performed and how does data transform?"</em></p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>The Three OMT Models Comparison Matrix (AKTU Que 1.13)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Object Model</th>
        <th>Dynamic Model</th>
        <th>Functional Model</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Dimension</strong></td>
        <td><strong>Structure</strong> (Static)</td>
        <td><strong>Time &amp; Sequence</strong> (Dynamic)</td>
        <td><strong>Transformation</strong> (Functional)</td>
      </tr>
      <tr>
        <td><strong>Core Question</strong></td>
        <td>What entities exist?</td>
        <td>When do state changes happen?</td>
        <td>What values are computed?</td>
      </tr>
      <tr>
        <td><strong>Key Graphical Tool</strong></td>
        <td>Class Diagrams &amp; Object Diagrams</td>
        <td>State Transition Diagrams, Sequence Diagrams</td>
        <td>Data Flow Diagrams (DFD)</td>
      </tr>
      <tr>
        <td><strong>Main Elements</strong></td>
        <td>Classes, Attributes, Operations, Links</td>
        <td>States, Events, Transitions, Actions</td>
        <td>Processes, Data Flows, Actors, Data Stores</td>
      </tr>
      <tr>
        <td><strong>Lifecycle Phase</strong></td>
        <td>Built first; foundational skeleton</td>
        <td>Built second; animates objects</td>
        <td>Built concurrently; specifies algorithms</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Three Orthogonal Models of OMT</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Model 1: Object Model (Left) -->
      <g transform="translate(30, 30)">
        <rect width="230" height="220" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="230" height="34" rx="8" fill="#0369a1"/>
        <text x="115" y="22" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">1. OBJECT MODEL</text>

        <text x="15" y="58" fill="#38bdf8" font-size="10" font-weight="bold">Static Structure (Classes)</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Identifies classes &amp; objects</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Attributes &amp; operations</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• Associations &amp; inheritance</text>
        
        <!-- Miniature Class Icon -->
        <g transform="translate(35, 135)">
          <rect width="160" height="65" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
          <rect width="160" height="18" rx="4" fill="#0284c7"/>
          <text x="80" y="13" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Account</text>
          <text x="10" y="32" fill="#94a3b8" font-size="8">- balance: double</text>
          <line x1="5" y1="38" x2="155" y2="38" stroke="#334155" stroke-width="1"/>
          <text x="10" y="52" fill="#38bdf8" font-size="8">+ deposit(amt): void</text>
        </g>
      </g>

      <!-- Model 2: Dynamic Model (Center) -->
      <g transform="translate(295, 30)">
        <rect width="230" height="220" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="230" height="34" rx="8" fill="#7e22ce"/>
        <text x="115" y="22" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2. DYNAMIC MODEL</text>

        <text x="15" y="58" fill="#c084fc" font-size="10" font-weight="bold">Behavior Over Time (States)</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• State changes &amp; events</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Control sequencing &amp; timing</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• State transition graphs</text>

        <!-- Miniature State Icon -->
        <g transform="translate(20, 145)">
          <rect x="0" y="5" width="75" height="35" rx="15" fill="#581c87" stroke="#c084fc" stroke-width="1.5"/>
          <text x="37" y="26" fill="#ffffff" font-size="9" text-anchor="middle">Idle</text>
          
          <path d="M 75 22 L 115 22" stroke="#c084fc" stroke-width="1.5" marker-end="url(#u1-omt-arr-p)"/>
          <text x="95" y="16" fill="#e9d5ff" font-size="7" text-anchor="middle">cardInserted</text>

          <rect x="115" y="5" width="75" height="35" rx="15" fill="#581c87" stroke="#c084fc" stroke-width="1.5"/>
          <text x="152" y="26" fill="#ffffff" font-size="9" text-anchor="middle">Active</text>
        </g>
      </g>

      <!-- Model 3: Functional Model (Right) -->
      <g transform="translate(560, 30)">
        <rect width="230" height="220" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="230" height="34" rx="8" fill="#047857"/>
        <text x="115" y="22" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. FUNCTIONAL MODEL</text>

        <text x="15" y="58" fill="#34d399" font-size="10" font-weight="bold">Transformations (DFD)</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Values computed by system</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Data flow &amp; algorithms</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• Actors, stores &amp; processes</text>

        <!-- Miniature DFD Icon -->
        <g transform="translate(25, 140)">
          <rect x="0" y="10" width="45" height="35" fill="#0f172a" stroke="#6ee7b7" stroke-width="1.5"/>
          <text x="22" y="31" fill="#6ee7b7" font-size="8" text-anchor="middle">User</text>

          <path d="M 45 27 L 85 27" stroke="#34d399" stroke-width="1.5" marker-end="url(#u1-omt-arr-g)"/>

          <ellipse cx="110" cy="27" rx="25" ry="20" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
          <text x="110" y="30" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Compute</text>

          <path d="M 135 27 L 155 27" stroke="#34d399" stroke-width="1.5" marker-end="url(#u1-omt-arr-g)"/>

          <!-- Data Store -->
          <line x1="155" y1="17" x2="180" y2="17" stroke="#fcd34d" stroke-width="2"/>
          <line x1="155" y1="37" x2="180" y2="37" stroke="#fcd34d" stroke-width="2"/>
          <text x="167" y="30" fill="#fcd34d" font-size="6" text-anchor="middle">DB</text>
        </g>
      </g>

      <defs>
        <marker id="u1-omt-arr-p" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#c084fc"/>
        </marker>
        <marker id="u1-omt-arr-g" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2015-16):</strong> <em>"What are the different models used in object-oriented languages? Write short note on dynamic modeling and functional modeling."</em> [5 to 10 Marks - Que 1.13, Que 1.18]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Draw the 3 orthogonal models clearly. Explain that the <strong>Object Model</strong> represents static structure via class diagrams; the <strong>Dynamic Model</strong> captures state changes over time via state diagrams; and the <strong>Functional Model</strong> details data flow transformations via DFDs (processes, actors, data stores).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Object Model:</strong> Static blueprint of classes, attributes, operations, and associations.</li>
    <li><strong>Dynamic Model:</strong> State machine capturing temporal behavior, events, and control flow.</li>
    <li><strong>Functional Model:</strong> Data Flow Diagram (DFD) capturing algorithmic input-to-output data transformation.</li>
    <li><strong>Orthogonal Views:</strong> Together, the 3 models completely define an enterprise system.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 14: Data Store
        # -------------------------------------------------------------
        {
            "id": "u1-sec-14",
            "number": "14",
            "part": "Part 3 — Modelling",
            "title": "Data Store",
            "subtitle": "Passive DFD Object, Asynchronous Access & Read/Write Arrow Notation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Functional Model Element</div>
    <h3>What is a Data Store?</h3>
    <p>A <strong>Data Store</strong> is a <strong>passive object</strong> within a Data Flow Diagram (DFD) that stores data persistently for later access by system processes.</p>
    <p>According to AKTU Quantum (Que 1.14a), unlike an active actor, a data store <strong>does not generate any operations on its own</strong>; it merely responds passively to external requests to store or retrieve values. Crucially, a data store decouples time, allowing values to be accessed in a completely different sequence from how they were generated.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Bank Safety Deposit Vault &amp; Warehouse Pallet Rack</div>
  <p>A <strong>warehouse pallet rack</strong> or <strong>bank safe</strong> is purely passive. The steel shelf never drives a forklift, never places an order, and never packs a carton. It simply holds boxes. If 10 suppliers drop off 500 packages on Monday morning, the warehouse workers can retrieve item #47 on Friday afternoon. The data store allows asynchronous buffering and out-of-order consumption without losing state!</p>
</div>

<div class="subtopics-container">
  <h4>Key Properties &amp; Notational Rules of Data Stores (AKTU Que 1.14a)</h4>

  <div class="detail-block">
    <h5>1. Passive Reactivity</h5>
    <p>A data store has zero initiative. It cannot independently trigger an alert, fire a timer, or send a network packet. It only responds when an external process executes a read or write operation.</p>
  </div>

  <div class="detail-block">
    <h5>2. Temporal Decoupling (Time Buffering)</h5>
    <p>In a pure pipeline without storage, producer and consumer must be tightly synchronized. A data store allows values to be written in real time (e.g. sensor readings logged every millisecond) and analyzed hours later in batches (e.g. nightly analytical reporting).</p>
  </div>

  <div class="detail-block">
    <h5>3. Standard Graphical Notation</h5>
    <p>In OMT and classical structured analysis (Gane &amp; Sarson / Yourdon):</p>
    <ul>
      <li>Drawn as a <strong>pair of parallel horizontal lines</strong> (or an open-ended rectangle) enclosing the name of the store.</li>
      <li><strong>Incoming Arrow (Write/Update):</strong> Represents information deposited into the store; includes adding new elements, modifying values, or deleting records.</li>
      <li><strong>Outgoing Arrow (Read/Query):</strong> Represents information retrieved from the store; includes reading full records or querying specific fields.</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Data Store vs Actor vs Process (DFD Elements)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>DFD Element</th>
        <th>Behavior Nature</th>
        <th>Standard Notation</th>
        <th>Role in Data Flow</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Data Store</strong></td>
        <td><strong>Passive</strong> (holds state)</td>
        <td>Two parallel horizontal lines</td>
        <td>Stores data persistently; responds to read/write queries</td>
      </tr>
      <tr>
        <td><strong>Actor</strong></td>
        <td><strong>Active</strong> (initiates actions)</td>
        <td>Rectangle or stick figure</td>
        <td>Drives system by producing or consuming boundary data</td>
      </tr>
      <tr>
        <td><strong>Process</strong></td>
        <td><strong>Transformational</strong> (computes)</td>
        <td>Circle or rounded rectangle</td>
        <td>Transforms input data flows into output data flows</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Data Store Notation with Read &amp; Write Data Flows (AKTU Que 1.14a)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="260" fill="#0f172a" rx="12"/>

      <!-- Process 1: Write Operation (Left) -->
      <g transform="translate(40, 95)">
        <ellipse cx="80" cy="35" rx="75" ry="32" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="32" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Process 1.0</text>
        <text x="80" y="47" fill="#38bdf8" font-size="9" text-anchor="middle">RegisterUser()</text>
      </g>

      <!-- Input Data Flow Arrow (Write) -->
      <path d="M 195 130 L 305 130" stroke="#38bdf8" stroke-width="2" marker-end="url(#u1-ds-arr-blue)"/>
      <rect x="205" y="105" width="90" height="18" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1"/>
      <text x="250" y="117" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Write: UserData</text>

      <!-- Data Store (Center) -->
      <g transform="translate(315, 90)">
        <!-- Top Parallel Line -->
        <line x1="0" y1="0" x2="190" y2="0" stroke="#fbbf24" stroke-width="3"/>
        <!-- Bottom Parallel Line -->
        <line x1="0" y1="80" x2="190" y2="80" stroke="#fbbf24" stroke-width="3"/>
        <!-- Background Fill -->
        <rect x="0" y="2" width="190" height="76" fill="#1e293b" opacity="0.9"/>
        
        <text x="95" y="35" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">D1: UserAccounts</text>
        <text x="95" y="55" fill="#94a3b8" font-size="9" text-anchor="middle">Passive Persistent Store</text>
      </g>

      <!-- Output Data Flow Arrow (Read) -->
      <path d="M 505 130 L 615 130" stroke="#34d399" stroke-width="2" marker-end="url(#u1-ds-arr-green)"/>
      <rect x="515" y="105" width="90" height="18" rx="4" fill="#0f172a" stroke="#047857" stroke-width="1"/>
      <text x="560" y="117" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Read: Credentials</text>

      <!-- Process 2: Read Operation (Right) -->
      <g transform="translate(625, 95)">
        <ellipse cx="80" cy="35" rx="75" ry="32" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <text x="80" y="32" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Process 2.0</text>
        <text x="80" y="47" fill="#34d399" font-size="9" text-anchor="middle">Authenticate()</text>
      </g>

      <!-- Annotational Notes -->
      <g transform="translate(260, 200)">
        <rect width="300" height="40" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
        <text x="150" y="18" fill="#e2e8f0" font-size="9" text-anchor="middle">• Input arrows add, update, or delete records</text>
        <text x="150" y="32" fill="#e2e8f0" font-size="9">• Output arrows retrieve full or partial values</text>
      </g>

      <defs>
        <marker id="u1-ds-arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="u1-ds-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2015-16):</strong> <em>"Write short note on: Data store."</em> [Part of 15-Mark Composite Question - Que 1.14a]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> State that a data store is a passive object in DFDs storing data for later access. Highlight that it does not generate operations on its own. Draw the pair of parallel lines notation. Explain the meaning of incoming arrows (modifying/deleting/inserting) and outgoing arrows (retrieving data).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Passive Entity:</strong> Does not generate actions; responds only to external read/write operations.</li>
    <li><strong>Temporal Decoupling:</strong> Allows values to be retrieved in a different order from how they were saved.</li>
    <li><strong>Notation:</strong> Drawn as two parallel horizontal lines enclosing the store's name.</li>
    <li><strong>Flows:</strong> Incoming arrow = write/modify/delete; Outgoing arrow = retrieve/query.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 15: Actors
        # -------------------------------------------------------------
        {
            "id": "u1-sec-15",
            "number": "15",
            "part": "Part 3 — Modelling",
            "title": "Actors",
            "subtitle": "Active Driving Entities, System Boundaries & Hardware/User Categorization",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Boundary Element</div>
    <h3>What is an Actor?</h3>
    <p>An <strong>Actor</strong> is an <strong>active entity</strong> that resides outside the system boundary and drives the system by producing inputs (values/stimuli) or consuming outputs generated by system processes.</p>
    <p>According to AKTU Quantum (Que 1.14b), actors are attached to the inputs and outputs of a data flow graph. Crucially, actors are not limited to human users: they encompass external hardware devices, automated sensors, actuators, and third-party software systems.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Smart Home Thermostat System</div>
  <p>Consider a smart home heating and cooling system: (1) The <strong>Homeowner</strong> is a human actor who inputs the desired temperature (<em>e.g., 22&deg;C</em>) via a mobile app; (2) The <strong>Bimetallic Thermostat Sensor</strong> is an autonomous hardware actor that continuously measures ambient temperature and outputs voltage signals; (3) The <strong>Gas Furnace Motor</strong> is an actuator actor that consumes on/off control commands. All three exist on the boundary of the smart control software!</p>
</div>

<div class="subtopics-container">
  <h4>Characteristics &amp; Classifications of Actors (AKTU Que 1.14b)</h4>

  <div class="detail-block">
    <h5>1. Active Driver of the System</h5>
    <p>Unlike passive data stores, actors have autonomy and initiative. They generate events unpredictably based on real-world triggers (e.g. a user pressing a keyboard key or a sensor reaching a temperature threshold).</p>
  </div>

  <div class="detail-block">
    <h5>2. Three Primary Categories of Actors</h5>
    <ul>
      <li><strong>Human Users:</strong> Customers, Bank Tellers, System Administrators who interact via graphical user interfaces.</li>
      <li><strong>Autonomous Hardware / Sensors:</strong> Thermostats, GPS transceivers, barcode scanners, and radar antennae that pump continuous telemetry data.</li>
      <li><strong>External Software Systems:</strong> Third-party payment gateways (Stripe, PayPal), credit scoring agencies, or national weather APIs.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Graphical Representation</h5>
    <p>In OMT and DFD diagrams, an actor is drawn as a <strong>solid rectangle</strong> (to signify that it is an object) or as a <strong>stick figure</strong> in UML Use Case models. Directed arrows connecting the actor to system processes represent input stimuli or output delivery.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Actor Types &amp; Interaction Profiles</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Actor Category</th>
        <th>Concrete Example</th>
        <th>Data Produced (Input to System)</th>
        <th>Data Consumed (Output from System)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Human Operator</strong></td>
        <td>Bank Customer</td>
        <td>PIN, Account Number, Withdrawal Amount</td>
        <td>Account Balance, Cash Receipt, Error Prompts</td>
      </tr>
      <tr>
        <td><strong>Hardware Sensor</strong></td>
        <td>Digital Thermostat</td>
        <td>Continuous temperature voltage readings</td>
        <td>Calibration commands, ping health checks</td>
      </tr>
      <tr>
        <td><strong>Actuator Device</strong></td>
        <td>Computer-controlled Motor</td>
        <td>Speed tachometer feedback</td>
        <td>Start/Stop signals, RPM drive frequency</td>
      </tr>
      <tr>
        <td><strong>External System</strong></td>
        <td>Payment Gateway (Stripe)</td>
        <td>Transaction auth tokens, charge settlement</td>
        <td>Encrypted credit card payload, charge amount</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Actors Driving the System Boundary (AKTU Que 1.14b)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- System Boundary Box -->
      <rect x="260" y="20" width="300" height="240" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
      <text x="410" y="42" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">SYSTEM BOUNDARY</text>

      <!-- Internal Process -->
      <g transform="translate(330, 90)">
        <ellipse cx="80" cy="45" rx="75" ry="40" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="42" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Temperature</text>
        <text x="80" y="58" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Control Subsystem</text>
      </g>

      <!-- Actor 1: Human User (Left Top) -->
      <g transform="translate(30, 40)">
        <rect width="170" height="75" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="170" height="24" rx="8" fill="#7e22ce"/>
        <text x="85" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">&lt;&lt;Actor&gt;&gt; Homeowner</text>
        <text x="85" y="48" fill="#c084fc" font-size="9" text-anchor="middle">Human User</text>
        <text x="85" y="64" fill="#94a3b8" font-size="8" text-anchor="middle">Sets desired temp</text>
      </g>
      <!-- Flow from User -->
      <path d="M 200 80 L 330 115" stroke="#a855f7" stroke-width="2" marker-end="url(#u1-act-arr-purple)"/>
      <text x="250" y="90" fill="#c084fc" font-size="8" font-weight="bold">targetTemp (22°C)</text>

      <!-- Actor 2: Thermostat Sensor (Left Bottom) -->
      <g transform="translate(30, 160)">
        <rect width="170" height="75" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="170" height="24" rx="8" fill="#047857"/>
        <text x="85" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">&lt;&lt;Actor&gt;&gt; Thermostat</text>
        <text x="85" y="48" fill="#6ee7b7" font-size="9" text-anchor="middle">Hardware Sensor</text>
        <text x="85" y="64" fill="#94a3b8" font-size="8" text-anchor="middle">Measures ambient temp</text>
      </g>
      <!-- Flow from Sensor -->
      <path d="M 200 195 L 330 155" stroke="#10b981" stroke-width="2" marker-end="url(#u1-act-arr-green)"/>
      <text x="250" y="185" fill="#6ee7b7" font-size="8" font-weight="bold">ambientTemp (18°C)</text>

      <!-- Actor 3: Motor Actuator (Right Center) -->
      <g transform="translate(620, 100)">
        <rect width="170" height="75" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="170" height="24" rx="8" fill="#b45309"/>
        <text x="85" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">&lt;&lt;Actor&gt;&gt; Furnace Motor</text>
        <text x="85" y="48" fill="#fcd34d" font-size="9" text-anchor="middle">Actuator Device</text>
        <text x="85" y="64" fill="#94a3b8" font-size="8" text-anchor="middle">Consumes control values</text>
      </g>
      <!-- Flow to Motor -->
      <path d="M 490 135 L 620 135" stroke="#f59e0b" stroke-width="2" marker-end="url(#u1-act-arr-yellow)"/>
      <text x="555" y="125" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle">startFurnace()</text>

      <defs>
        <marker id="u1-act-arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
        <marker id="u1-act-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981"/>
        </marker>
        <marker id="u1-act-arr-yellow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2015-16):</strong> <em>"Write short note on: Actors."</em> [Part of 15-Mark Composite Question - Que 1.14b]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define an actor as an active object that drives the data flow graph by producing or consuming values. Emphasize that actors are attached to inputs and outputs of the diagram. Cite the exact three examples given in Quantum: <strong>(1) User of a program, (2) A thermostat, and (3) A motor under computer control</strong>. Note that it is drawn as a solid rectangle.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Active Object:</strong> Has autonomy and drives computation by producing or consuming values.</li>
    <li><strong>System Boundary:</strong> Always resides outside the system boundary.</li>
    <li><strong>Three Flavors:</strong> Human users, hardware sensors (thermostat), and actuators (motor).</li>
    <li><strong>Notation:</strong> Drawn as a solid rectangle in DFDs or a stick figure in UML Use Case models.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 16: Control Flow
        # -------------------------------------------------------------
        {
            "id": "u1-sec-16",
            "number": "16",
            "part": "Part 3 — Modelling",
            "title": "Control Flow",
            "subtitle": "Boolean Enable Signals in DFDs, Dotted Line Notation & Data Flow vs Control Flow",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Execution Mechanism</div>
    <h3>What is Control Flow in Modelling?</h3>
    <p>In standard Data Flow Diagrams (DFDs), all possible computational paths for data values are depicted, but the diagram does not inherently indicate <strong>which paths are executed or in what temporal sequence</strong>.</p>
    <p>According to AKTU Quantum (Que 1.14c), sequence and conditional execution are expressed through <strong>Control Flow</strong>. A control flow is a <strong>Boolean signal</strong> that affects whether a process is evaluated or suppressed. Crucially, <em>a control flow is not an input value to the calculation itself</em>—it acts as an execution trigger or gatekeeper.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Conveyor Belt Photocell &amp; Emergency Stop Wire</div>
  <p>Think of an automated bottling plant: A conveyor belt carries soda cans toward a capping machine (<em>Data Flow of physical items</em>). Mounted above the belt is an infrared photocell sensor. If no can is under the nozzle, the sensor sends a Boolean <code>FALSE</code> signal along a thin electrical wire to disable the capper (<em>Control Flow</em>). The capping machine does not crush the wire or drink the electricity; the Boolean wire simply controls <em>whether</em> the pneumatic press fires!</p>
</div>

<div class="subtopics-container">
  <h4>Key Principles of Control Flow (AKTU Que 1.14c)</h4>

  <div class="detail-block">
    <h5>1. Not an Input to Computation</h5>
    <p>A mathematical process computing <code>netPay = grossPay - tax</code> receives <code>grossPay</code> and <code>tax</code> as numerical data inputs. A control flow signal from an authorization module (<code>isEmployeeActive == true</code>) dictates whether the payroll process runs at all, but the Boolean value is not added or subtracted in the formula.</p>
  </div>

  <div class="detail-block">
    <h5>2. Graphical Notation: The Dotted Line</h5>
    <p>To avoid confusing data values with execution signals, graphical modeling standards define distinct line styles:</p>
    <ul>
      <li><strong>Solid Arrow (&rarr;):</strong> Represents a pipeline carrying tangible data values (integers, strings, structures).</li>
      <li><strong>Dotted / Dashed Arrow (- - &rarr;):</strong> Represents a Boolean control flow signal originating from a decision process and terminating on the border of the process being controlled.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Bridging Functional and Dynamic Models</h5>
    <p>Control flows serve as the critical semantic bridge between the Functional Model (which describes data transformations) and the Dynamic Model (which describes state machines and decision logic).</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Data Flow (Solid Line) vs Control Flow (Dotted Line)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Dimension</th>
        <th>Data Flow (Solid Line &rarr;)</th>
        <th>Control Flow (Dotted Line - - &rarr;)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Line Representation</strong></td>
        <td>Continuous solid line with arrowhead</td>
        <td>Dotted or dashed line with arrowhead</td>
      </tr>
      <tr>
        <td><strong>Content Carried</strong></td>
        <td>Concrete data values (objects, numbers, text)</td>
        <td>Discrete Boolean execution signals (True/False, Enable/Disable)</td>
      </tr>
      <tr>
        <td><strong>Role in Process</strong></td>
        <td>Serves as raw input values consumed in calculation</td>
        <td>Enables, disables, triggers, or halts the process execution</td>
      </tr>
      <tr>
        <td><strong>OMT Model Origin</strong></td>
        <td>Native to the <strong>Functional Model</strong> (DFD)</td>
        <td>Bridges the <strong>Dynamic Model</strong> (events) to DFD processes</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Control Flow (Dotted Line) Controlling a DFD Process (AKTU Que 1.14c)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Decision Process (Top Left) -->
      <g transform="translate(60, 30)">
        <ellipse cx="85" cy="40" rx="80" ry="35" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="85" y="37" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Verify PIN &amp;</text>
        <text x="85" y="52" fill="#fcd34d" font-size="9" text-anchor="middle">Check Card Limits</text>
      </g>

      <!-- Controlled Computation Process (Center Bottom) -->
      <g transform="translate(330, 130)">
        <ellipse cx="90" cy="50" rx="85" ry="45" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="47" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Dispense Cash</text>
        <text x="90" y="64" fill="#38bdf8" font-size="9" text-anchor="middle">&amp; Deduct Balance</text>
      </g>

      <!-- DOTTED CONTROL FLOW LINE -->
      <path d="M 225 70 C 310 70, 420 80, 420 130" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#u1-cf-arr-yellow)"/>
      <rect x="255" y="48" width="150" height="22" rx="4" fill="#0f172a" stroke="#b45309" stroke-width="1"/>
      <text x="330" y="63" fill="#fcd34d" font-size="8" font-weight="bold" text-anchor="middle">CONTROL FLOW: isAuthorized?</text>

      <!-- SOLID DATA FLOW INPUT -->
      <g transform="translate(60, 155)">
        <rect width="130" height="40" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="65" y="24" fill="#93c5fd" font-size="9" text-anchor="middle">Requested Cash Amount</text>
      </g>
      <path d="M 190 175 L 330 175" stroke="#38bdf8" stroke-width="2" marker-end="url(#u1-cf-arr-blue)"/>
      <text x="250" y="168" fill="#38bdf8" font-size="8" font-weight="bold">data: $500.00</text>

      <!-- SOLID DATA FLOW OUTPUT -->
      <path d="M 500 175 L 640 175" stroke="#34d399" stroke-width="2" marker-end="url(#u1-cf-arr-green)"/>
      <text x="560" y="168" fill="#34d399" font-size="8" font-weight="bold">data: Cash Dispensed</text>
      <g transform="translate(640, 155)">
        <rect width="130" height="40" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
        <text x="65" y="24" fill="#6ee7b7" font-size="9" text-anchor="middle">Cash Tray Output</text>
      </g>

      <!-- Legend -->
      <g transform="translate(560, 30)">
        <rect width="220" height="65" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1"/>
        <line x1="15" y1="20" x2="60" y2="20" stroke="#38bdf8" stroke-width="2"/>
        <text x="70" y="24" fill="#e2e8f0" font-size="8">Solid Line = Data Flow (Values)</text>
        <line x1="15" y1="45" x2="60" y2="45" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,3"/>
        <text x="70" y="49" fill="#fcd34d" font-size="8">Dotted Line = Control Flow (Boolean)</text>
      </g>

      <defs>
        <marker id="u1-cf-arr-yellow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
        <marker id="u1-cf-arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="u1-cf-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2015-16):</strong> <em>"Write short note on: Control flow."</em> [Part of 15-Mark Composite Question - Que 1.14c]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Explain that DFDs show all possible computation paths, but not which paths execute or their sequence. Define control flow as a Boolean value affecting whether a process runs. Emphasize that it is <strong>not an input value</strong> to the calculation. State clearly that it is drawn as a <strong>dotted line</strong> from the process producing the Boolean to the process being controlled.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Control Flow:</strong> A Boolean execution signal enabling or disabling a process in a DFD.</li>
    <li><strong>Not an Input:</strong> It triggers or inhibits execution, but is not consumed as an arithmetic input.</li>
    <li><strong>Notation:</strong> Always drawn as a <strong>dotted / dashed arrow</strong> (- - &rarr;).</li>
    <li><strong>Contrast:</strong> Solid arrows carry data values; dotted arrows carry Boolean execution control.</li>
  </ul>
</div>
"""
        }
    ]
