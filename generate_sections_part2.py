# generate_sections_part2.py: Part 2 - Class and Object Diagram (Sections 7 to 10)

def get_part2_sections():
    return [
        {
            "id": "sec-7",
            "number": "07",
            "part": "Part 2 — Class and Object Diagram",
            "title": "Class Diagram",
            "subtitle": "Static System View, Notation, Multiplicities & Modeling Real-World Domains",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational Diagram</div>
    <h3>Definition and Purpose of Class Diagrams</h3>
    <p>A <strong>Class Diagram</strong> is the foundational structural diagram in Object-Oriented Modeling. It provides a <strong>static view</strong> of the system by modeling the classes that populate the domain, their internal structures (attributes and operations), and the static semantic relationships (associations, generalizations, dependencies) connecting them.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Architectural Components</h4>

  <div class="detail-block">
    <h5>1. The Static View of a System</h5>
    <p>A class diagram does not capture time, method invocations, or data transformations. Instead, it defines the invariant rules of the universe in which the software operates. It serves three distinct phases:</p>
    <ul>
      <li><strong>Conceptual Phase:</strong> Captures domain vocabulary and business entities without implementation details.</li>
      <li><strong>Specification / Design Phase:</strong> Defines software interfaces, contracts, parameter types, and architectural abstractions.</li>
      <li><strong>Implementation Phase:</strong> Maps directly to source code classes, database relational schemas, or ORM entities.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Relationships and Constraints in Class Diagrams</h5>
    <p>Classes connect through rich semantic relationships:</p>
    <ul>
      <li><strong>Associations with Multiplicities:</strong> Specifies allowable instances (e.g. <code>1</code> to <code>1..*</code>).</li>
      <li><strong>Role Names:</strong> Labels the function a class plays in the association (e.g., <code>employer</code> vs <code>employee</code>).</li>
      <li><strong>Navigability:</strong> Indicated by arrowheads; shows which class maintains a reference to the other.</li>
      <li><strong>Constraints:</strong> Tagged rules such as <code>{ordered}</code>, <code>{unique}</code>, or <code>{xor}</code> governing association links.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Comprehensive Real-World Example: Library Management System</h5>
    <p>Let us consider a university library management system showing classes, attributes, operations, multiplicities, aggregation, and inheritance:</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Library Management System Class Diagram</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 320" width="100%" height="320" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="triGen" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="9" markerHeight="9" orient="auto">
          <polygon points="0,1 11,6 0,11" fill="#fff" stroke="#10b981" stroke-width="1.8"/>
        </marker>
      </defs>

      <!-- Library Class -->
      <g transform="translate(30, 20)">
        <rect width="180" height="90" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect width="180" height="26" fill="#3b82f6" fill-opacity="0.15"/>
        <text x="90" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">Library</text>
        <line x1="0" y1="26" x2="180" y2="26" stroke="#3b82f6"/>
        <text x="8" y="42" font-size="10" fill="var(--text-primary)">- name : String</text>
        <text x="8" y="56" font-size="10" fill="var(--text-primary)">- address : String</text>
        <line x1="0" y1="62" x2="180" y2="62" stroke="#3b82f6"/>
        <text x="8" y="77" font-size="10" fill="var(--text-primary)">+ openLibrary() : void</text>
      </g>

      <!-- Aggregation to Book -->
      <!-- Diamond on Library -->
      <polygon points="120,110 126,120 120,130 114,120" fill="#fff" stroke="#f59e0b" stroke-width="2"/>
      <line x1="120" y1="130" x2="120" y2="160" stroke="#f59e0b" stroke-width="2"/>
      <text x="130" y="150" font-size="10" fill="#f59e0b">1..*</text>

      <!-- Book Class -->
      <g transform="translate(30, 160)">
        <rect width="180" height="110" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect width="180" height="26" fill="#3b82f6" fill-opacity="0.15"/>
        <text x="90" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">Book</text>
        <line x1="0" y1="26" x2="180" y2="26" stroke="#3b82f6"/>
        <text x="8" y="42" font-size="10" fill="var(--text-primary)">- isbn : String</text>
        <text x="8" y="56" font-size="10" fill="var(--text-primary)">- title : String</text>
        <text x="8" y="70" font-size="10" fill="var(--text-primary)">- isIssued : boolean</text>
        <line x1="0" y1="76" x2="180" y2="76" stroke="#3b82f6"/>
        <text x="8" y="92" font-size="10" fill="var(--text-primary)">+ checkOut() : void</text>
        <text x="8" y="104" font-size="10" fill="var(--text-primary)">+ returnBook() : void</text>
      </g>

      <!-- Association between Book and Patron -->
      <line x1="210" y1="200" x2="350" y2="200" stroke="#64748b" stroke-width="2"/>
      <text x="220" y="193" font-size="10" fill="var(--text-muted)">0..* borrows</text>
      <text x="325" y="193" font-size="10" fill="var(--text-muted)">0..1</text>

      <!-- Patron Class -->
      <g transform="translate(350, 160)">
        <rect width="180" height="95" rx="4" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect width="180" height="26" fill="#3b82f6" fill-opacity="0.15"/>
        <text x="90" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">Patron</text>
        <line x1="0" y1="26" x2="180" y2="26" stroke="#3b82f6"/>
        <text x="8" y="42" font-size="10" fill="var(--text-primary)">- patronId : String</text>
        <text x="8" y="56" font-size="10" fill="var(--text-primary)">- name : String</text>
        <line x1="0" y1="62" x2="180" y2="62" stroke="#3b82f6"/>
        <text x="8" y="78" font-size="10" fill="var(--text-primary)">+ getBorrowedBooks()</text>
      </g>

      <!-- Generalization from Student &amp; Faculty to Patron -->
      <line x1="440" y1="160" x2="440" y2="100" stroke="#10b981" stroke-width="2" marker-end="url(#triGen)"/>
      
      <!-- General Class Person -->
      <g transform="translate(350, 10)">
        <rect width="180" height="80" rx="4" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <rect width="180" height="26" fill="#10b981" fill-opacity="0.15"/>
        <text x="90" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">&lt;&lt;abstract&gt;&gt; Person</text>
        <line x1="0" y1="26" x2="180" y2="26" stroke="#10b981"/>
        <text x="8" y="42" font-size="10" fill="var(--text-primary)"># name : String</text>
        <text x="8" y="56" font-size="10" fill="var(--text-primary)"># email : String</text>
        <line x1="0" y1="62" x2="180" y2="62" stroke="#10b981"/>
        <text x="8" y="74" font-size="10" fill="var(--text-primary)">+ getContact() : String</text>
      </g>
      <line x1="440" y1="160" x2="440" y2="90" stroke="#10b981" stroke-width="2" marker-end="url(#triGen)"/>

      <!-- Notes/Constraints callout -->
      <g transform="translate(560, 175)">
        <rect width="170" height="70" rx="4" fill="rgba(245, 158, 11, 0.2)" stroke="#d97706" stroke-width="1.5"/>
        <text x="85" y="20" text-anchor="middle" font-size="10" font-weight="bold" fill="#b45309">Constraint Rule</text>
        <text x="10" y="38" font-size="9" fill="#92400e">{ maxBooks &lt;= 5 }</text>
        <text x="10" y="52" font-size="9" fill="#92400e">Undergrad loan period</text>
        <text x="10" y="64" font-size="9" fill="#92400e">cannot exceed 14 days.</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14, 2014-15):</strong> <em>"Explain the class diagram with a suitable example. Discuss classes, attributes, operations, and relationships."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Full Marks Strategy:</strong> Never draw an isolated class! Always draw at least 3 connected classes (e.g. <code>Library</code>, <code>Book</code>, <code>Patron</code>) with multiplicities (<code>1</code>, <code>1..*</code>), visibilities (<code>+</code>, <code>-</code>, <code>#</code>), and relationship types clearly labeled.
  </div>
</div>
"""
        },
        {
            "id": "sec-8",
            "number": "08",
            "part": "Part 2 — Class and Object Diagram",
            "title": "Object Diagram",
            "subtitle": "Runtime Snapshots, Object Notation, Attribute Values & Links vs Associations",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Instance Snapshot</div>
    <h3>Meaning of Object Diagram</h3>
    <p>An <strong>Object Diagram</strong> (also called an <em>Instance Diagram</em>) represents a <strong>static snapshot of a system at a particular moment in runtime execution</strong>. While a class diagram models abstract rules and templates, an object diagram portrays the concrete objects that exist in memory, their current attribute values, and the real links instantiated between them.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>Key Subtopics & Syntax Rules</h4>

  <div class="detail-block">
    <h5>1. Object as an Instance of a Class</h5>
    <p>An object is an entity with concrete state, behavior, and identity:</p>
    <ul>
      <li><strong>State:</strong> Represented by exact values assigned to attributes at that instant (e.g., <code>balance = 5000.50</code>).</li>
      <li><strong>Identity:</strong> Every object is distinct, even if its attribute values match another object.</li>
      <li><strong>Notation Rule:</strong> The name compartment of an object is <strong>ALWAYS UNDERLINED</strong>.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Object Name Syntax Options</h5>
    <p>In UML, object headers follow three standard conventions (all underlined):</p>
    <ol>
      <li><code><u>objectName : ClassName</u></code> — Named object of a known class (e.g., <code><u>book1 : Book</u></code>).</li>
      <li><code><u>: ClassName</u></code> — <strong>Anonymous Object</strong>: The object identity is unnamed, but its class type is known.</li>
      <li><code><u>objectName</u></code> — An object whose class is either implied or unspecified.</li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>3. Links Between Objects</h5>
    <p>A <strong>Link</strong> is an instance of an association. If an association exists between class <code>Book</code> and class <code>Patron</code>, then a runtime link can exist between <code>book1</code> and <code>johnDoe</code>. Important differences:</p>
    <ul>
      <li>Links do <strong>NOT</strong> have multiplicities (multiplicity is a class-level rule). A link simply exists or does not exist.</li>
      <li>Links connect specific object instances with solid lines.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>4. Comprehensive Comparison: Class Diagram vs. Object Diagram</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Feature</th>
          <th>Class Diagram</th>
          <th>Object Diagram</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Nature</strong></td>
          <td>Abstract template / blueprint</td>
          <td>Concrete runtime snapshot</td>
        </tr>
        <tr>
          <td><strong>Header Syntax</strong></td>
          <td>Plain bold text: <code>ClassName</code></td>
          <td><u>Underlined</u> text: <code><u>obj : ClassName</u></code></td>
        </tr>
        <tr>
          <td><strong>Compartments</strong></td>
          <td>3 compartments (Name, Attributes, Operations)</td>
          <td>2 compartments (Name, Attribute Values). <em>Operations omitted!</em></td>
        </tr>
        <tr>
          <td><strong>Attribute Content</strong></td>
          <td>Attribute names and data types (<code>price : float</code>)</td>
          <td>Specific runtime values (<code>price = 49.99</code>)</td>
        </tr>
        <tr>
          <td><strong>Connections</strong></td>
          <td>Associations with multiplicities (<code>1..*</code>)</td>
          <td>Links (instances of associations, no multiplicities)</td>
        </tr>
        <tr>
          <td><strong>Time Dimension</strong></td>
          <td>Invariant across entire system life</td>
          <td>Valid only at one frozen instant of time</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Class Diagram (Template) vs Object Diagram (Snapshot)</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: Class Diagram -->
      <g transform="translate(30, 20)">
        <rect width="320" height="215" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <rect width="320" height="30" rx="8" fill="#3b82f6" fill-opacity="0.15"/>
        <text x="160" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">CLASS DIAGRAM (Schema / Type Level)</text>
        
        <!-- Class 1: Order -->
        <rect x="20" y="50" width="120" height="65" rx="3" fill="var(--bg-secondary)" stroke="#3b82f6"/>
        <text x="80" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Order</text>
        <line x1="20" y1="75" x2="140" y2="75" stroke="#3b82f6"/>
        <text x="25" y="90" font-size="9" fill="var(--text-primary)">- orderId : int</text>
        <text x="25" y="103" font-size="9" fill="var(--text-primary)">- total : double</text>

        <!-- Association Line -->
        <line x1="140" y1="85" x2="190" y2="85" stroke="#3b82f6" stroke-width="1.8"/>
        <text x="145" y="78" font-size="9" fill="#3b82f6">1</text>
        <text x="175" y="78" font-size="9" fill="#3b82f6">1..*</text>

        <!-- Class 2: Item -->
        <rect x="190" y="50" width="110" height="65" rx="3" fill="var(--bg-secondary)" stroke="#3b82f6"/>
        <text x="245" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--text-primary)">Item</text>
        <line x1="190" y1="75" x2="300" y2="75" stroke="#3b82f6"/>
        <text x="195" y="90" font-size="9" fill="var(--text-primary)">- sku : String</text>
        <text x="195" y="103" font-size="9" fill="var(--text-primary)">- price : double</text>
        
        <text x="160" y="170" text-anchor="middle" font-size="10" fill="var(--text-muted)">Defines types, fields, and multiplicity rules.</text>
      </g>

      <!-- Right: Object Diagram -->
      <g transform="translate(390, 20)">
        <rect width="340" height="215" rx="8" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <rect width="340" height="30" rx="8" fill="#10b981" fill-opacity="0.15"/>
        <text x="170" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">OBJECT DIAGRAM (Runtime Snapshot at t = 10:15 AM)</text>
        
        <!-- Instance 1: Order -->
        <rect x="15" y="50" width="135" height="65" rx="3" fill="var(--bg-secondary)" stroke="#10b981"/>
        <text x="82" y="68" text-anchor="middle" font-size="11" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">o101 : Order</text>
        <line x1="15" y1="75" x2="150" y2="75" stroke="#10b981"/>
        <text x="20" y="90" font-size="9" fill="var(--text-primary)">orderId = 101</text>
        <text x="20" y="103" font-size="9" fill="var(--text-primary)">total = 149.50</text>

        <!-- Links to two item instances -->
        <line x1="150" y1="70" x2="195" y2="60" stroke="#10b981" stroke-width="1.8"/>
        <line x1="150" y1="90" x2="195" y2="135" stroke="#10b981" stroke-width="1.8"/>

        <!-- Instance 2: Item 1 -->
        <rect x="195" y="40" width="130" height="55" rx="3" fill="var(--bg-secondary)" stroke="#10b981"/>
        <text x="260" y="56" text-anchor="middle" font-size="10" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">item1 : Item</text>
        <line x1="195" y1="62" x2="325" y2="62" stroke="#10b981"/>
        <text x="200" y="75" font-size="9" fill="var(--text-primary)">sku = "KBD-99"</text>
        <text x="200" y="87" font-size="9" fill="var(--text-primary)">price = 99.50</text>

        <!-- Instance 3: Item 2 -->
        <rect x="195" y="115" width="130" height="55" rx="3" fill="var(--bg-secondary)" stroke="#10b981"/>
        <text x="260" y="131" text-anchor="middle" font-size="10" font-weight="bold" text-decoration="underline" fill="var(--text-primary)">item2 : Item</text>
        <line x1="195" y1="137" x2="325" y2="137" stroke="#10b981"/>
        <text x="200" y="150" font-size="9" fill="var(--text-primary)">sku = "MOU-50"</text>
        <text x="200" y="162" font-size="9" fill="var(--text-primary)">price = 50.00</text>

        <text x="170" y="195" text-anchor="middle" font-size="10" fill="var(--text-muted)">Concrete objects, explicit values, and links (no operations!).</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2013-14):</strong> <em>"What is the difference between a class diagram and an instance/object diagram? Prepare an object diagram for a library book checkout system."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Crucial Examiner Alert:</strong> In exams, 90% of lost marks occur because students forget to <strong>UNDERLINE the object name</strong> or mistakenly include operations inside object boxes. Never draw operations in an object diagram!
  </div>
</div>
"""
        },
        {
            "id": "sec-9",
            "number": "09",
            "part": "Part 2 — Class and Object Diagram",
            "title": "Terms and Concepts of Class/Object Diagrams",
            "subtitle": "Class, Object, Attribute, Operation, Association, Link, Multiplicity & Constraints",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Terminology Master</div>
    <h3>Core Vocabulary for Structural Modeling</h3>
    <p>To master structural modeling, you must possess an unambiguous grasp of the ten fundamental terms that form the backbone of both class and object diagrams.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The 10 Essential Concepts Explained</h4>

  <div class="detail-block">
    <h5>1. Class vs. 2. Object</h5>
    <p>A <strong>Class</strong> is an abstract descriptor and classifier that defines a set of features (properties and behavior). An <strong>Object</strong> is a discrete concrete instance of a class that occupies runtime memory and maintains a unique identity and specific state.</p>
  </div>

  <div class="detail-block">
    <h5>3. Attribute vs. 4. Operation</h5>
    <p>An <strong>Attribute</strong> is a named property of a class that describes a range of values that instances may hold. An <strong>Operation</strong> is the implementation of a service that can be requested from any object of the class to affect behavior or mutate state.</p>
  </div>

  <div class="detail-block">
    <h5>5. Association vs. 6. Link</h5>
    <p>An <strong>Association</strong> is a structural relationship between classifiers describing a set of connections among instances. A <strong>Link</strong> is a specific physical or conceptual connection among objects (a tuple of object references); it is literally an <em>instance of an association</em>.</p>
  </div>

  <div class="detail-block">
    <h5>7. Generalization vs. 8. Aggregation</h5>
    <p><strong>Generalization</strong> is a taxonomic relationship between a general classifier and a specific classifier (<em>"is-a"</em>). <strong>Aggregation</strong> is a specialized association specifying a whole-part hierarchy (<em>"has-a"</em> or <em>"part-of"</em>).</p>
  </div>

  <div class="detail-block">
    <h5>9. Multiplicity & 10. Constraints</h5>
    <p><strong>Multiplicity</strong> defines the allowable cardinality range of instances that can participate in a relationship:</p>
    <ul>
      <li><code>1</code> or <code>1..1</code>: Exactly one instance.</li>
      <li><code>0..1</code>: Zero or one (optional).</li>
      <li><code>*</code> or <code>0..*</code>: Zero or many (unbounded).</li>
      <li><code>1..*</code>: At least one, up to many.</li>
      <li><code>m..n</code>: Specified range from m to n.</li>
    </ul>
    <p>A <strong>Constraint</strong> is an extension mechanism specifying a condition or proposition that must hold true for the model element, declared within curly braces: <code>{age &gt;= 0}</code>, <code>{ordered}</code>, <code>{frozen}</code>.</p>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: Conceptual Mapping (Class Term -> Object Counterpart)</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="mapArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#8b5cf6"/>
        </marker>
      </defs>

      <!-- Left Column: Class Diagram Domain -->
      <g transform="translate(60, 25)">
        <rect width="250" height="160" rx="8" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="2"/>
        <text x="125" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">CLASS LEVEL CONCEPTS</text>
        <line x1="20" y1="35" x2="230" y2="35" stroke="var(--border-color)"/>
        <text x="30" y="58" font-size="11" fill="var(--text-primary)">• Class (Abstraction / Type)</text>
        <text x="30" y="80" font-size="11" fill="var(--text-primary)">• Attribute (Type descriptor)</text>
        <text x="30" y="102" font-size="11" fill="var(--text-primary)">• Operation (Method signature)</text>
        <text x="30" y="124" font-size="11" fill="var(--text-primary)">• Association (Semantic link rule)</text>
        <text x="30" y="146" font-size="11" fill="var(--text-primary)">• Multiplicity (Range: 1..*)</text>
      </g>

      <!-- Center mapping arrows -->
      <line x1="320" y1="65" x2="420" y2="65" stroke="#8b5cf6" stroke-width="2" marker-end="url(#mapArr)"/>
      <text x="370" y="58" text-anchor="middle" font-size="9" fill="#7c3aed">instantiates</text>

      <line x1="320" y1="130" x2="420" y2="130" stroke="#8b5cf6" stroke-width="2" marker-end="url(#mapArr)"/>
      <text x="370" y="123" text-anchor="middle" font-size="9" fill="#7c3aed">realizes</text>

      <!-- Right Column: Object Diagram Domain -->
      <g transform="translate(440, 25)">
        <rect width="250" height="160" rx="8" fill="var(--card-bg)" stroke="#10b981" stroke-width="2"/>
        <text x="125" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">OBJECT LEVEL CONCEPTS</text>
        <line x1="20" y1="35" x2="230" y2="35" stroke="var(--border-color)"/>
        <text x="30" y="58" font-size="11" fill="var(--text-primary)">• Object (Instance with Identity)</text>
        <text x="30" y="80" font-size="11" fill="var(--text-primary)">• Slot / Value (Concrete data)</text>
        <text x="30" y="102" font-size="11" fill="var(--text-muted)">• <tspan font-style="italic">(Omitted in snapshot)</tspan></text>
        <text x="30" y="124" font-size="11" fill="var(--text-primary)">• Link (Concrete tuple reference)</text>
        <text x="30" y="146" font-size="11" fill="var(--text-primary)">• Exact count of linked objects</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>Short Note Question:</strong> <em>"Define the following: (i) Link, (ii) Multiplicity, (iii) Constraint, (iv) Abstract Class."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Quick Scoring Definitions:</strong>
    <ul>
      <li><strong>Link:</strong> An instance of an association representing a concrete connection between two specific objects.</li>
      <li><strong>Multiplicity:</strong> The specification of the allowable range of cardinality that an association end may have.</li>
      <li><strong>Constraint:</strong> A condition that extends semantics and must be evaluated as true at all times.</li>
    </ul>
  </div>
</div>
"""
        },
        {
            "id": "sec-10",
            "number": "10",
            "part": "Part 2 — Class and Object Diagram",
            "title": "Modeling Techniques for Class and Object Diagrams",
            "subtitle": "Noun Extraction, Identifying Responsibilities, Multiplicity Representation & Validation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Engineering Methodology</div>
    <h3>Step-by-Step Modeling Methodology</h3>
    <p>How do software architects transform ambiguous english problem statements into rigorous, bug-free UML Class and Object Diagrams? By following a disciplined 7-step engineering pipeline based on the classic <strong>Abbott Grammatical Analysis Method</strong>.</p>
  </div>
</div>

<div class="subtopics-container">
  <h4>The 7-Step Modeling Pipeline</h4>

  <div class="detail-block">
    <h5>Step 1: Identify Classes (Noun Extraction Method)</h5>
    <p>Analyze the system requirements document and highlight all <strong>nouns and noun phrases</strong>. Candidate nouns represent candidate classes:</p>
    <ul>
      <li><em>Rule:</em> Filter out synonyms, system boundaries, and primitive values (e.g. <code>Customer</code>, <code>Order</code>, <code>Invoice</code> are classes; <code>String</code>, <code>Age</code> are attributes).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Step 2: Identify Attributes and Operations (State vs. Action)</h5>
    <ul>
      <li><strong>Attributes (Adjectives / Possessive Nouns):</strong> Properties that describe an object's state (e.g., customer name, order date).</li>
      <li><strong>Operations (Verbs / Verb Phrases):</strong> Actions, requests, or services performed by or on the object (e.g., <code>calculateDiscount()</code>, <code>cancelOrder()</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Step 3: Identify and Categorize Relationships</h5>
    <p>Examine how entities interact:</p>
    <ul>
      <li><em>"A is a B"</em> &rarr; <strong>Generalization</strong> (e.g. SavingsAccount is an Account).</li>
      <li><em>"A has a B" (part cannot exist alone)</em> &rarr; <strong>Composition</strong> (e.g. Order has OrderLineItems).</li>
      <li><em>"A has a B" (part can exist alone)</em> &rarr; <strong>Aggregation</strong> (e.g. Team has Players).</li>
      <li><em>"A works with / references B"</em> &rarr; <strong>Association</strong> (e.g. Customer places Order).</li>
      <li><em>"A temporarily uses B"</em> &rarr; <strong>Dependency</strong> (e.g. Order uses PaymentService).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Step 4: Represent Multiplicities Accurately</h5>
    <p>Ask boundary questions for both directions of the association: <em>"Can a Customer exist with 0 Orders? Yes (0..*). Can an Order exist without a Customer? No (1..1)."</em></p>
  </div>

  <div class="detail-block">
    <h5>Step 5: Convert Conceptual Model to Formal Class/Object Diagrams</h5>
    <p>Draw the 3-compartment class boxes, attach association lines, assign role names, and add necessary constraints (e.g. <code>{ordered}</code>).</p>
  </div>

  <div class="detail-block">
    <h5>Step 6: Instantiate Object Diagram Test Snapshots</h5>
    <p>Create an instance diagram with concrete values to sanity-check corner cases (e.g. what does a customer with zero orders look like? what does a cancelled order link to?).</p>
  </div>

  <div class="detail-block">
    <h5>Step 7: Validating the Diagram (Architectural Checklist)</h5>
    <table class="styled-table">
      <thead>
        <tr>
          <th>Validation Check</th>
          <th>Verification Rule</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Completeness</strong></td>
          <td>Does every use case requirement have supporting classes, attributes, and operations?</td>
        </tr>
        <tr>
          <td><strong>Minimality</strong></td>
          <td>Are there redundant classes, orphan classes with no links, or unused attributes?</td>
        </tr>
        <tr>
          <td><strong>Consistency</strong></td>
          <td>Do role names and navigabilities align with real-world business constraints?</td>
        </tr>
        <tr>
          <td><strong>Decoupling</strong></td>
          <td>Are high-level classes decoupled from volatile implementations via interfaces?</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="diagram-container">
  <h4>Visual Model: 7-Step Requirements-to-UML Workflow</h4>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 140" width="100%" height="140" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="wfArr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#3b82f6"/>
        </marker>
      </defs>
      <!-- Step 1 -->
      <g transform="translate(10, 30)">
        <rect width="130" height="80" rx="6" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="65" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Step 1: Nouns</text>
        <text x="65" y="44" text-anchor="middle" font-size="9" fill="var(--text-primary)">Extract Candidate</text>
        <text x="65" y="58" text-anchor="middle" font-size="9" fill="var(--text-primary)">Classes</text>
      </g>
      <line x1="140" y1="70" x2="160" y2="70" stroke="#3b82f6" stroke-width="2" marker-end="url(#wfArr)"/>

      <!-- Step 2 -->
      <g transform="translate(160, 30)">
        <rect width="130" height="80" rx="6" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="65" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Step 2: Verbs</text>
        <text x="65" y="44" text-anchor="middle" font-size="9" fill="var(--text-primary)">Extract Attributes</text>
        <text x="65" y="58" text-anchor="middle" font-size="9" fill="var(--text-primary)">&amp; Operations</text>
      </g>
      <line x1="290" y1="70" x2="310" y2="70" stroke="#3b82f6" stroke-width="2" marker-end="url(#wfArr)"/>

      <!-- Step 3 -->
      <g transform="translate(310, 30)">
        <rect width="130" height="80" rx="6" fill="var(--card-bg)" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="65" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Step 3: Relations</text>
        <text x="65" y="44" text-anchor="middle" font-size="9" fill="var(--text-primary)">Classify Links &amp;</text>
        <text x="65" y="58" text-anchor="middle" font-size="9" fill="var(--text-primary)">Multiplicities</text>
      </g>
      <line x1="440" y1="70" x2="460" y2="70" stroke="#3b82f6" stroke-width="2" marker-end="url(#wfArr)"/>

      <!-- Step 4 -->
      <g transform="translate(460, 30)">
        <rect width="130" height="80" rx="6" fill="var(--card-bg)" stroke="#10b981" stroke-width="1.5"/>
        <text x="65" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">Step 4: Draw UML</text>
        <text x="65" y="44" text-anchor="middle" font-size="9" fill="var(--text-primary)">Construct Class &amp;</text>
        <text x="65" y="58" text-anchor="middle" font-size="9" fill="var(--text-primary)">Object Models</text>
      </g>
      <line x1="590" y1="70" x2="610" y2="70" stroke="#10b981" stroke-width="2" marker-end="url(#wfArr)"/>

      <!-- Step 5 -->
      <g transform="translate(610, 30)">
        <rect width="135" height="80" rx="6" fill="var(--card-bg)" stroke="#8b5cf6" stroke-width="1.5"/>
        <text x="67" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="#7c3aed">Step 5: Validate</text>
        <text x="67" y="44" text-anchor="middle" font-size="9" fill="var(--text-primary)">Verify Consistency</text>
        <text x="67" y="58" text-anchor="middle" font-size="9" fill="var(--text-primary)">&amp; Completeness</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2012-13):</strong> <em>"Discuss the modeling techniques for class and object diagrams. Explain how multiplicity is identified and represented."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Key Tip:</strong> Frame your answer around the <strong>Noun-Verb Analysis</strong>: Nouns become Classes, Adjectives become Attributes, Verbs become Operations, and Prepositional phrases (<em>"belongs to"</em>, <em>"works in"</em>) become Associations.
  </div>
</div>
"""
        }
    ]
