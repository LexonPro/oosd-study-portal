# generate_unit1_part2.py: Part 2 - Object Identity, Encapsulation & Polymorphism (Sections 04 to 08)

def get_unit1_part2_sections():
    return [
        # -------------------------------------------------------------
        # Section 04: Object Identity
        # -------------------------------------------------------------
        {
            "id": "u1-sec-4",
            "number": "04",
            "part": "Part 2 — Object Identity, Encapsulation & Polymorphism",
            "title": "Object Identity",
            "subtitle": "Object IDs, State Equivalence vs Identity Equivalence & Pointer Comparisons in C++",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational Concept</div>
    <h3>What is Object Identity?</h3>
    <p><strong>Object Identity</strong> is an intrinsic property of an object in an object data model that distinguishes it from all other objects in the universe, regardless of its class, state, or attribute values. An object is assigned a unique internal <strong>Object Identifier (OID)</strong> upon creation.</p>
    <p>According to AKTU Quantum (Que 1.8), the object identifier is used to define associations between objects and to support data retrieval and comparison based on the internal identifier rather than the transient values of an object's attributes.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Identical Twins &amp; National Passport Numbers</div>
  <p>Consider identical twin brothers, <strong>Rahul</strong> and <strong>Rohan</strong>. Both share the exact same surname, eye color, blood group, age (21), and even dress alike (identical attribute values). If a system compared them purely by their physical traits (state equivalence), it would falsely conclude they are the exact same person. However, each possesses a distinct <strong>Passport Number / Biometric ID</strong> (Object Identity). Even if Rahul changes his hair color or job, his identity remains immutable.</p>
</div>

<div class="subtopics-container">
  <h4>Key Principles of Object Identity</h4>

  <div class="detail-block">
    <h5>1. Identity vs Attribute Values (State)</h5>
    <p>Two objects may have identical state (e.g., two <code>Account</code> objects both having balance <code>$5,000</code> and owner <code>"Alice"</code>), yet they are distinct physical entities in memory. Modifying the balance of one account must never alter the balance of the other.</p>
  </div>

  <div class="detail-block">
    <h5>2. Implementation in Programming Languages (C++)</h5>
    <p>Modern object-oriented languages have built-in mechanisms for managing object identity without requiring explicit identifier fields:</p>
    <ul>
      <li>In <strong>C++</strong>, an object's physical <strong>memory address</strong> serves as its unique identifier.</li>
      <li>The address is retrieved using the address-of operator (<code>&amp;obj</code>).</li>
      <li>Identity comparison is performed via <strong>pointer equality</strong> (<code>&amp;obj1 == &amp;obj2</code>).</li>
      <li>In <strong>Java</strong>, the default <code>==</code> operator compares object references (identity), while <code>.equals()</code> evaluates logical state equality.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Value Objects vs Identity Objects</h5>
    <p>In domain modeling, primitive types like numbers, colors (<code>Color(255, 0, 0)</code>), and coordinates (<code>Point(10, 20)</code>) are treated as <strong>Value Objects</strong> where identity is defined entirely by value. Conversely, domain entities like <code>Customer</code>, <code>Order</code>, and <code>Employee</code> rely on invariant OIDs.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>State Equivalence (Value) vs Identity Equivalence (Address)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Dimension</th>
        <th>State Equivalence (Value Equality)</th>
        <th>Identity Equivalence (OID Equality)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Definition</strong></td>
        <td>Two objects hold the same field values</td>
        <td>Two references point to the exact same physical memory cell</td>
      </tr>
      <tr>
        <td><strong>Comparison Operator</strong></td>
        <td>Overloaded <code>operator==</code> (C++) or <code>.equals()</code> (Java)</td>
        <td>Pointer equality: <code>&amp;objA == &amp;objB</code> (C++) or <code>refA == refB</code> (Java)</td>
      </tr>
      <tr>
        <td><strong>Mutability</strong></td>
        <td>Can change over time as attributes mutate</td>
        <td>Permanent and immutable throughout object lifetime</td>
      </tr>
      <tr>
        <td><strong>Example</strong></td>
        <td>Two $100 bills have identical value ($100)</td>
        <td>Each bill has a distinct, unique Serial Number</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Demonstration: Object Identity vs Value Equivalence</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>

<span class="c-keyword">class</span> Student {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> name;
    <span class="c-type">int</span> age;

<span class="c-keyword">public</span>:
    Student(<span class="c-type">std::string</span> name, <span class="c-type">int</span> age) : name(name), age(age) {}

    <span class="c-comment">// Overloaded operator== tests STATE EQUIVALENCE</span>
    <span class="c-type">bool</span> operator==(<span class="c-keyword">const</span> Student&amp; other) <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> (this-&gt;name == other.name &amp;&amp; this-&gt;age == other.age);
    }

    <span class="c-type">void</span> display() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"Student: "</span> &lt;&lt; name &lt;&lt; <span class="c-string">", Age: "</span> &lt;&lt; age 
                  &lt;&lt; <span class="c-string">" | Memory Address (OID): "</span> &lt;&lt; this &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">// Two distinct objects with IDENTICAL state</span>
    <span class="c-type">Student</span> s1(<span class="c-string">"Rahul"</span>, <span class="c-number">21</span>);
    <span class="c-type">Student</span> s2(<span class="c-string">"Rahul"</span>, <span class="c-number">21</span>);

    <span class="c-comment">// A reference pointing to the SAME physical object</span>
    <span class="c-type">Student</span>&amp; s3 = s1;

    s1.display();
    s2.display();

    <span class="c-comment">// 1. Testing State Equivalence (Values match)</span>
    <span class="c-keyword">if</span> (s1 == s2) {
        std::cout &lt;&lt; <span class="c-string">"[State Check]: s1 and s2 have identical state (Rahul, 21).\\n"</span>;
    }

    <span class="c-comment">// 2. Testing Identity Equivalence (Pointer addresses)</span>
    <span class="c-keyword">if</span> (&amp;s1 == &amp;s2) {
        std::cout &lt;&lt; <span class="c-string">"[Identity Check]: s1 and s2 are the SAME object.\\n"</span>;
    } <span class="c-keyword">else</span> {
        std::cout &lt;&lt; <span class="c-string">"[Identity Check]: s1 and s2 are DISTINCT objects (Addresses differ)!\\n"</span>;
    }

    <span class="c-comment">// 3. Testing Reference Identity</span>
    <span class="c-keyword">if</span> (&amp;s1 == &amp;s3) {
        std::cout &lt;&lt; <span class="c-string">"[Identity Check]: s1 and s3 share the EXACT SAME identity (&amp;s1 == &amp;s3).\\n"</span>;
    }

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Identity (Address) vs State in System Memory</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Stack Frame -->
      <g transform="translate(40, 30)">
        <rect width="220" height="220" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="220" height="34" rx="8" fill="#0369a1"/>
        <text x="110" y="22" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">CALL STACK / REFERENCES</text>

        <!-- Variable s1 -->
        <rect x="15" y="50" width="190" height="42" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="25" y="70" fill="#38bdf8" font-size="11" font-weight="bold">Variable s1</text>
        <text x="25" y="85" fill="#94a3b8" font-size="9">ptr → 0x7FFEE10</text>

        <!-- Variable s2 -->
        <rect x="15" y="105" width="190" height="42" rx="6" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
        <text x="25" y="125" fill="#38bdf8" font-size="11" font-weight="bold">Variable s2</text>
        <text x="25" y="140" fill="#94a3b8" font-size="9">ptr → 0x7FFEE58</text>

        <!-- Variable s3 -->
        <rect x="15" y="160" width="190" height="42" rx="6" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
        <text x="25" y="180" fill="#c084fc" font-size="11" font-weight="bold">Reference s3 (&amp;s1)</text>
        <text x="25" y="195" fill="#94a3b8" font-size="9">alias → 0x7FFEE10</text>
      </g>

      <!-- Heap / Object Memory -->
      <g transform="translate(360, 30)">
        <rect width="420" height="220" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
        <rect width="420" height="34" rx="8" fill="#4338ca"/>
        <text x="210" y="22" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">OBJECT MEMORY / PHYSICAL HEAP</text>

        <!-- Object 1 -->
        <g transform="translate(20, 50)">
          <rect width="175" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
          <rect width="175" height="28" rx="8" fill="#0284c7"/>
          <text x="87" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Object @ 0x7FFEE10</text>
          
          <text x="15" y="45" fill="#fbbf24" font-size="10" font-weight="bold">OID: #10492</text>
          <line x1="15" y1="52" x2="160" y2="52" stroke="#334155" stroke-width="1"/>
          
          <text x="15" y="72" fill="#e2e8f0" font-size="10">name = "Rahul"</text>
          <text x="15" y="92" fill="#e2e8f0" font-size="10">age = 21</text>
          
          <rect x="15" y="110" width="145" height="24" rx="4" fill="#0369a1" opacity="0.6"/>
          <text x="87" y="126" fill="#38bdf8" font-size="9" text-anchor="middle">Identity: Unique</text>
        </g>

        <!-- Object 2 -->
        <g transform="translate(225, 50)">
          <rect width="175" height="150" rx="8" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
          <rect width="175" height="28" rx="8" fill="#2563eb"/>
          <text x="87" y="18" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Object @ 0x7FFEE58</text>
          
          <text x="15" y="45" fill="#fbbf24" font-size="10" font-weight="bold">OID: #10493</text>
          <line x1="15" y1="52" x2="160" y2="52" stroke="#334155" stroke-width="1"/>
          
          <text x="15" y="72" fill="#e2e8f0" font-size="10">name = "Rahul"</text>
          <text x="15" y="92" fill="#e2e8f0" font-size="10">age = 21</text>
          
          <rect x="15" y="110" width="145" height="24" rx="4" fill="#1d4ed8" opacity="0.6"/>
          <text x="87" y="126" fill="#93c5fd" font-size="9" text-anchor="middle">State: Equal to Obj 1</text>
        </g>
      </g>

      <!-- Connecting Arrows -->
      <path d="M 245 100 C 290 100, 310 100, 375 100" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#u1-id-arr)"/>
      <path d="M 245 155 C 310 155, 480 155, 580 155" fill="none" stroke="#60a5fa" stroke-width="2" marker-end="url(#u1-id-arr)"/>
      <path d="M 245 210 C 310 210, 320 125, 375 125" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="4" marker-end="url(#u1-id-arr-purple)"/>

      <defs>
        <marker id="u1-id-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="u1-id-arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#c084fc"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14):</strong> <em>"What do you understand by object identity? Explain with an example."</em> [5 Marks - Que 1.8]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define OID as an intrinsic property distinguishing data independent of attribute values. Highlight that in C++, an object's memory address serves as its unique identifier via the <code>&amp;</code> operator, and pointer comparison evaluates identity. Mention that two objects with identical attributes <code>("Rahul", 21)</code> are still distinct entities.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Object Identity:</strong> Inherent property distinguishing each object uniquely from all others.</li>
    <li><strong>State Equivalence:</strong> Objects having matching field values (<code>s1 == s2</code>).</li>
    <li><strong>Identity Equivalence:</strong> Pointers referencing the exact same memory address (<code>&amp;s1 == &amp;s2</code>).</li>
    <li><strong>C++ Mechanism:</strong> The address-of operator <code>&amp;</code> returns the physical OID.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 05: Encapsulation
        # -------------------------------------------------------------
        {
            "id": "u1-sec-5",
            "number": "05",
            "part": "Part 2 — Object Identity, Encapsulation & Polymorphism",
            "title": "Encapsulation",
            "subtitle": "Data + Behavior Packaging, Inviolable Shell & Message Passing Architecture",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Core OO Pillar</div>
    <h3>What is Encapsulation?</h3>
    <p><strong>Encapsulation</strong> is the mechanism of binding together data (attributes) and the code that manipulates them (methods) into a single self-contained unit, forming an <strong>inviolable protective shell</strong> around the object.</p>
    <p>According to AKTU Quantum (Que 1.9), encapsulation consists of separating the external aspects of an object—which are accessible to other objects—from the internal implementation details of the object, which are hidden. It prevents a program from becoming so interdependent that a small change has massive ripple effects.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Bank ATM Machine</div>
  <p>An <strong>ATM</strong> contains millions of dollars in cash, cryptographic vaults, and complex network hardware. You cannot pry open the steel door and adjust the cash cassette directly. Instead, the ATM provides an encapsulated public interface: a keypad and screen. When you insert your card and request $100 via <code>withdraw(100)</code>, the internal mechanisms verify your balance, log the transaction, and dispense the cash. The internal ledger is protected from unauthorized tampering.</p>
</div>

<div class="subtopics-container">
  <h4>Architectural Tenets of Encapsulation</h4>

  <div class="detail-block">
    <h5>1. The Inviolable Protective Shell</h5>
    <p>An encapsulated object acts like a biological cell with a selective semi-permeable membrane. The state inside the shell is declared <code>private</code>. Outside entities cannot read or write directly to these fields; they can only interact via <code>public</code> methods.</p>
  </div>

  <div class="detail-block">
    <h5>2. Preventing Ripple Effects</h5>
    <p>In procedural code, changing a global record structure forces modifications across thousands of lines of dependent code. Encapsulation establishes a contract: as long as public method signatures remain stable, the internal implementation (algorithms, data storage) can be refactored, optimized, or bug-fixed with zero ripple effect on client code.</p>
  </div>

  <div class="detail-block">
    <h5>3. Message Passing as an Encapsulation Enforcer (Que 1.9)</h5>
    <p>In an OO system, objects communicate exclusively via <strong>Message Passing</strong>. An object only exposes its interface (services and operation signatures). To retrieve an employee's salary, an outside object sends the message <code>getSalary()</code>. The <code>Employee</code> object verifies authorization, computes bonuses, and returns the result. The internal variable <code>salary</code> remains completely hidden.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Procedural Global Access vs Encapsulated OO Design</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Procedural (Unencapsulated)</th>
        <th>Object-Oriented (Encapsulated)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Data Security</strong></td>
        <td>Data is exposed globally or passed across functions</td>
        <td>Data is strictly private within the class shell</td>
      </tr>
      <tr>
        <td><strong>Access Path</strong></td>
        <td>Direct memory / variable assignment (<code>emp.salary = -5000</code>)</td>
        <td>Controlled method invocation with validation (<code>emp.setSalary(5000)</code>)</td>
      </tr>
      <tr>
        <td><strong>Coupling</strong></td>
        <td>High coupling; modifications cause cascade failures</td>
        <td>Loose coupling; internal refactoring preserves client code</td>
      </tr>
      <tr>
        <td><strong>Communication</strong></td>
        <td>Direct function calls on raw data structs</td>
        <td>Asynchronous or synchronous formal Message Passing</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Demonstration: Encapsulation with Message Passing (AKTU Que 1.9 Example)</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>
<span class="c-keyword">#include &lt;stdexcept&gt;</span>

<span class="c-keyword">class</span> Employee {
<span class="c-keyword">private</span>:
    <span class="c-comment">// Hidden attributes (Internal State)</span>
    <span class="c-type">std::string</span> empName;
    <span class="c-type">double</span> salary;
    <span class="c-type">double</span> taxDeduction;

    <span class="c-comment">// Internal helper method hidden from external callers</span>
    <span class="c-type">double</span> calculateNetSalary() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> salary - taxDeduction;
    }

<span class="c-keyword">public</span>:
    <span class="c-comment">// Constructor initializes the encapsulated state</span>
    Employee(<span class="c-type">std::string</span> name, <span class="c-type">double</span> sal) : empName(name) {
        <span class="c-keyword">if</span> (sal &lt; <span class="c-number">0</span>) <span class="c-keyword">throw</span> std::invalid_argument(<span class="c-string">"Salary cannot be negative!"</span>);
        this-&gt;salary = sal;
        this-&gt;taxDeduction = sal * <span class="c-number">0.15</span>; <span class="c-comment">// 15% flat deduction</span>
    }

    <span class="c-comment">// Public Interface: Controlled access via Message Passing</span>
    <span class="c-type">std::string</span> getName() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> empName;
    }

    <span class="c-comment">// Message: getSalary() - client requests salary without touching private field</span>
    <span class="c-type">double</span> getSalary() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> calculateNetSalary();
    }

    <span class="c-comment">// Message: updateSalary(newSal) with strict business rule validation</span>
    <span class="c-type">void</span> updateSalary(<span class="c-type">double</span> newSalary) {
        <span class="c-keyword">if</span> (newSalary &gt;= this-&gt;salary) {
            this-&gt;salary = newSalary;
            this-&gt;taxDeduction = newSalary * <span class="c-number">0.15</span>;
            std::cout &lt;&lt; <span class="c-string">"[Update]: Salary updated successfully for "</span> &lt;&lt; empName &lt;&lt; <span class="c-string">"\\n"</span>;
        } <span class="c-keyword">else</span> {
            std::cout &lt;&lt; <span class="c-string">"[Error]: Salary reduction rejected by business policy!\\n"</span>;
        }
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">Employee</span> emp(<span class="c-string">"Vikram"</span>, <span class="c-number">75000.0</span>);

    <span class="c-comment">// Direct access to emp.salary is PREVENTED by the compiler:</span>
    <span class="c-comment">// emp.salary = 90000; // COMPILE ERROR: 'salary' is private</span>

    <span class="c-comment">// Access via message passing:</span>
    std::cout &lt;&lt; <span class="c-string">"Employee: "</span> &lt;&lt; emp.getName() &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Net Take-Home Salary: $"</span> &lt;&lt; emp.getSalary() &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Requesting operation through valid message signature:</span>
    emp.updateSalary(<span class="c-number">82000.0</span>);
    std::cout &lt;&lt; <span class="c-string">"Revised Salary: $"</span> &lt;&lt; emp.getSalary() &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Attempting invalid state transition:</span>
    emp.updateSalary(<span class="c-number">50000.0</span>); <span class="c-comment">// Rejected by validation logic!</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Encapsulation Shell &amp; Message Passing (AKTU Fig. 1.9.1)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="300" fill="#0f172a" rx="12"/>

      <!-- Outer Shell: Encapsulation Boundary -->
      <g transform="translate(230, 20)">
        <ellipse cx="180" cy="130" rx="170" ry="120" fill="#1e293b" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,3"/>
        <text x="180" y="32" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">ENCAPSULATION BARRIER (PUBLIC INTERFACE)</text>

        <!-- Methods Ring -->
        <rect x="50" y="55" width="110" height="32" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="105" y="75" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">getSalary()</text>

        <rect x="200" y="55" width="110" height="32" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="255" y="75" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">updateSalary()</text>

        <rect x="50" y="175" width="110" height="32" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="105" y="195" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">getName()</text>

        <rect x="200" y="175" width="110" height="32" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="255" y="195" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">calcBonus()</text>

        <!-- Hidden Core (Private Attributes) -->
        <rect x="100" y="105" width="160" height="50" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
        <text x="180" y="126" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">HIDDEN ATTRIBUTES</text>
        <text x="180" y="144" fill="#ffffff" font-size="10" text-anchor="middle">salary, taxDeduction</text>
      </g>

      <!-- External Client 1 (Left) -->
      <g transform="translate(20, 100)">
        <rect width="150" height="80" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="150" height="24" rx="8" fill="#7e22ce"/>
        <text x="75" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">PayrollSubsystem</text>
        <text x="75" y="48" fill="#c084fc" font-size="9" text-anchor="middle">External Caller</text>
        <text x="75" y="66" fill="#94a3b8" font-size="8" text-anchor="middle">Cannot access .salary</text>
      </g>

      <!-- Message Arrow 1 -->
      <path d="M 175 140 L 275 90" fill="none" stroke="#a855f7" stroke-width="2.5" marker-end="url(#u1-enc-arr-purple)"/>
      <rect x="180" y="96" width="90" height="18" rx="4" fill="#0f172a" stroke="#7e22ce" stroke-width="1"/>
      <text x="225" y="109" fill="#c084fc" font-size="8" font-weight="bold" text-anchor="middle">msg: getSalary()</text>

      <!-- External Client 2 (Right) -->
      <g transform="translate(650, 100)">
        <rect width="150" height="80" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="150" height="24" rx="8" fill="#047857"/>
        <text x="75" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">HRManagement</text>
        <text x="75" y="48" fill="#6ee7b7" font-size="9" text-anchor="middle">External Caller</text>
        <text x="75" y="66" fill="#94a3b8" font-size="8" text-anchor="middle">Sends message</text>
      </g>

      <!-- Message Arrow 2 -->
      <path d="M 645 140 L 545 90" fill="none" stroke="#10b981" stroke-width="2.5" marker-end="url(#u1-enc-arr-green)"/>
      <rect x="548" y="96" width="105" height="18" rx="4" fill="#0f172a" stroke="#047857" stroke-width="1"/>
      <text x="600" y="109" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">msg: updateSalary()</text>

      <defs>
        <marker id="u1-enc-arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
        <marker id="u1-enc-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2012-13):</strong> <em>"What do you mean by encapsulation? How does the object-oriented concept of message passing help to encapsulate the implementation of an object, including its data?"</em> [5 Marks - Que 1.9]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Draw AKTU Fig. 1.9.1 showing methods surrounding hidden attributes. Clearly state that external callers only interact with operation signatures via messages; the receiver decides how to process the request. Explain that encapsulation prevents ripple effects by allowing internal state refactoring without breaking clients.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Encapsulation:</strong> Bundling data and methods into a single unit; hiding internal state behind public methods.</li>
    <li><strong>Ripple Effect Prevention:</strong> Modifying internal logic does not break external dependent callers.</li>
    <li><strong>Message Passing:</strong> Clients invoke services by dispatching messages with valid signatures.</li>
    <li><strong>AKTU Example:</strong> <code>Employee.salary</code> is protected and queried only via <code>getSalary()</code>.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 06: Information Hiding
        # -------------------------------------------------------------
        {
            "id": "u1-sec-6",
            "number": "06",
            "part": "Part 2 — Object Identity, Encapsulation & Polymorphism",
            "title": "Information Hiding",
            "subtitle": "Abstraction, Decoupling Calling Code & Encapsulation vs Information Hiding",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Design Principle</div>
    <h3>What is Information Hiding?</h3>
    <p><strong>Information Hiding</strong> is a foundational software design principle (originated by David Parnas) asserting that modules should hide design decisions that are most volatile, complex, or subject to future change from all other modules.</p>
    <p>According to AKTU Quantum (Que 1.10), information hiding results in an <strong>abstraction</strong> that reduces external complexity and makes components easier to use. It decouples the calling code from internal workings, allowing hidden implementations to change freely without breaking client code.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Modern Automobile Transmission</div>
  <p>When you drive an automatic car, your interface consists of an accelerator pedal, brake, and a gear selector (<code>P, R, N, D</code>). You do not know—nor do you need to know—whether the transmission uses a dual-clutch gearbox, a torque converter, or an electronic continuously variable transmission (CVT). If the automaker replaces the 6-speed transmission with an 8-speed electric motor in the next model year, you do not need to relearn how to drive. The complex mechanical implementation is completely hidden!</p>
</div>

<div class="subtopics-container">
  <h4>Key Principles of Information Hiding</h4>

  <div class="detail-block">
    <h5>1. Abstraction &amp; Complexity Reduction</h5>
    <p>By exposing only the abstract contract (what a component does) and concealing the internal mechanics (how it does it), the cognitive load on developers is minimized. A programmer using a <code>Map</code> data structure needs only <code>put()</code> and <code>get()</code>, not red-black tree balancing rotations.</p>
  </div>

  <div class="detail-block">
    <h5>2. Decoupling Calling Code</h5>
    <p>Information hiding creates an architectural firebreak. If an internal data structure is migrated from an unsorted dynamic array to a hash table to improve algorithmic lookup speed from <code>O(n)</code> to <code>O(1)</code>, zero lines of client code need recompilation or editing.</p>
  </div>

  <div class="detail-block">
    <h5>3. Relationship with Encapsulation</h5>
    <p>While often conflated, <strong>Information Hiding is the design goal</strong> (the principle of concealing secrets), whereas <strong>Encapsulation is the programming technique</strong> (the language construct like classes, <code>private</code> access specifiers, and packages) used to realize that goal.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Encapsulation vs Information Hiding (Key AKTU Distinction)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Encapsulation</th>
        <th>Information Hiding</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Nature</strong></td>
        <td>Language mechanism / implementation technique</td>
        <td>Architectural design principle / theoretical concept</td>
      </tr>
      <tr>
        <td><strong>Focus</strong></td>
        <td>Packaging data and methods into a single class unit</td>
        <td>Concealing complex, volatile design secrets behind interfaces</td>
      </tr>
      <tr>
        <td><strong>How Achieved</strong></td>
        <td>Using classes, structures, and access specifiers (<code>private</code>)</td>
        <td>Designing rigorous abstract interfaces, APIs, and modules</td>
      </tr>
      <tr>
        <td><strong>Relationship</strong></td>
        <td>The tool / vehicle</td>
        <td>The ultimate objective / destination</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Demonstration: Refactoring Internal Storage Without Changing Client Contract</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>
<span class="c-keyword">#include &lt;vector&gt;</span>
<span class="c-keyword">#include &lt;unordered_map&gt;</span>

<span class="c-comment">// Abstract Public Interface (Client Contract)</span>
<span class="c-keyword">class</span> IStudentDirectory {
<span class="c-keyword">public</span>:
    <span class="c-keyword">virtual</span> ~IStudentDirectory() = <span class="c-keyword">default</span>;
    <span class="c-keyword">virtual</span> <span class="c-type">void</span> addStudent(<span class="c-type">int</span> roll, <span class="c-keyword">const</span> <span class="c-type">std::string</span>&amp; name) = <span class="c-number">0</span>;
    <span class="c-keyword">virtual</span> <span class="c-type">std::string</span> findStudent(<span class="c-type">int</span> roll) = <span class="c-number">0</span>;
};

<span class="c-comment">// Implementation: Internal structure hidden inside private section</span>
<span class="c-keyword">class</span> FastStudentDirectory : <span class="c-keyword">public</span> IStudentDirectory {
<span class="c-keyword">private</span>:
    <span class="c-comment">// DESIGN SECRET: We use an unordered_map for O(1) hash lookups.</span>
    <span class="c-comment">// Earlier this was a slow vector&lt;pair&lt;int, string&gt;&gt; with O(n) search.</span>
    <span class="c-comment">// The client code never knew about the change!</span>
    <span class="c-type">std::unordered_map</span>&lt;<span class="c-type">int</span>, <span class="c-type">std::string</span>&gt; studentMap;

<span class="c-keyword">public</span>:
    <span class="c-type">void</span> addStudent(<span class="c-type">int</span> roll, <span class="c-keyword">const</span> <span class="c-type">std::string</span>&amp; name) <span class="c-keyword">override</span> {
        studentMap[roll] = name;
    }

    <span class="c-type">std::string</span> findStudent(<span class="c-type">int</span> roll) <span class="c-keyword">override</span> {
        auto it = studentMap.find(roll);
        <span class="c-keyword">if</span> (it != studentMap.end()) {
            <span class="c-keyword">return</span> it-&gt;second;
        }
        <span class="c-keyword">return</span> <span class="c-string">"Student Not Found"</span>;
    }
};

<span class="c-comment">// Client Code relies ONLY on the abstract interface</span>
<span class="c-type">void</span> executeDirectoryQueries(IStudentDirectory&amp; dir) {
    dir.addStudent(<span class="c-number">101</span>, <span class="c-string">"Aman Gupta"</span>);
    dir.addStudent(<span class="c-number">102</span>, <span class="c-string">"Priya Sharma"</span>);

    std::cout &lt;&lt; <span class="c-string">"Query Roll 101: "</span> &lt;&lt; dir.findStudent(<span class="c-number">101</span>) &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Query Roll 999: "</span> &lt;&lt; dir.findStudent(<span class="c-number">999</span>) &lt;&lt; <span class="c-string">"\\n"</span>;
}

<span class="c-type">int</span> main() {
    FastStudentDirectory dir;
    executeDirectoryQueries(dir);
    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Information Hiding Wall (Public Contract vs Hidden Volatile Details)</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="260" fill="#0f172a" rx="12"/>

      <!-- Client Side (Left) -->
      <g transform="translate(30, 40)">
        <rect width="210" height="180" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="210" height="32" rx="8" fill="#0369a1"/>
        <text x="105" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLIENT / CALLING CODE</text>
        
        <text x="15" y="60" fill="#93c5fd" font-size="10" font-weight="bold">Sees Only Abstractions:</text>
        <text x="15" y="85" fill="#e2e8f0" font-size="9">• addStudent(id, name)</text>
        <text x="15" y="105" fill="#e2e8f0" font-size="9">• findStudent(id)</text>
        
        <rect x="15" y="125" width="180" height="40" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
        <text x="105" y="142" fill="#38bdf8" font-size="9" text-anchor="middle">Zero dependency on</text>
        <text x="105" y="156" fill="#38bdf8" font-size="9" text-anchor="middle">internal data layout!</text>
      </g>

      <!-- The Information Hiding Wall -->
      <g transform="translate(280, 20)">
        <rect width="22" height="220" rx="4" fill="#64748b" stroke="#94a3b8" stroke-width="1"/>
        <line x1="291" y1="20" x2="291" y2="240" stroke="#f8fafc" stroke-width="2" stroke-dasharray="8,4"/>
        <text x="-130" y="295" fill="#f8fafc" font-size="10" font-weight="bold" transform="rotate(-90)" letter-spacing="2">INTERFACE BARRIER</text>
      </g>

      <!-- Public Interface Facade -->
      <g transform="translate(330, 40)">
        <rect width="180" height="180" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="180" height="32" rx="8" fill="#047857"/>
        <text x="90" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">STABLE INTERFACE</text>

        <circle cx="90" cy="75" r="22" fill="#065f46" stroke="#34d399" stroke-width="2"/>
        <text x="90" y="80" fill="#34d399" font-size="16" font-weight="bold" text-anchor="middle">API</text>
        
        <text x="90" y="125" fill="#e2e8f0" font-size="10" text-anchor="middle" font-weight="bold">Public Contract</text>
        <text x="90" y="145" fill="#94a3b8" font-size="9" text-anchor="middle">Guaranteed signatures</text>
        <text x="90" y="160" fill="#94a3b8" font-size="9" text-anchor="middle">Immutable API shape</text>
      </g>

      <!-- Hidden Volatile Internals (Right) -->
      <g transform="translate(540, 40)">
        <rect width="240" height="180" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
        <rect width="240" height="32" rx="8" fill="#991b1b"/>
        <text x="120" y="21" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">HIDDEN VOLATILE SECRETS</text>
        
        <rect x="15" y="48" width="210" height="34" rx="4" fill="#0f172a" stroke="#f87171" stroke-width="1"/>
        <text x="25" y="65" fill="#fca5a5" font-size="9" font-weight="bold">Storage: Hash Bucket Layout</text>
        <text x="25" y="76" fill="#94a3b8" font-size="8">O(1) hash map vs dynamic array</text>

        <rect x="15" y="90" width="210" height="34" rx="4" fill="#0f172a" stroke="#f87171" stroke-width="1"/>
        <text x="25" y="107" fill="#fca5a5" font-size="9" font-weight="bold">Concurrency: Mutex / Locks</text>
        <text x="25" y="118" fill="#94a3b8" font-size="8">Thread-safe synchronization code</text>

        <rect x="15" y="132" width="210" height="34" rx="4" fill="#0f172a" stroke="#f87171" stroke-width="1"/>
        <text x="25" y="149" fill="#fca5a5" font-size="9" font-weight="bold">Algorithm: Tree Rebalancing</text>
        <text x="25" y="160" fill="#94a3b8" font-size="8">Subject to refactoring at any time</text>
      </g>

      <!-- Connecting arrows -->
      <path d="M 240 120 L 320 120" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#u1-ih-arr)"/>
      <path d="M 510 120 L 535 120" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#u1-ih-arr-green)"/>

      <defs>
        <marker id="u1-ih-arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="u1-ih-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ:</strong> <em>"Write a short note on Information Hiding. How does it differ from encapsulation?"</em> [5 Marks - Que 1.10]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define Information Hiding as the design principle of concealing volatile decisions to decouple calling code. Emphasize that Encapsulation is the language mechanism (class + access modifiers) while Information Hiding is the design motivation (decoupling &amp; modularity). Mention that it prevents ripple effects and simplifies mental models through abstraction.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Information Hiding:</strong> Concealing internal details to produce a clean, decoupled abstraction.</li>
    <li><strong>David Parnas Principle:</strong> Hide design decisions most likely to change or cause bugs.</li>
    <li><strong>Encapsulation vs Hiding:</strong> Encapsulation is the vehicle (packaging); Information Hiding is the destination (abstraction).</li>
    <li><strong>Benefit:</strong> Internal data structures can be refactored with zero ripple effect on client code.</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 07: Polymorphism
        # -------------------------------------------------------------
        {
            "id": "u1-sec-7",
            "number": "07",
            "part": "Part 2 — Object Identity, Encapsulation & Polymorphism",
            "title": "Polymorphism",
            "subtitle": "Many Forms, File.print() Case Study & Ad-hoc vs Universal Polymorphism",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Core OO Pillar</div>
    <h3>What is Polymorphism?</h3>
    <p><strong>Polymorphism</strong> (from Greek: <em>poly</em> = many, <em>morph</em> = form) is the ability of a single interface or operation to take on different forms and exhibit different behaviors depending upon the class of the target object on which it is invoked.</p>
    <p>According to AKTU Quantum (Que 1.11), polymorphism plays an important role in allowing objects with distinct internal structures to share the same external interface. Each operation has a target object as an implicit argument, and the object <em>"knows"</em> its class to execute the correct method implementation.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Universal Power Switch &amp; Media Play Button</div>
  <p>Consider the <strong>Play</strong> button on modern electronic devices. Whether pressed on a cassette player, a DVD deck, Spotify on an iPhone, or a 4K laser projector, the user interaction is identical: <code>play()</code>. However, the internal actions are radically different: the cassette motor spins magnetic tape; the DVD player focuses an infrared laser; Spotify decompresses an encrypted AAC stream; the projector ignites a laser diode. The user commands one interface; each target object performs its unique specialized implementation!</p>
</div>

<div class="subtopics-container">
  <h4>The Canonical File.print() Example (AKTU Que 1.11)</h4>
  <p>In operating systems and document processors, a base class <code>File</code> defines an abstract operation <code>print()</code>:</p>
  <ul>
    <li><strong>AsciiFile:</strong> Sends raw ASCII character streams directly to a console or dot-matrix printer.</li>
    <li><strong>BinaryFile:</strong> Formats raw hexadecimal memory dumps with offset addresses.</li>
    <li><strong>PictureFile:</strong> Decodes JPEG/PNG raster pixels, applies color rendering, and scales resolutions for printer hardware.</li>
  </ul>
  <p>Logically, all three methods perform the same semantic task (<em>"print the file"</em>), but each is implemented by completely different source code. The caller simply issues <code>file-&gt;print()</code> without branching with <code>if/else</code> type checks.</p>
</div>

<div class="comparison-table-wrapper">
  <h4>Taxonomy of Polymorphism: Ad-hoc vs Universal (AKTU Core Que 1.11)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Category</th>
        <th>Sub-Type</th>
        <th>Mechanism</th>
        <th>Environment Applicability</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="2"><strong>Ad-hoc Polymorphism</strong></td>
        <td><strong>Function Overloading</strong></td>
        <td>Same function name with different parameter signatures resolved at compile-time</td>
        <td>Both Traditional (C, Pascal) and OO languages</td>
      </tr>
      <tr>
        <td><strong>Coercion (Casting)</strong></td>
        <td>Automatic or explicit type conversion (e.g., <code>float + int</code>)</td>
        <td>Both Traditional and OO languages</td>
      </tr>
      <tr>
        <td rowspan="2"><strong>Universal Polymorphism</strong></td>
        <td><strong>Parametric (Generics)</strong></td>
        <td>Functions/classes written without mention of specific types (Templates, Generics)</td>
        <td>Primarily Modern OO languages</td>
      </tr>
      <tr>
        <td><strong>Subtyping (Inclusion)</strong></td>
        <td>Derived classes override virtual operations of base class (Dynamic dispatch / VTable)</td>
        <td><strong>Exclusively Object-Oriented Systems</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Demonstration: The File.print() Polymorphic Hierarchy with Dynamic Dispatch</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;vector&gt;</span>
<span class="c-keyword">#include &lt;memory&gt;</span>

<span class="c-comment">// Abstract Base Class</span>
<span class="c-keyword">class</span> File {
<span class="c-keyword">protected</span>:
    <span class="c-type">std::string</span> filename;

<span class="c-keyword">public</span>:
    File(<span class="c-type">std::string</span> name) : filename(name) {}
    <span class="c-keyword">virtual</span> ~File() = <span class="c-keyword">default</span>;

    <span class="c-comment">// Pure virtual function defining polymorphic operation</span>
    <span class="c-keyword">virtual</span> <span class="c-type">void</span> print() <span class="c-keyword">const</span> = <span class="c-number">0</span>;
};

<span class="c-comment">// Concrete Derived Class 1: ASCII File</span>
<span class="c-keyword">class</span> AsciiFile : <span class="c-keyword">public</span> File {
<span class="c-keyword">public</span>:
    AsciiFile(<span class="c-type">std::string</span> name) : File(name) {}

    <span class="c-type">void</span> print() <span class="c-keyword">const</span> <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[ASCII Print]: Streaming plain text characters from '"</span> 
                  &lt;&lt; filename &lt;&lt; <span class="c-string">"' to standard terminal.\\n"</span>;
    }
};

<span class="c-comment">// Concrete Derived Class 2: Binary File</span>
<span class="c-keyword">class</span> BinaryFile : <span class="c-keyword">public</span> File {
<span class="c-keyword">public</span>:
    BinaryFile(<span class="c-type">std::string</span> name) : File(name) {}

    <span class="c-type">void</span> print() <span class="c-keyword">const</span> <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[Binary Print]: Formatting hex bytes [0x4F, 0xA2, 0xFF] from '"</span> 
                  &lt;&lt; filename &lt;&lt; <span class="c-string">"'.\\n"</span>;
    }
};

<span class="c-comment">// Concrete Derived Class 3: Picture File</span>
<span class="c-keyword">class</span> PictureFile : <span class="c-keyword">public</span> File {
<span class="c-keyword">public</span>:
    PictureFile(<span class="c-type">std::string</span> name) : File(name) {}

    <span class="c-type">void</span> print() <span class="c-keyword">const</span> <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[Picture Print]: Rendering raster image pixels (1920x1080 CMYK) from '"</span> 
                  &lt;&lt; filename &lt;&lt; <span class="c-string">"' to laser printer.\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">// Heterogeneous collection of files managed polymorphically via base pointers</span>
    <span class="c-type">std::vector</span>&lt;<span class="c-type">std::unique_ptr</span>&lt;File&gt;&gt; printQueue;
    printQueue.push_back(std::make_unique&lt;AsciiFile&gt;(<span class="c-string">"readme.txt"</span>));
    printQueue.push_back(std::make_unique&lt;BinaryFile&gt;(<span class="c-string">"kernel.bin"</span>));
    printQueue.push_back(std::make_unique&lt;PictureFile&gt;(<span class="c-string">"landscape.png"</span>));

    std::cout &lt;&lt; <span class="c-string">"--- Executing Unified Print Queue ---\\n"</span>;
    <span class="c-comment">// Universal subtyping polymorphism in action:</span>
    <span class="c-keyword">for</span> (<span class="c-keyword">const</span> auto&amp; filePtr : printQueue) {
        filePtr-&gt;print(); <span class="c-comment">// Dynamic dispatch determines the exact method at runtime!</span>
    }

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The File.print() Polymorphic Hierarchy &amp; Dispatch</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="300" fill="#0f172a" rx="12"/>

      <!-- Base Class File -->
      <g transform="translate(305, 20)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="210" height="28" rx="8" fill="#0369a1"/>
        <text x="105" y="19" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">&lt;&lt;abstract&gt;&gt; File</text>
        <text x="15" y="48" fill="#94a3b8" font-size="10"># filename: String</text>
        <line x1="10" y1="56" x2="200" y2="56" stroke="#334155" stroke-width="1"/>
        <text x="15" y="75" fill="#38bdf8" font-size="10" font-weight="bold">+ print(): void = 0</text>
      </g>

      <!-- Inheritance Lines -->
      <line x1="410" y1="115" x2="410" y2="155" stroke="#94a3b8" stroke-width="2"/>
      <line x1="135" y1="155" x2="685" y2="155" stroke="#94a3b8" stroke-width="2"/>

      <line x1="135" y1="155" x2="135" y2="185" stroke="#94a3b8" stroke-width="2"/>
      <line x1="410" y1="155" x2="410" y2="185" stroke="#94a3b8" stroke-width="2"/>
      <line x1="685" y1="155" x2="685" y2="185" stroke="#94a3b8" stroke-width="2"/>

      <polygon points="410,115 403,127 417,127" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>

      <!-- Derived Class 1: AsciiFile -->
      <g transform="translate(30, 185)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="210" height="28" rx="8" fill="#7e22ce"/>
        <text x="105" y="19" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">AsciiFile</text>
        <text x="15" y="48" fill="#94a3b8" font-size="9">charEncoding: UTF8</text>
        <line x1="10" y1="56" x2="200" y2="56" stroke="#334155" stroke-width="1"/>
        <text x="15" y="75" fill="#c084fc" font-size="10" font-weight="bold">+ print(): streamText()</text>
      </g>

      <!-- Derived Class 2: BinaryFile -->
      <g transform="translate(305, 185)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="210" height="28" rx="8" fill="#047857"/>
        <text x="105" y="19" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">BinaryFile</text>
        <text x="15" y="48" fill="#94a3b8" font-size="9">rawBytes: byte[]</text>
        <line x1="10" y1="56" x2="200" y2="56" stroke="#334155" stroke-width="1"/>
        <text x="15" y="75" fill="#6ee7b7" font-size="10" font-weight="bold">+ print(): formatHex()</text>
      </g>

      <!-- Derived Class 3: PictureFile -->
      <g transform="translate(580, 185)">
        <rect width="210" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="210" height="28" rx="8" fill="#b45309"/>
        <text x="105" y="19" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">PictureFile</text>
        <text x="15" y="48" fill="#94a3b8" font-size="9">pixels: CMYKRaster</text>
        <line x1="10" y1="56" x2="200" y2="56" stroke="#334155" stroke-width="1"/>
        <text x="15" y="75" fill="#fcd34d" font-size="10" font-weight="bold">+ print(): rasterize()</text>
      </g>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2012-13, 2014-15):</strong> <em>"What do you mean by polymorphism? Is this concept only applicable to object-oriented systems? Explain with the File.print() example."</em> [5 Marks - Que 1.11]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Answer the applicability question clearly: <strong>No, polymorphism is NOT exclusively applicable to OO systems!</strong> Ad-hoc polymorphism (function overloading and coercion) exists in traditional procedural languages (like C and Pascal). However, <strong>Universal Polymorphism (specifically Subtyping/Dynamic Binding)</strong> is strictly unique to object-oriented systems. Explain <code>File.print()</code> across ASCII, Binary, and Picture files.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Polymorphism:</strong> "Many forms"; same interface executing different behaviors per target class.</li>
    <li><strong>Is it OO-only?</strong> No! Ad-hoc (overloading/coercion) works in non-OO; Universal subtyping requires OO.</li>
    <li><strong>File.print() Example:</strong> ASCII streams text, Binary dumps hex, Picture renders raster pixels.</li>
    <li><strong>Resolution:</strong> Resolved at runtime via dynamic method lookup (VTable in C++).</li>
  </ul>
</div>
"""
        },

        # -------------------------------------------------------------
        # Section 08: Generosity / Genericity
        # -------------------------------------------------------------
        {
            "id": "u1-sec-8",
            "number": "08",
            "part": "Part 2 — Object Identity, Encapsulation & Polymorphism",
            "title": "Generosity / Genericity",
            "subtitle": "Parameterized Types, Generic Classes, Type Safety & Reusable Components",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Advanced Language Feature</div>
    <h3>What is Generosity (Genericity)?</h3>
    <p><strong>Generosity</strong> (more commonly referred to in modern computer science literature as <strong>Genericity</strong> or <strong>Parameterized Types</strong>) is the capability of a programming language to define classes, interfaces, and algorithms parameterized by one or more data types.</p>
    <p>According to Bertrand Meyer (the creator of Eiffel and pioneer of OO design principles referenced in the AKTU syllabus), <strong>Genericity</strong> provides parametric polymorphism, enabling developers to build general-purpose, reusable software components—such as collections, stacks, and queues—without sacrificing compile-time type safety.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Standard Intermodal Shipping Container</div>
  <p>Think of an <strong>intermodal shipping container</strong>. The crane, ship hull, and train flatbed do not care whether the container is filled with 10,000 smart televisions, 50 tons of grain, or vintage automobiles. The container handles hoisting, locking, and transport uniformly. However, when sealed, the cargo inside retains its exact identity. A grain container cannot accidentally mix with a television shipment. Genericity gives you standardized containers (<code>Box&lt;T&gt;</code>) with 100% cargo integrity!</p>
</div>

<div class="subtopics-container">
  <h4>Core Principles of Genericity</h4>

  <div class="detail-block">
    <h5>1. Elimination of Dangerous Void* / Object Casting</h5>
    <p>In languages without genericity, general collections must store untyped pointers (<code>void*</code> in C or raw <code>Object</code> references in Java 1.4). This requires explicit, unsafe downcasting at runtime, leading to catastrophic <code>ClassCastException</code> crashes. Genericity shifts type verification entirely to the compiler.</p>
  </div>

  <div class="detail-block">
    <h5>2. Reusability Without Code Duplication</h5>
    <p>Without genericity, a developer wanting a linked list of integers, a linked list of strings, and a linked list of students would have to write and maintain three separate classes (<code>IntList</code>, <code>StringList</code>, <code>StudentList</code>). With generic programming, one single template <code>List&lt;T&gt;</code> serves all types.</p>
  </div>

  <div class="detail-block">
    <h5>3. Genericity vs Inheritance (Two Complementary Techniques)</h5>
    <p>Bertrand Meyer famously demonstrated that <strong>Inheritance</strong> and <strong>Genericity</strong> are orthogonal mechanisms for software extension:</p>
    <ul>
      <li><strong>Inheritance:</strong> Expresses specialization and variance in behavior (<em>"A Dog is a specialized Animal"</em>).</li>
      <li><strong>Genericity:</strong> Expresses uniformity of structural operations across varied types (<em>"A List can contain Dogs, Integers, or Strings in the exact same container shape"</em>).</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Type Safety Approaches: Untyped Containers vs Generic Templates</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Untyped Pointer (void* / Raw Object)</th>
        <th>Generic / Parameterized Type (Box&lt;T&gt;)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Type Safety</strong></td>
        <td>Zero type safety; compiler cannot detect mismatches</td>
        <td><strong>100% Compile-Time Type Safety</strong></td>
      </tr>
      <tr>
        <td><strong>Runtime Overhead</strong></td>
        <td>Frequent runtime downcasting checks</td>
        <td>Zero runtime penalty (monomorphized in C++ templates)</td>
      </tr>
      <tr>
        <td><strong>Error Detection</strong></td>
        <td>Fails at runtime in production</td>
        <td>Fails immediately during compilation with descriptive errors</td>
      </tr>
      <tr>
        <td><strong>Code Duplication</strong></td>
        <td>None, but completely unsafe</td>
        <td>Single source code parameterized by type <code>&lt;T&gt;</code></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">C++ Demonstration: Generic Parameterized Class Template</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include &lt;iostream&gt;</span>
<span class="c-keyword">#include &lt;string&gt;</span>

<span class="c-comment">// Generic Template Class parameterized by type T</span>
<span class="c-keyword">template</span> &lt;<span class="c-keyword">typename</span> T&gt;
<span class="c-keyword">class</span> StorageVault {
<span class="c-keyword">private</span>:
    T content;
    <span class="c-type">bool</span> hasItem;

<span class="c-keyword">public</span>:
    StorageVault() : hasItem(false) {}

    <span class="c-type">void</span> store(<span class="c-keyword">const</span> T&amp; item) {
        content = item;
        hasItem = true;
    }

    T retrieve() <span class="c-keyword">const</span> {
        <span class="c-keyword">if</span> (!hasItem) {
            <span class="c-keyword">throw</span> std::runtime_error(<span class="c-string">"Vault is empty!"</span>);
        }
        <span class="c-keyword">return</span> content;
    }

    <span class="c-type">void</span> inspect() <span class="c-keyword">const</span> {
        <span class="c-keyword">if</span> (hasItem) {
            std::cout &lt;&lt; <span class="c-string">"[Vault Contents]: "</span> &lt;&lt; content &lt;&lt; <span class="c-string">"\\n"</span>;
        } <span class="c-keyword">else</span> {
            std::cout &lt;&lt; <span class="c-string">"[Vault]: Empty\\n"</span>;
        }
    }
};

<span class="c-keyword">struct</span> StudentRecord {
    <span class="c-type">std::string</span> name;
    <span class="c-type">int</span> rollNo;

    <span class="c-comment">// Stream operator for formatted printing</span>
    <span class="c-keyword">friend</span> std::ostream&amp; <span class="c-keyword">operator</span>&lt;&lt;(std::ostream&amp; os, <span class="c-keyword">const</span> StudentRecord&amp; s) {
        <span class="c-keyword">return</span> os &lt;&lt; <span class="c-string">"Student("</span> &lt;&lt; s.name &lt;&lt; <span class="c-string">", Roll: "</span> &lt;&lt; s.rollNo &lt;&lt; <span class="c-string">")"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. Instantiating vault for primitive integer</span>
    StorageVault&lt;<span class="c-type">int</span>&gt; intVault;
    intVault.store(<span class="c-number">42</span>);
    intVault.inspect();

    <span class="c-comment">// 2. Instantiating vault for std::string</span>
    StorageVault&lt;<span class="c-type">std::string</span>&gt; stringVault;
    stringVault.store(<span class="c-string">"AKTU OOSD Unit 1 Master Notes"</span>);
    stringVault.inspect();

    <span class="c-comment">// 3. Instantiating vault for complex user-defined entity</span>
    StorageVault&lt;StudentRecord&gt; studentVault;
    studentVault.store({<span class="c-string">"Aditya Verma"</span>, <span class="c-number">108</span>});
    studentVault.inspect();

    <span class="c-comment">// Type Mismatch is caught at COMPILE-TIME:</span>
    <span class="c-comment">// intVault.store("Invalid String"); // COMPILER ERROR: cannot convert string to int!</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Generic Type Parameterization Blueprint</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 820 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect width="820" height="280" fill="#0f172a" rx="12"/>

      <!-- Generic Blueprint (Center Top) -->
      <g transform="translate(295, 20)">
        <rect width="230" height="100" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
        <rect width="230" height="28" rx="8" fill="#7e22ce"/>
        <text x="115" y="19" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">GENERIC TEMPLATE &lt;T&gt;</text>
        
        <!-- Parameter Box -->
        <rect x="180" y="-10" width="55" height="22" rx="4" fill="#6d28d9" stroke="#c084fc" stroke-width="1.5" stroke-dasharray="3,2"/>
        <text x="207" y="5" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">&lt;T&gt;</text>

        <text x="15" y="52" fill="#e2e8f0" font-size="10">Class StorageVault&lt;T&gt; {</text>
        <text x="25" y="72" fill="#c084fc" font-size="10">private: T content;</text>
        <text x="25" y="90" fill="#38bdf8" font-size="10">public: void store(T item);</text>
      </g>

      <!-- Instantiation Arrows -->
      <path d="M 330 120 L 160 170" fill="none" stroke="#60a5fa" stroke-width="2" marker-end="url(#u1-gen-arr-blue)"/>
      <path d="M 410 120 L 410 165" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#u1-gen-arr-green)"/>
      <path d="M 490 120 L 660 170" fill="none" stroke="#fbbf24" stroke-width="2" marker-end="url(#u1-gen-arr-yellow)"/>

      <!-- Instance 1: int -->
      <g transform="translate(40, 175)">
        <rect width="220" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <rect width="220" height="26" rx="8" fill="#0284c7"/>
        <text x="110" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">StorageVault&lt;int&gt;</text>
        <text x="15" y="48" fill="#38bdf8" font-size="10" font-weight="bold">• Type Bound: Integer</text>
        <text x="15" y="68" fill="#94a3b8" font-size="9">Safe store/retrieve 32-bit int</text>
      </g>

      <!-- Instance 2: string -->
      <g transform="translate(300, 175)">
        <rect width="220" height="85" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
        <rect width="220" height="26" rx="8" fill="#047857"/>
        <text x="110" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">StorageVault&lt;std::string&gt;</text>
        <text x="15" y="48" fill="#34d399" font-size="10" font-weight="bold">• Type Bound: String</text>
        <text x="15" y="68" fill="#94a3b8" font-size="9">Safe character buffer storage</text>
      </g>

      <!-- Instance 3: Student -->
      <g transform="translate(560, 175)">
        <rect width="220" height="85" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <rect width="220" height="26" rx="8" fill="#b45309"/>
        <text x="110" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">StorageVault&lt;StudentRecord&gt;</text>
        <text x="15" y="48" fill="#fbbf24" font-size="10" font-weight="bold">• Type Bound: User Class</text>
        <text x="15" y="68" fill="#94a3b8" font-size="9">Custom entity type integrity</text>
      </g>

      <defs>
        <marker id="u1-gen-arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
        <marker id="u1-gen-arr-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
        <marker id="u1-gen-arr-yellow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#fbbf24"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Syllabus Note)</div>
  <p><strong>Syllabus Note:</strong> The AKTU syllabus lists <em>"generosity"</em> as a core topic under Unit 1. In academic computer science and classic object-oriented literature (Meyer, OOSC), <strong>generosity</strong> is the synonym for <strong>genericity</strong> (generic classes and templates).</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Write that Generosity / Genericity is parametric polymorphism. Explain that it parameterizes classes with type variables (e.g. <code>template &lt;typename T&gt;</code>), enabling high code reusability without sacrificing compile-time type safety. Contrast it with unsafe <code>void*</code> pointers and compare it with inheritance.
  </div>
</div>

<div class="quick-recall">
  <div class="recall-header">⚡ 30-Second Quick Recall</div>
  <ul>
    <li><strong>Generosity / Genericity:</strong> Parameterizing classes with type arguments (e.g., <code>Box&lt;T&gt;</code>).</li>
    <li><strong>Type Safety:</strong> Prevents dangerous runtime downcasting bugs; catches errors at compile time.</li>
    <li><strong>Reusability:</strong> One template implementation serves unlimited data types.</li>
    <li><strong>Orthogonal to Inheritance:</strong> Genericity handles uniform containers; inheritance handles behavioral specialization.</li>
  </ul>
</div>
"""
        }
    ]
