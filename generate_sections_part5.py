# generate_sections_part5.py: Part 5 - Basic Behavioural Modeling (Sections 22 to 31)

def get_part5_sections():
    return [
        {
            "id": "sec-22",
            "number": "22",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Basic Behavioural Modeling",
            "subtitle": "Internal Dynamic Aspects, SDLC Phases & Two Categories of Behavioral Models",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Dynamic Perspective</div>
    <h3>Meaning of Behavioral Modeling</h3>
    <p><strong>Behavioral Modeling</strong> captures the <em>internal dynamic aspects</em> of an information system. While structural models define what entities exist, behavioral models define how those entities respond to stimuli, coordinate through messages, alter their internal state, and execute computational procedures over time.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Behavior Across the Software Development Life Cycle (SDLC)</h4>

  <div class="detail-block">
    <h5>1. Dynamic Behavior Across SDLC Phases</h5>
    <ul>
      <li><strong>Behavior During Analysis:</strong> Focuses on user-observable functionality and business requirements without technical implementation bias (modeled via <em>Use Case Diagrams</em> and <em>High-Level Activity Diagrams</em>).</li>
      <li><strong>Behavior During Design:</strong> Focuses on how software objects collaborate to realize use cases, assigning responsibilities and message sequencing (modeled via <em>Sequence Diagrams</em> and <em>Collaboration Diagrams</em>).</li>
      <li><strong>Behavior During Implementation:</strong> Focuses on multi-threaded execution, concurrency locks, state transitions, and exception signals (modeled via <em>State Machines</em>, <em>Timing Diagrams</em>, and <em>Active Objects</em>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. The Two Fundamental Categories of Behavioral Models</h5>
    <div class="two-col-cards">
      <div class="feature-card">
        <div class="col-head blue-head">Category 1: Models Representing Business Processes</div>
        <p>Emphasizes step-by-step algorithms, workflow control logic, and inter-object message exchanges across time and space:</p>
        <ul>
          <li><strong>Activity Diagrams:</strong> Procedural and dataflow logic.</li>
          <li><strong>Sequence Diagrams:</strong> Time-ordered message traces.</li>
          <li><strong>Communication / Collaboration Diagrams:</strong> Link-oriented object collaborations.</li>
        </ul>
      </div>

      <div class="feature-card">
        <div class="col-head green-head">Category 2: Models Representing Changes in Underlying Data</div>
        <p>Emphasizes the lifecycle and state transitions of individual reactive objects across their lifetime:</p>
        <ul>
          <li><strong>Behavioral State Machines (Statechart Diagrams):</strong> Models states, triggers, guards, and action effects.</li>
          <li><strong>Timing Diagrams:</strong> Models explicit state changes against a continuous millisecond timeline.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: The Behavioral Modeling Spectrum</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <rect x="40" y="20" width="320" height="165" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
      <rect x="40" y="20" width="320" height="32" rx="8" fill="#3b82f6" fill-opacity="0.15"/>
      <text x="200" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">Category 1: Business Process &amp; Interaction</text>
      <text x="60" y="75" font-size="11" fill="var(--text-primary)">• Focus: Workflows, steps &amp; message exchanges</text>
      <text x="60" y="98" font-size="11" fill="var(--text-primary)">• Diagrams: Sequence, Collaboration, Activity</text>
      <text x="60" y="121" font-size="11" fill="var(--text-primary)">• Scope: Multi-object collaboration</text>
      <text x="60" y="144" font-size="11" fill="var(--text-muted)">• Driven by: User goals &amp; scenarios</text>

      <rect x="400" y="20" width="320" height="165" rx="8" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
      <rect x="400" y="20" width="320" height="32" rx="8" fill="#10b981" fill-opacity="0.15"/>
      <text x="560" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">Category 2: Data &amp; State Transformation</text>
      <text x="420" y="75" font-size="11" fill="var(--text-primary)">• Focus: Internal state changes of reactive objects</text>
      <text x="420" y="98" font-size="11" fill="var(--text-primary)">• Diagrams: State Machine, Timing Diagrams</text>
      <text x="420" y="121" font-size="11" fill="var(--text-primary)">• Scope: Single object lifecycle</text>
      <text x="420" y="144" font-size="11" fill="var(--text-muted)">• Driven by: Stimuli, events, timeouts</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12):</strong> <em>"Discuss in brief basic behavioural modeling. What are the two main categories of behavioural models?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Scoring Guide:</strong> Cite the two source categories: (1) Models representing business processes (Interaction & Activity); (2) Models representing changes in underlying data (Behavioral State Machines).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Behavioral Modeling = Dynamic execution, triggers, message passing, states.</li>
    <li>Covers Analysis (Use cases), Design (Sequences), and Implementation (State machines & threads).</li>
    <li>2 Categories: Business process / Interaction vs. Data lifecycle / State machines.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-23",
            "number": "23",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Use Cases",
            "subtitle": "Capturing Functional Requirements, Actors, System Boundaries & Use Case Relationships",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Requirements Engineering</div>
    <h3>Meaning and Purpose of Use Cases</h3>
    <p>A <strong>Use Case</strong> specifies a sequence of actions, including variants, that a system performs to yield an observable result of value to a specific <strong>Actor</strong>. Pioneered by Ivar Jacobson, use cases bridge informal customer requirements and formal software architecture.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Core Terms & Relationships</h4>

  <div class="detail-block">
    <h5>1. Key Terminology</h5>
    <ul>
      <li><strong>Actor:</strong> An idealized external entity (human role, external hardware, or third-party software) that interacts with the system. Actors reside <em>outside</em> the system boundary.</li>
      <li><strong>System:</strong> The software application or boundary under design.</li>
      <li><strong>Interaction:</strong> The dialogue of input stimuli and responses between an actor and the system.</li>
      <li><strong>Functionality:</strong> What the system does to deliver business value.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. The Three Use Case Relationships</h5>
    <div class="three-col-cards">
      <div class="feature-card">
        <div class="col-head blue-head">&lt;&lt;include&gt;&gt;</div>
        <p><strong>Mandatory Subroutine:</strong> The base use case unconditionally incorporates the behavior of another use case. Avoids code/spec duplication.</p>
        <p><strong>Arrow:</strong> Dashed arrow pointing from Base to Included use case.</p>
        <p><em>Example:</em> <code>TransferFunds</code> &rarr; <code>&lt;&lt;include&gt;&gt;</code> &rarr; <code>AuthenticateUser</code>.</p>
      </div>

      <div class="feature-card">
        <div class="col-head green-head">&lt;&lt;extend&gt;&gt;</div>
        <p><strong>Optional / Conditional:</strong> The extending use case conditionally adds behavior to the base use case only if a specific extension point rule triggers.</p>
        <p><strong>Arrow:</strong> Dashed arrow pointing from Extension to Base use case.</p>
        <p><em>Example:</em> <code>ApplyBonusDiscount</code> &rarr; <code>&lt;&lt;extend&gt;&gt;</code> &rarr; <code>CalculateBill</code>.</p>
      </div>

      <div class="feature-card">
        <div class="col-head purple-head">Generalization</div>
        <p><strong>Inheritance:</strong> A specialized use case inherits behavior and goals from a general use case, or a specialized actor inherits roles from a general actor.</p>
        <p><strong>Arrow:</strong> Solid line with hollow triangle pointing to parent.</p>
        <p><em>Example:</em> <code>CardPayment</code> specializes <code>MakePayment</code>.</p>
      </div>
    </div>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: &lt;&lt;include&gt;&gt;, &lt;&lt;extend&gt;&gt; and Generalization</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ucArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
        <marker id="ucGen" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="9" markerHeight="9" orient="auto">
          <polygon points="0,1 11,6 0,11" fill="#fff" stroke="#8b5cf6" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Actor -->
      <g transform="translate(40, 100)">
        <circle cx="20" cy="15" r="12" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="27" x2="20" y2="55" stroke="#3b82f6" stroke-width="2"/>
        <line x1="5" y1="38" x2="35" y2="38" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="6" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="34" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <text x="20" y="92" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Customer</text>
      </g>

      <!-- Base Use Case: Withdraw Cash -->
      <g transform="translate(190, 110)">
        <ellipse cx="80" cy="30" rx="75" ry="28" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="80" y="34" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Withdraw Cash</text>
      </g>
      <line x1="85" y1="140" x2="190" y2="140" stroke="#64748b" stroke-width="1.8"/>

      <!-- Included Use Case: Verify PIN (Right) -->
      <g transform="translate(490, 110)">
        <ellipse cx="80" cy="30" rx="75" ry="28" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="80" y="34" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Verify PIN</text>
      </g>
      <!-- Include arrow: Base -> Included -->
      <line x1="345" y1="140" x2="485" y2="140" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="4,4" marker-end="url(#ucArr)"/>
      <text x="415" y="132" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">&lt;&lt;include&gt;&gt;</text>

      <!-- Extending Use Case: Print Receipt (Top) -->
      <g transform="translate(190, 15)">
        <ellipse cx="80" cy="25" rx="75" ry="24" fill="var(--card-bg)" stroke="#f59e0b" stroke-width="2"/>
        <text x="80" y="29" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Print Receipt</text>
      </g>
      <!-- Extend arrow: Extension -> Base -->
      <line x1="270" y1="65" x2="270" y2="105" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4,4" marker-end="url(#ucArr)"/>
      <text x="315" y="88" text-anchor="middle" font-size="10" font-weight="bold" fill="#d97706">&lt;&lt;extend&gt;&gt;</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2014-15):</strong> <em>"Explain the relationships in use case diagrams. Differentiate between &lt;&lt;include&gt;&gt; and &lt;&lt;extend&gt;&gt; with suitable diagrams."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Crucial Direction Alert:</strong> <code>&lt;&lt;include&gt;&gt;</code> points from Base to Included (Base needs the subroutine). <code>&lt;&lt;extend&gt;&gt;</code> points from Extension to Base (The extension hooks into the base). Getting arrow directions backwards loses 5 marks!
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Use case = Goal-oriented sequence yielding observable value to an actor.</li>
    <li>Actor = External entity interacting with system (human, device, external service).</li>
    <li><code>&lt;&lt;include&gt;&gt;</code> = Mandatory shared routine (Base &rarr; Included).</li>
    <li><code>&lt;&lt;extend&gt;&gt;</code> = Optional hook (Extension &rarr; Base).</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-24",
            "number": "24",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Use Case Diagram",
            "subtitle": "System Boundary, Actor-System Interactions & Forward/Reverse Engineering Utility",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">System Context</div>
    <h3>Meaning of Use Case Diagram</h3>
    <p>A <strong>Use Case Diagram</strong> captures the dynamic behavior of a system from the perspective of external actors. It establishes the <strong>system boundary</strong>, showing what functionality is inside the system and which external users, hardware, and systems interact with it.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Components and Utility in System Design</h4>

  <div class="detail-block">
    <h5>1. Core Components</h5>
    <ul>
      <li><strong>Actors:</strong> Stick figures representing external roles.</li>
      <li><strong>Use Cases:</strong> Horizontal ellipses enclosing verb-phrase goals.</li>
      <li><strong>System Boundary Box:</strong> A large labeled rectangle framing the system; use cases reside inside, actors reside outside.</li>
      <li><strong>Communication Association:</strong> Solid lines connecting actors to the use cases they trigger or participate in.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Utility Across System Design</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Engineering Phase</th>
          <th>Practical Utility</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Requirement Gathering</strong></td>
          <td>Engages non-technical clients to discover functional scope without getting bogged down in database schemas.</td>
        </tr>
        <tr>
          <td><strong>High-Level Design</strong></td>
          <td>Defines system boundaries and partitions large monolithic systems into modular subsystems.</td>
        </tr>
        <tr>
          <td><strong>Forward Engineering</strong></td>
          <td>Provides test engineers with unambiguous Acceptance Test Scenarios and QA test suites directly from use case paths.</td>
        </tr>
        <tr>
          <td><strong>Reverse Engineering</strong></td>
          <td>Allows engineers inspecting legacy source code to reconstruct high-level user features and capabilities.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Banking System Use Case Diagram with Boundary Box</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 300" width="100%" height="300" xmlns="http://www.w3.org/2000/svg">
      <!-- System Boundary Box -->
      <rect x="180" y="20" width="380" height="260" rx="8" fill="var(--bg-secondary)" stroke="#64748b" stroke-width="2"/>
      <text x="370" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">BANKING ATM SYSTEM (Boundary)</text>

      <!-- Actor 1: Customer (Left) -->
      <g transform="translate(40, 110)">
        <circle cx="20" cy="15" r="12" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="27" x2="20" y2="55" stroke="#3b82f6" stroke-width="2"/>
        <line x1="5" y1="38" x2="35" y2="38" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="6" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="34" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <text x="20" y="92" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Customer</text>
      </g>

      <!-- Actor 2: Bank Admin (Right) -->
      <g transform="translate(680, 110)">
        <circle cx="20" cy="15" r="12" fill="rgba(99, 102, 241, 0.2)" stroke="#10b981" stroke-width="2"/>
        <line x1="20" y1="27" x2="20" y2="55" stroke="#10b981" stroke-width="2"/>
        <line x1="5" y1="38" x2="35" y2="38" stroke="#10b981" stroke-width="2"/>
        <line x1="20" y1="55" x2="6" y2="75" stroke="#10b981" stroke-width="2"/>
        <line x1="20" y1="55" x2="34" y2="75" stroke="#10b981" stroke-width="2"/>
        <text x="20" y="92" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">ATM Tech</text>
      </g>

      <!-- Use Case 1: Check Balance -->
      <ellipse cx="370" cy="75" rx="90" ry="24" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
      <text x="370" y="79" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Check Balance</text>
      <line x1="85" y1="135" x2="285" y2="75" stroke="#3b82f6" stroke-width="1.8"/>

      <!-- Use Case 2: Withdraw Funds -->
      <ellipse cx="370" cy="140" rx="90" ry="24" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
      <text x="370" y="144" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Withdraw Funds</text>
      <line x1="85" y1="140" x2="280" y2="140" stroke="#3b82f6" stroke-width="1.8"/>

      <!-- Use Case 3: Refill Cash -->
      <ellipse cx="370" cy="215" rx="90" ry="24" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
      <text x="370" y="219" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Refill Cash Dispenser</text>
      <line x1="460" y1="215" x2="680" y2="140" stroke="#10b981" stroke-width="1.8"/>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2014-15):</strong> <em>"Write short notes on use case diagram with suitable diagram and their utility in system design."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Always draw the rectangular <strong>System Boundary Box</strong>! Placing use cases inside without a bounding box signals an incomplete UML model to university evaluators.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Components: Actors (Outside), Use Cases (Inside), System Boundary (Box), Associations (Lines).</li>
    <li>Utility: Requirement scoping, test-case generation, forward/reverse engineering.</li>
    <li>Actors can be humans, external hardware sensors, or third-party web services.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-25",
            "number": "25",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Activity Diagram",
            "subtitle": "Workflows, Control Flow, Branching, Concurrency (Fork & Join) & Swimlanes",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Workflow Architecture</div>
    <h3>Meaning of Activity Diagram</h3>
    <p>An <strong>Activity Diagram</strong> is an advanced, object-oriented flowchart that models the <strong>flow of control and computation from activity to activity</strong>. It excels at visualizing step-by-step algorithms, multi-department business processes, and concurrent/parallel operations.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Activity Diagram Notations and Components</h4>

  <div class="detail-block">
    <h5>1. Foundational Nodes</h5>
    <ul>
      <li><strong>Initial State (<code>●</code>):</strong> A solid black circle marking the entry point of the workflow.</li>
      <li><strong>Activity / Action State:</strong> A rounded rectangle representing a discrete step of computation.</li>
      <li><strong>Control Flow:</strong> Solid directed arrows showing progression between activities.</li>
      <li><strong>Decision & Merge (<code>◇</code>):</strong> A diamond node with guard conditions (e.g., <code>[isApproved]</code> vs <code>[else]</code>).</li>
      <li><strong>Final State (<code>◉</code>):</strong> A solid circle enclosed inside an outer circle (bullseye) marking termination.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Concurrency: Fork and Join Synchronization Bars</h5>
    <div class="two-col-cards">
      <div class="feature-card">
        <div class="col-head blue-head">Fork Bar (Splitting Concurrency)</div>
        <p>A solid thick horizontal or vertical bar with <strong>one incoming transition and two or more outgoing parallel flows</strong>. Demonstrates concurrent thread execution.</p>
      </div>

      <div class="feature-card">
        <div class="col-head green-head">Join Bar (Synchronizing Concurrency)</div>
        <p>A solid thick bar with <strong>multiple incoming concurrent flows and exactly one outgoing flow</strong>. The outgoing flow cannot execute until ALL incoming activities finish.</p>
      </div>
    </div>
  </div>

  <div class="detail-block">
    <h5>3. Swimlanes (Activity Partitions)</h5>
    <p>Vertical or horizontal parallel columns dividing the diagram into distinct organizational departments, actors, or microservices (e.g. Customer, OrderService, Warehouse). Shows exactly <em>who is responsible</em> for each action.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Order Processing Activity Diagram with Concurrency & Swimlanes</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 330" width="100%" height="330" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="actArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#3b82f6" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Swimlane 1: Customer -->
      <rect x="40" y="20" width="340" height="290" fill="var(--bg-secondary)" stroke="#cbd5e1"/>
      <text x="210" y="40" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">Customer Partition</text>

      <!-- Swimlane 2: Warehouse / Billing -->
      <rect x="380" y="20" width="340" height="290" fill="var(--card-bg)" stroke="#cbd5e1"/>
      <text x="550" y="40" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--text-primary)">Warehouse &amp; Billing Partition</text>

      <!-- Start Node -->
      <circle cx="210" cy="70" r="10" class="uml-dark-shape" fill="#60a5fa"/>
      <line x1="210" y1="80" x2="210" y2="105" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#actArr)"/>

      <!-- Action 1: Place Order -->
      <rect x="150" y="105" width="120" height="35" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
      <text x="210" y="127" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Place Order</text>

      <!-- Flow over to Fork in Warehouse -->
      <line x1="270" y1="122" x2="430" y2="122" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#actArr)"/>

      <!-- Fork Bar (Thick line) -->
      <line x1="430" y1="100" x2="430" y2="150" class="uml-dark-stroke" stroke="#60a5fa" stroke-width="6"/>
      <text x="410" y="90" font-size="9" font-weight="bold" fill="#2563eb">FORK</text>

      <!-- Parallel Action A: Charge Credit Card -->
      <line x1="430" y1="110" x2="490" y2="90" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#actArr)"/>
      <rect x="490" y="75" width="140" height="30" rx="6" fill="var(--bg-secondary)" stroke="#10b981" stroke-width="1.5"/>
      <text x="560" y="94" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--text-primary)">Charge Credit Card</text>

      <!-- Parallel Action B: Pack Items -->
      <line x1="430" y1="140" x2="490" y2="155" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#actArr)"/>
      <rect x="490" y="140" width="140" height="30" rx="6" fill="var(--bg-secondary)" stroke="#10b981" stroke-width="1.5"/>
      <text x="560" y="159" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--text-primary)">Pack Inventory Items</text>

      <!-- Join Bar -->
      <line x1="630" y1="90" x2="680" y2="110" stroke="#3b82f6" stroke-width="1.8"/>
      <line x1="630" y1="155" x2="680" y2="135" stroke="#3b82f6" stroke-width="1.8"/>
      <line x1="680" y1="100" x2="680" y2="150" class="uml-dark-stroke" stroke="#60a5fa" stroke-width="6"/>
      <text x="690" y="90" font-size="9" font-weight="bold" fill="#2563eb">JOIN</text>

      <!-- Action: Ship Order -->
      <line x1="680" y1="125" x2="680" y2="210" stroke="#3b82f6" stroke-width="1.8"/>
      <line x1="680" y1="210" x2="590" y2="210" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#actArr)"/>
      <rect x="470" y="195" width="120" height="35" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
      <text x="530" y="217" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Ship Package</text>

      <!-- Final Node -->
      <line x1="470" y1="212" x2="350" y2="212" stroke="#3b82f6" stroke-width="1.8" marker-end="url(#actArr)"/>
      <g transform="translate(320, 212)">
        <circle cx="10" cy="0" r="10" fill="none" class="uml-dark-stroke" stroke="#60a5fa" stroke-width="2"/>
        <circle cx="10" cy="0" r="6" class="uml-dark-shape" fill="#60a5fa"/>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15):</strong> <em>"What do you mean by activity diagram? Explain with an example showing fork, join, decision, and swimlanes."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Full Marks Strategy:</strong> The diagram above contains all required elements: Start node, Actions, Fork (concurrency), Join (synchronization), Swimlanes (responsibility columns), and Final bullseye state.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Activity Diagram = Flow of control and computation across steps.</li>
    <li>Initial state = <code>●</code> | Final state = <code>◉</code>.</li>
    <li>Fork bar = 1 flow splits into parallel flows.</li>
    <li>Join bar = Parallel flows synchronize back into 1 flow.</li>
    <li>Swimlanes = Group activities by role/department.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-26",
            "number": "26",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "State Machine",
            "subtitle": "Reactive Object Lifecycle, States, Events, Guards, Actions & Telephone Call Example",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Reactive Lifecycle</div>
    <h3>Meaning of State Machine Diagram</h3>
    <p>A <strong>State Machine Diagram</strong> (or <em>Statechart</em>) models the <strong>lifecycle of a single reactive object</strong> from creation to destruction. It specifies how an object transitions between discrete states in response to external events, signals, and internal conditions.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>State Machine Anatomy & Syntax</h4>

  <div class="detail-block">
    <h5>1. Core Concepts</h5>
    <ul>
      <li><strong>State:</strong> A condition or situation in the life of an object during which it satisfies some condition, performs an activity, or waits for an event. Rendered as a rounded rectangle.</li>
      <li><strong>Initial State (<code>●</code>):</strong> The default state upon object instantiation.</li>
      <li><strong>Final State (<code>◉</code>):</strong> Termination of the object's lifecycle.</li>
      <li><strong>Transition:</strong> A directed relationship between two states indicating movement.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Complete Transition Syntax</h5>
    <div class="code-box"><code>event-name (parameters) [guard-condition] / action-expression</code></div>
    <ul>
      <li><strong>Trigger Event:</strong> The occurrence that prompts the transition (e.g. <code>liftReceiver</code>).</li>
      <li><strong>Guard Condition:</strong> A boolean expression enclosed in square brackets <code>[...]</code>; transition occurs only if true.</li>
      <li><strong>Action:</strong> An atomic, uninterruptible calculation executed during the transition (e.g. <code>/ playDialTone()</code>).</li>
      <li><strong>Internal State Activities:</strong> <code>entry / action</code>, <code>exit / action</code>, <code>do / ongoingActivity</code>.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Classic AKTU Exam Scenario: Answering a Telephone Call</h5>
    <p>States: <code>Idle</code> &rarr; <code>Ringing</code> (on incoming call) &rarr; <code>Connected</code> (on pickup) &rarr; <code>Talking</code> &rarr; <code>Disconnected</code> (on hangup) &rarr; <code>Idle</code>.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Statechart Diagram for Answering a Telephone Call</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="stArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Start Node -->
      <circle cx="40" cy="110" r="10" class="uml-dark-shape" fill="#60a5fa"/>
      <line x1="50" y1="110" x2="85" y2="110" stroke="#2563eb" stroke-width="1.8" marker-end="url(#stArr)"/>

      <!-- State 1: Idle -->
      <g transform="translate(85, 85)">
        <rect width="100" height="50" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="50" y="30" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Idle</text>
      </g>

      <!-- Transition 1 -->
      <line x1="185" y1="110" x2="265" y2="110" stroke="#2563eb" stroke-width="1.8" marker-end="url(#stArr)"/>
      <text x="225" y="100" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">incomingCall / ring</text>

      <!-- State 2: Ringing -->
      <g transform="translate(265, 85)">
        <rect width="110" height="50" rx="8" fill="var(--card-bg)" stroke="#f59e0b" stroke-width="2"/>
        <text x="55" y="30" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Ringing</text>
      </g>

      <!-- Transition 2 -->
      <line x1="375" y1="110" x2="455" y2="110" stroke="#2563eb" stroke-width="1.8" marker-end="url(#stArr)"/>
      <text x="415" y="100" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">pickUp / connect</text>

      <!-- State 3: Connected / Talking -->
      <g transform="translate(455, 75)">
        <rect width="140" height="70" rx="8" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="70" y="25" text-anchor="middle" font-size="11" font-weight="bold" fill="#059669">Connected</text>
        <line x1="0" y1="35" x2="140" y2="35" stroke="#10b981"/>
        <text x="10" y="52" font-size="9" fill="var(--text-primary)">do / streamAudio()</text>
      </g>

      <!-- Transition 3: Hangup returning to Idle -->
      <path d="M 525 75 C 525 20, 135 20, 135 85" fill="none" stroke="#ef4444" stroke-width="1.8" marker-end="url(#stArr)"/>
      <text x="330" y="32" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">hangUp / terminateLine</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15):</strong> <em>"Define state machine. Draw a state machine diagram for answering a telephone call."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Label transitions with the complete standard syntax: <code>Event [Guard] / Action</code>. Ensure your diagram includes the return transition (hanging up returns phone to <code>Idle</code>).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>State Machine = Models lifecycle states of a single reactive object.</li>
    <li>State = Rounded rectangle | Initial = <code>●</code> | Final = <code>◉</code>.</li>
    <li>Transition syntax: <code>trigger [guard] / action</code>.</li>
    <li>State actions: <code>entry /</code>, <code>exit /</code>, <code>do /</code>.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-27",
            "number": "27",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Process and Thread",
            "subtitle": "Concurrency Foundations, Active Objects, Context Switching & Architectural Differences",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Concurrent Systems</div>
    <h3>Processes and Threads in Behavioral Modeling</h3>
    <p>Modern software systems rarely execute on a single linear execution thread. To model real-time responsiveness, multi-core hardware, and distributed microservices, UML integrates the operating system abstractions of <strong>Processes</strong> and <strong>Threads</strong> via <em>Active Objects</em>.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Deep Architectural Comparison: Process vs. Thread</h4>

  <div class="detail-block">
    <h5>1. Foundational Definitions</h5>
    <ul>
      <li><strong>Process:</strong> A heavyweight, independent execution unit that owns its own dedicated virtual memory space, file descriptors, and OS security credentials.</li>
      <li><strong>Thread:</strong> A lightweight unit of execution that resides <em>inside</em> a host process, sharing the memory heap, global variables, and open files with its sibling threads.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Systematic Comparison Matrix</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Criterion</th>
          <th>Process</th>
          <th>Thread</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Memory Address Space</strong></td>
          <td>Isolated memory space (safe from corruption by other processes)</td>
          <td>Shared address space (requires synchronization locks)</td>
        </tr>
        <tr>
          <td><strong>Weight & Overhead</strong></td>
          <td>Heavyweight (expensive creation, destruction, and context switching)</td>
          <td>Lightweight (cheap creation and fast CPU context switching)</td>
        </tr>
        <tr>
          <td><strong>Inter-Communication</strong></td>
          <td>IPC mechanisms (Sockets, Pipes, Shared Memory, Message Queues)</td>
          <td>Direct memory reference (Shared pointers, Mutexes, Semaphores)</td>
        </tr>
        <tr>
          <td><strong>Crash Impact</strong></td>
          <td>Failure in one process does not crash other processes</td>
          <td>An unhandled exception in one thread can terminate the entire process</td>
        </tr>
        <tr>
          <td><strong>UML Stereotype</strong></td>
          <td><code>&lt;&lt;process&gt;&gt;</code></td>
          <td><code>&lt;&lt;thread&gt;&gt;</code></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="detail-block">
    <h5>3. Active Objects in UML</h5>
    <p>An <strong>Active Object</strong> is an object that owns an independent thread of control and can initiate behavior autonomously. In UML, an active class is depicted as a standard class rectangle with <strong>double vertical lines on its left and right borders</strong>.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Process Address Space vs Multi-Threaded Process Architecture</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Process 1 Box -->
      <g transform="translate(40, 20)">
        <rect width="320" height="170" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect width="320" height="28" rx="8" fill="#3b82f6" fill-opacity="0.15"/>
        <text x="160" y="19" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">&lt;&lt;process&gt;&gt; WebServerProcess (PID: 4012)</text>
        <!-- Memory sections -->
        <rect x="15" y="40" width="135" height="110" rx="4" fill="var(--bg-secondary)" stroke="var(--border-color)"/>
        <text x="82" y="58" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Dedicated Heap &amp; Code</text>
        <text x="25" y="80" font-size="9" fill="var(--text-muted)">• Global variables</text>
        <text x="25" y="98" font-size="9" fill="var(--text-muted)">• Open file handles</text>
        <text x="25" y="116" font-size="9" fill="var(--text-muted)">• Network sockets</text>

        <!-- Threads inside -->
        <g transform="translate(165, 40)">
          <rect width="140" height="32" rx="3" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6"/>
          <text x="70" y="20" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;thread&gt;&gt; WorkerThread 1</text>
          <rect y="40" width="140" height="32" rx="3" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6"/>
          <text x="70" y="60" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;thread&gt;&gt; WorkerThread 2</text>
          <rect y="80" width="140" height="32" rx="3" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6"/>
          <text x="70" y="100" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;thread&gt;&gt; LoggerThread</text>
        </g>
      </g>

      <!-- Active Class UML Box (Right) -->
      <g transform="translate(430, 40)">
        <rect width="260" height="130" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <!-- Double vertical lines for Active Class -->
        <line x1="12" y1="0" x2="12" y2="130" stroke="#10b981" stroke-width="2"/>
        <line x1="248" y1="0" x2="248" y2="130" stroke="#10b981" stroke-width="2"/>
        <rect x="12" y="0" width="236" height="32" fill="#10b981" fill-opacity="0.15"/>
        <text x="130" y="21" text-anchor="middle" font-size="11" font-weight="bold" fill="#059669">TelemetryCollector</text>
        <line x1="12" y1="32" x2="248" y2="32" stroke="#10b981"/>
        <text x="25" y="55" font-size="10" fill="var(--text-primary)">- pollRate : int = 50ms</text>
        <line x1="12" y1="70" x2="248" y2="70" stroke="#10b981"/>
        <text x="25" y="92" font-size="10" fill="var(--text-primary)">+ run() : void</text>
        <text x="25" y="110" font-size="10" fill="var(--text-primary)">+ stopThread() : void</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Differentiate between process and thread in the context of behavioral modeling. How is an active class represented in UML?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Must-Draw:</strong> Draw the active class rectangle with <strong>double vertical border lines</strong> on the left and right edges! Explain that active objects own their own thread of control.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Process = Heavyweight, isolated memory space, owns resources.</li>
    <li>Thread = Lightweight execution unit inside a process, shares heap.</li>
    <li>Active Object = Box with double vertical border lines (runs its own thread).</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-28",
            "number": "28",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Events and Signals",
            "subtitle": "Stimuli Triggers, Signal Hierarchies, Call/Time/Change Events & State Transitions",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Stimulus Modeling</div>
    <h3>Meaning of Events and Signals</h3>
    <p>An <strong>Event</strong> is the specification of a significant occurrence in time and space that has no duration and can trigger a state transition or dynamic execution. A <strong>Signal</strong> is an asynchronous package of data transmitted between objects.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The Four Fundamental UML Event Types</h4>

  <div class="detail-block">
    <h5>1. The 4 Kinds of Events in UML</h5>
    <div class="two-col-cards">
      <div class="feature-card">
        <div class="col-head blue-head">1. Call Event</div>
        <p>Represents the dispatch of an operation on an object. Often synchronous: caller waits for return value.</p>
        <p><em>Syntax:</em> <code>depositFunds(accountNo, amount)</code></p>
      </div>

      <div class="feature-card">
        <div class="col-head green-head">2. Signal Event</div>
        <p>Represents the receipt of an asynchronous signal entity. Signals are first-class classifiers adorned with <code>&lt;&lt;signal&gt;&gt;</code>.</p>
        <p><em>Syntax:</em> <code>PowerFailureSignal</code></p>
      </div>

      <div class="feature-card">
        <div class="col-head purple-head">3. Time Event</div>
        <p>Represents the expiration of a specific time duration or the arrival of a scheduled deadline.</p>
        <p><em>Syntax:</em> <code>after (30 seconds)</code> or <code>at (12:00 AM)</code></p>
      </div>

      <div class="feature-card">
        <div class="col-head red-head">4. Change Event</div>
        <p>Represents the satisfaction of a continuous boolean condition.</p>
        <p><em>Syntax:</em> <code>when (temperature &gt; 120°C)</code></p>
      </div>
    </div>
  </div>

  <div class="detail-block">
    <h5>2. Signal Communication and Classifiers</h5>
    <p>Signals can be structured in inheritance hierarchies. For example, <code>HardwareErrorSignal</code> can generalize into <code>DiskError</code> and <code>MemoryParityError</code>. Subclasses inherit all parameters of parent signals.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: The Four Event Types Triggering State Transitions</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="evArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Center State -->
      <g transform="translate(300, 75)">
        <rect width="160" height="60" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="80" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">Operational State</text>
      </g>

      <!-- Event 1: Call Event (Left) -->
      <line x1="80" y1="85" x2="295" y2="85" stroke="#2563eb" stroke-width="1.8" marker-end="url(#evArr)"/>
      <text x="180" y="75" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">1. Call: startProcess(data)</text>

      <!-- Event 2: Signal Event (Top) -->
      <line x1="380" y1="15" x2="380" y2="70" stroke="#10b981" stroke-width="1.8" marker-end="url(#evArr)"/>
      <text x="470" y="40" font-size="10" font-weight="bold" fill="#059669">2. Signal: &lt;&lt;signal&gt;&gt; Interrupt</text>

      <!-- Event 3: Time Event (Right) -->
      <line x1="680" y1="105" x2="465" y2="105" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#evArr)"/>
      <text x="565" y="95" text-anchor="middle" font-size="10" font-weight="bold" fill="#d97706">3. Time: after(60 sec)</text>

      <!-- Event 4: Change Event (Bottom) -->
      <line x1="380" y1="195" x2="380" y2="140" stroke="#ef4444" stroke-width="1.8" marker-end="url(#evArr)"/>
      <text x="485" y="175" font-size="10" font-weight="bold" fill="#dc2626">4. Change: when(volts &lt; 3.0V)</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"What is an event? Name and explain the different types of events recognized in UML with syntax."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Formula:</strong> Write down all 4 types with exact syntax: Call event <code>op()</code>, Signal event <code>SignalName</code>, Time event <code>after(...)</code>, and Change event <code>when(...)</code>.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Event = Occurrence in time triggering a transition.</li>
    <li>Signal = Asynchronous package of data sent between objects.</li>
    <li>4 Types: Call, Signal, Time (<code>after</code>), Change (<code>when</code>).</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-29",
            "number": "29",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Time Diagram",
            "subtitle": "Timing Diagrams, Real-Time Duration Constraints, State Waveforms & Embedded Systems",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Real-Time Interaction</div>
    <h3>Meaning of Time Diagram (Timing Diagram)</h3>
    <p>A <strong>Time Diagram</strong> (officially <em>Timing Diagram</em>) is an interaction diagram that models the <strong>exact change in state or condition of an object along a calibrated, continuous time axis</strong>.</p>
    <p>While sequence diagrams show the qualitative order of messages, timing diagrams model quantitative durations, response latencies, and clock intervals.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Real-Time Utility</h4>

  <div class="detail-block">
    <h5>1. Key Structural Elements</h5>
    <ul>
      <li><strong>Horizontal Time Axis:</strong> Calibrated with explicit time units (microseconds, milliseconds, or clock cycles).</li>
      <li><strong>Lifeline / State Tracks:</strong> Displays discrete state levels (e.g., Idle, Busy, Transmitting) as stepped waveform lines.</li>
      <li><strong>State Transitions:</strong> Stepped transitions rising or falling from one state level to another.</li>
      <li><strong>Duration Constraints:</strong> Mathematical limits (e.g. <code>{t..t+10ms}</code>) specifying strict real-time deadlines.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Utility in System Design</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Application Area</th>
          <th>Engineering Importance</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Embedded & Automotive Systems</strong></td>
          <td>Verifies sensor read deadlines and airbag deployment latencies (&lt; 20ms).</td>
        </tr>
        <tr>
          <td><strong>Digital Electronics & ASIC Design</strong></td>
          <td>Models clock jitter, setup/hold times, and bus bus-arbitration protocols.</td>
        </tr>
        <tr>
          <td><strong>Distributed Telecommunications</strong></td>
          <td>Ensures packet timeout retransmission limits and handshake validity windows.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Timing Diagram Waveform with Duration Constraint</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Time Axis -->
      <line x1="80" y1="160" x2="680" y2="160" stroke="#64748b" stroke-width="2"/>
      <text x="680" y="180" font-size="11" font-weight="bold" fill="#64748b">Time (ms) →</text>
      <!-- Time Ticks -->
      <line x1="120" y1="155" x2="120" y2="165" stroke="#64748b"/>
      <text x="120" y="178" text-anchor="middle" font-size="9" fill="var(--text-muted)">0ms</text>
      <line x1="260" y1="155" x2="260" y2="165" stroke="#64748b"/>
      <text x="260" y="178" text-anchor="middle" font-size="9" fill="var(--text-muted)">10ms</text>
      <line x1="420" y1="155" x2="420" y2="165" stroke="#64748b"/>
      <text x="420" y="178" text-anchor="middle" font-size="9" fill="var(--text-muted)">25ms</text>
      <line x1="600" y1="155" x2="600" y2="165" stroke="#64748b"/>
      <text x="600" y="178" text-anchor="middle" font-size="9" fill="var(--text-muted)">40ms</text>

      <!-- State Labels (Vertical) -->
      <text x="70" y="70" text-anchor="end" font-size="10" font-weight="bold" fill="#2563eb">Active</text>
      <text x="70" y="125" text-anchor="end" font-size="10" font-weight="bold" fill="#64748b">Idle</text>

      <!-- Grid lines -->
      <line x1="80" y1="65" x2="680" y2="65" stroke="#cbd5e1" stroke-dasharray="3,3"/>
      <line x1="80" y1="120" x2="680" y2="120" stroke="#cbd5e1" stroke-dasharray="3,3"/>

      <!-- Waveform Line -->
      <path d="M 80 120 L 260 120 L 260 65 L 420 65 L 420 120 L 680 120" fill="none" stroke="#2563eb" stroke-width="2.5"/>

      <!-- Duration Constraint annotation -->
      <line x1="260" y1="45" x2="420" y2="45" stroke="#ef4444" stroke-width="1.5"/>
      <line x1="260" y1="40" x2="260" y2="50" stroke="#ef4444" stroke-width="1.5"/>
      <line x1="420" y1="40" x2="420" y2="50" stroke="#ef4444" stroke-width="1.5"/>
      <text x="340" y="38" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">{duration &lt;= 15ms}</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11):</strong> <em>"Write a short note on time diagram with suitable diagram and its utility in system design."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Distinction:</strong> Contrast Time Diagrams with Sequence Diagrams: Sequence diagrams show chronological message order without scale; Time diagrams map exact state transitions against calibrated physical time.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Time Diagram = Visualizes exact object state changes along a time axis.</li>
    <li>Includes horizontal time scale, state levels, waveforms, and duration constraints.</li>
    <li>Vital for embedded, real-time, and telecommunication systems.</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-30",
            "number": "30",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Interaction Diagram",
            "subtitle": "Collective Interaction Modeling, Sequence vs Communication vs Timing Overview",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Interaction Family</div>
    <h3>Meaning of Interaction Diagrams</h3>
    <p>In UML, <strong>Interaction Diagram</strong> is the umbrella category for diagrams that capture <strong>dynamic message-passing behavior among collaborating objects</strong>. They visualize how a group of objects achieve a common goal.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The Four Standard Interaction Diagrams</h4>

  <div class="detail-block">
    <h5>Comprehensive Matrix of Interaction Diagrams</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Interaction Diagram</th>
          <th>Primary Structural Dimension</th>
          <th>Best Architectural Usage</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Sequence Diagram</strong></td>
          <td>Chronological time sequence (Top to bottom)</td>
          <td>Visualizing use case execution flows, API request-response lifecycles.</td>
        </tr>
        <tr>
          <td><strong>2. Communication / Collaboration</strong></td>
          <td>Structural topology & links between objects</td>
          <td>Analyzing localized subsystem clusters, network hops, and object coupling.</td>
        </tr>
        <tr>
          <td><strong>3. Timing Diagram</strong></td>
          <td>Continuous time axis & state waveforms</td>
          <td>Real-time firmware, embedded sensor control, protocol timeout compliance.</td>
        </tr>
        <tr>
          <td><strong>4. Interaction Overview Diagram</strong></td>
          <td>High-level flow of control enclosing sequence frames</td>
          <td>Decomposing large complex business workflows into smaller modular interaction frames.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: The Interaction Diagram Quadrant</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <rect x="40" y="20" width="320" height="75" rx="6" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.8"/>
      <text x="55" y="42" font-size="12" font-weight="bold" fill="#2563eb">1. Sequence Diagram</text>
      <text x="55" y="62" font-size="10" fill="var(--text-muted)">Focus: Strict chronological message order along vertical lifelines.</text>

      <rect x="400" y="20" width="320" height="75" rx="6" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.8"/>
      <text x="415" y="42" font-size="12" font-weight="bold" fill="#059669">2. Communication Diagram</text>
      <text x="415" y="62" font-size="10" fill="var(--text-muted)">Focus: Spatial links and numbered message arrows across object clusters.</text>

      <rect x="40" y="115" width="320" height="75" rx="6" fill="var(--card-bg)" stroke="#f59e0b" stroke-width="1.8"/>
      <text x="55" y="137" font-size="12" font-weight="bold" fill="#d97706">3. Timing Diagram</text>
      <text x="55" y="157" font-size="10" fill="var(--text-muted)">Focus: Explicit time axis, state waveforms, and millisecond duration limits.</text>

      <rect x="400" y="115" width="320" height="75" rx="6" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="1.8"/>
      <text x="415" y="137" font-size="12" font-weight="bold" fill="#7c3aed">4. Interaction Overview Diagram</text>
      <text x="415" y="157" font-size="10" fill="var(--text-muted)">Focus: Activity diagram nodes that enclose complete nested sequence diagrams.</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>Short Question:</strong> <em>"What is an interaction diagram? List all diagrams that belong to the interaction family."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Scoring Tip:</strong> Mention that Sequence and Communication diagrams are semantically isomorphic, and explicitly list all 4 members of the family.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Interaction diagrams = Model dynamic message passing among objects.</li>
    <li>4 types: Sequence (Time), Communication (Space/Links), Timing (Duration), Interaction Overview (Hybrid).</li>
  </ul>
</div>
"""
        },
        {
            "id": "sec-31",
            "number": "31",
            "part": "Part 5 — Basic Behavioural Modeling",
            "title": "Package Diagram",
            "subtitle": "Modular Namespaces, Layered Subsystems, Dependencies & Large-Scale System Organization",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Modular Architecture</div>
    <h3>Meaning of Package and Package Diagram</h3>
    <p>A <strong>Package</strong> is a general-purpose grouping mechanism used to organize UML elements (classes, interfaces, use cases, components) into high-level, manageable, modular namespaces. A <strong>Package Diagram</strong> depicts the dependencies and hierarchical relationships among these subsystems.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Package Notation and Architectural Dependencies</h4>

  <div class="detail-block">
    <h5>1. Package Notation</h5>
    <p>Represented as a <strong>tabbed folder icon</strong>. The package name can appear inside the tab (if content elements are drawn inside the folder body) or centered in the folder body (if elements are omitted).</p>
  </div>

  <div class="detail-block">
    <h5>2. Package Stereotyped Dependencies</h5>
    <ul>
      <li><code>&lt;&lt;import&gt;&gt;</code>: Adds the public contents of the target package into the source package's public namespace.</li>
      <li><code>&lt;&lt;access&gt;&gt;</code>: Adds the contents into the source package's private namespace.</li>
      <li><code>&lt;&lt;merge&gt;&gt;</code>: Combines the contents of two packages.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Uses in Large-Scale Enterprise Systems</h5>
    <ul>
      <li><strong>Structuring High-Level Subsystems:</strong> Enforces architectural patterns like 3-Tier Layering (UI Layer &rarr; Business Logic &rarr; Data Access).</li>
      <li><strong>Managing Namespace Collisions:</strong> Encapsulates common class names (e.g. <code>ui::Button</code> vs <code>hardware::Button</code>).</li>
      <li><strong>Preventing Cyclic Dependencies:</strong> Enforces unidirectional dependency flows across enterprise libraries.</li>
    </ul>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: 3-Tier Enterprise Architecture Package Diagram</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="pkgArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Package 1: Presentation Tier -->
      <g transform="translate(40, 60)">
        <path d="M 0 15 L 0 90 L 170 90 L 170 15 L 70 15 L 60 0 L 0 0 Z" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="35" y="11" font-size="9" font-weight="bold" fill="#2563eb">Presentation</text>
        <text x="85" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">UI Layer</text>
        <text x="85" y="72" text-anchor="middle" font-size="9" fill="var(--text-muted)">Controllers, Views</text>
      </g>

      <!-- Dependency: UI -> Business -->
      <line x1="210" y1="105" x2="280" y2="105" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#pkgArr)"/>
      <text x="245" y="95" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;import&gt;&gt;</text>

      <!-- Package 2: Business Tier -->
      <g transform="translate(290, 60)">
        <path d="M 0 15 L 0 90 L 180 90 L 180 15 L 70 15 L 60 0 L 0 0 Z" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="35" y="11" font-size="9" font-weight="bold" fill="#059669">BusinessLogic</text>
        <text x="90" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Domain Services</text>
        <text x="90" y="72" text-anchor="middle" font-size="9" fill="var(--text-muted)">Billing, OrderEngine</text>
      </g>

      <!-- Dependency: Business -> DataAccess -->
      <line x1="470" y1="105" x2="540" y2="105" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#pkgArr)"/>
      <text x="505" y="95" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">&lt;&lt;import&gt;&gt;</text>

      <!-- Package 3: Data Tier -->
      <g transform="translate(550, 60)">
        <path d="M 0 15 L 0 90 L 170 90 L 170 15 L 70 15 L 60 0 L 0 0 Z" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="2"/>
        <text x="35" y="11" font-size="9" font-weight="bold" fill="#7c3aed">DataAccess</text>
        <text x="85" y="55" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Persistence</text>
        <text x="85" y="72" text-anchor="middle" font-size="9" fill="var(--text-muted)">Repositories, DB</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14):</strong> <em>"Define package. Explain the package diagram with suitable examples and discuss its uses."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Blueprint:</strong> Draw the classic <strong>tabbed folder symbol</strong>. Mention that packages control namespace visibility and structure multi-tier architectures without cyclic dependencies.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Package = Tabbed folder icon for grouping elements into namespaces.</li>
    <li>Relationships: <code>&lt;&lt;import&gt;&gt;</code> (public), <code>&lt;&lt;access&gt;&gt;</code> (private), <code>&lt;&lt;merge&gt;&gt;</code>.</li>
    <li>Uses: Layered enterprise architecture, managing complexity, modularity.</li>
  </ul>
</div>
"""
        }
    ]
