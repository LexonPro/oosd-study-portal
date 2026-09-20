# generate_sections_part4.py: Part 4 - Sequence Diagram (Sections 17 to 21)

def get_part4_sections():
    return [
        {
            "id": "sec-17",
            "number": "17",
            "part": "Part 4 — Sequence Diagram",
            "title": "Sequence Diagram",
            "subtitle": "Temporal Interaction, Chronological Message Exchange & Runtime Scenario Modeling",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Temporal Interaction</div>
    <h3>Meaning and Purpose of Sequence Diagrams</h3>
    <p>A <strong>Sequence Diagram</strong> is the premier interaction diagram in UML, modeling <strong>how objects interact through message exchanges organized in strict chronological time order</strong>.</p>
    <p>It explicitly captures runtime execution scenarios, event sequences, method invocations, and return values along an unmistakable two-dimensional plane.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Temporal Dimensions</h4>

  <div class="detail-block">
    <h5>1. The Two-Dimensional Coordinate System of Sequence Diagrams</h5>
    <ul>
      <li><strong>Horizontal Axis (X-Axis):</strong> Represents the participating objects, classifiers, and actors arrayed side-by-side across the top. Order does not imply priority, though standard practice places initiating actors on the far left.</li>
      <li><strong>Vertical Axis (Y-Axis):</strong> Represents <strong>Time progressing downwards</strong>. Messages drawn lower down chronologically occur strictly after messages drawn higher up.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Modeling Runtime Scenarios & Event Diagrams</h5>
    <p>Sequence diagrams excel at modeling a single, concrete execution path through a Use Case (known as a <em>Scenario</em>):</p>
    <ul>
      <li><strong>Sunny Day / Primary Scenario:</strong> The standard happy-path flow without errors (e.g. successful ATM cash withdrawal).</li>
      <li><strong>Alternate / Exception Scenario:</strong> Branching error-handling paths (e.g. invalid PIN entered 3 times, insufficient account balance).</li>
      <li><strong>Event Diagrams:</strong> Used in telecommunications and embedded systems to trace signals emitted by sensors and received by controllers over millisecond timelines.</li>
    </ul>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: 2D Coordinate Grid of a Sequence Diagram</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 270" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="syncArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <polygon points="0,1 10,5 0,9" class="uml-dark-shape" fill="#60a5fa"/>
        </marker>
        <marker id="dashArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#64748b" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Time Axis Indicator -->
      <line x1="30" y1="40" x2="30" y2="230" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,4"/>
      <polygon points="26,230 30,242 34,230" class="uml-cube-side" fill="#182335"/>
      <text x="30" y="255" text-anchor="middle" font-size="10" font-weight="bold" fill="#64748b">TIME (↓)</text>

      <!-- Participant 1: User -->
      <g transform="translate(100, 20)">
        <rect width="110" height="35" rx="3" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="55" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:Customer</text>
        <line x1="55" y1="35" x2="55" y2="220" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="50" y="60" width="10" height="140" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Participant 2: Controller -->
      <g transform="translate(320, 20)">
        <rect width="130" height="35" rx="3" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="65" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:ATMController</text>
        <line x1="65" y1="35" x2="65" y2="220" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="60" y="70" width="10" height="120" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Participant 3: BankServer -->
      <g transform="translate(540, 20)">
        <rect width="130" height="35" rx="3" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="65" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:BankServer</text>
        <line x1="65" y1="35" x2="65" y2="220" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="60" y="100" width="10" height="60" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Message 1 -->
      <line x1="165" y1="90" x2="380" y2="90" class="uml-dark-stroke" stroke="#60a5fa" stroke-width="1.8" marker-end="url(#syncArr)"/>
      <text x="270" y="82" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">insertCard(pin)</text>

      <!-- Message 2 -->
      <line x1="395" y1="120" x2="600" y2="120" class="uml-dark-stroke" stroke="#60a5fa" stroke-width="1.8" marker-end="url(#syncArr)"/>
      <text x="500" y="112" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--text-primary)">verifyPin(pin)</text>

      <!-- Reply 1 -->
      <line x1="600" y1="155" x2="395" y2="155" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#dashArr)"/>
      <text x="500" y="148" text-anchor="middle" font-size="9" fill="var(--text-muted)">pinVerified = true</text>

      <!-- Reply 2 -->
      <line x1="380" y1="185" x2="165" y2="185" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#dashArr)"/>
      <text x="270" y="178" text-anchor="middle" font-size="9" fill="var(--text-muted)">displayMenu()</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2014-15):</strong> <em>"Discuss the significance of sequence diagrams. What are the two dimensions in a sequence diagram?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Answer Key:</strong> State clearly: (1) Horizontal dimension represents objects/lifelines; (2) Vertical dimension represents chronological time flowing downwards.
  </div>
</div>
"""
        },
        {
            "id": "sec-18",
            "number": "18",
            "part": "Part 4 — Sequence Diagram",
            "title": "Terms and Symbols in Sequence Diagram",
            "subtitle": "Lifelines, Activation Bars, Synchronous/Asynchronous Messages, Object Destruction & Control Focus",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Notation Master</div>
    <h3>Standard Symbols of Sequence Diagrams</h3>
    <p>To construct semantically accurate sequence diagrams, UML defines seven standardized graphical primitives representing participants, execution control, message types, and object lifecycles.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The Standard Primitives Explained</h4>

  <div class="detail-block">
    <h5>1. Participants and Class Roles</h5>
    <p>Rendered as labeled boxes at the top of the diagram: <code><u>objectName : ClassName</u></code>.</p>
  </div>

  <div class="detail-block">
    <h5>2. Lifelines</h5>
    <p>A vertical dashed line extending downward from the participant box. It represents the existence of an object over time during the interaction.</p>
  </div>

  <div class="detail-block">
    <h5>3. Activation / Execution Occurrence (Focus of Control)</h5>
    <p>A thin vertical rectangle overlaid on top of a lifeline. It denotes the exact period during which the object has the CPU focus of control and is actively performing an operation (either directly or waiting on a nested sub-operation).</p>
  </div>

  <div class="detail-block">
    <h5>4. Types of Messages (Strict UML Arrowhead Rules)</h5>
    <ul>
      <li><strong>Synchronous Call (<code>──▶</code>):</strong> Solid line with a <strong>solid filled triangular arrowhead</strong>. The caller blocks and halts execution until the call finishes.</li>
      <li><strong>Asynchronous Call (<code>──></code>):</strong> Solid line with an <strong>open stick arrowhead</strong>. The caller fires the message and immediately resumes execution without waiting.</li>
      <li><strong>Reply / Return Message (<code>╌╌></code>):</strong> Dashed line with an <strong>open stick arrowhead</strong>. Carries return data back to the caller.</li>
      <li><strong>Found Message:</strong> Originates from an unknown sender outside the diagram (drawn from a black dot).</li>
      <li><strong>Lost Message:</strong> Sent to an unknown recipient outside the system boundary.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>5. Destroying Objects (The Big "X")</h5>
    <p>When an object is destroyed or garbage-collected during execution, its lifeline terminates with a prominent <strong>large "X" symbol</strong>, indicating its death.</p>
  </div>

  <div class="detail-block">
    <h5>6. Combined Fragments (Frames)</h5>
    <p>Rectangular boundary frames with an operator tag in the top-left corner:</p>
    <ul>
      <li><code>alt</code>: Conditional branching (equivalent to <code>if-else</code>).</li>
      <li><code>opt</code>: Optional execution (equivalent to <code>if without else</code>).</li>
      <li><code>loop</code>: Iteration with guard condition <code>[min..max]</code>.</li>
      <li><code>par</code>: Parallel / concurrent thread execution.</li>
    </ul>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Master Symbol Guide for Sequence Diagrams</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="mSync" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <polygon points="0,1 10,5 0,9" fill="#2563eb"/>
        </marker>
        <marker id="mAsync" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#10b981" stroke-width="1.8"/>
        </marker>
        <marker id="mReply" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#64748b" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Symbol 1: Synchronous -->
      <g transform="translate(40, 25)">
        <line x1="0" y1="20" x2="160" y2="20" stroke="#2563eb" stroke-width="2" marker-end="url(#mSync)"/>
        <text x="80" y="12" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">syncCall()</text>
        <text x="180" y="24" font-size="11" fill="var(--text-primary)"><tspan font-weight="bold">Synchronous:</tspan> Solid line + Filled Triangle (Blocks)</text>
      </g>

      <!-- Symbol 2: Asynchronous -->
      <g transform="translate(40, 75)">
        <line x1="0" y1="20" x2="160" y2="20" stroke="#10b981" stroke-width="2" marker-end="url(#mAsync)"/>
        <text x="80" y="12" text-anchor="middle" font-size="11" font-weight="bold" fill="#10b981">asyncSignal()</text>
        <text x="180" y="24" font-size="11" fill="var(--text-primary)"><tspan font-weight="bold">Asynchronous:</tspan> Solid line + Open Arrow (Non-blocking)</text>
      </g>

      <!-- Symbol 3: Reply -->
      <g transform="translate(40, 125)">
        <line x1="0" y1="20" x2="160" y2="20" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#mReply)"/>
        <text x="80" y="12" text-anchor="middle" font-size="11" font-weight="bold" fill="#64748b">returnResult</text>
        <text x="180" y="24" font-size="11" fill="var(--text-primary)"><tspan font-weight="bold">Reply / Return:</tspan> Dashed line + Open Arrow</text>
      </g>

      <!-- Symbol 4: Destruction -->
      <g transform="translate(40, 175)">
        <line x1="80" y1="0" x2="80" y2="35" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,3"/>
        <line x1="68" y1="35" x2="92" y2="59" stroke="#ef4444" stroke-width="3"/>
        <line x1="92" y1="35" x2="68" y2="59" stroke="#ef4444" stroke-width="3"/>
        <text x="180" y="48" font-size="11" fill="var(--text-primary)"><tspan font-weight="bold">Object Destruction:</tspan> Big 'X' terminating the lifeline</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Explain the symbols used in sequence diagrams: lifeline, execution occurrence, synchronous message, asynchronous message, and object destruction."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Examiner Trap:</strong> Drawing an open arrow for a synchronous message is considered a major UML syntax error! Always draw a <strong>solid filled black triangle</strong> for synchronous calls, and an <strong>open stick arrow</strong> for asynchronous messages.
  </div>
</div>
"""
        },
        {
            "id": "sec-19",
            "number": "19",
            "part": "Part 4 — Sequence Diagram",
            "title": "Asynchronous Messages",
            "subtitle": "Non-blocking Invocations, Priority Queues, FIFO Buffering & Multi-priority Scheduling",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Concurrent Processing</div>
    <h3>Meaning of Asynchronous Messages</h3>
    <p>In distributed, multi-threaded, and reactive systems, an <strong>Asynchronous Message</strong> allows a sender to dispatch a request or signal and immediately resume its own processing without waiting for the recipient to receive, process, or acknowledge the message.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Message Queues and Priority Handling</h4>

  <div class="detail-block">
    <h5>1. Asynchronous Message Without Priority (Standard FIFO Queue)</h5>
    <p>In a standard non-priority setup, incoming asynchronous messages are buffered inside a First-In, First-Out (FIFO) queue:</p>
    <ul>
      <li>Messages are appended to the rear of the queue as they arrive.</li>
      <li>The consumer thread pops messages from the front in strict temporal order of arrival.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Asynchronous Message With Priority</h5>
    <p>In real-time and mission-critical systems, certain events (e.g. <code>emergencyHalt()</code>, <code>hardwareFault()</code>) cannot wait behind hundreds of routine requests. Messages carry an explicit <strong>priority tag</strong> (e.g., High, Normal, Low):</p>
    <ul>
      <li>High-priority messages jump ahead of normal messages in the queue.</li>
      <li>A priority queue dispatcher continuously services the highest priority message available.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Multiple Priority Queues Architecture</h5>
    <p>Instead of a single complex sorting heap, modern real-time operating systems and event dispatchers maintain <strong>multiple distinct FIFO queues</strong>—one dedicated to each priority level (e.g., Critical, High, Standard, Background). The scheduler always drains higher queues before touching lower ones.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Asynchronous Messaging & Multi-Priority Queue Buffering</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="asyncQ" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
        <marker id="critQ" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#ef4444" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Producer Lifeline -->
      <g transform="translate(60, 20)">
        <rect width="120" height="35" rx="3" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="60" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:SensorProducer</text>
        <line x1="60" y1="35" x2="60" y2="210" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="55" y="60" width="10" height="130" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Priority Queue Dispatcher (Center) -->
      <g transform="translate(300, 20)">
        <rect width="180" height="35" rx="3" fill="rgba(245, 158, 11, 0.2)" stroke="#d97706" stroke-width="1.5"/>
        <text x="90" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">Priority Message Queue</text>
        <!-- Queue Visual Box -->
        <rect x="15" y="65" width="150" height="120" rx="4" fill="var(--card-bg)" stroke="#d97706" stroke-width="1.5"/>
        <!-- High Priority Slot -->
        <rect x="25" y="75" width="130" height="24" rx="3" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444"/>
        <text x="90" y="91" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">Q1: Emergency Halt [High]</text>
        <!-- Normal Priority Slot -->
        <rect x="25" y="105" width="130" height="24" rx="3" fill="rgba(99, 102, 241, 0.2)" stroke="#3b82f6"/>
        <text x="90" y="121" text-anchor="middle" font-size="10" fill="#2563eb">Q2: Telemetry [Normal]</text>
        <!-- Low Priority Slot -->
        <rect x="25" y="135" width="130" height="24" rx="3" fill="rgba(148, 163, 184, 0.15)" stroke="#94a3b8"/>
        <text x="90" y="151" text-anchor="middle" font-size="10" fill="#64748b">Q3: Log Heartbeat [Low]</text>
      </g>

      <!-- Consumer Lifeline -->
      <g transform="translate(560, 20)">
        <rect width="120" height="35" rx="3" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <text x="60" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:WorkerConsumer</text>
        <line x1="60" y1="35" x2="60" y2="210" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="55" y="90" width="10" height="100" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Asynchronous arrows -->
      <line x1="125" y1="85" x2="315" y2="85" stroke="#ef4444" stroke-width="1.8" marker-end="url(#critQ)"/>
      <text x="215" y="78" text-anchor="middle" font-size="9" font-weight="bold" fill="#dc2626">postEmergency()</text>

      <line x1="125" y1="120" x2="315" y2="120" stroke="#2563eb" stroke-width="1.8" marker-end="url(#asyncQ)"/>
      <text x="215" y="113" text-anchor="middle" font-size="9" fill="#2563eb">postTelemetry()</text>

      <!-- Dispatch to Consumer -->
      <line x1="480" y1="100" x2="615" y2="100" stroke="#ef4444" stroke-width="2" marker-end="url(#critQ)"/>
      <text x="548" y="93" text-anchor="middle" font-size="9" font-weight="bold" fill="#dc2626">dispatchFirst()</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14, 2014-15):</strong> <em>"Discuss asynchronous messages in sequence diagrams. How are priority queues and multiple priority queues handled?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Exam Answer Blueprint:</strong> Differentiate non-priority (FIFO) from priority-based dispatch. Explain that priority messages jump queue positions and mention multiple priority queues where schedulers drain high-priority queues first.
  </div>
</div>
"""
        },
        {
            "id": "sec-20",
            "number": "20",
            "part": "Part 4 — Sequence Diagram",
            "title": "Callback Mechanism",
            "subtitle": "Inversion of Control, Registering Interest, Listener Pattern & Event Notification",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Design Pattern</div>
    <h3>Meaning of Callback Mechanism</h3>
    <p>A <strong>Callback</strong> is a software mechanism implementing <em>Inversion of Control (IoC)</em>. Instead of a client continuously polling a server for long-running task status, the client passes an executable reference (a callback interface or lambda) during registration, and the server invokes that callback when the task completes or an event occurs.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The 3-Phase Callback Lifecycle</h4>

  <div class="detail-block">
    <h5>1. Phase 1: Registering Interest (Subscription)</h5>
    <p>The client issues a synchronous message to the service: <code>registerListener(this)</code> or <code>subscribe(callback)</code>. The server stores this reference in its internal subscriber collection.</p>
  </div>

  <div class="detail-block">
    <h5>2. Phase 2: Asynchronous Trigger (Background Event)</h5>
    <p>The client continues with its independent tasks. Concurrently, the server processes the long-running job (e.g., downloading a massive file, waiting on a payment webhook, or listening for hardware sensor interrupts).</p>
  </div>

  <div class="detail-block">
    <h5>3. Phase 3: Callback Message Invocation</h5>
    <p>Upon event occurrence, the server actively initiates a call <strong>back</strong> to the client: <code>onTaskCompleted(result)</code>. The client handles the result asynchronously.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Sequence Diagram of the Callback Mechanism</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 270" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="cbSync" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <polygon points="0,1 10,5 0,9" fill="#2563eb"/>
        </marker>
        <marker id="cbAsync" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#10b981" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Client Participant -->
      <g transform="translate(100, 20)">
        <rect width="140" height="35" rx="3" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="70" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">client : DownloadUI</text>
        <line x1="70" y1="35" x2="70" y2="230" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="65" y="60" width="10" height="40" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
        <rect x="65" y="170" width="10" height="40" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Server Participant -->
      <g transform="translate(500, 20)">
        <rect width="150" height="35" rx="3" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <text x="75" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">server : DownloadMgr</text>
        <line x1="75" y1="35" x2="75" y2="230" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="70" y="70" width="10" height="120" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Step 1: Register -->
      <line x1="175" y1="75" x2="570" y2="75" stroke="#2563eb" stroke-width="1.8" marker-end="url(#cbSync)"/>
      <text x="372" y="67" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">1: startDownload(url, callbackRef)</text>

      <!-- Server internal processing -->
      <path d="M 580 100 L 610 100 L 610 130 L 580 130" fill="none" stroke="#64748b" stroke-width="1.5"/>
      <text x="618" y="118" font-size="9" fill="var(--text-muted)">downloading bytes...</text>

      <!-- Step 2: Callback Invocation -->
      <line x1="570" y1="180" x2="175" y2="180" stroke="#10b981" stroke-width="2" marker-end="url(#cbAsync)"/>
      <text x="372" y="172" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">2: onDownloadComplete(fileData) [CALLBACK]</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2014-15):</strong> <em>"Explain the callback mechanism in sequence diagrams with an example of event notification."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Examiner Advice:</strong> Point out that the server becomes the caller in Phase 3. Draw the arrow pointing from Server back to Client, and explicitly label it as a callback invocation.
  </div>
</div>
"""
        },
        {
            "id": "sec-21",
            "number": "21",
            "part": "Part 4 — Sequence Diagram",
            "title": "Broadcast Message",
            "subtitle": "Publish-Subscribe, One-to-Many Notification & Event Broker Architecture",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">One-to-Many Interaction</div>
    <h3>Meaning of Broadcast Messages</h3>
    <p>A <strong>Broadcast Message</strong> occurs when a single event or notification originating from one source is transmitted to <strong>multiple recipient objects simultaneously</strong>. This is the structural foundation of the <em>Observer Pattern</em>, <em>Event Bus</em>, and <em>Publish-Subscribe (Pub/Sub)</em> architectural styles.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Representation and Architectural Patterns</h4>

  <div class="detail-block">
    <h5>1. Direct Multi-Branch Representation</h5>
    <p>A single message line originating from the sender forks or fans out into multiple parallel arrowheads targeting different receiver lifelines at the same vertical time coordinate.</p>
  </div>

  <div class="detail-block">
    <h5>2. Event Broker (Mediated Broadcast) Representation</h5>
    <p>In enterprise software, broadcasters do not know their subscribers directly. An intermediary <strong>Event Broker / Event Bus</strong> receives the single broadcast and dispatches asynchronous notifications to all registered listeners.</p>
  </div>

  <div class="detail-block">
    <h5>3. Unicast vs. Multicast vs. Broadcast</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Communication Type</th>
          <th>Recipient Count</th>
          <th>Coupling Level</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Unicast</strong></td>
          <td>Exactly 1 recipient</td>
          <td>Tightly coupled point-to-point</td>
        </tr>
        <tr>
          <td><strong>Multicast</strong></td>
          <td>Selective subset of subscribers</td>
          <td>Decoupled via topic or group ID</td>
        </tr>
        <tr>
          <td><strong>Broadcast</strong></td>
          <td>All available nodes/objects in system</td>
          <td>Fully decoupled global event bus</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Broadcast Event Notification via Event Bus</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 270" width="100%" height="270" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="bcastArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#2563eb" stroke-width="1.8"/>
        </marker>
        <marker id="fanArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9" fill="none" stroke="#8b5cf6" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Broadcaster -->
      <g transform="translate(60, 20)">
        <rect width="130" height="35" rx="3" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="65" y="22" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:OrderService</text>
        <line x1="65" y1="35" x2="65" y2="230" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="60" y="60" width="10" height="40" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Event Bus -->
      <g transform="translate(260, 20)">
        <rect width="130" height="35" rx="3" fill="rgba(139, 92, 246, 0.15)" stroke="#8b5cf6" stroke-width="1.5"/>
        <text x="65" y="22" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">:EventBus</text>
        <line x1="65" y1="35" x2="65" y2="230" stroke="#8b5cf6" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="60" y="70" width="10" height="130" fill="#ddd6fe" stroke="#8b5cf6"/>
      </g>

      <!-- Subscriber 1: EmailService -->
      <g transform="translate(440, 20)">
        <rect width="120" height="35" rx="3" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <text x="60" y="22" text-anchor="middle" font-size="10" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:EmailService</text>
        <line x1="60" y1="35" x2="60" y2="230" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="55" y="110" width="10" height="30" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Subscriber 2: AnalyticsService -->
      <g transform="translate(590, 20)">
        <rect width="130" height="35" rx="3" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <text x="65" y="22" text-anchor="middle" font-size="10" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">:AnalyticsEngine</text>
        <line x1="65" y1="35" x2="65" y2="230" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <rect x="60" y="150" width="10" height="30" class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"/>
      </g>

      <!-- Step 1: Publish -->
      <line x1="130" y1="80" x2="320" y2="80" stroke="#2563eb" stroke-width="2" marker-end="url(#bcastArr)"/>
      <text x="225" y="72" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">publish(OrderPlaced)</text>

      <!-- Step 2: Broadcast Fanout 1 -->
      <line x1="330" y1="120" x2="495" y2="120" stroke="#8b5cf6" stroke-width="1.8" marker-end="url(#fanArr)"/>
      <text x="410" y="112" text-anchor="middle" font-size="9" fill="#7c3aed">notify(OrderPlaced)</text>

      <!-- Step 3: Broadcast Fanout 2 -->
      <line x1="330" y1="160" x2="650" y2="160" stroke="#8b5cf6" stroke-width="1.8" marker-end="url(#fanArr)"/>
      <text x="490" y="152" text-anchor="middle" font-size="9" fill="#7c3aed">notify(OrderPlaced)</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2015-16):</strong> <em>"How is broadcast messaging implemented in a sequence diagram? Differentiate between unicast and broadcast communication."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Illustrate either the forked-arrow convention or the Event Bus mediator pattern. Mention that broadcast messages are always asynchronous in nature because the publisher does not wait for each listener to reply.
  </div>
</div>
"""
        }
    ]
