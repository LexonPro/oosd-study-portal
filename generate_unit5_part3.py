# -*- coding: utf-8 -*-
"""
generate_unit5_part3.py: Generates Sections 12 to 17 for Unit 5
Topics:
  12. Concept of Inheritance (Base & Derived Classes, Code Reusability, Is-A Hierarchy)
  13. Modes of Inheritance (Public, Protected, Private & The 3x3 Visibility Matrix)
  14. Types of Inheritance (Single, Multiple, Multilevel, Hierarchical, Hybrid)
  15. Protected Members (Access Mechanics, Encapsulation vs Inheritance Trade-off)
  16. Function Overriding (Derived Class Specialization & Overloading vs Overriding)
  17. Virtual Base Class (The Diamond Problem, Multipath Redundancy Resolution)
"""

def get_unit5_part3_sections():
    sections = []

    # =========================================================================
    # SECTION 12: Concept of Inheritance
    # =========================================================================
    sec12_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 3</div>
    <h3 class="card-title">12. Concept of Inheritance: Hierarchical Code Reusability</h3>
  </div>

  <div class="detail-block">
    <h5>12.1 Meaning and Purpose of Inheritance</h5>
    <p>
      <strong>Inheritance</strong> is the core mechanism of Object-Oriented Programming by which a new class (called the <strong>Derived Class</strong> or Subclass) derives attributes (data members) and behaviors (member functions) from an existing class (called the <strong>Base Class</strong> or Superclass).
    </p>
    <ul>
      <li><strong>Is-A Relationship:</strong> Models fundamental real-world hierarchical taxonomies (e.g. <code>Car is-a Vehicle</code>, <code>Manager is-a Employee</code>, <code>Circle is-a Shape</code>).</li>
      <li><strong>Software Reusability:</strong> Common foundational logic is authored once in the base class. Derived classes instantly inherit this logic without re-writing or copy-pasting code, dramatically reducing codebase size and bug surface area.</li>
      <li><strong>Extensibility:</strong> New features can be cleanly added to derived classes without modifying or endangering the battle-tested base class code (conforming to the Open/Closed Principle).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>12.2 Basic Syntax of Inheritance in C++</h5>
    <div class="code-box">
      <code>class DerivedClass : accessSpecifier BaseClass {<br>
&nbsp;&nbsp;&nbsp;&nbsp;// Additional derived data members and functions<br>
};</code>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Automotive Vehicle Hierarchy</span>
  </div>
  <p>
    Consider the design of modern transportation vehicles:<br>
    - <strong>Base Class (Vehicle):</strong> Defines universal traits: <code>engineCapacity</code>, <code>fuelType</code>, and actions <code>startIgnition()</code> and <code>applyBrakes()</code>.<br>
    - <strong>Derived Class (ElectricCar):</strong> Automatically inherits <code>engineCapacity</code> and <code>applyBrakes()</code> from Vehicle for free! It then adds its own specialized derived members: <code>batteryKWh</code> and <code>engageRegenerativeBraking()</code>.<br>
    The electrical automotive engineers did not need to reinvent the wheel or re-engineer hydraulic brake calipers from scratch; they inherited the foundation and specialized on top!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Base Class vs. Derived Class: Code Reusability & Feature Specialization</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// 1. BASE CLASS (Parent / Super Class)</span>
<span class="c-keyword">class</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">protected</span>:
    <span class="c-type">std::string</span> brandName;
    <span class="c-type">int</span> topSpeedKmPerHour;

<span class="c-keyword">public</span>:
    <span class="c-type">Vehicle</span>(<span class="c-type">std::string</span> brand, <span class="c-type">int</span> speed) 
        : brandName(brand), topSpeedKmPerHour(speed) {}

    <span class="c-type">void</span> startIgnition() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"["</span> &lt;&lt; brandName &lt;&lt; <span class="c-string">"] Ignition activated. Ready to roll.\\n"</span>;
    }

    <span class="c-type">void</span> showSpecs() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Brand: "</span> &lt;&lt; brandName 
                  &lt;&lt; <span class="c-string">" | Top Speed: "</span> &lt;&lt; topSpeedKmPerHour &lt;&lt; <span class="c-string">" km/h\\n"</span>;
    }
};

<span class="c-comment">// 2. DERIVED CLASS (Child / Sub Class): Inherits publicly from Vehicle</span>
<span class="c-keyword">class</span> <span class="c-type">ElectricCar</span> : <span class="c-keyword">public</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">double</span> batteryCapacityKWh;

<span class="c-keyword">public</span>:
    <span class="c-comment">// Passes base parameters up to Vehicle constructor via initialization list</span>
    <span class="c-type">ElectricCar</span>(<span class="c-type">std::string</span> brand, <span class="c-type">int</span> speed, <span class="c-type">double</span> battery)
        : <span class="c-type">Vehicle</span>(brand, speed), batteryCapacityKWh(battery) {}

    <span class="c-type">void</span> engageAutopilot() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"["</span> &lt;&lt; brandName 
                  &lt;&lt; <span class="c-string">"] Neural Vision Autopilot engaged with "</span> 
                  &lt;&lt; batteryCapacityKWh &lt;&lt; <span class="c-string">" kWh battery reserve.\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Testing Inheritance in C++ ===\\n"</span>;

    <span class="c-comment">// Instantiate derived class object</span>
    <span class="c-type">ElectricCar</span> myTesla(<span class="c-string">"Tesla Model S"</span>, <span class="c-number">250</span>, <span class="c-number">100.0</span>);

    <span class="c-comment">// Calling INHERITED base class methods directly on derived object</span>
    myTesla.startIgnition();
    myTesla.showSpecs();

    <span class="c-comment">// Calling specialized derived class method</span>
    myTesla.engageAutopilot();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Base Class to Derived Class Inheritance Hierarchy</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Base Class Box -->
      <g transform="translate(40, 20)">
        <rect width="280" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="140" y="28" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Base Class: Vehicle</text>
        <rect x="15" y="45" width="250" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="140" y="65" fill="var(--text-secondary)" font-family="monospace" font-size="10" text-anchor="middle">protected: brandName, topSpeed</text>
        <rect x="15" y="95" width="250" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="140" y="115" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">public: startIgnition(), showSpecs()</text>
        <text x="140" y="155" fill="var(--text-muted)" font-size="9" text-anchor="middle">Universal automotive foundation</text>
      </g>

      <!-- UML Generalization Arrow -->
      <g transform="translate(340, 105)">
        <path d="M 60 0 L 0 0" stroke="#10b981" stroke-width="2"/>
        <polygon points="60,-8 75,0 60,8" fill="none" stroke="#10b981" stroke-width="2"/>
        <text x="35" y="-12" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">is-a</text>
      </g>

      <!-- Derived Class Box -->
      <g transform="translate(440, 20)">
        <rect width="280" height="170" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="2"/>
        <text x="140" y="28" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Derived Class: ElectricCar</text>
        <rect x="15" y="45" width="250" height="30" rx="4" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="140" y="65" fill="#38bdf8" font-size="10" text-anchor="middle">&check; Inherits all Vehicle members!</text>
        <rect x="15" y="85" width="250" height="40" rx="4" fill="var(--bg-elevated)"/>
        <text x="140" y="105" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">private: double batteryCapacityKWh</text>
        <rect x="15" y="130" width="250" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="140" y="150" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">public: engageAutopilot()</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Quantum asks: <em>"What is inheritance? What are the advantages of inheritance in C++?"</em> Emphasize two major advantages: 1) Code Reusability, and 2) Facilitating Runtime Polymorphism through dynamic binding.
</div>
"""
    sections.append({
        "id": "u5-sec-12",
        "number": 12,
        "part": "PART 3 — INHERITANCE",
        "title": "12. Concept of Inheritance",
        "subtitle": "Base vs Derived Classes, Is-A Relationships, Code Reusability & Constructor Delegation",
        "content": sec12_content
    })

    # =========================================================================
    # SECTION 13: Modes of Inheritance
    # =========================================================================
    sec13_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 3</div>
    <h3 class="card-title">13. Modes of Inheritance: The 3x3 Visibility Matrix</h3>
  </div>

  <div class="detail-block">
    <h5>13.1 What is an Inheritance Mode?</h5>
    <p>
      When deriving a class in C++, an access specifier (<code>public</code>, <code>protected</code>, or <code>private</code>) is placed immediately before the base class name. This access specifier determines the maximum visibility level of inherited members inside the derived class and to external client code.
    </p>
    <ul>
      <li><strong>Public Inheritance (<code>class Derived : public Base</code>):</strong> Models true subtyping (<em>is-a</em>). Public members remain public; protected members remain protected.</li>
      <li><strong>Protected Inheritance (<code>class Derived : protected Base</code>):</strong> Both public and protected base members become <code>protected</code> in the derived class. External code cannot access them.</li>
      <li><strong>Private Inheritance (<code>class Derived : private Base</code>):</strong> Both public and protected base members become <code>private</code> in the derived class. Models implementation reuse (<em>has-a / implemented-in-terms-of</em>). Default inheritance mode if specifier is omitted!</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>13.2 The Master 3x3 Inheritance Visibility Matrix</h5>
    <div class="spec-table-wrap">
      <table class="spec-table">
        <thead>
          <tr>
            <th>Base Class Member Visibility</th>
            <th>Derived via <code>public</code></th>
            <th>Derived via <code>protected</code></th>
            <th>Derived via <code>private</code></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong><code>public</code></strong></td>
            <td><code>public</code></td>
            <td><code>protected</code></td>
            <td><code>private</code></td>
          </tr>
          <tr>
            <td><strong><code>protected</code></strong></td>
            <td><code>protected</code></td>
            <td><code>protected</code></td>
            <td><code>private</code></td>
          </tr>
          <tr style="background: rgba(239, 68, 68, 0.08);">
            <td><strong><code>private</code></strong></td>
            <td><strong>Never Inherited Directly</strong> (Hidden / Inaccessible)</td>
            <td><strong>Never Inherited Directly</strong> (Hidden / Inaccessible)</td>
            <td><strong>Never Inherited Directly</strong> (Hidden / Inaccessible)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Security Classification Downgrade Rules</span>
  </div>
  <p>
    Think of inheritance modes as a corporate security clearance gateway:<br>
    - <strong>Public Mode (Open Gateway):</strong> What was public stays public; what was confidential stays confidential.<br>
    - <strong>Protected Mode (Internal Downgrade):</strong> The corporate headquarters declares: <em>"Everything inherited from parent firm is now classified as Internal Company Confidential."</em> External customers cannot see it, but child branch offices can.<br>
    - <strong>Private Mode (Top-Secret Lockdown):</strong> Everything inherited from the parent firm is classified as <em>Top-Secret Black Box</em>. Neither external customers nor any future grandchild subsidiaries can access it!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Comparing Public, Protected & Private Inheritance Access Constraints</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Base</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">int</span> pubVar = <span class="c-number">10</span>;
<span class="c-keyword">protected</span>:
    <span class="c-type">int</span> protVar = <span class="c-number">20</span>;
<span class="c-keyword">private</span>:
    <span class="c-type">int</span> privVar = <span class="c-number">30</span>; <span class="c-comment">// Inaccessible to ANY derived class!</span>
};

<span class="c-comment">// 1. PUBLIC INHERITANCE: pubVar remains public; protVar remains protected</span>
<span class="c-keyword">class</span> <span class="c-type">PubDerived</span> : <span class="c-keyword">public</span> <span class="c-type">Base</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">void</span> accessMembers() {
        std::cout &lt;&lt; pubVar &lt;&lt; <span class="c-string">" "</span> &lt;&lt; protVar &lt;&lt; <span class="c-string">"\\n"</span>; <span class="c-comment">// Allowed</span>
        <span class="c-comment">// std::cout &lt;&lt; privVar; // COMPILE ERROR: private in Base</span>
    }
};

<span class="c-comment">// 2. PROTECTED INHERITANCE: pubVar and protVar become protected</span>
<span class="c-keyword">class</span> <span class="c-type">ProtDerived</span> : <span class="c-keyword">protected</span> <span class="c-type">Base</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">void</span> accessMembers() {
        std::cout &lt;&lt; pubVar &lt;&lt; <span class="c-string">" "</span> &lt;&lt; protVar &lt;&lt; <span class="c-string">"\\n"</span>; <span class="c-comment">// Allowed inside class</span>
    }
};

<span class="c-comment">// 3. PRIVATE INHERITANCE: pubVar and protVar become private</span>
<span class="c-keyword">class</span> <span class="c-type">PrivDerived</span> : <span class="c-keyword">private</span> <span class="c-type">Base</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">void</span> accessMembers() {
        std::cout &lt;&lt; pubVar &lt;&lt; <span class="c-string">" "</span> &lt;&lt; protVar &lt;&lt; <span class="c-string">"\\n"</span>; <span class="c-comment">// Allowed inside class</span>
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">PubDerived</span> obj1;
    std::cout &lt;&lt; <span class="c-string">"PubDerived pubVar: "</span> &lt;&lt; obj1.pubVar &lt;&lt; <span class="c-string">"\\n"</span>; <span class="c-comment">// Legal</span>

    <span class="c-type">ProtDerived</span> obj2;
    <span class="c-comment">// std::cout &lt;&lt; obj2.pubVar; // COMPILE ERROR: pubVar became protected!</span>

    <span class="c-type">PrivDerived</span> obj3;
    <span class="c-comment">// std::cout &lt;&lt; obj3.pubVar; // COMPILE ERROR: pubVar became private!</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Access Specifier Inheritance Transformation Pipeline</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Base Class Definition -->
      <g transform="translate(30, 20)">
        <rect width="180" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="90" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Base Class Scope</text>
        <rect x="15" y="45" width="150" height="30" rx="4" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="90" y="65" fill="#10b981" font-size="11" text-anchor="middle">public: pubVar</text>
        <rect x="15" y="85" width="150" height="30" rx="4" fill="rgba(245, 158, 11, 0.15)"/>
        <text x="90" y="105" fill="#f59e0b" font-size="11" text-anchor="middle">protected: protVar</text>
        <rect x="15" y="125" width="150" height="30" rx="4" fill="rgba(239, 68, 68, 0.15)"/>
        <text x="90" y="145" fill="#ef4444" font-size="11" text-anchor="middle">private: privVar</text>
      </g>

      <!-- 3 Destination Mode Columns -->
      <!-- Public Mode -->
      <g transform="translate(250, 20)">
        <rect width="150" height="170" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="75" y="28" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">: public Base</text>
        <rect x="10" y="45" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="65" fill="#10b981" font-size="10" text-anchor="middle">public</text>
        <rect x="10" y="85" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="105" fill="#f59e0b" font-size="10" text-anchor="middle">protected</text>
        <rect x="10" y="125" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="145" fill="#ef4444" font-size="10" text-anchor="middle">Hidden (Inaccessible)</text>
      </g>

      <!-- Protected Mode -->
      <g transform="translate(420, 20)">
        <rect width="150" height="170" rx="8" fill="var(--bg-card)" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="75" y="28" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">: protected Base</text>
        <rect x="10" y="45" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="65" fill="#f59e0b" font-size="10" text-anchor="middle">protected</text>
        <rect x="10" y="85" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="105" fill="#f59e0b" font-size="10" text-anchor="middle">protected</text>
        <rect x="10" y="125" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="145" fill="#ef4444" font-size="10" text-anchor="middle">Hidden (Inaccessible)</text>
      </g>

      <!-- Private Mode -->
      <g transform="translate(590, 20)">
        <rect width="150" height="170" rx="8" fill="var(--bg-card)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="75" y="28" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">: private Base</text>
        <rect x="10" y="45" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="65" fill="#ef4444" font-size="10" text-anchor="middle">private</text>
        <rect x="10" y="85" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="105" fill="#ef4444" font-size="10" text-anchor="middle">private</text>
        <rect x="10" y="125" width="130" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="75" y="145" fill="#ef4444" font-size="10" text-anchor="middle">Hidden (Inaccessible)</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> AKTU questions routinely ask: <em>"Explain the visibility of base class members in public, private, and protected inheritance modes with a table."</em> Draw the 3x3 table above and highlight that <code>private</code> members are NEVER directly accessible in derived classes.
</div>
"""
    sections.append({
        "id": "u5-sec-13",
        "number": 13,
        "part": "PART 3 — INHERITANCE",
        "title": "13. Modes of Inheritance",
        "subtitle": "Public, Protected & Private Access Modes, The 3x3 Visibility Matrix & Downgrade Semantics",
        "content": sec13_content
    })

    # =========================================================================
    # SECTION 14: Types of Inheritance
    # =========================================================================
    sec14_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 3</div>
    <h3 class="card-title">14. Types of Inheritance: Architectural Taxonomies</h3>
  </div>

  <div class="detail-block">
    <h5>14.1 The Five Structural Types of Inheritance</h5>
    <p>
      Depending on how base and derived classes are connected, C++ supports 5 distinct inheritance configurations:
    </p>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6>Single Inheritance</h6>
          <p>A single derived class inherits from a single base class (<code>A &rarr; B</code>). The simplest and cleanest form of subtyping.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6>Multiple Inheritance</h6>
          <p>A single derived class inherits directly from two or more base classes simultaneously (<code>A, B &rarr; C</code>). Powerful, but can introduce name ambiguity.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">3</span>
        <div class="step-content">
          <h6>Multilevel Inheritance</h6>
          <p>A derived class acts as the base class for another derived class, forming a chain of inheritance (<code>A &rarr; B &rarr; C</code>).</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">4</span>
        <div class="step-content">
          <h6>Hierarchical Inheritance</h6>
          <p>Multiple derived classes inherit from a single common base class (<code>A &rarr; B</code> and <code>A &rarr; C</code>), forming a tree branch.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">5</span>
        <div class="step-content">
          <h6>Hybrid Inheritance</h6>
          <p>A combination of two or more of the above inheritance types in a single system (e.g. Hierarchical + Multiple, forming a Diamond pattern).</p>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Academic University Hierarchy</span>
  </div>
  <p>
    - <strong>Single:</strong> <code>Student &rarr; EngineeringStudent</code>.<br>
    - <strong>Multilevel:</strong> <code>Person &rarr; Employee &rarr; Professor</code> (Professor has Person properties through Employee).<br>
    - <strong>Multiple:</strong> <code>TeachingAssistant</code> inherits both from <code>Student</code> (submits coursework) and <code>Employee</code> (receives monthly salary stipend).<br>
    - <strong>Hierarchical:</strong> <code>Person &rarr; Student</code> and <code>Person &rarr; Faculty</code> (both branch off from Person).<br>
    - <strong>Hybrid:</strong> Combining all the above creates the campus operational architecture!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Multiple Inheritance: TeachingAssistant Deriving from Student & Faculty</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// Base Class 1</span>
<span class="c-keyword">class</span> <span class="c-type">Student</span> {
<span class="c-keyword">protected</span>:
    <span class="c-type">int</span> rollNumber;
<span class="c-keyword">public</span>:
    <span class="c-type">Student</span>(<span class="c-type">int</span> roll) : rollNumber(roll) {}
    <span class="c-type">void</span> showAcademicInfo() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Student Roll: "</span> &lt;&lt; rollNumber &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-comment">// Base Class 2</span>
<span class="c-keyword">class</span> <span class="c-type">Faculty</span> {
<span class="c-keyword">protected</span>:
    <span class="c-type">std::string</span> department;
<span class="c-keyword">public</span>:
    <span class="c-type">Faculty</span>(<span class="c-type">std::string</span> dept) : department(dept) {}
    <span class="c-type">void</span> showFacultyInfo() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Department:   "</span> &lt;&lt; department &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-comment">// MULTIPLE INHERITANCE: TeachingAssistant inherits from BOTH Student & Faculty</span>
<span class="c-keyword">class</span> <span class="c-type">TeachingAssistant</span> : <span class="c-keyword">public</span> <span class="c-type">Student</span>, <span class="c-keyword">public</span> <span class="c-type">Faculty</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">double</span> monthlyStipend;
<span class="c-keyword">public</span>:
    <span class="c-type">TeachingAssistant</span>(<span class="c-type">int</span> roll, <span class="c-type">std::string</span> dept, <span class="c-type">double</span> stipend)
        : <span class="c-type">Student</span>(roll), <span class="c-type">Faculty</span>(dept), monthlyStipend(stipend) {}

    <span class="c-type">void</span> showFullProfile() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"=== Teaching Assistant Profile ===\\n"</span>;
        showAcademicInfo(); <span class="c-comment">// From Student</span>
        showFacultyInfo();  <span class="c-comment">// From Faculty</span>
        std::cout &lt;&lt; <span class="c-string">"Stipend:      Rs. "</span> &lt;&lt; monthlyStipend &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">TeachingAssistant</span> ta(<span class="c-number">202401</span>, <span class="c-string">"Computer Science"</span>, <span class="c-number">35000.0</span>);
    ta.showFullProfile();
    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The 5 Canonical Topologies of Inheritance</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- 1. Single -->
      <g transform="translate(25, 20)">
        <rect width="125" height="170" rx="6" fill="var(--bg-elevated)" stroke="#38bdf8"/>
        <text x="62" y="22" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Single</text>
        <rect x="27" y="40" width="70" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="60" fill="var(--text-primary)" font-size="11" text-anchor="middle">A</text>
        <path d="M 62 70 L 62 110" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <rect x="27" y="110" width="70" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="130" fill="var(--text-primary)" font-size="11" text-anchor="middle">B</text>
      </g>

      <!-- 2. Multiple -->
      <g transform="translate(170, 20)">
        <rect width="130" height="170" rx="6" fill="var(--bg-elevated)" stroke="#10b981"/>
        <text x="65" y="22" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Multiple</text>
        <rect x="12" y="40" width="45" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="34" y="60" fill="var(--text-primary)" font-size="11" text-anchor="middle">A</text>
        <rect x="73" y="40" width="45" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="95" y="60" fill="var(--text-primary)" font-size="11" text-anchor="middle">B</text>
        <path d="M 34 70 L 65 110" stroke="#10b981" stroke-width="1.5"/>
        <path d="M 95 70 L 65 110" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <rect x="35" y="110" width="60" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="65" y="130" fill="var(--text-primary)" font-size="11" text-anchor="middle">C</text>
      </g>

      <!-- 3. Multilevel -->
      <g transform="translate(320, 20)">
        <rect width="125" height="170" rx="6" fill="var(--bg-elevated)" stroke="#6366f1"/>
        <text x="62" y="22" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Multilevel</text>
        <rect x="32" y="35" width="60" height="25" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="52" fill="var(--text-primary)" font-size="10" text-anchor="middle">A</text>
        <path d="M 62 60 L 62 85" stroke="#6366f1" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <rect x="32" y="85" width="60" height="25" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="102" fill="var(--text-primary)" font-size="10" text-anchor="middle">B</text>
        <path d="M 62 110 L 62 135" stroke="#6366f1" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <rect x="32" y="135" width="60" height="25" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="152" fill="var(--text-primary)" font-size="10" text-anchor="middle">C</text>
      </g>

      <!-- 4. Hierarchical -->
      <g transform="translate(465, 20)">
        <rect width="130" height="170" rx="6" fill="var(--bg-elevated)" stroke="#f59e0b"/>
        <text x="65" y="22" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Hierarchical</text>
        <rect x="35" y="40" width="60" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="65" y="60" fill="var(--text-primary)" font-size="11" text-anchor="middle">A</text>
        <path d="M 50 70 L 34 110" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <path d="M 80 70 L 96 110" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <rect x="12" y="110" width="45" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="34" y="130" fill="var(--text-primary)" font-size="11" text-anchor="middle">B</text>
        <rect x="73" y="110" width="45" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="95" y="130" fill="var(--text-primary)" font-size="11" text-anchor="middle">C</text>
      </g>

      <!-- 5. Hybrid (Diamond) -->
      <g transform="translate(615, 20)">
        <rect width="125" height="170" rx="6" fill="var(--bg-elevated)" stroke="#ef4444"/>
        <text x="62" y="22" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Hybrid</text>
        <rect x="37" y="35" width="50" height="22" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="50" fill="var(--text-primary)" font-size="9" text-anchor="middle">A</text>
        <path d="M 50 57 L 27 80" stroke="#ef4444" stroke-width="1.5"/>
        <path d="M 74 57 L 97 80" stroke="#ef4444" stroke-width="1.5"/>
        <rect x="12" y="80" width="40" height="22" rx="4" fill="var(--bg-card)"/>
        <text x="32" y="95" fill="var(--text-primary)" font-size="9" text-anchor="middle">B</text>
        <rect x="73" y="80" width="40" height="22" rx="4" fill="var(--bg-card)"/>
        <text x="93" y="95" fill="var(--text-primary)" font-size="9" text-anchor="middle">C</text>
        <path d="M 32 102 L 55 125" stroke="#ef4444" stroke-width="1.5"/>
        <path d="M 93 102 L 69 125" stroke="#ef4444" stroke-width="1.5" marker-end="url(#arrowhead)"/>
        <rect x="37" y="125" width="50" height="22" rx="4" fill="var(--bg-card)"/>
        <text x="62" y="140" fill="var(--text-primary)" font-size="9" text-anchor="middle">D</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"Explain different types of inheritance in C++ with diagrams and examples"</em> is a classic 10-mark question. Draw the 5 topological boxes shown in the visual diagram above, write the class header syntax for each, and demonstrate Multiple inheritance using <code>Student</code>, <code>Faculty</code>, and <code>TeachingAssistant</code>.
</div>
"""
    sections.append({
        "id": "u5-sec-14",
        "number": 14,
        "part": "PART 3 — INHERITANCE",
        "title": "14. Types of Inheritance",
        "subtitle": "Single, Multiple, Multilevel, Hierarchical & Hybrid Topologies with Concrete Implementations",
        "content": sec14_content
    })

    # =========================================================================
    # SECTION 15: Protected Members
    # =========================================================================
    sec15_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 3</div>
    <h3 class="card-title">15. Protected Members: The Inheritance Access Bridge</h3>
  </div>

  <div class="detail-block">
    <h5>15.1 Meaning of Protected Members</h5>
    <p>
      In pure OOP, <code>private</code> variables are completely hidden from the entire universe &mdash; including a class's own derived children. However, a derived class frequently needs direct access to base attributes (e.g. <code>Circle</code> needs direct access to <code>Shape::originX</code>) without exposing those variables publicly to external code in <code>main()</code>.
    </p>
    <p>
      The <strong><code>protected:</code></strong> access specifier provides precisely this compromise: <strong>it acts as private to external client code, but acts as accessible to derived classes</strong> throughout the inheritance hierarchy.
    </p>
  </div>

  <div class="detail-block">
    <h5>15.2 Public vs. Protected vs. Private: The Definitive Comparison</h5>
    <div class="spec-table-wrap">
      <table class="spec-table">
        <thead>
          <tr>
            <th>Access Location</th>
            <th><code>public</code> Members</th>
            <th><code>protected</code> Members</th>
            <th><code>private</code> Members</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Inside Base Class</strong></td>
            <td>&#x2713; Full Access</td>
            <td>&#x2713; Full Access</td>
            <td>&#x2713; Full Access</td>
          </tr>
          <tr>
            <td><strong>Inside Derived Class</strong></td>
            <td>&#x2713; Full Access</td>
            <td>&#x2713; Full Access</td>
            <td>&#x2717; <strong>Inaccessible</strong></td>
          </tr>
          <tr>
            <td><strong>Outside Client Code (main)</strong></td>
            <td>&#x2713; Full Access (<code>obj.var</code>)</td>
            <td>&#x2717; <strong>Inaccessible</strong></td>
            <td>&#x2717; <strong>Inaccessible</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Family Secret Recipe Book</span>
  </div>
  <p>
    Consider a grandmother's secret heirloom culinary recipe:<br>
    - <strong>Public:</strong> The restaurant menu outside the dining hall. Any passerby can read it.<br>
    - <strong>Private:</strong> Grandmother's personal secret bank account PIN. She shares it with nobody, not even her own children.<br>
    - <strong>Protected:</strong> The handwritten <strong>Secret Spice Blend Recipe</strong> locked in the family cabinet. Strangers on the street cannot read it (it is hidden from the public). However, her children and grandchildren (the Derived Classes) are granted permission to open the cabinet and cook with it!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Direct Manipulation of Protected Base Data Members Inside Derived Classes</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Shape</span> {
<span class="c-keyword">protected</span>:
    <span class="c-comment">// PROTECTED: Inaccessible from main(), but fully accessible in Derived</span>
    <span class="c-type">double</span> dimensionX;
    <span class="c-type">double</span> dimensionY;

<span class="c-keyword">public</span>:
    <span class="c-type">Shape</span>(<span class="c-type">double</span> x, <span class="c-type">double</span> y) : dimensionX(x), dimensionY(y) {}
};

<span class="c-keyword">class</span> <span class="c-type">Rectangle</span> : <span class="c-keyword">public</span> <span class="c-type">Shape</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">Rectangle</span>(<span class="c-type">double</span> width, <span class="c-type">double</span> height) : <span class="c-type">Shape</span>(width, height) {}

    <span class="c-type">double</span> computeArea() {
        <span class="c-comment">// Direct read access to base protected members!</span>
        <span class="c-keyword">return</span> dimensionX * dimensionY;
    }

    <span class="c-type">void</span> scaleDimensions(<span class="c-type">double</span> factor) {
        <span class="c-comment">// Direct write mutation of base protected members!</span>
        dimensionX *= factor;
        dimensionY *= factor;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">Rectangle</span> rect(<span class="c-number">10.0</span>, <span class="c-number">5.0</span>);

    std::cout &lt;&lt; <span class="c-string">"Rectangle Area: "</span> &lt;&lt; rect.computeArea() &lt;&lt; <span class="c-string">" sq units\\n"</span>;
    rect.scaleDimensions(<span class="c-number">2.0</span>);
    std::cout &lt;&lt; <span class="c-string">"Scaled Area:    "</span> &lt;&lt; rect.computeArea() &lt;&lt; <span class="c-string">" sq units\\n"</span>;

    <span class="c-comment">// ILLEGAL ATTEMPT (Compile Error!):</span>
    <span class="c-comment">// rect.dimensionX = 50.0; // COMPILE ERROR: 'dimensionX' is protected!</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Three-Tier Access Membrane (Public, Protected, Private)</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Public Tier -->
      <g transform="translate(30, 20)">
        <rect width="220" height="170" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5"/>
        <text x="110" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">1. Public Tier (Open)</text>
        <rect x="15" y="45" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="65" fill="#10b981" font-size="10" text-anchor="middle">&check; Base Class Members</text>
        <rect x="15" y="85" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="105" fill="#10b981" font-size="10" text-anchor="middle">&check; Derived Class Members</text>
        <rect x="15" y="125" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="145" fill="#10b981" font-size="10" text-anchor="middle">&check; External main() Code</text>
      </g>

      <!-- Protected Tier -->
      <g transform="translate(270, 20)">
        <rect width="220" height="170" rx="8" fill="rgba(245, 158, 11, 0.08)" stroke="#f59e0b" stroke-width="2"/>
        <text x="110" y="28" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">2. Protected Tier (Family)</text>
        <rect x="15" y="45" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="65" fill="#10b981" font-size="10" text-anchor="middle">&check; Base Class Members</text>
        <rect x="15" y="85" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="105" fill="#10b981" font-size="10" text-anchor="middle">&check; Derived Class Members</text>
        <rect x="15" y="125" width="190" height="30" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444"/>
        <text x="110" y="145" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">&cross; External main() BLOCKED</text>
      </g>

      <!-- Private Tier -->
      <g transform="translate(510, 20)">
        <rect width="220" height="170" rx="8" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="110" y="28" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">3. Private Tier (Vault)</text>
        <rect x="15" y="45" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="65" fill="#10b981" font-size="10" text-anchor="middle">&check; Base Class Members</text>
        <rect x="15" y="85" width="190" height="30" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444"/>
        <text x="110" y="105" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">&cross; Derived Class BLOCKED</text>
        <rect x="15" y="125" width="190" height="30" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444"/>
        <text x="110" y="145" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">&cross; External main() BLOCKED</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Quantum asks: <em>"What is the role of protected access specifier in inheritance? Compare public vs protected vs private."</em> Draw the 3-column access table above for full marks.
</div>
"""
    sections.append({
        "id": "u5-sec-15",
        "number": 15,
        "part": "PART 3 — INHERITANCE",
        "title": "15. Protected Members",
        "subtitle": "The Family Access Tier, Public vs Protected vs Private Matrix & Derived Class State Mutation",
        "content": sec15_content
    })

    # =========================================================================
    # SECTION 16: Function Overriding
    # =========================================================================
    sec16_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 3</div>
    <h3 class="card-title">16. Function Overriding: Derived Class Specialization</h3>
  </div>

  <div class="detail-block">
    <h5>16.1 Meaning of Function Overriding</h5>
    <p>
      <strong>Function Overriding</strong> occurs when a derived class defines a member function with the <strong>exact same identifier, identical parameter types, and identical return type</strong> as a function already defined in its base class.
    </p>
    <p>
      When invoked on a derived object instance, the derived class's specialized implementation takes precedence, effectively overriding the inherited generic base version.
    </p>
  </div>

  <div class="detail-block">
    <h5>16.2 Invoking the Overridden Base Method</h5>
    <p>
      If client code needs to explicitly call the base class version from within the overriding derived method, it uses the base class name with the scope resolution operator:
    </p>
    <div class="code-box"><code>BaseClass::functionName(); // Reaches through override to invoke base routine</code></div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Specialized Braking Protocol</span>
  </div>
  <p>
    Consider two vehicles:<br>
    - <strong>Base Vehicle:</strong> Implements <code>applyBrakes()</code> by applying mechanical friction pads against a rotating steel disc.<br>
    - <strong>Formula 1 Racecar (Derived):</strong> Overrides <code>applyBrakes()</code> with an ultra-high-temperature carbon-ceramic regenerative kinetic recovery system (KERS)!<br>
    Both operations are fundamentally called <code>applyBrakes()</code> with zero arguments, but the specialized sports vehicle replaces the generic mechanical pad friction with carbon-ceramic aerodynamics.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating Function Overriding & Explicit Base Method Invocation via ::</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Printer</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">void</span> renderDocument() {
        std::cout &lt;&lt; <span class="c-string">"[Base Printer] Printing standard 300 DPI monochrome text.\\n"</span>;
    }
};

<span class="c-keyword">class</span> <span class="c-type">LaserPrinter</span> : <span class="c-keyword">public</span> <span class="c-type">Printer</span> {
<span class="c-keyword">public</span>:
    <span class="c-comment">// FUNCTION OVERRIDING: Identical name, parameters, and return type</span>
    <span class="c-type">void</span> renderDocument() {
        std::cout &lt;&lt; <span class="c-string">"[LaserPrinter] Heating toner drum; printing 2400 DPI ultra-HD color!\\n"</span>;
    }

    <span class="c-type">void</span> printLegacyMonochrome() {
        <span class="c-comment">// Explicitly invokes base class implementation using scope resolution (::)</span>
        <span class="c-type">Printer</span>::renderDocument();
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Function Overriding Demonstration ===\\n"</span>;

    <span class="c-type">LaserPrinter</span> myLaser;

    <span class="c-comment">// 1. Invokes Derived class overridden implementation</span>
    myLaser.renderDocument();

    <span class="c-comment">// 2. Invokes Base class implementation explicitly</span>
    myLaser.printLegacyMonochrome();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Overridden Method Resolution in Derived Scope</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Base Class Scope -->
      <g transform="translate(40, 20)">
        <rect width="280" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="140" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Base Class: Printer</text>
        <rect x="15" y="55" width="250" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="140" y="80" fill="var(--text-secondary)" font-family="monospace" font-size="11" text-anchor="middle">void renderDocument()</text>
        <text x="140" y="125" fill="var(--text-muted)" font-size="9" text-anchor="middle">Generic Base Implementation</text>
        <text x="140" y="145" fill="#38bdf8" font-size="9" text-anchor="middle">Accessible via Printer::renderDocument()</text>
      </g>

      <!-- Inheritance Path -->
      <path d="M 320 105 L 435 105" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="375" y="95" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Overrides</text>

      <!-- Derived Class Scope -->
      <g transform="translate(440, 20)">
        <rect width="280" height="170" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="2"/>
        <text x="140" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Derived: LaserPrinter</text>
        <rect x="15" y="55" width="250" height="40" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981"/>
        <text x="140" y="80" fill="#10b981" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">void renderDocument()</text>
        <text x="140" y="125" fill="#10b981" font-size="10" text-anchor="middle">&#x2713; Takes precedence on derived calls</text>
        <text x="140" y="145" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Specialized high-resolution logic</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Comparative Analysis: Function Overloading vs. Function Overriding</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Function Overloading</th>
        <th>Function Overriding</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Scope</strong></td>
        <td>Within the <strong>same class</strong> scope.</td>
        <td>Across a <strong>Base and Derived</strong> class hierarchy.</td>
      </tr>
      <tr>
        <td><strong>Function Signatures</strong></td>
        <td><strong>Must differ</strong> in arity, types, or sequence.</td>
        <td><strong>Must be identical</strong> in name, params &amp; return.</td>
      </tr>
      <tr>
        <td><strong>Binding Time</strong></td>
        <td><strong>Compile-time</strong> (Static binding).</td>
        <td><strong>Runtime</strong> when virtual (Dynamic binding).</td>
      </tr>
      <tr>
        <td><strong>Behavioral Intent</strong></td>
        <td>Offers multiple ways to call an operation.</td>
        <td>Specializes an existing inherited operation.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When examiners ask: <em>"Differentiate between function overloading and function overriding with examples"</em>, write the 4-point matrix above. Mention that changing only the parameter list in a derived class results in <strong>Function Hiding</strong>, not overriding.
</div>
"""
    sections.append({
        "id": "u5-sec-16",
        "number": 16,
        "part": "PART 3 — INHERITANCE",
        "title": "16. Function Overriding",
        "subtitle": "Derived Class Specialization, Scope Resolution Access (::) & Overloading vs Overriding Matrix",
        "content": sec16_content
    })

    # =========================================================================
    # SECTION 17: Virtual Base Class
    # =========================================================================
    sec17_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 3</div>
    <h3 class="card-title">17. Virtual Base Class: Resolving the Diamond Problem</h3>
  </div>

  <div class="detail-block">
    <h5>17.1 The Diamond Problem in Multipath Inheritance</h5>
    <p>
      In Hybrid / Multipath inheritance, a derived class (<code>D</code>) inherits from two intermediate classes (<code>B</code> and <code>C</code>), both of which share a common ancestor base class (<code>A</code>):
    </p>
    <div class="code-box">
      <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[A]<br>
&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;\\<br>
&nbsp;&nbsp;[B]&nbsp;&nbsp;&nbsp;&nbsp;[C]<br>
&nbsp;&nbsp;&nbsp;&nbsp;\\&nbsp;&nbsp;&nbsp;/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[D]</code>
    </div>
    <p>
      <strong>The Fatal Bug:</strong> Without virtual base classes, class <code>D</code> receives <strong>two duplicate copies</strong> of class <code>A</code>'s data members (one through path <code>A &rarr; B &rarr; D</code>, and a second through <code>A &rarr; C &rarr; D</code>). This leads to two critical problems:
    </p>
    <ol>
      <li><strong>Wasted RAM:</strong> Redundant duplication of all base class variables in every object of <code>D</code>.</li>
      <li><strong>Fatal Ambiguity:</strong> Accessing a member of <code>A</code> like <code>d.val;</code> causes a compilation error: <em>"member 'val' is ambiguous"</em> because the compiler cannot deduce whether <code>B::val</code> or <code>C::val</code> was intended!</li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>17.2 The Solution: Virtual Base Class</h5>
    <p>
      By qualifying the intermediate inheritance declarations with the <code>virtual</code> keyword:
    </p>
    <div class="code-box">
      <code>class B : virtual public A { /* ... */ };<br>
class C : virtual public A { /* ... */ };</code>
    </div>
    <p>
      we instruct the C++ compiler to maintain <strong>only ONE shared instance</strong> of class <code>A</code> in the memory layout of the most-derived class <code>D</code>, completely eliminating redundancy and ambiguity!
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The University Student Identity Card</span>
  </div>
  <p>
    Consider an engineering university system:<br>
    - Base Class <code>Person</code>: Has <code>name</code> and <code>aadharCardNumber</code>.<br>
    - Intermediate 1 <code>AcademicScholar</code> inherits from <code>Person</code>.<br>
    - Intermediate 2 <code>SportsAthlete</code> inherits from <code>Person</code>.<br>
    - Student <code>AllRounder</code> inherits from both <code>AcademicScholar</code> and <code>SportsAthlete</code>.<br>
    Without a <strong>Virtual Base Class</strong>, the student would receive <em>two distinct Aadhar Card records</em> and two legal identities, throwing campus exams into chaos! With <code>virtual public Person</code>, the university recognizes that the scholar and the athlete are the exact same single human being!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Resolving Diamond Problem using Virtual Base Class (virtual public)</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-comment">// 1. COMMON ROOT BASE CLASS</span>
<span class="c-keyword">class</span> <span class="c-type">Person</span> {
<span class="c-keyword">protected</span>:
    <span class="c-type">int</span> nationalId;

<span class="c-keyword">public</span>:
    <span class="c-type">Person</span>(<span class="c-type">int</span> id = <span class="c-number">0</span>) : nationalId(id) {
        std::cout &lt;&lt; <span class="c-string">"++ [Person Constructor] National ID: "</span> &lt;&lt; nationalId &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-comment">// 2. INTERMEDIATE CLASS 1: Declares Person as VIRTUAL base</span>
<span class="c-keyword">class</span> <span class="c-type">Student</span> : <span class="c-keyword">virtual</span> <span class="c-keyword">public</span> <span class="c-type">Person</span> {
<span class="c-keyword">protected</span>:
    <span class="c-type">double</span> gpa;

<span class="c-keyword">public</span>:
    <span class="c-type">Student</span>(<span class="c-type">int</span> id, <span class="c-type">double</span> g) : <span class="c-type">Person</span>(id), gpa(g) {}
};

<span class="c-comment">// 3. INTERMEDIATE CLASS 2: Declares Person as VIRTUAL base</span>
<span class="c-keyword">class</span> <span class="c-type">Athlete</span> : <span class="c-keyword">virtual</span> <span class="c-keyword">public</span> <span class="c-type">Person</span> {
<span class="c-keyword">protected</span>:
    <span class="c-type">int</span> sportsRank;

<span class="c-keyword">public</span>:
    <span class="c-type">Athlete</span>(<span class="c-type">int</span> id, <span class="c-type">int</span> rank) : <span class="c-type">Person</span>(id), sportsRank(rank) {}
};

<span class="c-comment">// 4. MOST DERIVED CLASS: Inherits from Student & Athlete</span>
<span class="c-keyword">class</span> <span class="c-type">SportsScholar</span> : <span class="c-keyword">public</span> <span class="c-type">Student</span>, <span class="c-keyword">public</span> <span class="c-type">Athlete</span> {
<span class="c-keyword">public</span>:
    <span class="c-comment">// In virtual inheritance, MOST DERIVED class directly initializes the virtual base!</span>
    <span class="c-type">SportsScholar</span>(<span class="c-type">int</span> id, <span class="c-type">double</span> g, <span class="c-type">int</span> rank)
        : <span class="c-type">Person</span>(id), <span class="c-type">Student</span>(id, g), <span class="c-type">Athlete</span>(id, rank) {}

    <span class="c-type">void</span> displayRecord() <span class="c-keyword">const</span> {
        <span class="c-comment">// ZERO AMBIGUITY: Only one nationalId exists!</span>
        std::cout &lt;&lt; <span class="c-string">"SportsScholar [ID: "</span> &lt;&lt; nationalId 
                  &lt;&lt; <span class="c-string">" | GPA: "</span> &lt;&lt; gpa 
                  &lt;&lt; <span class="c-string">" | Rank: #"</span> &lt;&lt; sportsRank &lt;&lt; <span class="c-string">"]\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Testing Virtual Base Class (Diamond Resolution) ===\\n"</span>;

    <span class="c-type">SportsScholar</span> scholar(<span class="c-number">908201</span>, <span class="c-number">9.65</span>, <span class="c-number">1</span>);
    scholar.displayRecord();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Diamond Problem Ambiguity vs Single Shared Virtual Instance</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- Diamond Topology in Center -->
      <g transform="translate(190, 15)">
        <!-- Root Class A -->
        <rect x="130" y="0" width="120" height="35" rx="4" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="190" y="22" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Person (Root A)</text>

        <!-- Left Branch B -->
        <rect x="30" y="70" width="120" height="35" rx="4" fill="var(--bg-card)" stroke="#f59e0b"/>
        <text x="90" y="92" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Student (B)</text>

        <!-- Right Branch C -->
        <rect x="230" y="70" width="120" height="35" rx="4" fill="var(--bg-card)" stroke="#f59e0b"/>
        <text x="290" y="92" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Athlete (C)</text>

        <!-- Bottom Derived D -->
        <rect x="110" y="140" width="160" height="40" rx="4" fill="var(--bg-card)" stroke="#10b981" stroke-width="2"/>
        <text x="190" y="165" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">SportsScholar (D)</text>

        <!-- Connecting Lines -->
        <path d="M 160 35 L 100 70" stroke="#38bdf8" stroke-width="1.5"/>
        <path d="M 220 35 L 280 70" stroke="#38bdf8" stroke-width="1.5"/>
        <path d="M 90 105 L 150 140" stroke="#10b981" stroke-width="1.5"/>
        <path d="M 290 105 L 230 140" stroke="#10b981" stroke-width="1.5"/>

        <text x="190" y="105" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">virtual public</text>
      </g>

      <!-- Explanation Callout -->
      <g transform="translate(580, 45)">
        <rect width="155" height="120" rx="6" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981"/>
        <text x="77" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">&#x2713; Diamond Solved</text>
        <text x="77" y="50" fill="var(--text-primary)" font-size="9" text-anchor="middle">Single Person instance;</text>
        <text x="77" y="68" fill="var(--text-primary)" font-size="9" text-anchor="middle">Zero ambiguous paths;</text>
        <text x="77" y="86" fill="var(--text-primary)" font-size="9" text-anchor="middle">Reduced memory size;</text>
        <text x="77" y="104" fill="#38bdf8" font-size="9" text-anchor="middle">Clean unified state</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"What is a virtual base class? Explain the Diamond Problem with an example and diagram"</em> is one of the most famous 10-mark questions in the entire AKTU curriculum. Draw the diamond diagram above, provide the complete code with <code>virtual public Person</code>, and mention that only one shared copy of <code>Person</code> is instantiated.
</div>
"""
    sections.append({
        "id": "u5-sec-17",
        "number": 17,
        "part": "PART 3 — INHERITANCE",
        "title": "17. Virtual Base Class",
        "subtitle": "The Diamond Problem, Multipath Inheritance Ambiguity & The virtual public Solution",
        "content": sec17_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit5_part3_sections()
    print(f"generate_unit5_part3.py compiled {len(secs)} sections successfully.")
