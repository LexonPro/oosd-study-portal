# -*- coding: utf-8 -*-
"""
generate_unit4_part4.py: Generates Sections 16 to 20 for Unit 4 (C++ Functions)
Topics:
  16. Function Overloading & Compile-Time Polymorphism
  17. Default Arguments & Syntactic Rules
  18. Friend Functions & Inter-Class Architectural Bridges
  19. Virtual Functions & Dynamic Dispatch (VTable/VPtr)
  20. Rules of Virtual Functions, Virtual Destructors & Abstract Classes
"""

def get_unit4_part4_sections():
    sections = []

    # =========================================================================
    # SECTION 16: Function Overloading
    # =========================================================================
    sec16_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">16. Function Overloading &amp; Compile-Time Polymorphism</h3>
  </div>

  <div class="detail-block">
    <h5>16.1 Meaning of Function Overloading</h5>
    <p>
      <strong>Function Overloading</strong> is a powerful C++ feature that allows multiple functions within the same scope to share the exact same identifier (name), provided their formal parameter lists (signatures) are distinct. It represents a fundamental form of <strong>Compile-Time Polymorphism</strong> (static binding or ad-hoc polymorphism), where the compiler determines the appropriate target function at build time with zero runtime dispatch overhead.
    </p>
  </div>

  <div class="detail-block">
    <h5>16.2 Overloading Criteria &amp; Rules</h5>
    <p>Two or more functions sharing the same name are legally overloaded if they differ in at least one of the following dimensions:</p>
    <ul>
      <li><strong>Number of Arguments (Arity):</strong> Functions accept different numbers of parameters (e.g., <code>int area(int r)</code> vs. <code>int area(int l, int w)</code>).</li>
      <li><strong>Data Types of Arguments:</strong> Functions accept identical numbers of parameters, but with differing types (e.g., <code>void print(int val)</code> vs. <code>void print(double val)</code>).</li>
      <li><strong>Sequence / Order of Argument Types:</strong> Functions accept the same types, but in a different order (e.g., <code>void display(int id, string name)</code> vs. <code>void display(string name, int id)</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>16.3 The Return Type Rule (Why Return Type Alone Cannot Overload)</h5>
    <p>
      <strong>Critical Rule:</strong> Functions <strong>CANNOT</strong> be overloaded based solely on differing return types.
    </p>
    <div class="code-box">
      <code>int compute(int x);<br>double compute(int x); // COMPILE ERROR: Cannot overload on return type alone!</code>
    </div>
    <p>
      <strong>Rationale:</strong> At the call site, an expression like <code>compute(10);</code> does not require capturing the return value. In that case, the compiler has zero context to deduce whether the programmer intended to call the <code>int</code> or <code>double</code> version, creating an irreconcilable ambiguity.
    </p>
  </div>

  <div class="detail-block">
    <h5>16.4 Behind the Scenes: Name Mangling (Name Decoration)</h5>
    <p>
      How does the linker resolve multiple functions with identical source names? The C++ compiler applies <strong>Name Mangling (Name Decoration)</strong>. It encodes the function identifier along with its parameter types, namespace, and class scope into a globally unique assembly label. For instance, under the Itanium C++ ABI:
    </p>
    <ul>
      <li><code>print(int)</code> &rarr; mangled to <code>_Z5printi</code></li>
      <li><code>print(double)</code> &rarr; mangled to <code>_Z5printd</code></li>
      <li><code>print(const char*, int)</code> &rarr; mangled to <code>_Z5printPKci</code></li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Multi-Mode Payment Terminal</span>
  </div>
  <p>
    Consider tapping a supermarket payment terminal with the single generic intent: <strong>"Pay()"</strong>.<br>
    - If you present a <strong>Chip Card</strong>, the terminal prompts for a 4-digit PIN.<br>
    - If you present a <strong>Smartphone (NFC)</strong>, the terminal verifies biometric FaceID.<br>
    - If you hand over <strong>Cash Currency</strong>, the cashier inputs banknote denominations.<br>
    The universal action verb is <code>Pay</code>, but the actual procedure carried out depends entirely on the <em>type and nature of payment tokens</em> provided. You do not need distinct buttons labeled <code>PayWithPIN()</code>, <code>PayWithNFC()</code>, and <code>PayWithNotes()</code>.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Exhaustive Function Overloading: Arity, Type & Sequence Disambiguation</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// Overload 1: Single integer parameter</span>
<span class="c-type">void</span> renderData(<span class="c-type">int</span> value) {
    std::cout &lt;&lt; <span class="c-string">"[INT OVERLOAD] Integer Value: "</span> &lt;&lt; value 
              &lt;&lt; <span class="c-string">" (Mangled Symbol: _Z10renderDatai)\\n"</span>;
}

<span class="c-comment">// Overload 2: Single double parameter (Different type)</span>
<span class="c-type">void</span> renderData(<span class="c-type">double</span> value) {
    std::cout &lt;&lt; <span class="c-string">"[DOUBLE OVERLOAD] Floating Precision: "</span> &lt;&lt; value 
              &lt;&lt; <span class="c-string">" (Mangled Symbol: _Z10renderDatad)\\n"</span>;
}

<span class="c-comment">// Overload 3: String and integer parameters (Different arity and types)</span>
<span class="c-type">void</span> renderData(<span class="c-keyword">const</span> <span class="c-type">std::string</span>&amp; label, <span class="c-type">int</span> code) {
    std::cout &lt;&lt; <span class="c-string">"[LABEL-CODE OVERLOAD] "</span> &lt;&lt; label &lt;&lt; <span class="c-string">": Status Code "</span> &lt;&lt; code &lt;&lt; <span class="c-string">"\\n"</span>;
}

<span class="c-comment">// Overload 4: Sequence swapped (Integer first, string second)</span>
<span class="c-type">void</span> renderData(<span class="c-type">int</span> code, <span class="c-keyword">const</span> <span class="c-type">std::string</span>&amp; label) {
    std::cout &lt;&lt; <span class="c-string">"[CODE-LABEL OVERLOAD] Code "</span> &lt;&lt; code &lt;&lt; <span class="c-string">" mapped to "</span> &lt;&lt; label &lt;&lt; <span class="c-string">"\\n"</span>;
}

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Function Overloading Dispatch Demonstration ===\\n"</span>;

    <span class="c-comment">// Compiler inspects argument types at compile-time to bind correct address</span>
    renderData(<span class="c-number">101</span>);                      <span class="c-comment">// Binds to Overload 1</span>
    renderData(<span class="c-number">98.6</span>);                     <span class="c-comment">// Binds to Overload 2</span>
    renderData(<span class="c-string">"HTTP_GATEWAY"</span>, <span class="c-number">200</span>);      <span class="c-comment">// Binds to Overload 3</span>
    renderData(<span class="c-number">404</span>, <span class="c-string">"PAGE_NOT_FOUND"</span>);    <span class="c-comment">// Binds to Overload 4</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Compiler Name Mangling & Linker Symbol Binding</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- C++ Source Definitions -->
      <g transform="translate(30, 20)">
        <rect width="220" height="180" rx="8" fill="var(--bg-elevated)" stroke="var(--border-default)" stroke-width="1.5"/>
        <text x="110" y="30" fill="var(--accent-blue)" font-size="13" font-weight="bold" text-anchor="middle">C++ Source Identifier</text>
        <rect x="15" y="45" width="190" height="32" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="66" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">renderData(int)</text>
        <rect x="15" y="87" width="190" height="32" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="108" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">renderData(double)</text>
        <rect x="15" y="129" width="190" height="32" rx="4" fill="var(--bg-card)"/>
        <text x="110" y="150" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">renderData(string, int)</text>
      </g>

      <!-- Compiler Pipeline Transformation -->
      <g transform="translate(280, 70)">
        <rect width="180" height="80" rx="8" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="1.5"/>
        <text x="90" y="35" fill="#a5b4fc" font-size="12" font-weight="bold" text-anchor="middle">Compiler Front-End</text>
        <text x="90" y="55" fill="#38bdf8" font-size="10" font-family="monospace" text-anchor="middle">Name Mangler (ABI)</text>
        <!-- Connector Arrows -->
        <path d="M -25 20 L -2 30" stroke="#6366f1" stroke-width="1.5" fill="none"/>
        <path d="M -25 40 L -2 40" stroke="#6366f1" stroke-width="1.5" fill="none"/>
        <path d="M -25 60 L -2 50" stroke="#6366f1" stroke-width="1.5" fill="none"/>
        <path d="M 182 40 L 218 40" stroke="#10b981" stroke-width="2" fill="none"/>
      </g>

      <!-- Mangled Symbol Table (Linker) -->
      <g transform="translate(505, 20)">
        <rect width="225" height="180" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="1.5"/>
        <text x="112" y="30" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Linker Object Symbols</text>
        <rect x="15" y="45" width="195" height="32" rx="4" fill="var(--bg-card)"/>
        <text x="112" y="66" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">_Z10renderDatai</text>
        <rect x="15" y="87" width="195" height="32" rx="4" fill="var(--bg-card)"/>
        <text x="112" y="108" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">_Z10renderDatad</text>
        <rect x="15" y="129" width="195" height="32" rx="4" fill="var(--bg-card)"/>
        <text x="112" y="150" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">_Z10renderDataNSt7__cxx11i</text>
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
        <th>Feature / Dimension</th>
        <th>Function Overloading</th>
        <th>Function Overriding</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Scope of Declaration</strong></td>
        <td>Within the <strong>same class</strong> or enclosing namespace.</td>
        <td>Across a <strong>Base class and Derived class</strong> hierarchy.</td>
      </tr>
      <tr>
        <td><strong>Function Signature</strong></td>
        <td><strong>Must differ</strong> in arity, argument types, or sequence.</td>
        <td><strong>Must be strictly identical</strong> (name and parameters).</td>
      </tr>
      <tr>
        <td><strong>Binding Mechanism</strong></td>
        <td><strong>Compile-Time (Early / Static Binding)</strong> via Name Mangling.</td>
        <td><strong>Run-Time (Late / Dynamic Binding)</strong> via VTable/VPtr.</td>
      </tr>
      <tr>
        <td><strong>Keyword Requirement</strong></td>
        <td>No special keyword required.</td>
        <td>Requires <code>virtual</code> in Base and optional <code>override</code> in Derived.</td>
      </tr>
      <tr>
        <td><strong>Return Type Flexibility</strong></td>
        <td>Can be different, but cannot be the <em>sole</em> distinction.</td>
        <td>Must match identically (or follow covariant pointer/ref rules).</td>
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
    <li><span class="check-box"></span> What are the 3 valid criteria for overloading a function in C++?</li>
    <li><span class="check-box"></span> Why does changing only the return type produce a compile-time error?</li>
    <li><span class="check-box"></span> Explain how compiler Name Mangling prevents symbol collisions in object files.</li>
    <li><span class="check-box"></span> List at least 4 key differences between function overloading and function overriding.</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Quantum highlights the question: <em>"Can return type be used to overload a function? Justify with an example."</em> Always answer <strong>NO</strong> and provide the <code>compute(10);</code> ambiguity example showing the compiler cannot infer return intent without an assignment target.
</div>
"""
    sections.append({
        "id": "u4-sec-16",
        "number": 16,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "16. Function Overloading & Compile-Time Polymorphism",
        "subtitle": "Arity, Type Signatures, Ordering Rules, Return Type Constraints & Name Mangling Architecture",
        "content": sec16_content
    })

    # =========================================================================
    # SECTION 17: Default Arguments
    # =========================================================================
    sec17_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">17. Default Arguments &amp; Syntactic Binding Rules</h3>
  </div>

  <div class="detail-block">
    <h5>17.1 Meaning and Purpose of Default Arguments</h5>
    <p>
      A <strong>Default Argument</strong> is a fallback value assigned to a function parameter in its declaration. If the caller does not supply an actual argument for that parameter during an invocation, the compiler automatically substitutes the pre-configured default value. This eliminates boilerplate code and reduces the need for creating numerous trivial overloaded functions.
    </p>
  </div>

  <div class="detail-block">
    <h5>17.2 The Strict Right-to-Left (Trailing) Assignment Rule</h5>
    <p>
      In C++, default arguments <strong>must be assigned strictly from right to left</strong>. Once a parameter is given a default value, every subsequent parameter appearing to its right in the parameter list must also have a default value:
    </p>
    <ul>
      <li><strong style="color: #10b981;">&check; VALID:</strong> <code>void drawBox(int width, int height = 100, int depth = 50);</code></li>
      <li><strong style="color: #10b981;">&check; VALID:</strong> <code>void logEvent(string msg, int severity = 1, bool sendAlert = false);</code></li>
      <li><strong style="color: #ef4444;">&cross; ILLEGAL:</strong> <code>void drawBox(int width = 50, int height, int depth = 100); // Compile Error!</code></li>
    </ul>
    <p>
      <strong>Reasoning:</strong> C++ matches actual arguments to formal parameters positionally from left to right. If a middle parameter could have a default while a right-side parameter remained mandatory, the compiler would have no way to determine which parameter an omitted argument was meant to correspond to.
    </p>
  </div>

  <div class="detail-block">
    <h5>17.3 Declaration vs. Definition Constraint</h5>
    <p>
      Default arguments should be specified in the <strong>function prototype (declaration)</strong>, typically inside header files, and <strong>must NOT be repeated in the function definition</strong>. Repeating default values in both the declaration and definition produces a <em>"redefinition of default argument"</em> compiler error.
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Coffee Shop Standard Order</span>
  </div>
  <p>
    When ordering coffee at a café, you might simply say: <em>"One Latte, please."</em><br>
    The barista serves you with standard presets: <code>milk = RegularCowMilk</code>, <code>sugar = 0 packets</code>, <code>size = Medium</code>.<br>
    However, if you explicitly specify <em>"One Latte with Oat Milk and 2 Sugars"</em>, your explicit arguments override the defaults.<br>
    Notice you cannot say <em>"Give me with 2 sugars"</em> without first stating the primary beverage; essential base arguments must always come first!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Default Arguments: Prototype Definition, Multi-Arity Calls & Ambiguity Prevention</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;iomanip&gt;</span>

<span class="c-comment">// 1. FUNCTION PROTOTYPE: Default values specified HERE (Right-to-Left)</span>
<span class="c-type">double</span> computeLoanInterest(<span class="c-type">double</span> principal, <span class="c-type">int</span> tenureMonths = <span class="c-number">12</span>, <span class="c-type">double</span> annualRate = <span class="c-number">8.5</span>);

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; std::fixed &lt;&lt; std::setprecision(<span class="c-number">2</span>);
    std::cout &lt;&lt; <span class="c-string">"=== Default Argument Invocations ===\\n"</span>;

    <span class="c-comment">// Call Case A: All defaults utilized (tenureMonths = 12, annualRate = 8.5%)</span>
    <span class="c-type">double</span> intA = computeLoanInterest(<span class="c-number">100000.0</span>);
    std::cout &lt;&lt; <span class="c-string">"1. Default 12M @ 8.5%:  Rs. "</span> &lt;&lt; intA &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Call Case B: Override tenureMonths to 36; annualRate remains default 8.5%</span>
    <span class="c-type">double</span> intB = computeLoanInterest(<span class="c-number">100000.0</span>, <span class="c-number">36</span>);
    std::cout &lt;&lt; <span class="c-string">"2. Custom 36M @ 8.5%:   Rs. "</span> &lt;&lt; intB &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Call Case C: Override both optional arguments (tenureMonths = 60, annualRate = 10.2%)</span>
    <span class="c-type">double</span> intC = computeLoanInterest(<span class="c-number">100000.0</span>, <span class="c-number">60</span>, <span class="c-number">10.2</span>);
    std::cout &lt;&lt; <span class="c-string">"3. Custom 60M @ 10.2%:  Rs. "</span> &lt;&lt; intC &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}

<span class="c-comment">// 2. FUNCTION DEFINITION: Notice default values are NOT repeated here!</span>
<span class="c-type">double</span> computeLoanInterest(<span class="c-type">double</span> principal, <span class="c-type">int</span> tenureMonths, <span class="c-type">double</span> annualRate) {
    <span class="c-type">double</span> years = tenureMonths / <span class="c-number">12.0</span>;
    <span class="c-keyword">return</span> (principal * annualRate * years) / <span class="c-number">100.0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Argument Matching & Default Parameter Binding</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Prototype Slots -->
      <g transform="translate(40, 25)">
        <rect width="680" height="60" rx="8" fill="var(--bg-elevated)" stroke="var(--border-default)" stroke-width="1.5"/>
        <text x="20" y="35" fill="var(--accent-blue)" font-size="12" font-weight="bold">Prototype:</text>
        <rect x="110" y="15" width="160" height="30" rx="4" fill="var(--bg-card)" stroke="var(--border-default)"/>
        <text x="190" y="35" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">double principal</text>
        <rect x="290" y="15" width="180" height="30" rx="4" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1"/>
        <text x="380" y="35" fill="#a5b4fc" font-family="monospace" font-size="11" text-anchor="middle">int tenure = 12</text>
        <rect x="490" y="15" width="180" height="30" rx="4" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1"/>
        <text x="580" y="35" fill="#a5b4fc" font-family="monospace" font-size="11" text-anchor="middle">double rate = 8.5</text>
      </g>

      <!-- Call Site Example -->
      <g transform="translate(40, 115)">
        <rect width="680" height="70" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="20" y="40" fill="#10b981" font-size="12" font-weight="bold">Call Site:</text>
        <text x="110" y="40" fill="#10b981" font-family="monospace" font-size="13">computeLoanInterest(100000.0, 36);</text>

        <!-- Dynamic Arrows -->
        <path d="M 330 -10 L 330 15" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
        <text x="380" y="85" fill="#10b981" font-size="11">Slot 1 &amp; 2 Supplied</text>
        <text x="580" y="85" fill="#f59e0b" font-size="11">Slot 3 Auto-Defaulted (8.5)</text>
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
    <li><span class="check-box"></span> What is the Right-to-Left rule for default arguments in C++?</li>
    <li><span class="check-box"></span> Why must default arguments NOT be repeated in the function definition?</li>
    <li><span class="check-box"></span> How can combining default arguments with function overloading cause call ambiguity?</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Watch out for the famous ambiguity trap:
  <code>void print(int x);</code> and <code>void print(int x, int y = 10);</code>. Calling <code>print(5);</code> causes a compiler error because the compiler cannot determine whether to invoke the single-argument version or the two-argument version with its default value.
</div>
"""
    sections.append({
        "id": "u4-sec-17",
        "number": 17,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "17. Default Arguments & Syntactic Binding Rules",
        "subtitle": "Trailing Parameter Assignment, The Right-to-Left Principle, Prototype vs Definition & Overload Ambiguities",
        "content": sec17_content
    })

    # =========================================================================
    # SECTION 18: Friend Functions
    # =========================================================================
    sec18_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">18. Friend Functions &amp; Inter-Class Architectural Bridges</h3>
  </div>

  <div class="detail-block">
    <h5>18.1 Meaning and Architectural Necessity</h5>
    <p>
      In pure OOP, a class's <code>private</code> and <code>protected</code> data members are inaccessible to external non-member functions. However, specific design scenarios (e.g., operator overloading like <code>cin &gt;&gt; obj</code>, matrix multiplication between distinct representations, or calculating distance between geometrical coordinate classes) require an external function to inspect private state without exposing internal fields to the public API.
    </p>
    <p>
      A <strong>Friend Function</strong> is an external non-member function granted explicit permission to access the <code>private</code> and <code>protected</code> members of a class through the <code>friend</code> declaration inside the class body.
    </p>
  </div>

  <div class="detail-block">
    <h5>18.2 Characteristics &amp; Special Rules of Friend Functions</h5>
    <ul>
      <li><strong>Non-Member Status:</strong> A friend function is <em>not</em> a member of the class that declares it. It has global or namespace scope.</li>
      <li><strong>Invocation Syntax:</strong> It is invoked like a regular standalone function (e.g., <code>compareVal(a, b);</code>) and <strong>never</strong> with an object dot operator (<code>a.compareVal(b); // ERROR</code>).</li>
      <li><strong>No <code>this</code> Pointer:</strong> Because it is not a member function, it receives no implicit <code>this</code> pointer. It must access members through explicitly passed object arguments (e.g., <code>obj.dataMember</code>).</li>
      <li><strong>Placement Invariance:</strong> Declaring a friend inside <code>public:</code>, <code>private:</code>, or <code>protected:</code> sections has identical meaning and effect.</li>
      <li><strong>Friendship is Asymmetric:</strong> If Class A grants friendship to Class B, Class B can access Class A's private members, but Class A cannot access Class B's private members unless reciprocated.</li>
      <li><strong>Friendship is NOT Transitive or Inherited:</strong> If A is friends with B, and B is friends with C, A is not automatically friends with C. Derived classes do not inherit friend status from their base classes.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Certified External Financial Auditor</span>
  </div>
  <p>
    Imagine two rival corporations: Alpha Corp and Beta Enterprises. Neither allows the other to inspect its private financial ledgers and bank balances. However, during a joint merger, both corporations retain a <strong>Certified External Auditor</strong>.<br>
    Both companies sign a legal board resolution (the <code>friend</code> declaration): <em>"We authorize this external auditor to inspect our private balance sheets."</em><br>
    The auditor is not an employee of Alpha nor Beta; they remain an independent third-party, but hold privileged access to bridge the gap and compare both private records.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Inter-Class Friend Function Bridge with Forward Declaration</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// 1. FORWARD DECLARATION: Required because Class Alpha references Class Beta</span>
<span class="c-keyword">class</span> <span class="c-type">ClassBeta</span>;

<span class="c-keyword">class</span> <span class="c-type">ClassAlpha</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> companyName;
    <span class="c-type">double</span> revenueMillions;

<span class="c-keyword">public</span>:
    <span class="c-type">ClassAlpha</span>(<span class="c-type">std::string</span> name, <span class="c-type">double</span> rev) : companyName(name), revenueMillions(rev) {}

    <span class="c-comment">// Declare friend bridge function</span>
    <span class="c-keyword">friend</span> <span class="c-type">void</span> compareRevenues(<span class="c-keyword">const</span> <span class="c-type">ClassAlpha</span>&amp; a, <span class="c-keyword">const</span> <span class="c-type">ClassBeta</span>&amp; b);
};

<span class="c-keyword">class</span> <span class="c-type">ClassBeta</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> companyName;
    <span class="c-type">double</span> revenueMillions;

<span class="c-keyword">public</span>:
    <span class="c-type">ClassBeta</span>(<span class="c-type">std::string</span> name, <span class="c-type">double</span> rev) : companyName(name), revenueMillions(rev) {}

    <span class="c-comment">// Declare the SAME friend bridge function</span>
    <span class="c-keyword">friend</span> <span class="c-type">void</span> compareRevenues(<span class="c-keyword">const</span> <span class="c-type">ClassAlpha</span>&amp; a, <span class="c-keyword">const</span> <span class="c-type">ClassBeta</span>&amp; b);
};

<span class="c-comment">// 2. GLOBAL FRIEND FUNCTION DEFINITION: Accesses private members of BOTH classes</span>
<span class="c-type">void</span> compareRevenues(<span class="c-keyword">const</span> <span class="c-type">ClassAlpha</span>&amp; a, <span class="c-keyword">const</span> <span class="c-type">ClassBeta</span>&amp; b) {
    std::cout &lt;&lt; <span class="c-string">"=== Auditor Joint Evaluation Report ===\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Entity 1: "</span> &lt;&lt; a.companyName &lt;&lt; <span class="c-string">" | Revenue: $"</span> &lt;&lt; a.revenueMillions &lt;&lt; <span class="c-string">"M\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Entity 2: "</span> &lt;&lt; b.companyName &lt;&lt; <span class="c-string">" | Revenue: $"</span> &lt;&lt; b.revenueMillions &lt;&lt; <span class="c-string">"M\\n"</span>;

    <span class="c-keyword">if</span> (a.revenueMillions &gt; b.revenueMillions) {
        std::cout &lt;&lt; <span class="c-string">"&gt;&gt; "</span> &lt;&lt; a.companyName &lt;&lt; <span class="c-string">" leads by $"</span> 
                  &lt;&lt; (a.revenueMillions - b.revenueMillions) &lt;&lt; <span class="c-string">"M\\n"</span>;
    } <span class="c-keyword">else</span> <span class="c-keyword">if</span> (b.revenueMillions &gt; a.revenueMillions) {
        std::cout &lt;&lt; <span class="c-string">"&gt;&gt; "</span> &lt;&lt; b.companyName &lt;&lt; <span class="c-string">" leads by $"</span> 
                  &lt;&lt; (b.revenueMillions - a.revenueMillions) &lt;&lt; <span class="c-string">"M\\n"</span>;
    } <span class="c-keyword">else</span> {
        std::cout &lt;&lt; <span class="c-string">"&gt;&gt; Both entities report identical revenues.\\n"</span>;
    }
}

<span class="c-type">int</span> main() {
    <span class="c-type">ClassAlpha</span> firm1(<span class="c-string">"OmniTech"</span>, <span class="c-number">450.75</span>);
    <span class="c-type">ClassBeta</span> firm2(<span class="c-string">"CyberDyne"</span>, <span class="c-number">620.30</span>);

    <span class="c-comment">// Invoked as a standard standalone function</span>
    compareRevenues(firm1, firm2);

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Friend Function as a Secure Inter-Class Bridge</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Class A Box -->
      <g transform="translate(30, 20)">
        <rect width="210" height="170" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="105" y="30" fill="#ef4444" font-size="13" font-weight="bold" text-anchor="middle">Class Alpha</text>
        <rect x="15" y="45" width="180" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="105" y="65" fill="var(--text-secondary)" font-family="monospace" font-size="11" text-anchor="middle">private: double revA</text>
        <rect x="15" y="85" width="180" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="105" y="105" fill="var(--accent-blue)" font-size="10" text-anchor="middle">friend compareRevenues()</text>
      </g>

      <!-- Central Friend Bridge Node -->
      <g transform="translate(295, 55)">
        <circle cx="85" cy="50" r="48" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2"/>
        <text x="85" y="45" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">FRIEND BRIDGE</text>
        <text x="85" y="62" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">compareRevenues()</text>
        <!-- Bi-directional arrows -->
        <path d="M 37 50 L -55 50" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2"/>
        <path d="M 133 50 L 225 50" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2"/>
      </g>

      <!-- Class B Box -->
      <g transform="translate(520, 20)">
        <rect width="210" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="105" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Class Beta</text>
        <rect x="15" y="45" width="180" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="105" y="65" fill="var(--text-secondary)" font-family="monospace" font-size="11" text-anchor="middle">private: double revB</text>
        <rect x="15" y="85" width="180" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="105" y="105" fill="var(--accent-blue)" font-size="10" text-anchor="middle">friend compareRevenues()</text>
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
    <li><span class="check-box"></span> Why does a friend function not have a <code>this</code> pointer?</li>
    <li><span class="check-box"></span> Why is a forward declaration required when writing a friend function bridging two classes?</li>
    <li><span class="check-box"></span> Does friendship transfer across class inheritance? (No, friendship is not inherited).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> AKTU consistently asks: <em>"Write a program to find the maximum of two numbers belonging to two different classes using a friend function."</em> The code above directly solves this 10-mark question with full formatting and forward declaration.
</div>
"""
    sections.append({
        "id": "u4-sec-18",
        "number": 18,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "18. Friend Functions & Inter-Class Architectural Bridges",
        "subtitle": "Encapsulation Bridges, Forward Declarations, Non-Member Characteristics & Multi-Class Privilege Sharing",
        "content": sec18_content
    })

    # =========================================================================
    # SECTION 19: Virtual Functions
    # =========================================================================
    sec19_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">19. Virtual Functions &amp; Dynamic Dispatch (VTable/VPtr Mechanics)</h3>
  </div>

  <div class="detail-block">
    <h5>19.1 The Need for Run-Time Polymorphism (Late Binding)</h5>
    <p>
      In C++, when a member function is called through a base class pointer or reference, the compiler typically uses <strong>Early Binding (Static Binding)</strong>: it looks solely at the declared static type of the pointer, ignoring the actual object residing at that memory location.
    </p>
    <p>
      Marking a member function with the <code>virtual</code> keyword in the base class instructs the compiler to defer resolution to <strong>Run-Time (Late Binding / Dynamic Binding)</strong>. The program inspects the actual object type at execution time and dynamically dispatches execution to its overridden derived implementation.
    </p>
  </div>

  <div class="detail-block">
    <h5>19.2 The VTable &amp; VPtr Internal Architecture</h5>
    <p>Dynamic dispatch is orchestrated by two low-level mechanisms:</p>
    <ul>
      <li><strong>Virtual Table (VTable):</strong> An internal array of function pointers constructed per-class by the compiler for any class containing at least one virtual function. Each entry holds the memory address of the most-derived implementation of a virtual method.</li>
      <li><strong>Virtual Pointer (VPtr):</strong> A hidden pointer automatically added as the first field of every polymorphic object instance (occupying 8 bytes on 64-bit architectures). During object construction, the object's <code>vptr</code> is initialized to point to that class's <code>vtable</code>.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>19.3 The C++11 override Specifier</h5>
    <p>
      Modern C++ provides the <code>override</code> contextual keyword. Appending <code>override</code> to a derived class member function declaration tells the compiler to verify that the base class contains an identical virtual signature. This eliminates insidious bugs caused by signature typos (e.g., mismatched <code>const</code> or argument types).
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Universal Flight Simulator Cockpit</span>
  </div>
  <p>
    Imagine an advanced flight simulator training cockpit equipped with a universal throttle lever labeled <strong>"EngagePropulsion()"</strong>.<br>
    - When docked to a <strong>Cessna Propeller Simulator</strong>, moving the throttle injects fuel into a reciprocating piston engine.<br>
    - When docked to a <strong>Jet Fighter Simulator</strong>, the exact same lever movement ignites twin afterburning turbofans.<br>
    The pilot's controls (the Base Class pointer) remain identical, but the actual simulation model loaded (the Derived object) dynamically determines the propulsion physics executed.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Polymorphic Base Pointer Dispatch with VTable and Non-Virtual Early Binding Comparison</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">public</span>:
    <span class="c-comment">// 1. VIRTUAL FUNCTION: Enables dynamic dispatch via vtable lookup</span>
    <span class="c-keyword">virtual</span> <span class="c-type">void</span> startIgnition() {
        std::cout &lt;&lt; <span class="c-string">"[Base Vehicle] Starting generic mechanical ignition.\\n"</span>;
    }

    <span class="c-comment">// 2. NON-VIRTUAL FUNCTION: Binds statically at compile-time</span>
    <span class="c-type">void</span> honk() {
        std::cout &lt;&lt; <span class="c-string">"[Base Vehicle] Generic acoustic horn sound.\\n"</span>;
    }

    <span class="c-comment">// 3. VIRTUAL DESTRUCTOR: Crucial for safe polymorphic cleanup</span>
    <span class="c-keyword">virtual</span> ~<span class="c-type">Vehicle</span>() {
        std::cout &lt;&lt; <span class="c-string">"[Base Vehicle] Destructor invoked.\\n"</span>;
    }
};

<span class="c-keyword">class</span> <span class="c-type">Supercar</span> : <span class="c-keyword">public</span> <span class="c-type">Vehicle</span> {
<span class="c-keyword">public</span>:
    <span class="c-type">void</span> startIgnition() <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[Supercar] V12 Twin-Turbo engine ROARS to life!\\n"</span>;
    }

    <span class="c-comment">// Hiding base function, NOT overriding (since base was non-virtual)</span>
    <span class="c-type">void</span> honk() {
        std::cout &lt;&lt; <span class="c-string">"[Supercar] Loud dual-frequency sport blast!\\n"</span>;
    }

    ~<span class="c-type">Supercar</span>() <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[Supercar] Turbochargers cooled and shut down.\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Dynamic Binding vs Static Binding Test ===\\n"</span>;

    <span class="c-comment">// Base pointer referencing derived heap instance</span>
    <span class="c-type">Vehicle</span>* vPtr = <span class="c-keyword">new</span> <span class="c-type">Supercar</span>();

    <span class="c-comment">// DYNAMIC BINDING: Inspects Supercar's vtable -&gt; calls Supercar::startIgnition()</span>
    vPtr-&gt;startIgnition();

    <span class="c-comment">// STATIC BINDING: Bound at compile-time to Vehicle::honk() because non-virtual!</span>
    vPtr-&gt;honk();

    std::cout &lt;&lt; <span class="c-string">"\\nInitiating Polymorphic Destruction:\\n"</span>;
    <span class="c-keyword">delete</span> vPtr; <span class="c-comment">// Safely invokes Supercar destructor first due to virtual ~Vehicle()</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Object Memory Layout (VPtr) &amp; Class VTable Dispatch</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 230" width="100%" height="230" xmlns="http://www.w3.org/2000/svg">
      <!-- Base Pointer -->
      <g transform="translate(30, 40)">
        <rect width="140" height="70" rx="8" fill="var(--bg-elevated)" stroke="var(--border-default)" stroke-width="1.5"/>
        <text x="70" y="30" fill="var(--accent-blue)" font-size="12" font-weight="bold" text-anchor="middle">Base Pointer</text>
        <rect x="15" y="40" width="110" height="20" rx="4" fill="var(--bg-card)"/>
        <text x="70" y="55" fill="var(--text-secondary)" font-family="monospace" font-size="10" text-anchor="middle">Vehicle* vPtr</text>
      </g>

      <!-- Supercar Instance Memory Layout -->
      <g transform="translate(230, 20)">
        <rect width="210" height="180" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="2"/>
        <text x="105" y="30" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Heap: Supercar Instance</text>
        <rect x="15" y="45" width="180" height="35" rx="4" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981"/>
        <text x="105" y="67" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">__vptr (8 Bytes)</text>
        <rect x="15" y="90" width="180" height="30" rx="4" fill="var(--bg-elevated)"/>
        <text x="105" y="110" fill="var(--text-primary)" font-size="10" text-anchor="middle">Derived Data Members</text>
      </g>

      <!-- VTable Array (.rodata) -->
      <g transform="translate(500, 20)">
        <rect width="220" height="180" rx="8" fill="var(--bg-elevated)" stroke="#6366f1" stroke-width="2"/>
        <text x="110" y="30" fill="#a5b4fc" font-size="13" font-weight="bold" text-anchor="middle">Supercar VTable (.rodata)</text>
        <rect x="15" y="45" width="190" height="35" rx="4" fill="var(--bg-card)" stroke="var(--border-default)"/>
        <text x="105" y="67" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">&amp;Supercar::startIgnition()</text>
        <rect x="15" y="90" width="190" height="35" rx="4" fill="var(--bg-card)" stroke="var(--border-default)"/>
        <text x="105" y="112" fill="var(--text-primary)" font-family="monospace" font-size="10" text-anchor="middle">&amp;Supercar::~Supercar()</text>
      </g>

      <!-- Pointer Lines -->
      <path d="M 170 75 L 230 75" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowhead)"/>
      <path d="M 425 65 L 500 65" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
    </svg>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> Distinguish between Early (Static) Binding and Late (Dynamic) Binding.</li>
    <li><span class="check-box"></span> What is the role of the <code>__vptr</code> inside a polymorphic object?</li>
    <li><span class="check-box"></span> What happens when a non-virtual function is called through a base class pointer?</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When explaining virtual functions, always sketch the <strong>VTable and VPtr diagram</strong> shown above. AKTU examiners reward full marks to students who demonstrate that <code>vptr</code> points to the class's table of function pointers.
</div>
"""
    sections.append({
        "id": "u4-sec-19",
        "number": 19,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "19. Virtual Functions & Dynamic Dispatch (VTable/VPtr Mechanics)",
        "subtitle": "Late Binding, Base Pointer Polymorphic Dispatch, Virtual Method Tables & Internal Memory Layout",
        "content": sec19_content
    })

    # =========================================================================
    # SECTION 20: Rules of Virtual Functions
    # =========================================================================
    sec20_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">20. Rules of Virtual Functions, Virtual Destructors &amp; Abstract Interfaces</h3>
  </div>

  <div class="detail-block">
    <h5>20.1 The 7 Rigorous Rules of Virtual Functions</h5>
    <p>Examiners routinely ask for the fundamental rules governing virtual functions in C++:</p>
    <ol class="styled-list">
      <li><strong>Class Member Requirement:</strong> Virtual functions must be members of a class; they cannot be standalone global functions or declared as a <code>friend</code> to another class.</li>
      <li><strong>Cannot be Static:</strong> Static member functions belong to the class itself and lack a <code>this</code> pointer. Because virtual dispatch relies on an object's runtime <code>vptr</code>, a static virtual function is an architectural impossibility.</li>
      <li><strong>Accessed via Pointer or Reference:</strong> Dynamic polymorphism only activates when invoked via a <strong>Base pointer</strong> (<code>Base*</code>) or <strong>Base reference</strong> (<code>Base&amp;</code>). Calling on value objects triggers <em>Object Slicing</em> and executes static binding.</li>
      <li><strong>Identical Prototypes:</strong> Overriding functions in derived classes must share the exact same signature (name, parameter types, and return type, excluding covariant pointer returns).</li>
      <li><strong>Constructors CANNOT be Virtual:</strong> An object's concrete type must be fully known at compile time to construct its memory layout. Furthermore, the <code>vptr</code> is initialized inside the constructor; dynamic dispatch cannot function before construction completes.</li>
      <li><strong>Destructors SHOULD be Virtual:</strong> If a class contains any virtual function, its destructor must be declared virtual to ensure proper cleanup when deleting derived objects via base pointers.</li>
      <li><strong>Inherited Virtuality:</strong> Once declared <code>virtual</code> in a base class, a function remains virtual across all levels of derived classes, even if the <code>virtual</code> keyword is omitted in derived declarations.</li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>20.2 The Virtual Destructor Imperative</h5>
    <p>
      If a derived class allocates heap memory and is deleted through a <code>Base*</code> pointer with a <strong>non-virtual destructor</strong>:
    </p>
    <div class="code-box">
      <code>Base* b = new Derived();<br>delete b; // FATAL: Only ~Base() runs; ~Derived() is bypassed &rarr; HEAP LEAK!</code>
    </div>
    <p>
      Declaring <code>virtual ~Base()</code> ensures the destructor call dynamically resolves to <code>~Derived()</code> first, reclaiming derived heap buffers before automatically executing <code>~Base()</code>.
    </p>
  </div>

  <div class="detail-block">
    <h5>20.3 Pure Virtual Functions &amp; Abstract Base Classes</h5>
    <p>
      A <strong>Pure Virtual Function</strong> is declared with the pure specifier <code>= 0</code>:
    </p>
    <div class="code-box">
      <code>virtual void render() = 0; // Pure virtual function</code>
    </div>
    <p>
      Any class containing at least one pure virtual function becomes an <strong>Abstract Base Class (ABC)</strong>:
    </p>
    <ul>
      <li>Cannot be instantiated directly (e.g., <code>Shape s; // COMPILE ERROR</code>).</li>
      <li>Pointers and references to abstract classes are completely legal and form polymorphic interfaces (<code>Shape* s = new Circle();</code>).</li>
      <li>Forces all concrete derived classes to implement every pure virtual method.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Demolition Protocol</span>
  </div>
  <p>
    Imagine hiring a General Demolition Crew (Base Class) to tear down a high-security research facility containing a specialized subterranean hazardous materials lab (Derived Class).<br>
    If the demolition permit only directs the generic building crew (<strong>non-virtual destructor</strong>), the workers demolish the concrete structure above but leave hazardous waste buried and leaking in the soil.<br>
    A <strong>Virtual Destructor</strong> guarantees that before the generic bulldozers strike, the specialized hazmat decontamination team is summoned first to safely dismantle the basement reactors, followed by full site teardown!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Abstract Base Class, Pure Virtual Functions & Safe Virtual Destructor Teardown</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;cstring&gt;</span>

<span class="c-comment">// 1. ABSTRACT BASE CLASS: Defines an uninstantiable hardware contract</span>
<span class="c-keyword">class</span> <span class="c-type">DisplaySurface</span> {
<span class="c-keyword">public</span>:
    <span class="c-comment">// Pure Virtual Function: Mandates concrete implementation in derived classes</span>
    <span class="c-keyword">virtual</span> <span class="c-type">void</span> renderFrame(<span class="c-keyword">const</span> <span class="c-type">char</span>* frameData) = <span class="c-number">0</span>;

    <span class="c-comment">// VIRTUAL DESTRUCTOR: Ensures derived resources are cleanly freed</span>
    <span class="c-keyword">virtual</span> ~<span class="c-type">DisplaySurface</span>() {
        std::cout &lt;&lt; <span class="c-string">"[Base DisplaySurface] Primary bus disconnected.\\n"</span>;
    }
};

<span class="c-comment">// 2. CONCRETE DERIVED CLASS: Implements pure virtual interface</span>
<span class="c-keyword">class</span> <span class="c-type">OledDisplay</span> : <span class="c-keyword">public</span> <span class="c-type">DisplaySurface</span> {
<span class="c-keyword">private</span>:
    <span class="c-type">char</span>* pixelBuffer; <span class="c-comment">// Heap resource requiring cleanup!</span>

<span class="c-keyword">public</span>:
    <span class="c-type">OledDisplay</span>() {
        pixelBuffer = <span class="c-keyword">new</span> <span class="c-type">char</span>[<span class="c-number">512</span>];
        std::strcpy(pixelBuffer, <span class="c-string">"4K Ultra-HD OLED Matrix Buffer"</span>);
        std::cout &lt;&lt; <span class="c-string">"[OledDisplay] Allocated 512 bytes hardware VRAM.\\n"</span>;
    }

    <span class="c-type">void</span> renderFrame(<span class="c-keyword">const</span> <span class="c-type">char</span>* frameData) <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[OledDisplay] Rendering '"</span> &lt;&lt; frameData 
                  &lt;&lt; <span class="c-string">"' through "</span> &lt;&lt; pixelBuffer &lt;&lt; <span class="c-string">"\\n"</span>;
    }

    ~<span class="c-type">OledDisplay</span>() <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[OledDisplay] Deallocating 512 bytes VRAM...\\n"</span>;
        <span class="c-keyword">delete</span>[] pixelBuffer; <span class="c-comment">// Prevent memory leak</span>
    }
};

<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"=== Pure Virtual Function &amp; Virtual Destructor Test ===\\n"</span>;

    <span class="c-comment">// DisplaySurface surf; // COMPILE ERROR: Cannot instantiate abstract class</span>

    <span class="c-comment">// Polymorphic pointer managing derived instance</span>
    <span class="c-type">DisplaySurface</span>* display = <span class="c-keyword">new</span> <span class="c-type">OledDisplay</span>();

    display-&gt;renderFrame(<span class="c-string">"Render Pipeline Test 1"</span>);

    std::cout &lt;&lt; <span class="c-string">"\\nTriggering Polymorphic Deletion:\\n"</span>;
    <span class="c-keyword">delete</span> display; <span class="c-comment">// Safely invokes ~OledDisplay() first, then ~DisplaySurface()</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Virtual Destructor Teardown vs Non-Virtual Leak Hazard</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Non-Virtual Destructor Path (Bug) -->
      <g transform="translate(30, 20)">
        <rect width="330" height="170" rx="8" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="165" y="30" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Non-Virtual Destructor (LEAK HAZARD)</text>
        <rect x="20" y="50" width="290" height="35" rx="4" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="165" y="72" fill="#10b981" font-size="11" text-anchor="middle">✓ ~Base() Executes via Static Binding</text>
        <rect x="20" y="100" width="290" height="45" rx="4" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444"/>
        <text x="165" y="120" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">✗ ~Derived() Completely Bypassed!</text>
        <text x="165" y="135" fill="var(--text-muted)" font-size="10" text-anchor="middle">Derived heap buffers leak permanently!</text>
      </g>

      <!-- Virtual Destructor Path (Correct) -->
      <g transform="translate(400, 20)">
        <rect width="330" height="170" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5"/>
        <text x="165" y="30" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Virtual Destructor (SAFE CLEANUP)</text>
        <rect x="20" y="50" width="290" height="35" rx="4" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="165" y="72" fill="#10b981" font-size="11" text-anchor="middle">1. ~Derived() Dispatched Dynamically</text>
        <rect x="20" y="100" width="290" height="35" rx="4" fill="rgba(99, 102, 241, 0.15)"/>
        <text x="165" y="122" fill="#a5b4fc" font-size="11" text-anchor="middle">2. ~Base() Automatically Called Next</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-card">
  <div class="comparison-header">
    <span class="comp-icon">⚖️</span>
    <span class="comp-title">Comparative Analysis: Virtual Function vs. Pure Virtual Function</span>
  </div>
  <table class="comp-table">
    <thead>
      <tr>
        <th>Criterion</th>
        <th>Virtual Function</th>
        <th>Pure Virtual Function</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Declaration Syntax</strong></td>
        <td><code>virtual void render() { /* body */ }</code></td>
        <td><code>virtual void render() = 0;</code></td>
      </tr>
      <tr>
        <td><strong>Base Implementation</strong></td>
        <td>Provides a default implementation in base.</td>
        <td>Usually provides no implementation in base class.</td>
      </tr>
      <tr>
        <td><strong>Derived Obligation</strong></td>
        <td>Derived classes <strong>may</strong> override if desired.</td>
        <td>Derived classes <strong>must</strong> implement to be concrete.</td>
      </tr>
      <tr>
        <td><strong>Instantiation Impact</strong></td>
        <td>Enclosing class remains concrete and instantiable.</td>
        <td>Turns enclosing class into an <strong>Abstract Base Class</strong>.</td>
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
    <li><span class="check-box"></span> Enumerate the 7 canonical rules of virtual functions.</li>
    <li><span class="check-box"></span> Why can constructors never be virtual in C++?</li>
    <li><span class="check-box"></span> Why must a base class destructor be virtual when polymorphism is involved?</li>
    <li><span class="check-box"></span> What syntax turns a standard virtual function into a pure virtual function?</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> AKTU viva and semester exams frequently feature the question: <em>"Can constructors be virtual? Why or why not?"</em><br>
  Always state: <strong>No, constructors cannot be virtual</strong> because 1) Object construction requires knowing the exact concrete type and memory size at compile time, and 2) The <code>vptr</code> is initialized inside the constructor, so virtual dispatch is impossible before construction finishes.
</div>
"""
    sections.append({
        "id": "u4-sec-20",
        "number": 20,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "20. Rules of Virtual Functions, Virtual Destructors & Abstract Interfaces",
        "subtitle": "The 7 Canonical Rules, Virtual Destructor Memory Teardown, Pure Virtual Functions (= 0) & Abstract Base Classes",
        "content": sec20_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit4_part4_sections()
    print(f"generate_unit4_part4.py compiled {len(secs)} sections successfully.")
