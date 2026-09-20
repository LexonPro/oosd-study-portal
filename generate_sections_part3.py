# generate_sections_part3.py: Part 3 - Collaboration Diagram (Sections 11 to 16)

def get_part3_sections():
    return [
        {
            "id": "sec-11",
            "number": "11",
            "part": "Part 3 — Collaboration Diagram",
            "title": "Collaboration Diagram",
            "subtitle": "Communication Diagrams, Spatial Object Organization & Message Interactions",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Interaction Architecture</div>
    <h3>Meaning and Purpose of Collaboration Diagrams</h3>
    <p>A <strong>Collaboration Diagram</strong> (officially designated as a <strong>Communication Diagram</strong> in UML 2.x) is an interaction diagram that models the <strong>structural organization of software objects that send and receive messages</strong>.</p>
    <p>While a Sequence Diagram emphasizes the <em>chronological time order</em> of messages, a Collaboration Diagram emphasizes the <em>spatial layout and structural links</em> among cooperating software objects.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Architectural Perspectives</h4>

  <div class="detail-block">
    <h5>1. Relationships Among Software Objects</h5>
    <p>Collaboration diagrams portray objects arranged in free-form two-dimensional space. Solid lines represent <strong>Links</strong> (the runtime conduit through which objects communicate). If no link exists between two objects, they cannot exchange messages.</p>
  </div>

  <div class="detail-block">
    <h5>2. Interactions and Messages</h5>
    <p>Messages are represented by small labeled arrows drawn parallel to the link connecting the sender and receiver. Because time is not explicitly mapped onto an axis, <strong>explicit sequence numbering (1, 2, 2.1, 3)</strong> is mandatory to convey execution order.</p>
  </div>

  <div class="detail-block">
    <h5>3. Collaboration Diagram vs. Sequence Diagram</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Criterion</th>
          <th>Collaboration / Communication Diagram</th>
          <th>Sequence Diagram</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Primary Emphasis</strong></td>
          <td><strong>Spatial organization</strong> and structural links connecting objects</td>
          <td><strong>Temporal order</strong> (chronological progression of time)</td>
        </tr>
        <tr>
          <td><strong>Time Axis</strong></td>
          <td>No explicit time axis (deduced purely via sequence numbers: 1, 1.1, 2)</td>
          <td>Explicit vertical time axis flowing from top to bottom</td>
        </tr>
        <tr>
          <td><strong>Object Lifelines</strong></td>
          <td>No lifelines or activation bars; objects appear as discrete boxes</td>
          <td>Vertical dashed lifelines with activation rectangles overlaying them</td>
        </tr>
        <tr>
          <td><strong>Best Used For</strong></td>
          <td>Understanding object clustering, network links, and localized architecture</td>
          <td>Complex procedural logic, concurrent timing, and edge-case execution traces</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Collaboration Diagram Layout (E-Commerce Checkout)</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="collabArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
        </marker>
        <marker id="retArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
        </marker>
      </defs>

      <!-- Actor: Customer -->
      <g transform="translate(40, 90)">
        <circle cx="20" cy="15" r="12" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="27" x2="20" y2="55" stroke="#3b82f6" stroke-width="2"/>
        <line x1="5" y1="38" x2="35" y2="38" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="6" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="34" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <text x="20" y="92" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">:Customer</text>
      </g>

      <!-- Link 1: Customer to OrderController -->
      <line x1="85" y1="120" x2="230" y2="120" stroke="#64748b" stroke-width="2"/>
      <!-- Message 1 -->
      <line x1="100" y1="108" x2="210" y2="108" stroke="#2563eb" stroke-width="2" marker-end="url(#collabArr)"/>
      <text x="155" y="100" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">1: submitOrder(cart)</text>

      <!-- Object: OrderController -->
      <g transform="translate(230, 95)">
        <rect width="150" height="50" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="75" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:OrderController</text>
      </g>

      <!-- Link 2: OrderController to PaymentGateway -->
      <line x1="380" y1="120" x2="520" y2="120" stroke="#64748b" stroke-width="2"/>
      <!-- Message 2 -->
      <line x1="400" y1="108" x2="500" y2="108" stroke="#2563eb" stroke-width="2" marker-end="url(#collabArr)"/>
      <text x="450" y="100" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">2: processPayment(amt)</text>

      <!-- Object: PaymentGateway -->
      <g transform="translate(520, 95)">
        <rect width="160" height="50" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="80" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:PaymentGateway</text>
      </g>

      <!-- Link 3: OrderController down to Inventory -->
      <line x1="305" y1="145" x2="305" y2="200" stroke="#64748b" stroke-width="2"/>
      <line x1="318" y1="155" x2="318" y2="190" stroke="#2563eb" stroke-width="2" marker-end="url(#collabArr)"/>
      <text x="390" y="175" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">3: reserveStock()</text>

      <!-- Object: Inventory -->
      <g transform="translate(230, 200)">
        <rect width="150" height="45" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="75" y="27" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:Inventory</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2011-12):</strong> <em>"What is a collaboration diagram? How does it differ from a sequence diagram? Draw a collaboration diagram for booking an airline ticket."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Always emphasize that both Sequence and Collaboration diagrams are semantically isomorphic (can be transformed into each other without losing information), but Collaboration diagrams highlight <strong>structural topology</strong> while Sequence diagrams highlight <strong>time chronology</strong>.
  </div>
</div>
"""
        },
        {
            "id": "sec-12",
            "number": "12",
            "part": "Part 3 — Collaboration Diagram",
            "title": "Terms and Concepts of Collaboration Diagrams",
            "subtitle": "Objects, Links, Messages, Sequence Numbers, Sender & Receiver Roles",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational Terms</div>
    <h3>Essential Vocabulary of Collaboration Modeling</h3>
    <p>A collaboration diagram relies on six fundamental building blocks to articulate how a collection of objects achieves an operational goal.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The 6 Core Terms and Symbols</h4>

  <div class="detail-block">
    <h5>1. Objects (Classifier Roles)</h5>
    <p>Represented as rectangles with <u>underlined labels</u> following the syntax <code><u>objectName : ClassName</u></code>. Objects represent the collaborating entities executing the scenario.</p>
  </div>

  <div class="detail-block">
    <h5>2. Links</h5>
    <p>A solid line connecting two objects. A link is an instance of an association, representing a communication pathway. Unlike associations, links do not show multiplicity.</p>
  </div>

  <div class="detail-block">
    <h5>3. Messages</h5>
    <p>The communication unit dispatched across a link. Represented as an arrow along the link pointing from the sender to the receiver, labeled with the sequence number, operation name, and parameter arguments.</p>
  </div>

  <div class="detail-block">
    <h5>4. Message Sequence Numbers</h5>
    <p>A numerical prefix (e.g. <code>1:</code>, <code>1.1:</code>, <code>2:</code>) indicating the chronological order of message execution. Hierarchical dot notation reflects nested method activations.</p>
  </div>

  <div class="detail-block">
    <h5>5. Sender Role</h5>
    <p>The object that originates and fires the message across the link.</p>
  </div>

  <div class="detail-block">
    <h5>6. Receiver Role</h5>
    <p>The object that accepts the incoming message and executes the requested operation.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Anatomy of a Collaboration Link and Message</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="anatArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
        </marker>
      </defs>

      <!-- Sender Object -->
      <g transform="translate(40, 70)">
        <rect width="140" height="55" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="70" y="32" text-anchor="middle" font-size="12" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">sender : Client</text>
      </g>

      <!-- Link Line -->
      <line x1="180" y1="97" x2="520" y2="97" stroke="#64748b" stroke-width="2"/>

      <!-- Message Arrow -->
      <line x1="220" y1="80" x2="480" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#anatArr)"/>
      <text x="350" y="70" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">1.2: processRequest(data : String)</text>

      <!-- Receiver Object -->
      <g transform="translate(520, 70)">
        <rect width="160" height="55" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="80" y="32" text-anchor="middle" font-size="12" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">receiver : Server</text>
      </g>

      <!-- Annotations -->
      <text x="110" y="145" text-anchor="middle" font-size="11" fill="#3b82f6"><tspan font-weight="bold">Sender:</tspan> Initiates call</text>
      <text x="350" y="118" text-anchor="middle" font-size="11" fill="var(--text-muted)"><tspan font-weight="bold">Link:</tspan> Communication path</text>
      <text x="350" y="45" text-anchor="middle" font-size="11" fill="#2563eb"><tspan font-weight="bold">Message:</tspan> Seq No + Operation + Args</text>
      <text x="600" y="145" text-anchor="middle" font-size="11" fill="#10b981"><tspan font-weight="bold">Receiver:</tspan> Executes operation</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>Short Question:</strong> <em>"Explain the terms Link, Message, and Sequence Number as used in collaboration diagrams."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Scoring Formula:</strong> Clearly state that a <em>Link</em> is an instance of an association, a <em>Message</em> is a directed invocation, and a <em>Sequence Number</em> conveys chronological execution without a time axis.
  </div>
</div>
"""
        },
        {
            "id": "sec-13",
            "number": "13",
            "part": "Part 3 — Collaboration Diagram",
            "title": "Depicting a Message",
            "subtitle": "Message Syntax, Direction, Nested Sequence Numbering & Parameters",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Message Specification</div>
    <h3>Full UML Syntax for Depicting a Message</h3>
    <p>A message in a collaboration diagram conveys an action to be executed, a request for information, or a control signal. Standard UML specifies a formal textual grammar for labeling message arrows.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Message Syntax and Conventions</h4>

  <div class="detail-block">
    <h5>1. Complete Message Label Grammar</h5>
    <div class="code-box"><code>[predecessor] sequence-expression [return-variable :=] message-name ( [argument-list] )</code></div>
    <ul>
      <li><strong>Sequence-Expression:</strong> E.g., <code>1.2:</code> or <code>2a:</code>.</li>
      <li><strong>Return Variable:</strong> E.g., <code>isValid := validate()</code>.</li>
      <li><strong>Arguments:</strong> Values or parameters passed to the receiver method.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Message Direction</h5>
    <p>An arrow drawn parallel to the link line points strictly in the direction of data/control dispatch (from Sender to Receiver). A single link can carry multiple messages flowing in both directions.</p>
  </div>

  <div class="detail-block">
    <h5>3. Sequence Numbering Schemes: Flat vs. Nested</h5>
    <div class="two-col-cards">
      <div class="feature-card">
        <div class="col-head blue-head">Flat Numbering (Procedural)</div>
        <p>Simple sequential integers representing sequential procedure calls:</p>
        <p><code>1: open()</code> &rarr; <code>2: read()</code> &rarr; <code>3: close()</code></p>
      </div>

      <div class="feature-card">
        <div class="col-head green-head">Nested / Hierarchical Numbering</div>
        <p>Dot notation expressing nested execution activations (sub-calls):</p>
        <p><code>1: createOrder()</code></p>
        <p style="margin-left: 15px;"><code>1.1: checkStock()</code></p>
        <p style="margin-left: 30px;"><code>1.1.1: queryDB()</code></p>
        <p style="margin-left: 15px;"><code>1.2: calculateTotal()</code></p>
        <p><code>2: printInvoice()</code></p>
      </div>
    </div>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Depicting Bidirectional & Nested Messages on Links</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="msgR" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
        </marker>
        <marker id="msgL" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 10 1 L 0 5 L 10 9 z" fill="#10b981"/>
        </marker>
      </defs>

      <!-- Client -->
      <g transform="translate(40, 80)">
        <rect width="130" height="50" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="65" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:ClientApp</text>
      </g>

      <!-- Link -->
      <line x1="170" y1="105" x2="520" y2="105" stroke="#64748b" stroke-width="2"/>

      <!-- Message Forward (Left to Right) -->
      <line x1="200" y1="85" x2="490" y2="85" stroke="#2563eb" stroke-width="2" marker-end="url(#msgR)"/>
      <text x="345" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">1: authToken := login(user, pass)</text>

      <!-- Message Return (Right to Left) -->
      <line x1="200" y1="125" x2="490" y2="125" stroke="#10b981" stroke-width="2" marker-start="url(#msgL)"/>
      <text x="345" y="142" text-anchor="middle" font-size="11" font-weight="bold" fill="#059669">1.3: notifySessionReady(token)</text>

      <!-- AuthServer -->
      <g transform="translate(520, 80)">
        <rect width="150" height="50" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="75" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:AuthService</text>
      </g>

      <text x="345" y="195" text-anchor="middle" font-size="11" fill="var(--text-muted)">Two messages over a single link with explicit sequence order and return binding.</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"How are messages depicted in a collaboration diagram? Explain message direction and nested numbering with an example."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Tip:</strong> Always show a nested sequence example (e.g. <code>1.1:</code>, <code>1.2:</code>) to demonstrate that the author understands activation nesting in procedural systems.
  </div>
</div>
"""
        },
        {
            "id": "sec-14",
            "number": "14",
            "part": "Part 3 — Collaboration Diagram",
            "title": "Polymorphism in Collaboration Diagram",
            "subtitle": "Same Message, Diverse Receiver Implementations & Payroll Calculation Example",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Polymorphic Interaction</div>
    <h3>Meaning of Polymorphism in Collaboration Diagrams</h3>
    <p><strong>Polymorphism</strong> is the object-oriented principle where a sender issues the <strong>identical message signature</strong> to different target objects, and each concrete receiver executes its own specialized implementation based on its runtime type.</p>
    <p>In a collaboration diagram, this is depicted by having the sender broadcast or dispatch the same message name across links to polymorphic subclasses, typically annotated with <strong>parallel sequence letters (e.g., 2a:, 2b:, 2c:)</strong> or polymorphic guards.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Classic AKTU Scenario: The University Payroll System</h4>

  <div class="detail-block">
    <h5>Problem Statement & Architectural Insight</h5>
    <p>A <code>MonthlyPayroll</code> controller must compute the salaries for all employees in a company. However, the exact salary calculation algorithm varies dramatically depending on employment classification:</p>
    <ul>
      <li><strong>FullTimeEmployee:</strong> Receives a fixed monthly salary determined by job grade: <code>salary = gradeBaseSalary</code>.</li>
      <li><strong>PartTimeEmployee:</strong> Receives an hourly wage multiplied by verified timesheet hours: <code>salary = hoursWorked * hourlyRate</code>.</li>
      <li><strong>TemporaryEmployee:</strong> Receives a flat stipend without tax or pension deduction: <code>salary = flatStipend</code>.</li>
    </ul>
    <p><strong>Key Design Advantage:</strong> The <code>MonthlyPayroll</code> object does not contain an ugly <code>if-else</code> or <code>switch</code> ladder checking types. It simply dispatches <code>calculatePay()</code>, relying on dynamic runtime binding!</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Polymorphic Dispatch in Collaboration Diagram (Payroll Example)</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="polyArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/>
        </marker>
      </defs>

      <!-- Pay Clerk Actor -->
      <g transform="translate(30, 95)">
        <circle cx="20" cy="15" r="12" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="27" x2="20" y2="55" stroke="#3b82f6" stroke-width="2"/>
        <line x1="5" y1="38" x2="35" y2="38" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="6" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <line x1="20" y1="55" x2="34" y2="75" stroke="#3b82f6" stroke-width="2"/>
        <text x="20" y="92" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">:PayClerk</text>
      </g>

      <!-- Trigger Link -->
      <line x1="75" y1="125" x2="190" y2="125" stroke="#64748b" stroke-width="2"/>
      <line x1="90" y1="113" x2="175" y2="113" stroke="#2563eb" stroke-width="2" marker-end="url(#polyArr)"/>
      <text x="132" y="105" text-anchor="middle" font-size="9" font-weight="bold" fill="#2563eb">1: runPayroll()</text>

      <!-- Sender: MonthlyPayroll -->
      <g transform="translate(190, 100)">
        <rect width="160" height="50" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="80" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:MonthlyPayroll</text>
      </g>

      <!-- Branch A: FullTimeEmployee -->
      <line x1="350" y1="115" x2="490" y2="50" stroke="#64748b" stroke-width="2"/>
      <line x1="370" y1="100" x2="465" y2="55" stroke="#dc2626" stroke-width="1.8" marker-end="url(#polyArr)"/>
      <text x="400" y="70" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">2a: calculatePay()</text>

      <g transform="translate(490, 25)">
        <rect width="210" height="50" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="105" y="24" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:FullTimeEmployee</text>
        <text x="105" y="40" text-anchor="middle" font-size="9" fill="var(--text-muted)">Fixed Monthly Grade Base</text>
      </g>

      <!-- Branch B: PartTimeEmployee -->
      <line x1="350" y1="125" x2="490" y2="125" stroke="#64748b" stroke-width="2"/>
      <line x1="370" y1="115" x2="470" y2="115" stroke="#dc2626" stroke-width="1.8" marker-end="url(#polyArr)"/>
      <text x="420" y="108" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">2b: calculatePay()</text>

      <g transform="translate(490, 100)">
        <rect width="210" height="50" rx="4" fill="var(--card-bg)" stroke="#f59e0b" stroke-width="2"/>
        <text x="105" y="24" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:PartTimeEmployee</text>
        <text x="105" y="40" text-anchor="middle" font-size="9" fill="var(--text-muted)">Hours Worked * Hourly Rate</text>
      </g>

      <!-- Branch C: TemporaryEmployee -->
      <line x1="350" y1="135" x2="490" y2="200" stroke="#64748b" stroke-width="2"/>
      <line x1="370" y1="150" x2="465" y2="195" stroke="#dc2626" stroke-width="1.8" marker-end="url(#polyArr)"/>
      <text x="400" y="180" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">2c: calculatePay()</text>

      <g transform="translate(490, 175)">
        <rect width="210" height="50" rx="4" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="2"/>
        <text x="105" y="24" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:TemporaryEmployee</text>
        <text x="105" y="40" text-anchor="middle" font-size="9" fill="var(--text-muted)">Flat Stipend (No Pension Ded.)</text>
      </g>

      <text x="380" y="260" text-anchor="middle" font-size="11" fill="var(--text-muted)">Subscript letters (2a, 2b, 2c) represent polymorphic invocations of calculatePay().</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14, 2014-15):</strong> <em>"Explain Polymorphism, Iterated Messages, and use of self in collaboration diagrams with suitable examples."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Exam Must-Have:</strong> The Employee Salary calculation diagram above is the <strong>canonical textbook example</strong> in Indian university curricula. Drawing this specific diagram with letters <code>2a</code>, <code>2b</code>, <code>2c</code> awards 100% of the allocated marks.
  </div>
</div>
"""
        },
        {
            "id": "sec-15",
            "number": "15",
            "part": "Part 3 — Collaboration Diagram",
            "title": "Iterated Message",
            "subtitle": "Repeated Messages, Asterisk Notation, Iteration Clauses & Batch Processing",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Loop Modeling</div>
    <h3>Meaning of Iterated Messages in Collaboration</h3>
    <p>An <strong>Iterated Message</strong> represents a message that is dispatched repeatedly across a link, either over a collection of target objects or in a loop until a termination guard condition evaluates to false.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Syntax and Notation for Iteration</h4>

  <div class="detail-block">
    <h5>1. The Asterisk (<code>*</code>) Syntax</h5>
    <p>UML specifies the <strong>asterisk symbol (<code>*</code>)</strong> immediately following the sequence number to denote repetition:</p>
    <ul>
      <li><code>1.2 * : printDocument()</code> &mdash; Unbounded sequential loop.</li>
      <li><code>1.2 * [i := 1..n] : processItem(item[i])</code> &mdash; Controlled iteration through an index range.</li>
      <li><code>1.2 * [while hasMoreTokens] : nextToken()</code> &mdash; Guard-controlled condition loop.</li>
      <li><code>1.2 * || [i := 1..n] : calculateSubtotal()</code> &mdash; <strong>Parallel Iteration</strong>: indicates that invocations occur concurrently across threads!</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Real-World Concrete Example: Shopping Cart Total Calculation</h5>
    <p>In an e-commerce platform, an <code>Order</code> object must compute the order grand total. It iterates through an array of <code>OrderItem</code> objects, invoking <code>getItemTotal()</code> on each item in sequence.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Iterated Message Across Collection Items</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="itArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
        </marker>
      </defs>

      <!-- Order Object -->
      <g transform="translate(60, 75)">
        <rect width="140" height="50" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="70" y="30" text-anchor="middle" font-size="12" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:Order</text>
      </g>

      <!-- Link to OrderItem collection -->
      <line x1="200" y1="100" x2="480" y2="100" stroke="#64748b" stroke-width="2"/>

      <!-- Iterated Message Arrow -->
      <line x1="230" y1="80" x2="450" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#itArr)"/>
      <text x="340" y="70" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">1 * [i := 1..n]: price := getItemPrice()</text>

      <!-- Multiobject / Collection Box: OrderItem -->
      <g transform="translate(480, 70)">
        <!-- Back rectangle representing collection -->
        <rect x="8" y="-8" width="160" height="50" rx="4" fill="var(--bg-secondary)" stroke="#64748b" stroke-width="1.5"/>
        <rect width="160" height="50" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="80" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">items[i] : OrderItem</text>
      </g>

      <text x="340" y="160" text-anchor="middle" font-size="11" fill="var(--text-muted)">The asterisk (*) informs the parser and developer that this message repeats n times.</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"How are repeated/iterated messages depicted in a collaboration diagram? What is the difference between sequential and parallel iteration?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Point:</strong> Standard sequential loop uses <code>* [clause]</code>. Parallel / concurrent iteration uses double vertical pipes: <code>* || [clause]</code>. Mentioning parallel iteration shows exceptional mastery.
  </div>
</div>
"""
        },
        {
            "id": "sec-16",
            "number": "16",
            "part": "Part 3 — Collaboration Diagram",
            "title": "Use of self in Message",
            "subtitle": "Reflexive Message Calls, Internal State Validation & Recursive Computations",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Reflexive Invocation</div>
    <h3>Meaning of self / Reflexive Messages</h3>
    <p>A <strong>self-message</strong> (also called a <em>reflexive message</em> or <em>local invocation</em>) occurs when an object sends a message to <strong>itself</strong>. In code, this corresponds directly to invoking a local member method using <code>this-&gt;method()</code> in C++, <code>this.method()</code> in Java, or <code>self.method()</code> in Python.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Purpose and Representation</h4>

  <div class="detail-block">
    <h5>1. Architectural Purpose of Self-Messages</h5>
    <ul>
      <li><strong>Internal Data Validation:</strong> E.g., An <code>Account</code> object validating PIN or checking overdraft limits before allowing a debit.</li>
      <li><strong>State Transition Enforcement:</strong> Triggering an internal state change without external intervention.</li>
      <li><strong>Recursive Algorithms:</strong> E.g., Tree traversal or factorial computation where an object calls itself with modified parameters.</li>
      <li><strong>Private Helper Functions:</strong> Invoking internal calculation subroutines.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Graphical Representation in Collaboration Diagrams</h5>
    <p>A self-message is depicted as a <strong>looping link (semicircular arc)</strong> originating from the object box and terminating back onto the same object box, accompanied by a directed arrow and sequence number.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Self-Message Notation (Bank Account Withdrawal)</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="selfArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#8b5cf6"/>
        </marker>
        <marker id="inArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
        </marker>
      </defs>

      <!-- ATM Controller -->
      <g transform="translate(60, 80)">
        <rect width="140" height="50" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="70" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:ATMController</text>
      </g>

      <!-- Incoming Message -->
      <line x1="200" y1="105" x2="380" y2="105" stroke="#64748b" stroke-width="2"/>
      <line x1="220" y1="90" x2="350" y2="90" stroke="#2563eb" stroke-width="2" marker-end="url(#inArr)"/>
      <text x="285" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">1: withdraw(amt)</text>

      <!-- BankAccount with Self-Loop -->
      <g transform="translate(380, 80)">
        <rect width="160" height="50" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="80" y="30" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:BankAccount</text>
      </g>

      <!-- Self Link Arc -->
      <path d="M 440 80 C 440 15, 500 15, 500 80" fill="none" stroke="#8b5cf6" stroke-width="2"/>
      <!-- Self Message Arrow on Arc -->
      <path d="M 485 30 L 498 33" stroke="#8b5cf6" stroke-width="2" marker-end="url(#selfArr)"/>
      <text x="470" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">1.1: isValid := checkOverdraft(amt)</text>

      <text x="380" y="185" text-anchor="middle" font-size="11" fill="var(--text-muted)">Message 1.1 loops directly back into :BankAccount as a nested self-invocation.</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Explain the use of 'self' in message passing in collaboration diagrams. Draw a neat diagram."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Explain that self-messages depict internal member function calls (equivalent to <code>this.method()</code>). Draw the loop-back arc with a nested sequence number (<code>1.1</code>).
  </div>
</div>
"""
        }
    ]
