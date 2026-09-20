# -*- coding: utf-8 -*-
"""
generate_unit5_part1.py: Generates Sections 1 to 5 for Unit 5 (Objects and Classes in C++)
Topics:
  1. Basics of Object and Class in C++ (Runtime Entity, Blueprint, Memory Allocation)
  2. Data Members and Member Functions (Inside vs Outside Class via ::)
  3. Private and Public Members (Access Control, Encapsulation, Interface vs Implementation)
  4. Static Data Members (Shared Class State, Memory Layout, Instance Counting)
  5. Static Member Functions (Class-level Invocations without 'this', Restrictions)
"""

def get_unit5_part1_sections():
    sections = []

    # =========================================================================
    # SECTION 1: Basics of Object and Class in C++
    # =========================================================================
    sec1_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 1</div>
    <h3 class="card-title">1. Basics of Object and Class in C++</h3>
  </div>

  <div class="detail-block">
    <h5>1.1 What is an Object?</h5>
    <p>
      An <strong>Object</strong> is a fundamental runtime entity in an object-oriented system that encapsulates both <strong>state (data members)</strong> and <strong>behavior (member functions)</strong> into a single cohesive, addressable package.
    </p>
    <ul>
      <li><strong>Runtime Existence:</strong> While a class exists only at compile time as a blueprint, an object occupies physical RAM at runtime.</li>
      <li><strong>Instantiation:</strong> Creating an object is termed <em>instantiation</em>. When an object is instantiated, the system allocates contiguous physical bytes in memory equal to the cumulative size of its non-static data members (subject to CPU architecture alignment padding).</li>
      <li><strong>Real-World Representation:</strong> Every tangible or conceptual entity in the problem domain (e.g. an ATM Transaction, an Automobile, a Bank Account, or a Student) is modeled directly as a software object.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>1.2 What is a Class?</h5>
    <p>
      A <strong>Class</strong> is a user-defined data type (UDT) that serves as the architectural template or prototype from which individual objects are instantiated.
    </p>
    <ul>
      <li><strong>Data Abstraction &amp; Encapsulation:</strong> A class binds data members and member functions together, hiding internal representation behind public interfaces.</li>
      <li><strong>User-Defined Type:</strong> Once defined, a class behaves identically to fundamental primitive types like <code>int</code> or <code>float</code>; you can create objects, pointers to objects, arrays of objects, and pass them to functions.</li>
      <li><strong>Class Body Anatomy:</strong> Enclosed in curly braces and terminated by a mandatory semicolon (<code>};</code>). Contains data member declarations and member function prototypes or inline bodies.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Architectural Blueprint vs. The Physical Villa</span>
  </div>
  <p>
    An architectural engineer draws a detailed <strong>Blueprint</strong> on paper for a modern smart villa. The blueprint specifies the number of bedrooms, electrical wiring, plumbing pipe layouts, and the dimensions of every door. That blueprint is the <strong>Class</strong>: it occupies virtually no physical terrain, you cannot sleep inside it, and you cannot walk through its doors.<br><br>
    When civil contractors build the actual concrete villa in Sector 62, laying bricks and mortar on physical land with a distinct GPS coordinate, that villa is the <strong>Object</strong>. You can instantiate five villas (<code>Villa v1, v2, v3, v4, v5;</code>) from the exact same single blueprint. Each villa has its own distinct physical location and resident, yet all share the identical architectural structure.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Declaration of Class, Instantiation of Objects & Memory Inspection</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// 1. CLASS DECLARATION: Blueprint defining user-defined type</span>
<span class="c-keyword">class</span> <span class="c-type">Student</span> {
<span class="c-keyword">public</span>:
    <span class="c-comment">// Data Members (State attributes)</span>
    <span class="c-type">int</span> rollNumber;
    <span class="c-type">std::string</span> studentName;
    <span class="c-type">double</span> gpaScore;

    <span class="c-comment">// Member Function (Behavior / Action)</span>
    <span class="c-type">void</span> printAcademicRecord() {
        std::cout &lt;&lt; <span class="c-string">"Student [Roll: "</span> &lt;&lt; rollNumber 
                  &lt;&lt; <span class="c-string">" | Name: "</span> &lt;&lt; studentName 
                  &lt;&lt; <span class="c-string">" | GPA: "</span> &lt;&lt; gpaScore &lt;&lt; <span class="c-string">"]\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Class &amp; Object Demonstration ===\\n"</span>;

    <span class="c-comment">// 2. INSTANTIATION: Objects created at runtime occupying physical RAM</span>
    <span class="c-type">Student</span> s1; <span class="c-comment">// Object 1</span>
    s1.rollNumber = <span class="c-number">101</span>;
    s1.studentName = <span class="c-string">"Aarav Sharma"</span>;
    s1.gpaScore = <span class="c-number">9.45</span>;

    <span class="c-type">Student</span> s2; <span class="c-comment">// Object 2</span>
    s2.rollNumber = <span class="c-number">102</span>;
    s2.studentName = <span class="c-string">"Ananya Verma"</span>;
    s2.gpaScore = <span class="c-number">9.82</span>;

    <span class="c-comment">// 3. INVOKING BEHAVIOR</span>
    s1.printAcademicRecord();
    s2.printAcademicRecord();

    <span class="c-comment">// 4. MEMORY VERIFICATION</span>
    std::cout &lt;&lt; <span class="c-string">"\\n[Memory Analysis]\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Size of Class Student blueprint: "</span> &lt;&lt; <span class="c-keyword">sizeof</span>(<span class="c-type">Student</span>) &lt;&lt; <span class="c-string">" bytes\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Physical RAM Address of s1:       "</span> &lt;&lt; &amp;s1 &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Physical RAM Address of s2:       "</span> &lt;&lt; &amp;s2 &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Class Blueprint to Runtime Physical RAM Instantiation</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- Blueprint Box (Compile Time) -->
      <g transform="translate(30, 20)">
        <rect width="220" height="180" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="110" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Class Blueprint (Compile-Time)</text>
        <rect x="15" y="45" width="190" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="65" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">class Student {</text>
        <text x="30" y="95" fill="var(--text-secondary)" font-family="monospace" font-size="10">int rollNumber; (4B)</text>
        <text x="30" y="115" fill="var(--text-secondary)" font-family="monospace" font-size="10">string studentName; (32B)</text>
        <text x="30" y="135" fill="var(--text-secondary)" font-family="monospace" font-size="10">double gpaScore; (8B)</text>
        <text x="30" y="155" fill="#10b981" font-family="monospace" font-size="10">void printRecord();</text>
        <text x="110" y="175" fill="var(--text-muted)" font-size="9" text-anchor="middle">Zero RAM allocated!</text>
      </g>

      <!-- Instantiation Arrows -->
      <path d="M 260 80 L 330 60" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <path d="M 260 140 L 330 160" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="295" y="105" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">instantiate</text>

      <!-- Object s1 (Runtime RAM) -->
      <g transform="translate(340, 20)">
        <rect width="185" height="85" rx="6" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="92" y="22" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Object s1 [0x7FFE40]</text>
        <text x="15" y="42" fill="var(--text-primary)" font-family="monospace" font-size="10">roll: 101</text>
        <text x="15" y="58" fill="var(--text-primary)" font-family="monospace" font-size="10">name: "Aarav Sharma"</text>
        <text x="15" y="74" fill="var(--text-primary)" font-family="monospace" font-size="10">gpa: 9.45</text>
      </g>

      <!-- Object s2 (Runtime RAM) -->
      <g transform="translate(340, 115)">
        <rect width="185" height="85" rx="6" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="92" y="22" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Object s2 [0x7FFE80]</text>
        <text x="15" y="42" fill="var(--text-primary)" font-family="monospace" font-size="10">roll: 102</text>
        <text x="15" y="58" fill="var(--text-primary)" font-family="monospace" font-size="10">name: "Ananya Verma"</text>
        <text x="15" y="74" fill="var(--text-primary)" font-family="monospace" font-size="10">gpa: 9.82</text>
      </g>

      <!-- Shared Code Segment -->
      <g transform="translate(545, 45)">
        <rect width="190" height="130" rx="8" fill="rgba(99, 102, 241, 0.12)" stroke="#6366f1" stroke-width="1.5"/>
        <text x="95" y="25" fill="#a5b4fc" font-size="11" font-weight="bold" text-anchor="middle">Code Segment (.text)</text>
        <rect x="15" y="40" width="160" height="40" rx="4" fill="var(--bg-elevated)"/>
        <text x="95" y="62" fill="var(--accent-blue)" font-family="monospace" font-size="10" text-anchor="middle">Student::printRecord()</text>
        <text x="95" y="100" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Single shared executable binary;</text>
        <text x="95" y="115" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Invoked via implicit this ptr</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Head-to-Head Comparison: Class vs. Object</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Architectural Criterion</th>
        <th>Class</th>
        <th>Object</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Conceptual Nature</strong></td>
        <td>Abstract architectural blueprint / user-defined data type.</td>
        <td>Concrete real-world instance of a class.</td>
      </tr>
      <tr>
        <td><strong>Memory Allocation</strong></td>
        <td><strong>No physical RAM</strong> allocated when class is declared.</td>
        <td><strong>Allocates physical RAM</strong> upon instantiation.</td>
      </tr>
      <tr>
        <td><strong>Existence Timeline</strong></td>
        <td>Exists primarily at <strong>compile time</strong> as a type definition.</td>
        <td>Exists dynamically at <strong>runtime</strong> as an active entity.</td>
      </tr>
      <tr>
        <td><strong>Multiplicity</strong></td>
        <td>Declared once per definition scope.</td>
        <td>Can instantiate multiple independent objects from one class.</td>
      </tr>
      <tr>
        <td><strong>Values &amp; State</strong></td>
        <td>Defines properties and operations; holds no actual values.</td>
        <td>Holds distinct, mutable state values in memory.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Quantum asks: <em>"Define class and object. Differentiate between them with a suitable C++ example."</em> Write the 5-point comparison table above, include the <code>Student</code> class code, and state clearly that member functions reside in the code segment once, while data members replicate per object instance in the stack/heap.
</div>
"""
    sections.append({
        "id": "u5-sec-1",
        "number": 1,
        "part": "PART 1 — OBJECTS AND CLASSES",
        "title": "1. Basics of Object and Class in C++",
        "subtitle": "Runtime Entity, User-Defined Blueprint, Memory Allocation & The Class vs Object Divide",
        "content": sec1_content
    })

    # =========================================================================
    # SECTION 2: Data Members and Member Functions
    # =========================================================================
    sec2_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 1</div>
    <h3 class="card-title">2. Data Members and Member Functions</h3>
  </div>

  <div class="detail-block">
    <h5>2.1 What are Data Members?</h5>
    <p>
      <strong>Data Members</strong> are variables declared inside a class that represent the state, attributes, or properties of an object. Each object instantiated from the class receives its own independent copy of every non-static data member.
    </p>
  </div>

  <div class="detail-block">
    <h5>2.2 What are Member Functions?</h5>
    <p>
      <strong>Member Functions</strong> are functions declared inside a class that operate directly upon its data members. Member functions embody the object's behavior and define the legal operations permitted on its state.
    </p>
  </div>

  <div class="detail-block">
    <h5>2.3 Defining Member Functions: Two Approaches</h5>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6>Inside Class Definition (Inline by Default)</h6>
          <p>
            When a member function is defined directly inside the class body, the compiler treats it as an implicit request for <strong>inlining</strong>. Ideal for small, lightweight accessor or mutator routines (1–3 lines).
          </p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6>Outside Class Definition via Scope Resolution (<code>::</code>)</h6>
          <p>
            The function prototype is declared inside the class, and its full implementation is written outside using the binary <strong>Scope Resolution Operator (<code>::</code>)</strong>:
          </p>
          <div class="code-box"><code>returnType ClassName::functionName(parameterList) { /* body */ }</code></div>
          <p>
            Standard practice in production C++ to separate interface (header <code>.h</code>) from implementation (source <code>.cpp</code>).
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Digital Microwave Oven</span>
  </div>
  <p>
    Consider a modern Digital Microwave Oven:<br>
    - <strong>Data Members:</strong> Internal state variables: <code>temperatureCelsius</code>, <code>timerSecondsRemaining</code>, <code>powerLevelWatts</code>, and <code>isDoorClosed</code>.<br>
    - <strong>Member Functions:</strong> Operations you trigger through its keypad: <code>startHeating()</code>, <code>cancel()</code>, and <code>setTimer(30)</code>.<br>
    You cannot reach inside and manually spin the magnetron frequency dials; you press the keypad buttons (member functions) which safely manipulate the internal sensors (data members) under strict rules!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Defining Member Functions Inside vs. Outside Class via Scope Resolution</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;iomanip&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">BankAccount</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">long</span> accountNumber;
    <span class="c-type">double</span> balanceAmount;

<span class="c-keyword">public</span>:
    <span class="c-comment">// 1. DEFINED INSIDE CLASS: Implicitly inlined by compiler</span>
    <span class="c-type">double</span> getBalance() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> balanceAmount;
    }

    <span class="c-comment">// Prototypes for functions defined outside</span>
    <span class="c-type">void</span> initializeAccount(<span class="c-type">long</span> accNo, <span class="c-type">double</span> initialDeposit);
    <span class="c-type">void</span> depositMoney(<span class="c-type">double</span> amount);
    <span class="c-type">bool</span> withdrawMoney(<span class="c-type">double</span> amount);
    <span class="c-type">void</span> displayAccountSummary() <span class="c-keyword">const</span>;
};

<span class="c-comment">// 2. DEFINED OUTSIDE CLASS USING SCOPE RESOLUTION OPERATOR (::)</span>
<span class="c-type">void</span> <span class="c-type">BankAccount</span>::initializeAccount(<span class="c-type">long</span> accNo, <span class="c-type">double</span> initialDeposit) {
    accountNumber = accNo;
    balanceAmount = (initialDeposit &gt;= <span class="c-number">0</span>) ? initialDeposit : <span class="c-number">0.0</span>;
}

<span class="c-type">void</span> <span class="c-type">BankAccount</span>::depositMoney(<span class="c-type">double</span> amount) {
    <span class="c-keyword">if</span> (amount &gt; <span class="c-number">0</span>) {
        balanceAmount += amount;
        std::cout &lt;&lt; <span class="c-string">"Deposited Rs. "</span> &lt;&lt; amount &lt;&lt; <span class="c-string">" successfully.\\n"</span>;
    }
}

<span class="c-type">bool</span> <span class="c-type">BankAccount</span>::withdrawMoney(<span class="c-type">double</span> amount) {
    <span class="c-keyword">if</span> (amount &gt; <span class="c-number">0</span> &amp;&amp; balanceAmount &gt;= amount) {
        balanceAmount -= amount;
        std::cout &lt;&lt; <span class="c-string">"Withdrew Rs. "</span> &lt;&lt; amount &lt;&lt; <span class="c-string">" successfully.\\n"</span>;
        <span class="c-keyword">return</span> <span class="c-keyword">true</span>;
    }
    std::cout &lt;&lt; <span class="c-string">"Withdrawal failed: Insufficient funds!\\n"</span>;
    <span class="c-keyword">return</span> <span class="c-keyword">false</span>;
}

<span class="c-type">void</span> <span class="c-type">BankAccount</span>::displayAccountSummary() <span class="c-keyword">const</span> {
    std::cout &lt;&lt; <span class="c-string">"Account ["</span> &lt;&lt; accountNumber 
              &lt;&lt; <span class="c-string">"] | Current Balance: Rs. "</span> &lt;&lt; balanceAmount &lt;&lt; <span class="c-string">"\\n"</span>;
}

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; std::fixed &lt;&lt; std::setprecision(<span class="c-number">2</span>);
    std::cout &lt;&lt; <span class="c-string">"=== Bank Account Operations ===\\n"</span>;

    <span class="c-type">BankAccount</span> myAcc;
    myAcc.initializeAccount(<span class="c-number">9876543210L</span>, <span class="c-number">25000.0</span>);
    myAcc.displayAccountSummary();

    myAcc.depositMoney(<span class="c-number">12500.0</span>);
    myAcc.withdrawMoney(<span class="c-number">8000.0</span>);
    myAcc.displayAccountSummary();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Inside Class vs Outside Class Member Function Resolution</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Class Boundary Container -->
      <g transform="translate(30, 20)">
        <rect width="320" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="160" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Class BankAccount Declaration</text>
        
        <rect x="20" y="45" width="280" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="67" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">double getBalance() { return bal; } (INLINE)</text>

        <rect x="20" y="95" width="280" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="117" fill="var(--accent-blue)" font-family="monospace" font-size="10" text-anchor="middle">void depositMoney(double amount); (PROTOTYPE)</text>
        
        <text x="160" y="155" fill="var(--text-muted)" font-size="9" text-anchor="middle">Informs compiler of member function signatures</text>
      </g>

      <!-- Scope Resolution Bridge -->
      <path d="M 350 112 L 440 112" stroke="#6366f1" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="395" y="105" fill="#a5b4fc" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">::</text>

      <!-- External Definition Container -->
      <g transform="translate(440, 20)">
        <rect width="290" height="170" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="145" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Outside Class Definition</text>

        <rect x="15" y="45" width="260" height="50" rx="4" fill="var(--bg-elevated)"/>
        <text x="145" y="65" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">void BankAccount::depositMoney(double a) {</text>
        <text x="145" y="82" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">    balanceAmount += a;</text>
        <text x="145" y="99" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">}</text>

        <text x="145" y="130" fill="var(--text-secondary)" font-size="9" text-anchor="middle">Full body lives in compilation unit</text>
        <text x="145" y="150" fill="#38bdf8" font-size="9" text-anchor="middle">Separates API interface from implementation logic</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Quantum asks: <em>"How are member functions defined inside and outside the class? Explain with syntax and code."</em> Always demonstrate both styles using the <code>BankAccount</code> example and mention that defining outside with <code>::</code> promotes header/source code separation.
</div>
"""
    sections.append({
        "id": "u5-sec-2",
        "number": 2,
        "part": "PART 1 — OBJECTS AND CLASSES",
        "title": "2. Data Members and Member Functions",
        "subtitle": "State vs Behavior, Inline Definitions Inside Class & Out-of-Line Scope Resolution (::)",
        "content": sec2_content
    })

    # =========================================================================
    # SECTION 3: Private and Public Members
    # =========================================================================
    sec3_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 1</div>
    <h3 class="card-title">3. Private and Public Members: Access Control &amp; Encapsulation</h3>
  </div>

  <div class="detail-block">
    <h5>3.1 Principles of Access Control</h5>
    <p>
      Access specifiers in C++ define the visibility and accessibility of class members from various program scopes. They are the primary linguistic mechanism for implementing <strong>Data Hiding</strong> and <strong>Encapsulation</strong>.
    </p>
    <ul>
      <li><strong>Default Access in C++ Class:</strong> By default, all members declared inside a <code>class</code> are strictly <code>private</code> (unlike a <code>struct</code> where default access is <code>public</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3.2 Private Members</h5>
    <p>
      Members declared under the <code>private:</code> specifier can only be accessed by member functions and friend functions of the same class. External functions and client code (such as <code>main()</code>) cannot read or modify private members directly (e.g. <code>obj.privateVar; // COMPILE ERROR</code>).
    </p>
    <p>
      <strong>Purpose:</strong> Protects internal state integrity against corrupted, out-of-range, or unauthorized modifications.
    </p>
  </div>

  <div class="detail-block">
    <h5>3.3 Public Members</h5>
    <p>
      Members declared under the <code>public:</code> specifier are accessible from anywhere in the program wherever the object instance is in scope.
    </p>
    <p>
      <strong>Purpose:</strong> Formulates the external interface (contract) through which client code interacts with the class.
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Bank Teller Counter vs. The Vault</span>
  </div>
  <p>
    When you walk into a physical retail bank:<br>
    - <strong>Public Interface:</strong> The teller counter window. Any citizen can walk up to the teller window, present a withdrawal slip, or ask for an account statement. The teller window is <code>public:</code>.<br>
    - <strong>Private Data:</strong> The subterranean high-security titanium bank vault storing currency stacks. Customers are legally forbidden from walking directly into the vault to grab cash. The vault is <code>private:</code>.<br>
    The public teller function validates your identity, checks your balance, and securely transfers money on your behalf without ever exposing direct access to the vault!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Encapsulation Barrier: Private Data Protected by Public Getters & Setters</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Employee</span> {
<span class="c-keyword">private</span>:
    <span class="c-comment">// PRIVATE MEMBERS: Shielded from external tampering</span>
    <span class="c-type">int</span> employeeId;
    <span class="c-type">double</span> monthlySalary;

<span class="c-keyword">public</span>:
    <span class="c-comment">// PUBLIC INTERFACE: Controlled accessor and mutator methods</span>
    <span class="c-type">void</span> setEmployeeDetails(<span class="c-type">int</span> id, <span class="c-type">double</span> salary) {
        employeeId = id;
        <span class="c-comment">// Business logic validation: salary cannot be negative</span>
        <span class="c-keyword">if</span> (salary &gt;= <span class="c-number">0.0</span>) {
            monthlySalary = salary;
        } <span class="c-keyword">else</span> {
            monthlySalary = <span class="c-number">0.0</span>;
            std::cout &lt;&lt; <span class="c-string">"Warning: Negative salary rejected! Set to 0.0\\n"</span>;
        }
    }

    <span class="c-type">double</span> getSalary() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> monthlySalary;
    }

    <span class="c-type">void</span> displayProfile() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Employee [ID: "</span> &lt;&lt; employeeId 
                  &lt;&lt; <span class="c-string">" | Monthly Salary: Rs. "</span> &lt;&lt; monthlySalary &lt;&lt; <span class="c-string">"]\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">Employee</span> emp;

    <span class="c-comment">// 1. LEGAL: Calling public member functions</span>
    emp.setEmployeeDetails(<span class="c-number">501</span>, <span class="c-number">75000.0</span>);
    emp.displayProfile();

    <span class="c-comment">// 2. ILLEGAL COMPILATION ERRORS: Direct private access rejected</span>
    <span class="c-comment">// emp.monthlySalary = -50000.0; // COMPILE ERROR: 'monthlySalary' is private!</span>
    <span class="c-comment">// std::cout &lt;&lt; emp.employeeId;  // COMPILE ERROR: 'employeeId' is private!</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Encapsulation Membrane (Private Core vs Public Shell)</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- External Client Scope -->
      <g transform="translate(30, 40)">
        <rect width="180" height="130" rx="8" fill="var(--bg-elevated)" stroke="var(--border-default)" stroke-width="1.5"/>
        <text x="90" y="30" fill="var(--accent-blue)" font-size="12" font-weight="bold" text-anchor="middle">Client Code: main()</text>
        <rect x="15" y="45" width="150" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="90" y="65" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">emp.setDetails()</text>
        <rect x="15" y="85" width="150" height="30" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444"/>
        <text x="90" y="105" fill="#ef4444" font-family="monospace" font-size="10" text-anchor="middle">emp.salary = -100</text>
      </g>

      <!-- Legal Call Arrow -->
      <path d="M 210 85 L 290 85" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="250" y="75" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">ALLOWED</text>

      <!-- Blocked Call Arrow -->
      <path d="M 210 125 L 285 125" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 2"/>
      <text x="250" y="142" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">BLOCKED ✗</text>

      <!-- Encapsulated Object Structure -->
      <g transform="translate(290, 15)">
        <!-- Outer Public Shell -->
        <rect width="440" height="180" rx="12" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="2"/>
        <text x="220" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">PUBLIC INTERFACE (External Shell)</text>
        <text x="35" y="50" fill="#10b981" font-family="monospace" font-size="11">setEmployeeDetails() &bull; getSalary() &bull; displayProfile()</text>

        <!-- Inner Private Vault -->
        <rect x="30" y="70" width="380" height="90" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="2"/>
        <text x="220" y="95" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">PRIVATE INNER VAULT (Hidden State)</text>
        <rect x="50" y="110" width="160" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="130" y="132" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">int employeeId</text>
        <rect x="230" y="110" width="160" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="310" y="132" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">double monthlySalary</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Comparative Analysis: Private vs. Public Members</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Private Members (<code>private:</code>)</th>
        <th>Public Members (<code>public:</code>)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Accessibility Scope</strong></td>
        <td>Accessible <strong>only within the class</strong> (and friend functions).</td>
        <td>Accessible from <strong>anywhere</strong> in the program.</td>
      </tr>
      <tr>
        <td><strong>Primary Purpose</strong></td>
        <td>Protects internal state data (Data Hiding).</td>
        <td>Provides the operational interface to client code.</td>
      </tr>
      <tr>
        <td><strong>Access via Dot Operator</strong></td>
        <td><strong>Disallowed:</strong> <code>obj.privMember;</code> fails compilation.</td>
        <td><strong>Allowed:</strong> <code>obj.pubFunction();</code> executes freely.</td>
      </tr>
      <tr>
        <td><strong>Default Access in Class</strong></td>
        <td><strong>Yes:</strong> Default access specifier in a C++ <code>class</code>.</td>
        <td><strong>No:</strong> Must be explicitly declared under <code>public:</code>.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When examiners ask: <em>"What is the difference between private and public access specifiers in C++?"</em>, provide the 4-point comparison table above and explain how private variables prevent invalid state (e.g. negative balance or invalid age) using getter/setter validation code.
</div>
"""
    sections.append({
        "id": "u5-sec-3",
        "number": 3,
        "part": "PART 1 — OBJECTS AND CLASSES",
        "title": "3. Private and Public Members",
        "subtitle": "Access Control, Data Hiding, Public Interface vs Private Vault & The Encapsulation Membrane",
        "content": sec3_content
    })

    # =========================================================================
    # SECTION 4: Static Data Members
    # =========================================================================
    sec4_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 1</div>
    <h3 class="card-title">4. Static Data Members: Shared Class-Level State</h3>
  </div>

  <div class="detail-block">
    <h5>4.1 Meaning of Static Data Members</h5>
    <p>
      In standard C++, each object instantiated from a class receives its own separate, distinct copy of all data members. However, when a data member is qualified with the <code>static</code> keyword, <strong>only one single copy of that member is created for the entire class</strong>, and that single copy is shared collaboratively across all instantiated objects.
    </p>
  </div>

  <div class="detail-block">
    <h5>4.2 Characteristics &amp; Lifetime Rules</h5>
    <ul>
      <li><strong>Class-Level Scope:</strong> It belongs to the class as a whole rather than any individual object instance.</li>
      <li><strong>Lifetime:</strong> Initialized once when the program starts (before <code>main()</code> executes) and persists in the static data segment throughout the entire program lifetime.</li>
      <li><strong>Default Initialization:</strong> Automatically zero-initialized by the runtime system if not explicitly assigned.</li>
      <li><strong>Declaration vs Definition:</strong> Must be <em>declared</em> inside the class declaration, but <strong>must be defined and allocated outside the class at file scope</strong> (in the <code>.cpp</code> file) using the scope resolution operator:
        <div class="code-box"><code>int ClassName::staticVarName = initialValue; // Mandatory definition!</code></div>
      </li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The University Central Student Admission Registry</span>
  </div>
  <p>
    Imagine an engineering university campus:<br>
    - <strong>Normal Data Members:</strong> Each student carries their own personal Identity Card, backpack, and laptop. If Student A changes their laptop wallpaper, it has zero impact on Student B's laptop. These are <em>instance members</em>.<br>
    - <strong>Static Data Member:</strong> The <strong>Total Admitted Students Counter</strong> displayed on the central digital notice board in the Registrar's Office. Every time a new student registers at the campus gates, the central counter increments (<code>totalAdmittedStudents++</code>). There is only one shared counter for all 5,000 students on campus!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Static Data Member Declaration, External Definition & Live Instance Counting</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Car</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> chassisNumber;
    <span class="c-type">std::string</span> modelName;

    <span class="c-comment">// 1. DECLARATION OF STATIC DATA MEMBER (Shared across all Car instances)</span>
    <span class="c-keyword">static</span> <span class="c-type">int</span> totalCarsManufactured;

<span class="c-keyword">public</span>:
    <span class="c-type">Car</span>(<span class="c-type">std::string</span> chassis, <span class="c-type">std::string</span> model) 
        : chassisNumber(chassis), modelName(model) {
        <span class="c-comment">// Increments the single shared class-level counter upon creation</span>
        totalCarsManufactured++;
    }

    ~<span class="c-type">Car</span>() {
        <span class="c-comment">// Decrements when a car object is dismantled/destroyed</span>
        totalCarsManufactured--;
    }

    <span class="c-type">void</span> printCarDetails() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Car [Chassis: "</span> &lt;&lt; chassisNumber 
                  &lt;&lt; <span class="c-string">" | Model: "</span> &lt;&lt; modelName 
                  &lt;&lt; <span class="c-string">" | Total Fleet Active: "</span> &lt;&lt; totalCarsManufactured &lt;&lt; <span class="c-string">"]\\n"</span>;
    }
};

<span class="c-comment">// 2. MANDATORY OUT-OF-CLASS DEFINITION: Allocates physical memory in static storage</span>
<span class="c-type">int</span> <span class="c-type">Car</span>::totalCarsManufactured = <span class="c-number">0</span>;

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Static Data Member Demonstration ===\\n"</span>;

    <span class="c-type">Car</span> c1(<span class="c-string">"VIN-9081"</span>, <span class="c-string">"Sedan Prime"</span>);
    c1.printCarDetails();

    <span class="c-type">Car</span> c2(<span class="c-string">"VIN-9082"</span>, <span class="c-string">"EV SUV Extreme"</span>);
    c2.printCarDetails();

    {
        <span class="c-comment">// Temporary inner scope car</span>
        <span class="c-type">Car</span> c3(<span class="c-string">"VIN-9083"</span>, <span class="c-string">"Track Roadster"</span>);
        c3.printCarDetails();
        std::cout &lt;&lt; <span class="c-string">"Exiting local block; c3 will be destructed...\\n"</span>;
    }

    std::cout &lt;&lt; <span class="c-string">"After c3 destruction:\\n"</span>;
    c1.printCarDetails();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Instance Variables vs Shared Static Data Member in Memory</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Object 1 Box -->
      <g transform="translate(30, 20)">
        <rect width="180" height="170" rx="8" fill="var(--bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="90" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Object c1 (Stack)</text>
        <rect x="15" y="45" width="150" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="90" y="65" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">chassis: "VIN-9081"</text>
        <rect x="15" y="85" width="150" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="90" y="105" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">model: "Sedan Prime"</text>
        <text x="90" y="145" fill="var(--text-muted)" font-size="9" text-anchor="middle">Independent copy of state</text>
      </g>

      <!-- Object 2 Box -->
      <g transform="translate(250, 20)">
        <rect width="180" height="170" rx="8" fill="var(--bg-card)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="90" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Object c2 (Stack)</text>
        <rect x="15" y="45" width="150" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="90" y="65" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">chassis: "VIN-9082"</text>
        <rect x="15" y="85" width="150" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="90" y="105" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">model: "EV SUV"</text>
        <text x="90" y="145" fill="var(--text-muted)" font-size="9" text-anchor="middle">Independent copy of state</text>
      </g>

      <!-- Shared Static Data Member in .data segment -->
      <g transform="translate(480, 20)">
        <rect width="250" height="170" rx="8" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981" stroke-width="2"/>
        <text x="125" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Static Data Segment (.data)</text>
        
        <rect x="25" y="55" width="200" height="50" rx="6" fill="var(--bg-elevated)" stroke="#10b981"/>
        <text x="125" y="77" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">Car::totalCarsManufactured</text>
        <text x="125" y="95" fill="#10b981" font-family="monospace" font-size="13" font-weight="bold" text-anchor="middle">Value = 2</text>

        <text x="125" y="135" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Single shared memory location</text>
        <text x="125" y="152" fill="var(--accent-blue)" font-size="9" text-anchor="middle">Lives for entire program duration</text>
      </g>

      <!-- Connection Arrows pointing to shared static block -->
      <path d="M 210 100 L 480 80" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
      <path d="M 430 100 L 480 90" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
    </svg>
  </div>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"Explain static data member with an example"</em>, emphasize that it MUST be defined outside the class using <code>Type Class::var = val;</code>. Forgetting this definition is the #1 mistake students make in programming exams!
</div>
"""
    sections.append({
        "id": "u5-sec-4",
        "number": 4,
        "part": "PART 1 — OBJECTS AND CLASSES",
        "title": "4. Static Data Members",
        "subtitle": "Shared Class-Level State, Memory Architecture, Out-of-Class Definition & Instance Counting",
        "content": sec4_content
    })

    # =========================================================================
    # SECTION 5: Static Member Functions
    # =========================================================================
    sec5_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 1</div>
    <h3 class="card-title">5. Static Member Functions: Class-Level Routines</h3>
  </div>

  <div class="detail-block">
    <h5>5.1 Meaning of Static Member Functions</h5>
    <p>
      A <strong>Static Member Function</strong> is a member function qualified with the <code>static</code> keyword that operates at the class level rather than on a specific object instance. It can be invoked directly using the class name without creating any object.
    </p>
  </div>

  <div class="detail-block">
    <h5>5.2 Three Fundamental Rules of Static Member Functions</h5>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6>No Implicit <code>this</code> Pointer</h6>
          <p>
            Because a static member function can be invoked without an object instance (<code>ClassName::func()</code>), it does not receive an implicit <code>this</code> pointer.
          </p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6>Restricted Member Access</h6>
          <p>
            A static member function can <strong>ONLY access static data members</strong> and call other static member functions directly. It cannot directly access non-static data members (because there is no object instance to select from).
          </p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">3</span>
        <div class="step-content">
          <h6>Invocation via Scope Resolution</h6>
          <p>
            Invoked through the class identifier: <code>ClassName::staticFunction();</code>, although calling through an object (<code>obj.staticFunction();</code>) is syntactically permitted but discouraged as misleading.
          </p>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Bank Interest Rate Inquiry Hotline</span>
  </div>
  <p>
    Imagine calling a commercial bank's automated phone hotline and pressing 1 for <em>"Current Home Loan Benchmark Interest Rate"</em>.<br>
    The automated voice immediately states: <em>"The current benchmark rate is 8.25% per annum."</em><br>
    Notice: the automated hotline did not ask you for your personal 16-digit account number or PIN! The benchmark rate is a <strong>class-level property</strong> applicable to everyone. You do not need to log in to a specific personal account to query the general benchmark rate. That query routine is a <strong>Static Member Function</strong>!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Static Member Function: Class-Level Invocation without Instantiation</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">ServerCluster</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">int</span> serverId;                  <span class="c-comment">// Non-static member (instance specific)</span>
    <span class="c-keyword">static</span> <span class="c-type">int</span> activeNodeCount;     <span class="c-comment">// Static data member</span>
    <span class="c-keyword">static</span> <span class="c-type">double</span> networkBandwidth; <span class="c-comment">// Static data member</span>

<span class="c-keyword">public</span>:
    <span class="c-type">ServerCluster</span>(<span class="c-type">int</span> id) : serverId(id) {
        activeNodeCount++;
    }

    ~<span class="c-type">ServerCluster</span>() {
        activeNodeCount--;
    }

    <span class="c-comment">// STATIC MEMBER FUNCTION: Operates at class scope without 'this' pointer</span>
    <span class="c-keyword">static</span> <span class="c-type">void</span> configureGlobalNetwork(<span class="c-type">double</span> bandwidthGbps) {
        networkBandwidth = bandwidthGbps;
        <span class="c-comment">// serverId = 10; // COMPILE ERROR: Cannot access non-static member without object!</span>
    }

    <span class="c-keyword">static</span> <span class="c-type">void</span> displayClusterDiagnostics() {
        std::cout &lt;&lt; <span class="c-string">"=== Cluster Telemetry ===\\n"</span>;
        std::cout &lt;&lt; <span class="c-string">"Active Nodes:      "</span> &lt;&lt; activeNodeCount &lt;&lt; <span class="c-string">"\\n"</span>;
        std::cout &lt;&lt; <span class="c-string">"Network Bandwidth: "</span> &lt;&lt; networkBandwidth &lt;&lt; <span class="c-string">" Gbps\\n"</span>;
    }
};

<span class="c-comment">// Allocate memory for static variables</span>
<span class="c-type">int</span> <span class="c-type">ServerCluster</span>::activeNodeCount = <span class="c-number">0</span>;
<span class="c-type">double</span> <span class="c-type">ServerCluster</span>::networkBandwidth = <span class="c-number">10.0</span>;

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. INVOKING STATIC FUNCTION BEFORE CREATING ANY OBJECT!</span>
    std::cout &lt;&lt; <span class="c-string">"1. Diagnostics before node spin-up:\\n"</span>;
    <span class="c-type">ServerCluster</span>::displayClusterDiagnostics();

    <span class="c-comment">// 2. Spin up instances</span>
    <span class="c-type">ServerCluster</span> node1(<span class="c-number">101</span>);
    <span class="c-type">ServerCluster</span> node2(<span class="c-number">102</span>);
    <span class="c-type">ServerCluster</span> node3(<span class="c-number">103</span>);

    <span class="c-comment">// 3. Reconfigure cluster dynamically via class name</span>
    <span class="c-type">ServerCluster</span>::configureGlobalNetwork(<span class="c-number">40.0</span>);

    std::cout &lt;&lt; <span class="c-string">"\\n2. Diagnostics after node spin-up &amp; reconfiguration:\\n"</span>;
    <span class="c-type">ServerCluster</span>::displayClusterDiagnostics();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Static Member Function Invocation Mechanics</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Call Site (No Object Needed) -->
      <g transform="translate(30, 40)">
        <rect width="210" height="130" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="105" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Call Site in main()</text>
        <rect x="15" y="45" width="180" height="40" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
        <text x="105" y="70" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">ServerCluster::</text>
        <text x="105" y="84" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">displayDiagnostics();</text>
        <text x="105" y="112" fill="var(--text-muted)" font-size="9" text-anchor="middle">No object instance required!</text>
      </g>

      <!-- Direct Arrow to Routine -->
      <path d="M 240 105 L 320 105" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="280" y="95" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Direct Call</text>

      <!-- Static Routine Block -->
      <g transform="translate(320, 25)">
        <rect width="410" height="160" rx="8" fill="var(--bg-card)" stroke="#6366f1" stroke-width="1.5"/>
        <text x="205" y="28" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Static Function: displayClusterDiagnostics()</text>
        
        <rect x="25" y="45" width="170" height="55" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981"/>
        <text x="110" y="65" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">&check; CAN ACCESS</text>
        <text x="110" y="85" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">activeNodeCount</text>

        <rect x="215" y="45" width="170" height="55" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444"/>
        <text x="300" y="65" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">&cross; CANNOT ACCESS</text>
        <text x="300" y="85" fill="var(--text-secondary)" font-family="monospace" font-size="10" text-anchor="middle">int serverId (No this)</text>

        <text x="205" y="125" fill="var(--accent-blue)" font-size="10" text-anchor="middle">Operates directly in class namespace scope</text>
        <text x="205" y="142" fill="var(--text-muted)" font-size="9" text-anchor="middle">No hidden this pointer passed into activation record</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Comparative Analysis: Static Data vs. Static Function</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Dimension</th>
        <th>Static Data Member</th>
        <th>Static Member Function</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Core Nature</strong></td>
        <td>A single shared class-level <strong>variable</strong>.</td>
        <td>A class-level <strong>routine/operation</strong>.</td>
      </tr>
      <tr>
        <td><strong>Invocation / Access</strong></td>
        <td>Accessed via <code>ClassName::var</code>.</td>
        <td>Invoked via <code>ClassName::func()</code>.</td>
      </tr>
      <tr>
        <td><strong><code>this</code> Pointer</strong></td>
        <td>N/A (Represents state).</td>
        <td>Has <strong>no <code>this</code> pointer</strong>.</td>
      </tr>
      <tr>
        <td><strong>Data Access Scope</strong></td>
        <td>Read/written by both static &amp; non-static member functions.</td>
        <td>Can directly access <strong>only static members</strong>.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Questions on <em>"Explain static member functions and state their properties"</em> frequently appear in 5-mark short notes. Write the 3 rules: 1) No <code>this</code> pointer, 2) Only access static data, 3) Called via <code>Class::func()</code>. Mentioning that static functions cannot be virtual or const earns full marks!
</div>
"""
    sections.append({
        "id": "u5-sec-5",
        "number": 5,
        "part": "PART 1 — OBJECTS AND CLASSES",
        "title": "5. Static Member Functions",
        "subtitle": "Class-Level Invocations, this Pointer Absence, Access Restrictions & Diagnostic Operations",
        "content": sec5_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit5_part1_sections()
    print(f"generate_unit5_part1.py compiled {len(secs)} sections successfully.")
