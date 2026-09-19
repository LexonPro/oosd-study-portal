# -*- coding: utf-8 -*-
"""
generate_unit5_part2.py: Generates Sections 6 to 11 for Unit 5
Topics:
  6. Constructors (Characteristics, Auto-Invocation, Constructor vs Normal Function)
  7. Types of Constructors (Default, Parameterized, Copy Constructor, Shallow vs Deep Copy)
  8. Destructors (Syntax, Execution Order, Scope Teardown, RAII Principles)
  9. Operator Overloading (Member vs Friend Function, Unary ++ vs Binary + Complex Arithmetic)
  10. Rules of Operator Overloading (Non-Overloadable Operators, Arity Rules, Assignment Restrictions)
  11. Type Conversion (Basic to Class, Class to Basic, Class to Class & Modern Casts)
"""

def get_unit5_part2_sections():
    sections = []

    # =========================================================================
    # SECTION 6: Constructors
    # =========================================================================
    sec6_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 2</div>
    <h3 class="card-title">6. Constructors: Automatic Object Initialization</h3>
  </div>

  <div class="detail-block">
    <h5>6.1 Meaning of a Constructor</h5>
    <p>
      A <strong>Constructor</strong> is a specialized member function of a class whose primary responsibility is to initialize the state of an object automatically at the moment of its physical creation. It ensures that no object ever enters program execution in an uninitialized, garbage-filled state.
    </p>
  </div>

  <div class="detail-block">
    <h5>6.2 Essential Architectural Characteristics of Constructors</h5>
    <ul>
      <li><strong>Name Invariance:</strong> Must bear the exact same identifier as the enclosing class (e.g. class <code>Matrix</code> has constructor <code>Matrix()</code>).</li>
      <li><strong>Absence of Return Type:</strong> Has <strong>no return type</strong> whatsoever &mdash; not even <code>void</code>. Attempting to write <code>void Matrix()</code> turns it into a regular member function, not a constructor.</li>
      <li><strong>Automatic Invocation:</strong> Automatically triggered by the C++ runtime system whenever an object instance is created on the stack (<code>Matrix m;</code>) or heap (<code>new Matrix()</code>). It cannot be called explicitly like a normal function (e.g. <code>m.Matrix(); // ILLEGAL</code>).</li>
      <li><strong>Public Visibility:</strong> Normally declared in the <code>public:</code> section so that external scopes can instantiate objects (private constructors are reserved for specialized design patterns like Singleton).</li>
      <li><strong>Cannot be Virtual:</strong> In standard C++, constructors cannot be virtual because an object's concrete type must be known at compile time to allocate memory, and the virtual table pointer (<code>vptr</code>) is initialized inside the constructor body.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Factory Reset Sequence of a New Smartphone</span>
  </div>
  <p>
    When you purchase a brand-new smartphone and power it on for the very first time, you do not find random corrupted fragments from previous owners in its storage. The device automatically runs its <strong>out-of-box initialization sequence</strong> (the Constructor): it sets the system language to default English, formats the solid-state storage, zeroes the battery health monitor, and initializes the operating system variables to a clean, reliable baseline before you ever touch a single app!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Constructor Declaration, Automatic Invocation & Garbage-Prevention Comparison</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">FlightRecord</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> flightCode;
    <span class="c-type">int</span> altitudeFeet;
    <span class="c-type">double</span> fuelRemainingKg;

<span class="c-keyword">public</span>:
    <span class="c-comment">// CONSTRUCTOR: Same name as class, NO return type</span>
    <span class="c-type">FlightRecord</span>() {
        flightCode = <span class="c-string">"AI-101"</span>;
        altitudeFeet = <span class="c-number">0</span>;           <span class="c-comment">// Ground baseline</span>
        fuelRemainingKg = <span class="c-number">15000.0</span>;  <span class="c-comment">// Full tank</span>
        std::cout &lt;&lt; <span class="c-string">"[Constructor Activated] Flight "</span> &lt;&lt; flightCode 
                  &lt;&lt; <span class="c-string">" telemetry initialized successfully!\\n"</span>;
    }

    <span class="c-type">void</span> printStatus() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Flight "</span> &lt;&lt; flightCode 
                  &lt;&lt; <span class="c-string">" | Altitude: "</span> &lt;&lt; altitudeFeet &lt;&lt; <span class="c-string">" ft"</span>
                  &lt;&lt; <span class="c-string">" | Fuel: "</span> &lt;&lt; fuelRemainingKg &lt;&lt; <span class="c-string">" kg\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Testing Automatic Constructor Invocation ===\\n"</span>;

    <span class="c-comment">// Automatic invocation occurs on object creation line</span>
    <span class="c-type">FlightRecord</span> f1; 

    f1.printStatus();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Object Memory Lifecycle &amp; Constructor Initialization Pipeline</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Step 1: Raw Allocation -->
      <g transform="translate(30, 25)">
        <rect width="200" height="160" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="100" y="28" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Step 1: Raw RAM Allocation</text>
        <rect x="15" y="45" width="170" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="100" y="65" fill="#ef4444" font-family="monospace" font-size="10" text-anchor="middle">altitude = 0x7F2A9C (Garbage!)</text>
        <rect x="15" y="85" width="170" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="100" y="105" fill="#ef4444" font-family="monospace" font-size="10" text-anchor="middle">fuel = -NaN (Undefined!)</text>
        <text x="100" y="145" fill="var(--text-muted)" font-size="9" text-anchor="middle">Uninitialized stack bytes</text>
      </g>

      <!-- Arrow 1 to 2 -->
      <path d="M 240 105 L 290 105" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="265" y="95" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Auto-Call</text>

      <!-- Step 2: Constructor Routine -->
      <g transform="translate(290, 25)">
        <rect width="180" height="160" rx="8" fill="rgba(99, 102, 241, 0.12)" stroke="#6366f1" stroke-width="2"/>
        <text x="90" y="28" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Step 2: Constructor</text>
        <rect x="15" y="45" width="150" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="90" y="67" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">FlightRecord() {</text>
        <text x="90" y="100" fill="var(--text-primary)" font-size="10" text-anchor="middle">Writes valid initial state</text>
        <text x="90" y="115" fill="var(--text-primary)" font-size="10" text-anchor="middle">Initializes vptr (if any)</text>
        <text x="90" y="145" fill="#a5b4fc" font-size="9" text-anchor="middle">Guaranteed zero-garbage</text>
      </g>

      <!-- Arrow 2 to 3 -->
      <path d="M 480 105 L 530 105" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="505" y="95" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Ready</text>

      <!-- Step 3: Valid Object -->
      <g transform="translate(530, 25)">
        <rect width="200" height="160" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="100" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Step 3: Initialized Object</text>
        <rect x="15" y="45" width="170" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="100" y="65" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">altitude = 0 ft</text>
        <rect x="15" y="85" width="170" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="100" y="105" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">fuel = 15000.0 kg</text>
        <text x="100" y="145" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">&#x2713; Safe for Program Execution</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Comparative Analysis: Constructor vs. Normal Member Function</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Architectural Criterion</th>
        <th>Constructor</th>
        <th>Normal Member Function</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Function Identifier</strong></td>
        <td><strong>Must match class name</strong> identically.</td>
        <td>Any valid user-defined identifier.</td>
      </tr>
      <tr>
        <td><strong>Return Type</strong></td>
        <td><strong>No return type</strong> (not even <code>void</code>).</td>
        <td>Must explicitly specify return type (or <code>void</code>).</td>
      </tr>
      <tr>
        <td><strong>Invocation Mechanism</strong></td>
        <td><strong>Automatically called</strong> upon object creation.</td>
        <td>Must be explicitly called via <code>obj.func()</code>.</td>
      </tr>
      <tr>
        <td><strong>Primary Responsibility</strong></td>
        <td>Initializes object state and allocates resources.</td>
        <td>Executes general algorithmic operations on state.</td>
      </tr>
      <tr>
        <td><strong>Inheritance &amp; Virtual</strong></td>
        <td><strong>Cannot be inherited</strong>; cannot be virtual.</td>
        <td>Inherited by derived classes; can be virtual.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> What happens if a programmer writes <code>void ClassName()</code>? (The compiler treats it as a normal member function, not a constructor!).</li>
    <li><span class="check-box"></span> Can a constructor return a value using <code>return 10;</code>? (No, returning a value from a constructor is a compile error).</li>
    <li><span class="check-box"></span> Why can constructors never be virtual in C++? (VTable/VPtr does not exist until construction completes).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"What is a constructor? Differentiate it from a normal function"</em>, draw the comparison table above. Highlight that a constructor has NO return type and is invoked implicitly by the runtime system.
</div>
"""
    sections.append({
        "id": "u5-sec-6",
        "number": 6,
        "part": "PART 2 — CONSTRUCTORS, DESTRUCTORS & TYPE CONVERSION",
        "title": "6. Constructors",
        "subtitle": "Automatic State Initialization, Characteristics, Execution Order & The Normal Function Divide",
        "content": sec6_content
    })

    # =========================================================================
    # SECTION 7: Types of Constructors
    # =========================================================================
    sec7_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 2</div>
    <h3 class="card-title">7. Types of Constructors: Default, Parameterized &amp; Copy</h3>
  </div>

  <div class="detail-block">
    <h5>7.1 The Three Core Types of Constructors</h5>
    <p>
      In C++, constructors can be overloaded to provide multiple flexible mechanisms for initializing objects. The AKTU curriculum rigorously tests three canonical forms:
    </p>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6>Default Constructor</h6>
          <p>
            A constructor that accepts <strong>no parameters</strong> (or where all parameters have default values). If no constructor is written by the programmer, the C++ compiler automatically synthesizes a trivial default constructor. However, if <em>any</em> parameterized constructor is defined, the compiler-generated default constructor is suppressed!
          </p>
          <div class="code-box"><code>Complex() : real(0.0), imag(0.0) {}</code></div>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6>Parameterized Constructor</h6>
          <p>
            A constructor that accepts one or more arguments to initialize an object with specific customized data values at creation time. Best implemented using modern <strong>Member Initializer Lists</strong> for optimal performance.
          </p>
          <div class="code-box"><code>Complex(double r, double i) : real(r), imag(i) {}</code></div>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">3</span>
        <div class="step-content">
          <h6>Copy Constructor</h6>
          <p>
            A constructor that initializes a new object by copying data members from an existing object of the same class:
          </p>
          <div class="code-box"><code>ClassName(const ClassName&amp; other); // Mandatory const reference parameter!</code></div>
          <p>
            <strong>Why Passed by Reference?</strong> If passed by value (<code>ClassName(ClassName other)</code>), passing the argument would itself require calling the copy constructor, triggering an <em>infinite recursive loop</em> and stack overflow!
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="detail-block">
    <h5>7.2 Shallow Copy vs. Deep Copy Hazard</h5>
    <p>
      The default compiler-generated copy constructor performs a <strong>Shallow Copy (member-wise bitwise copy)</strong>. If a class owns raw heap pointers (<code>int* ptr = new int[10];</code>), shallow copying duplicates only the pointer address, causing two objects to point to the exact same heap memory. When both objects destruct, the second destructor triggers a fatal <strong>Double-Free Crash</strong>! A user-defined <strong>Deep Copy Constructor</strong> must allocate distinct heap memory and copy the actual underlying data.
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Three Ways to Buy a Laptop</span>
  </div>
  <p>
    1. <strong>Default Constructor:</strong> You walk into an electronics store and say: <em>"Give me the standard laptop off the shelf."</em> It comes with base factory defaults (8GB RAM, 256GB SSD, Silver color).<br>
    2. <strong>Parameterized Constructor:</strong> You customize your order online: <em>"Give me a laptop with 32GB RAM, 2TB SSD, in Space Grey."</em> You pass explicit custom arguments at checkout.<br>
    3. <strong>Copy Constructor:</strong> You love your colleague's perfectly configured development laptop. You hand a blank laptop to IT and say: <em>"Clone all installed tools, configs, and environments from my colleague's machine into my new machine."</em> A fresh, independent duplicate is born!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Exhaustive Demonstration: Default, Parameterized & Deep Copy Constructors</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;cstring&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">CustomString</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">char</span>* buffer;
    <span class="c-type">int</span> length;

<span class="c-keyword">public</span>:
    <span class="c-comment">// 1. DEFAULT CONSTRUCTOR</span>
    <span class="c-type">CustomString</span>() {
        length = <span class="c-number">0</span>;
        buffer = <span class="c-keyword">new</span> <span class="c-type">char</span>[<span class="c-number">1</span>];
        buffer[<span class="c-number">0</span>] = <span class="c-string">'\\0'</span>;
        std::cout &lt;&lt; <span class="c-string">"[Default Constructor] Empty string initialized.\\n"</span>;
    }

    <span class="c-comment">// 2. PARAMETERIZED CONSTRUCTOR</span>
    <span class="c-type">CustomString</span>(<span class="c-keyword">const</span> <span class="c-type">char</span>* text) {
        length = std::strlen(text);
        buffer = <span class="c-keyword">new</span> <span class="c-type">char</span>[length + <span class="c-number">1</span>];
        std::strcpy(buffer, text);
        std::cout &lt;&lt; <span class="c-string">"[Parameterized Constructor] Created: '"</span> &lt;&lt; buffer &lt;&lt; <span class="c-string">"'\\n"</span>;
    }

    <span class="c-comment">// 3. DEEP COPY CONSTRUCTOR (Must pass by reference: const CustomString&amp;)</span>
    <span class="c-type">CustomString</span>(<span class="c-keyword">const</span> <span class="c-type">CustomString</span>&amp; other) {
        length = other.length;
        <span class="c-comment">// Allocate completely SEPARATE heap memory buffer (Deep Copy)</span>
        buffer = <span class="c-keyword">new</span> <span class="c-type">char</span>[length + <span class="c-number">1</span>];
        std::strcpy(buffer, other.buffer);
        std::cout &lt;&lt; <span class="c-string">"[Deep Copy Constructor] Safely cloned: '"</span> &lt;&lt; buffer &lt;&lt; <span class="c-string">"'\\n"</span>;
    }

    <span class="c-comment">// Destructor cleans up allocated heap buffer</span>
    ~<span class="c-type">CustomString</span>() {
        <span class="c-keyword">delete</span>[] buffer;
    }

    <span class="c-type">void</span> display() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Content: \\""</span> &lt;&lt; buffer &lt;&lt; <span class="c-string">"\\" | Address: "</span> 
                  &lt;&lt; <span class="c-keyword">static_cast</span>&lt;<span class="c-keyword">void</span>*&gt;(buffer) &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Constructor Types Demonstration ===\\n"</span>;

    <span class="c-type">CustomString</span> s1;                      <span class="c-comment">// Invokes Default Constructor</span>
    <span class="c-type">CustomString</span> s2(<span class="c-string">"C++ Systems Design"</span>); <span class="c-comment">// Invokes Parameterized Constructor</span>
    <span class="c-type">CustomString</span> s3(s2);                  <span class="c-comment">// Invokes Copy Constructor</span>

    std::cout &lt;&lt; <span class="c-string">"\\nMemory Verification (Notice distinct heap addresses!):\\n"</span>;
    s2.display();
    s3.display();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Shallow Copy (Pointer Aliasing Hazard) vs Deep Copy (Independent Buffer)</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- Shallow Copy Hazard Panel -->
      <g transform="translate(30, 20)">
        <rect width="330" height="180" rx="8" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="165" y="28" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Default Shallow Copy (CRASH HAZARD)</text>
        
        <rect x="20" y="45" width="130" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="85" y="65" fill="var(--text-primary)" font-size="10" text-anchor="middle">Object A: ptr</text>
        <text x="85" y="78" fill="#ef4444" font-family="monospace" font-size="9" text-anchor="middle">0x10A400</text>

        <rect x="180" y="45" width="130" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="245" y="65" fill="var(--text-primary)" font-size="10" text-anchor="middle">Object B: ptr</text>
        <text x="245" y="78" fill="#ef4444" font-family="monospace" font-size="9" text-anchor="middle">0x10A400</text>

        <!-- Both point to single heap block -->
        <rect x="75" y="115" width="180" height="40" rx="4" fill="var(--bg-elevated)" stroke="#ef4444"/>
        <text x="165" y="135" fill="#ef4444" font-family="monospace" font-size="11" text-anchor="middle">Single Heap [0x10A400]</text>
        <path d="M 85 85 L 130 115" stroke="#ef4444" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <path d="M 245 85 L 200 115" stroke="#ef4444" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <text x="165" y="170" fill="#ef4444" font-size="10" text-anchor="middle">&#x2717; Destructor double-free triggers crash!</text>
      </g>

      <!-- Deep Copy Panel -->
      <g transform="translate(400, 20)">
        <rect width="330" height="180" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5"/>
        <text x="165" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">User Deep Copy Constructor (SAFE)</text>
        
        <rect x="20" y="45" width="130" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="85" y="65" fill="var(--text-primary)" font-size="10" text-anchor="middle">Object A: ptr</text>
        <text x="85" y="78" fill="#10b981" font-family="monospace" font-size="9" text-anchor="middle">0x10A400</text>

        <rect x="180" y="45" width="130" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="245" y="65" fill="var(--text-primary)" font-size="10" text-anchor="middle">Object B: ptr</text>
        <text x="245" y="78" fill="#10b981" font-family="monospace" font-size="9" text-anchor="middle">0x10B800</text>

        <!-- Two separate heap blocks -->
        <rect x="20" y="115" width="130" height="40" rx="4" fill="var(--bg-elevated)" stroke="#10b981"/>
        <text x="85" y="138" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">Heap [0x10A400]</text>

        <rect x="180" y="115" width="130" height="40" rx="4" fill="var(--bg-elevated)" stroke="#10b981"/>
        <text x="245" y="138" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">Heap [0x10B800]</text>

        <path d="M 85 85 L 85 115" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <path d="M 245 85 L 245 115" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <text x="165" y="170" fill="#10b981" font-size="10" text-anchor="middle">&#x2713; Separate buffers; clean independent teardowns</text>
      </g>
    </svg>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> Why must a copy constructor take its argument by reference (<code>const ClassName&amp;</code>)? (Passing by value would trigger infinite recursion).</li>
    <li><span class="check-box"></span> What is the fatal bug of a shallow copy when raw dynamic pointers are present? (Pointer aliasing leads to double-free undefined behavior).</li>
    <li><span class="check-box"></span> When does the compiler stop generating an implicit default constructor? (As soon as any parameterized constructor is declared).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"Explain the different types of constructors with examples. Why is the copy constructor argument passed by reference?"</em> is a guaranteed 10-mark question. Provide code for all 3 constructors and state clearly that pass-by-value causes infinite constructor recursion.
</div>
"""
    sections.append({
        "id": "u5-sec-7",
        "number": 7,
        "part": "PART 2 — CONSTRUCTORS, DESTRUCTORS & TYPE CONVERSION",
        "title": "7. Types of Constructors",
        "subtitle": "Default, Parameterized, Copy Constructors, Deep vs Shallow Copy & The Infinite Recursion Trap",
        "content": sec7_content
    })

    # =========================================================================
    # SECTION 8: Destructors
    # =========================================================================
    sec8_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 2</div>
    <h3 class="card-title">8. Destructors: Deterministic Teardown &amp; RAII</h3>
  </div>

  <div class="detail-block">
    <h5>8.1 Meaning of a Destructor</h5>
    <p>
      A <strong>Destructor</strong> is a special member function that is automatically invoked when an object's lifetime ends. Its primary architectural duty is to release resources acquired by the object during its lifetime (e.g. freeing heap memory allocated via <code>new</code>, closing open file descriptors, closing database sockets, or unlocking mutexes).
    </p>
  </div>

  <div class="detail-block">
    <h5>8.2 Essential Rules &amp; Characteristics of Destructors</h5>
    <ul>
      <li><strong>Tilde (<code>~</code>) Prefix:</strong> Must share the exact class name preceded by a tilde symbol (e.g., <code>~FileStream()</code>).</li>
      <li><strong>No Arguments &amp; No Return Type:</strong> Destructors cannot accept any parameters and cannot return any value.</li>
      <li><strong>Zero Overloading:</strong> Because it accepts no arguments, a class can have <strong>only ONE destructor</strong>. Overloading a destructor is impossible.</li>
      <li><strong>Automatic Invocation Scenarios:</strong>
        <ol>
          <li>When a local stack-allocated object exits its enclosing scope (e.g. at the closing brace <code>}</code>).</li>
          <li>When dynamically allocated heap objects are explicitly deallocated using <code>delete</code> or <code>delete[]</code>.</li>
          <li>When global or static objects are destroyed upon program exit.</li>
        </ol>
      </li>
      <li><strong>Reverse Order of Construction:</strong> Local stack objects are destructed in strict <strong>LIFO (Last-In, First-Out)</strong> order &mdash; the object created last is destructed first.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Hotel Room Checkout Protocol</span>
  </div>
  <p>
    When you check into a hotel room (Constructor), you are handed the room keycard, towels are placed on the racks, and your minibar account is initialized.<br>
    When your stay ends and you checkout (Destructor), the hotel protocol triggers automatically: you return the keycard, room utilities are powered down, and your security deposit is reconciled.<br>
    If hotel guests walked away without a checkout protocol (a missing destructor), rooms would stay occupied, keys would leak, and the hotel would run out of resources! In C++, destructors guarantee that every object leaves no orphaned memory behind.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating Stack LIFO Destruction Order & Dynamic Heap Deallocation</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">ScopedTracker</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> trackerName;

<span class="c-keyword">public</span>:
    <span class="c-type">ScopedTracker</span>(<span class="c-type">std::string</span> name) : trackerName(name) {
        std::cout &lt;&lt; <span class="c-string">"++ [Constructor] Initializing: "</span> &lt;&lt; trackerName &lt;&lt; <span class="c-string">"\\n"</span>;
    }

    ~<span class="c-type">ScopedTracker</span>() {
        std::cout &lt;&lt; <span class="c-string">"-- [Destructor] Cleaning up:   "</span> &lt;&lt; trackerName &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Testing LIFO Destructor Execution Order ===\\n"</span>;

    <span class="c-type">ScopedTracker</span> objA(<span class="c-string">"Object-A (Outer Scope)"</span>);

    {
        std::cout &lt;&lt; <span class="c-string">"\\n-- Entering Inner Block --\\n"</span>;
        <span class="c-type">ScopedTracker</span> objB(<span class="c-string">"Object-B (Inner Scope 1)"</span>);
        <span class="c-type">ScopedTracker</span> objC(<span class="c-string">"Object-C (Inner Scope 2)"</span>);
        std::cout &lt;&lt; <span class="c-string">"-- Exiting Inner Block (Notice C destructs before B!) --\\n"</span>;
    }

    std::cout &lt;&lt; <span class="c-string">"\\n-- Heap Dynamic Object Allocation --\\n"</span>;
    <span class="c-type">ScopedTracker</span>* heapObj = <span class="c-keyword">new</span> <span class="c-type">ScopedTracker</span>(<span class="c-string">"HeapObject"</span>);
    
    std::cout &lt;&lt; <span class="c-string">"Explicitly invoking delete on heap object:\\n"</span>;
    <span class="c-keyword">delete</span> heapObj; <span class="c-comment">// Triggers destructor immediately</span>

    std::cout &lt;&lt; <span class="c-string">"\\n-- Reaching End of main() --\\n"</span>;
    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: LIFO Stack Frame Destruction Order</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Construction Timeline -->
      <g transform="translate(30, 20)">
        <rect width="330" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="165" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">1. Construction Order (FIFO Creation)</text>
        <rect x="25" y="45" width="280" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="65" fill="var(--text-primary)" font-size="10" text-anchor="middle">1st: ScopedTracker objA</text>
        <rect x="25" y="82" width="280" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="102" fill="var(--text-primary)" font-size="10" text-anchor="middle">2nd: ScopedTracker objB</text>
        <rect x="25" y="119" width="280" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="139" fill="var(--text-primary)" font-size="10" text-anchor="middle">3rd: ScopedTracker objC</text>
        <text x="165" y="165" fill="#38bdf8" font-size="9" text-anchor="middle">Pushed onto Call Stack in Order</text>
      </g>

      <!-- Reversal Flow Arrow -->
      <path d="M 370 105 L 430 105" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="400" y="95" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">LIFO</text>

      <!-- Destruction Timeline -->
      <g transform="translate(440, 20)">
        <rect width="290" height="170" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="1.5"/>
        <text x="145" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">2. Destruction Order (Strict LIFO Pop)</text>
        <rect x="20" y="45" width="250" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="145" y="65" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">1st to Die: ~ScopedTracker() [objC]</text>
        <rect x="20" y="82" width="250" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="145" y="102" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">2nd to Die: ~ScopedTracker() [objB]</text>
        <rect x="20" y="119" width="250" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="145" y="139" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Last to Die: ~ScopedTracker() [objA]</text>
        <text x="145" y="165" fill="var(--text-muted)" font-size="9" text-anchor="middle">Stack unwinds in reverse creation order</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Comparative Analysis: Constructor vs. Destructor</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Constructor</th>
        <th>Destructor</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Naming</strong></td>
        <td><code>ClassName()</code></td>
        <td><code>~ClassName()</code> (preceded by tilde)</td>
      </tr>
      <tr>
        <td><strong>Parameters &amp; Overloading</strong></td>
        <td>Can accept parameters; <strong>can be overloaded</strong>.</td>
        <td>No parameters; <strong>cannot be overloaded</strong>.</td>
      </tr>
      <tr>
        <td><strong>Trigger Timing</strong></td>
        <td>When an object is <strong>created</strong>.</td>
        <td>When an object is <strong>destroyed</strong> / goes out of scope.</td>
      </tr>
      <tr>
        <td><strong>Primary Role</strong></td>
        <td>Initializes state and acquires resources.</td>
        <td>Releases resources and cleans up memory.</td>
      </tr>
      <tr>
        <td><strong>Execution Order</strong></td>
        <td>Top-to-bottom in order of declaration.</td>
        <td><strong>Strict reverse order (LIFO)</strong>.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> Why can a destructor never have parameters or return values? (It is invoked automatically by the runtime with no call-site syntax).</li>
    <li><span class="check-box"></span> In what order are local stack objects destructed? (Strict reverse order of construction: LIFO).</li>
    <li><span class="check-box"></span> What happens if you forget to write <code>delete</code> on a heap object allocated with <code>new</code>? (Its destructor never runs, causing a permanent memory leak).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Questions asking to predict the output of nested scopes with constructors and destructors are common. Remember the rule: <strong>Objects created last are destructed first (LIFO)</strong>, and local scope objects die at the closing brace <code>}</code> before subsequent code executes.
</div>
"""
    sections.append({
        "id": "u5-sec-8",
        "number": 8,
        "part": "PART 2 — CONSTRUCTORS, DESTRUCTORS & TYPE CONVERSION",
        "title": "8. Destructors",
        "subtitle": "Deterministic Resource Teardown, LIFO Destruction Sequence & Constructor vs Destructor Matrix",
        "content": sec8_content
    })

    # =========================================================================
    # SECTION 9: Operator Overloading
    # =========================================================================
    sec9_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 2</div>
    <h3 class="card-title">9. Operator Overloading: Syntactic Elegance for Custom Types</h3>
  </div>

  <div class="detail-block">
    <h5>9.1 Meaning and Purpose of Operator Overloading</h5>
    <p>
      <strong>Operator Overloading</strong> is a form of compile-time polymorphism in C++ that allows standard built-in operators (such as <code>+</code>, <code>-</code>, <code>*</code>, <code>++</code>, <code>==</code>, <code>&lt;&lt;</code>) to be given customized definitions when applied to user-defined class objects.
    </p>
    <p>
      <strong>Why Overload Operators?</strong> Rather than forcing awkward, verbose function calls like <code>c3 = c1.addComplex(c2);</code>, operator overloading enables intuitive, mathematically natural expressions:
    </p>
    <div class="code-box"><code>Complex c3 = c1 + c2; // Natural, clean mathematical syntax</code></div>
  </div>

  <div class="detail-block">
    <h5>9.2 General Operator Syntax</h5>
    <div class="code-box">
      <code>returnType operator op(argumentList) { /* body */ }</code>
    </div>
    <p>where <code>operator</code> is a C++ keyword followed immediately by the operator symbol being overloaded (e.g. <code>operator+</code>, <code>operator++</code>).</p>
  </div>

  <div class="detail-block">
    <h5>9.3 Member Function vs. Friend Function Approach</h5>
    <ul>
      <li><strong>Member Function:</strong> The left-hand operand is implicitly passed as the invoking object (<code>*this</code>). A unary operator takes <strong>0 explicit arguments</strong>; a binary operator takes <strong>1 explicit argument</strong> (the right-hand operand).</li>
      <li><strong>Friend Function:</strong> Independent function without a <code>this</code> pointer. A unary operator takes <strong>1 explicit argument</strong>; a binary operator takes <strong>2 explicit arguments</strong> (left and right operands). Mandatory when the left operand is not a class object (e.g. <code>cout &lt;&lt; obj</code> requires a friend operator function).</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Universal "+" Sign</span>
  </div>
  <p>
    Consider the <code>+</code> symbol in human communication:<br>
    - If applied to two bank currency amounts: <code>Rs. 500 + Rs. 200 = Rs. 700</code> (numerical addition).<br>
    - If applied to two postal addresses: <code>"Flat 402" + "Gaur City" = "Flat 402, Gaur City"</code> (string concatenation).<br>
    - If applied to two vectors in physics: <code>Vector A + Vector B = Resultant Vector</code> (parallelogram law addition).<br>
    Humans naturally understand that the operational mechanics of <code>+</code> depend entirely on the <em>types of objects</em> being joined. Operator overloading gives C++ user-defined classes this exact semantic elegance!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Overloading Unary Increment (++) & Binary Addition (+) on Complex Numbers</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Complex</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">double</span> real;
    <span class="c-type">double</span> imag;

<span class="c-keyword">public</span>:
    <span class="c-type">Complex</span>(<span class="c-type">double</span> r = <span class="c-number">0.0</span>, <span class="c-type">double</span> i = <span class="c-number">0.0</span>) : real(r), imag(i) {}

    <span class="c-comment">// 1. UNARY OPERATOR OVERLOAD (++ prefix) as Member Function</span>
    <span class="c-comment">// Takes 0 explicit arguments because '*this' is the operand</span>
    <span class="c-type">Complex</span>&amp; <span class="c-keyword">operator</span>++() {
        ++real;
        ++imag;
        <span class="c-keyword">return</span> *<span class="c-keyword">this</span>; <span class="c-comment">// Return modified object reference</span>
    }

    <span class="c-comment">// 2. BINARY OPERATOR OVERLOAD (+) as Member Function</span>
    <span class="c-comment">// Takes 1 explicit argument: the Right-Hand Side (rhs) operand</span>
    <span class="c-type">Complex</span> <span class="c-keyword">operator</span>+(<span class="c-keyword">const</span> <span class="c-type">Complex</span>&amp; rhs) <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> <span class="c-type">Complex</span>(real + rhs.real, imag + rhs.imag);
    }

    <span class="c-comment">// 3. FRIEND STREAM EXTRACTION OPERATOR (&lt;&lt;)</span>
    <span class="c-comment">// Requires 2 arguments because left operand is std::ostream, NOT Complex!</span>
    <span class="c-keyword">friend</span> <span class="c-type">std::ostream</span>&amp; <span class="c-keyword">operator</span>&lt;&lt;(<span class="c-type">std::ostream</span>&amp; out, <span class="c-keyword">const</span> <span class="c-type">Complex</span>&amp; c) {
        out &lt;&lt; c.real &lt;&lt; <span class="c-string">" + "</span> &lt;&lt; c.imag &lt;&lt; <span class="c-string">"i"</span>;
        <span class="c-keyword">return</span> out;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">Complex</span> c1(<span class="c-number">3.5</span>, <span class="c-number">2.5</span>);
    <span class="c-type">Complex</span> c2(<span class="c-number">1.5</span>, <span class="c-number">4.5</span>);

    std::cout &lt;&lt; <span class="c-string">"=== Operator Overloading Demonstration ===\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"c1: "</span> &lt;&lt; c1 &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"c2: "</span> &lt;&lt; c2 &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Binary Addition: Resolves to c1.operator+(c2)</span>
    <span class="c-type">Complex</span> sum = c1 + c2;
    std::cout &lt;&lt; <span class="c-string">"c1 + c2 = "</span> &lt;&lt; sum &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Unary Increment: Resolves to c1.operator++()</span>
    ++c1;
    std::cout &lt;&lt; <span class="c-string">"After ++c1: "</span> &lt;&lt; c1 &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Member Function vs Friend Function Operator Dispatch</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Member Function Binary Operator -->
      <g transform="translate(30, 20)">
        <rect width="330" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="165" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Member Function: c1 + c2</text>
        <rect x="20" y="45" width="290" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="68" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">c1.operator+(c2)</text>
        <text x="165" y="105" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Left Operand (c1) = Implicit 'this' Pointer</text>
        <text x="165" y="125" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Right Operand (c2) = Explicit Formal Parameter</text>
        <text x="165" y="155" fill="#38bdf8" font-size="9" text-anchor="middle">Binary operator requires exactly 1 explicit argument</text>
      </g>

      <!-- Friend Function Operator -->
      <g transform="translate(400, 20)">
        <rect width="330" height="170" rx="8" fill="var(--bg-elevated)" stroke="#6366f1" stroke-width="1.5"/>
        <text x="165" y="28" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Friend Function: cout &lt;&lt; c1</text>
        <rect x="20" y="45" width="290" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="68" fill="#a5b4fc" font-family="monospace" font-size="11" text-anchor="middle">operator&lt;&lt;(std::cout, c1)</text>
        <text x="165" y="105" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Left Operand (cout) = Explicit Argument 1</text>
        <text x="165" y="125" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Right Operand (c1) = Explicit Argument 2</text>
        <text x="165" y="155" fill="#10b981" font-size="9" text-anchor="middle">Mandatory when left operand is not a class instance</text>
      </g>
    </svg>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> How many arguments does a binary operator take when overloaded as a member function? (Exactly 1; left operand is <code>this</code>).</li>
    <li><span class="check-box"></span> Why must <code>&lt;&lt;</code> and <code>&gt;&gt;</code> stream operators be overloaded as friend functions? (Because the left operand is <code>std::ostream</code> or <code>std::istream</code>, which cannot be modified).</li>
    <li><span class="check-box"></span> How does the compiler distinguish between prefix <code>++c</code> and postfix <code>c++</code>? (Postfix takes a dummy <code>int</code> parameter: <code>operator++(int)</code>).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"Write a complete C++ program to add two Complex numbers by overloading the '+' operator"</em> is one of the top 3 most frequently asked 10-mark questions in Unit 5. The exact code above provides the full solution.
</div>
"""
    sections.append({
        "id": "u5-sec-9",
        "number": 9,
        "part": "PART 2 — CONSTRUCTORS, DESTRUCTORS & TYPE CONVERSION",
        "title": "9. Operator Overloading",
        "subtitle": "Syntactic Elegance, Member vs Friend Operator Approaches & Unary/Binary Complex Arithmetic",
        "content": sec9_content
    })

    # =========================================================================
    # SECTION 10: Rules of Operator Overloading
    # =========================================================================
    sec10_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 2</div>
    <h3 class="card-title">10. Rules of Operator Overloading: Constraints &amp; Non-Overloadable Operators</h3>
  </div>

  <div class="detail-block">
    <h5>10.1 The Canonical Rules of Operator Overloading</h5>
    <p>
      The C++ compiler enforces strict safety boundaries to prevent programmers from corrupting language grammar:
    </p>
    <ol class="styled-list">
      <li><strong>Existing Operators Only:</strong> Only existing C++ operators can be overloaded. You <strong>cannot invent new operators</strong> (e.g. <code>**</code> for exponentiation or <code>$$</code> are illegal).</li>
      <li><strong>Must Involve at Least One User-Defined Type:</strong> You cannot alter the meaning of operators on primitive types (e.g. you cannot redefine <code>1 + 2</code> to equal <code>5</code>). At least one operand must be a class, struct, or enum.</li>
      <li><strong>Precedence and Associativity are Preserved:</strong> Overloading an operator does NOT alter its binding priority or evaluation direction. <code>*</code> will always have higher precedence than <code>+</code> regardless of user definition.</li>
      <li><strong>Arity Cannot Change:</strong> Unary operators remain unary; binary operators remain binary. You cannot turn division <code>/</code> into a unary operator.</li>
      <li><strong>Default Arguments Disallowed:</strong> Overloaded operator functions cannot have default argument values.</li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>10.2 The Non-Overloadable Operators in C++</h5>
    <p>
      The AKTU syllabus specifically asks which operators <strong>CANNOT be overloaded</strong> under any circumstances:
    </p>
    <div class="spec-table-wrap">
      <table class="spec-table">
        <thead>
          <tr>
            <th>Operator Symbol</th>
            <th>Name / Description</th>
            <th>Reason for Prohibition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>.</code></td>
            <td>Class Member Access Operator</td>
            <td>Guarantees deterministic access to an object's members without redirection.</td>
          </tr>
          <tr>
            <td><code>.*</code></td>
            <td>Pointer-to-Member Dereference Operator</td>
            <td>Core language reflection mechanism that must remain compile-time invariant.</td>
          </tr>
          <tr>
            <td><code>::</code></td>
            <td>Scope Resolution Operator</td>
            <td>Directs compiler lookup across symbol tables; not an expression operator.</td>
          </tr>
          <tr>
            <td><code>?:</code></td>
            <td>Conditional (Ternary) Operator</td>
            <td>Short-circuit evaluation semantics cannot be guaranteed if overloaded.</td>
          </tr>
          <tr>
            <td><code>sizeof</code></td>
            <td>Object Size Query Operator</td>
            <td>Compile-time evaluation required for memory layouts and array sizing.</td>
          </tr>
          <tr>
            <td><code>typeid</code></td>
            <td>RTTI Type Identification Operator</td>
            <td>Core runtime type inquiry mechanism guaranteed by C++ ABI.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="detail-block">
    <h5>10.3 Operators That MUST Be Member Functions</h5>
    <p>
      The following four operators <strong>cannot be overloaded as friend functions</strong>; they MUST be non-static member functions of the class:
    </p>
    <ul>
      <li><code>=</code> (Assignment Operator)</li>
      <li><code>[]</code> (Subscript Operator)</li>
      <li><code>()</code> (Function Call Operator)</li>
      <li><code>-&gt;</code> (Member Access via Pointer Operator)</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Rules of Road Traffic Signs</span>
  </div>
  <p>
    In a sovereign country, municipal authorities allow local districts to assign custom meanings to designated multipurpose spaces (e.g. turning a town square into a festival market). However, the central government enforces non-negotiable highway rules:<br>
    1) You cannot invent your own hexagon traffic signs and force drivers to obey them.<br>
    2) A <strong>Red Traffic Light</strong> and a <strong>Stop Sign</strong> can NEVER be overridden by local shops.<br>
    In C++, operators like <code>.</code>, <code>::</code>, and <code>sizeof</code> are the non-negotiable red lights of the compiler: allowing user code to alter them would break compilation integrity and make everyday code unpredictable!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Valid Operator Overloading vs. Forbidden Operations (Compile-Error Commentary)</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">SafeArray</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">int</span> data[<span class="c-number">5</span>];

<span class="c-keyword">public</span>:
    <span class="c-type">SafeArray</span>() {
        <span class="c-keyword">for</span> (<span class="c-type">int</span> i = <span class="c-number">0</span>; i &lt; <span class="c-number">5</span>; ++i) data[i] = (i + <span class="c-number">1</span>) * <span class="c-number">10</span>;
    }

    <span class="c-comment">// RULE DEMO: Subscript operator [] MUST be a member function!</span>
    <span class="c-type">int</span>&amp; <span class="c-keyword">operator</span>[](<span class="c-type">int</span> index) {
        <span class="c-keyword">if</span> (index &lt; <span class="c-number">0</span> || index &gt;= <span class="c-number">5</span>) {
            std::cout &lt;&lt; <span class="c-string">"Error: Out of bounds! Returning data[0]\\n"</span>;
            <span class="c-keyword">return</span> data[<span class="c-number">0</span>];
        }
        <span class="c-keyword">return</span> data[index];
    }

    <span class="c-comment">// FORBIDDEN OPERATORS (Uncommenting produces compile errors):</span>
    <span class="c-comment">// void operator.() {}      // COMPILE ERROR: '.' cannot be overloaded!</span>
    <span class="c-comment">// void operator::() {}     // COMPILE ERROR: '::' cannot be overloaded!</span>
    <span class="c-comment">// void operator?:() {}     // COMPILE ERROR: '?:' cannot be overloaded!</span>
    <span class="c-comment">// void operator sizeof() {}// COMPILE ERROR: 'sizeof' cannot be overloaded!</span>
};

<span class="c-type">int</span> main() {
    <span class="c-type">SafeArray</span> arr;

    std::cout &lt;&lt; <span class="c-string">"arr[2] = "</span> &lt;&lt; arr[<span class="c-number">2</span>] &lt;&lt; <span class="c-string">"\\n"</span>;
    arr[<span class="c-number">2</span>] = <span class="c-number">99</span>; <span class="c-comment">// Returns L-Value reference</span>
    std::cout &lt;&lt; <span class="c-string">"Mutated arr[2] = "</span> &lt;&lt; arr[<span class="c-number">2</span>] &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Permitted vs Prohibited Overloadable Operators</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Permitted Column -->
      <g transform="translate(30, 20)">
        <rect width="330" height="170" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5"/>
        <text x="165" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">&#x2713; OVERLOADABLE OPERATORS</text>
        <rect x="20" y="45" width="290" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="67" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">+  -  *  /  %  ^  &amp;  |  ~  !</text>
        <rect x="20" y="85" width="290" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="107" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">&lt;  &gt;  &lt;=  &gt;=  ==  !=  &amp;&amp;  ||</text>
        <rect x="20" y="125" width="290" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="147" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">=  []  ()  -&gt;  ++  --  &lt;&lt;  &gt;&gt;</text>
      </g>

      <!-- Forbidden Column -->
      <g transform="translate(400, 20)">
        <rect width="330" height="170" rx="8" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="165" y="28" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">&#x2717; STRICTLY NON-OVERLOADABLE</text>
        
        <g transform="translate(30, 45)">
          <rect x="0" y="0" width="75" height="45" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
          <text x="37" y="28" fill="#ef4444" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">.</text>

          <rect x="95" y="0" width="75" height="45" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
          <text x="132" y="28" fill="#ef4444" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">.*</text>

          <rect x="190" y="0" width="75" height="45" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
          <text x="227" y="28" fill="#ef4444" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">::</text>
        </g>

        <g transform="translate(30, 100)">
          <rect x="0" y="0" width="75" height="45" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
          <text x="37" y="28" fill="#ef4444" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">?:</text>

          <rect x="95" y="0" width="75" height="45" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
          <text x="132" y="28" fill="#ef4444" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">sizeof</text>

          <rect x="190" y="0" width="75" height="45" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
          <text x="227" y="28" fill="#ef4444" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">typeid</text>
        </g>
        <text x="165" y="170" fill="#ef4444" font-size="9" text-anchor="middle">Guaranteed compiler invariants across C++ specification</text>
      </g>
    </svg>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> Name the 6 operators in C++ that can NEVER be overloaded. (<code>.</code>, <code>.*</code>, <code>::</code>, <code>?:</code>, <code>sizeof</code>, <code>typeid</code>).</li>
    <li><span class="check-box"></span> Name the 4 operators that MUST be overloaded as member functions only. (<code>=</code>, <code>[]</code>, <code>()</code>, <code>-&gt;</code>).</li>
    <li><span class="check-box"></span> Can you invent a new operator such as <code>**</code> for exponents in C++? (No! Only existing operators can be overloaded).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"List the rules of operator overloading and mention which operators cannot be overloaded"</em> is a classic 5-mark and 10-mark examination question. Recite the 5 rules above and list all 6 forbidden operators for maximum score.
</div>
"""
    sections.append({
        "id": "u5-sec-10",
        "number": 10,
        "part": "PART 2 — CONSTRUCTORS, DESTRUCTORS & TYPE CONVERSION",
        "title": "10. Rules of Operator Overloading",
        "subtitle": "Syntactic Boundaries, Non-Overloadable Operator Catalog & Mandatory Member Operator Rules",
        "content": sec10_content
    })

    # =========================================================================
    # SECTION 11: Type Conversion
    # =========================================================================
    sec11_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 2</div>
    <h3 class="card-title">11. Type Conversion in C++: Basic &amp; Class Types</h3>
  </div>

  <div class="detail-block">
    <h5>11.1 Taxonomy of Type Conversions in C++</h5>
    <p>
      In pure procedural C, type conversion occurs between primitive numeric types (e.g. <code>float</code> to <code>int</code>). In C++, because classes define brand-new types, type conversions span three distinct architectural dimensions:
    </p>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6>Basic Type to Class Type</h6>
          <p>
            Converting a primitive type (e.g. <code>int</code> or <code>double</code>) into a custom class object. Accomplished via a <strong>Single-Argument Conversion Constructor</strong>:
          </p>
          <div class="code-box"><code>Time t = 120; // 120 minutes converted to Time object (2 hrs, 0 mins)</code></div>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6>Class Type to Basic Type</h6>
          <p>
            Converting a custom class object into a primitive type (e.g. <code>Complex</code> to <code>double</code> magnitude). Accomplished via a <strong>Conversion Operator Function (Casting Operator)</strong>:
          </p>
          <div class="code-box"><code>operator double() const { return std::sqrt(real*real + imag*imag); }</code></div>
          <p>Rules: Has no return type in header, accepts no arguments, must be a member function.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">3</span>
        <div class="step-content">
          <h6>Class Type to Another Class Type</h6>
          <p>
            Converting an object of <code>ClassSource</code> into an object of <code>ClassDestination</code> (e.g. converting <code>PolarCoords</code> to <code>CartesianCoords</code>). Can be implemented either as a conversion constructor in the destination class, or as a casting operator in the source class.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Currency Exchange &amp; Units Conversion</span>
  </div>
  <p>
    - <strong>Basic to Class Type:</strong> You hand a raw integer number <code>5000</code> to an international bank teller, and they hand you back a structured <strong>BankDraft Object</strong> (with security seals, watermarks, account tokens). A raw number became a rich object.<br>
    - <strong>Class to Basic Type:</strong> You hand an international traveler's check object to the cashier, and they hand you back raw cash banknotes (<code>double totalCash</code>). A rich object collapsed into a primitive value!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating Basic-to-Class (Constructor) & Class-to-Basic (Casting Operator)</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Duration</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">int</span> hours;
    <span class="c-type">int</span> minutes;

<span class="c-keyword">public</span>:
    <span class="c-type">Duration</span>() : hours(<span class="c-number">0</span>), minutes(<span class="c-number">0</span>) {}

    <span class="c-comment">// 1. BASIC TYPE TO CLASS TYPE: Single-argument constructor</span>
    <span class="c-type">Duration</span>(<span class="c-type">int</span> totalMinutes) {
        hours = totalMinutes / <span class="c-number">60</span>;
        minutes = totalMinutes % <span class="c-number">60</span>;
        std::cout &lt;&lt; <span class="c-string">"[Conversion Constructor] "</span> &lt;&lt; totalMinutes 
                  &lt;&lt; <span class="c-string">" mins &rarr; "</span> &lt;&lt; hours &lt;&lt; <span class="c-string">"h "</span> &lt;&lt; minutes &lt;&lt; <span class="c-string">"m\\n"</span>;
    }

    <span class="c-comment">// 2. CLASS TYPE TO BASIC TYPE: Casting operator</span>
    <span class="c-comment">// Notice: NO return type written; returns int; accepts 0 args</span>
    <span class="c-keyword">operator</span> <span class="c-type">int</span>() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> (hours * <span class="c-number">60</span>) + minutes;
    }

    <span class="c-type">void</span> display() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; hours &lt;&lt; <span class="c-string">" hrs, "</span> &lt;&lt; minutes &lt;&lt; <span class="c-string">" mins\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Type Conversion Demonstration ===\\n"</span>;

    <span class="c-comment">// Basic to Class: 155 (int) converted automatically to Duration object</span>
    <span class="c-type">int</span> rawMins = <span class="c-number">155</span>;
    <span class="c-type">Duration</span> d1 = rawMins; <span class="c-comment">// Implicit conversion</span>
    std::cout &lt;&lt; <span class="c-string">"Duration d1: "</span>;
    d1.display();

    <span class="c-comment">// Class to Basic: Duration object converted back to int</span>
    <span class="c-type">int</span> extractedMins = d1; <span class="c-comment">// Calls operator int()</span>
    std::cout &lt;&lt; <span class="c-string">"Extracted back to primitive int: "</span> &lt;&lt; extractedMins &lt;&lt; <span class="c-string">" minutes\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Two-Way Type Conversion Bridge</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Basic Type Block -->
      <g transform="translate(30, 40)">
        <rect width="200" height="130" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="100" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Basic Type (Primitive)</text>
        <rect x="20" y="50" width="160" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="100" y="75" fill="var(--text-primary)" font-family="monospace" font-size="12" text-anchor="middle">int rawMins = 155;</text>
        <text x="100" y="112" fill="var(--text-muted)" font-size="9" text-anchor="middle">4 Bytes primitive scalar</text>
      </g>

      <!-- Conversion Constructor (Right Arrow) -->
      <path d="M 235 75 L 515 75" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <rect x="280" y="55" width="190" height="24" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
      <text x="375" y="71" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Conversion Constructor &rarr;</text>

      <!-- Casting Operator (Left Arrow) -->
      <path d="M 515 135 L 235 135" stroke="#a855f7" stroke-width="2" marker-end="url(#arrowhead)"/>
      <rect x="280" y="123" width="190" height="24" rx="4" fill="var(--bg-card)" stroke="#a855f7"/>
      <text x="375" y="139" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">&larr; operator int() Casting</text>

      <!-- Class Type Block -->
      <g transform="translate(520, 40)">
        <rect width="210" height="130" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="105" y="30" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Class Type (Object)</text>
        <rect x="15" y="50" width="180" height="40" rx="4" fill="var(--bg-elevated)"/>
        <text x="105" y="68" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">Duration d1;</text>
        <text x="105" y="82" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">hours=2, mins=35</text>
        <text x="105" y="112" fill="var(--text-muted)" font-size="9" text-anchor="middle">Structured user-defined object</text>
      </g>
    </svg>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> How is Basic-to-Class type conversion implemented? (Using a single-argument conversion constructor in the class).</li>
    <li><span class="check-box"></span> What are the 3 syntax rules of a Class-to-Basic casting operator? (No return type, no arguments, must be a class member function).</li>
    <li><span class="check-box"></span> How do you prevent unintentional implicit basic-to-class conversions? (Prefix the constructor with the <code>explicit</code> keyword).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Questions asking: <em>"Explain type conversion in C++: Basic to Class type and Class to Basic type with examples"</em> appear repeatedly. Always write the <code>Duration</code> / <code>Time</code> class with its constructor <code>Time(int)</code> and casting operator <code>operator int()</code>.
</div>
"""
    sections.append({
        "id": "u5-sec-11",
        "number": 11,
        "part": "PART 2 — CONSTRUCTORS, DESTRUCTORS & TYPE CONVERSION",
        "title": "11. Type Conversion",
        "subtitle": "Basic to Class Type (Constructors), Class to Basic Type (Casting Operators) & Two-Way Conversions",
        "content": sec11_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit5_part2_sections()
    print(f"generate_unit5_part2.py compiled {len(secs)} sections successfully.")
