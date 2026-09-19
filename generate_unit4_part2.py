# generate_unit4_part2.py: Generates Sections 6 to 11 for Unit 4 (C++ Basics & Problem Solving)

def get_unit4_part2_sections():
    sections = []

    # =========================================================================
    # SECTION 6: Constants & Literals
    # =========================================================================
    sec6_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">6. Constants, Literal Types &amp; The const Qualifier</h3>
  </div>

  <div class="detail-block">
    <h5>6.1 Meaning of a Constant</h5>
    <p>
      A <strong>Constant</strong> in C++ is a data value that remains immutable throughout program execution. Attempting to modify a constant after its initialization triggers a compile-time error.
    </p>
  </div>

  <div class="detail-block">
    <h5>6.2 Comprehensive Classification of Literal Constants</h5>
    <p>
      Literals are raw, fixed values embedded directly in source code:
    </p>
    <ul>
      <li><strong>Integer Constants:</strong>
        <ul>
          <li><em>Decimal:</em> Standard base-10 numbers without leading zeros (e.g., <code>123</code>, <code>-45</code>).</li>
          <li><em>Octal:</em> Base-8 numbers prefixed with a leading zero <code>0</code> (e.g., <code>077</code> = 63 in decimal).</li>
          <li><em>Hexadecimal:</em> Base-16 numbers prefixed with <code>0x</code> or <code>0X</code> (e.g., <code>0x2F</code> = 47 in decimal).</li>
          <li><em>Suffixes:</em> <code>100L</code> (long), <code>100UL</code> (unsigned long), <code>100LL</code> (long long).</li>
        </ul>
      </li>
      <li><strong>Floating-Point Constants:</strong> Expressed in decimal or scientific notation (e.g., <code>12.34</code>, <code>3.14159f</code>, <code>2.5e-3</code>). Default type is <code>double</code>; suffix <code>f</code>/<code>F</code> forces single-precision <code>float</code>.</li>
      <li><strong>Character Constants:</strong> Single characters enclosed in single quotation marks (e.g., <code>'A'</code>, <code>'9'</code>). Includes escape sequences such as <code>'\\n'</code> (newline), <code>'\\t'</code> (horizontal tab), and <code>'\\0'</code> (null terminator).</li>
      <li><strong>String Constants:</strong> Zero or more characters enclosed in double quotes (e.g., <code>"C++ Programming"</code>). Stored as an immutable character array terminating in a hidden null byte (<code>'\\0'</code>).</li>
      <li><strong>Wide-Character Constants:</strong> Prefixed with <code>L</code> for 16-bit or 32-bit Unicode characters (e.g., <code>L'Ω'</code>, <code>L"Unicode String"</code> of type <code>wchar_t</code>).</li>
      <li><strong>Boolean Literals:</strong> The reserved tokens <code>true</code> (1) and <code>false</code> (0).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>6.3 The <code>const</code> &amp; <code>constexpr</code> Qualifiers</h5>
    <ul>
      <li><strong>The <code>const</code> Keyword:</strong> Qualifies a variable as read-only. It must be initialized at declaration: <code>const double PI = 3.14159265;</code>.</li>
      <li><strong>Pointer to Const vs Const Pointer (Crucial AKTU Exam Distinction):</strong>
        <ol>
          <li><code>const int* ptr = &amp;x;</code> (Pointer to Constant): The value pointed to cannot be altered via <code>*ptr</code>, but the pointer itself can point elsewhere.</li>
          <li><code>int* const ptr = &amp;x;</code> (Constant Pointer): The pointer address is fixed to <code>&amp;x</code> forever, but the integer value at that address can be modified.</li>
          <li><code>const int* const ptr = &amp;x;</code>: Neither address nor value can be changed.</li>
        </ol>
      </li>
      <li><strong><code>constexpr</code> (Modern C++):</strong> Enforces that evaluation happens strictly during <em>compilation</em>, enabling zero-runtime-cost computations for array bounds and template arguments.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Stone Carving vs Chalkboard Writing</span>
  </div>
  <p>
    A standard <strong>Variable</strong> is like writing notes on a classroom <strong>Chalkboard</strong>: you write 50, erase it 5 minutes later, and overwrite 75. Anyone in the room can rewrite the board.<br>
    A <strong>Constant (<code>const</code>)</strong> is like an inscription chiseled into a <strong>Granite Stone Tablet</strong> at a bank vault entrance: once the sculptor carves the year <em>"FOUNDED 1920"</em>, it is physically unalterable. If someone attempts to erase it with an eraser, the universe rejects the action (compiler rejection).
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating Integer Bases, Character Literals, and Const Pointers</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;iomanip&gt;</span>

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. Literal Constants in Multiple Number Bases</span>
    <span class="c-type">int</span> decVal = <span class="c-number">42</span>;       <span class="c-comment">// Base 10</span>
    <span class="c-type">int</span> octVal = <span class="c-number">052</span>;      <span class="c-comment">// Base 8 (Octal 52 = 5*8 + 2 = 42)</span>
    <span class="c-type">int</span> hexVal = <span class="c-number">0x2A</span>;     <span class="c-comment">// Base 16 (Hex 2A = 2*16 + 10 = 42)</span>

    std::cout &lt;&lt; <span class="c-string">"Decimal: "</span> &lt;&lt; decVal 
              &lt;&lt; <span class="c-string">" | Octal 052: "</span> &lt;&lt; octVal 
              &lt;&lt; <span class="c-string">" | Hex 0x2A: "</span> &lt;&lt; hexVal &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// 2. const Symbolic Constant</span>
    <span class="c-keyword">const</span> <span class="c-type">double</span> SPEED_OF_LIGHT = <span class="c-number">299792458.0</span>; <span class="c-comment">// m/s</span>
    <span class="c-comment">// SPEED_OF_LIGHT = 300000000.0; // COMPILE ERROR: assignment of read-only variable!</span>

    <span class="c-comment">// 3. Pointer to Const vs Const Pointer</span>
    <span class="c-type">int</span> a = <span class="c-number">10</span>, b = <span class="c-number">20</span>;

    <span class="c-comment">// Pointer to const data: Data is protected, pointer can move</span>
    <span class="c-keyword">const</span> <span class="c-type">int</span>* ptrToConst = &amp;a;
    ptrToConst = &amp;b; <span class="c-comment">// Valid! Pointer redirected to b</span>
    <span class="c-comment">// *ptrToConst = 30; // COMPILE ERROR: cannot modify read-only integer</span>

    <span class="c-comment">// Const pointer to mutable data: Address is locked, data can mutate</span>
    <span class="c-type">int</span>* <span class="c-keyword">const</span> constPtr = &amp;a;
    *constPtr = <span class="c-number">99</span>; <span class="c-comment">// Valid! Modifies 'a'</span>
    <span class="c-comment">// constPtr = &amp;b; // COMPILE ERROR: cannot reassign constant pointer!</span>

    std::cout &lt;&lt; <span class="c-string">"Updated value of 'a' through const pointer: "</span> &lt;&lt; a &lt;&lt; <span class="c-string">"\\n"</span>;
    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Pointer to Const vs Const Pointer Memory Mechanics</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <!-- Case 1: const int* p -->
      <g transform="translate(40, 30)">
        <rect width="320" height="190" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="160" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">const int* ptr (Pointer to Const)</text>
        
        <rect x="20" y="45" width="110" height="40" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
        <text x="75" y="70" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">ptr (&amp;a → &amp;b)</text>
        <text x="75" y="105" fill="#10b981" font-size="10" text-anchor="middle">✓ Address Rebindable</text>

        <path d="M 130 65 L 180 65" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-blue)"/>

        <rect x="185" y="45" width="115" height="40" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
        <text x="242" y="70" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Target Value [10]</text>
        <text x="242" y="105" fill="#ef4444" font-size="10" text-anchor="middle">✗ Value Read-Only</text>

        <rect x="20" y="130" width="280" height="45" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="157" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">*ptr = 50; // ILLEGAL</text>
      </g>

      <!-- Case 2: int* const p -->
      <g transform="translate(400, 30)">
        <rect width="320" height="190" rx="8" fill="var(--bg-elevated)" stroke="#a855f7" stroke-width="2"/>
        <text x="160" y="25" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">int* const ptr (Const Pointer)</text>

        <rect x="20" y="45" width="110" height="40" rx="4" fill="var(--bg-card)" stroke="#ef4444"/>
        <text x="75" y="70" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">ptr [LOCKED]</text>
        <text x="75" y="105" fill="#ef4444" font-size="10" text-anchor="middle">✗ Address Locked</text>

        <path d="M 130 65 L 180 65" stroke="#a855f7" stroke-width="2" marker-end="url(#arrow-blue)"/>

        <rect x="185" y="45" width="115" height="40" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
        <text x="242" y="70" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Target Value [10]</text>
        <text x="242" y="105" fill="#10b981" font-size="10" text-anchor="middle">✓ Value Mutable</text>

        <rect x="20" y="130" width="280" height="45" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="157" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">ptr = &amp;b; // ILLEGAL</text>
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
    <li><span class="check-box"></span> What distinguishes an octal literal from a decimal literal in C++? (Leading zero <code>0</code>, e.g. <code>052</code>).</li>
    <li><span class="check-box"></span> What is the hidden terminating character automatically placed at the end of every string literal? (<code>'\\0'</code> null terminator).</li>
    <li><span class="check-box"></span> Decode the difference between <code>const int* p</code> and <code>int* const p</code>.</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Questions asking to explain <em>"Types of constants in C++ with examples"</em> appear regularly in Section B (7 or 10 marks). Ensure you explicitly illustrate decimal, octal, hexadecimal, floating-point, character, string, and const pointer declarations.
</div>
"""
    sections.append({
        "id": "u4-sec-6",
        "number": 6,
        "part": "PART 1 — C++ BASICS",
        "title": "6. Constants, Literal Types & The const Concept",
        "subtitle": "Numeric Bases, String vs Character Literals, const Pointers vs Pointer to const & Immutability Guarantees",
        "content": sec6_content
    })

    # =========================================================================
    # SECTION 7: Enumeration — enum
    # =========================================================================
    sec7_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">7. Enumerations: Classic enum &amp; Modern enum class</h3>
  </div>

  <div class="detail-block">
    <h5>7.1 Meaning of Enumeration</h5>
    <p>
      An <strong>Enumeration</strong> is a user-defined ordinal data type consisting of a restricted set of named integral identifiers called <strong>Enumerators</strong>.
    </p>
    <p>
      Instead of permitting a variable to take any arbitrary integer value, an enumeration bounds the variable strictly to a domain-specific group of named possibilities.
    </p>
  </div>

  <div class="detail-block">
    <h5>7.2 Quantum Syllabus Focus: Days of the Week Example</h5>
    <p>
      The standard syllabus example illustrates how enumerators default to zero-indexed integer values unless explicitly overridden:
    </p>
    <div class="code-box"><code>enum days { Sun, Mon, Tue, Wed, Thu, Fri, Sat };</code></div>
    <ul>
      <li><code>Sun = 0</code>, <code>Mon = 1</code>, <code>Tue = 2</code>, <code>Wed = 3</code>, <code>Thu = 4</code>, <code>Fri = 5</code>, <code>Sat = 6</code>.</li>
      <li>If initialized explicitly: <code>enum ErrorCodes { SUCCESS = 0, TIMEOUT = 408, NOT_FOUND = 404 };</code>, subsequent unassigned enumerators increment by 1 from the previous value.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>7.3 Enumeration vs Integer: Architectural Rationale</h5>
    <ul>
      <li><strong>Raw Integer (<code>int</code>):</strong> Unbounded range ($-2 \times 10^9$ to $+2 \times 10^9$). A function taking <code>int day</code> can accept meaningless numbers like <code>-999</code> or <code>12345</code> without compiler warning.</li>
      <li><strong>Enumeration (<code>enum</code>):</strong> Self-documenting, type-safe, and bounded. The compiler enforces that only valid named states can be assigned.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>7.4 Modern Scoped Enumerations: <code>enum class</code> (C++11)</h5>
    <p>
      Classic C-style <code>enum</code> leaks its names into the surrounding scope (e.g. <code>Sun</code> can collide with another library's <code>Sun</code>) and implicitly converts to integers. Modern C++ introduces <strong>Scoped Enumerations (<code>enum class</code>)</strong>:
    </p>
    <ul>
      <li><strong>Scope Enforced:</strong> Enumerators must be prefixed by the enum name: <code>Days::Sun</code>.</li>
      <li><strong>No Implicit Conversion:</strong> Does NOT silently decay to <code>int</code> without an explicit <code>static_cast</code>, preventing accidental bugs.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Vehicle Automatic Transmission Shifter</span>
  </div>
  <p>
    Consider an automobile automatic gear shifter. It has strictly defined, discrete mechanical slots: <strong>P</strong> (Park), <strong>R</strong> (Reverse), <strong>N</strong> (Neutral), <strong>D</strong> (Drive), and <strong>L</strong> (Low Gear).<br>
    If the transmission gear was represented as an arbitrary raw integer, a driver could theoretically set the gear to <code>-42</code> or <code>999</code>, blowing up the gearbox.<br>
    An <strong><code>enum TransmissionMode { PARK, REVERSE, NEUTRAL, DRIVE, LOW }</code></strong> guarantees at compile-time that the driver can ONLY engage one of those 5 authorized mechanical positions.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Days of the Week State Machine & Scoped enum class Usage</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// 1. Classic AKTU Syllabus Example: Unscoped enum</span>
<span class="c-keyword">enum</span> Days {
    Sun, Mon, Tue, Wed, Thu, Fri, Sat
};

<span class="c-comment">// 2. Modern Strongly-Typed Scoped Enum</span>
<span class="c-keyword">enum</span> <span class="c-keyword">class</span> TrafficLight : <span class="c-type">char</span> {
    RED = <span class="c-string">'R'</span>,
    AMBER = <span class="c-string">'A'</span>,
    GREEN = <span class="c-string">'G'</span>
};

<span class="c-type">void</span> printDaySchedule(Days day) {
    <span class="c-keyword">switch</span> (day) {
        <span class="c-keyword">case</span> Sun:
        <span class="c-keyword">case</span> Sat:
            std::cout &lt;&lt; <span class="c-string">"[Schedule]: Weekend Rest &amp; OOSD Revision.\\n"</span>;
            <span class="c-keyword">break</span>;
        <span class="c-keyword">case</span> Mon:
        <span class="c-keyword">case</span> Tue:
        <span class="c-keyword">case</span> Wed:
        <span class="c-keyword">case</span> Thu:
        <span class="c-keyword">case</span> Fri:
            std::cout &lt;&lt; <span class="c-string">"[Schedule]: University Lecture &amp; Lab Sessions.\\n"</span>;
            <span class="c-keyword">break</span>;
    }
}

<span class="c-type">int</span> main() {
    Days today = Wed;
    std::cout &lt;&lt; <span class="c-string">"Current Day Numeric Index (Wed): "</span> &lt;&lt; today &lt;&lt; <span class="c-string">"\\n"</span>;
    printDaySchedule(today);

    <span class="c-comment">// Scoped enum usage</span>
    TrafficLight signal = TrafficLight::GREEN;
    <span class="c-keyword">if</span> (signal == TrafficLight::GREEN) {
        std::cout &lt;&lt; <span class="c-string">"Traffic Light is GREEN: Vehicles proceed.\\n"</span>;
    }

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Enumeration Discrete Value Mapping vs Raw Integer Domain</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- Raw Int Box -->
      <g transform="translate(40, 40)">
        <rect width="320" height="140" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="2"/>
        <text x="160" y="28" fill="#ef4444" font-size="13" font-weight="bold" text-anchor="middle">Raw int (Unrestricted Range)</text>
        <text x="160" y="60" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Domain: -2,147,483,648 to +2,147,483,647</text>
        <text x="160" y="90" fill="#ef4444" font-size="11" font-weight="600" text-anchor="middle">Dangerous: Accepts -99, 500, 88888 for a 'Day'</text>
        <text x="160" y="115" fill="var(--text-primary)" font-size="10" text-anchor="middle">Zero Type Safety • High Bug Risk</text>
      </g>

      <!-- Arrow -->
      <path d="M 375 110 L 415 110" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-flow)"/>

      <!-- Enum Box -->
      <g transform="translate(430, 40)">
        <rect width="290" height="140" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="2"/>
        <text x="145" y="28" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">enum Days (Restricted Discrete Set)</text>
        <text x="145" y="60" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">{ Sun, Mon, Tue, Wed, Thu, Fri, Sat }</text>
        <text x="145" y="90" fill="#10b981" font-size="11" font-weight="600" text-anchor="middle">Guaranteed: Only 0 through 6 accepted</text>
        <text x="145" y="115" fill="var(--text-primary)" font-size="10" text-anchor="middle">Full Compile-Time Validation • Self-Documenting</text>
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
    <li><span class="check-box"></span> What integer value is assigned to the first enumerator if not explicitly initialized? (<code>0</code>).</li>
    <li><span class="check-box"></span> Write the syntax for declaring an enum of the days of the week.</li>
    <li><span class="check-box"></span> What are the two primary advantages of <code>enum class</code> over classic <code>enum</code>? (Scoped names, no implicit integer conversion).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> In short questions (2 marks), examiners routinely ask: <em>"What is an enumeration? Write its syntax."</em> Always provide the <code>enum days { Sun, Mon, Tue, Wed, Thu, Fri, Sat };</code> example as specified directly in the AKTU Quantum guide.
</div>
"""
    sections.append({
        "id": "u4-sec-7",
        "number": 7,
        "part": "PART 1 — C++ BASICS",
        "title": "7. Enumeration — enum & Scoped Enumerators",
        "subtitle": "Restricted Domain Typing, Days of the Week Implementation, enum vs int Trade-offs & Scoped enum class",
        "content": sec7_content
    })

    # =========================================================================
    # SECTION 8: Operators in C++ & Memory Management
    # =========================================================================
    sec8_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">8. Operators in C++ &amp; Memory Management (new/delete)</h3>
  </div>

  <div class="detail-block">
    <h5>8.1 Primary Operator Categories in C++</h5>
    <p>
      C++ inherits all standard C operators (arithmetic, relational, logical, bitwise, assignment) while introducing specialized language-level operators tested in AKTU examinations:
    </p>
  </div>

  <div class="detail-block">
    <h5>8.2 Dynamic Memory Management Operators: <code>new</code> &amp; <code>delete</code></h5>
    <p>
      Unlike C which relies on library subroutines (<code>malloc()</code> and <code>free()</code> from <code>stdlib.h</code>), C++ provides native, type-safe unary operators:
    </p>
    <ul>
      <li><strong>The <code>new</code> Operator:</strong>
        <ul>
          <li>Calculates byte size automatically based on type.</li>
          <li>Returns a correctly typed pointer (no clumsy casting required like <code>(int*)malloc(...)</code>).</li>
          <li><strong>Crucial:</strong> Automatically invokes the object's <strong>constructor</strong> to initialize state.</li>
          <li>Throws <code>std::bad_alloc</code> exception if heap memory is exhausted (instead of returning <code>NULL</code>).</li>
          <li><em>Single Object:</em> <code>int* p = new int(100);</code></li>
          <li><em>Array Allocation:</em> <code>int* arr = new int[50];</code></li>
        </ul>
      </li>
      <li><strong>The <code>delete</code> Operator:</strong>
        <ul>
          <li>Deallocates heap memory occupied by the target object.</li>
          <li><strong>Crucial:</strong> Automatically invokes the object's <strong>destructor</strong> before freeing bytes.</li>
          <li><em>Single Object:</em> <code>delete p;</code></li>
          <li><em>Array Deallocation:</em> <code>delete[] arr;</code> (The square brackets ensure destructors are invoked for <em>every</em> element in the array).</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>8.3 Stream Manipulator Operators (Formatting Output)</h5>
    <p>
      Manipulators are specialized operators and helper functions passed to stream insertion (<code>&lt;&lt;</code>) and extraction (<code>&gt;&gt;</code>) operators to format data:
    </p>
    <ul>
      <li><code>endl</code>: Inserts a newline character (<code>'\\n'</code>) and immediately flushes the output stream buffer.</li>
      <li><code>setw(int n)</code> (Header <code>&lt;iomanip&gt;</code>): Sets the minimum field width for the next display item.</li>
      <li><code>setfill(char c)</code>: Fills unused padding spaces with character <code>c</code>.</li>
      <li><code>setprecision(int n)</code>: Controls the number of decimal digits for floating-point values.</li>
      <li><code>fixed</code>: Forces fixed-point floating-point representation.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>8.4 Specialized C++ Operators</h5>
    <ul>
      <li><strong>Scope Resolution Operator (<code>::</code>):</strong> Accesses global variables obscured by local names (<code>::x</code>), accesses static class members, and binds method definitions to classes.</li>
      <li><strong>Pointer-to-Member Operators:</strong> <code>.*</code> (dereference member through object) and <code>-&gt;*</code> (dereference member through pointer to object).</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Hotel Room Key Reservation & Maid Checkout</span>
  </div>
  <p>
    Think of <strong>Stack memory</strong> as taking a seat in a lecture hall: you sit down when the lecture starts, and when the bell rings (function returns), you get up—zero administrative paperwork.<br>
    <strong>Heap memory with <code>new</code></strong> is like checking into a luxury <strong>Hotel Room</strong>: the front desk gives you a room key card (pointer to memory), and the concierge cleans and prepares the bed with fresh sheets (constructor runs).<br>
    If you leave the hotel without returning the key and checking out with <strong><code>delete</code></strong>, the room stays reserved forever, locked and wasted—a <strong>Memory Leak</strong>! Calling <code>delete</code> lets the hotel clean up (destructor runs) and lease the room to future guests.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Dynamic Memory Lifecycle with new/delete & Table Formatting with iomanip</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;iomanip&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> StudentRecord {
<span class="c-keyword">public</span>:
    <span class="c-type">std::string</span> name;
    <span class="c-type">double</span> gpa;

    StudentRecord(<span class="c-type">std::string</span> n, <span class="c-type">double</span> g) : name(n), gpa(g) {
        std::cout &lt;&lt; <span class="c-string">"[Constructor]: Allocating record for "</span> &lt;&lt; name &lt;&lt; <span class="c-string">"\\n"</span>;
    }

    ~StudentRecord() {
        std::cout &lt;&lt; <span class="c-string">"[Destructor]: Deallocating record for "</span> &lt;&lt; name &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. Dynamic Single Object Allocation</span>
    StudentRecord* s1 = <span class="c-keyword">new</span> StudentRecord(<span class="c-string">"Aarav Mehta"</span>, <span class="c-number">9.45</span>);

    <span class="c-comment">// 2. Dynamic Array Allocation</span>
    <span class="c-type">int</span> size = <span class="c-number">3</span>;
    <span class="c-type">int</span>* scores = <span class="c-keyword">new</span> <span class="c-type">int</span>[size]{<span class="c-number">88</span>, <span class="c-number">92</span>, <span class="c-number">96</span>};

    <span class="c-comment">// 3. Output Formatting with iomanip Manipulators</span>
    std::cout &lt;&lt; <span class="c-string">"\\n=== Formatted Student Marksheet ===\\n"</span>;
    std::cout &lt;&lt; std::left &lt;&lt; std::setw(<span class="c-number">15</span>) &lt;&lt; <span class="c-string">"Subject"</span> 
              &lt;&lt; std::right &lt;&lt; std::setw(<span class="c-number">10</span>) &lt;&lt; <span class="c-string">"Score"</span> &lt;&lt; std::endl;
    std::cout &lt;&lt; std::setfill(<span class="c-string">'-'</span>) &lt;&lt; std::setw(<span class="c-number">25</span>) &lt;&lt; <span class="c-string">""</span> &lt;&lt; std::setfill(<span class="c-string">' '</span>) &lt;&lt; std::endl;

    std::cout &lt;&lt; std::left &lt;&lt; std::setw(<span class="c-number">15</span>) &lt;&lt; <span class="c-string">"Maths"</span> 
              &lt;&lt; std::right &lt;&lt; std::setw(<span class="c-number">10</span>) &lt;&lt; scores[<span class="c-number">0</span>] &lt;&lt; std::endl;
    std::cout &lt;&lt; std::left &lt;&lt; std::setw(<span class="c-number">15</span>) &lt;&lt; <span class="c-string">"Algorithms"</span> 
              &lt;&lt; std::right &lt;&lt; std::setw(<span class="c-number">10</span>) &lt;&lt; scores[<span class="c-number">1</span>] &lt;&lt; std::endl;
    std::cout &lt;&lt; std::left &lt;&lt; std::setw(<span class="c-number">15</span>) &lt;&lt; <span class="c-string">"OOSD"</span> 
              &lt;&lt; std::right &lt;&lt; std::setw(<span class="c-number">10</span>) &lt;&lt; scores[<span class="c-number">2</span>] &lt;&lt; std::endl;

    <span class="c-comment">// 4. Proper Cleanup (Crucial to prevent leaks)</span>
    <span class="c-keyword">delete</span> s1;          <span class="c-comment">// Invokes StudentRecord destructor</span>
    <span class="c-keyword">delete</span>[] scores;    <span class="c-comment">// Deallocates array storage</span>

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="comparison-table-wrapper">
  <h4>Comparative Matrix: C malloc/free vs C++ new/delete</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Evaluation Metric</th>
        <th>C <code>malloc()</code> / <code>free()</code></th>
        <th>C++ <code>new</code> / <code>delete</code></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Language Construct</strong></td>
        <td>Library Functions (Declared in <code>&lt;stdlib.h&gt;</code>)</td>
        <td>Built-in Language Operators (Keywords)</td>
      </tr>
      <tr>
        <td><strong>Constructor / Destructor</strong></td>
        <td>Never invoked (Allocates raw uninitialized memory)</td>
        <td>Automatically invokes Constructor on <code>new</code> &amp; Destructor on <code>delete</code></td>
      </tr>
      <tr>
        <td><strong>Return Type &amp; Casting</strong></td>
        <td>Returns <code>void*</code>; requires manual typecast</td>
        <td>Returns exact type pointer; fully type-safe</td>
      </tr>
      <tr>
        <td><strong>Byte Size Computation</strong></td>
        <td>Manual via <code>sizeof(type) * count</code></td>
        <td>Automatic by compiler based on target type</td>
      </tr>
      <tr>
        <td><strong>Failure Handling</strong></td>
        <td>Returns <code>NULL</code> pointer on failure</td>
        <td>Throws <code>std::bad_alloc</code> exception</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Dynamic Memory Allocation Lifecycle (new[] &amp; delete[])</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
      <!-- Stack Pointer -->
      <g transform="translate(40, 25)">
        <rect width="180" height="160" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="90" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Stack Segment</text>
        <rect x="15" y="50" width="150" height="40" rx="4" fill="var(--bg-card)" stroke="var(--border-default)"/>
        <text x="90" y="70" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">int* ptr</text>
        <text x="90" y="85" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">0x10A240</text>
        <text x="90" y="125" fill="var(--text-muted)" font-size="10" text-anchor="middle">Address: 0x7FFE40</text>
        <text x="90" y="145" fill="var(--accent-blue)" font-size="10" text-anchor="middle">Size: 8 Bytes</text>
      </g>

      <!-- Dynamic Heap Array -->
      <g transform="translate(300, 25)">
        <rect width="420" height="160" rx="8" fill="var(--bg-card)" stroke="#10b981" stroke-width="1.5"/>
        <text x="210" y="30" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Free Store (Heap Memory Segment)</text>
        <!-- 5 Array Slots -->
        <g transform="translate(20, 50)">
          <rect x="0" y="0" width="70" height="50" fill="var(--bg-elevated)" stroke="#10b981"/>
          <text x="35" y="25" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">ptr[0]</text>
          <text x="35" y="42" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">10</text>

          <rect x="75" y="0" width="70" height="50" fill="var(--bg-elevated)" stroke="#10b981"/>
          <text x="110" y="25" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">ptr[1]</text>
          <text x="110" y="42" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">20</text>

          <rect x="150" y="0" width="70" height="50" fill="var(--bg-elevated)" stroke="#10b981"/>
          <text x="185" y="25" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">ptr[2]</text>
          <text x="185" y="42" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">30</text>

          <rect x="225" y="0" width="70" height="50" fill="var(--bg-elevated)" stroke="#10b981"/>
          <text x="260" y="25" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">ptr[3]</text>
          <text x="260" y="42" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">40</text>

          <rect x="300" y="0" width="70" height="50" fill="var(--bg-elevated)" stroke="#10b981"/>
          <text x="335" y="25" fill="var(--text-primary)" font-family="monospace" font-size="11" text-anchor="middle">ptr[4]</text>
          <text x="335" y="42" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">50</text>
        </g>
        <text x="210" y="130" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Contiguous 20 Bytes Allocated via new int[5]</text>
        <text x="210" y="148" fill="#ef4444" font-size="10" text-anchor="middle">Reclaimed cleanly to free pool via delete[] ptr</text>
      </g>

      <!-- Connecting Pointer Arrow -->
      <path d="M 220 95 L 300 95" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)"/>
    </svg>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> What is the syntax for deallocating an array allocated with <code>new[]</code>? (<code>delete[] ptr;</code>).</li>
    <li><span class="check-box"></span> Which header file is required to use <code>setw</code> and <code>setfill</code>? (<code>&lt;iomanip&gt;</code>).</li>
    <li><span class="check-box"></span> Name at least 3 fundamental advantages of <code>new</code> over <code>malloc()</code>.</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"Compare malloc vs new and free vs delete"</em> (classic 5 or 10-mark question), write the comparison table above. Highlight that <strong>constructors and destructors are invoked</strong> by C++ operators, which is impossible with C library calls.
</div>
"""
    sections.append({
        "id": "u4-sec-8",
        "number": 8,
        "part": "PART 1 — C++ BASICS",
        "title": "8. Operators in C++ & Memory Management",
        "subtitle": "new/delete Lifecycle, Array Allocation, Stream Manipulators (setw, endl) & Scope Resolution (::)",
        "content": sec8_content
    })

    # =========================================================================
    # SECTION 9: Typecasting / Type Conversion
    # =========================================================================
    sec9_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">9. Typecasting, The 4 Modern Casts &amp; typeid</h3>
  </div>

  <div class="detail-block">
    <h5>9.1 Meaning of Type Conversion</h5>
    <p>
      <strong>Type Conversion (Typecasting)</strong> is the process of converting an expression from its current data type into another destination data type.
    </p>
  </div>

  <div class="detail-block">
    <h5>9.2 Implicit vs Explicit Conversion</h5>
    <ul>
      <li><strong>Implicit Conversion (Type Coercion):</strong> Executed automatically by the compiler without data loss during expression evaluation. Narrower types are promoted to wider types (e.g., <code>short a = 2000; int b = a;</code> or <code>int + double &rarr; double</code>).</li>
      <li><strong>Explicit Conversion:</strong> Commanded deliberately by the programmer when a potentially lossy transformation or pointer reinterpretation is intended (e.g. converting <code>double 5.7</code> to <code>int 5</code>).</li>
      <li><strong>Legacy C-Style Cast:</strong> <code>(int) 5.7</code> or function-style <code>int(5.7)</code>. Highly discouraged in professional C++ because it acts as an unchecked sledgehammer combining static, const, and reinterpret casts without compiler safety verification.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>9.3 The Four Modern C++ Named Cast Operators</h5>
    <p>
      The AKTU syllabus heavily tests the 4 distinct, type-safe casting operators introduced to replace C-style casts:
    </p>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6><code>static_cast&lt;TargetType&gt;(expr)</code></h6>
          <p>Performs well-defined, compile-time reversible conversions. Used for numeric conversions (e.g., <code>double</code> to <code>int</code>), converting <code>void*</code> back to typed pointers, and safe upcasts in an inheritance tree.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6><code>dynamic_cast&lt;TargetType&gt;(expr)</code></h6>
          <p>Performs runtime-checked polymorphic downcasting across inheritance hierarchies. Inspects the object's Virtual Table (vtable). Returns <code>nullptr</code> if a pointer cast fails, or throws <code>std::bad_cast</code> for references. <strong>Requirement: Base class must possess at least one virtual function!</strong></p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">3</span>
        <div class="step-content">
          <h6><code>const_cast&lt;TargetType&gt;(expr)</code></h6>
          <p>Exclusively used to add or remove <code>const</code> or <code>volatile</code> qualifiers from a pointer or reference. Modifying a truly constant object after stripping constness invokes undefined behavior.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">4</span>
        <div class="step-content">
          <h6><code>reinterpret_cast&lt;TargetType&gt;(expr)</code></h6>
          <p>Low-level, non-portable reinterpretation of raw binary bit patterns (e.g., casting an integer memory address to a pointer or converting between unrelated pointer types). Used in drivers, network packet parsing, and memory managers.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="detail-block">
    <h5>9.4 Runtime Type Information (RTTI) &amp; <code>typeid</code></h5>
    <p>
      The <code>typeid</code> operator (defined in <code>&lt;typeinfo&gt;</code>) queries the exact runtime type of an expression. It returns a reference to a <code>std::type_info</code> object providing member functions like <code>.name()</code>. When applied to a polymorphic base pointer, <code>typeid(*ptr)</code> resolves to the concrete derived type at runtime!
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The International Electrical Adapter Kit</span>
  </div>
  <p>
    Think of typecasting as fitting electrical plugs into international wall sockets:
    <br>&bull; <strong>Implicit Conversion:</strong> Like plugging a standard dual-voltage phone charger (110V-240V) into a European outlet—it adapts automatically without manual tools.
    <br>&bull; <strong><code>static_cast</code>:</strong> A certified, standardized travel adapter (US 2-pin to UK 3-pin). It fits cleanly because the shapes and voltages are mathematically documented and checked.
    <br>&bull; <strong><code>dynamic_cast</code>:</strong> A smart surge protector with a built-in sensor: it tests the live circuit first. If it detects a compatible voltage (valid derived class), it delivers power; if incompatible, it flips the circuit breaker safely (returns <code>nullptr</code>) to prevent a fire.
    <br>&bull; <strong><code>const_cast</code>:</strong> Stripping the "Do Not Touch" inspection seal off a piece of machinery.
    <br>&bull; <strong><code>reinterpret_cast</code>:</strong> Splicing raw copper wires directly into a 10,000-volt high-tension electrical line with bare hands. It works if you know exactly what you are doing, but one slip electrocutes the entire system!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Testing All 4 Named Casts and typeid in a Class Hierarchy</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;typeinfo&gt;</span>

<span class="c-comment">// Polymorphic Base Class</span>
<span class="c-keyword">class</span> Shape {
<span class="c-keyword">public</span>:
    <span class="c-keyword">virtual</span> ~Shape() = <span class="c-keyword">default</span>; <span class="c-comment">// Ensures vtable generation for dynamic_cast</span>
    <span class="c-keyword">virtual</span> <span class="c-type">void</span> draw() <span class="c-keyword">const</span> { std::cout &lt;&lt; <span class="c-string">"Drawing Shape\\n"</span>; }
};

<span class="c-keyword">class</span> Circle : <span class="c-keyword">public</span> Shape {
<span class="c-keyword">public</span>:
    <span class="c-type">void</span> draw() <span class="c-keyword">const</span> <span class="c-keyword">override</span> { std::cout &lt;&lt; <span class="c-string">"Drawing Circle\\n"</span>; }
    <span class="c-type">void</span> roll() <span class="c-keyword">const</span> { std::cout &lt;&lt; <span class="c-string">"Rolling circle across canvas!\\n"</span>; }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. static_cast: Compile-time conversion</span>
    <span class="c-type">double</span> rawGpa = <span class="c-number">8.75</span>;
    <span class="c-type">int</span> roundedGpa = <span class="c-keyword">static_cast</span>&lt;<span class="c-type">int</span>&gt;(rawGpa);
    std::cout &lt;&lt; <span class="c-string">"static_cast: "</span> &lt;&lt; rawGpa &lt;&lt; <span class="c-string">" -&gt; "</span> &lt;&lt; roundedGpa &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// 2. dynamic_cast: Safe runtime polymorphic downcasting</span>
    Shape* polyPtr = <span class="c-keyword">new</span> Circle();
    Circle* circlePtr = <span class="c-keyword">dynamic_cast</span>&lt;Circle*&gt;(polyPtr);

    <span class="c-keyword">if</span> (circlePtr) {
        std::cout &lt;&lt; <span class="c-string">"dynamic_cast SUCCESS: Pointer safely resolved to Circle!\\n"</span>;
        circlePtr-&gt;roll();
    }

    <span class="c-comment">// 3. const_cast: Removing const qualifier</span>
    <span class="c-keyword">const</span> <span class="c-type">int</span> secretPin = <span class="c-number">4321</span>;
    <span class="c-type">int</span>* mutablePinPtr = <span class="c-keyword">const_cast</span>&lt;<span class="c-type">int</span>*&gt;(&amp;secretPin);
    std::cout &lt;&lt; <span class="c-string">"const_cast: Address inspected: "</span> &lt;&lt; mutablePinPtr &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// 4. reinterpret_cast: Raw pointer to integer bit conversion</span>
    <span class="c-type">uintptr_t</span> memoryAddress = <span class="c-keyword">reinterpret_cast</span>&lt;<span class="c-type">uintptr_t</span>&gt;(polyPtr);
    std::cout &lt;&lt; <span class="c-string">"reinterpret_cast: Memory Pointer as Integer: 0x"</span> 
              &lt;&lt; std::hex &lt;&lt; memoryAddress &lt;&lt; std::dec &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// 5. typeid RTTI Inspection</span>
    std::cout &lt;&lt; <span class="c-string">"typeid(*polyPtr) Runtime Name: "</span> &lt;&lt; <span class="c-keyword">typeid</span>(*polyPtr).name() &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">delete</span> polyPtr;
    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="comparison-table-wrapper">
  <h4>Comparative Matrix: The 4 Modern C++ Named Casts</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Cast Operator</th>
        <th>Checking Phase</th>
        <th>Runtime Overhead</th>
        <th>Primary Use Case &amp; Safety</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>static_cast</code></td>
        <td>Compile-Time</td>
        <td>Zero</td>
        <td>Numeric conversions, reversing implicit conversions, safe conversions.</td>
      </tr>
      <tr>
        <td><code>dynamic_cast</code></td>
        <td>Runtime (RTTI)</td>
        <td>Yes (vtable traversal)</td>
        <td>Downcasting polymorphic base pointers to derived classes; returns <code>nullptr</code> on failure.</td>
      </tr>
      <tr>
        <td><code>const_cast</code></td>
        <td>Compile-Time</td>
        <td>Zero</td>
        <td>Adding or stripping <code>const</code>/<code>volatile</code> qualifiers.</td>
      </tr>
      <tr>
        <td><code>reinterpret_cast</code></td>
        <td>Compile-Time</td>
        <td>Zero</td>
        <td>Low-level bit reinterpretation between unrelated types. Dangerous.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: The Four Modern C++ Casts &amp; Safety Hierarchy</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(15, 15)">
        <!-- 1. static_cast -->
        <rect x="0" y="0" width="170" height="165" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="85" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">static_cast&lt;T&gt;</text>
        <rect x="12" y="42" width="146" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="85" y="58" fill="var(--text-primary)" font-size="10" text-anchor="middle">Compile-Time Check</text>
        <text x="85" y="70" fill="#10b981" font-size="9" text-anchor="middle">&amp;#x2713; Zero Runtime Cost</text>
        <text x="85" y="105" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Numeric conversions</text>
        <text x="85" y="122" fill="var(--text-secondary)" font-size="10" text-anchor="middle">void* to typed ptr</text>
        <text x="85" y="145" fill="var(--accent-blue)" font-size="9" text-anchor="middle">Safe Upcasts</text>

        <!-- 2. dynamic_cast -->
        <rect x="185" y="0" width="170" height="165" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="1.5"/>
        <text x="270" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">dynamic_cast&lt;T&gt;</text>
        <rect x="197" y="42" width="146" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="270" y="58" fill="var(--text-primary)" font-size="10" text-anchor="middle">Run-Time RTTI Check</text>
        <text x="270" y="70" fill="#f59e0b" font-size="9" text-anchor="middle">VTable Lookup Cost</text>
        <text x="270" y="105" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Safe Downcasting</text>
        <text x="270" y="122" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Requires Virtual Base</text>
        <text x="270" y="145" fill="#10b981" font-size="9" text-anchor="middle">Returns nullptr on fail</text>

        <!-- 3. const_cast -->
        <rect x="370" y="0" width="170" height="165" rx="8" fill="var(--bg-elevated)" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="455" y="28" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">const_cast&lt;T&gt;</text>
        <rect x="382" y="42" width="146" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="455" y="58" fill="var(--text-primary)" font-size="10" text-anchor="middle">Qualifier Modification</text>
        <text x="455" y="70" fill="#10b981" font-size="9" text-anchor="middle">&amp;#x2713; Zero Runtime Cost</text>
        <text x="455" y="105" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Strips const / volatile</text>
        <text x="455" y="122" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Legacy C library calls</text>
        <text x="455" y="145" fill="#ef4444" font-size="9" text-anchor="middle">Modifying const is UB</text>

        <!-- 4. reinterpret_cast -->
        <rect x="555" y="0" width="170" height="165" rx="8" fill="var(--bg-elevated)" stroke="#ef4444" stroke-width="1.5"/>
        <text x="640" y="28" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">reinterpret_cast&lt;T&gt;</text>
        <rect x="567" y="42" width="146" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="640" y="58" fill="var(--text-primary)" font-size="10" text-anchor="middle">Raw Bit Pattern Cast</text>
        <text x="640" y="70" fill="#10b981" font-size="9" text-anchor="middle">&amp;#x2713; Zero Runtime Cost</text>
        <text x="640" y="105" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Pointer to / from Int</text>
        <text x="640" y="122" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Device Drivers / DMA</text>
        <text x="640" y="145" fill="#ef4444" font-size="9" text-anchor="middle">Non-portable / Unsafe</text>
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
    <li><span class="check-box"></span> What does <code>dynamic_cast</code> return when pointer downcasting fails? (<code>nullptr</code>).</li>
    <li><span class="check-box"></span> What prerequisite must a base class satisfy to support <code>dynamic_cast</code>? (Must contain at least one virtual function).</li>
    <li><span class="check-box"></span> Which cast operator is used exclusively to strip constness? (<code>const_cast</code>).</li>
    <li><span class="check-box"></span> Which header file is required to invoke the <code>typeid</code> operator? (<code>&lt;typeinfo&gt;</code>).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Questions asking <em>"Explain different types of typecasting operators in C++ with examples"</em> appear in almost every semester exam. Always explain <code>static_cast</code>, <code>dynamic_cast</code>, <code>const_cast</code>, <code>reinterpret_cast</code>, and mention <code>typeid</code> with the comparison matrix.
</div>
"""
    sections.append({
        "id": "u4-sec-9",
        "number": 9,
        "part": "PART 1 — C++ BASICS",
        "title": "9. Typecasting, The 4 Modern Casts & typeid",
        "subtitle": "Implicit Coercion, Explicit Conversion, static_cast, dynamic_cast (RTTI), const_cast, reinterpret_cast & typeid",
        "content": sec9_content
    })

    # =========================================================================
    # SECTION 10: Control Structures
    # =========================================================================
    sec10_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">10. Control Structures: Decision Making &amp; Looping Mechanisms</h3>
  </div>

  <div class="detail-block">
    <h5>10.1 Taxonomy of Control Structures</h5>
    <p>
      In structured programming theory (Böhm-Jacopini theorem), all computable algorithms can be expressed using three foundational control patterns: <strong>Sequence</strong>, <strong>Selection (Decision)</strong>, and <strong>Iteration (Repetition)</strong>.
    </p>
  </div>

  <div class="detail-block">
    <h5>10.2 Decision Making Statements</h5>
    <ul>
      <li><strong>Simple <code>if</code> Statement:</strong> Executes a single branch if a boolean condition evaluates to <code>true</code>.</li>
      <li><strong><code>if-else</code> Statement:</strong> Provides mutually exclusive two-way branching: executes block 1 if true, block 2 if false.</li>
      <li><strong>Cascaded <code>if-else if-else</code> Ladder:</strong> Evaluates sequential mutually exclusive conditions from top to bottom.</li>
      <li><strong><code>switch</code> Statement (Multiple Branching):</strong>
        <ul>
          <li>Evaluates an integral or character expression and matches it against discrete <code>case</code> constant labels.</li>
          <li><strong>The <code>break</code> Statement:</strong> Halts execution and jumps out of the switch block. Omitting <code>break</code> causes intentional or unintentional <strong>Fall-Through</strong> to subsequent cases.</li>
          <li><strong>The <code>default</code> Label:</strong> Catch-all execution branch executed when no case label matches.</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>10.3 Iteration (Looping) Structures: Entry vs Exit Controlled</h5>
    <p>
      A core AKTU theoretical question hinges on distinguishing <strong>Entry-Controlled</strong> vs <strong>Exit-Controlled</strong> loops:
    </p>
    <ul>
      <li><strong>Entry-Controlled Loops (Pre-Test):</strong> The loop condition is evaluated <em>BEFORE</em> the body executes. If the initial condition is false, the loop body executes <strong>ZERO times</strong>.
        <ul>
          <li><code>while(condition) { ... }</code>: Used when the number of iterations is unknown in advance and depends on dynamic state.</li>
          <li><code>for(init; condition; step) { ... }</code>: Used when loop boundaries (initialization, termination bound, increment step) are well-defined.</li>
        </ul>
      </li>
      <li><strong>Exit-Controlled Loops (Post-Test):</strong> The loop body executes <em>FIRST</em>, and the condition is evaluated at the end.
        <ul>
          <li><code>do { ... } while(condition);</code>: Guarantees that the body executes <strong>AT LEAST ONCE</strong>, regardless of whether the condition is true or false initially. Ideal for menu-driven CLI interfaces.</li>
        </ul>
      </li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Movie Theater Ticket Gate vs Restaurant Dining</span>
  </div>
  <p>
    &bull; <strong>Entry-Controlled Loop (<code>while</code> / <code>for</code>):</strong> Like entering a <strong>Movie Cinema</strong>. The usher checks your ticket <em>at the door</em> before you enter. If you don't have a valid ticket, you watch 0 minutes of the movie.<br>
    &bull; <strong>Exit-Controlled Loop (<code>do-while</code>):</strong> Like dining at an upscale <strong>Restaurant</strong>. You walk in, sit down, and eat your meal first (body executes at least once). The waiter presents the bill <em>at the exit door</em> before you leave.
  </p>
</div>

<div class="comparison-table-wrapper">
  <h4>AKTU Master Comparison Table: Control Structures Architecture</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Statement</th>
        <th>Control Category</th>
        <th>Condition Evaluation Timing</th>
        <th>Minimum Iteration Count</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>if / if-else</code></td>
        <td>Selection / Decision</td>
        <td>Evaluated once before branch entry</td>
        <td>N/A (Executes branch 0 or 1 time)</td>
      </tr>
      <tr>
        <td><code>switch</code></td>
        <td>Multiple Branching</td>
        <td>Single expression evaluated against cases</td>
        <td>N/A (Jumps to matching label)</td>
      </tr>
      <tr>
        <td><code>while</code></td>
        <td>Entry-Controlled Loop</td>
        <td>Pre-test: Checked before body entry</td>
        <td><strong>0 times</strong> (Can skip entirely)</td>
      </tr>
      <tr>
        <td><code>do-while</code></td>
        <td>Exit-Controlled Loop</td>
        <td>Post-test: Checked after body execution</td>
        <td><strong>1 time</strong> (Guaranteed execution)</td>
      </tr>
      <tr>
        <td><code>for</code></td>
        <td>Entry-Controlled Loop</td>
        <td>Pre-test: Checked before each iteration</td>
        <td><strong>0 times</strong> (Can skip entirely)</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Demonstrating switch Fall-Through & while vs do-while Execution Bounds</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-type">int</span> main() {
    <span class="c-comment">// 1. switch Statement for Grade Evaluation</span>
    <span class="c-type">char</span> studentGrade = <span class="c-string">'A'</span>;
    std::cout &lt;&lt; <span class="c-string">"=== Testing switch Statement ===\\n"</span>;
    <span class="c-keyword">switch</span> (studentGrade) {
        <span class="c-keyword">case</span> <span class="c-string">'A'</span>:
            std::cout &lt;&lt; <span class="c-string">"Grade A: Outstanding Academic Performance!\\n"</span>;
            <span class="c-keyword">break</span>;
        <span class="c-keyword">case</span> <span class="c-string">'B'</span>:
            std::cout &lt;&lt; <span class="c-string">"Grade B: Good Effort.\\n"</span>;
            <span class="c-keyword">break</span>;
        <span class="c-keyword">default</span>:
            std::cout &lt;&lt; <span class="c-string">"Grade Other: Keep Practicing.\\n"</span>;
            <span class="c-keyword">break</span>;
    }

    <span class="c-comment">// 2. Comparing while vs do-while with FALSE condition</span>
    <span class="c-type">int</span> counter = <span class="c-number">100</span>;

    std::cout &lt;&lt; <span class="c-string">"\\n=== Testing while (Pre-Test) ===\\n"</span>;
    <span class="c-keyword">while</span> (counter &lt; <span class="c-number">10</span>) {
        std::cout &lt;&lt; <span class="c-string">"This line will NEVER execute!\\n"</span>;
    }
    std::cout &lt;&lt; <span class="c-string">"while loop bypassed completely because initial condition was false.\\n"</span>;

    std::cout &lt;&lt; <span class="c-string">"\\n=== Testing do-while (Post-Test) ===\\n"</span>;
    <span class="c-keyword">do</span> {
        std::cout &lt;&lt; <span class="c-string">"do-while body executes ONCE even though counter (100) &lt; 10 is false!\\n"</span>;
    } <span class="c-keyword">while</span> (counter &lt; <span class="c-number">10</span>);

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Entry-Controlled vs Exit-Controlled Loop Execution Flow</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <!-- While Loop -->
      <g transform="translate(40, 25)">
        <rect width="320" height="200" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="160" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Entry-Controlled (while / for)</text>
        
        <polygon points="160,40 230,70 160,100 90,70" fill="var(--bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="160" y="74" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Condition?</text>

        <path d="M 160 100 L 160 135" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-blue)"/>
        <text x="175" y="120" fill="#10b981" font-size="10" font-weight="bold">TRUE</text>

        <rect x="100" y="135" width="120" height="35" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
        <text x="160" y="157" fill="var(--text-primary)" font-size="11" text-anchor="middle">Loop Body</text>

        <path d="M 230 70 L 290 70 L 290 190 L 160 190" stroke="#ef4444" stroke-width="1.5"/>
        <text x="250" y="62" fill="#ef4444" font-size="10" font-weight="bold">FALSE</text>
        <text x="225" y="205" fill="#ef4444" font-size="10" text-anchor="middle">Exit: Minimum 0 Executions</text>
      </g>

      <!-- Do-While Loop -->
      <g transform="translate(400, 25)">
        <rect width="320" height="200" rx="8" fill="var(--bg-elevated)" stroke="#a855f7" stroke-width="2"/>
        <text x="160" y="24" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">Exit-Controlled (do-while)</text>

        <rect x="100" y="45" width="120" height="35" rx="4" fill="var(--bg-card)" stroke="#10b981"/>
        <text x="160" y="67" fill="var(--text-primary)" font-size="11" text-anchor="middle">Loop Body</text>

        <path d="M 160 80 L 160 105" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-blue)"/>

        <polygon points="160,105 230,135 160,165 90,135" fill="var(--bg-card)" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="160" y="139" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Condition?</text>

        <path d="M 90 135 L 50 135 L 50 62 L 95 62" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrow-blue)"/>
        <text x="70" y="125" fill="#10b981" font-size="10" font-weight="bold">TRUE</text>

        <path d="M 160 165 L 160 195" stroke="#ef4444" stroke-width="1.5"/>
        <text x="180" y="185" fill="#ef4444" font-size="10" font-weight="bold">FALSE</text>
        <text x="210" y="205" fill="#10b981" font-size="10" text-anchor="middle">Exit: Guaranteed ≥ 1 Execution</text>
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
    <li><span class="check-box"></span> Why is <code>while</code> classified as an entry-controlled loop? (Condition checked before body entry).</li>
    <li><span class="check-box"></span> What happens if a <code>break</code> statement is omitted in a <code>switch</code> case? (Execution falls through into subsequent cases).</li>
    <li><span class="check-box"></span> What is the minimum number of times a <code>do-while</code> loop executes? (Exactly 1 time).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"Differentiate between while and do-while loops with examples"</em>, make sure to write: 1. Condition evaluation point (Entry vs Exit), 2. Minimum iterations (0 vs 1), and 3. Provide the counter = 100 test code snippet demonstrating do-while executing once while while executes zero times.
</div>
"""
    sections.append({
        "id": "u4-sec-10",
        "number": 10,
        "part": "PART 1 — C++ BASICS",
        "title": "10. Control Structures: Decisions & Loops",
        "subtitle": "Selection Branching (if, switch), Loop Paradigms (for, while, do-while), Entry vs Exit Control & Flow Matrix",
        "content": sec10_content
    })

    # =========================================================================
    # SECTION 11: Basic C++ Programming Problems
    # =========================================================================
    sec11_content = r"""
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">11. Classical C++ Programming Problems &amp; Algorithms</h3>
  </div>

  <div class="detail-block">
    <h5>11.1 The Classical AKTU Practical &amp; Theory Problems</h5>
    <p>
      The AKTU examination frequently includes practical coding questions in Unit 4. Students must be prepared to write complete, working programs covering:
    </p>
    <ol>
      <li><strong>Mathematical Series:</strong> Computing Taylor/Maclaurin series expansions for $\\sin(x)$ and $\\cos(x)$ without using standard <code>pow()</code> or <code>tgamma()</code>.</li>
      <li><strong>String Processing:</strong> Counting frequency of vowels in a user sentence and identifying the longest word.</li>
      <li><strong>Numeric Algorithms:</strong> Prime number testing, Fibonacci generation, and Matrix multiplication.</li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>11.2 Mathematical Derivation: Taylor Series Recurrence Formulation</h5>
    <p>
      The Taylor series expansion for $\\sin(x)$ around $x = 0$ is given by:
    </p>
    <div class="code-box"><code>sin(x) = x - (x^3 / 3!) + (x^5 / 5!) - (x^7 / 7!) + ...</code></div>
    <p>
      Calculating factorials directly (e.g. $15!$) causes catastrophic 64-bit integer overflow. The efficient algorithm uses the <strong>Recurrence Relation</strong> between term $i$ and term $i-1$:
    </p>
    <div class="code-box"><code>Term(i) = -Term(i-1) * (x^2) / ( (2*i) * (2*i + 1) )</code></div>
    <p>
      This yields an optimal $O(N)$ numerical approximation without any power or factorial overflow!
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Taylor Series as Audio Equalizer Harmonics</span>
  </div>
  <p>
    Imagine synthesizing a smooth, pure acoustic flute tone ($\sin(x)$ sine wave) using an audio synthesizer.<br>
    The first term ($x$) is a harsh, linear buzzer. Adding the second harmonic ($-x^3/6$) bends the corners into a soft wave. Adding the third ($+x^5/120$) smooths the peaks. With just 6 to 8 iterations, the mathematical audio tone becomes indistinguishable from a natural sound wave!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Complete Solution: sin(x) Taylor Series, Vowel Frequency & Longest Word Finder</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;sstream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;cctype&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;cmath&gt;</span>

<span class="c-comment">// PROBLEM 1: Calculate sin(x) using Taylor Series Recurrence</span>
<span class="c-type">double</span> computeSinTaylor(<span class="c-type">double</span> xRadians, <span class="c-type">int</span> numTerms) {
    <span class="c-type">double</span> term = xRadians; <span class="c-comment">// First term: x^1 / 1!</span>
    <span class="c-type">double</span> sum = term;

    <span class="c-keyword">for</span> (<span class="c-type">int</span> i = <span class="c-number">1</span>; i &lt; numTerms; ++i) {
        <span class="c-comment">// Recurrence relation eliminates factorial overflow</span>
        term = -term * xRadians * xRadians / ((<span class="c-number">2</span> * i) * (<span class="c-number">2</span> * i + <span class="c-number">1</span>));
        sum += term;
    }
    <span class="c-keyword">return</span> sum;
}

<span class="c-comment">// PROBLEM 2: Count Frequency of Vowels (A, E, I, O, U)</span>
<span class="c-type">void</span> countVowels(<span class="c-keyword">const</span> <span class="c-type">std::string</span>&amp; text) {
    <span class="c-type">int</span> a = <span class="c-number">0</span>, e = <span class="c-number">0</span>, i = <span class="c-number">0</span>, o = <span class="c-number">0</span>, u = <span class="c-number">0</span>;
    <span class="c-keyword">for</span> (<span class="c-type">char</span> ch : text) {
        <span class="c-type">char</span> lower = std::tolower(ch);
        <span class="c-keyword">if</span> (lower == <span class="c-string">'a'</span>) a++;
        <span class="c-keyword">else</span> <span class="c-keyword">if</span> (lower == <span class="c-string">'e'</span>) e++;
        <span class="c-keyword">else</span> <span class="c-keyword">if</span> (lower == <span class="c-string">'i'</span>) i++;
        <span class="c-keyword">else</span> <span class="c-keyword">if</span> (lower == <span class="c-string">'o'</span>) o++;
        <span class="c-keyword">else</span> <span class="c-keyword">if</span> (lower == <span class="c-string">'u'</span>) u++;
    }
    std::cout &lt;&lt; <span class="c-string">"[Vowel Frequency] A: "</span> &lt;&lt; a &lt;&lt; <span class="c-string">" | E: "</span> &lt;&lt; e 
              &lt;&lt; <span class="c-string">" | I: "</span> &lt;&lt; i &lt;&lt; <span class="c-string">" | O: "</span> &lt;&lt; o &lt;&lt; <span class="c-string">" | U: "</span> &lt;&lt; u 
              &lt;&lt; <span class="c-string">" | Total: "</span> &lt;&lt; (a + e + i + o + u) &lt;&lt; <span class="c-string">"\\n"</span>;
}

<span class="c-comment">// PROBLEM 3: Find Longest Word in a Sentence</span>
<span class="c-type">std::string</span> findLongestWord(<span class="c-keyword">const</span> <span class="c-type">std::string</span>&amp; sentence) {
    <span class="c-type">std::stringstream</span> ss(sentence);
    <span class="c-type">std::string</span> word, longest = <span class="c-string">""</span>;

    <span class="c-keyword">while</span> (ss &gt;&gt; word) {
        <span class="c-keyword">if</span> (word.length() &gt; longest.length()) {
            longest = word;
        }
    }
    <span class="c-keyword">return</span> longest;
}

<span class="c-type">int</span> main() {
    <span class="c-comment">// Test 1: sin(30 degrees = PI / 6 radians approx 0.52359877)</span>
    <span class="c-type">double</span> pi = <span class="c-number">3.141592653589793</span>;
    <span class="c-type">double</span> angle30 = pi / <span class="c-number">6.0</span>;
    <span class="c-type">double</span> sinVal = computeSinTaylor(angle30, <span class="c-number">8</span>);
    std::cout &lt;&lt; <span class="c-string">"Taylor Series sin(30°): "</span> &lt;&lt; sinVal 
              &lt;&lt; <span class="c-string">" | cmath sin(): "</span> &lt;&lt; std::sin(angle30) &lt;&lt; <span class="c-string">"\\n\\n"</span>;

    <span class="c-comment">// Test 2 &amp; 3: String Processing</span>
    <span class="c-type">std::string</span> sampleText = <span class="c-string">"Object Oriented System Design develops robust high performance applications"</span>;
    std::cout &lt;&lt; <span class="c-string">"Input Sentence: \\\""</span> &lt;&lt; sampleText &lt;&lt; <span class="c-string">"\\\"\\n"</span>;
    countVowels(sampleText);

    <span class="c-type">std::string</span> longest = findLongestWord(sampleText);
    std::cout &lt;&lt; <span class="c-string">"[Longest Word]: \\\""</span> &lt;&lt; longest 
              &lt;&lt; <span class="c-string">"\\\" (Length: "</span> &lt;&lt; longest.length() &lt;&lt; <span class="c-string">" characters)\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Taylor Series Recurrence Pipeline &amp; String Tokenizer</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- Taylor series pipeline -->
      <g transform="translate(40, 35)">
        <rect width="320" height="150" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="160" y="25" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">sin(x) Recurrence Iteration</text>
        <rect x="20" y="45" width="280" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="65" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Term(0) = x</text>
        <rect x="20" y="85" width="280" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="160" y="105" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Term(i) = -Term(i-1) • x² / (2i(2i+1))</text>
        <text x="160" y="135" fill="var(--text-secondary)" font-size="10" text-anchor="middle">Zero Factorial Overflow • O(N) Complexity</text>
      </g>

      <!-- Arrow -->
      <path d="M 375 110 L 415 110" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

      <!-- String Tokenizer -->
      <g transform="translate(430, 35)">
        <rect width="290" height="150" rx="8" fill="var(--bg-elevated)" stroke="#c084fc" stroke-width="2"/>
        <text x="145" y="25" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">String Processing Pipeline</text>
        <rect x="20" y="45" width="250" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="145" y="65" fill="var(--text-primary)" font-size="11" text-anchor="middle">Stream Tokenization: ss &gt;&gt; word</text>
        <rect x="20" y="85" width="250" height="30" rx="4" fill="var(--bg-card)"/>
        <text x="145" y="105" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Vowel Counter: tolower() == 'a'..'u'</text>
        <text x="145" y="135" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Max Length Tracker: word.length() &gt; max</text>
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
    <li><span class="check-box"></span> Why should you avoid calculating $N!$ directly when implementing Taylor series? (Causes 64-bit integer overflow).</li>
    <li><span class="check-box"></span> Write the recurrence relation for finding the next term of $\\sin(x)$.</li>
    <li><span class="check-box"></span> Which stream class from <code>&lt;sstream&gt;</code> is ideal for tokenizing a sentence into words? (<code>std::stringstream</code>).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When writing the Taylor series code in an exam, always comment on the recurrence formula. Examiners specifically look for students who avoid direct factorial multiplication!
</div>
"""
    sections.append({
        "id": "u4-sec-11",
        "number": 11,
        "part": "PART 1 — C++ BASICS",
        "title": "11. Basic C++ Programming Problems & Algorithms",
        "subtitle": "Taylor Series Expansions for sin(x)/cos(x), Vowel Frequency Analytics & Longest Word Tokenization",
        "content": sec11_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit4_part2_sections()
    print(f"generate_unit4_part2.py compiled {len(secs)} sections successfully.")
