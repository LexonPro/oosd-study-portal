# generate_unit3_part2.py: Part 2 - Structured Analysis & Design (SA/SD) & Non-OO Implementation (Sections 12 to 19)

def get_unit3_part2_sections():
    return [
        {
            "id": "u3-sec-12",
            "number": "12",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Structured Analysis & Structured Design (SA/SD)",
            "subtitle": "Process-Driven Modeling, DFDs, Data Dictionaries, Structure Charts & OMT Comparison",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Procedural Paradigm</div>
    <h3>Meaning & Purpose of SA/SD</h3>
    <p><strong>Structured Analysis and Structured Design (SA/SD)</strong> is a classical, diagrammatic software engineering methodology developed in the late 1970s (by DeMarco, Yourdon, and Constantine). It decomposes a complex software system from a <strong>functional/process-oriented</strong> perspective rather than an object-oriented one.</p>
    <p>SA/SD treats software as a collection of subroutines transforming input data streams into output data streams. The core philosophy centers on <strong>functional decomposition</strong>: breaking large processes down into smaller, manageable, hierarchical subprocesses.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Factory Assembly Line vs Smart City</div>
  <p><strong>SA/SD is like an automobile assembly line:</strong> Raw steel enters at one end, machine A stamps the frame, conveyor belt transfers it to machine B (welding), then to machine C (painting), and finally out rolls a car. The focus is entirely on the <em>stations (functions)</em> and the <em>conveyor belts (data flows)</em>.</p>
  <p>In contrast, <strong>OMT (Object-Oriented) is like a smart city:</strong> Autonomous entities (citizens, cars, traffic lights, buildings) have identities, own their private state, and communicate by exchanging messages. When you expand a city, you add new buildings or citizens; when you modify an assembly line, you risk halting the entire conveyor flow.</p>
</div>

<div class="subtopics-container">
  <h4>Core Artifacts & Techniques of SA/SD</h4>

  <div class="detail-block">
    <h5>1. Data Flow Diagram (DFD)</h5>
    <p>A graphical modeling tool showing how data moves through a system of processes without specifying control logic, sequence, or loops. Core components include:</p>
    <ul>
      <li><strong>External Entities (Sources/Sinks):</strong> Rectangles representing external actors sending or receiving data (e.g., <code>Customer</code>, <code>Bank Server</code>).</li>
      <li><strong>Processes (Bubbles/Circles):</strong> Transformations of incoming data into outgoing data (e.g., <code>Validate Card</code>, <code>Compute Interest</code>).</li>
      <li><strong>Data Stores (Parallel Lines/Open Rectangles):</strong> Data repositories at rest (e.g., <code>Accounts Database</code>).</li>
      <li><strong>Data Flows (Directed Arrows):</strong> Named data packets passing between entities, processes, and stores.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Data Dictionary</h5>
    <p>A structured, centralized repository containing precise definitions of all data elements, data structures, control flags, and data stores appearing in the DFDs. It uses algebraic notations such as <code>+</code> (sequence/and), <code>[ | ]</code> (selection/or), and <code>{ }*</code> (iteration/repetition).</p>
  </div>

  <div class="detail-block">
    <h5>3. Structure Chart</h5>
    <p>A hierarchical tree diagram showing how a program is partitioned into procedural modules, their calling hierarchy, and the exact parameters exchanged:</p>
    <ul>
      <li><strong>Module Box:</strong> Represents a function or procedure.</li>
      <li><strong>Call Vector:</strong> Directed arrow indicating caller invokes callee.</li>
      <li><strong>Data Couple:</strong> Arrow with an open circle (○&rarr;) carrying data values.</li>
      <li><strong>Control Couple:</strong> Arrow with a filled circle (•&rarr;) carrying status flags (e.g., <code>EOF_FLAG</code>, <code>VALID_STATUS</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>4. Transformation of DFD to Structure Chart</h5>
    <p>Converting a network-oriented DFD into a hierarchical Structure Chart is performed via two primary strategies:</p>
    <ul>
      <li><strong>Transform Analysis:</strong> Used when data passes through an <em>input flow (afferent branch)</em>, gets transformed by a <em>central transform</em>, and leaves via an <em>output flow (efferent branch)</em>. The central transform becomes the root controller module.</li>
      <li><strong>Transaction Analysis:</strong> Used when an incoming transaction item determines which of several mutually exclusive operational paths is executed (e.g., ATM menu selection triggering Deposit, Withdrawal, or Balance Inquiry).</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Deep Comparison: OMT (Object Modeling Technique) vs SA/SD</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Feature / Dimension</th>
        <th>OMT (Object-Oriented)</th>
        <th>SA/SD (Structured Analysis / Design)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Real-world <strong>objects</strong>, data structures &amp; behaviors</td>
        <td>Functions, subroutines &amp; <strong>data flow</strong></td>
      </tr>
      <tr>
        <td><strong>Dominance Hierarchy</strong></td>
        <td>Object Model &gt; Dynamic Model &gt; Functional Model</td>
        <td>Functional (DFD) &gt; Dynamic (STD) &gt; Data (ERD)</td>
      </tr>
      <tr>
        <td><strong>Component Reusability</strong></td>
        <td><strong>High</strong> (classes, inheritance, polymorphism)</td>
        <td><strong>Low</strong> (functions tightly coupled to data formats)</td>
      </tr>
      <tr>
        <td><strong>Extensibility</strong></td>
        <td>Easy to extend via subclassing without modifying existing code</td>
        <td>Difficult; altering data formats causes ripple effects across functions</td>
      </tr>
      <tr>
        <td><strong>System Representation</strong></td>
        <td>Autonomous collaborating objects with hidden state</td>
        <td>Hierarchical tree of module function calls</td>
      </tr>
      <tr>
        <td><strong>Real-World Fit</strong></td>
        <td>Naturally maps to business domains &amp; UI components</td>
        <td>Good for pure algorithmic or batch calculation pipelines</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C (Procedural SA/SD Implementation)</span>
    <span class="code-desc">Structure Chart module hierarchy with data couples and control flags</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">/* SA/SD Paradigm: System organized as a hierarchy of functions */</span>
<span class="c-comment">/* Root Boss Module invokes worker modules passing data and control couples */</span>

<span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdbool.h&gt;</span>

<span class="c-comment">/* --- Data Structures (Shared records) --- */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">int</span> orderId;
    <span class="c-type">double</span> amount;
    <span class="c-type">char</span> customerStatus; <span class="c-comment">/* 'R' = Regular, 'P' = Premium */</span>
} <span class="c-type">OrderData</span>;

<span class="c-comment">/* --- Afferent Module: Read &amp; Validate (Data Couple In, Control Flag Out) --- */</span>
<span class="c-type">bool</span> validateOrder(<span class="c-type">const</span> <span class="c-type">OrderData</span>* order, <span class="c-type">char</span>* errorMsg) {
    <span class="c-keyword">if</span> (order-&gt;amount &lt;= 0.0) {
        sprintf(errorMsg, <span class="c-string">"Invalid transaction amount"</span>);
        <span class="c-keyword">return false</span>; <span class="c-comment">/* Control Couple: failure flag */</span>
    }
    <span class="c-keyword">return true</span>;      <span class="c-comment">/* Control Couple: success flag */</span>
}

<span class="c-comment">/* --- Central Transform Module: Compute Discount --- */</span>
<span class="c-type">double</span> calculateDiscount(<span class="c-type">const</span> <span class="c-type">OrderData</span>* order) {
    <span class="c-keyword">if</span> (order-&gt;customerStatus == <span class="c-string">'P'</span>) {
        <span class="c-keyword">return</span> order-&gt;amount * 0.15; <span class="c-comment">/* 15% discount */</span>
    }
    <span class="c-keyword">return</span> order-&gt;amount * 0.05;     <span class="c-comment">/* 5% discount */</span>
}

<span class="c-comment">/* --- Efferent Module: Produce Output Invoice --- */</span>
<span class="c-type">void</span> generateInvoice(<span class="c-type">int</span> id, <span class="c-type">double</span> total, <span class="c-type">double</span> discount) {
    printf(<span class="c-string">"=== INVOICE #%d ===\\n"</span>, id);
    printf(<span class="c-string">"Net Payable: $%.2f (Saved: $%.2f)\\n"</span>, total - discount, discount);
}

<span class="c-comment">/* --- Root Boss Controller Module (Structure Chart Root) --- */</span>
<span class="c-type">void</span> processOrderTransaction(<span class="c-type">OrderData</span> order) {
    <span class="c-type">char</span> err[64];
    <span class="c-comment">/* Step 1: Invoke validation subroutine */</span>
    <span class="c-type">bool</span> isValid = validateOrder(&amp;order, err);
    <span class="c-keyword">if</span> (!isValid) {
        printf(<span class="c-string">"Transaction Aborted: %s\\n"</span>, err);
        <span class="c-keyword">return</span>;
    }

    <span class="c-comment">/* Step 2: Invoke transform subroutine */</span>
    <span class="c-type">double</span> discount = calculateDiscount(&amp;order);

    <span class="c-comment">/* Step 3: Invoke output subroutine */</span>
    generateInvoice(order.orderId, order.amount, discount);
}

<span class="c-type">int</span> main() {
    <span class="c-type">OrderData</span> testOrder = {101, 250.0, <span class="c-string">'P'</span>};
    processOrderTransaction(testOrder);
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: DFD to Structure Chart Mapping</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 880 340" width="100%" height="320" xmlns="http://www.w3.org/2000/svg">
      <!-- Dark Executive Canvas -->
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Subsystem 1: DFD Flow (Left) -->
      <rect x="25" y="20" width="380" height="300" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
      <text x="215" y="48" fill="#38bdf8" font-size="14" font-family="system-ui, sans-serif" font-weight="bold" text-anchor="middle">Data Flow Diagram (Network Flow)</text>
      
      <!-- External Entity -->
      <rect x="45" y="80" width="90" height="45" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="90" y="107" fill="#ffffff" font-size="12" font-family="system-ui, sans-serif" font-weight="bold" text-anchor="middle">Customer</text>
      
      <!-- Arrow to Process 1 -->
      <path d="M 135 102 L 180 102" stroke="#38bdf8" stroke-width="2" marker-end="url(#cyan-arrow)"/>
      <text x="157" y="94" fill="#94a3b8" font-size="10" text-anchor="middle">Order</text>
      
      <!-- Bubble Process 1 -->
      <circle cx="220" cy="102" r="35" fill="#0f766e" stroke="#2dd4bf" stroke-width="2"/>
      <text x="220" y="100" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1.0 Validate</text>
      <text x="220" y="114" fill="#ccfbf1" font-size="9" text-anchor="middle">Order</text>
      
      <!-- Arrow to Process 2 -->
      <path d="M 255 102 L 295 102" stroke="#38bdf8" stroke-width="2" marker-end="url(#cyan-arrow)"/>
      
      <!-- Bubble Process 2 -->
      <circle cx="335" cy="102" r="35" fill="#0f766e" stroke="#2dd4bf" stroke-width="2"/>
      <text x="335" y="100" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">2.0 Compute</text>
      <text x="335" y="114" fill="#ccfbf1" font-size="9" text-anchor="middle">Discount</text>

      <!-- Data Store -->
      <line x1="180" y1="230" x2="280" y2="230" stroke="#f59e0b" stroke-width="2.5"/>
      <line x1="180" y1="270" x2="280" y2="270" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="230" y="255" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">D1: Rates Store</text>

      <path d="M 230 230 L 335 140" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4" marker-end="url(#amber-arrow)"/>

      <!-- Transition Transform Arrow -->
      <path d="M 415 170 L 455 170" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6" marker-end="url(#blue-arrow)"/>
      <text x="435" y="158" fill="#60a5fa" font-size="11" font-weight="bold" text-anchor="middle">Map</text>

      <!-- Subsystem 2: Structure Chart (Right) -->
      <rect x="470" y="20" width="385" height="300" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
      <text x="662" y="48" fill="#a855f7" font-size="14" font-family="system-ui, sans-serif" font-weight="bold" text-anchor="middle">Structure Chart (Module Hierarchy)</text>

      <!-- Root Boss Module -->
      <rect x="585" y="70" width="155" height="45" rx="5" fill="#6d28d9" stroke="#c084fc" stroke-width="2"/>
      <text x="662" y="97" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Process Order (Boss)</text>

      <!-- Calling vectors -->
      <path d="M 620 115 L 540 180" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#gray-arrow)"/>
      <path d="M 662 115 L 662 180" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#gray-arrow)"/>
      <path d="M 705 115 L 780 180" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#gray-arrow)"/>

      <!-- Subordinate Modules -->
      <rect x="490" y="185" width="105" height="42" rx="4" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <text x="542" y="210" fill="#e2e8f0" font-size="11" text-anchor="middle">Validate</text>

      <rect x="610" y="185" width="105" height="42" rx="4" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <text x="662" y="210" fill="#e2e8f0" font-size="11" text-anchor="middle">Calculate</text>

      <rect x="730" y="185" width="105" height="42" rx="4" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      <text x="782" y="210" fill="#e2e8f0" font-size="11" text-anchor="middle">Invoice</text>

      <!-- Data Couple Indicator -->
      <circle cx="560" cy="145" r="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <path d="M 560 141 L 550 149" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="532" y="142" fill="#38bdf8" font-size="9">data</text>

      <!-- Control Couple Indicator -->
      <circle cx="590" cy="155" r="4" fill="#ef4444" stroke="#ef4444" stroke-width="2"/>
      <path d="M 590 151 L 600 143" stroke="#ef4444" stroke-width="1.5"/>
      <text x="605" y="160" fill="#f87171" font-size="9">flag</text>

      <!-- Markers -->
      <defs>
        <marker id="cyan-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="blue-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
        <marker id="amber-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
        <marker id="gray-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#94a3b8"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15, 2015-16):</strong> <em>"Compare the OMT methodology with SA/SD methodology with a suitable example."</em> [10 Marks]</p>
  <p><strong>PYQ (AKTU 2012-13, 2013-14):</strong> <em>"Describe Structured Analysis and Structured Design approach with an example."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Strategy:</strong> Draw both the DFD and Structure Chart side-by-side. Highlight that SA/SD organizes around <em>functions</em> (functional decomposition) whereas OMT organizes around <em>real-world objects</em>. Mention the 2 mapping strategies: Transform Analysis and Transaction Analysis.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>SA/SD Core:</strong> Function/Process-centric; system = hierarchy of subroutines.</li>
    <li><strong>Artifacts:</strong> DFD (flow), Data Dictionary (data definitions), Structure Chart (module call tree).</li>
    <li><strong>Transform vs Transaction:</strong> Transform = linear input-transform-output; Transaction = menu-driven branch dispatcher.</li>
    <li><strong>OMT vs SA/SD:</strong> OMT centers on data/objects (high reuse); SA/SD centers on functions (low reuse).</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-13",
            "number": "13",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Jackson Structured Development (JSD)",
            "subtitle": "Principles, Sequential Entity Life Histories, System Specification Diagram (SSD) & OMT Comparison",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Sequential Process Modeling</div>
    <h3>Meaning & Scope of JSD</h3>
    <p><strong>Jackson Structured Development (JSD)</strong>, introduced by Michael A. Jackson in 1983, is a linear and sequential software development methodology. Unlike SA/SD which focuses on functions, and unlike OMT which focuses on static object relationships, JSD describes the real world as a set of <strong>communicating sequential processes</strong> whose events unfold over time.</p>
    <p>JSD models the <em>complete life history</em> of real-world entities (from creation to termination) as a time-ordered sequence of actions, ensuring that the software process mirrors the time constraints of the real world.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Musical Symphony Score</div>
  <p>Think of an orchestra playing a symphony. Each musician (Violinist, Cellist, Flutist) has a <strong>sheet of music (Entity Life History)</strong> that dictates their actions in strict chronological order: play note A &rarr; wait 2 beats (selection) &rarr; repeat chorus 4 times (iteration). The conductor coordinates these independent, concurrent players via tempo signals (data streams). <strong>That is JSD:</strong> concurrent entities executing structured sequential actions over time.</p>
</div>

<div class="subtopics-container">
  <h4>The Three Major Phases of JSD</h4>

  <div class="detail-block">
    <h5>1. Modeling Phase</h5>
    <p>In this initial phase, the analyst examines the problem environment to identify:</p>
    <ul>
      <li><strong>Entities:</strong> Objects in the real world that perform or suffer actions (e.g., <code>Customer</code>, <code>Order</code>, <code>Elevator</code>).</li>
      <li><strong>Actions:</strong> Real-world atomic events taking place at a specific point in time (e.g., <code>OpenAccount</code>, <code>DepositMoney</code>, <code>CloseAccount</code>).</li>
      <li><strong>Entity Structure Diagrams (ESD):</strong> Tree structures modeling the chronological order of actions using three classic Jackson operators:
        <ul>
          <li><strong>Sequence:</strong> Left-to-right chronological execution of steps.</li>
          <li><strong>Selection:</strong> Represented with a small circle <code>(o)</code> in the upper corner, indicating mutually exclusive choices.</li>
          <li><strong>Iteration:</strong> Represented with an asterisk <code>(*)</code>, indicating 0 or more repetitions.</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Specification (Network) Phase</h5>
    <p>Builds the <strong>System Specification Diagram (SSD)</strong>, connecting the model processes to input/output functions. Processes communicate via two primary communication channels:</p>
    <ul>
      <li><strong>Data Streams (FIFO Queues):</strong> Asynchronous buffered channels where process A writes records and process B consumes them without loss.</li>
      <li><strong>State Vector Inspection:</strong> Process B directly reads the internal state variables of Process A at a given moment without consuming data.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Implementation Phase</h5>
    <p>Because real systems historically lacked unlimited concurrent processors, JSD provides <strong>Program Inversion</strong>: transforming concurrent processes into callable subroutines (coroutines/state machines) whose state vectors are swapped into memory upon each invocation.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Comparative Analysis: JSD vs OMT (Object Modeling Technique)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Dimension</th>
        <th>JSD (Jackson Structured Development)</th>
        <th>OMT (Object Modeling Technique)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Foundation</strong></td>
        <td>Time-ordered <strong>sequential processes &amp; events</strong></td>
        <td><strong>Classes, objects</strong>, associations &amp; state diagrams</td>
      </tr>
      <tr>
        <td><strong>Entity Concept</strong></td>
        <td>An entity is an active process with a chronological life history</td>
        <td>An entity is a class encapsulating data attributes &amp; methods</td>
      </tr>
      <tr>
        <td><strong>Concurrency Model</strong></td>
        <td>Built natively on Communicating Sequential Processes (CSP)</td>
        <td>Dynamic model handles events; concurrency added during system design</td>
      </tr>
      <tr>
        <td><strong>Graphical Modeling</strong></td>
        <td>Entity Structure Diagrams (ESD) &amp; System Specification (SSD)</td>
        <td>Class diagrams, Statecharts, and DFDs</td>
      </tr>
      <tr>
        <td><strong>Industry Adoption</strong></td>
        <td>Mainly batch processing, telecom &amp; real-time sequential systems</td>
        <td>Became the direct foundation for UML; universally adopted worldwide</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C Implementation (JSD Entity Life History State Machine)</span>
    <span class="code-desc">Simulating an Account entity life history with state vector inspection</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">/* JSD Concept: Entity Life History implemented via Program Inversion */</span>
<span class="c-comment">/* Entity: BankAccount = Open -&gt; (Deposit | Withdraw)* -&gt; Close */</span>

<span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdbool.h&gt;</span>

<span class="c-keyword">typedef enum</span> {
    STATE_UNOPENED,
    STATE_ACTIVE,
    STATE_CLOSED
} <span class="c-type">AccountLifeState</span>;

<span class="c-comment">/* State Vector of the Account Entity */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">int</span> accountNumber;
    <span class="c-type">double</span> balance;
    <span class="c-type">AccountLifeState</span> currentState; <span class="c-comment">/* JSD State Vector */</span>
} <span class="c-type">AccountStateVector</span>;

<span class="c-comment">/* JSD Action 1: Open Account (Sequence Start) */</span>
<span class="c-type">void</span> actionOpenAccount(<span class="c-type">AccountStateVector</span>* sv, <span class="c-type">int</span> accNo, <span class="c-type">double</span> initialDep) {
    <span class="c-keyword">if</span> (sv-&gt;currentState != STATE_UNOPENED) {
        printf(<span class="c-string">"Error: Account already exists in life history!\\n"</span>);
        <span class="c-keyword">return</span>;
    }
    sv-&gt;accountNumber = accNo;
    sv-&gt;balance = initialDep;
    sv-&gt;currentState = STATE_ACTIVE;
    printf(<span class="c-string">"[JSD Event] Account #%d OPENED with balance $%.2f\\n"</span>, accNo, initialDep);
}

<span class="c-comment">/* JSD Action 2: Iterative Transaction (Deposit/Withdraw Selection) */</span>
<span class="c-type">void</span> actionTransact(<span class="c-type">AccountStateVector</span>* sv, <span class="c-type">double</span> amount, <span class="c-type">bool</span> isDeposit) {
    <span class="c-keyword">if</span> (sv-&gt;currentState != STATE_ACTIVE) {
        printf(<span class="c-string">"Error: Cannot transact on inactive account.\\n"</span>);
        <span class="c-keyword">return</span>;
    }
    <span class="c-keyword">if</span> (isDeposit) {
        sv-&gt;balance += amount;
        printf(<span class="c-string">"[JSD Event] Deposit: +$%.2f | Current: $%.2f\\n"</span>, amount, sv-&gt;balance);
    } <span class="c-keyword">else</span> {
        <span class="c-keyword">if</span> (sv-&gt;balance &gt;= amount) {
            sv-&gt;balance -= amount;
            printf(<span class="c-string">"[JSD Event] Withdraw: -$%.2f | Current: $%.2f\\n"</span>, amount, sv-&gt;balance);
        } <span class="c-keyword">else</span> {
            printf(<span class="c-string">"[JSD Event] Withdraw FAILED: Insufficient balance!\\n"</span>);
        }
    }
}

<span class="c-comment">/* JSD Action 3: Close Account (Sequence End) */</span>
<span class="c-type">void</span> actionCloseAccount(<span class="c-type">AccountStateVector</span>* sv) {
    <span class="c-keyword">if</span> (sv-&gt;currentState != STATE_ACTIVE) {
        printf(<span class="c-string">"Error: Cannot close non-active account.\\n"</span>);
        <span class="c-keyword">return</span>;
    }
    sv-&gt;currentState = STATE_CLOSED;
    printf(<span class="c-string">"[JSD Event] Account #%d CLOSED. Final payout: $%.2f\\n"</span>, sv-&gt;accountNumber, sv-&gt;balance);
}

<span class="c-type">int</span> main() {
    <span class="c-type">AccountStateVector</span> myAcc = {0, 0.0, STATE_UNOPENED};
    
    <span class="c-comment">/* Executing the Entity Life History */</span>
    actionOpenAccount(&amp;myAcc, 501, 1000.0);
    actionTransact(&amp;myAcc, 250.0, <span class="c-keyword">true</span>);   <span class="c-comment">/* Iteration step 1 */</span>
    actionTransact(&amp;myAcc, 400.0, <span class="c-keyword">false</span>);  <span class="c-comment">/* Iteration step 2 */</span>
    actionCloseAccount(&amp;myAcc);            <span class="c-comment">/* Lifecycle End */</span>
    
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: JSD Entity Structure Diagram (ESD)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 320" width="100%" height="300" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Root Node: Account Life History -->
      <rect x="340" y="25" width="160" height="42" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
      <text x="420" y="51" fill="#ffffff" font-size="13" font-family="system-ui, sans-serif" font-weight="bold" text-anchor="middle">ACCOUNT LIFE</text>
      
      <!-- Branches from Root to Sequence Children -->
      <path d="M 370 67 L 150 125" stroke="#64748b" stroke-width="1.8"/>
      <path d="M 420 67 L 420 125" stroke="#64748b" stroke-width="1.8"/>
      <path d="M 470 67 L 690 125" stroke="#64748b" stroke-width="1.8"/>
      
      <!-- Child 1: OPEN (Sequence Step 1) -->
      <rect x="80" y="125" width="140" height="40" rx="4" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
      <text x="150" y="150" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">1. OPEN-ACC</text>

      <!-- Child 2: ACTIVE PERIOD (Iteration *) -->
      <rect x="340" y="125" width="160" height="40" rx="4" fill="#854d0e" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="420" y="150" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. ACTIVE-LIFE (*)</text>
      <circle cx="490" cy="133" r="5" fill="#f59e0b"/>
      <text x="490" y="136" fill="#000000" font-size="9" font-weight="bold" text-anchor="middle">*</text>

      <!-- Child 3: CLOSE (Sequence Step 3) -->
      <rect x="620" y="125" width="140" height="40" rx="4" fill="#991b1b" stroke="#f87171" stroke-width="1.5"/>
      <text x="690" y="150" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. CLOSE-ACC</text>

      <!-- Sub-branches under ACTIVE-LIFE (Selection o) -->
      <path d="M 390 165 L 300 230" stroke="#64748b" stroke-width="1.5"/>
      <path d="M 450 165 L 540 230" stroke="#64748b" stroke-width="1.5"/>

      <!-- Selection Node 1: Deposit (o) -->
      <rect x="230" y="230" width="140" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="300" y="255" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">DEPOSIT (o)</text>
      <circle cx="360" cy="238" r="5" fill="#0284c7"/>
      <text x="360" y="241" fill="#ffffff" font-size="9" text-anchor="middle">o</text>

      <!-- Selection Node 2: Withdraw (o) -->
      <rect x="470" y="230" width="140" height="40" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="540" y="255" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">WITHDRAW (o)</text>
      <circle cx="600" cy="238" r="5" fill="#0284c7"/>
      <text x="600" y="241" fill="#ffffff" font-size="9" text-anchor="middle">o</text>

      <text x="420" y="300" fill="#94a3b8" font-size="11" text-anchor="middle">Notation Legend: [Sequence: Left-to-Right] | [Iteration: (*)] | [Selection: (o)]</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2012-13, 2013-14):</strong> <em>"Write a short note on Jackson Structured Development (JSD). Explain its various phases."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Always list the 3 phases: <strong>Modeling</strong> (Entities, Actions, ESD), <strong>Specification</strong> (SSD, Data Streams, State Vector), and <strong>Implementation</strong> (Program Inversion). Mention Michael Jackson (1983) and draw the ESD tree with sequence, selection <code>(o)</code>, and iteration <code>(*)</code>.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>JSD Core:</strong> Real-world entities modeled as Communicating Sequential Processes over time.</li>
    <li><strong>Tree Operators:</strong> Sequence (ordered left-to-right), Selection <code>(o)</code>, Iteration <code>(*)</code>.</li>
    <li><strong>Communication Channels:</strong> Data Streams (buffered FIFO) &amp; State Vector Inspection (direct memory read).</li>
    <li><strong>Program Inversion:</strong> Converts long-running concurrent processes into single callable subroutines.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-14",
            "number": "14",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Mapping OO Concepts to Non-OO Languages",
            "subtitle": "Bridging Object-Oriented Designs into Procedural C/Pascal Environments",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Language Interoperability</div>
    <h3>Why Map OO Concepts to Non-OO Languages?</h3>
    <p>Although object-oriented languages (C++, Java, Python) provide native syntactic keywords for classes, inheritance, and polymorphism, developers frequently must implement OO designs in <strong>procedural non-OO languages</strong> (such as C, Fortran, Ada, or Pascal).</p>
    <p>This is common in <strong>embedded systems, automotive ECUs, operating system kernels (like the Linux kernel), and legacy mainframes</strong> where C is the only supported, certified, or performant compiler available.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Translating an English Idiom into Ancient Latin</div>
  <p>Ancient Latin has no single word for <em>"Smartwatch"</em> or <em>"Cloud Computing"</em>. Yet, a skilled translator can still express these modern concepts using descriptive Latin phrases (e.g., <em>horologium intelligente</em>). Similarly, while procedural C lacks the <code>class</code> keyword, a developer can faithfully express classes, methods, and polymorphism using C <code>struct</code>s, pointers, and function tables!</p>
</div>

<div class="subtopics-container">
  <h4>The Master Mapping Rosetta Stone</h4>

  <div class="detail-block">
    <h5>1. The 6 Core Mapping Transformations</h5>
    <p>Every modern OO paradigm construct has an exact procedural equivalent:</p>
    <ul>
      <li><strong>Class &rarr; Struct:</strong> A class definition becomes a C <code>struct</code> containing all data attributes.</li>
      <li><strong>Object &rarr; Struct Instance:</strong> An instantiated object becomes a variable or dynamically allocated block on the heap (<code>malloc</code>).</li>
      <li><strong>Method &rarr; Standalone Function:</strong> A method becomes a standard procedural function with an explicit <code>self</code> pointer as its first parameter.</li>
      <li><strong>Inheritance &rarr; Embedded Struct:</strong> Subclassing is realized by placing the superclass struct as the very first member of the subclass struct.</li>
      <li><strong>Polymorphism &rarr; Function Pointer Table (VTable):</strong> Dynamic method dispatch is achieved via an array or struct of function pointers.</li>
      <li><strong>Encapsulation &rarr; Opaque Pointers:</strong> Declaring incomplete struct types in <code>.h</code> and hiding field definitions inside <code>.c</code>.</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Comprehensive Mapping Matrix: OO vs Non-OO (C)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Object-Oriented Construct (C++/Java)</th>
        <th>Procedural Non-OO Construct (ANSI C)</th>
        <th>Implementation Mechanism</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>class Circle { ... };</code></td>
        <td><code>typedef struct Circle { ... } Circle;</code></td>
        <td>Contiguous memory block holding attribute fields</td>
      </tr>
      <tr>
        <td><code>Circle* c = new Circle(5.0);</code></td>
        <td><code>Circle* c = Circle_create(5.0);</code></td>
        <td>Dynamic heap allocation via <code>malloc(sizeof(Circle))</code></td>
      </tr>
      <tr>
        <td><code>c-&gt;getArea();</code></td>
        <td><code>Circle_getArea(c);</code></td>
        <td>Explicitly passing object memory address as first parameter</td>
      </tr>
      <tr>
        <td><code>class Dog : public Animal</code></td>
        <td><code>struct Dog { Animal base; ... };</code></td>
        <td>Base struct placed at offset 0 for memory compatibility</td>
      </tr>
      <tr>
        <td><code>virtual void draw();</code></td>
        <td><code>void (*draw)(void* self);</code></td>
        <td>Function pointer in struct or separate vtable struct</td>
      </tr>
      <tr>
        <td><code>private: int secretKey;</code></td>
        <td>Opaque pointer (incomplete type in header)</td>
        <td>Client code cannot dereference struct fields directly</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C (Complete OO-in-C Implementation)</span>
    <span class="code-desc">Simulating an OO Class, Constructor, and Method in ANSI C</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">/* Mapping an OO Class 'Rectangle' to procedural C */</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdlib.h&gt;</span>

<span class="c-comment">/* 1. Class mapped to C Struct */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">double</span> width;
    <span class="c-type">double</span> height;
} <span class="c-type">Rectangle</span>;

<span class="c-comment">/* 2. Constructor mapped to initialization function */</span>
<span class="c-type">Rectangle</span>* Rectangle_create(<span class="c-type">double</span> w, <span class="c-type">double</span> h) {
    <span class="c-type">Rectangle</span>* rect = (<span class="c-type">Rectangle</span>*)malloc(<span class="c-keyword">sizeof</span>(<span class="c-type">Rectangle</span>));
    <span class="c-keyword">if</span> (rect != NULL) {
        rect-&gt;width = w;
        rect-&gt;height = h;
    }
    <span class="c-keyword">return</span> rect;
}

<span class="c-comment">/* 3. Method mapped to function with explicit 'self' pointer */</span>
<span class="c-type">double</span> Rectangle_getArea(<span class="c-type">const</span> <span class="c-type">Rectangle</span>* self) {
    <span class="c-keyword">return</span> self-&gt;width * self-&gt;height;
}

<span class="c-comment">/* 4. Destructor mapped to cleanup function */</span>
<span class="c-type">void</span> Rectangle_destroy(<span class="c-type">Rectangle</span>* self) {
    <span class="c-keyword">if</span> (self != NULL) {
        free(self);
    }
}

<span class="c-type">int</span> main() {
    <span class="c-comment">/* Instantiate object */</span>
    <span class="c-type">Rectangle</span>* myRect = Rectangle_create(10.0, 5.0);
    
    <span class="c-comment">/* Invoke method */</span>
    printf(<span class="c-string">"Rectangle Area = %.2f\\n"</span>, Rectangle_getArea(myRect));
    
    <span class="c-comment">/* Destroy object */</span>
    Rectangle_destroy(myRect);
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The OO to Non-OO Rosetta Stone</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- OO World Column -->
      <rect x="40" y="25" width="340" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
      <text x="210" y="55" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Object-Oriented World (C++/Java)</text>
      
      <rect x="60" y="75" width="300" height="30" rx="4" fill="#0369a1"/>
      <text x="210" y="95" fill="#ffffff" font-size="11" text-anchor="middle">Class (Attributes + Methods)</text>

      <rect x="60" y="115" width="300" height="30" rx="4" fill="#0369a1"/>
      <text x="210" y="135" fill="#ffffff" font-size="11" text-anchor="middle">Implicit 'this' pointer in methods</text>

      <rect x="60" y="155" width="300" height="30" rx="4" fill="#0369a1"/>
      <text x="210" y="175" fill="#ffffff" font-size="11" text-anchor="middle">Inheritance Hierarchy (class Derived : Base)</text>

      <rect x="60" y="195" width="300" height="30" rx="4" fill="#0369a1"/>
      <text x="210" y="215" fill="#ffffff" font-size="11" text-anchor="middle">Virtual Method Dispatch (Polymorphism)</text>

      <!-- Center Transformation Column -->
      <path d="M 395 90 L 445 90" stroke="#a855f7" stroke-width="2" marker-end="url(#purple-arrow)"/>
      <path d="M 395 130 L 445 130" stroke="#a855f7" stroke-width="2" marker-end="url(#purple-arrow)"/>
      <path d="M 395 170 L 445 170" stroke="#a855f7" stroke-width="2" marker-end="url(#purple-arrow)"/>
      <path d="M 395 210 L 445 210" stroke="#a855f7" stroke-width="2" marker-end="url(#purple-arrow)"/>

      <!-- Procedural World Column -->
      <rect x="460" y="25" width="340" height="230" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
      <text x="630" y="55" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">Procedural Non-OO World (C)</text>

      <rect x="480" y="75" width="300" height="30" rx="4" fill="#065f46"/>
      <text x="630" y="95" fill="#ffffff" font-size="11" text-anchor="middle">typedef struct { ... } DataStruct;</text>

      <rect x="480" y="115" width="300" height="30" rx="4" fill="#065f46"/>
      <text x="630" y="135" fill="#ffffff" font-size="11" text-anchor="middle">Explicit 'self*' as first parameter</text>

      <rect x="480" y="155" width="300" height="30" rx="4" fill="#065f46"/>
      <text x="630" y="175" fill="#ffffff" font-size="11" text-anchor="middle">Embedded Struct at offset 0</text>

      <rect x="480" y="195" width="300" height="30" rx="4" fill="#065f46"/>
      <text x="630" y="215" fill="#ffffff" font-size="11" text-anchor="middle">Struct of Function Pointers (VTable)</text>

      <defs>
        <marker id="purple-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2011-12):</strong> <em>"How do you map object-oriented concepts using non-object-oriented languages? Explain with an example."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Systematically list the 6 transformations: Classes &rarr; Structs, Methods &rarr; Functions with explicit self pointer, Storage allocation &rarr; malloc/stack, Inheritance &rarr; Embedded records, Method resolution &rarr; Function pointers, Encapsulation &rarr; Opaque pointers. Provide a clean C code example.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Classes become C <code>struct</code>s containing contiguous attribute variables.</li>
    <li>Methods become standalone functions receiving an explicit <code>self*</code> pointer.</li>
    <li>Encapsulation is achieved by hiding struct internals behind header opaque pointers.</li>
    <li>Inheritance is modeled via struct embedding; polymorphism via function pointers.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-15",
            "number": "15",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Translating Classes into Data Structures",
            "subtitle": "Struct Representation, Memory Alignment, Padding & Static vs Stack vs Heap Storage Allocation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Memory Engineering</div>
    <h3>Class Representation in Procedural Memory</h3>
    <p>In procedural languages like C, a class is implemented as a <strong>single contiguous block of attributes</strong> known as a <code>struct</code> or record. Each object instance has a distinct state, unique identity, and is allocated physical memory.</p>
    <p>Because an object has identity and can be modified through side effects, references to objects must be implemented as <strong>sharable memory pointers</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Blank Printed ID Badge</div>
  <p>A <strong>Class</strong> is like the blank layout of an employee ID badge printed at a factory (specifying boxes for Photo, Name, and ID Number). An <strong>Object</strong> is a physical plastic card filled in with an employee's details. The card can be stored in three ways: permanently pinned to a wall bulletin board (<strong>Static</strong>), temporarily clipped to your shirt for a 10-minute visitor meeting (<strong>Stack</strong>), or kept in an expandable locker that you rent on demand (<strong>Heap</strong>).</p>
</div>

<div class="subtopics-container">
  <h4>Storage Allocation Strategies for Objects</h4>

  <div class="detail-block">
    <h5>1. Static Allocation</h5>
    <p>Objects are allocated at compile-time in the global data segment. Their memory remains allocated throughout the entire lifetime of the program.</p>
    <ul>
      <li><strong>Pros:</strong> Zero runtime allocation overhead; extremely fast access; immune to stack overflows.</li>
      <li><strong>Cons:</strong> Number of objects must be fixed at compile time; cannot support dynamic scaling.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Stack Allocation (Automatic Variables)</h5>
    <p>Objects are declared as local variables inside functions. They are allocated automatically when the function frame is pushed onto the stack and destroyed upon return.</p>
    <ul>
      <li><strong>Pros:</strong> Ultra-fast pointer decrement allocation; automatic memory deallocation without memory leaks.</li>
      <li><strong>Cons:</strong> Lifetime is strictly limited to the enclosing function scope; cannot return stack pointers.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Dynamic Heap Allocation</h5>
    <p>Objects are allocated on demand at runtime using heap managers like <code>malloc()</code> or <code>calloc()</code>. This is necessary when the number of objects cannot be known at compile time.</p>
    <ul>
      <li><strong>Pros:</strong> Arbitrary lifetime across function calls; supports complex dynamic networks of objects.</li>
      <li><strong>Cons:</strong> Slower allocation; prone to fragmentation and memory leaks if <code>free()</code> is omitted.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>4. Memory Alignment &amp; Padding</h5>
    <p>CPUs read memory in word chunks (4 or 8 bytes). Compilers automatically insert invisible padding bytes between struct members to align fields to word boundaries. Developers must order struct members from largest to smallest to minimize padding waste.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C (Memory Allocation &amp; Alignment Demonstration)</span>
    <span class="code-desc">Comparing Static, Stack, and Heap Object Allocations</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdlib.h&gt;</span>

<span class="c-comment">/* Class represented as a C struct */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">int</span> id;           <span class="c-comment">/* 4 bytes */</span>
    <span class="c-type">char</span> roleCode;    <span class="c-comment">/* 1 byte + 3 padding bytes */</span>
    <span class="c-type">double</span> salary;    <span class="c-comment">/* 8 bytes (Aligned on 8-byte boundary) */</span>
} <span class="c-type">Employee</span>;

<span class="c-comment">/* 1. Static Allocation (Global memory segment) */</span>
<span class="c-type">static Employee</span> globalAdmin = {1, <span class="c-string">'A'</span>, 95000.0};

<span class="c-type">void</span> demonstrateStackAndHeap() {
    <span class="c-comment">/* 2. Stack Allocation (Local activation record) */</span>
    <span class="c-type">Employee</span> stackEmp = {10, <span class="c-string">'E'</span>, 52000.0};
    printf(<span class="c-string">"Stack Object Address: %p (Size: %zu bytes)\\n"</span>, 
           (<span class="c-type">void</span>*)&amp;stackEmp, <span class="c-keyword">sizeof</span>(stackEmp));

    <span class="c-comment">/* 3. Heap Allocation (Dynamic runtime request) */</span>
    <span class="c-type">Employee</span>* heapEmp = (<span class="c-type">Employee</span>*)malloc(<span class="c-keyword">sizeof</span>(<span class="c-type">Employee</span>));
    <span class="c-keyword">if</span> (heapEmp != NULL) {
        heapEmp-&gt;id = 20;
        heapEmp-&gt;roleCode = <span class="c-string">'M'</span>;
        heapEmp-&gt;salary = 82000.0;
        printf(<span class="c-string">"Heap Object Address:  %p\\n"</span>, (<span class="c-type">void</span>*)heapEmp);
        
        <span class="c-comment">/* Crucial: Manual deallocation */</span>
        free(heapEmp);
    }
}

<span class="c-type">int</span> main() {
    printf(<span class="c-string">"Static Object Address: %p\\n"</span>, (<span class="c-type">void</span>*)&amp;globalAdmin);
    demonstrateStackAndHeap();
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Memory Architecture: Process Memory Segments for Objects</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Memory Segments Box -->
      <rect x="50" y="30" width="220" height="220" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
      <text x="160" y="55" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Process Address Space</text>

      <!-- Stack Segment (Top down) -->
      <rect x="65" y="70" width="190" height="40" rx="4" fill="#1d4ed8" stroke="#60a5fa" stroke-width="1.5"/>
      <text x="160" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">STACK (Local Objects)</text>

      <!-- Arrow down -->
      <path d="M 160 115 L 160 135" stroke="#94a3b8" stroke-width="2" marker-end="url(#down-arrow)"/>

      <!-- Free memory gap -->
      <text x="160" y="148" fill="#64748b" font-size="10" text-anchor="middle">↑ ↓ Dynamic Growth</text>

      <!-- Heap Segment (Bottom up) -->
      <rect x="65" y="160" width="190" height="40" rx="4" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
      <text x="160" y="185" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">HEAP (malloc Objects)</text>

      <!-- Data Segment (Static) -->
      <rect x="65" y="205" width="190" height="35" rx="4" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="160" y="228" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">DATA / BSS (Static Objects)</text>

      <!-- Struct Memory Layout Breakdown (Right) -->
      <rect x="310" y="30" width="490" height="220" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
      <text x="555" y="55" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Contiguous Struct Memory Layout (with Word Padding)</text>

      <!-- Byte Offset Ruler -->
      <rect x="330" y="80" width="110" height="50" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="385" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">id (int)</text>
      <text x="385" y="120" fill="#bae6fd" font-size="9" text-anchor="middle">4 Bytes [Offset 0-3]</text>

      <rect x="440" y="80" width="40" height="50" fill="#0f766e" stroke="#2dd4bf" stroke-width="1.5"/>
      <text x="460" y="105" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">role</text>
      <text x="460" y="120" fill="#ccfbf1" font-size="8" text-anchor="middle">1 Byte</text>

      <!-- Padding Block -->
      <rect x="480" y="80" width="70" height="50" fill="#475569" stroke="#94a3b8" stroke-dasharray="4" stroke-width="1.5"/>
      <text x="515" y="105" fill="#cbd5e1" font-size="10" text-anchor="middle">PAD</text>
      <text x="515" y="120" fill="#cbd5e1" font-size="8" text-anchor="middle">3 Bytes</text>

      <rect x="550" y="80" width="230" height="50" fill="#7e22ce" stroke="#c084fc" stroke-width="1.5"/>
      <text x="665" y="105" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">salary (double)</text>
      <text x="665" y="120" fill="#f3e8ff" font-size="9" text-anchor="middle">8 Bytes [Aligned at Offset 8-15]</text>

      <text x="555" y="165" fill="#e2e8f0" font-size="11" text-anchor="middle">Total Struct Size = 16 Bytes (Not 13 Bytes due to 8-byte CPU Alignment)</text>
      
      <rect x="340" y="185" width="430" height="50" rx="4" fill="#0f172a" stroke="#334155"/>
      <text x="555" y="205" fill="#38bdf8" font-size="10" text-anchor="middle">• Pointers to struct enable object identity &amp; side effects</text>
      <text x="555" y="222" fill="#38bdf8" font-size="10" text-anchor="middle">• Struct pointer size on 64-bit architecture = 8 Bytes</text>

      <defs>
        <marker id="down-arrow" viewBox="0 0 10 10" refX="5" refY="6" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 1 0 L 5 8 L 9 0 z" fill="#94a3b8"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2014-15):</strong> <em>"Explain how storage is allocated for objects in non-object-oriented languages."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Clearly explain all three allocation schemes: <strong>Static</strong> (global segment, fixed count), <strong>Stack</strong> (automatic scope, temporary variables), and <strong>Heap</strong> (dynamic <code>malloc()</code> for objects whose count is determined at runtime). Mention why object references must be pointers (for identity and side effects).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Classes translate directly into contiguous C <code>struct</code> memory records.</li>
    <li>Object variables are pointers to allow identity, sharing, and state mutations.</li>
    <li>3 Storage types: Static (forever), Stack (function lifetime), Heap (dynamic via <code>malloc</code>).</li>
    <li>Compilers add alignment padding so multi-byte values align with CPU memory boundaries.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-16",
            "number": "16",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Passing Arguments to Methods",
            "subtitle": "Explicit Object Reference ('this'/'self'), Formal vs Actual Parameters & Pass-by-Value vs Reference",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Calling Conventions</div>
    <h3>Method Invocation Mechanics</h3>
    <p>In native object-oriented languages, calling an operation on an object uses member access syntax: <code>obj.calculate(arg);</code>. Here, the target object <code>obj</code> is passed <strong>implicitly</strong> into the method as the hidden <code>this</code> (C++/Java) or <code>self</code> (Python) pointer.</p>
    <p>In a non-object-oriented language, there is no implicit context. The target object <strong>must be made completely explicit</strong> as the very first argument of the function: <code>calculate(&amp;obj, arg);</code>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Car Mechanic &amp; The Key</div>
  <p>If you tell a mechanic <em>"Change the oil"</em>, the mechanic needs to know <strong>which car</strong> to service! In OOP, you sit inside your car and push the dashboard button (the car is implicit). In procedural programming, you must explicitly hand the mechanic the physical keys and parking ticket to your car (explicit object pointer). If you hand them a photocopy of the car (pass-by-value), they cannot change the real car's oil!</p>
</div>

<div class="subtopics-container">
  <h4>Parameter Passing Concepts &amp; Types</h4>

  <div class="detail-block">
    <h5>1. Formal vs Actual Parameters (AKTU Question 3.20 Definition)</h5>
    <ul>
      <li><strong>Formal Parameters:</strong> The variable names and their data types as they appear in the declaration or prototype of the function/method (e.g., <code>void deposit(Account* self, double amt)</code>).</li>
      <li><strong>Actual Parameters (Arguments):</strong> The concrete variables, expressions, or memory addresses passed into the function by the caller at the execution point (e.g., <code>deposit(&amp;myAccount, 500.0)</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Pass-by-Value vs Pass-by-Reference (Pointers)</h5>
    <ul>
      <li><strong>Pass-by-Value:</strong> The compiler makes a full bitwise copy of the entire struct onto the callee's stack frame. Modifications inside the method operate strictly on the copy and are lost when the function returns. Inefficient for large objects.</li>
      <li><strong>Pass-by-Reference (Pointers):</strong> The caller passes the 8-byte memory address of the object. Allows the method to update the object's actual state (side effects) and incurs zero copying overhead. Use <code>const ClassName* self</code> when the method only inspects (reads) state.</li>
    </ul>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C (Explicit Self Pointer Implementation)</span>
    <span class="code-desc">Demonstrating mutating vs read-only method invocations in C</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdbool.h&gt;</span>

<span class="c-keyword">typedef struct</span> {
    <span class="c-type">int</span> accNumber;
    <span class="c-type">double</span> balance;
} <span class="c-type">BankAccount</span>;

<span class="c-comment">/* Mutating Method: Receives mutable pointer (BankAccount* self) */</span>
<span class="c-type">bool</span> BankAccount_deposit(<span class="c-type">BankAccount</span>* self, <span class="c-type">double</span> amount) {
    <span class="c-comment">/* Formal parameters: 'self' (target object) and 'amount' */</span>
    <span class="c-keyword">if</span> (amount &lt;= 0.0) {
        <span class="c-keyword">return false</span>;
    }
    self-&gt;balance += amount; <span class="c-comment">/* Modifies original object state directly */</span>
    <span class="c-keyword">return true</span>;
}

<span class="c-comment">/* Read-Only Inspector Method: Receives const pointer to prevent mutation */</span>
<span class="c-type">void</span> BankAccount_printDetails(<span class="c-type">const</span> <span class="c-type">BankAccount</span>* self) {
    printf(<span class="c-string">"Account #%d | Current Balance: $%.2f\\n"</span>, 
           self-&gt;accNumber, self-&gt;balance);
}

<span class="c-type">int</span> main() {
    <span class="c-comment">/* Local object on stack */</span>
    <span class="c-type">BankAccount</span> acc = {1001, 450.0};
    
    <span class="c-comment">/* Calling mutating method: pass address (&amp;acc) as actual argument */</span>
    BankAccount_deposit(&amp;acc, 150.0);
    
    <span class="c-comment">/* Calling inspector method */</span>
    BankAccount_printDetails(&amp;acc);
    
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Call Stack Diagram: Explicit 'this' Pointer Dereferencing</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 260" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Caller Stack Frame (main) -->
      <rect x="50" y="30" width="220" height="200" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="160" y="58" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Caller Frame: main()</text>
      
      <rect x="70" y="75" width="180" height="60" rx="4" fill="#0369a1"/>
      <text x="160" y="100" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Object 'acc'</text>
      <text x="160" y="118" fill="#e0f2fe" font-size="10" text-anchor="middle">accNumber = 1001</text>
      <text x="160" y="130" fill="#e0f2fe" font-size="10" text-anchor="middle">balance = $450.00</text>
      <text x="75" y="150" fill="#94a3b8" font-size="9">Address: 0x7FFF00</text>

      <!-- Callee Stack Frame -->
      <rect x="570" y="30" width="220" height="200" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
      <text x="680" y="58" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Callee Frame: deposit()</text>

      <rect x="590" y="75" width="180" height="40" rx="4" fill="#065f46"/>
      <text x="680" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">self pointer (8B)</text>
      <text x="680" y="108" fill="#a7f3d0" font-size="9" text-anchor="middle">Value: 0x7FFF00</text>

      <rect x="590" y="125" width="180" height="35" rx="4" fill="#065f46"/>
      <text x="680" y="147" fill="#ffffff" font-size="11" text-anchor="middle">amount = $150.00</text>

      <!-- Pointer Arrow Linking Callee to Caller Object -->
      <path d="M 590 95 C 430 40, 380 40, 250 95" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#amber-point-arrow)"/>
      <text x="420" y="50" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">self-&gt;balance updates 0x7FFF00 directly</text>

      <defs>
        <marker id="amber-point-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13):</strong> <em>"Describe passing arguments to methods with an example. Differentiate formal and actual parameters."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> State that in OO languages the object reference is implicit (<code>this</code>), whereas in non-OO languages it must be passed explicitly as the first argument. Define formal vs actual parameters clearly and explain why passing by pointer is mandatory for mutating state.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>OO languages pass <code>this</code> implicitly; procedural C must pass <code>self*</code> explicitly.</li>
    <li><strong>Formal params:</strong> Variable definitions in function header.</li>
    <li><strong>Actual params:</strong> Concrete values/addresses supplied at call-site.</li>
    <li>Pass-by-pointer avoids expensive struct copies and allows direct state updates.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-17",
            "number": "17",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Implementing Inheritance in Non-OO Languages",
            "subtitle": "Embedded Structs at Offset 0, Hierarchy Flattening & Simulating Polymorphism with VTables",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Inheritance Engineering</div>
    <h3>Representing Inheritance Hierarchies Without Classes</h3>
    <p>Inheritance enables derived classes to share attributes and operations defined in superclasses. Because non-object-oriented languages lack an <code>extends</code> or <code>: public</code> inheritance keyword, developers must physically construct hierarchical memory structures.</p>
    <p>Rumbaugh's OMT methodology and classical compiler engineering outline three primary approaches to implement inheritance in non-OO environments:</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Russian Matryoshka Nesting Doll</div>
  <p>Imagine a Russian nesting doll. Inside the larger <em>"Manager"</em> doll is an identical <em>"Employee"</em> doll, and inside that is a <em>"Person"</em> doll. If you ask for the Person's name, you simply look at the core doll nested inside. <strong>Embedded struct inheritance</strong> works the exact same way: a <code>Manager</code> struct embeds an <code>Employee</code> struct as its very first internal member!</p>
</div>

<div class="subtopics-container">
  <h4>The Three Classical Inheritance Implementations</h4>

  <div class="detail-block">
    <h5>1. Embedded Records (Embedded Structs at Offset 0) &mdash; Best Practice</h5>
    <p>The base class struct is declared as the <strong>very first field</strong> of the derived class struct. According to the ANSI C standard, the memory address of a struct is guaranteed to be identical to the address of its first member:</p>
    <pre class="inline-code"><code>&amp;derived == (Base*)&amp;derived</code></pre>
    <p>This allows safe, zero-cost upcasting: any pointer to a derived struct can be cast directly to a pointer to the base struct!</p>
  </div>

  <div class="detail-block">
    <h5>2. Flattened Class Hierarchy</h5>
    <p>All attributes from the entire superclass hierarchy are manually duplicated into every leaf struct. While conceptually simple, it violates the DRY (Don't Repeat Yourself) principle, makes updates to base attributes hazardous, and prevents polymorphic base-pointer collections.</p>
  </div>

  <div class="detail-block">
    <h5>3. Separate Objects with Explicit Pointers</h5>
    <p>The derived struct holds a pointer to a separately allocated base class struct on the heap. While flexible and capable of simulating multiple inheritance, it causes heap fragmentation and requires multiple pointer dereferences.</p>
  </div>

  <div class="detail-block">
    <h5>4. Simulating Dynamic Polymorphism via VTables (Virtual Tables)</h5>
    <p>To support runtime method overriding, a <code>VTable</code> struct containing function pointers is created. Each class holds a pointer (<code>vptr</code>) to its corresponding static VTable, mirroring how C++ compilers implement virtual dispatch.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C (Embedded Struct &amp; VTable Polymorphism)</span>
    <span class="code-desc">Full simulation of C++ virtual function inheritance in pure ANSI C</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>

<span class="c-comment">/* Forward declaration */</span>
<span class="c-keyword">typedef struct</span> Shape <span class="c-type">Shape</span>;

<span class="c-comment">/* VTable: Function pointer table for polymorphic methods */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">double</span> (*getArea)(<span class="c-type">const</span> <span class="c-type">Shape</span>* self);
    <span class="c-type">void</span> (*draw)(<span class="c-type">const</span> <span class="c-type">Shape</span>* self);
} <span class="c-type">ShapeVTable</span>;

<span class="c-comment">/* --- Base Class --- */</span>
<span class="c-keyword">struct</span> <span class="c-type">Shape</span> {
    <span class="c-type">const</span> <span class="c-type">ShapeVTable</span>* vptr; <span class="c-comment">/* Virtual pointer to class vtable */</span>
    <span class="c-type">int</span> id;
};

<span class="c-comment">/* --- Derived Class: Circle --- */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">Shape</span> base; <span class="c-comment">/* EMBEDDED STRUCT AT OFFSET 0: Guarantees &amp;circle == &amp;base */</span>
    <span class="c-type">double</span> radius;
} <span class="c-type">Circle</span>;

<span class="c-comment">/* Overridden Circle Method implementations */</span>
<span class="c-type">double</span> Circle_getArea(<span class="c-type">const</span> <span class="c-type">Shape</span>* self) {
    <span class="c-comment">/* Downcast base pointer to Circle */</span>
    <span class="c-type">const</span> <span class="c-type">Circle</span>* c = (<span class="c-type">const</span> <span class="c-type">Circle</span>*)self;
    <span class="c-keyword">return</span> 3.14159 * c-&gt;radius * c-&gt;radius;
}

<span class="c-type">void</span> Circle_draw(<span class="c-type">const</span> <span class="c-type">Shape</span>* self) {
    <span class="c-type">const</span> <span class="c-type">Circle</span>* c = (<span class="c-type">const</span> <span class="c-type">Circle</span>*)self;
    printf(<span class="c-string">"Drawing Circle (ID: %d, Radius: %.1f)\\n"</span>, c-&gt;base.id, c-&gt;radius);
}

<span class="c-comment">/* Static VTable for Circle */</span>
<span class="c-type">static const</span> <span class="c-type">ShapeVTable</span> circleVTable = {
    Circle_getArea,
    Circle_draw
};

<span class="c-comment">/* Circle Initializer */</span>
<span class="c-type">void</span> Circle_init(<span class="c-type">Circle</span>* c, <span class="c-type">int</span> id, <span class="c-type">double</span> radius) {
    c-&gt;base.vptr = &amp;circleVTable; <span class="c-comment">/* Bind vptr to Circle's vtable */</span>
    c-&gt;base.id = id;
    c-&gt;radius = radius;
}

<span class="c-comment">/* Polymorphic Caller Function */</span>
<span class="c-type">void</span> renderShape(<span class="c-type">const</span> <span class="c-type">Shape</span>* s) {
    <span class="c-comment">/* Dynamic dispatch through vptr! */</span>
    s-&gt;vptr-&gt;draw(s);
    printf(<span class="c-string">"Calculated Area: %.2f\\n"</span>, s-&gt;vptr-&gt;getArea(s));
}

<span class="c-type">int</span> main() {
    <span class="c-type">Circle</span> myCircle;
    Circle_init(&amp;myCircle, 101, 7.0);

    <span class="c-comment">/* Polymorphism in C: Safe upcasting &amp;myCircle to Shape* */</span>
    renderShape((<span class="c-type">Shape</span>*)&amp;myCircle);
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Memory Architecture: Embedded Struct &amp; VTable Layout</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Derived Object Memory (Circle) -->
      <rect x="50" y="30" width="360" height="210" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="230" y="55" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Derived Object Memory: Circle instance</text>

      <!-- Embedded Base Struct -->
      <rect x="70" y="70" width="320" height="90" rx="5" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="230" y="92" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Embedded 'Shape' Base Struct (Offset 0)</text>

      <!-- vptr inside Base -->
      <rect x="90" y="105" width="130" height="40" rx="3" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
      <text x="155" y="125" fill="#c7d2fe" font-size="10" font-weight="bold" text-anchor="middle">vptr (8 Bytes)</text>
      <text x="155" y="137" fill="#818cf8" font-size="8" text-anchor="middle">Points to VTable</text>

      <!-- id inside Base -->
      <rect x="240" y="105" width="130" height="40" rx="3" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
      <text x="305" y="130" fill="#f8fafc" font-size="10" text-anchor="middle">id (4 Bytes)</text>

      <!-- Derived Fields -->
      <rect x="70" y="170" width="320" height="50" rx="5" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
      <text x="230" y="195" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Circle Specific: radius (double, 8 Bytes)</text>
      <text x="230" y="210" fill="#a7f3d0" font-size="9" text-anchor="middle">Offset 16</text>

      <!-- VTable Memory Box (Right) -->
      <rect x="490" y="30" width="300" height="210" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
      <text x="640" y="55" fill="#c7d2fe" font-size="13" font-weight="bold" text-anchor="middle">Circle Class Static VTable</text>

      <!-- Function Pointers in VTable -->
      <rect x="510" y="75" width="260" height="45" rx="4" fill="#312e81" stroke="#a5b4fc"/>
      <text x="640" y="98" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">(*getArea) -&gt; Circle_getArea</text>
      <text x="640" y="112" fill="#c7d2fe" font-size="9" text-anchor="middle">Address: 0x401050</text>

      <rect x="510" y="135" width="260" height="45" rx="4" fill="#312e81" stroke="#a5b4fc"/>
      <text x="640" y="158" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">(*draw) -&gt; Circle_draw</text>
      <text x="640" y="172" fill="#c7d2fe" font-size="9" text-anchor="middle">Address: 0x401090</text>

      <!-- Arrow from vptr to VTable -->
      <path d="M 220 125 C 360 125, 400 95, 505 95" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#gold-arrow)"/>
      <text x="430" y="105" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">vptr binding</text>

      <defs>
        <marker id="gold-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13):</strong> <em>"Describe implementation of inheritance with example in non-object-oriented languages."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Cite the 3 ways: <strong>Avoid it</strong>, <strong>Flatten the hierarchy</strong>, and <strong>Embedded records (best)</strong>. Explain that placing the base struct at offset 0 guarantees that a derived pointer equals the base pointer. Explain how a table of function pointers (VTable) simulates polymorphism.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Embedded struct at offset 0 provides seamless, zero-cost pointer upcasting.</li>
    <li>Flattening duplicates fields across structs; simple but violates DRY.</li>
    <li>Dynamic polymorphism is simulated via VTables (struct of function pointers).</li>
    <li>The instance stores a <code>vptr</code> pointing to the class's shared static VTable.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-18",
            "number": "18",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Implementing Associations",
            "subtitle": "Buried Pointers vs Distinct Association Objects across 1:1, 1:N & M:N Relationships",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Data Relationship Modeling</div>
    <h3>Implementing Associations in Procedural Environments</h3>
    <p>An <strong>Association</strong> is a structural relationship establishing a semantic connection between independent objects. While relational databases use Foreign Keys and OO languages use object references, implementing associations in procedural code requires choosing between two core architectural patterns:</p>
    <ul>
      <li><strong>Buried Pointers (Embedded References):</strong> Pointers to related objects are embedded directly inside the participant structs.</li>
      <li><strong>Distinct Association Objects:</strong> The association is realized as an independent, standalone data structure (or table) linking the participant objects.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Tattoos vs The Marriage Certificate</div>
  <p><strong>Buried Pointers is like a tattoo:</strong> A husband tattoos his wife's name on his arm, and the wife tattoos his name on hers. It's fast and direct to check, but modifying or removing it is messy, and you cannot easily record extra details (like wedding date or venue) without messing up the personal skin.</p>
  <p><strong>Distinct Association Object is like a Marriage Certificate:</strong> Neither person's body is marked. Instead, City Hall maintains a separate legal registry document containing: <code>(Husband ID, Wife ID, Date, Minister, Venue)</code>. It is completely decoupled, handles link attributes naturally, and can be dissolved without altering the people themselves!</p>
</div>

<div class="subtopics-container">
  <h4>Cardinality Implementations: 1:1, 1:N, and M:N</h4>

  <div class="detail-block">
    <h5>1. One-to-One (1:1) Associations</h5>
    <p>Implemented as a single direct pointer in one or both directions. For example, a <code>Car</code> has a pointer to its <code>Engine*</code>, and <code>Engine</code> has a back-pointer to <code>Car*</code>.</p>
  </div>

  <div class="detail-block">
    <h5>2. One-to-Many (1:N) Associations</h5>
    <p>The "One" side holds a dynamic collection (linked list, dynamic array, or pointer array) pointing to multiple "Many" objects. Each object on the "Many" side holds a single back-pointer to its parent (e.g., a <code>Department</code> holds <code>Employee* staff[]</code>; each <code>Employee</code> holds <code>Department* dept</code>).</p>
  </div>

  <div class="detail-block">
    <h5>3. Many-to-Many (M:N) Associations</h5>
    <p>Difficult to implement cleanly with buried pointers because both sides must manage dynamically expanding pointer lists. The industry best practice is to implement M:N associations using <strong>Distinct Association Objects</strong>.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Deep Comparison: Buried Pointers vs Distinct Association Objects</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Evaluation Criteria</th>
        <th>Buried Pointers (Embedded References)</th>
        <th>Distinct Association Objects</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Performance / Speed</strong></td>
        <td><strong>Fastest</strong>; direct $O(1)$ memory pointer dereference</td>
        <td>Slightly slower; requires table search or hash index lookup</td>
      </tr>
      <tr>
        <td><strong>Link Attributes Support</strong></td>
        <td><strong>Poor</strong>; where do you put <code>enrollmentDate</code> or <code>grade</code>?</td>
        <td><strong>Natural</strong>; link attributes become fields inside the association record</td>
      </tr>
      <tr>
        <td><strong>Decoupling / Modularity</strong></td>
        <td>Low; participating classes must know about each other</td>
        <td><strong>High</strong>; classes remain completely unaware of the association</td>
      </tr>
      <tr>
        <td><strong>Many-to-Many (M:N) Suitability</strong></td>
        <td>Cumbersome and prone to pointer desynchronization</td>
        <td><strong>Ideal</strong>; models standard relational join tables</td>
      </tr>
      <tr>
        <td><strong>Memory Footprint</strong></td>
        <td>Compact (just 8 bytes per pointer)</td>
        <td>Requires extra memory for distinct node allocations</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C Implementation (Buried Pointers vs Distinct Objects)</span>
    <span class="code-desc">Contrasting 1:N Buried Pointer with M:N Distinct Association Record</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdlib.h&gt;</span>

<span class="c-comment">/* --- APPROACH 1: BURIED POINTERS (1:1 or 1:N) --- */</span>
<span class="c-keyword">typedef struct</span> Department <span class="c-type">Department</span>;

<span class="c-keyword">typedef struct</span> {
    <span class="c-type">int</span> empId;
    <span class="c-type">char</span> name[32];
    <span class="c-type">Department</span>* dept; <span class="c-comment">/* Buried Pointer: Direct link to parent */</span>
} <span class="c-type">Employee</span>;

<span class="c-keyword">struct</span> <span class="c-type">Department</span> {
    <span class="c-type">int</span> deptId;
    <span class="c-type">char</span> deptName[32];
};

<span class="c-comment">/* --- APPROACH 2: DISTINCT ASSOCIATION OBJECT (M:N with Link Attributes) --- */</span>
<span class="c-keyword">typedef struct</span> {
    <span class="c-type">int</span> studentId;
    <span class="c-type">int</span> courseId;
    <span class="c-type">double</span> grade;       <span class="c-comment">/* Link Attribute: specific to this student-course pair */</span>
    <span class="c-type">char</span> semester[16];  <span class="c-comment">/* Link Attribute */</span>
} <span class="c-type">EnrollmentRecord</span>;    <span class="c-comment">/* Standalone Association Entity */</span>

<span class="c-type">int</span> main() {
    <span class="c-comment">/* 1. Using Buried Pointer */</span>
    <span class="c-type">Department</span> csDept = {10, <span class="c-string">"Computer Science"</span>};
    <span class="c-type">Employee</span> emp1 = {101, <span class="c-string">"Alice"</span>, &amp;csDept};
    printf(<span class="c-string">"[Buried Pointer] %s works in %s\\n"</span>, emp1.name, emp1.dept-&gt;deptName);

    <span class="c-comment">/* 2. Using Distinct Association Object */</span>
    <span class="c-type">EnrollmentRecord</span> er = {501, 302, 92.5, <span class="c-string">"Fall 2026"</span>};
    printf(<span class="c-string">"[Distinct Object] Student #%d in Course #%d: Grade = %.1f (%s)\\n"</span>,
           er.studentId, er.courseId, er.grade, er.semester);

    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Buried Pointers vs Distinct Association Object</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Top Half: Buried Pointers -->
      <rect x="30" y="20" width="780" height="110" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="420" y="42" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Approach A: Buried Pointers (Embedded Reference)</text>

      <rect x="70" y="55" width="220" height="55" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <text x="180" y="78" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Employee Instance</text>
      <text x="180" y="98" fill="#38bdf8" font-size="10" text-anchor="middle">dept: 0x8A40 (Buried Pointer)</text>

      <!-- Direct Arrow -->
      <path d="M 290 82 L 530 82" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#cyan-assoc-arrow)"/>
      <text x="410" y="75" fill="#bae6fd" font-size="10" text-anchor="middle">Direct 8-Byte Address</text>

      <rect x="540" y="55" width="220" height="55" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <text x="650" y="78" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Department Instance</text>
      <text x="650" y="98" fill="#94a3b8" font-size="10" text-anchor="middle">Address: 0x8A40</text>

      <!-- Bottom Half: Distinct Association Object -->
      <rect x="30" y="145" width="780" height="120" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="420" y="168" fill="#a855f7" font-size="13" font-weight="bold" text-anchor="middle">Approach B: Distinct Association Object (Independent Entity)</text>

      <rect x="70" y="185" width="180" height="60" rx="5" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
      <text x="160" y="210" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Student Entity</text>
      <text x="160" y="228" fill="#94a3b8" font-size="10" text-anchor="middle">(No Course pointers)</text>

      <!-- Junction Association Box in Center -->
      <rect x="310" y="180" width="220" height="70" rx="6" fill="#4c1d95" stroke="#c084fc" stroke-width="2"/>
      <text x="420" y="202" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Enrollment Record</text>
      <text x="420" y="218" fill="#e9d5ff" font-size="9" text-anchor="middle">studentId | courseId</text>
      <text x="420" y="233" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Link Attributes: grade, term</text>

      <!-- Connecting Lines -->
      <path d="M 250 215 L 310 215" stroke="#c084fc" stroke-width="2"/>
      <path d="M 530 215 L 590 215" stroke="#c084fc" stroke-width="2"/>

      <rect x="590" y="185" width="180" height="60" rx="5" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
      <text x="680" y="210" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Course Entity</text>
      <text x="680" y="228" fill="#94a3b8" font-size="10" text-anchor="middle">(No Student pointers)</text>

      <defs>
        <marker id="cyan-assoc-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2014-15):</strong> <em>"Explain the implementation of associations in non-object-oriented languages. Compare buried pointers and distinct association objects."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Draw the comparison table above. Highlight that Buried Pointers provide fast dereferencing for 1:1 and 1:N relations, while Distinct Association Objects decouple classes, support link attributes, and naturally implement M:N associations.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Buried pointers:</strong> Pointers embedded in structs; fast $O(1)$, but tightly coupled.</li>
    <li><strong>Distinct objects:</strong> Separate standalone join records; ideal for M:N and link attributes.</li>
    <li>1:1 uses single pointer; 1:N uses pointer collection + child back-pointer.</li>
    <li>Link attributes (e.g., grade, hireDate) require distinct association records.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-19",
            "number": "19",
            "part": "Part 2 — SA/SD & Non-OO Implementation",
            "title": "Implementing Encapsulation in Non-OO Languages",
            "subtitle": "Information Hiding via Opaque Pointers (Incomplete Types), Static Scoping & Header API Firewalls",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Data Security &amp; Information Hiding</div>
    <h3>Simulating Encapsulation Without 'private' Keywords</h3>
    <p><strong>Encapsulation</strong> bundles data and operations while strictly hiding internal representations from external manipulation. Although procedural languages like C lack <code>public</code>, <code>private</code>, and <code>protected</code> keywords, robust encapsulation can still be enforced at the <strong>compiler and linker level</strong>.</p>
    <p>By separating the interface from the implementation using <strong>Opaque Pointers (Incomplete Struct Types)</strong> and the <code>static</code> keyword for internal translation-unit linkage, C developers can build airtight encapsulation firewalls.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Bank ATM &amp; The Armored Vault</div>
  <p>When you use an ATM, the bank gives you a screen, card slot, and cash dispenser (the public header interface <code>atm.h</code>). You cannot reach through the slot to touch the money cassettes, motor gears, or security sensors inside the vault (the hidden implementation <code>atm.c</code>). <strong>Opaque pointers</strong> provide that exact armored vault: client code is given a pointer to the vault, but the compiler forbids them from looking inside!</p>
</div>

<div class="subtopics-container">
  <h4>The 3 Pillars of Encapsulation in Procedural C</h4>

  <div class="detail-block">
    <h5>1. Opaque Pointers (Incomplete Struct Declarations)</h5>
    <p>In the public header file (<code>account.h</code>), the struct is forward-declared without defining its members:</p>
    <pre class="inline-code"><code>typedef struct BankAccount BankAccount; /* Incomplete Type */</code></pre>
    <p>The actual struct definition is placed exclusively inside the implementation file (<code>account.c</code>). Because external client code only sees the incomplete type, attempting to write <code>acc-&gt;balance = 1000000;</code> causes a compile-time error: <em>"dereferencing pointer to incomplete type"</em>.</p>
  </div>

  <div class="detail-block">
    <h5>2. Static Internal Linkage (Private Helper Functions)</h5>
    <p>Functions and global variables marked with the <code>static</code> keyword in C are scoped strictly to their local <code>.c</code> translation unit. The linker strips their symbols from external object files, making them completely invisible to outside modules.</p>
  </div>

  <div class="detail-block">
    <h5>3. Controlled Accessor &amp; Mutator API</h5>
    <p>External callers interact with object state strictly via exported public API functions (e.g., <code>BankAccount_deposit()</code>, <code>BankAccount_getBalance()</code>) which validate preconditions before updating internal state.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C (The Opaque Pointer Pattern - PIMPL in C)</span>
    <span class="code-desc">Airtight compiler-enforced encapsulation in ANSI C</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">/* ========================================================== */</span>
<span class="c-comment">/* FILE 1: account.h (PUBLIC INTERFACE DISTRIBUTED TO CLIENT) */</span>
<span class="c-comment">/* ========================================================== */</span>
<span class="c-keyword">#ifndef</span> ACCOUNT_H
<span class="c-keyword">#define</span> ACCOUNT_H

<span class="c-comment">/* OPAQUE POINTER: Incomplete type declaration */</span>
<span class="c-keyword">typedef struct</span> BankAccount <span class="c-type">BankAccount</span>;

<span class="c-comment">/* Public API Prototypes */</span>
<span class="c-type">BankAccount</span>* BankAccount_create(<span class="c-type">int</span> id, <span class="c-type">double</span> initialBalance);
<span class="c-type">void</span> BankAccount_deposit(<span class="c-type">BankAccount</span>* self, <span class="c-type">double</span> amount);
<span class="c-type">double</span> BankAccount_getBalance(<span class="c-type">const</span> <span class="c-type">BankAccount</span>* self);
<span class="c-type">void</span> BankAccount_destroy(<span class="c-type">BankAccount</span>* self);

<span class="c-keyword">#endif</span>

<span class="c-comment">/* ========================================================== */</span>
<span class="c-comment">/* FILE 2: account.c (PRIVATE IMPLEMENTATION COMPILED TO .o) */</span>
<span class="c-comment">/* ========================================================== */</span>
<span class="c-keyword">#include</span> <span class="c-string">"account.h"</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdlib.h&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>

<span class="c-comment">/* FULL STRUCT DEFINITION (Hidden inside .c) */</span>
<span class="c-keyword">struct</span> <span class="c-type">BankAccount</span> {
    <span class="c-type">int</span> id;
    <span class="c-type">double</span> balance;      <span class="c-comment">/* Encapsulated private state */</span>
    <span class="c-type">int</span> transactionCount;
};

<span class="c-comment">/* Private helper function (static linkage = invisible outside) */</span>
<span class="c-keyword">static void</span> logAudit(<span class="c-type">int</span> id, <span class="c-type">const char</span>* msg) {
    printf(<span class="c-string">"[AUDIT LOG] Account #%d: %s\\n"</span>, id, msg);
}

<span class="c-type">BankAccount</span>* BankAccount_create(<span class="c-type">int</span> id, <span class="c-type">double</span> initialBalance) {
    <span class="c-type">BankAccount</span>* acc = (<span class="c-type">BankAccount</span>*)malloc(<span class="c-keyword">sizeof</span>(<span class="c-type">BankAccount</span>));
    <span class="c-keyword">if</span> (acc != NULL) {
        acc-&gt;id = id;
        acc-&gt;balance = initialBalance;
        acc-&gt;transactionCount = 0;
        logAudit(id, <span class="c-string">"Created successfully"</span>);
    }
    <span class="c-keyword">return</span> acc;
}

<span class="c-type">void</span> BankAccount_deposit(<span class="c-type">BankAccount</span>* self, <span class="c-type">double</span> amount) {
    <span class="c-keyword">if</span> (amount &gt; 0.0) {
        self-&gt;balance += amount;
        self-&gt;transactionCount++;
        logAudit(self-&gt;id, <span class="c-string">"Deposit verified"</span>);
    }
}

<span class="c-type">double</span> BankAccount_getBalance(<span class="c-type">const</span> <span class="c-type">BankAccount</span>* self) {
    <span class="c-keyword">return</span> self-&gt;balance;
}

<span class="c-type">void</span> BankAccount_destroy(<span class="c-type">BankAccount</span>* self) {
    <span class="c-keyword">if</span> (self != NULL) {
        free(self);
    }
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The Opaque Pointer Encapsulation Firewall</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Client Code Domain (Left) -->
      <rect x="40" y="30" width="230" height="210" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="155" y="58" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Client Application (main.c)</text>
      
      <rect x="55" y="75" width="200" height="40" rx="4" fill="#0f172a" stroke="#475569"/>
      <text x="155" y="98" fill="#e2e8f0" font-size="10" text-anchor="middle">#include "account.h"</text>

      <rect x="55" y="125" width="200" height="40" rx="4" fill="#065f46" stroke="#34d399"/>
      <text x="155" y="148" fill="#a7f3d0" font-size="10" text-anchor="middle">BankAccount_deposit(acc, 500)</text>

      <rect x="55" y="175" width="200" height="45" rx="4" fill="#7f1d1d" stroke="#ef4444"/>
      <text x="155" y="195" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">acc-&gt;balance = 99999;</text>
      <text x="155" y="210" fill="#f87171" font-size="8" text-anchor="middle">❌ COMPILE ERROR (Incomplete type)</text>

      <!-- Center Firewall Barrier -->
      <rect x="300" y="20" width="140" height="230" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
      <text x="370" y="48" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">INTERFACE</text>
      <text x="370" y="65" fill="#e9d5ff" font-size="11" text-anchor="middle">account.h</text>
      
      <line x1="315" y1="80" x2="425" y2="80" stroke="#a855f7" stroke-width="1.5"/>

      <text x="370" y="110" fill="#f8fafc" font-size="9" text-anchor="middle">typedef struct</text>
      <text x="370" y="125" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">BankAccount</text>
      <text x="370" y="140" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">BankAccount;</text>

      <text x="370" y="175" fill="#94a3b8" font-size="9" text-anchor="middle">Only pointers (*)</text>
      <text x="370" y="190" fill="#94a3b8" font-size="9" text-anchor="middle">are permitted!</text>
      <text x="370" y="220" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Public API</text>

      <!-- Private Implementation Domain (Right) -->
      <rect x="470" y="30" width="330" height="210" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
      <text x="635" y="58" fill="#4ade80" font-size="13" font-weight="bold" text-anchor="middle">Implementation (account.c)</text>

      <rect x="490" y="75" width="290" height="90" rx="5" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
      <text x="635" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Hidden Struct Definition</text>
      <text x="635" y="115" fill="#86efac" font-size="10" text-anchor="middle">int id;</text>
      <text x="635" y="130" fill="#86efac" font-size="10" text-anchor="middle">double balance; (ENCRYPTED / PROTECTED)</text>
      <text x="635" y="145" fill="#86efac" font-size="10" text-anchor="middle">int transactionCount;</text>

      <rect x="490" y="175" width="290" height="45" rx="4" fill="#0f172a" stroke="#64748b"/>
      <text x="635" y="195" fill="#f59e0b" font-size="10" text-anchor="middle">static void logAudit(...) [Private Linkage]</text>
      <text x="635" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Stripped by linker from external symbol table</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2015-16):</strong> <em>"Explain how encapsulation and information hiding are implemented in non-object-oriented languages."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Explain the <strong>Opaque Pointer technique</strong> (incomplete struct type in header). Show how attempting direct field access triggers a compiler error. Mention <code>static</code> internal linkage for private subroutines.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Encapsulation is enforced in C via <strong>Opaque Pointers</strong> (incomplete struct types).</li>
    <li>Header file declares <code>typedef struct Foo Foo;</code>; fields defined only in <code>.c</code>.</li>
    <li>Direct field access <code>foo-&gt;bar</code> is blocked at compile-time by the compiler.</li>
    <li><code>static</code> functions restrict scope to the single file, preventing external linker calls.</li>
  </ul>
</div>
"""
        }
    ]
