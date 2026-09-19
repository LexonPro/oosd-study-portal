# generate_unit1_part1.py: Part 1 - Object-Oriented Concepts (Sections 01 to 03)

def get_unit1_part1_sections():
    return [
        {
            "id": "u1-sec-1",
            "number": "01",
            "part": "Part 1 — Object-Oriented Concepts",
            "title": "Meaning of Object Orientation",
            "subtitle": "Core Elements: Objects, Attributes, Behaviors, Classes, Methods & Message Passing",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Core Paradigm</div>
    <h3>What is Object Orientation?</h3>
    <p><strong>Object Orientation (OO)</strong> is a software development paradigm that organizes software design around <strong>data (objects)</strong> rather than functions and logic. In this approach, a system is modeled as a collection of cooperating autonomous objects, each encapsulating its own private state and operations.</p>
    <p>According to standard engineering literature and AKTU Quantum (Que 1.2), an object-oriented system is fundamentally composed of six core elements: <strong>Objects, Attributes, Behavior, Classes, Methods, and Message Passing</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The University Campus Ecosystem</div>
  <p>Think of a university campus. The university is not a giant monolithic list of rules. Instead, it is populated by real-world autonomous entities: <strong>Students, Professors, and Bank Accounts</strong>. Each student has unique attributes (Roll Number, Name, GPA) and behaviors (attending lectures, taking exams). When the Dean wants to inspect a student's grades, the Dean does not directly rewire the student's brain; the Dean sends a message (<em>"Please submit your transcript"</em>), and the student executes the request!</p>
</div>

<div class="subtopics-container">
  <h4>The 6 Fundamental Elements of an OO System</h4>

  <div class="detail-block">
    <h5>1.1 Object (Data + Behavior)</h5>
    <p>An <strong>Object</strong> is a tangible or intangible entity existing within the problem domain that possesses:</p>
    <ul>
      <li><strong>State:</strong> Represented by its internal data values (attributes).</li>
      <li><strong>Behavior:</strong> What the object can do (operations).</li>
      <li><strong>Unique Identity:</strong> Distinguishes it from all other objects in memory.</li>
      <li><strong>Tangible Examples:</strong> <code>Student</code>, <code>Employee</code>, <code>Patient</code>.</li>
      <li><strong>Intangible Examples:</strong> <code>BankAccount</code>, <code>FlightReservation</code>, <code>SecurityToken</code>.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>1.2 Attributes (Object State)</h5>
    <p>Attributes represent the information or properties associated with an object. For a <code>Student</code> entity, attributes include <code>name</code> (string), <code>rollNumber</code> (integer), and <code>age</code> (integer).</p>
  </div>

  <div class="detail-block">
    <h5>1.3 Behavior &amp; Operations</h5>
    <p>Behavior defines what an object can do and how it responds to external stimuli. For a <code>Student</code>, behaviors include <code>study()</code>, <code>attendClass()</code>, and <code>giveExam()</code>.</p>
  </div>

  <div class="detail-block">
    <h5>1.4 Class (Blueprint vs Instance)</h5>
    <p>A <strong>Class</strong> is an abstract template or blueprint that groups similar objects sharing identical attributes, operations, relationships, and semantics. While a class exists at compile time as a type definition, objects are instantiated instances occupying physical memory at runtime.</p>
  </div>

  <div class="detail-block">
    <h5>1.5 Methods</h5>
    <p>A <strong>Method</strong> is the concrete procedural code implementation of an operation defined within a class. Methods determine and realize the behavior of the class.</p>
  </div>

  <div class="detail-block">
    <h5>1.6 Message Passing</h5>
    <p>In object orientation, objects communicate strictly through <strong>Message Passing</strong>. One object sends a message to another object requesting it to invoke one of its public methods (e.g., sending the message <code>getSalary()</code> to an <code>Employee</code> object). The receiver executes the corresponding method and returns the response.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Core Comparison: Class vs Object</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Class (Type Definition)</th>
        <th>Object (Instance)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Definition</strong></td>
        <td>Blueprint or user-defined prototype for creating objects</td>
        <td>A concrete, real-world instance created from a class</td>
      </tr>
      <tr>
        <td><strong>Memory Allocation</strong></td>
        <td>Allocates no physical memory when declared (just a type)</td>
        <td>Allocated physical memory in Stack or Heap on creation</td>
      </tr>
      <tr>
        <td><strong>Existence</strong></td>
        <td>Purely logical concept existing at compile time</td>
        <td>Physical entity with unique memory identity at runtime</td>
      </tr>
      <tr>
        <td><strong>Cardinality</strong></td>
        <td>Declared once in source code</td>
        <td>Can be instantiated many times (e.g. 10,000 students)</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Objects, Classes &amp; Message Passing)</span>
    <span class="code-desc">Demonstrating attributes, methods, and message passing between objects</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">/* 1. Class: The Blueprint defining common attributes &amp; behaviors */</span>
<span class="c-keyword">class</span> <span class="c-type">Student</span> {
<span class="c-keyword">private:</span>
    <span class="c-comment">/* 1.2 Attributes: Internal data state */</span>
    std::string name;
    <span class="c-type">int</span> rollNumber;
    <span class="c-type">double</span> gpa;

<span class="c-keyword">public:</span>
    <span class="c-comment">/* Constructor: Initializes the object instance */</span>
    Student(std::string n, <span class="c-type">int</span> roll, <span class="c-type">double</span> g) 
        : name(n), rollNumber(roll), gpa(g) {}

    <span class="c-comment">/* 1.3 &amp; 1.5 Behaviors &amp; Methods */</span>
    <span class="c-type">void</span> study(<span class="c-type">int</span> hours) {
        std::cout &lt;&lt; <span class="c-string">"["</span> &lt;&lt; name &lt;&lt; <span class="c-string">"] Studied for "</span> &lt;&lt; hours &lt;&lt; <span class="c-string">" hours."</span> &lt;&lt; std::endl;
        gpa += (hours * 0.02); <span class="c-comment">/* Updating internal state */</span>
    }

    <span class="c-comment">/* Message response method */</span>
    <span class="c-type">double</span> getGPA() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> gpa;
    }

    std::string getName() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> name;
    }
};

<span class="c-comment">/* Second Entity: Teacher interacting via Message Passing */</span>
<span class="c-keyword">class</span> <span class="c-type">Teacher</span> {
<span class="c-keyword">public:</span>
    <span class="c-type">void</span> evaluateStudent(<span class="c-type">Student</span>&amp; s) {
        <span class="c-comment">/* 1.6 Message Passing: Teacher sends message 'getGPA()' to Student object */</span>
        std::cout &lt;&lt; <span class="c-string">"[Teacher] Inquiring GPA of "</span> &lt;&lt; s.getName() &lt;&lt; <span class="c-string">": "</span> 
                  &lt;&lt; s.getGPA() &lt;&lt; std::endl;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">/* 1.1 Object Instantiation: Concrete entities in memory */</span>
    <span class="c-type">Student</span> s1(<span class="c-string">"Aarav"</span>, 101, 8.5);
    <span class="c-type">Teacher</span> prof;

    s1.study(5); <span class="c-comment">/* Invoking behavior */</span>
    prof.evaluateStudent(s1); <span class="c-comment">/* Message passing */</span>

    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Anatomy of an Object-Oriented System</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Class Blueprint (Left) -->
      <rect x="40" y="30" width="240" height="220" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <rect x="40" y="30" width="240" height="35" rx="8" fill="#0284c7"/>
      <text x="160" y="53" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">CLASS: Student (Blueprint)</text>

      <text x="55" y="85" fill="#38bdf8" font-size="11" font-weight="bold">Attributes (State):</text>
      <text x="65" y="105" fill="#e2e8f0" font-size="10">• name: string</text>
      <text x="65" y="122" fill="#e2e8f0" font-size="10">• rollNumber: int</text>
      <text x="65" y="139" fill="#e2e8f0" font-size="10">• gpa: double</text>

      <line x1="45" y1="150" x2="275" y2="150" stroke="#334155" stroke-width="1.5"/>

      <text x="55" y="172" fill="#34d399" font-size="11" font-weight="bold">Methods (Behavior):</text>
      <text x="65" y="192" fill="#e2e8f0" font-size="10">• + study(hours)</text>
      <text x="65" y="209" fill="#e2e8f0" font-size="10">• + attendClass()</text>
      <text x="65" y="226" fill="#e2e8f0" font-size="10">• + getGPA(): double</text>

      <!-- Instantiation Arrow -->
      <path d="M 290 140 L 355 140" stroke="#60a5fa" stroke-width="2.5" stroke-dasharray="6" marker-end="url(#u1-blue-arr)"/>
      <text x="322" y="130" fill="#60a5fa" font-size="10" font-weight="bold" text-anchor="middle">Instantiate</text>

      <!-- Object Instances (Right) -->
      <!-- Object 1 -->
      <rect x="370" y="35" width="200" height="95" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
      <rect x="370" y="35" width="200" height="28" rx="6" fill="#065f46"/>
      <text x="470" y="54" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">s1: Student (Heap: 0x7A10)</text>
      <text x="385" y="80" fill="#a7f3d0" font-size="10">name = "Aarav"</text>
      <text x="385" y="96" fill="#a7f3d0" font-size="10">rollNumber = 101</text>
      <text x="385" y="112" fill="#a7f3d0" font-size="10">gpa = 8.60</text>

      <!-- Object 2 -->
      <rect x="370" y="150" width="200" height="95" rx="6" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
      <rect x="370" y="150" width="200" height="28" rx="6" fill="#065f46"/>
      <text x="470" y="169" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">s2: Student (Heap: 0x7B50)</text>
      <text x="385" y="195" fill="#a7f3d0" font-size="10">name = "Priya"</text>
      <text x="385" y="211" fill="#a7f3d0" font-size="10">rollNumber = 102</text>
      <text x="385" y="227" fill="#a7f3d0" font-size="10">gpa = 9.20</text>

      <!-- Message Passing Sender (Far Right) -->
      <rect x="650" y="90" width="160" height="85" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
      <text x="730" y="120" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">prof: Teacher</text>
      <text x="730" y="140" fill="#c084fc" font-size="10" text-anchor="middle">(Message Sender)</text>

      <!-- Message Arrow -->
      <path d="M 650 115 L 580 85" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#u1-amber-arr)"/>
      <text x="615" y="85" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">getGPA()</text>

      <!-- Response Arrow -->
      <path d="M 580 95 L 650 125" stroke="#34d399" stroke-width="2" stroke-dasharray="4" marker-end="url(#u1-green-arr)"/>
      <text x="615" y="128" fill="#34d399" font-size="8" text-anchor="middle">return 8.60</text>

      <defs>
        <marker id="u1-blue-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
        <marker id="u1-amber-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
        <marker id="u1-green-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Describe the elements of an object-oriented system. Explain objects, attributes, behavior, classes, methods, and message passing."</em> [5 Marks - Que 1.2]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define all 6 elements clearly. Cite both tangible entities (Student, Employee, Patient) and intangible entities (Bank Account). Explain that message passing is the only mechanism through which encapsulated object methods are triggered.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Object:</strong> Tangible or intangible entity in the problem domain (State + Behavior + Identity).</li>
    <li><strong>Attribute:</strong> Data values representing object state.</li>
    <li><strong>Class:</strong> Abstract template grouping objects with common attributes and behaviors.</li>
    <li><strong>Message Passing:</strong> Communication mechanism where one object requests another to execute a method.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u1-sec-2",
            "number": "02",
            "part": "Part 1 — Object-Oriented Concepts",
            "title": "Features of Object-Oriented Languages",
            "subtitle": "The 3 Major Pillars: Encapsulation, Polymorphism, Inheritance & Their Synergistic Interrelationship",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">OOP Pillars</div>
    <h3>The Triad of Object-Oriented Features</h3>
    <p>A programming language is classified as true object-oriented if it natively supports the three foundational pillars: <strong>Encapsulation, Polymorphism, and Inheritance</strong>. These three features work synergistically to provide data security, behavioral flexibility, and massive code reusability.</p>
    <p>As asked repeatedly in AKTU semester exams (2012-13, 2013-14), mastering these three features and their mutual relationships forms the bedrock of object-oriented system design.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Holy Trinity of Automobile Design</div>
  <p>Consider the modern automobile:</p>
  <ul>
    <li><strong>Encapsulation:</strong> You drive using the dashboard pedals and steering wheel; the hazardous combustion explosions and high-pressure fuel injectors are locked behind the steel engine hood (information hiding).</li>
    <li><strong>Inheritance:</strong> A <em>Tesla CyberTruck</em> and a <em>Honda Civic</em> both inherit base vehicular features (4 wheels, steering column, headlights, brakes) from the generic <code>Automobile</code> class, eliminating redundant redesign.</li>
    <li><strong>Polymorphism:</strong> Pressing the accelerator pedal sends the uniform command <em>"Accelerate"</em>. In the electric Tesla, software pulses battery current to AC induction motors; in the gasoline Civic, it opens an engine throttle cable. Same action, radically different internal mechanics!</li>
  </ul>
</div>

<div class="subtopics-container">
  <h4>Detailed Breakdown of the Three Pillars</h4>

  <div class="detail-block">
    <h5>2.1 Encapsulation (Data Shielding)</h5>
    <p>Encapsulation is the bundling of data attributes and the methods that operate upon them into an inviolable container (the class), while strictly restricting direct outside access to internal state.</p>
    <ul>
      <li>Data can only be accessed through validated public interface methods.</li>
      <li>Protects internal state against accidental corruption and malicious tampering.</li>
      <li>Prevents system-wide ripple effects when internal algorithms change.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2.2 Polymorphism (Many Forms)</h5>
    <p>Polymorphism allows a single interface, message, or operation name to take on different behaviors depending on the target object receiving the request at runtime.</p>
    <ul>
      <li>Enables objects with differing internal structures to share the exact same external API.</li>
      <li>Facilitates dynamic late binding and extensible plugin architectures.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2.3 Inheritance (Code Reusability)</h5>
    <p>Inheritance is the mechanism by which a derived class (subclass) automatically inherits all attributes and operations of an existing base class (superclass), while allowing the addition of specialized properties.</p>
    <ul>
      <li>Promotes high code reuse across projects.</li>
      <li>Establishes an <em>is-a</em> hierarchical relationship (e.g., <code>Manager is-an Employee</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2.4 Synergistic Relationship Between the Major Features</h5>
    <p>The three features do not operate in isolation; they reinforce each other:</p>
    <blockquote>
      <strong>Encapsulation protects data</strong> &rarr; <strong>Inheritance reuses existing structure</strong> &rarr; <strong>Polymorphism allows customized behavior</strong>!
    </blockquote>
    <p>Without encapsulation, inheritance would expose private superclass internals to external corruption. Without inheritance, polymorphism would lack a common base interface to dispatch across.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Synergy Matrix: The 3 Major OOP Features</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Primary Objective</th>
        <th>Mechanism</th>
        <th>Key Benefit</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Encapsulation</strong></td>
        <td><strong>Data Protection</strong> &amp; Information Hiding</td>
        <td>Access specifiers (<code>private</code>, <code>public</code>)</td>
        <td>Prevents unauthorized mutation; eliminates ripple effects</td>
      </tr>
      <tr>
        <td><strong>Inheritance</strong></td>
        <td><strong>Code Reusability</strong> &amp; Classification</td>
        <td>Class derivation (<code>subclass extends superclass</code>)</td>
        <td>Eliminates boilerplate code; models domain hierarchies</td>
      </tr>
      <tr>
        <td><strong>Polymorphism</strong></td>
        <td><strong>Behavioral Flexibility</strong> &amp; Extensibility</td>
        <td>Virtual methods &amp; dynamic late binding</td>
        <td>Allows new types to be plugged in without modifying callers</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Encapsulation, Inheritance &amp; Polymorphism)</span>
    <span class="code-desc">A unified example demonstrating all three pillars in a Shape hierarchy</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;memory&gt;</span>

<span class="c-comment">/* --- Pillar 1 &amp; 2: Base Class with Encapsulated Data &amp; Polymorphic Interface --- */</span>
<span class="c-keyword">class</span> <span class="c-type">Shape</span> {
<span class="c-keyword">private:</span>
    <span class="c-comment">/* ENCAPSULATION: color attribute is private and shielded */</span>
    std::string color;

<span class="c-keyword">public:</span>
    Shape(std::string c) : color(c) {}
    <span class="c-keyword">virtual</span> ~Shape() = <span class="c-keyword">default</span>;

    <span class="c-comment">/* Controlled Accessor */</span>
    std::string getColor() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> color; }

    <span class="c-comment">/* POLYMORPHISM: Pure virtual operation to be overridden by subclasses */</span>
    <span class="c-keyword">virtual double</span> getArea() <span class="c-keyword">const</span> = 0;
    <span class="c-keyword">virtual void</span> draw() <span class="c-keyword">const</span> = 0;
};

<span class="c-comment">/* --- Pillar 3: INHERITANCE (Circle reuses Shape's color and interface) --- */</span>
<span class="c-keyword">class</span> <span class="c-type">Circle</span> : <span class="c-keyword">public</span> <span class="c-type">Shape</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">double</span> radius; <span class="c-comment">/* Encapsulated attribute */</span>

<span class="c-keyword">public:</span>
    Circle(std::string c, <span class="c-type">double</span> r) : Shape(c), radius(r) {}

    <span class="c-comment">/* POLYMORPHIC OVERRIDE: Specific area calculation for Circle */</span>
    <span class="c-type">double</span> getArea() <span class="c-keyword">const override</span> {
        <span class="c-keyword">return</span> 3.14159 * radius * radius;
    }

    <span class="c-type">void</span> draw() <span class="c-keyword">const override</span> {
        std::cout &lt;&lt; <span class="c-string">"Drawing "</span> &lt;&lt; getColor() &lt;&lt; <span class="c-string">" Circle with Area: "</span> &lt;&lt; getArea() &lt;&lt; std::endl;
    }
};

<span class="c-keyword">class</span> <span class="c-type">Rectangle</span> : <span class="c-keyword">public</span> <span class="c-type">Shape</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">double</span> width, height;

<span class="c-keyword">public:</span>
    Rectangle(std::string c, <span class="c-type">double</span> w, <span class="c-type">double</span> h) : Shape(c), width(w), height(h) {}

    <span class="c-type">double</span> getArea() <span class="c-keyword">const override</span> {
        <span class="c-keyword">return</span> width * height;
    }

    <span class="c-type">void</span> draw() <span class="c-keyword">const override</span> {
        std::cout &lt;&lt; <span class="c-string">"Drawing "</span> &lt;&lt; getColor() &lt;&lt; <span class="c-string">" Rectangle with Area: "</span> &lt;&lt; getArea() &lt;&lt; std::endl;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">/* Polymorphic collection: Base pointers dispatching dynamically */</span>
    std::vector&lt;std::unique_ptr&lt;<span class="c-type">Shape</span>&gt;&gt; canvas;
    canvas.push_back(std::make_unique&lt;<span class="c-type">Circle</span>&gt;(<span class="c-string">"Crimson"</span>, 5.0));
    canvas.push_back(std::make_unique&lt;<span class="c-type">Rectangle</span>&gt;(<span class="c-string">"Azure"</span>, 4.0, 6.0));

    <span class="c-keyword">for</span> (<span class="c-keyword">const auto</span>&amp; shape : canvas) {
        shape-&gt;draw(); <span class="c-comment">/* Dynamic dispatch */</span>
    }
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The Three Pillars of Object-Oriented Programming</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Pillar 1: Encapsulation -->
      <g transform="translate(50, 30)">
        <rect width="220" height="210" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="220" height="35" rx="8" fill="#0284c7"/>
        <text x="110" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">1. ENCAPSULATION</text>
        
        <!-- Shield Icon Graphic -->
        <circle cx="110" cy="95" r="35" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="110" y="92" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">DATA</text>
        <text x="110" y="106" fill="#94a3b8" font-size="9" text-anchor="middle">Private Shell</text>

        <rect x="25" y="145" width="170" height="30" rx="4" fill="#0369a1"/>
        <text x="110" y="164" fill="#ffffff" font-size="10" text-anchor="middle">Public Methods Gateway</text>

        <text x="110" y="200" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Protects Data State</text>
      </g>

      <!-- Pillar 2: Inheritance -->
      <g transform="translate(310, 30)">
        <rect width="220" height="210" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="220" height="35" rx="8" fill="#b45309"/>
        <text x="110" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. INHERITANCE</text>
        
        <rect x="50" y="55" width="120" height="30" rx="4" fill="#78350f" stroke="#fbbf24"/>
        <text x="110" y="74" fill="#ffffff" font-size="10" text-anchor="middle">Superclass (Base)</text>

        <path d="M 110 85 L 110 115" stroke="#fbbf24" stroke-width="2" marker-end="url(#u1-inh-arrow)"/>

        <rect x="50" y="125" width="120" height="30" rx="4" fill="#78350f" stroke="#fbbf24"/>
        <text x="110" y="144" fill="#ffffff" font-size="10" text-anchor="middle">Subclass (Derived)</text>

        <text x="110" y="180" fill="#fef3c7" font-size="9" text-anchor="middle">"is-a" Relationship</text>
        <text x="110" y="200" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Reuses Code &amp; Structure</text>
      </g>

      <!-- Pillar 3: Polymorphism -->
      <g transform="translate(570, 30)">
        <rect width="220" height="210" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="220" height="35" rx="8" fill="#6d28d9"/>
        <text x="110" y="23" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. POLYMORPHISM</text>
        
        <rect x="35" y="55" width="150" height="30" rx="4" fill="#4c1d95" stroke="#c084fc"/>
        <text x="110" y="74" fill="#ffffff" font-size="10" text-anchor="middle">Message: draw()</text>

        <path d="M 80 85 L 45 125" stroke="#c084fc" stroke-width="1.8"/>
        <path d="M 140 85 L 175 125" stroke="#c084fc" stroke-width="1.8"/>

        <rect x="15" y="125" width="80" height="30" rx="4" fill="#1e1b4b"/>
        <text x="55" y="144" fill="#e9d5ff" font-size="9" text-anchor="middle">Circle.draw</text>

        <rect x="125" y="125" width="80" height="30" rx="4" fill="#1e1b4b"/>
        <text x="165" y="144" fill="#e9d5ff" font-size="9" text-anchor="middle">Rect.draw</text>

        <text x="110" y="180" fill="#e9d5ff" font-size="9" text-anchor="middle">Many Forms / Late Binding</text>
        <text x="110" y="200" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Enables Flexible Behavior</text>
      </g>

      <defs>
        <marker id="u1-inh-arrow" viewBox="0 0 10 10" refX="5" refY="6" markerWidth="6" markerHeight="6" orient="auto">
          <polygon points="0 0, 10 0, 5 10" fill="#fbbf24"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2012-13, 2013-14):</strong> <em>"Describe the features of object-oriented languages. Explain the relationship between the major OOP features."</em> [5 Marks - Que 1.3]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Always define the triad: <strong>Encapsulation</strong> (protects data), <strong>Inheritance</strong> (reuses code), and <strong>Polymorphism</strong> (allows many forms). Draw the 3 pillars diagram and summarize their mutual synergy using the formula: <em>Encapsulation protects data + Inheritance reuses structure + Polymorphism provides flexible behavior</em>.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Encapsulation:</strong> Bundles data with methods in an inviolable shell; hides internal representation.</li>
    <li><strong>Inheritance:</strong> Allows subclasses to reuse and extend superclass properties (code reusability).</li>
    <li><strong>Polymorphism:</strong> Same message/operation exhibits different behaviors across different classes.</li>
    <li>The 3 features combine to make software modular, secure, reusable, and extensible.</li>
  </ul>
</div>
"""
        },
        {
            "id": "u1-sec-3",
            "number": "03",
            "part": "Part 1 — Object-Oriented Concepts",
            "title": "Object-Oriented Design Process",
            "subtitle": "The 4-Stage Development Sequence: System Analysis → System Design → Object Design → Implementation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Engineering Lifecycle</div>
    <h3>The Four Stages of the OO Design Process</h3>
    <p>Software development in the object-oriented paradigm progresses through a disciplined, phased sequence that bridges the gap between informal customer requirements and executable machine code.</p>
    <p>As documented in standard OMT literature and AKTU Quantum (Que 1.4, 2010-11 PYQ), this process follows a strict four-stage sequence: <strong>System Analysis &rarr; System Design &rarr; Object Design &rarr; Implementation</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Constructing an International Airport</div>
  <p>You cannot build a multi-billion dollar airport by simply sending bulldozers to dump asphalt. The process unfolds in 4 distinct engineering phases:</p>
  <ol>
    <li><strong>System Analysis:</strong> Surveying airline passenger traffic, runway capacities, and safety requirements (<em>"What must the airport handle?"</em>).</li>
    <li><strong>System Design:</strong> High-level architectural zoning (Terminal 1, Terminal 2, Air Traffic Control tower, fuel depot placement).</li>
    <li><strong>Object Design:</strong> Detailed engineering blueprints for individual components (baggage carousel motor horsepower, gate boarding bridge hydraulics, HVAC pipe dimensions).</li>
    <li><strong>Implementation:</strong> Pouring concrete, wiring electrical circuits, and installing baggage scanner firmware.</li>
  </ol>
</div>

<div class="subtopics-container">
  <h4>Comprehensive Analysis of the 4 Stages</h4>

  <div class="detail-block">
    <h5>Stage 1: System Analysis (Problem Domain)</h5>
    <p>The analyst works with end users to formulate a rigorous problem statement and construct an abstract conceptual model of the real-world situation:</p>
    <ul>
      <li>Captures <strong>WHAT</strong> the system must do without concerning itself with technical implementation.</li>
      <li>Identifies domain entities (objects), their real-world attributes, and essential business relationships.</li>
      <li>Produces the conceptual <em>Object Model</em>, <em>Dynamic Model</em>, and <em>Functional Model</em>.</li>
      <li>Must be fully understandable by application domain experts who are non-programmers.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Stage 2: System Design (System Architecture)</h5>
    <p>The system designer establishes high-level architectural policies and organizes the target system into major collaborating subsystems:</p>
    <ul>
      <li>Partitions the overall system into loosely coupled <strong>subsystems</strong> based on domain cohesion.</li>
      <li>Determines allocation of subsystems to hardware nodes, CPUs, and processes (Client-Server, Multi-tier).</li>
      <li>Chooses data persistence strategies (Relational DB, NoSQL, in-memory cache) and inter-process communication protocols (REST, WebSockets, Message Queues).</li>
      <li>Identifies global performance characteristics to optimize (throughput, memory budget, low latency).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Stage 3: Object Design (Solution Domain Details)</h5>
    <p>The object designer takes the conceptual analysis classes and enriches them with technical, computer-domain implementation details:</p>
    <ul>
      <li>Maps conceptual attributes into concrete data structures (arrays, hash maps, binary trees).</li>
      <li>Designs and optimizes algorithms to realize required operations efficiently.</li>
      <li>Resolves inheritance hierarchies, adds private helper methods, and decides between buried pointers vs association tables.</li>
      <li>Designs public API interfaces, parameter signatures, and exception handling specifications.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>Stage 4: Implementation (Coding &amp; Traceability)</h5>
    <p>The classes and associations developed during object design are translated into actual programming language code (C++, Java, Python):</p>
    <ul>
      <li>Adheres to disciplined software engineering practices to ensure <strong>traceability</strong> back to design models.</li>
      <li>Implements database schemas, GUI controllers, and operating system calls.</li>
      <li>Ensures the resulting software system is robust, flexible, and extensible.</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>The 4-Stage OOD Waterfall Matrix</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Stage</th>
        <th>Primary Goal</th>
        <th>Input Artifact</th>
        <th>Output Deliverable</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. System Analysis</strong></td>
        <td>Understand problem; discover domain objects</td>
        <td>Informal user requirements</td>
        <td>Conceptual Analysis Model (OMT)</td>
      </tr>
      <tr>
        <td><strong>2. System Design</strong></td>
        <td>Define overall system architecture</td>
        <td>Conceptual Analysis Model</td>
        <td>Subsystem Decomposition &amp; Topology</td>
      </tr>
      <tr>
        <td><strong>3. Object Design</strong></td>
        <td>Add technical data structures &amp; algorithms</td>
        <td>Architecture &amp; Analysis Model</td>
        <td>Detailed Class Specs &amp; VTables</td>
      </tr>
      <tr>
        <td><strong>4. Implementation</strong></td>
        <td>Translate design into robust source code</td>
        <td>Detailed Object Design Specs</td>
        <td>Tested Source Code &amp; Binaries</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Traceability from Analysis to Implementation)</span>
    <span class="code-desc">Showing how an analysis requirement translates into an engineered implementation</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">/* STAGE 1 (Analysis): Requirement - Bank Account allows deposits and transfers */</span>
<span class="c-comment">/* STAGE 2 (System Design): Subsystem - Core Banking Service with thread synchronization */</span>
<span class="c-comment">/* STAGE 3 (Object Design): Concrete types (int64_t cents), mutex locks, validation */</span>
<span class="c-comment">/* STAGE 4 (Implementation): Final C++ Code with complete traceability */</span>

<span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;mutex&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdexcept&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">BankAccount</span> {
<span class="c-keyword">private:</span>
    std::string accountNumber;
    <span class="c-type">long long</span> balanceInCents; <span class="c-comment">/* Object Design: integer cents prevents floating point drift */</span>
    <span class="c-keyword">mutable</span> std::mutex mtx;   <span class="c-comment">/* System Design: Thread-safety concurrency lock */</span>

<span class="c-keyword">public:</span>
    BankAccount(std::string accNo, <span class="c-type">double</span> initialBal) 
        : accountNumber(accNo), balanceInCents(<span class="c-keyword">static_cast</span>&lt;<span class="c-type">long long</span>&gt;(initialBal * 100)) {
        <span class="c-keyword">if</span> (initialBal &lt; 0.0) {
            <span class="c-keyword">throw</span> std::invalid_argument(<span class="c-string">"Initial balance cannot be negative!"</span>);
        }
    }

    <span class="c-comment">/* Thread-safe withdrawal method */</span>
    <span class="c-type">bool</span> withdraw(<span class="c-type">double</span> dollars) {
        std::lock_guard&lt;std::mutex&gt; lock(mtx); <span class="c-comment">/* Concurrency safety */</span>
        <span class="c-type">long long</span> cents = <span class="c-keyword">static_cast</span>&lt;<span class="c-type">long long</span>&gt;(dollars * 100);
        
        <span class="c-keyword">if</span> (cents &lt;= 0 || cents &gt; balanceInCents) {
            <span class="c-keyword">return false</span>;
        }
        balanceInCents -= cents;
        <span class="c-keyword">return true</span>;
    }

    <span class="c-type">double</span> getBalance() <span class="c-keyword">const</span> {
        std::lock_guard&lt;std::mutex&gt; lock(mtx);
        <span class="c-keyword">return</span> balanceInCents / 100.0;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">BankAccount</span> acc(<span class="c-string">"ACC-9821"</span>, 1500.0);
    acc.withdraw(350.0);
    std::cout &lt;&lt; <span class="c-string">"Remaining Balance: $"</span> &lt;&lt; acc.getBalance() &lt;&lt; std::endl;
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The 4-Stage Object-Oriented Design Lifecycle</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 260" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Stage 1 -->
      <g transform="translate(30, 40)">
        <rect width="165" height="180" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="165" height="32" rx="8" fill="#0284c7"/>
        <text x="82" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">1. SYSTEM ANALYSIS</text>
        <text x="15" y="55" fill="#38bdf8" font-size="10" font-weight="bold">WHAT system does</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Problem statement</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Domain objects</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• Conceptual model</text>
        <text x="15" y="148" fill="#94a3b8" font-size="8">No technical details</text>
      </g>

      <!-- Arrow 1 to 2 -->
      <path d="M 195 130 L 230 130" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#u1-flow-arr)"/>

      <!-- Stage 2 -->
      <g transform="translate(235, 40)">
        <rect width="165" height="180" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="165" height="32" rx="8" fill="#b45309"/>
        <text x="82" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">2. SYSTEM DESIGN</text>
        <text x="15" y="55" fill="#fbbf24" font-size="10" font-weight="bold">Architecture Strategy</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Subsystems</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Process topology</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• DB &amp; IPC strategy</text>
        <text x="15" y="148" fill="#94a3b8" font-size="8">Resource allocations</text>
      </g>

      <!-- Arrow 2 to 3 -->
      <path d="M 400 130 L 435 130" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#u1-flow-arr)"/>

      <!-- Stage 3 -->
      <g transform="translate(440, 40)">
        <rect width="165" height="180" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="165" height="32" rx="8" fill="#6d28d9"/>
        <text x="82" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">3. OBJECT DESIGN</text>
        <text x="15" y="55" fill="#c084fc" font-size="10" font-weight="bold">HOW objects work</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Data structures</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Concrete algorithms</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• Public API specs</text>
        <text x="15" y="148" fill="#94a3b8" font-size="8">VTables &amp; associations</text>
      </g>

      <!-- Arrow 3 to 4 -->
      <path d="M 605 130 L 640 130" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#u1-flow-arr)"/>

      <!-- Stage 4 -->
      <g transform="translate(645, 40)">
        <rect width="165" height="180" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
        <rect width="165" height="32" rx="8" fill="#065f46"/>
        <text x="82" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">4. IMPLEMENTATION</text>
        <text x="15" y="55" fill="#34d399" font-size="10" font-weight="bold">Executable Software</text>
        <text x="15" y="78" fill="#e2e8f0" font-size="9">• Language code (C++)</text>
        <text x="15" y="98" fill="#e2e8f0" font-size="9">• Database schemas</text>
        <text x="15" y="118" fill="#e2e8f0" font-size="9">• Traceability checks</text>
        <text x="15" y="148" fill="#94a3b8" font-size="8">Robust binary system</text>
      </g>

      <defs>
        <marker id="u1-flow-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11):</strong> <em>"Describe steps of object-oriented design. Explain System Analysis, System Design, Object Design, and Final Implementation."</em> [5 Marks - Que 1.4]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Memorize the four-stage sequence: <strong>System Analysis &rarr; System Design &rarr; Object Design &rarr; Final Implementation</strong>. Highlight that System Analysis focuses on the problem domain (WHAT), System Design structures architecture into subsystems, Object Design details data structures/algorithms, and Implementation codes the classes while preserving traceability.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>System Analysis:</strong> Captures domain requirements and builds conceptual models (WHAT).</li>
    <li><strong>System Design:</strong> Partitions system into subsystems and allocates hardware/concurrency.</li>
    <li><strong>Object Design:</strong> Augments domain classes with computer algorithms and data structures (HOW).</li>
    <li><strong>Implementation:</strong> Translates design into robust code with full architectural traceability.</li>
  </ul>
</div>
"""
        }
    ]
