# generate_unit3_part1.py: Part 1 - Object-Oriented Analysis & Design (Sections 1 to 11)

def get_unit3_part1_sections():
    return [
        {
            "id": "u3-sec-1",
            "number": "01",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Object-Oriented Analysis (OOA)",
            "subtitle": "Problem Domain Understanding, Identifying Real-World Objects & System Requirements",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Analysis Phase</div>
    <h3>Meaning & Purpose of Object-Oriented Analysis (OOA)</h3>
    <p><strong>Object-Oriented Analysis (OOA)</strong> is the initial formal phase of the software engineering lifecycle where developers examine the <em>problem domain</em> to understand <strong>WHAT</strong> the system must do, without considering <em>how</em> it will be implemented in code, databases, or operating systems.</p>
    <p>The goal is to discover real-world entities (objects), capture user requirements via Use Cases, and construct a conceptual model that faithfully mirrors the customer's actual business domain.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Detective Investigating a Crime Scene</div>
  <p>Imagine a detective arriving at a crime scene. The detective does not immediately build a jail cell or forge handcuffs (that is implementation). Instead, the detective interviews eyewitnesses, identifies key people involved (suspect, victim, witness), lists what happened (events), and records their relationships. <strong>That is OOA</strong>: understanding the facts and rules of the world before designing the technical solution.</p>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Analysis Steps</h4>

  <div class="detail-block">
    <h5>1. Identifying & Organizing Objects</h5>
    <p>Objects are identified from the user's requirements description using the grammatical noun-extraction approach:</p>
    <ul>
      <li><strong>Domain Entities (Nouns):</strong> E.g., in a Banking system: <code>Customer</code>, <code>Account</code>, <code>Transaction</code>.</li>
      <li><strong>Object Attributes:</strong> Properties describing entity state (e.g., <code>accountNumber</code>, <code>balance</code>).</li>
      <li><strong>Object Behaviors & Actions:</strong> Services requested from objects (e.g., <code>deposit()</code>, <code>withdraw()</code>).</li>
      <li><strong>Object Interactions:</strong> How entities exchange messages to satisfy business use cases.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Use Cases and Object Models</h5>
    <p>Use cases model user interactions from the outside; OOA translates those use cases into conceptual object models containing classes, attributes, associations, and state charts.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Domain Concept (OOA Analysis Model)</span>
    <span class="code-desc">Simple representation of domain entities identified during Analysis</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">// OOA Focus: Capturing "WHAT" exists in the problem domain</span>
<span class="c-comment">// No technical concerns yet (no SQL, no socket networking, no GUI)</span>

<span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">BankAccount</span> {
<span class="c-keyword">private:</span>
    <span class="c-comment">// Attributes identified from domain requirements</span>
    std::string accountNumber;  <span class="c-comment">// Unique identifier for the account</span>
    <span class="c-type">double</span> balance;             <span class="c-comment">// Current monetary balance</span>

<span class="c-keyword">public:</span>
    <span class="c-comment">// Constructor: Initializes real-world state</span>
    BankAccount(std::string accNo, <span class="c-type">double</span> initialDeposit) {
        accountNumber = accNo;
        balance = initialDeposit;
    }

    <span class="c-comment">// Domain Operation: Depositing money increases balance</span>
    <span class="c-type">void</span> deposit(<span class="c-type">double</span> amount) {
        <span class="c-keyword">if</span> (amount &gt; 0) {
            balance += amount;  <span class="c-comment">// State change</span>
            std::cout &lt;&lt; <span class="c-string">"Deposited: $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">" | New Balance: $"</span> &lt;&lt; balance &lt;&lt; std::endl;
        }
    }

    <span class="c-comment">// Domain Operation: Withdrawing money with business rule validation</span>
    <span class="c-type">bool</span> withdraw(<span class="c-type">double</span> amount) {
        <span class="c-comment">// Rule: Cannot withdraw more than existing balance</span>
        <span class="c-keyword">if</span> (amount &gt; 0 &amp;&amp; balance &gt;= amount) {
            balance -= amount;
            std::cout &lt;&lt; <span class="c-string">"Withdrawn: $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">" | Remaining: $"</span> &lt;&lt; balance &lt;&lt; std::endl;
            <span class="c-keyword">return</span> <span class="c-keyword">true</span>;
        }
        std::cout &lt;&lt; <span class="c-string">"Transaction Rejected: Insufficient balance!"</span> &lt;&lt; std::endl;
        <span class="c-keyword">return</span> <span class="c-keyword">false</span>;
    }
};</code></pre>
</div>

<div class="diagram-container">
  <h4>Visual Model: Object-Oriented Analysis (Problem Domain &rarr; Conceptual Model)</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ooaArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>
      <!-- Real World Problem Domain -->
      <g transform="translate(40, 25)">
        <rect width="200" height="150" rx="8" fill="var(--bg-card)" stroke="#2a3a56" stroke-width="2"/>
        <rect width="200" height="32" rx="8" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="100" y="21" text-anchor="middle" font-size="11" font-weight="bold" fill="#38bdf8">Real-World Problem Domain</text>
        <text x="20" y="55" font-size="11" fill="var(--text-primary)">• Business Requirements</text>
        <text x="20" y="78" font-size="11" fill="var(--text-primary)">• End-User Workflows</text>
        <text x="20" y="101" font-size="11" fill="var(--text-primary)">• Real Entities (Nouns)</text>
        <text x="20" y="124" font-size="11" fill="var(--text-muted)">• Informal Problem Statement</text>
      </g>

      <!-- Processing Arrow -->
      <line x1="250" y1="100" x2="330" y2="100" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#ooaArr)"/>
      <text x="290" y="90" text-anchor="middle" font-size="9" font-weight="bold" fill="#38bdf8">OOA Process</text>

      <!-- Analysis Model -->
      <g transform="translate(340, 25)">
        <rect width="380" height="150" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="2"/>
        <rect width="380" height="32" rx="8" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="190" y="21" text-anchor="middle" font-size="11" font-weight="bold" fill="#34d399">OOA Analysis Model (Conceptual)</text>
        
        <rect x="20" y="48" width="105" height="85" rx="4" fill="var(--bg-surface)" stroke="#38bdf8"/>
        <text x="72" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Object Model</text>
        <text x="72" y="86" text-anchor="middle" font-size="9" fill="var(--text-muted)">Classes &amp; Props</text>
        <text x="72" y="102" text-anchor="middle" font-size="9" fill="var(--text-muted)">Associations</text>

        <rect x="135" y="48" width="105" height="85" rx="4" fill="var(--bg-surface)" stroke="#f59e0b"/>
        <text x="187" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Dynamic Model</text>
        <text x="187" y="86" text-anchor="middle" font-size="9" fill="var(--text-muted)">States &amp; Events</text>
        <text x="187" y="102" text-anchor="middle" font-size="9" fill="var(--text-muted)">State Transitions</text>

        <rect x="250" y="48" width="110" height="85" rx="4" fill="var(--bg-surface)" stroke="#a855f7"/>
        <text x="305" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">Functional Model</text>
        <text x="305" y="86" text-anchor="middle" font-size="9" fill="var(--text-muted)">DFD Computations</text>
        <text x="305" y="102" text-anchor="middle" font-size="9" fill="var(--text-muted)">Data Transformations</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"What is Object-Oriented Analysis? Discuss the steps involved in identifying and organizing objects."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Always highlight that OOA answers <strong>"WHAT the system does"</strong> while OOD answers <strong>"HOW the system does it"</strong>. Mention noun analysis for discovering candidate classes and use case modeling for interactions.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>OOA = Focuses on the problem domain ("WHAT"), not technical implementation.</li>
    <li>Identifies: Objects, Attributes, Operations, Associations, and Use Cases.</li>
    <li>Produces the conceptual Object Model, Dynamic Model, and Functional Model.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-2",
            "number": "02",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Object-Oriented Design (OOD)",
            "subtitle": "Solution Domain Mapping, Interface Design, Data Restructuring & Control Implementation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Design Phase</div>
    <h3>Meaning of Object-Oriented Design (OOD)</h3>
    <p><strong>Object-Oriented Design (OOD)</strong> is the phase where the <em>conceptual analysis model</em> is shifted into the <strong>solution domain</strong>. It specifies <strong>HOW</strong> the system will be built—incorporating programming language constraints, data structure selections, database schemas, network protocols, and execution concurrency.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Architect Drawing Construction Blueprints</div>
  <p>If OOA was the client explaining: <em>"I want a 3-bedroom house with an open kitchen"</em>, then <strong>OOD is the civil engineer drafting the load-bearing calculations</strong>: deciding whether to use reinforced concrete or steel beams, where the plumbing pipes run, electrical circuit wiring, and concrete grades. OOD addresses real physical constraints!</p>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Design Activities</h4>

  <div class="detail-block">
    <h5>1. Mapping Analysis Model to Implementation</h5>
    <p>OOD takes pure domain abstractions and augments them with software engineering constructs:</p>
    <ul>
      <li><strong>Implementing Classes:</strong> Deciding primitive vs complex types, container libraries (e.g. <code>std::vector</code>, <code>HashMap</code>).</li>
      <li><strong>Identifying Constraints:</strong> Speed bottlenecks, memory limits, database transaction atomicity.</li>
      <li><strong>Designing Interfaces:</strong> Specifying public method signatures, error return codes, and exception types.</li>
      <li><strong>Restructuring Class Data:</strong> Normalizing attributes or adding cached helper variables for performance.</li>
      <li><strong>Implementation of Associations:</strong> Choosing between raw pointers, reference counting, or dedicated association tables.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Comparison: OOA (Analysis) vs. OOD (Design)</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Criterion</th>
          <th>Object-Oriented Analysis (OOA)</th>
          <th>Object-Oriented Design (OOD)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Core Question</strong></td>
          <td><em>"WHAT must the system do?"</em></td>
          <td><em>"HOW will the software do it?"</em></td>
        </tr>
        <tr>
          <td><strong>Domain</strong></td>
          <td>Problem Domain (Real-world concepts)</td>
          <td>Solution Domain (Technical implementation)</td>
        </tr>
        <tr>
          <td><strong>Focus</strong></td>
          <td>Business entities, user goals, requirements</td>
          <td>Data structures, algorithms, DB queries, threads</td>
        </tr>
        <tr>
          <td><strong>Language Dependency</strong></td>
          <td>Completely language-independent</td>
          <td>Tailored to target language (C++, Java, Python)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Implementation Model (OOD Solution Domain)</span>
    <span class="code-desc">Adding technical solution details (Mutex thread safety, Transaction logs, Exception handling)</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">// OOD Focus: Addressing technical solution domain constraints</span>
<span class="c-comment">// Adding Thread-Safety (Mutex) and Error Logging</span>

<span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;mutex&gt;</span>      <span class="c-comment">// Solution domain: Concurrency protection</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>     <span class="c-comment">// Solution domain: Container for transaction audit log</span>

<span class="c-keyword">class</span> <span class="c-type">SecureBankAccount</span> {
<span class="c-keyword">private:</span>
    std::string accountNumber;
    <span class="c-type">double</span> balance;
    std::mutex accountLock;             <span class="c-comment">// OOD addition: Thread-safety mechanism</span>
    std::vector&lt;std::string&gt; auditLog;  <span class="c-comment">// OOD addition: Persistence &amp; auditing log</span>

<span class="c-keyword">public:</span>
    SecureBankAccount(std::string accNo, <span class="c-type">double</span> initialDeposit) 
        : accountNumber(accNo), balance(initialDeposit) {}

    <span class="c-comment">// Thread-safe withdrawal implementation</span>
    <span class="c-type">bool</span> withdraw(<span class="c-type">double</span> amount) {
        <span class="c-comment">// Lock the mutex to prevent race conditions across concurrent threads</span>
        std::lock_guard&lt;std::mutex&gt; lock(accountLock);

        <span class="c-keyword">if</span> (amount &gt; 0 &amp;&amp; balance &gt;= amount) {
            balance -= amount;
            auditLog.push_back(<span class="c-string">"SUCCESS: Withdrew $"</span> + std::to_string(amount));
            <span class="c-keyword">return</span> <span class="c-keyword">true</span>;
        } <span class="c-keyword">else</span> {
            auditLog.push_back(<span class="c-string">"FAILED: Insufficient funds for $"</span> + std::to_string(amount));
            <span class="c-keyword">return</span> <span class="c-keyword">false</span>;
        }
    }
};</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Problem Domain to Solution Domain Mapping</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 260" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      <!-- Problem Domain (Left) -->
      <rect x="40" y="30" width="260" height="200" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="170" y="60" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Problem Domain (OOA)</text>
      <rect x="60" y="80" width="220" height="35" rx="4" fill="#0369a1"/>
      <text x="170" y="102" fill="#ffffff" font-size="11" text-anchor="middle">Real-World Customer Entity</text>
      <rect x="60" y="125" width="220" height="35" rx="4" fill="#0369a1"/>
      <text x="170" y="147" fill="#ffffff" font-size="11" text-anchor="middle">Business Bank Account</text>
      <rect x="60" y="170" width="220" height="35" rx="4" fill="#0369a1"/>
      <text x="170" y="192" fill="#ffffff" font-size="11" text-anchor="middle">Deposit / Withdraw Rules</text>

      <!-- Mapping Arrow -->
      <path d="M 315 130 L 405 130" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6" marker-end="url(#ood-map-arrow)"/>
      <text x="360" y="118" fill="#60a5fa" font-size="11" font-weight="bold" text-anchor="middle">OOD Mapping</text>

      <!-- Solution Domain (Right) -->
      <rect x="420" y="30" width="380" height="200" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="610" y="60" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Solution Domain (OOD Implementation)</text>
      <rect x="440" y="80" width="340" height="32" rx="4" fill="#065f46"/>
      <text x="610" y="101" fill="#ffffff" font-size="10" text-anchor="middle">Data Structures: std::vector, Hash Indices</text>
      <rect x="440" y="120" width="340" height="32" rx="4" fill="#065f46"/>
      <text x="610" y="141" fill="#ffffff" font-size="10" text-anchor="middle">Concurrency: std::mutex Thread-Safety Locks</text>
      <rect x="440" y="160" width="340" height="32" rx="4" fill="#065f46"/>
      <text x="610" y="181" fill="#ffffff" font-size="10" text-anchor="middle">Persistence: SQL ACID Transaction Logging</text>

      <defs>
        <marker id="ood-map-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Differentiate between Object-Oriented Analysis (OOA) and Object-Oriented Design (OOD). How is the analysis model mapped to the implementation domain?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Scoring Guide:</strong> Draw the 2-column comparison table above. Mention that OOD introduces solution-domain artifacts: thread safety, persistence, data structures, and concrete algorithms.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>OOD = Translates the conceptual analysis model into technical software architecture ("HOW").</li>
    <li>Deals with: Data structures, concrete algorithms, thread synchronization, and associations.</li>
    <li>Bridges the gap between domain rules and raw computer execution.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-3",
            "number": "03",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Object Design",
            "subtitle": "Designing Identified Objects, Mapping Domain Concepts to Computer Concepts & Trade-offs",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Object Design</div>
    <h3>Meaning of Object Design</h3>
    <p><strong>Object Design</strong> is the detailed design phase where the high-level classes identified during analysis are refined into <strong>concrete implementation specifications</strong>. In this stage, application-domain concepts are mapped onto computer-domain concepts (memory pointers, arrays, hash tables, CPU loops).</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Custom Tailor</div>
  <p>During analysis, you told a tailor: <em>"I need a warm winter coat"</em> (concept). During <strong>Object Design</strong>, the tailor chooses the exact fabric (wool vs fleece), the thread count, zipper mechanism, and internal lining thickness to balance cost, warmth, and durability. You are finalizing the internal anatomy of the product.</p>
</div>

<div class="subtopics-container">
  <h4>Key Engineering Considerations in Object Design</h4>

  <div class="three-col-cards">
    <div class="feature-card">
      <div class="col-head blue-head">1. Execution-Time Considerations</div>
      <p>Choosing algorithms and lookup structures to minimize CPU cycles (e.g. replacing an O(N) linked-list search with an O(1) hash map).</p>
    </div>

    <div class="feature-card">
      <div class="col-head green-head">2. Memory-Consumption Considerations</div>
      <p>Minimizing memory footprint: packing bit flags, reusing objects via object pools, and preventing memory leaks.</p>
    </div>

    <div class="feature-card">
      <div class="col-head purple-head">3. Overall-Cost Considerations</div>
      <p>Balancing development effort, code readability, maintenance costs, and hardware hosting expenses.</p>
    </div>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Example: Mapping Domain Concept to Computer Concept</span>
    <span class="code-desc">A 'Student Record Roster' (Domain) mapped to a fast Hash Map with O(1) lookup (Computer Concept)</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">// Domain Concept: "A School has a Directory of registered Students"</span>
<span class="c-comment">// Object Design Decision: Use std::unordered_map for O(1) average lookup time</span>

<span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;unordered_map&gt;</span>  <span class="c-comment">// Computer concept: Hash table structure</span>

<span class="c-keyword">struct</span> <span class="c-type">Student</span> {
    std::string name;
    <span class="c-type">double</span> gpa;
};

<span class="c-keyword">class</span> <span class="c-type">StudentDirectory</span> {
<span class="c-keyword">private:</span>
    <span class="c-comment">// Map Roll Number (int) to Student record</span>
    std::unordered_map&lt;<span class="c-type">int</span>, Student&gt; studentTable;

<span class="c-keyword">public:</span>
    <span class="c-comment">// Add student in O(1) time</span>
    <span class="c-type">void</span> registerStudent(<span class="c-type">int</span> rollNo, std::string name, <span class="c-type">double</span> gpa) {
        studentTable[rollNo] = {name, gpa};
    }

    <span class="c-comment">// Find student in O(1) time instead of O(N) linear scanning</span>
    <span class="c-type">void</span> searchStudent(<span class="c-type">int</span> rollNo) {
        <span class="c-keyword">auto</span> it = studentTable.find(rollNo);
        <span class="c-keyword">if</span> (it != studentTable.end()) {
            std::cout &lt;&lt; <span class="c-string">"Found: "</span> &lt;&lt; it-&gt;second.name &lt;&lt; <span class="c-string">" (GPA: "</span> &lt;&lt; it-&gt;second.gpa &lt;&lt; <span class="c-string">")\n"</span>;
        } <span class="c-keyword">else</span> {
            std::cout &lt;&lt; <span class="c-string">"Student with ID "</span> &lt;&lt; rollNo &lt;&lt; <span class="c-string">" not found.\n"</span>;
        }
    }
};</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Object Detail Elaboration Process</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 260" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      <!-- Conceptual Object (Left) -->
      <rect x="50" y="40" width="240" height="170" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="50" y="40" width="240" height="35" rx="8" fill="#0284c7"/>
      <text x="170" y="62" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Conceptual Class (Analysis)</text>
      <text x="70" y="105" fill="#f8fafc" font-size="11" font-weight="bold">Account</text>
      <text x="70" y="130" fill="#94a3b8" font-size="10">• accountNumber: string</text>
      <text x="70" y="150" fill="#94a3b8" font-size="10">• balance: real</text>
      <text x="70" y="180" fill="#38bdf8" font-size="10">+ withdraw(amount)</text>

      <!-- Elaboration Transition -->
      <path d="M 310 125 L 415 125" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#obj-elab-arrow)"/>
      <text x="362" y="112" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Elaborate Details</text>

      <!-- Concrete Implementation Class (Right) -->
      <rect x="430" y="30" width="370" height="195" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <rect x="430" y="30" width="370" height="32" rx="8" fill="#065f46"/>
      <text x="615" y="52" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Elaborated Class (Object Design)</text>
      <text x="450" y="85" fill="#a7f3d0" font-size="10">• - accountNumber: std::string (UUIDv4)</text>
      <text x="450" y="103" fill="#a7f3d0" font-size="10">• - balanceInCents: int64_t (Avoid floating point errors)</text>
      <text x="450" y="121" fill="#f59e0b" font-size="10">• - mtx: std::mutex (Thread safety lock)</text>
      <text x="450" y="139" fill="#f59e0b" font-size="10">• - cachedFee: double (Optimization variable)</text>
      <line x1="440" y1="150" x2="790" y2="150" stroke="#334155" stroke-width="1"/>
      <text x="450" y="170" fill="#38bdf8" font-size="10">+ withdraw(amount: double): bool</text>
      <text x="450" y="190" fill="#94a3b8" font-size="10">- internalValidateLimits(): bool (Private helper)</text>

      <defs>
        <marker id="obj-elab-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12):</strong> <em>"Write a short note on Object Design. What trade-offs must an engineer balance during object design?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Explicitly mention the three engineering trade-offs: <strong>Execution Time</strong> (CPU), <strong>Memory Consumption</strong> (RAM), and <strong>Overall Cost</strong> (Development + Maintenance).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Object Design = Shifting domain entities into detailed computer data structures and algorithms.</li>
    <li>Trade-offs: Execution time vs. Memory footprint vs. Implementation cost.</li>
    <li>Chooses internal representation (e.g. Arrays, Trees, Hash Maps).</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-4",
            "number": "04",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Combining Three Models",
            "subtitle": "Object Model, Dynamic Model & Functional Model Integration in OMT",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">OMT Triad</div>
    <h3>The Three Models of OMT (Rumbaugh Methodology)</h3>
    <p>In Rumbaugh's classic Object Modeling Technique (OMT), a complete system cannot be captured by a single diagram. It requires the synthesis of <strong>Three Orthogonal Models</strong>: the <strong>Object Model</strong> (Structure), the <strong>Dynamic Model</strong> (Behavior &amp; Control), and the <strong>Functional Model</strong> (Computation &amp; Dataflow).</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Anatomy, Nervous System, and Metabolism of a Human</div>
  <ul>
    <li><strong>Object Model = The Skeletal Anatomy:</strong> Bones, muscles, and organs (What parts exist and how they link).</li>
    <li><strong>Dynamic Model = The Nervous System:</strong> Reflexes, nerve pulses, responses to pain (How the body reacts to stimuli over time).</li>
    <li><strong>Functional Model = The Metabolism:</strong> Digestive process turning food into energy (How data/materials are transformed).</li>
  </ul>
</div>

<div class="subtopics-container">
  <h4>Detailed Breakdown of the Three Models</h4>

  <div class="three-col-cards">
    <div class="feature-card">
      <div class="col-head blue-head">1. Object Model (Static)</div>
      <p><strong>Question:</strong> <em>"What things exist?"</em></p>
      <ul>
        <li>Objects &amp; Classes</li>
        <li>Attributes &amp; Operations</li>
        <li>Associations, Generalizations, Aggregations</li>
        <li><strong>Artifact:</strong> Class Diagrams</li>
      </ul>
    </div>

    <div class="feature-card">
      <div class="col-head green-head">2. Dynamic Model (Temporal)</div>
      <p><strong>Question:</strong> <em>"When and how do states change?"</em></p>
      <ul>
        <li>States &amp; Transitions</li>
        <li>Events &amp; Triggers</li>
        <li>Actions &amp; Sequencing</li>
        <li><strong>Artifact:</strong> Statecharts, Sequence Diagrams</li>
      </ul>
    </div>

    <div class="feature-card">
      <div class="col-head purple-head">3. Functional Model (Transformational)</div>
      <p><strong>Question:</strong> <em>"What transformations happen?"</em></p>
      <ul>
        <li>Processes &amp; Computations</li>
        <li>Data Flows &amp; Actors</li>
        <li>Data Stores (Files/DB)</li>
        <li><strong>Artifact:</strong> Data Flow Diagrams (DFDs)</li>
      </ul>
    </div>
  </div>

  <div class="detail-block">
    <h5>How the Three Models Connect</h5>
    <p>The three models are intimately linked:</p>
    <ul>
      <li><strong>Object Model provides the Actors and Classes</strong> that perform operations.</li>
      <li><strong>Dynamic Model specifies the Sequence and Triggers</strong> governing when those operations are invoked.</li>
      <li><strong>Functional Model describes the Arguments and Mathematical Calculations</strong> executed inside those operations.</li>
    </ul>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: The OMT Tri-Model Synthesis</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="tArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>

      <!-- Object Model (Top) -->
      <g transform="translate(280, 15)">
        <rect width="200" height="65" rx="8" fill="var(--bg-card)" stroke="#38bdf8" stroke-width="2"/>
        <text x="100" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#38bdf8">1. OBJECT MODEL</text>
        <text x="100" y="48" text-anchor="middle" font-size="10" fill="var(--text-primary)">Classes, Attributes, Links</text>
      </g>

      <!-- Dynamic Model (Bottom Left) -->
      <g transform="translate(60, 140)">
        <rect width="220" height="65" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="2"/>
        <text x="110" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#34d399">2. DYNAMIC MODEL</text>
        <text x="110" y="48" text-anchor="middle" font-size="10" fill="var(--text-primary)">States, Events, Triggers</text>
      </g>

      <!-- Functional Model (Bottom Right) -->
      <g transform="translate(480, 140)">
        <rect width="220" height="65" rx="8" fill="var(--bg-card)" stroke="#a855f7" stroke-width="2"/>
        <text x="110" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#a78bfa">3. FUNCTIONAL MODEL</text>
        <text x="110" y="48" text-anchor="middle" font-size="10" fill="var(--text-primary)">DFD, Calculations, Data Flows</text>
      </g>

      <!-- Connecting Tri-Lines -->
      <line x1="330" y1="80" x2="200" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#tArr)"/>
      <line x1="430" y1="80" x2="560" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#tArr)"/>
      <line x1="280" y1="172" x2="480" y2="172" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="380" y="165" text-anchor="middle" font-size="9" fill="var(--text-muted)">Events trigger DFD computations</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2014-15):</strong> <em>"What are the three models in OMT? Describe the relationship between Object Model, Dynamic Model, and Functional Model."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Scoring Formula:</strong> Dedicate 3 marks to defining the triad (Object = Structure, Dynamic = Timing/Events, Functional = Transformations). Draw the triangle diagram above showing how classes execute actions triggered by dynamic events.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Object Model = Static identity, classes, relationships (Class Diagram).</li>
    <li>Dynamic Model = Control, states, events over time (Statechart).</li>
    <li>Functional Model = Data transformations, computations (DFDs).</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-5",
            "number": "05",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Designing Algorithms",
            "subtitle": "Algorithm Selection, Computational Complexity, Execution Time vs Memory & Flexibility",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Algorithmic Design</div>
    <h3>Meaning of Algorithm Design in OOSD</h3>
    <p>During object design, operations defined on classes are abstract service contracts. <strong>Designing Algorithms</strong> involves selecting or creating the exact procedural logic, step-by-step instructions, and data traversals that realize each operation efficiently.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: GPS Navigation Route Selection</div>
  <p>When you ask GPS for directions from Delhi to Mumbai, there are multiple routes: the fastest expressway with toll costs, the shortest dirt road with vehicle wear, or the scenic highway. <strong>Algorithm selection</strong> is deciding which route to take based on your trade-offs (Time vs Fuel Cost vs Safety).</p>
</div>

<div class="subtopics-container">
  <h4>Criteria for Choosing an Optimal Algorithm</h4>

  <div class="detail-block">
    <h5>1. The 5 Cardinal Algorithm Selection Criteria</h5>
    <ul>
      <li><strong>Computational Complexity:</strong> Big-O time complexity (e.g. choosing <code>O(N log N)</code> QuickSort over <code>O(N²)</code> BubbleSort for large datasets).</li>
      <li><strong>Space vs Time Trade-off:</strong> Cache precomputed lookup results when execution speed outweighs memory cost.</li>
      <li><strong>Memory Requirements:</strong> Auxiliary space footprint (<code>O(1)</code> in-place sorting vs <code>O(N)</code> extra buffer allocation).</li>
      <li><strong>Flexibility:</strong> Ease of modifying the algorithm if business parameters change.</li>
      <li><strong>Understandability &amp; Maintainability:</strong> A slightly slower simple algorithm is often preferred over an incomprehensible convoluted one that introduces bugs.</li>
    </ul>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Example: Alternative Algorithms for Search Operation</span>
    <span class="code-desc">Comparing Linear Search O(N) vs Binary Search O(log N) for an Inventory operation</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;algorithm&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">ProductCatalog</span> {
<span class="c-keyword">private:</span>
    std::vector&lt;<span class="c-type">int</span>&gt; sortedProductIDs;  <span class="c-comment">// Maintained in sorted order</span>

<span class="c-keyword">public:</span>
    ProductCatalog(std::vector&lt;<span class="c-type">int</span>&gt; ids) : sortedProductIDs(ids) {
        std::sort(sortedProductIDs.begin(), sortedProductIDs.end());
    }

    <span class="c-comment">// Algorithm A: Binary Search - O(log N) Time Complexity</span>
    <span class="c-comment">// Optimal choice for large catalogs</span>
    <span class="c-type">bool</span> searchProductFast(<span class="c-type">int</span> targetID) {
        <span class="c-type">int</span> left = 0, right = sortedProductIDs.size() - 1;

        <span class="c-keyword">while</span> (left &lt;= right) {
            <span class="c-type">int</span> mid = left + (right - left) / 2;
            <span class="c-keyword">if</span> (sortedProductIDs[mid] == targetID) <span class="c-keyword">return</span> <span class="c-keyword">true</span>; <span class="c-comment">// Found</span>
            <span class="c-keyword">if</span> (sortedProductIDs[mid] &lt; targetID)  left = mid + 1;
            <span class="c-keyword">else</span>                                   right = mid - 1;
        }
        <span class="c-keyword">return</span> <span class="c-keyword">false</span>; <span class="c-comment">// Not found</span>
    }
};</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Algorithm Design &amp; Optimization Pipeline</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Step 1: Operation Specification -->
      <rect x="40" y="40" width="190" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="135" y="68" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">1. Operation Spec</text>
      <text x="55" y="100" fill="#e2e8f0" font-size="10">• Input parameters</text>
      <text x="55" y="125" fill="#e2e8f0" font-size="10">• Preconditions</text>
      <text x="55" y="150" fill="#e2e8f0" font-size="10">• Expected results</text>

      <path d="M 230 115 L 295 115" stroke="#60a5fa" stroke-width="2" marker-end="url(#alg-arrow)"/>

      <!-- Step 2: Complexity Trade-off -->
      <rect x="305" y="40" width="230" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="420" y="68" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">2. Trade-Off Analysis</text>
      <rect x="325" y="85" width="190" height="35" rx="4" fill="#78350f"/>
      <text x="420" y="107" fill="#fef3c7" font-size="10" text-anchor="middle">Time: O(n log n) vs O(n²)</text>
      <rect x="325" y="130" width="190" height="35" rx="4" fill="#065f46"/>
      <text x="420" y="152" fill="#a7f3d0" font-size="10" text-anchor="middle">Space: O(1) in-place vs Cache</text>

      <path d="M 535 115 L 600 115" stroke="#34d399" stroke-width="2" marker-end="url(#alg-arrow-green)"/>

      <!-- Step 3: Selected Algorithm -->
      <rect x="610" y="40" width="190" height="150" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="705" y="68" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">3. Concrete Algorithm</text>
      <text x="625" y="100" fill="#86efac" font-size="10">• Quicksort / TimSort</text>
      <text x="625" y="125" fill="#86efac" font-size="10">• Iterative execution</text>
      <text x="625" y="150" fill="#86efac" font-size="10">• Validated invariants</text>

      <defs>
        <marker id="alg-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
        <marker id="alg-arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"How can we design an algorithm for an operation in object design? What factors influence the selection of an optimal algorithm?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Always list the 5 selection criteria: Complexity, Execution time, Memory footprint, Flexibility, and Understandability.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Algorithm design = Choosing concrete logic for abstract class operations.</li>
    <li>Primary trade-off: Time Complexity vs Space Complexity vs Simplicity.</li>
    <li>Rule: Optimize for clarity first; profile and optimize for speed where bottlenecks occur.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-6",
            "number": "06",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Design Optimization",
            "subtitle": "Alternative Designs, Caching, Derived Attributes, Cost & Performance Trade-offs",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Optimization Strategy</div>
    <h3>Meaning of Design Optimization</h3>
    <p><strong>Design Optimization</strong> is the engineering practice of restructuring the design model to satisfy strict performance budgets (throughput, latency, memory limits, and hardware deployment cost) without violating the semantic correctness of the analysis model.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Formula 1 Racing Team Pit Strategy</div>
  <p>A street car is designed for simplicity and comfort. A Formula 1 racing car strips out air conditioning and soundproofing, installs ultra-light carbon fiber parts, and pre-heats tires to shave milliseconds off lap times. <strong>Design optimization</strong> tunes software systems for high-stress production environments.</p>
</div>

<div class="subtopics-container">
  <h4>Common Optimization Techniques in OMT</h4>

  <div class="detail-block">
    <h5>1. Adding Redundant / Derived Attributes (Caching)</h5>
    <p>If an operation repeatedly calculates a value from a collection (e.g. <code>Order.calculateGrandTotal()</code> by summing 50 items), calculating on-the-fly causes CPU overhead. The design is optimized by adding a cached attribute <code>cachedTotal</code> updated only when items change.</p>
  </div>

  <div class="detail-block">
    <h5>2. Reorganizing Execution Paths &amp; Flattening</h5>
    <p>Replacing deeply nested object delegator chains with direct associations to eliminate pointer chasing across memory caches.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Example: Caching Derived Attribute for Optimization</span>
    <span class="code-desc">Optimizing Grand Total retrieval from O(N) recalculation to O(1) cached access</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>

<span class="c-keyword">struct</span> <span class="c-type">Item</span> {
    std::string name;
    <span class="c-type">double</span> price;
};

<span class="c-keyword">class</span> <span class="c-type">OptimizedOrder</span> {
<span class="c-keyword">private:</span>
    std::vector&lt;Item&gt; items;
    <span class="c-type">double</span> cachedTotal;  <span class="c-comment">// Optimization: Redundant cached attribute</span>

<span class="c-keyword">public:</span>
    OptimizedOrder() : cachedTotal(0.0) {}

    <span class="c-comment">// Mutator: Updates cache incrementally in O(1)</span>
    <span class="c-type">void</span> addItem(<span class="c-keyword">const</span> Item&amp; item) {
        items.push_back(item);
        cachedTotal += item.price;  <span class="c-comment">// Maintain cached total incrementally</span>
    }

    <span class="c-comment">// Optimized Query: O(1) instant return instead of looping through all items</span>
    <span class="c-type">double</span> getTotal() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> cachedTotal;
    }
};</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Design Optimization &amp; Redundant Path Caching</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Slow Multi-Hop Path (Top) -->
      <rect x="60" y="40" width="180" height="50" rx="6" fill="#1e293b" stroke="#64748b"/>
      <text x="150" y="70" fill="#e2e8f0" font-size="11" text-anchor="middle">User Session</text>

      <path d="M 240 65 L 325 65" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#opt-gray-arr)"/>

      <rect x="335" y="40" width="180" height="50" rx="6" fill="#1e293b" stroke="#64748b"/>
      <text x="425" y="70" fill="#e2e8f0" font-size="11" text-anchor="middle">Organization Unit</text>

      <path d="M 515 65 L 600 65" stroke="#94a3b8" stroke-width="1.8" marker-end="url(#opt-gray-arr)"/>

      <rect x="610" y="40" width="180" height="50" rx="6" fill="#1e293b" stroke="#64748b"/>
      <text x="700" y="70" fill="#e2e8f0" font-size="11" text-anchor="middle">Permission Matrix</text>

      <!-- Fast Optimized Redundant Shortcut (Bottom) -->
      <path d="M 150 90 C 150 180, 700 180, 700 95" stroke="#34d399" stroke-width="3" stroke-dasharray="6" marker-end="url(#opt-green-arr)"/>
      <rect x="300" y="150" width="250" height="40" rx="6" fill="#065f46" stroke="#34d399"/>
      <text x="425" y="174" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">⚡ Optimized Redundant Cache Pointer: O(1)</text>

      <text x="425" y="215" fill="#fbbf24" font-size="10" text-anchor="middle">Trade-off: Fast O(1) lookup at cost of maintaining cache synchronization</text>

      <defs>
        <marker id="opt-gray-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#94a3b8"/>
        </marker>
        <marker id="opt-green-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14):</strong> <em>"What do you mean by optimization of design? Discuss design optimization with suitable examples."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Tip:</strong> Describe how adding <strong>redundant/derived attributes</strong> trades a tiny amount of memory to dramatically speed up frequent read queries.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Optimization = Restructuring design to satisfy speed, memory, or cost constraints.</li>
    <li>Key technique: Adding derived/cached attributes to avoid repetitive loops.</li>
    <li>Trade-off: Extra memory + cache invalidation logic for ultra-fast query execution.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-7",
            "number": "07",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Implementation of Control",
            "subtitle": "State-Machine Engines, Program Counter Location, Event Handling & Concurrency",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Control Architecture</div>
    <h3>Meaning of Implementation of Control</h3>
    <p>The Dynamic Model specifies state transitions and event reactions. <strong>Implementation of Control</strong> translates these abstract state machines into running code. It determines how execution flow moves through states, responds to asynchronous events, and schedules concurrent tasks.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Traffic Light Controller</div>
  <p>A traffic light transitions between Red, Yellow, and Green. It does not think; a small microcontroller runs a state loop with a timer interrupt. When the timer triggers, it switches states and turns on the corresponding light bulb. That hardware loop is the <strong>implementation of control</strong>.</p>
</div>

<div class="subtopics-container">
  <h4>The Two Primary Approaches to Control Implementation</h4>

  <div class="two-col-cards">
    <div class="feature-card">
      <div class="col-head blue-head">1. State as Program Location (Procedural)</div>
      <p>The current state is implicitly tracked by the <strong>CPU program counter</strong> inside nested sequential loops, <code>switch-case</code> blocks, or function call stacks.</p>
    </div>

    <div class="feature-card">
      <div class="col-head green-head">2. State-Machine Engine (Object-Oriented)</div>
      <p>Uses an explicit <strong>State Machine Pattern</strong> or state variable. An engine receives incoming events and dispatches them to state objects representing current behavior.</p>
    </div>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Example: State-Machine Engine Pattern</span>
    <span class="code-desc">Implementing an ATM Card State Machine with explicit state transitions</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-comment">// Enum representing discrete states from the Dynamic Model</span>
<span class="c-keyword">enum</span> <span class="c-keyword">class</span> <span class="c-type">ATMState</span> { IDLE, CARD_INSERTED, PIN_AUTHENTICATED };

<span class="c-keyword">class</span> <span class="c-type">ATMController</span> {
<span class="c-keyword">private:</span>
    ATMState currentState;  <span class="c-comment">// Explicit state tracking variable</span>

<span class="c-keyword">public:</span>
    ATMController() : currentState(ATMState::IDLE) {}

    <span class="c-comment">// Event Handler: Responding to events and driving transitions</span>
    <span class="c-type">void</span> handleEvent(std::string eventName) {
        <span class="c-keyword">switch</span> (currentState) {
            <span class="c-keyword">case</span> ATMState::IDLE:
                <span class="c-keyword">if</span> (eventName == <span class="c-string">"INSERT_CARD"</span>) {
                    currentState = ATMState::CARD_INSERTED;
                    std::cout &lt;&lt; <span class="c-string">"Action: Card accepted. Please enter PIN.\n"</span>;
                }
                <span class="c-keyword">break</span>;

            <span class="c-keyword">case</span> ATMState::CARD_INSERTED:
                <span class="c-keyword">if</span> (eventName == <span class="c-string">"PIN_CORRECT"</span>) {
                    currentState = ATMState::PIN_AUTHENTICATED;
                    std::cout &lt;&lt; <span class="c-string">"Action: Access Granted. Select Transaction.\n"</span>;
                } <span class="c-keyword">else if</span> (eventName == <span class="c-string">"EJECT"</span>) {
                    currentState = ATMState::IDLE;
                    std::cout &lt;&lt; <span class="c-string">"Action: Card ejected.\n"</span>;
                }
                <span class="c-keyword">break</span>;

            <span class="c-keyword">case</span> ATMState::PIN_AUTHENTICATED:
                <span class="c-keyword">if</span> (eventName == <span class="c-string">"EXIT"</span>) {
                    currentState = ATMState::IDLE;
                    std::cout &lt;&lt; <span class="c-string">"Action: Session finished. Card ejected.\n"</span>;
                }
                <span class="c-keyword">break</span>;
        }
    }
};</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Procedural vs Event-Driven Control Loops</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 260" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Left: Procedural Driven -->
      <rect x="40" y="30" width="360" height="200" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="220" y="58" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Procedural Control (Call Tree)</text>
      
      <rect x="130" y="80" width="180" height="35" rx="4" fill="#0284c7"/>
      <text x="220" y="102" fill="#ffffff" font-size="11" text-anchor="middle">main() Controller</text>

      <path d="M 180 115 L 120 150" stroke="#94a3b8" stroke-width="1.5"/>
      <path d="M 260 115 L 320 150" stroke="#94a3b8" stroke-width="1.5"/>

      <rect x="70" y="150" width="110" height="35" rx="4" fill="#334155"/>
      <text x="125" y="172" fill="#cbd5e1" font-size="10" text-anchor="middle">readInput()</text>

      <rect x="260" y="150" width="120" height="35" rx="4" fill="#334155"/>
      <text x="320" y="172" fill="#cbd5e1" font-size="10" text-anchor="middle">computeOutput()</text>

      <text x="220" y="212" fill="#94a3b8" font-size="9" text-anchor="middle">Fixed programmatic call sequence</text>

      <!-- Right: Event-Driven Dispatcher -->
      <rect x="440" y="30" width="360" height="200" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="620" y="58" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">Event-Driven Control (State Loop)</text>

      <!-- Central Event Loop -->
      <circle cx="620" cy="125" r="42" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
      <text x="620" y="122" fill="#e9d5ff" font-size="10" font-weight="bold" text-anchor="middle">Event Loop</text>
      <text x="620" y="136" fill="#c084fc" font-size="8" text-anchor="middle">(Wait for Event)</text>

      <!-- Outside Event Triggers -->
      <rect x="460" y="70" width="85" height="30" rx="4" fill="#065f46"/>
      <text x="502" y="89" fill="#ffffff" font-size="9" text-anchor="middle">Mouse Click</text>
      <path d="M 545 90 L 585 110" stroke="#34d399" stroke-width="1.5" marker-end="url(#ctrl-green-arr)"/>

      <rect x="460" y="150" width="85" height="30" rx="4" fill="#78350f"/>
      <text x="502" y="169" fill="#ffffff" font-size="9" text-anchor="middle">Network Packet</text>
      <path d="M 545 160 L 585 140" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#ctrl-amber-arr)"/>

      <rect x="690" y="110" width="95" height="35" rx="4" fill="#0369a1"/>
      <text x="737" y="132" fill="#ffffff" font-size="10" text-anchor="middle">Handler Callback</text>
      <path d="M 662 125 L 690 125" stroke="#38bdf8" stroke-width="2" marker-end="url(#ctrl-blue-arr)"/>

      <text x="620" y="212" fill="#94a3b8" font-size="9" text-anchor="middle">Reactive asynchronous state machine</text>

      <defs>
        <marker id="ctrl-green-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
        <marker id="ctrl-amber-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
        <marker id="ctrl-blue-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2014-15):</strong> <em>"Describe implementation of control in object-oriented design. Differentiate state as program location from a state-machine engine."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Contrast procedural execution (linear code location) with an event-driven state engine (decoupled state variables &amp; handler tables).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Implementation of Control = Turning dynamic state machines into running code.</li>
    <li>State as program location: Embedded in procedural code execution stacks.</li>
    <li>State engine: Explicit state variable/pattern reacting to event messages.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-8",
            "number": "08",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Adjustment of Inheritance",
            "subtitle": "Factoring Commonality, Generalizing Operations, Common Ancestors & Multiple Inheritance",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Inheritance Refinement</div>
    <h3>Meaning of Adjustment of Inheritance</h3>
    <p>During initial analysis, developers often identify classes independently. <strong>Adjustment of Inheritance</strong> is an architectural refactoring process that reorganizes class hierarchies to maximize code reuse, eliminate duplicated attributes, and promote common operations up to superclasses.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Family Tree Consolidation</div>
  <p>Imagine discovering that you and three cousins all share the exact same antique pocket watch and family surname, but each cousin maintains their own separate inventory record. You realize: <em>"Wait, this belonged to our common Grandfather!"</em> Moving it to a single ancestral family record avoids duplicating history across all cousins.</p>
</div>

<div class="subtopics-container">
  <h4>The 4 Core Inheritance Adjustment Operations</h4>

  <div class="detail-block">
    <h5>1. Identifying Commonality and Creating Common Ancestors</h5>
    <p>When two classes have similar fields (e.g., <code>Car</code> has <code>speed</code>, <code>licenseNo</code>; <code>Truck</code> has <code>speed</code>, <code>licenseNo</code>), create a common superclass <code>Vehicle</code> and hoist the common attributes upward.</p>
  </div>

  <div class="detail-block">
    <h5>2. Generalizing Operations &amp; Adding Missing Arguments</h5>
    <p>If two subclasses implement similar behaviors with slightly different signatures, generalize the method by unifying parameters into a single flexible signature.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ Example: Inheritance Adjustment via Common Ancestor</span>
    <span class="code-desc">Refactoring Car and Truck by hoisting common attributes to Vehicle ancestor</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// REFACTORED COMMON ANCESTOR: Hoisted shared state</span>
<span class="c-keyword">class</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">protected:</span>
    std::string registrationNumber;
    <span class="c-type">double</span> maxSpeed;

<span class="c-keyword">public:</span>
    Vehicle(std::string regNo, <span class="c-type">double</span> speed) 
        : registrationNumber(regNo), maxSpeed(speed) {}

    <span class="c-comment">// Generalized common operation</span>
    <span class="c-type">void</span> displaySpecs() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Reg: "</span> &lt;&lt; registrationNumber &lt;&lt; <span class="c-string">" | Top Speed: "</span> &lt;&lt; maxSpeed &lt;&lt; <span class="c-string">" km/h\n"</span>;
    }
};

<span class="c-comment">// Subclasses now focus strictly on specialized differences</span>
<span class="c-keyword">class</span> <span class="c-type">Car</span> : <span class="c-keyword">public</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">int</span> passengerCapacity;
<span class="c-keyword">public:</span>
    Car(std::string regNo, <span class="c-type">double</span> speed, <span class="c-type">int</span> capacity)
        : Vehicle(regNo, speed), passengerCapacity(capacity) {}
};

<span class="c-keyword">class</span> <span class="c-type">Truck</span> : <span class="c-keyword">public</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">double</span> cargoTonnage;
<span class="c-keyword">public:</span>
    Truck(std::string regNo, <span class="c-type">double</span> speed, <span class="c-type">double</span> tonnage)
        : Vehicle(regNo, speed), cargoTonnage(tonnage) {}
};</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Factoring Out Common Superclasses</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 250" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Factored Abstract Base Class (Top) -->
      <rect x="330" y="25" width="200" height="65" rx="6" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
      <text x="430" y="48" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Account (Abstract Superclass)</text>
      <text x="430" y="65" fill="#bfdbfe" font-size="9" text-anchor="middle">Shared: id, balance, getBalance()</text>
      <text x="430" y="80" fill="#38bdf8" font-size="9" text-anchor="middle">+ calculateInterest() = 0</text>

      <!-- Inheritance Generalization Arrows -->
      <path d="M 220 145 L 350 90" stroke="#60a5fa" stroke-width="2" marker-end="url(#inh-arrow)"/>
      <path d="M 640 145 L 510 90" stroke="#60a5fa" stroke-width="2" marker-end="url(#inh-arrow)"/>

      <!-- Subclass 1: Savings -->
      <rect x="110" y="145" width="220" height="70" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="220" y="170" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">SavingsAccount</text>
      <text x="220" y="188" fill="#a7f3d0" font-size="9" text-anchor="middle">Specialized: interestRate</text>
      <text x="220" y="204" fill="#e2e8f0" font-size="9" text-anchor="middle">Overrides: calculateInterest()</text>

      <!-- Subclass 2: Checking -->
      <rect x="530" y="145" width="220" height="70" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="640" y="170" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">CheckingAccount</text>
      <text x="640" y="188" fill="#fef3c7" font-size="9" text-anchor="middle">Specialized: overdraftLimit</text>
      <text x="640" y="204" fill="#e2e8f0" font-size="9" text-anchor="middle">Overrides: calculateInterest()</text>

      <defs>
        <marker id="inh-arrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
          <polygon points="0 0, 10 6, 0 12" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2013-14):</strong> <em>"How do we perform adjustment of inheritance? Explain factoring commonality and moving attributes to common ancestors."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Explain the term <strong>"Factoring Commonality"</strong>: detecting identical properties in peer classes and moving them into a newly created abstract ancestor.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Adjustment of Inheritance = Refactoring class hierarchies for optimal reuse.</li>
    <li>Move common attributes and operations to a newly formed superclass.</li>
    <li>Unify method signatures to enable polymorphic extension.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-9",
            "number": "09",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Object Representation",
            "subtitle": "Static vs Dynamic Design Models, Concrete Class Layouts & Relationship Representation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Model Synthesis</div>
    <h3>Meaning of Object Representation</h3>
    <p><strong>Object Representation</strong> defines how software models are drafted and maintained across two complementary perspectives: the <strong>Static Design Model</strong> (structural class and object diagrams) and the <strong>Dynamic Design Model</strong> (interaction and state-chart diagrams).</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Architectural Blueprint vs The Evacuation Drill</div>
  <p>A building has two representations: (1) The architectural schematic showing concrete walls, doors, and electrical sockets (Static Model); (2) The fire evacuation drill plan showing human movement pathways when an alarm sounds (Dynamic Model). Both describe the same building!</p>
</div>

<div class="subtopics-container">
  <h4>Static vs. Dynamic Representation Models</h4>

  <div class="two-col-cards">
    <div class="feature-card">
      <div class="col-head blue-head">Static Design Models</div>
      <p>Represents physical layout, class contracts, types, and links:</p>
      <ul>
        <li><strong>Class Diagrams:</strong> Classes, visibility, inheritance, associations.</li>
        <li><strong>Object Diagrams:</strong> Runtime instances and link references.</li>
      </ul>
    </div>

    <div class="feature-card">
      <div class="col-head green-head">Dynamic Design Models</div>
      <p>Represents behavioral triggers, control logic, and message timing:</p>
      <ul>
        <li><strong>Interaction Diagrams:</strong> Sequence and Collaboration diagrams.</li>
        <li><strong>State-Chart Diagrams:</strong> State transitions and event guards.</li>
      </ul>
    </div>
  </div>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Object Representation Spectrum</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 230" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Column 1: Primitive Types -->
      <rect x="40" y="30" width="230" height="170" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="55" y="45" width="200" height="30" rx="4" fill="#334155"/>
      <text x="155" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">1. Primitive Representation</text>
      <text x="65" y="105" fill="#e2e8f0" font-size="10">• int, double, bool, char</text>
      <text x="65" y="130" fill="#34d399" font-size="10">✓ Fastest CPU execution</text>
      <text x="65" y="155" fill="#34d399" font-size="10">✓ Zero memory overhead</text>
      <text x="65" y="180" fill="#ef4444" font-size="10">✗ No internal validation</text>

      <!-- Column 2: Enumeration Types -->
      <rect x="305" y="30" width="230" height="170" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <rect x="320" y="45" width="200" height="30" rx="4" fill="#78350f"/>
      <text x="420" y="65" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">2. Enumeration Types</text>
      <text x="330" y="105" fill="#e2e8f0" font-size="10">• enum class AccountType</text>
      <text x="330" y="130" fill="#34d399" font-size="10">✓ Type safety at compile time</text>
      <text x="330" y="155" fill="#34d399" font-size="10">✓ Fixed discrete states</text>
      <text x="330" y="180" fill="#94a3b8" font-size="10">✗ Cannot store behavior</text>

      <!-- Column 3: Full Encapsulated Object -->
      <rect x="570" y="30" width="230" height="170" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="585" y="45" width="200" height="30" rx="4" fill="#0284c7"/>
      <text x="685" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. Encapsulated Class</text>
      <text x="595" y="105" fill="#e2e8f0" font-size="10">• class Money / Currency</text>
      <text x="595" y="130" fill="#34d399" font-size="10">✓ Enforces business rules</text>
      <text x="595" y="155" fill="#34d399" font-size="10">✓ Bundles math methods</text>
      <text x="595" y="180" fill="#fbbf24" font-size="10">⚡ Small allocation cost</text>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"What do you mean by object representation in object design? Explain static and dynamic design models."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Clearly delineate between the <strong>Static Model</strong> (structure, class diagrams) and the <strong>Dynamic Model</strong> (behavior, interaction &amp; state diagrams).
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Static Design Model = Class &amp; Object diagrams (Invariants, structure).</li>
    <li>Dynamic Design Model = Sequence, Collaboration &amp; Statechart diagrams (Execution flow).</li>
    <li>Together, they form the complete specification for developers.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-10",
            "number": "10",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Physical Packaging",
            "subtitle": "Software Components, Module Boundaries, Interfaces & Subsystem Partitioning",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Packaging Architecture</div>
    <h3>Meaning of Physical Packaging</h3>
    <p><strong>Physical Packaging</strong> is the architectural activity of partitioning a large enterprise system into cohesive, manageable, and loosely coupled <strong>physical components, modules, packages, and assemblies</strong>. It bridges logical UML classes with real-world binaries (JARs, DLLs, Docker containers, source packages).</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Modern Kitchen Cabinet Organization</div>
  <p>You don't throw knives, flour bags, dinner plates, and ice cream into one giant pile on the floor. You put spices in the rack, perishables in the refrigerator, and silverware in drawers. <strong>Physical packaging</strong> organizes hundreds of software classes into separate, labeled storage units.</p>
</div>

<div class="subtopics-container">
  <h4>Key Aspects of Physical Packaging</h4>

  <div class="detail-block">
    <h5>1. Principles of Effective Packaging</h5>
    <ul>
      <li><strong>High Cohesion:</strong> Classes inside a single package should work closely toward a unified functional goal.</li>
      <li><strong>Loose Coupling:</strong> Dependencies between packages should be minimized and exposed strictly through clean Interfaces.</li>
      <li><strong>Information Hiding:</strong> Internal implementation classes remain package-private (<code>~</code>), preventing external coupling.</li>
    </ul>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">Java / C++ Packaging Namespace Example</span>
    <span class="code-desc">Organizing logical classes into cohesive physical packages / namespaces</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">// In C++: Managed using nested namespaces (Physical modular packaging)</span>

<span class="c-keyword">namespace</span> <span class="c-type">EnterpriseApp</span> {
    <span class="c-comment">// Subsystem 1: Billing Package</span>
    <span class="c-keyword">namespace</span> <span class="c-type">Billing</span> {
        <span class="c-keyword">class</span> <span class="c-type">InvoiceManager</span> { <span class="c-comment">/* ... */</span> };
        <span class="c-keyword">class</span> <span class="c-type">PaymentCalculator</span> { <span class="c-comment">/* ... */</span> };
    }

    <span class="c-comment">// Subsystem 2: Security &amp; Auth Package</span>
    <span class="c-keyword">namespace</span> <span class="c-type">Security</span> {
        <span class="c-keyword">class</span> <span class="c-type">TokenValidator</span> { <span class="c-comment">/* ... */</span> };
        <span class="c-keyword">class</span> <span class="c-type">UserCredentialStore</span> { <span class="c-comment">/* ... */</span> };
    }
}</code></pre>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Logical Model to Physical Packaging</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Logical Classes (Left) -->
      <rect x="40" y="35" width="240" height="170" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="160" y="62" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Logical Object Model</text>
      
      <rect x="60" y="80" width="200" height="30" rx="4" fill="#0f172a" stroke="#0284c7"/>
      <text x="160" y="100" fill="#e2e8f0" font-size="10" text-anchor="middle">class Customer</text>

      <rect x="60" y="120" width="200" height="30" rx="4" fill="#0f172a" stroke="#0284c7"/>
      <text x="160" y="140" fill="#e2e8f0" font-size="10" text-anchor="middle">class BankAccount</text>

      <rect x="60" y="160" width="200" height="30" rx="4" fill="#0f172a" stroke="#0284c7"/>
      <text x="160" y="180" fill="#e2e8f0" font-size="10" text-anchor="middle">class Transaction</text>

      <!-- Packaging Vector -->
      <path d="M 290 120 L 375 120" stroke="#a855f7" stroke-width="2.5" marker-end="url(#pkg-arrow)"/>
      <text x="332" y="110" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">Package</text>

      <!-- Physical Artifacts (Right) -->
      <rect x="390" y="35" width="410" height="170" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="595" y="62" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Physical Compilation Units &amp; Artifacts</text>

      <rect x="415" y="80" width="165" height="45" rx="4" fill="#065f46"/>
      <text x="497" y="100" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">banking.h</text>
      <text x="497" y="114" fill="#a7f3d0" font-size="8" text-anchor="middle">Header Interfaces</text>

      <rect x="605" y="80" width="175" height="45" rx="4" fill="#065f46"/>
      <text x="692" y="100" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">banking.cpp</text>
      <text x="692" y="114" fill="#a7f3d0" font-size="8" text-anchor="middle">Compiled Implementation</text>

      <rect x="415" y="140" width="365" height="45" rx="4" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="597" y="162" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">libbanking.so / libbanking.dll (Dynamic Shared Library)</text>
      <text x="597" y="176" fill="#c7d2fe" font-size="9" text-anchor="middle">Deployable binary component module</text>

      <defs>
        <marker id="pkg-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11):</strong> <em>"Describe physical packaging with an example. What are the different aspects of packaging?"</em> [2.5 / 5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Define cohesion and coupling in packages. Emphasize that packaging enables separate team compilation and independent testing.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Physical Packaging = Grouping classes into modules, namespaces, and libraries.</li>
    <li>Goals: High cohesion within packages, loose coupling between packages.</li>
    <li>Enables team collaboration and independent deployment.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u3-sec-11",
            "number": "11",
            "part": "Part 1 — Object-Oriented Analysis & Design",
            "title": "Documenting Design Considerations",
            "subtitle": "Recording Architectural Decisions, Team Roadmaps, Traceability & Living Documentation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Documentation Engineering</div>
    <h3>Meaning of Documenting Design Considerations</h3>
    <p>Software design is a series of trade-offs. <strong>Documenting Design Considerations</strong> is the formal practice of recording not just <em>what</em> was designed, but <strong>WHY</strong> specific architectural decisions, data structures, and algorithms were chosen over competing alternatives. It serves as the definitive roadmap for implementation teams and future maintainers.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Captain's Flight Log</div>
  <p>In aviation, pilots don't just fly; every detour around a thunderstorm, fuel recalculation, and altitude shift is recorded in the flight log. If an issue occurs later, investigators and future pilots understand exact rationale behind every pilot choice. Design documentation is the software flight log!</p>
</div>

<div class="subtopics-container">
  <h4>Key Requirements of Design Documentation</h4>

  <div class="detail-block">
    <h5>1. Guidelines for Robust Living Documentation</h5>
    <ul>
      <li><strong>Record Alternative Options Rejected:</strong> Explains why an alternative was discarded so future developers do not repeat failed experiments.</li>
      <li><strong>Roadmap for Distributed Teams:</strong> Acts as a single source of truth across geographically dispersed engineering teams.</li>
      <li><strong>Living Document in Iterative Development:</strong> Must be continuously updated alongside agile sprint code commits.</li>
      <li><strong>Periodic Review &amp; Safe Backups:</strong> Version-controlled in Git/SVN alongside source code repositories.</li>
    </ul>
  </div>
</div>
<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Architecture Decision Record (ADR) Lifecycle</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 240" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Stage 1: Context & Driver -->
      <rect x="40" y="45" width="160" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="120" y="75" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">1. Architectural Need</text>
      <text x="55" y="105" fill="#e2e8f0" font-size="9">• High read traffic</text>
      <text x="55" y="125" fill="#e2e8f0" font-size="9">• 10,000 req/sec</text>
      <text x="55" y="145" fill="#e2e8f0" font-size="9">• Sub-50ms SLA</text>

      <path d="M 200 115 L 235 115" stroke="#60a5fa" stroke-width="2" marker-end="url(#doc-arrow)"/>

      <!-- Stage 2: Decision & Alternatives -->
      <rect x="245" y="45" width="190" height="140" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="340" y="75" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">2. Decision &amp; Options</text>
      <rect x="260" y="90" width="160" height="30" rx="3" fill="#065f46"/>
      <text x="340" y="109" fill="#a7f3d0" font-size="9" text-anchor="middle">Chosen: Redis In-Memory</text>
      <rect x="260" y="130" width="160" height="30" rx="3" fill="#7f1d1d"/>
      <text x="340" y="149" fill="#fca5a5" font-size="9" text-anchor="middle">Rejected: File Cache</text>

      <path d="M 435 115 L 470 115" stroke="#60a5fa" stroke-width="2" marker-end="url(#doc-arrow)"/>

      <!-- Stage 3: Trade-off Consequences -->
      <rect x="480" y="45" width="160" height="140" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="560" y="75" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">3. Consequences</text>
      <text x="495" y="105" fill="#34d399" font-size="9">✓ Sub-10ms response</text>
      <text x="495" y="125" fill="#fbbf24" font-size="9">⚡ Higher RAM budget</text>
      <text x="495" y="145" fill="#f87171" font-size="9">⚠ Eviction policy needed</text>

      <path d="M 640 115 L 675 115" stroke="#34d399" stroke-width="2" marker-end="url(#doc-arrow-green)"/>

      <!-- Stage 4: Versioned Git Repo -->
      <rect x="685" y="45" width="125" height="140" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="747" y="75" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">4. Git / Docs</text>
      <rect x="695" y="95" width="105" height="35" rx="4" fill="#047857"/>
      <text x="747" y="117" fill="#ffffff" font-size="9" text-anchor="middle">ADR-004.md</text>
      <text x="747" y="155" fill="#94a3b8" font-size="8" text-anchor="middle">Committed to Repo</text>

      <defs>
        <marker id="doc-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
        <marker id="doc-arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>


<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2015-16):</strong> <em>"What do you mean by documentation? What are the various considerations in documentation designing? Explain."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Cite that documentation communicates intent, prevents architectural drift, explains trade-offs, and must be publicly accessible and periodically reviewed.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li>Design Documentation = Captures the 'WHY' behind architectural choices.</li>
    <li>Prevents future developers from repeating rejected, flawed approaches.</li>
    <li>Must be kept updated alongside code in version control.</li>
  </ul>
</div>
"""
        }
    ]
