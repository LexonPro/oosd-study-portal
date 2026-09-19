# generate_unit4_part3.py: Generates Sections 12 to 15 for Unit 4 (C++ Functions)

def get_unit4_part3_sections():
    sections = []

    # =========================================================================
    # SECTION 12: Simple Functions
    # =========================================================================
    sec12_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">12. Simple Functions: Prototypes, Calls &amp; Activation Records</h3>
  </div>

  <div class="detail-block">
    <h5>12.1 What is a Function?</h5>
    <p>
      A <strong>Function</strong> is an autonomous, reusable, named subroutine designed to execute a specific cohesive computational task. Functions are the primary building blocks for modularity, code reuse, and top-down problem decomposition.
    </p>
  </div>

  <div class="detail-block">
    <h5>12.2 Function Anatomy in C++</h5>
    <ul>
      <li><strong>Function Declaration (Prototype):</strong> Informs the compiler about the function's name, return type, and parameter list before its actual definition appears:
        <div class="code-box"><code>int calculateSquare(int number);</code></div>
        Enables the compiler to enforce strict type checking and validate argument types at call sites across multi-file projects.
      </li>
      <li><strong>Function Definition:</strong> Contains the complete header and executable body block:
        <div class="code-box"><code>int calculateSquare(int number) { return number * number; }</code></div>
      </li>
      <li><strong>Function Call (Invocation):</strong> Transfers CPU program counter to the function's memory address, passing actual arguments:
        <div class="code-box"><code>int result = calculateSquare(5);</code></div>
      </li>
      <li><strong>Return Value:</strong> Sends computed output back to the caller via the <code>return</code> keyword. A function returning <code>void</code> performs an action without yielding a value.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>12.3 The Call Stack &amp; Activation Records (Stack Frames)</h5>
    <p>
      When a function is called, the runtime CPU architecture allocates an <strong>Activation Record (Stack Frame)</strong> on the thread call stack:
    </p>
    <ol>
      <li>Pushes caller's return address and saved frame pointer.</li>
      <li>Pushes copies of actual arguments into formal parameters.</li>
      <li>Allocates memory for local variables defined inside the function body.</li>
      <li>Upon executing <code>return</code>, the stack frame is popped (deallocated instantly), and control resumes at the caller's return address.</li>
    </ol>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Corporate Department Work Order</span>
  </div>
  <p>
    Imagine you are a project manager (<code>main()</code> function). You need a financial audit completed.<br>
    Instead of doing the math yourself, you fill out a standard <strong>Work Order (Function Prototype)</strong>: <em>"To: Accounting, Input: Receipts, Output: Balance Sheet"</em>.<br>
    You dispatch the document to the accounting desk (<strong>Function Call</strong>). The accountant reserves a desk space (<strong>Stack Frame</strong>), crunches the numbers (<strong>Function Body</strong>), stamps the final report (<strong>Return Value</strong>), and clears their desk (<strong>Stack Frame Popped</strong>). You receive the audited report and proceed with your day.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Function Prototype, Implementation, Value Returning & Execution Tracing</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// 1. FUNCTION DECLARATIONS (PROTOTYPES)</span>
<span class="c-type">double</span> calculateCompoundInterest(<span class="c-type">double</span> principal, <span class="c-type">double</span> annualRatePercent, <span class="c-type">int</span> years);
<span class="c-type">void</span> displayFinancialReport(<span class="c-type">std::string</span> clientName, <span class="c-type">double</span> finalAmount);

<span class="c-type">int</span> main() {
    <span class="c-type">std::string</span> customer = <span class="c-string">"Vikramaditya"</span>;
    <span class="c-type">double</span> deposit = <span class="c-number">50000.0</span>; <span class="c-comment">// Rs. 50,000</span>
    <span class="c-type">double</span> interestRate = <span class="c-number">7.5</span>; <span class="c-comment">// 7.5% per annum</span>
    <span class="c-type">int</span> tenureYears = <span class="c-number">5</span>;

    <span class="c-comment">// 2. FUNCTION CALL: Passes arguments and captures returned value</span>
    <span class="c-type">double</span> maturedMaturityValue = calculateCompoundInterest(deposit, interestRate, tenureYears);

    <span class="c-comment">// 3. VOID FUNCTION CALL: Performs formatted reporting action</span>
    displayFinancialReport(customer, maturedMaturityValue);

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}

<span class="c-comment">// 4. FUNCTION DEFINITIONS</span>
<span class="c-type">double</span> calculateCompoundInterest(<span class="c-type">double</span> principal, <span class="c-type">double</span> annualRatePercent, <span class="c-type">int</span> years) {
    <span class="c-type">double</span> rateDecimal = annualRatePercent / <span class="c-number">100.0</span>;
    <span class="c-type">double</span> compoundFactor = <span class="c-number">1.0</span>;

    <span class="c-keyword">for</span> (<span class="c-type">int</span> i = <span class="c-number">0</span>; i &lt; years; ++i) {
        compoundFactor *= (<span class="c-number">1.0</span> + rateDecimal);
    }
    <span class="c-keyword">return</span> principal * compoundFactor; <span class="c-comment">// Result returned to caller</span>
}

<span class="c-type">void</span> displayFinancialReport(<span class="c-type">std::string</span> clientName, <span class="c-type">double</span> finalAmount) {
    std::cout &lt;&lt; <span class="c-string">"=== Official Financial Advisory Statement ===\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Client Name:       "</span> &lt;&lt; clientName &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Maturity Proceeds: Rs. "</span> &lt;&lt; finalAmount &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Status:            Verified &amp; Certified\\n"</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Call Stack Frame Allocation & Deallocation</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <!-- Step 1: main stack frame -->
      <g transform="translate(60, 30)">
        <rect width="280" height="200" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="140" y="26" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Step 1: main() Activation Record</text>
        <rect x="20" y="45" width="240" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="30" y="67" fill="var(--text-primary)" font-size="11">deposit = 50000.0</text>
        <rect x="20" y="90" width="240" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="30" y="112" fill="var(--text-primary)" font-size="11">customer = "Vikramaditya"</text>
        <rect x="20" y="135" width="240" height="45" rx="4" fill="var(--bg-card)" stroke="#fbbf24"/>
        <text x="30" y="155" fill="#fbbf24" font-size="11" font-weight="bold">Call: calculateCompoundInterest()</text>
        <text x="30" y="172" fill="var(--text-secondary)" font-size="10">Saved Return Address: 0x00401A20</text>
      </g>

      <!-- Arrow -->
      <path d="M 350 130 L 410 130" stroke="#10b981" stroke-width="3" marker-end="url(#arrow-flow)"/>
      <text x="380" y="120" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">PUSH</text>

      <!-- Step 2: Callee stack frame -->
      <g transform="translate(420, 30)">
        <rect width="280" height="200" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="2"/>
        <text x="140" y="26" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Step 2: Subroutine Stack Frame</text>
        <rect x="20" y="45" width="240" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="30" y="67" fill="var(--text-primary)" font-size="11">principal = 50000.0, rate = 7.5</text>
        <rect x="20" y="90" width="240" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="30" y="112" fill="var(--text-primary)" font-size="11">compoundFactor = 1.4356</text>
        <rect x="20" y="135" width="240" height="45" rx="4" fill="var(--bg-card)" stroke="#c084fc"/>
        <text x="30" y="155" fill="#c084fc" font-size="11" font-weight="bold">return principal * factor;</text>
        <text x="30" y="172" fill="#10b981" font-size="10">Frame POPPED upon return</text>
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
    <li><span class="check-box"></span> What is the purpose of a function prototype? (Declares signature to compiler before full definition).</li>
    <li><span class="check-box"></span> What happens to local variables when a function completes execution? (Their stack frame is popped; variables are destroyed).</li>
    <li><span class="check-box"></span> What does the <code>void</code> return type signify? (Function produces no return value).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> In theory questions asking to explain <em>"Components of a C++ function"</em>, clearly identify and define: 1. Function Prototype, 2. Formal Parameters vs Actual Arguments, 3. Function Body, and 4. Return Statement.
</div>
"""
    sections.append({
        "id": "u4-sec-12",
        "number": 12,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "12. Simple Functions: Prototypes, Calls & Stack Frames",
        "subtitle": "Declarations vs Definitions, Parameter Passing Mechanics, Return Typology & Activation Record Stack Lifecycles",
        "content": sec12_content
    })

    # =========================================================================
    # SECTION 13: Call by Reference & Return by Reference
    # =========================================================================
    sec13_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">13. Call by Reference &amp; Return by Reference</h3>
  </div>

  <div class="detail-block">
    <h5>13.1 What is a Reference in C++?</h5>
    <p>
      A <strong>Reference</strong> is an alternative symbolic name (an alias) bound permanently to an already existing variable in memory.
    </p>
    <div class="code-box"><code>int original = 100; int&amp; alias = original;</code></div>
    <ul>
      <li><strong>Crucial Reference Invariants:</strong>
        <ol>
          <li>A reference <strong>must be initialized</strong> at the point of declaration.</li>
          <li>A reference <strong>cannot be NULL</strong>.</li>
          <li>A reference <strong>cannot be reseated</strong> (rebound) to point to another variable later. Any assignment to <code>alias</code> mutates the value of <code>original</code>.</li>
        </ol>
      </li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>13.2 Call by Reference</h5>
    <p>
      When a function parameter is declared as a reference (e.g. <code>void swap(int&amp; a, int&amp; b)</code>), the function receives the <strong>original variables themselves</strong>, not copies:
    </p>
    <ul>
      <li><strong>In-Place Mutation:</strong> Any changes made inside the function directly modify the caller's original variables.</li>
      <li><strong>Zero Copy Overhead:</strong> Eliminates expensive byte-copying when passing large objects (like big structs or 10,000-element vectors). Passing <code>const MyLargeObject&amp; obj</code> achieves maximum read-only efficiency.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>13.3 Return by Reference</h5>
    <p>
      A function can return a <strong>Reference</strong> instead of a value. This returns an lvalue referring directly to an existing storage location, enabling the astounding syntax of placing a <strong>function call on the Left-Hand Side (LHS) of an assignment operator</strong>:
    </p>
    <div class="code-box"><code>getElement(2) = 999; // Modifies array[2] in-place!</code></div>
    <div class="exam-tip" style="margin: 12px 0;">
      <strong>CRITICAL SAFETY RULE (Common AKTU Pitfall):</strong> NEVER return a reference to a local automatic stack variable! When the function terminates, local variables are destroyed. The returned reference becomes a <strong>Dangling Reference</strong> pointing to dead memory, causing catastrophic crashes. Only return references to global variables, static variables, or object members passed in by reference.
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Photocopy vs Live Google Docs Shared Link</span>
  </div>
  <p>
    &bull; <strong>Call by Value:</strong> Like making a physical <strong>Photocopy</strong> of your resume and handing it to an interviewer. If the interviewer scribbles notes with a red pen on the photocopy, your original master copy at home remains 100% untouched.<br>
    &bull; <strong>Call by Reference:</strong> Like sending a live collaborative <strong>Google Docs Link with Edit Access</strong>. Both you and the interviewer are viewing the exact same document in the cloud. When the interviewer types a sentence, the text immediately updates on your screen!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating Classical Swap by Reference & Return by Reference on LHS</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-comment">// 1. CALL BY REFERENCE: Swapping two variables without pointer dereferencing syntax</span>
<span class="c-type">void</span> swapValues(<span class="c-type">int</span>&amp; a, <span class="c-type">int</span>&amp; b) {
    <span class="c-type">int</span> temp = a;
    a = b;
    b = temp; <span class="c-comment">// Mutates the caller's variables directly</span>
}

<span class="c-comment">// Global array for demonstrating Return by Reference</span>
<span class="c-type">int</span> globalScores[<span class="c-number">4</span>] = {<span class="c-number">85</span>, <span class="c-number">90</span>, <span class="c-number">78</span>, <span class="c-number">92</span>};

<span class="c-comment">// 2. RETURN BY REFERENCE: Returns lvalue reference to persistent array slot</span>
<span class="c-type">int</span>&amp; getScoreReference(<span class="c-type">int</span> index) {
    <span class="c-comment">// Safe: globalScores lives persistently in global data segment, NOT on local stack</span>
    <span class="c-keyword">return</span> globalScores[index];
}

<span class="c-type">int</span> main() {
    <span class="c-comment">// Testing Call by Reference</span>
    <span class="c-type">int</span> x = <span class="c-number">10</span>, y = <span class="c-number">50</span>;
    std::cout &lt;&lt; <span class="c-string">"Before swap: x = "</span> &lt;&lt; x &lt;&lt; <span class="c-string">", y = "</span> &lt;&lt; y &lt;&lt; <span class="c-string">"\\n"</span>;
    swapValues(x, y);
    std::cout &lt;&lt; <span class="c-string">"After swap:  x = "</span> &lt;&lt; x &lt;&lt; <span class="c-string">", y = "</span> &lt;&lt; y &lt;&lt; <span class="c-string">"\\n\\n"</span>;

    <span class="c-comment">// Testing Return by Reference: FUNCTION CALL ON LEFT-HAND SIDE OF ASSIGNMENT!</span>
    std::cout &lt;&lt; <span class="c-string">"Original globalScores[2]: "</span> &lt;&lt; globalScores[<span class="c-number">2</span>] &lt;&lt; <span class="c-string">"\\n"</span>;
    
    getScoreReference(<span class="c-number">2</span>) = <span class="c-number">99</span>; <span class="c-comment">// Overwrites globalScores[2] directly!</span>
    
    std::cout &lt;&lt; <span class="c-string">"Mutated globalScores[2]:  "</span> &lt;&lt; globalScores[<span class="c-number">2</span>] &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Return by reference successfully acted as a valid L-Value!\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="comparison-table-wrapper">
  <h4>Head-to-Head Comparison: Parameter Passing Modes in C++</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Architectural Criterion</th>
        <th>Call by Value</th>
        <th>Call by Reference (<code>int&amp;</code>)</th>
        <th>Call by Pointer (<code>int*</code>)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>What is Passed?</strong></td>
        <td>Duplicate copy of actual value</td>
        <td>Direct alias/reference to original variable</td>
        <td>Memory address of original variable</td>
      </tr>
      <tr>
        <td><strong>Can Modify Original?</strong></td>
        <td>No (Original is shielded)</td>
        <td>Yes (Direct in-place modification)</td>
        <td>Yes (Via pointer dereferencing <code>*p</code>)</td>
      </tr>
      <tr>
        <td><strong>Call Site Syntax</strong></td>
        <td><code>func(x)</code></td>
        <td><code>func(x)</code> (Clean and elegant)</td>
        <td><code>func(&amp;x)</code> (Requires address-of <code>&amp;</code>)</td>
      </tr>
      <tr>
        <td><strong>Inside Function Syntax</strong></td>
        <td><code>val = 10;</code></td>
        <td><code>ref = 10;</code> (Normal syntax)</td>
        <td><code>*ptr = 10;</code> (Explicit dereference)</td>
      </tr>
      <tr>
        <td><strong>Can Be NULL?</strong></td>
        <td>N/A</td>
        <td><strong>Never NULL</strong> (Guaranteed valid)</td>
        <td>Can be <code>nullptr</code> (Requires null check)</td>
      </tr>
      <tr>
        <td><strong>Memory Overhead</strong></td>
        <td>Copies entire object bytes</td>
        <td>Zero copy overhead (Passes pointer under the hood)</td>
        <td>Copies address (8 bytes on 64-bit)</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Call by Reference &amp; Return by Reference (L-Value Assignment)</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
      <!-- Left Panel: Call by Reference -->
      <g transform="translate(30, 15)">
        <rect width="330" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="165" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Call by Reference: Alias Binding</text>
        
        <rect x="25" y="45" width="280" height="50" rx="4" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="165" y="68" fill="var(--text-primary)" font-size="11" text-anchor="middle">Physical RAM Cell [0x7FFE48]</text>
        <text x="165" y="86" fill="#10b981" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Value = 50 (Mutates in-place)</text>

        <rect x="35" y="105" width="120" height="30" rx="4" fill="rgba(56, 189, 248, 0.15)"/>
        <text x="95" y="125" fill="#38bdf8" font-size="10" text-anchor="middle">Caller: int x</text>

        <rect x="175" y="105" width="120" height="30" rx="4" fill="rgba(16, 185, 129, 0.15)"/>
        <text x="235" y="125" fill="#10b981" font-size="10" text-anchor="middle">Callee: int&amp; a</text>

        <text x="165" y="155" fill="var(--text-muted)" font-size="9" text-anchor="middle">Both names refer to the identical memory address</text>
      </g>

      <!-- Right Panel: Return by Reference -->
      <g transform="translate(400, 15)">
        <rect width="330" height="170" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="1.5"/>
        <text x="165" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Return by Reference: L-Value Return</text>
        
        <rect x="25" y="45" width="280" height="45" rx="4" fill="var(--bg-card)"/>
        <text x="165" y="65" fill="#f59e0b" font-family="monospace" font-size="11" text-anchor="middle">getScoreReference(2) = 99;</text>
        <text x="165" y="80" fill="var(--text-muted)" font-size="9" text-anchor="middle">Function call acts as Left-Hand Side L-Value</text>

        <rect x="25" y="100" width="280" height="40" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981"/>
        <text x="165" y="120" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">&amp;globalScores[2] overwritten directly!</text>
        <text x="165" y="133" fill="var(--text-primary)" font-size="9" text-anchor="middle">Requires persistent target (Global / Static / Heap)</text>
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
    <li><span class="check-box"></span> What is the syntax for creating an alias reference to a variable? (<code>int&amp; ref = var;</code>).</li>
    <li><span class="check-box"></span> Why is it dangerous to return a reference to a local stack variable? (Becomes a dangling reference after stack frame deallocation).</li>
    <li><span class="check-box"></span> How does return-by-reference allow a function call to appear on the Left-Hand Side (LHS) of an assignment? (Returns an lvalue).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"Explain Call by Reference and Return by Reference with examples"</em>, provide the <code>swapValues(int&amp;, int&amp;)</code> function for call by reference, and demonstrate <code>getElement(i) = value;</code> for return by reference. Explicitly state the warning regarding local variable destruction.
</div>
"""
    sections.append({
        "id": "u4-sec-13",
        "number": 13,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "13. Call by Reference & Return by Reference",
        "subtitle": "Aliasing Semantics, L-Value Function Returns, Parameter Passing Matrices & The Dangling Reference Trap",
        "content": sec13_content
    })

    # =========================================================================
    # SECTION 14: Inline Functions
    # =========================================================================
    sec14_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">14. Inline Functions &amp; Call Overhead Optimization</h3>
  </div>

  <div class="detail-block">
    <h5>14.1 What is an Inline Function?</h5>
    <p>
      An <strong>Inline Function</strong> is a function designated with the <code>inline</code> keyword. It serves as an optimization request to the C++ compiler to substitute the full executable body of the function directly into every call site during compilation, rather than executing a normal hardware subroutine jump.
    </p>
    <div class="code-box"><code>inline int square(int x) { return x * x; }</code></div>
  </div>

  <div class="detail-block">
    <h5>14.2 The Problem Solved: Function Call Overhead</h5>
    <p>
      For tiny functions containing only 1 to 3 instructions (e.g., getters, simple calculations, clamping values), the time required to orchestrate the function call often drastically exceeds the time needed to compute the answer!
    </p>
    <ul>
      <li><strong>Standard Call Overhead:</strong> Pushing arguments onto stack, saving registers, jumping CPU program counter to function address, executing 1 line, popping stack, and jumping back.</li>
      <li><strong>Inline Solution:</strong> Replaces the call with raw arithmetic in-place. Zero stack frames, zero jump penalties, maximum CPU pipeline throughput.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>14.3 When Does the Compiler Ignore the <code>inline</code> Keyword?</h5>
    <p>
      The <code>inline</code> specifier is merely a <strong>suggestion (hint)</strong> to the compiler, not an absolute command. Compilers will automatically ignore the request and generate a normal function if:
    </p>
    <ol>
      <li>The function body is excessively large or complex.</li>
      <li>The function contains iteration loops (<code>for</code>, <code>while</code>, <code>do-while</code>).</li>
      <li>The function contains <code>switch</code> or <code>goto</code> statements.</li>
      <li>The function is <strong>recursive</strong> (calls itself).</li>
      <li>The function contains <code>static</code> local variables.</li>
      <li>The programmer takes the memory address of the function (requiring a physical code address).</li>
    </ol>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Sticky Note vs The Library Reference Desk</span>
  </div>
  <p>
    Suppose you are writing an engineering thesis. Every 5 minutes, you need to look up the exact mathematical value of gravitational acceleration ($9.80665$).<br>
    &bull; <strong>Standard Function Call:</strong> You put on your coat, walk downstairs, walk 3 blocks to the university central library, ask the reference librarian, receive the number, walk 3 blocks back, and sit down at your desk. The travel overhead is 99% of the effort!<br>
    &bull; <strong>Inline Function:</strong> You paste a small yellow <strong>Sticky Note</strong> directly onto your computer monitor frame reading <em>"g = 9.80665"</em>. You look up, copy the number instantly, and continue writing with zero travel delay.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating Inline Function Declaration & Optimization Feasibility</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-comment">// Explicit inline function: Compact, fast, zero function-call overhead</span>
<span class="c-keyword">inline</span> <span class="c-type">double</span> computeKineticEnergy(<span class="c-type">double</span> massKg, <span class="c-type">double</span> velocityMps) {
    <span class="c-keyword">return</span> <span class="c-number">0.5</span> * massKg * (velocityMps * velocityMps);
}

<span class="c-comment">// Member functions defined INSIDE class declarations are implicitly inlined</span>
<span class="c-keyword">class</span> Vector2D {
<span class="c-keyword">public</span>:
    <span class="c-type">double</span> x, y;
    Vector2D(<span class="c-type">double</span> x, <span class="c-type">double</span> y) : x(x), y(y) {}

    <span class="c-comment">// Implicitly inline getter</span>
    <span class="c-type">double</span> getX() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> x; }
};

<span class="c-type">int</span> main() {
    <span class="c-type">double</span> mass = <span class="c-number">1200.0</span>;  <span class="c-comment">// 1200 kg racecar</span>
    <span class="c-type">double</span> speed = <span class="c-number">45.0</span>;   <span class="c-comment">// 45 m/s (~162 km/h)</span>

    <span class="c-comment">// At compilation, this call is directly replaced with: 0.5 * 1200.0 * (45.0 * 45.0)</span>
    <span class="c-type">double</span> ke = computeKineticEnergy(mass, speed);

    std::cout &lt;&lt; <span class="c-string">"Calculated Kinetic Energy: "</span> &lt;&lt; ke &lt;&lt; <span class="c-string">" Joules\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Compiler expanded calculation directly in-place with zero subroutine jump!\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Standard Subroutine Jump vs Inline Code In-Place Expansion</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <!-- Normal function call -->
      <g transform="translate(40, 25)">
        <rect width="320" height="200" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="2"/>
        <text x="160" y="24" fill="#ef4444" font-size="13" font-weight="bold" text-anchor="middle">Normal Function Call (High Overhead)</text>
        
        <rect x="20" y="45" width="120" height="40" rx="4" fill="var(--bg-card)"/>
        <text x="80" y="70" fill="var(--text-primary)" font-size="11" text-anchor="middle">Caller: main()</text>

        <path d="M 140 65 L 195 65" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-blue)"/>
        <text x="167" y="55" fill="#fbbf24" font-size="9" text-anchor="middle">Jump</text>

        <rect x="200" y="45" width="100" height="40" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
        <text x="250" y="70" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">func() Body</text>

        <path d="M 200 80 L 140 80" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-blue)"/>
        <text x="170" y="95" fill="#10b981" font-size="9" text-anchor="middle">Return</text>

        <rect x="20" y="115" width="280" height="70" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="135" fill="var(--text-secondary)" font-size="10" text-anchor="middle">1. Push arguments onto call stack</text>
        <text x="160" y="153" fill="var(--text-secondary)" font-size="10" text-anchor="middle">2. Save registers &amp; jump program counter</text>
        <text x="160" y="171" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">Substantial overhead for small 1-line functions!</text>
      </g>

      <!-- Inline function call -->
      <g transform="translate(400, 25)">
        <rect width="320" height="200" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="2"/>
        <text x="160" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Inline Function (Zero Overhead)</text>

        <rect x="20" y="45" width="280" height="50" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
        <text x="160" y="67" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Caller: main()</text>
        <text x="160" y="85" fill="var(--text-primary)" font-family="monospace" font-size="10.5" text-anchor="middle">double ke = 0.5 * m * (v * v);</text>

        <rect x="20" y="115" width="280" height="70" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="135" fill="var(--text-secondary)" font-size="10" text-anchor="middle">1. Body substituted directly at compile-time</text>
        <text x="160" y="153" fill="var(--text-secondary)" font-size="10" text-anchor="middle">2. Zero stack pushes, zero register saves</text>
        <text x="160" y="171" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Zero jump latency • Max CPU pipeline efficiency</text>
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
    <li><span class="check-box"></span> What is the primary purpose of declaring a function as <code>inline</code>? (Eliminate function call overhead for small routines).</li>
    <li><span class="check-box"></span> Are member functions defined inside the class body inline by default? (Yes, implicitly inline).</li>
    <li><span class="check-box"></span> State at least 3 conditions where the C++ compiler will reject inline expansion. (Loops, recursion, static variables).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Whenever asked <em>"What are inline functions? What are their limitations?"</em>, list the 5 situations where compilers ignore inlining (loops, switch, recursion, large bodies, static variables) to score full marks.
</div>
"""
    sections.append({
        "id": "u4-sec-14",
        "number": 14,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "14. Inline Functions & Call Overhead Optimization",
        "subtitle": "Eliminating Subroutine Jumps, In-Place Assembly Expansion, Compiler Heuristics & Rejection Criteria",
        "content": sec14_content
    })

    # =========================================================================
    # SECTION 15: Macro vs Inline Function
    # =========================================================================
    sec15_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 2</div>
    <h3 class="card-title">15. Macro vs Inline Function: The Safety &amp; Semantics Divide</h3>
  </div>

  <div class="detail-block">
    <h5>15.1 The Evolutionary Shift: Why C++ Introduced Inline Functions</h5>
    <p>
      In legacy C, programmers used C-preprocessor macros (<code>#define SQUARE(x) ((x)*(x))</code>) to achieve fast inline execution without function call overhead.
    </p>
    <p>
      However, preprocessor macros are <strong>blind text-substitution tools</strong> completely ignorant of C++ type systems, operator precedence, and variable scopes. This causes notorious, difficult-to-debug runtime defects.
    </p>
  </div>

  <div class="detail-block">
    <h5>15.2 The Classical Dangerous Side-Effects of Macros</h5>
    <ul>
      <li><strong>Operator Precedence Trap:</strong>
        <div class="code-box"><code>#define SQUARE(x) x * x</code></div>
        If called with <code>SQUARE(2 + 3)</code>, the preprocessor textually expands this to:
        <div class="code-box"><code>2 + 3 * 2 + 3 = 2 + 6 + 3 = 11 // WRONG! Expected (2+3)^2 = 25!</code></div>
      </li>
      <li><strong>Double Evaluation Side-Effect Trap:</strong>
        <div class="code-box"><code>#define MAX(a, b) ((a) &gt; (b) ? (a) : (b))</code></div>
        If called with post-increment: <code>MAX(x++, y)</code>, whichever variable is larger is <strong>incremented TWICE</strong> because its name appears twice in the expanded ternary expansion!
      </li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>15.3 The Inline Function Solution</h5>
    <p>
      Inline functions offer all the execution speed of macros with none of the hazards:
    </p>
    <ul>
      <li>Evaluated by the <strong>Compiler</strong>, not the Preprocessor.</li>
      <li>Enforces strict <strong>Type-Checking</strong>.</li>
      <li>Guarantees that arguments are evaluated <strong>exactly once</strong> before invocation.</li>
      <li>Integrates with source-level symbol tables, making code debuggable with breakpoints.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Word Processor Find-and-Replace vs Professional Translator</span>
  </div>
  <p>
    &bull; <strong>Macro (<code>#define</code>):</strong> Like running a blunt <strong>"Find &amp; Replace All"</strong> script in a text editor. If you tell it to replace the word <em>"can"</em> with <em>"tin container"</em>, it blindly turns the sentence <em>"I can do this"</em> into <em>"I tin container do this"</em>. It has zero understanding of grammar or context!<br>
    &bull; <strong>Inline Function:</strong> Like hiring a bilingual <strong>Professional Translator</strong>. The translator understands sentence grammar, parts of speech, and nuances (type-checking and semantic evaluation), ensuring the translated sentence is grammatically flawless and contextually correct.
  </p>
</div>

<div class="comparison-table-wrapper">
  <h4>AKTU Master Comparison Matrix: Preprocessor Macro vs Inline Function</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Architectural Criterion</th>
        <th>Preprocessor Macro (<code>#define</code>)</th>
        <th>Inline Function (<code>inline</code>)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Processing Phase</strong></td>
        <td>Evaluated by Preprocessor before compilation starts</td>
        <td>Parsed and expanded by Compiler during code generation</td>
      </tr>
      <tr>
        <td><strong>Mechanism</strong></td>
        <td>Blind textual token substitution</td>
        <td>Actual C++ function with semantic type enforcement</td>
      </tr>
      <tr>
        <td><strong>Type Checking</strong></td>
        <td>None (Accepts any token; type errors caught late)</td>
        <td>Full, strict static type safety enforced by compiler</td>
      </tr>
      <tr>
        <td><strong>Side-Effects (e.g. <code>x++</code>)</strong></td>
        <td>Severe danger of multiple evaluations</td>
        <td>Argument evaluated strictly once; completely safe</td>
      </tr>
      <tr>
        <td><strong>Source-Level Debugging</strong></td>
        <td>Impossible (No symbol in debugger call stack)</td>
        <td>Supported (Symbols exist in debugger symbol table)</td>
      </tr>
      <tr>
        <td><strong>Scope Respect</strong></td>
        <td>Ignores scopes, classes, and namespaces</td>
        <td>Fully respects classes, access specifiers, and namespaces</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Exposing the Lethal Side-Effect Bug in Macros vs Inline Function Safety</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-comment">// Dangerous Preprocessor Macro</span>
<span class="c-keyword">#define</span> MACRO_SQUARE(x) ((x) * (x))

<span class="c-comment">// Safe, Type-Enforced Inline Function</span>
<span class="c-keyword">inline</span> <span class="c-type">int</span> inlineSquare(<span class="c-type">int</span> x) {
    <span class="c-keyword">return</span> x * x;
}

<span class="c-type">int</span> main() {
    <span class="c-comment">// Scenario 1: Standard Evaluation</span>
    std::cout &lt;&lt; <span class="c-string">"=== Scenario 1: Basic Evaluation ===\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"MACRO_SQUARE(5):  "</span> &lt;&lt; MACRO_SQUARE(<span class="c-number">5</span>) &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"inlineSquare(5):  "</span> &lt;&lt; inlineSquare(<span class="c-number">5</span>) &lt;&lt; <span class="c-string">"\\n\\n"</span>;

    <span class="c-comment">// Scenario 2: The Double-Increment Side-Effect Bug</span>
    <span class="c-type">int</span> a = <span class="c-number">5</span>;
    std::cout &lt;&lt; <span class="c-string">"=== Scenario 2: Post-Increment Side-Effect (a = 5) ===\\n"</span>;
    
    <span class="c-comment">// Macro expands to: ((a++) * (a++)) -&gt; 'a' is incremented TWICE!</span>
    <span class="c-type">int</span> macroResult = MACRO_SQUARE(a++);
    std::cout &lt;&lt; <span class="c-string">"MACRO_SQUARE(a++): Result = "</span> &lt;&lt; macroResult 
              &lt;&lt; <span class="c-string">" | Value of 'a' after: "</span> &lt;&lt; a &lt;&lt; <span class="c-string">" (INCREMENTED TWICE!)\\n"</span>;

    <span class="c-type">int</span> b = <span class="c-number">5</span>;
    <span class="c-comment">// Inline function evaluates 'b++' once (passing 5), then increments 'b' to 6</span>
    <span class="c-type">int</span> inlineResult = inlineSquare(b++);
    std::cout &lt;&lt; <span class="c-string">"inlineSquare(b++): Result = "</span> &lt;&lt; inlineResult 
              &lt;&lt; <span class="c-string">" | Value of 'b' after: "</span> &lt;&lt; b &lt;&lt; <span class="c-string">" (CORRECT: Incremented Once!)\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Macro Textual Splicing vs Inline Semantic Parsing</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- Macro pipeline -->
      <g transform="translate(40, 30)">
        <rect width="320" height="160" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="2"/>
        <text x="160" y="25" fill="#ef4444" font-size="13" font-weight="bold" text-anchor="middle">Macro: Preprocessor Phase</text>
        <rect x="20" y="45" width="280" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="67" fill="#ef4444" font-family="monospace" font-size="11" text-anchor="middle">#define SQUARE(x) ((x)*(x))</text>
        <text x="160" y="105" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Raw Text Substitution (No Syntax Tree)</text>
        <text x="160" y="125" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">✗ SQUARE(a++) → ((a++) * (a++))</text>
        <text x="160" y="145" fill="#ef4444" font-size="10" text-anchor="middle">Lethal Double Evaluation Bug!</text>
      </g>

      <!-- Arrow -->
      <path d="M 375 110 L 415 110" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

      <!-- Inline pipeline -->
      <g transform="translate(430, 30)">
        <rect width="290" height="160" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="2"/>
        <text x="145" y="25" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Inline: Compiler Phase</text>
        <rect x="20" y="45" width="250" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="145" y="67" fill="#10b981" font-family="monospace" font-size="11" text-anchor="middle">inline int square(int x)</text>
        <text x="145" y="105" fill="var(--text-secondary)" font-size="11" text-anchor="middle">AST Semantic Analysis • Type Checked</text>
        <text x="145" y="125" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">✓ Argument Evaluated Once</text>
        <text x="145" y="145" fill="#10b981" font-size="10" text-anchor="middle">100% Safe • Debugger Symbol Retained</text>
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
    <li><span class="check-box"></span> In which translation phase are macros evaluated versus inline functions? (Preprocessor vs Compiler).</li>
    <li><span class="check-box"></span> Explain the double-evaluation bug when <code>SQUARE(x++)</code> is passed to a macro.</li>
    <li><span class="check-box"></span> Name at least 4 critical advantages of inline functions over preprocessor macros.</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"Compare Macro and Inline Functions with an example"</em> is one of the most frequently asked 5-mark and 10-mark questions in AKTU OOSD. Always draw the comparison table above and demonstrate the <code>a++</code> double-increment bug in code!
</div>
"""
    sections.append({
        "id": "u4-sec-15",
        "number": 15,
        "part": "PART 2 — C++ FUNCTIONS",
        "title": "15. Macro vs Inline Function: The Safety & Semantics Divide",
        "subtitle": "Preprocessor Textual Splicing vs Compiler Semantic Trees, Operator Precedence Hazards & Side-Effect Immunity",
        "content": sec15_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit4_part3_sections()
    print(f"generate_unit4_part3.py compiled {len(secs)} sections successfully.")
