# generate_unit4_part1.py: Generates Sections 1 to 5 for Unit 4 (C++ Basics)

def get_unit4_part1_sections():
    sections = []

    # =========================================================================
    # SECTION 1: C++ Overview & Applications
    # =========================================================================
    sec1_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">1. Introduction to C++ & Industrial Applications</h3>
  </div>

  <div class="detail-block">
    <h5>1.1 What is C++? Origin &amp; Evolutionary Milestones</h5>
    <p>
      <strong>C++</strong> is a general-purpose, statically typed, compiled, multi-paradigm programming language created by Danish computer scientist <strong>Bjarne Stroustrup</strong> at <strong>Bell Laboratories (AT&amp;T)</strong> in Murray Hill, New Jersey, starting in 1979.
    </p>
    <ul>
      <li><strong>Original Name:</strong> Initially dubbed <em>"C with Classes"</em>, the language aimed to marry the raw execution speed and bare-metal control of Dennis Ritchie's <strong>C</strong> language with the data abstraction, object encapsulation, and modular organization pioneered by <strong>Simula67</strong>.</li>
      <li><strong>The Name Change:</strong> In 1983, computer scientist Rick Mascitti coined the moniker <strong>C++</strong>, referencing C's unary post-increment operator (<code>++</code>). It symbolized an evolutionary, upward extension of C while maintaining near-total backward compatibility.</li>
      <li><strong>Standardization:</strong> Formalized internationally by ISO/IEC in 1998 (C++98), followed by landmark modern revisions: C++11, C++14, C++17, C++20, and C++23.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>1.2 General Characteristics of C++</h5>
    <ul>
      <li><strong>Multi-Paradigm Paradigm:</strong> C++ does not force pure object orientation. It seamlessly unifies <em>Procedural Programming</em> (C-style functions and algorithms), <em>Object-Oriented Programming</em> (classes, inheritance, polymorphism, encapsulation), and <em>Generic Programming</em> (templates and STL).</li>
      <li><strong>Direct Hardware Manipulation:</strong> Direct access to physical memory addresses via raw pointers, bitwise arithmetic, and custom memory allocators with zero runtime garbage collection latency.</li>
      <li><strong>Zero-Overhead Principle:</strong> Coined by Bjarne Stroustrup: <em>"What you don't use, you don't pay for. And further: What you do use, you couldn't hand code any better."</em> Language abstractions (such as templates, inlining, and non-virtual member functions) incur zero runtime penalty.</li>
      <li><strong>Deterministic Resource Management (RAII):</strong> Resource Acquisition Is Initialization binds memory, file handles, and mutex locks to object lifetimes, automatically invoking destructors when stack frames exit.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>1.3 Primary Applications of C++ in Industry</h5>
    <p>
      The AKTU curriculum emphasizes why C++ remains irreplaceable in cutting-edge systems engineering:
    </p>
    <ul>
      <li><strong>Operating Systems &amp; Kernels:</strong> Major subsystems of Microsoft Windows, Apple macOS, Linux drivers, and Android core runtimes are authored in C and C++.</li>
      <li><strong>Compilers, Interpreters &amp; Virtual Machines:</strong> LLVM/Clang, GCC, and Google V8 JavaScript Engine (powering Chrome and Node.js) rely heavily on C++ for extreme compiler performance.</li>
      <li><strong>High-Performance Game Engines:</strong> Unreal Engine, Unity (core runtime), and EA Frostbite leverage C++ for real-time 60-120 FPS graphics rendering, physics simulation, and GPU compute pipelines.</li>
      <li><strong>Database Management Systems:</strong> High-throughput engines including Oracle Database, MySQL, Microsoft SQL Server, and MongoDB are built using C++ for low-latency disk I/O and concurrency.</li>
      <li><strong>GUI Editors &amp; Desktop Suites:</strong> Adobe Photoshop, Illustrator, Microsoft Office, Autodesk Maya, and CAD systems.</li>
      <li><strong>Financial &amp; Algorithmic Trading:</strong> Ultra-low latency trading platforms where microsecond and nanosecond execution speeds dictate millions of dollars.</li>
      <li><strong>Embedded, Aerospace &amp; Automotive:</strong> Flight control systems, NASA Mars Rovers, autonomous driving computers (NVIDIA DRIVE), and medical devices requiring strict deterministic timing.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Formula 1 Hybrid Supercar</span>
  </div>
  <p>
    Think of <strong>C</strong> as a classic, stripped-down mechanical race car: raw, extremely fast, but requiring manual management of every bolt and clutch. If you misjudge a turn, there are no airbags—you crash straight into the wall (segmentation fault).<br>
    <strong>Java or Python</strong> is like a modern self-driving electric commuter sedan: comfortable, highly automated, equipped with automatic speed governors and automatic trash cleanup (Garbage Collector), but heavily padded with overhead—unfit for a 200 MPH Formula 1 Grand Prix.<br>
    <strong>C++</strong> is an elite <strong>Formula 1 Hybrid Supercar</strong>: it offers the aerodynamically advanced composite cockpit and modular telemetry of modern design (OOP, Classes, Interfaces), yet leaves the high-octane turbo engine directly connected to your manual pedal. You command absolute speed, but with the professional steering wheel to orchestrate massive mechanical power cleanly.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Industrial Architecture: High-Performance Engine Telemetry Subsystem</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>

<span class="c-comment">// Demonstrating Multi-Paradigm C++: Classes, Encapsulation, and Raw Speed</span>
<span class="c-keyword">class</span> EngineTelemetry {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> engineModel;
    <span class="c-type">double</span> rpm;
    <span class="c-type">double</span> temperatureCelsius;

<span class="c-keyword">public</span>:
    <span class="c-comment">// Constructor initializing hardware state</span>
    EngineTelemetry(<span class="c-type">std::string</span> model, <span class="c-type">double</span> initialRpm, <span class="c-type">double</span> initialTemp)
        : engineModel(model), rpm(initialRpm), temperatureCelsius(initialTemp) {}

    <span class="c-comment">// Fast inline operation: Low-overhead real-time check</span>
    <span class="c-type">bool</span> isWithinSafetyThreshold() <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> (rpm &lt;= <span class="c-number">12500.0</span> &amp;&amp; temperatureCelsius &lt;= <span class="c-number">110.0</span>);
    }

    <span class="c-type">void</span> updateSensors(<span class="c-type">double</span> newRpm, <span class="c-type">double</span> newTemp) {
        rpm = newRpm;
        temperatureCelsius = newTemp;
    }

    <span class="c-type">void</span> renderStatus() <span class="c-keyword">const</span> {
        std::cout &lt;&lt; <span class="c-string">"[Telemetry] Model: "</span> &lt;&lt; engineModel 
                  &lt;&lt; <span class="c-string">" | RPM: "</span> &lt;&lt; rpm 
                  &lt;&lt; <span class="c-string">" | Temp: "</span> &lt;&lt; temperatureCelsius &lt;&lt; <span class="c-string">"°C"</span>
                  &lt;&lt; <span class="c-string">" | Status: "</span> 
                  &lt;&lt; (isWithinSafetyThreshold() ? <span class="c-string">"OPTIMAL"</span> : <span class="c-string">"WARNING: OVERHEAT!"</span>)
                  &lt;&lt; <span class="c-string">"\\n"</span>;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">// Stack allocation ensures instant performance without garbage collector pauses</span>
    EngineTelemetry v6Turbo(<span class="c-string">"Ferrari-F1-066/10"</span>, <span class="c-number">11200.0</span>, <span class="c-number">94.5</span>);
    v6Turbo.renderStatus();

    <span class="c-comment">// Simulate aggressive lap acceleration</span>
    v6Turbo.updateSensors(<span class="c-number">12800.0</span>, <span class="c-number">114.2</span>);
    v6Turbo.renderStatus();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: C++ Evolutionary Lineage &amp; Paradigm Matrix</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
        </marker>
      </defs>

      <!-- Parent 1: C Language -->
      <g transform="translate(60, 30)">
        <rect width="260" height="90" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="130" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">C Language (1972)</text>
        <text x="130" y="50" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Dennis Ritchie • Bell Labs</text>
        <text x="130" y="70" fill="var(--text-primary)" font-size="11" text-anchor="middle">Bare-metal speed • Raw memory • Pointers</text>
      </g>

      <!-- Parent 2: Simula67 -->
      <g transform="translate(440, 30)">
        <rect width="260" height="90" rx="8" fill="var(--bg-elevated)" stroke="#a855f7" stroke-width="2"/>
        <text x="130" y="28" fill="#c084fc" font-size="14" font-weight="bold" text-anchor="middle">Simula 67 (1967)</text>
        <text x="130" y="50" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Dahl &amp; Nygaard • Norwegian Center</text>
        <text x="130" y="70" fill="var(--text-primary)" font-size="11" text-anchor="middle">Classes • Inheritance • Encapsulation</text>
      </g>

      <!-- Arrows pointing to C++ -->
      <path d="M 190 120 L 330 180" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,4" marker-end="url(#arrow-blue)"/>
      <path d="M 570 120 L 430 180" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="4,4" marker-end="url(#arrow-blue)"/>

      <!-- Fusion Box: C++ -->
      <g transform="translate(190, 175)">
        <rect width="380" height="90" rx="10" fill="var(--bg-card)" stroke="#10b981" stroke-width="2.5"/>
        <text x="190" y="28" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">C++ : "C with Classes" (1979 → 1983)</text>
        <text x="190" y="48" fill="var(--text-secondary)" font-size="11.5" text-anchor="middle">Bjarne Stroustrup • ISO/IEC Standards</text>
        <text x="190" y="70" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Procedural + OOP (Polymorphism) + Generic Templates (STL)</text>
      </g>
    </svg>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Head-to-Head Comparison: C vs C++ Paradigm Architecture</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Architectural Criterion</th>
        <th>C Programming Language</th>
        <th>C++ Programming Language</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Dominant Paradigm</strong></td>
        <td>Strictly Procedural (Top-down functional decomposition)</td>
        <td>Multi-paradigm (Procedural, Object-Oriented, Generic, Functional)</td>
      </tr>
      <tr>
        <td><strong>Data Protection &amp; Hiding</strong></td>
        <td>None (All struct members and global variables are public)</td>
        <td>High (Encapsulation via <code>private</code>, <code>protected</code>, <code>public</code>)</td>
      </tr>
      <tr>
        <td><strong>Memory Management</strong></td>
        <td>Manual library routines (<code>malloc()</code>, <code>free()</code>)</td>
        <td>Type-safe operators (<code>new</code>, <code>delete</code>) + RAII smart pointers</td>
      </tr>
      <tr>
        <td><strong>Polymorphism Support</strong></td>
        <td>None (Requires complex manual function pointers)</td>
        <td>Built-in Compile-time (Overloading/Templates) &amp; Runtime (Virtual Tables)</td>
      </tr>
      <tr>
        <td><strong>Namespaces &amp; Scoping</strong></td>
        <td>Flat single global namespace (Prone to naming collisions)</td>
        <td>Hierarchical namespaces (e.g. <code>std::</code>, custom namespaces)</td>
      </tr>
      <tr>
        <td><strong>Function Flexibility</strong></td>
        <td>No function overloading, no default arguments</td>
        <td>Overloading, default arguments, inline expansion, templates</td>
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
    <li><span class="check-box"></span> Can you state who developed C++, in what year, and at which facility? (Bjarne Stroustrup, 1979, Bell Labs).</li>
    <li><span class="check-box"></span> What did the <code>++</code> in C++ signify? (Increment operator in C, indicating an evolutionary step forward).</li>
    <li><span class="check-box"></span> State the Zero-Overhead Principle in your own words.</li>
    <li><span class="check-box"></span> Name at least 4 critical real-world application domains where C++ is mandatory.</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"Explain features and applications of C++"</em> (frequently asked 10-mark question), draw the evolutionary chart showing C (speed) + Simula67 (classes) = C++, and list at least 5 industrial applications with concrete software names (e.g. Unreal Engine, Windows Kernel, V8 Engine).
</div>
"""
    sections.append({
        "id": "u4-sec-1",
        "number": 1,
        "part": "PART 1 — C++ BASICS",
        "title": "1. C++ Overview & Industrial Applications",
        "subtitle": "Origins by Bjarne Stroustrup, Multi-Paradigm Foundations, Zero-Overhead Principle & Systems Programming Dominance",
        "content": sec1_content
    })

    # =========================================================================
    # SECTION 2: Structure of a C++ Program
    # =========================================================================
    sec2_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">2. Structure of a C++ Program &amp; Interface Separation</h3>
  </div>

  <div class="detail-block">
    <h5>2.1 The Four Canonical Sections of a C++ Source File</h5>
    <p>
      The AKTU Quantum syllabus outlines four organized sequential tiers governing how an idiomatic C++ program is constructed:
    </p>
    <div class="workflow-steps">
      <div class="step-card">
        <span class="step-num">1</span>
        <div class="step-content">
          <h6>Include Directives &amp; Preprocessor Macros</h6>
          <p>Directs the preprocessor to inject declarations from external libraries before compilation begins (e.g., <code>#include &lt;iostream&gt;</code>, <code>#include &lt;vector&gt;</code>).</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">2</span>
        <div class="step-content">
          <h6>Class Declarations (The Interface Contract)</h6>
          <p>Declares class types, encapsulating internal private state (data members) and announcing public prototypes (member functions) without detailing algorithms.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">3</span>
        <div class="step-content">
          <h6>Member Function Definitions (The Implementation)</h6>
          <p>Provides the concrete executable statements for the declared methods, either defined inside the class or externally using the <strong>Scope Resolution Operator (<code>::</code>)</strong>.</p>
        </div>
      </div>
      <div class="step-card">
        <span class="step-num">4</span>
        <div class="step-content">
          <h6>The <code>main()</code> Execution Driver</h6>
          <p>The mandatory global operating system entry point. Execution commences in <code>int main()</code> and returns an integer status code (<code>0</code> = success).</p>
        </div>
      </div>
    </div>
  </div>

  <div class="detail-block">
    <h5>2.2 Header Files &amp; <code>#include</code> Directives</h5>
    <ul>
      <li><strong>Standard Angle Brackets (<code>&lt;...&gt;</code>):</strong> <code>#include &lt;iostream&gt;</code> commands the compiler to search designated standard system library directories. Modern standard C++ headers omit the archaic <code>.h</code> extension.</li>
      <li><strong>User-Defined Quotes (<code>"..."</code>):</strong> <code>#include "Student.h"</code> commands the compiler to look in the current working project directory first before falling back to system paths.</li>
      <li><strong>Header Guards:</strong> Preprocessor flags (<code>#ifndef MY_CLASS_H</code> ... <code>#define MY_CLASS_H</code> ... <code>#endif</code>) or <code>#pragma once</code> prevent destructive duplicate class redefinitions across translation units.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2.3 Separation of Interface and Implementation</h5>
    <p>
      A bedrock software engineering doctrine tested in AKTU examinations:
    </p>
    <ul>
      <li><strong>Interface (Header <code>.h</code> / <code>.hpp</code>):</strong> Discloses <em>WHAT</em> the object can do. It exposes public member function signatures and parameter types. Clients include this header to compile against the class contract.</li>
      <li><strong>Implementation (Source <code>.cpp</code>):</strong> Encapsulates <em>HOW</em> operations are realized. Houses algorithms, memory manipulations, and private helper logic. This can be pre-compiled into binary static (<code>.lib</code>, <code>.a</code>) or dynamic (<code>.dll</code>, <code>.so</code>) libraries without revealing source code.</li>
      <li><strong>Benefits:</strong> Drastically reduces compile times, shields proprietary algorithms, and allows internal algorithmic refactoring without breaking client code.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Restaurant Menu vs Kitchen Operations</span>
  </div>
  <p>
    Consider dining at an upscale restaurant:
    <br>&bull; <strong>The Menu (Header <code>.h</code>):</strong> Represents the public <strong>Interface</strong>. It lists what dishes you can order (e.g., <code>orderPizza(size, toppings)</code>) and what you receive in return. It contains zero cooking instructions or pantry secret recipes.
    <br>&bull; <strong>The Kitchen (Implementation <code>.cpp</code>):</strong> Represents the <strong>Implementation</strong> hidden behind closed doors. The chef uses ovens, knives, secret seasoning proportions, and precise cooking times (member function definitions).
    <br>&bull; <strong>The Diner (The <code>main()</code> function):</strong> Reads the menu, calls the order function, and enjoys the food. If the chef upgrades the oven from wood-fired to electric convection (implementation change), the diner's menu never changes!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Clean Architecture: Demonstrating the 4 Sequential Sections &amp; Scope Resolution (::)</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">// SECTION 1: INCLUDE DIRECTIVES</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// SECTION 2: CLASS DECLARATION (THE INTERFACE CONTRACT)</span>
<span class="c-keyword">class</span> BankAccount {
<span class="c-keyword">private</span>:
    <span class="c-type">std::string</span> accountNumber;
    <span class="c-type">double</span> balance;

<span class="c-keyword">public</span>:
    <span class="c-comment">// Constructor Prototype</span>
    BankAccount(<span class="c-type">std::string</span> accNum, <span class="c-type">double</span> initialBalance);

    <span class="c-comment">// Public Member Function Prototypes</span>
    <span class="c-type">void</span> deposit(<span class="c-type">double</span> amount);
    <span class="c-type">bool</span> withdraw(<span class="c-type">double</span> amount);
    <span class="c-type">void</span> printStatement() <span class="c-keyword">const</span>;
};

<span class="c-comment">// SECTION 3: MEMBER FUNCTION DEFINITIONS (THE IMPLEMENTATION)</span>
<span class="c-comment">// Notice the Scope Resolution Operator (::) binding function to class</span>
BankAccount::BankAccount(<span class="c-type">std::string</span> accNum, <span class="c-type">double</span> initialBalance) {
    accountNumber = accNum;
    balance = (initialBalance &gt;= <span class="c-number">0.0</span>) ? initialBalance : <span class="c-number">0.0</span>;
}

<span class="c-type">void</span> BankAccount::deposit(<span class="c-type">double</span> amount) {
    <span class="c-keyword">if</span> (amount &gt; <span class="c-number">0.0</span>) {
        balance += amount;
        std::cout &lt;&lt; <span class="c-string">"[Deposit]: Successfully credited $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">"\\n"</span>;
    }
}

<span class="c-type">bool</span> BankAccount::withdraw(<span class="c-type">double</span> amount) {
    <span class="c-keyword">if</span> (amount &gt; <span class="c-number">0.0</span> &amp;&amp; amount &lt;= balance) {
        balance -= amount;
        std::cout &lt;&lt; <span class="c-string">"[Withdrawal]: Successfully debited $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">"\\n"</span>;
        <span class="c-keyword">return</span> <span class="c-keyword">true</span>;
    }
    std::cout &lt;&lt; <span class="c-string">"[Error]: Insufficient funds for $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">"\\n"</span>;
    <span class="c-keyword">return</span> <span class="c-keyword">false</span>;
}

<span class="c-type">void</span> BankAccount::printStatement() <span class="c-keyword">const</span> {
    std::cout &lt;&lt; <span class="c-string">"Account: "</span> &lt;&lt; accountNumber 
              &lt;&lt; <span class="c-string">" | Current Balance: $"</span> &lt;&lt; balance &lt;&lt; <span class="c-string">"\\n"</span>;
}

<span class="c-comment">// SECTION 4: MAIN FUNCTION (EXECUTION ENTRY POINT)</span>
<span class="c-type">int</span> main() {
    std::cout &lt;&lt; <span class="c-string">"--- Initializing Bank Account Simulation ---\\n"</span>;
    BankAccount userAcc(<span class="c-string">"AKTU-OOSD-994"</span>, <span class="c-number">1500.0</span>);

    userAcc.printStatement();
    userAcc.deposit(<span class="c-number">500.0</span>);
    userAcc.withdraw(<span class="c-number">700.0</span>);
    userAcc.withdraw(<span class="c-number">2000.0</span>); <span class="c-comment">// Rejected by safety logic</span>
    userAcc.printStatement();

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: C++ 4-Stage Program Execution Pipeline</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-flow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>

      <!-- Stage 1 -->
      <g transform="translate(30, 80)">
        <rect width="140" height="90" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="70" y="25" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Stage 1: Includes</text>
        <text x="70" y="48" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">#include &lt;iostream&gt;</text>
        <text x="70" y="68" fill="var(--text-primary)" font-size="10" text-anchor="middle">Header Injection</text>
      </g>

      <path d="M 170 125 L 205 125" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-flow)"/>

      <!-- Stage 2 -->
      <g transform="translate(210, 80)">
        <rect width="150" height="90" rx="8" fill="var(--bg-elevated)" stroke="#c084fc" stroke-width="2"/>
        <text x="75" y="25" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">Stage 2: Interface</text>
        <text x="75" y="48" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">class BankAccount;</text>
        <text x="75" y="68" fill="var(--text-primary)" font-size="10" text-anchor="middle">Prototypes &amp; State</text>
      </g>

      <path d="M 360 125 L 395 125" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-flow)"/>

      <!-- Stage 3 -->
      <g transform="translate(400, 80)">
        <rect width="150" height="90" rx="8" fill="var(--bg-elevated)" stroke="#fbbf24" stroke-width="2"/>
        <text x="75" y="25" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Stage 3: Methods</text>
        <text x="75" y="48" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">BankAccount::func()</text>
        <text x="75" y="68" fill="var(--text-primary)" font-size="10" text-anchor="middle">Scope Resolution ::</text>
      </g>

      <path d="M 550 125 L 585 125" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-flow)"/>

      <!-- Stage 4 -->
      <g transform="translate(590, 80)">
        <rect width="140" height="90" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="2"/>
        <text x="70" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Stage 4: main()</text>
        <text x="70" y="48" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">int main() { ... }</text>
        <text x="70" y="68" fill="var(--text-primary)" font-size="10" text-anchor="middle">OS Entry Driver</text>
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
    <li><span class="check-box"></span> Can you draw the 4 sequential tiers of a C++ program from memory?</li>
    <li><span class="check-box"></span> What is the exact purpose of the scope resolution operator (<code>::</code>) when defining member functions?</li>
    <li><span class="check-box"></span> Why does separating interface (<code>.h</code>) from implementation (<code>.cpp</code>) improve large software projects?</li>
    <li><span class="check-box"></span> What does returning <code>0</code> from <code>main()</code> signal to the host operating system?</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked <em>"Describe the basic structure of a C++ program with an example"</em>, explicitly write out the code showing member functions defined <strong>outside</strong> the class using <code>ReturnType ClassName::FunctionName(...)</code>. This proves your mastery of scope resolution.
</div>
"""
    sections.append({
        "id": "u4-sec-2",
        "number": 2,
        "part": "PART 1 — C++ BASICS",
        "title": "2. Structure of a C++ Program & Interface Separation",
        "subtitle": "The 4 Canonical Program Sections, Header Inclusions, Scope Resolution Operator (::) & Header/Source Decoupling",
        "content": sec2_content
    })

    # =========================================================================
    # SECTION 3: Namespace
    # =========================================================================
    sec3_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">3. Namespaces &amp; Scope Management</h3>
  </div>

  <div class="detail-block">
    <h5>3.1 Meaning &amp; Problem Solved by Namespaces</h5>
    <p>
      In massive multi-library software development, different third-party vendors frequently pick identical names for classes, functions, or global variables (e.g., two libraries defining a class named <code>Array</code> or a function named <code>init()</code>). In C, this causes a catastrophic <strong>Linker Collision Error</strong> (duplicate symbol).
    </p>
    <p>
      A <strong>Namespace</strong> in C++ defines a named declarative scope. Any identifier defined inside a namespace is localized to that scope, preventing pollution of the global namespace.
    </p>
  </div>

  <div class="detail-block">
    <h5>3.2 The Standard <code>std</code> Namespace</h5>
    <p>
      All components belonging to the official C++ Standard Library (including <code>cout</code>, <code>cin</code>, <code>endl</code>, <code>vector</code>, <code>string</code>, <code>map</code>) reside inside the namespace named <code>std</code>.
    </p>
    <p>
      To access an identifier inside <code>std</code>, programmers use one of three techniques:
    </p>
    <ol>
      <li>
        <strong>Explicit Qualification (Best Practice):</strong> Prefix the symbol with <code>std::</code> (e.g. <code>std::cout &lt;&lt; "Hello";</code>). Highly recommended for headers and professional code because it leaves zero ambiguity.
      </li>
      <li>
        <strong>Using-Declaration:</strong> Injects a single symbol into the current scope (e.g. <code>using std::cout; using std::endl;</code>).
      </li>
      <li>
        <strong>Using-Directive (<code>using namespace std;</code>):</strong> Dumps the entire contents of <code>std</code> into the current lexical scope. While convenient for student lab exercises, it is considered poor practice in large production header files because it risks re-introducing naming collisions.
      </li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>3.3 Custom Namespaces &amp; Nested Scopes</h5>
    <p>
      Programmers can define their own namespaces using the <code>namespace</code> keyword:
    </p>
    <ul>
      <li><strong>Syntax:</strong> <code>namespace LibraryA { void print(); }</code></li>
      <li><strong>Resolution:</strong> <code>LibraryA::print();</code></li>
      <li><strong>Nesting:</strong> Namespaces can be nested: <code>namespace Graphics { namespace Rendering3D { class Camera; } }</code> accessed via <code>Graphics::Rendering3D::Camera</code>.</li>
      <li><strong>Anonymous (Unnamed) Namespaces:</strong> <code>namespace { int secret; }</code> restricts the identifier strictly to the current translation unit, acting as a modern, type-safe replacement for C's <code>static</code> global variables.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Country Calling Codes &amp; Company Extensions</span>
  </div>
  <p>
    Imagine dialing the phone number <strong>"9876543210"</strong> without specifying a country code. If someone in India and someone in the UK both have that exact domestic subscriber number, the global telecom network cannot know who to ring!<br>
    By introducing <strong>Country Codes</strong>:
    <br>&bull; <code>+91 :: 9876543210</code> connects to the Indian subscriber.
    <br>&bull; <code>+44 :: 9876543210</code> connects to the British subscriber.
    <br>In C++, <code>std::cout</code> says <em>"Use the cout located in the standard country code"</em>, while <code>MyEngine::cout</code> says <em>"Use the custom logging stream inside MyEngine"</em>.
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Disambiguating Colliding Symbols with Custom Namespaces</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">// Vendor A defines an encryption-focused Network module</span>
<span class="c-keyword">namespace</span> CyberSecurity {
    <span class="c-keyword">class</span> Connection {
    <span class="c-keyword">public</span>:
        <span class="c-type">void</span> establish() {
            std::cout &lt;&lt; <span class="c-string">"[CyberSecurity]: Establishing 256-bit TLS Encrypted Tunnel.\\n"</span>;
        }
    };
}

<span class="c-comment">// Vendor B defines a low-latency UDP Gaming module</span>
<span class="c-keyword">namespace</span> HighSpeedGaming {
    <span class="c-keyword">class</span> Connection {
    <span class="c-keyword">public</span>:
        <span class="c-type">void</span> establish() {
            std::cout &lt;&lt; <span class="c-string">"[HighSpeedGaming]: Opening Raw UDP Socket for 144Hz packet stream.\\n"</span>;
        }
    };
}

<span class="c-type">int</span> main() {
    <span class="c-comment">// Both classes are named 'Connection', but namespaces eliminate ambiguity</span>
    CyberSecurity::Connection secureLink;
    secureLink.establish();

    HighSpeedGaming::Connection gameLink;
    gameLink.establish();

    <span class="c-comment">// Using-declaration for targeted convenience</span>
    <span class="c-keyword">using</span> std::cout;
    cout &lt;&lt; <span class="c-string">"Both connections orchestrated concurrently with zero symbol collision!\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Namespace Partitioning &amp; Name Collision Elimination</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 240" width="100%" height="240" xmlns="http://www.w3.org/2000/svg">
      <!-- Global Scope -->
      <rect x="20" y="20" width="720" height="200" rx="10" fill="var(--bg-elevated)" stroke="var(--border-default)" stroke-width="1.5"/>
      <text x="40" y="45" fill="var(--text-secondary)" font-size="13" font-weight="bold">GLOBAL SCOPE</text>

      <!-- Namespace A -->
      <g transform="translate(60, 65)">
        <rect width="300" height="135" rx="8" fill="var(--bg-card)" stroke="#38bdf8" stroke-width="2"/>
        <text x="150" y="26" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">namespace CyberSecurity</text>
        <rect x="25" y="45" width="250" height="40" rx="4" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-dasharray="2,2"/>
        <text x="150" y="70" fill="var(--text-primary)" font-size="12" text-anchor="middle">class Connection { ... }</text>
        <text x="150" y="115" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Access: CyberSecurity::Connection</text>
      </g>

      <!-- Namespace B -->
      <g transform="translate(400, 65)">
        <rect width="300" height="135" rx="8" fill="var(--bg-card)" stroke="#a855f7" stroke-width="2"/>
        <text x="150" y="26" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">namespace HighSpeedGaming</text>
        <rect x="25" y="45" width="250" height="40" rx="4" fill="var(--bg-elevated)" stroke="#a855f7" stroke-dasharray="2,2"/>
        <text x="150" y="70" fill="var(--text-primary)" font-size="12" text-anchor="middle">class Connection { ... }</text>
        <text x="150" y="115" fill="#c084fc" font-size="11" font-weight="600" text-anchor="middle">Access: HighSpeedGaming::Connection</text>
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
    <li><span class="check-box"></span> Why is <code>using namespace std;</code> discouraged in production header (<code>.h</code>) files? (It forces all symbols into anyone who includes that header).</li>
    <li><span class="check-box"></span> What is the syntax to access a member inside a namespace? (<code>NamespaceName::MemberName</code>).</li>
    <li><span class="check-box"></span> What is an anonymous (unnamed) namespace used for? (Internal linkage within a single translation unit).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> In 2-mark questions, examiners frequently ask: <em>"What is the significance of namespace in C++?"</em> Write: <em>"Namespaces prevent name collisions by creating separate declarative scopes for identifiers. All standard library entities are grouped under namespace std."</em>
</div>
"""
    sections.append({
        "id": "u4-sec-3",
        "number": 3,
        "part": "PART 1 — C++ BASICS",
        "title": "3. Namespace & Scope Resolution",
        "subtitle": "Logical Scope Partitioning, Eliminating Symbol Collisions, std Namespace Management & Anonymous Namespaces",
        "content": sec3_content
    })

    # =========================================================================
    # SECTION 4: Identifiers
    # =========================================================================
    sec4_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">4. Identifiers &amp; Lexical Naming Rules</h3>
  </div>

  <div class="detail-block">
    <h5>4.1 What is an Identifier?</h5>
    <p>
      An <strong>Identifier</strong> is a user-defined symbolic name allocated to programmatic entities in memory or translation units. Programmers assign identifiers to:
    </p>
    <ul>
      <li>Variables and Constants</li>
      <li>Functions and Member Methods</li>
      <li>Classes, Structs, and Unions</li>
      <li>Enumeration types and Enumerator values</li>
      <li>Labels, Templates, and Namespaces</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>4.2 Strict Rules for Constructing C++ Identifiers</h5>
    <p>
      The C++ lexical grammar enforces strict rules during tokenization:
    </p>
    <ol>
      <li><strong>Permitted Characters:</strong> Only alphanumeric characters (uppercase <code>A-Z</code>, lowercase <code>a-z</code>), decimal digits (<code>0-9</code>), and the underscore character (<code>_</code>) are valid.</li>
      <li><strong>Initial Character Rule:</strong> An identifier <strong>must begin</strong> with a letter or an underscore. It <strong>CANNOT begin with a digit</strong> (e.g., <code>1student</code> triggers a compile-time syntax error).</li>
      <li><strong>Case Sensitivity:</strong> C++ is strictly case-sensitive. The identifiers <code>score</code>, <code>Score</code>, and <code>SCORE</code> refer to three distinct, unrelated memory locations.</li>
      <li><strong>No Special Symbols or Whitespace:</strong> Characters such as <code>@</code>, <code>$</code>, <code>#</code>, <code>-</code>, <code>%</code>, punctuation marks, or spaces are illegal within an identifier name.</li>
      <li><strong>Reserved Keywords Prohibition:</strong> An identifier cannot be identical to any reserved C++ keyword (e.g., <code>class</code>, <code>int</code>, <code>virtual</code>, <code>return</code>, <code>for</code>, <code>while</code>).</li>
      <li><strong>Length Limits:</strong> Under ANSI/ISO C++, there is no theoretical maximum length for an identifier, though standard compilers guarantee distinction across the first 1024 characters.</li>
      <li><strong>Reserved Standard Prefixes:</strong> Identifiers starting with an underscore followed by an uppercase letter (<code>_Temp</code>) or containing double underscores (<code>__init</code>) are reserved by the implementation/compiler and must be avoided.</li>
    </ol>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Government Passport Numbering &amp; Airport Luggage Tags</span>
  </div>
  <p>
    When you check luggage at an international airport, the barcode tag must follow precise aviation standards: it can contain alphanumeric tracking codes, but cannot contain spaces, emojis, or punctuation marks.<br>
    Similarly, your official national passport name cannot be an official reserved legal title like "PRESIDENT" or "POLICE" (prohibited keywords). If an airline ticket system encounters a boarding pass starting with an illegal character or punctuation, the scanner rejects it immediately at the boarding gate (compile-time token error).
  </p>
</div>

<div class="comparison-table-wrapper">
  <h4>AKTU Master Classification: Valid vs Invalid Identifiers</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Candidate Identifier</th>
        <th>Validity Status</th>
        <th>Compiler Diagnostics / Rule Justification</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>totalMarks</code></td>
        <td><span style="color:#10b981; font-weight:bold;">VALID</span></td>
        <td>CamelCase alphanumeric string starting with a letter.</td>
      </tr>
      <tr>
        <td><code>_student_age_2026</code></td>
        <td><span style="color:#10b981; font-weight:bold;">VALID</span></td>
        <td>Starts with an underscore, followed by letters, digits, and underscores.</td>
      </tr>
      <tr>
        <td><code>calculate_GPA</code></td>
        <td><span style="color:#10b981; font-weight:bold;">VALID</span></td>
        <td>Standard snake_case identifier used for functions.</td>
      </tr>
      <tr>
        <td><code>1student</code></td>
        <td><span style="color:#ef4444; font-weight:bold;">INVALID</span></td>
        <td><strong>Error:</strong> Starts with numeric digit <code>1</code>. Compiler expects a literal constant.</td>
      </tr>
      <tr>
        <td><code>total-marks</code></td>
        <td><span style="color:#ef4444; font-weight:bold;">INVALID</span></td>
        <td><strong>Error:</strong> Hyphen (<code>-</code>) is tokenized as subtraction arithmetic operator.</td>
      </tr>
      <tr>
        <td><code>student@aktu</code></td>
        <td><span style="color:#ef4444; font-weight:bold;">INVALID</span></td>
        <td><strong>Error:</strong> Special symbol <code>@</code> is illegal in C++ identifier grammar.</td>
      </tr>
      <tr>
        <td><code>class</code></td>
        <td><span style="color:#ef4444; font-weight:bold;">INVALID</span></td>
        <td><strong>Error:</strong> <code>class</code> is a reserved language keyword.</td>
      </tr>
      <tr>
        <td><code>roll number</code></td>
        <td><span style="color:#ef4444; font-weight:bold;">INVALID</span></td>
        <td><strong>Error:</strong> Embedded whitespace breaks the token into two separate identifiers.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Testing Case-Sensitivity &amp; Valid Identifier Construction</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-type">int</span> main() {
    <span class="c-comment">// Valid Identifiers: Demonstrating strict Case-Sensitivity</span>
    <span class="c-type">int</span> marks = <span class="c-number">85</span>;
    <span class="c-type">int</span> Marks = <span class="c-number">92</span>;
    <span class="c-type">int</span> MARKS = <span class="c-number">98</span>;

    <span class="c-comment">// Valid Identifiers with underscores and digits</span>
    <span class="c-type">double</span> _gpa_sem4 = <span class="c-number">9.45</span>;
    <span class="c-type">int</span> student_count_2026 = <span class="c-number">120</span>;

    std::cout &lt;&lt; <span class="c-string">"marks: "</span> &lt;&lt; marks &lt;&lt; <span class="c-string">" | Marks: "</span> &lt;&lt; Marks &lt;&lt; <span class="c-string">" | MARKS: "</span> &lt;&lt; MARKS &lt;&lt; <span class="c-string">"\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Case-sensitivity confirms all three occupy distinct memory cells!\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Semester GPA: "</span> &lt;&lt; _gpa_sem4 &lt;&lt; <span class="c-string">" | Total Cohort: "</span> &lt;&lt; student_count_2026 &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Lexical Grammar Rules for Identifier Tokenization</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <!-- First Char -->
      <g transform="translate(50, 40)">
        <rect width="180" height="140" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Character 1</text>
        <text x="90" y="60" fill="#10b981" font-size="11.5" font-weight="600" text-anchor="middle">✓ Letters (A-Z, a-z)</text>
        <text x="90" y="85" fill="#10b981" font-size="11.5" font-weight="600" text-anchor="middle">✓ Underscore ( _ )</text>
        <text x="90" y="115" fill="#ef4444" font-size="11.5" font-weight="bold" text-anchor="middle">✗ NO DIGITS (0-9)</text>
      </g>

      <path d="M 230 110 L 290 110" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-flow)"/>

      <!-- Subsequent Chars -->
      <g transform="translate(300, 40)">
        <rect width="200" height="140" rx="8" fill="var(--bg-elevated)" stroke="#c084fc" stroke-width="2"/>
        <text x="100" y="30" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">Characters 2 .. N</text>
        <text x="100" y="60" fill="#10b981" font-size="11.5" font-weight="600" text-anchor="middle">✓ Letters (A-Z, a-z)</text>
        <text x="100" y="85" fill="#10b981" font-size="11.5" font-weight="600" text-anchor="middle">✓ Underscore ( _ )</text>
        <text x="100" y="110" fill="#10b981" font-size="11.5" font-weight="600" text-anchor="middle">✓ Digits (0-9) Permitted</text>
      </g>

      <path d="M 500 110 L 560 110" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-flow)"/>

      <!-- Global Filter -->
      <g transform="translate(570, 40)">
        <rect width="150" height="140" rx="8" fill="var(--bg-elevated)" stroke="#fbbf24" stroke-width="2"/>
        <text x="75" y="30" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">Global Filter</text>
        <text x="75" y="65" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">✗ No Keywords</text>
        <text x="75" y="95" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">✗ No Hyphens / @</text>
        <text x="75" y="125" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">✗ No Spaces</text>
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
    <li><span class="check-box"></span> Why is <code>2nd_rank</code> an invalid identifier? (Starts with a numeric digit).</li>
    <li><span class="check-box"></span> Why is <code>total-sum</code> invalid? (Hyphen is parsed as subtraction operator).</li>
    <li><span class="check-box"></span> Name the only non-alphanumeric character permitted in a standard C++ identifier. (Underscore <code>_</code>).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Questions asking <em>"Identify valid and invalid identifiers with reasons"</em> are guaranteed 2 to 5-mark scorers. State the exact reason (e.g. "contains hyphen", "starts with digit", "is a keyword") for each candidate.
</div>
"""
    sections.append({
        "id": "u4-sec-4",
        "number": 4,
        "part": "PART 1 — C++ BASICS",
        "title": "4. Identifiers & Lexical Naming Rules",
        "subtitle": "Grammar Constraints, Case Sensitivity, Character Permutations, Valid vs Invalid Token Matrices",
        "content": sec4_content
    })

    # =========================================================================
    # SECTION 5: Variables & Memory Concept
    # =========================================================================
    sec5_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 4 Part 1</div>
    <h3 class="card-title">5. Variables &amp; Memory Allocation Concepts</h3>
  </div>

  <div class="detail-block">
    <h5>5.1 Meaning of a Variable</h5>
    <p>
      A <strong>Variable</strong> is a named, typed symbolic abstraction bound to a specific contiguous sequence of bytes in physical memory (RAM).
    </p>
    <p>
      Every variable in C++ is characterized by four fundamental attributes:
    </p>
    <ul>
      <li><strong>Name (Identifier):</strong> The symbolic label programmers use in source code (e.g., <code>studentAge</code>).</li>
      <li><strong>Type (Data Type):</strong> Dictates the quantity of bytes allocated, the binary encoding format (two's complement, IEEE 754 float), and the permissible operations.</li>
      <li><strong>Address (L-value attribute):</strong> The physical hexadecimal memory address where the first byte is located (queried via the address-of operator <code>&amp;</code>).</li>
      <li><strong>Value (R-value attribute):</strong> The actual bits currently stored inside those memory bytes, which can mutate over runtime execution.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>5.2 Variable Declaration vs Definition vs Initialization</h5>
    <ul>
      <li><strong>Declaration:</strong> Informs the compiler about the variable's name and type without necessarily reserving memory (e.g., <code>extern int globalCounter;</code>).</li>
      <li><strong>Definition:</strong> Commands the compiler to allocate physical storage bytes in memory (e.g., <code>int age;</code>).</li>
      <li><strong>Initialization:</strong> Assigns an initial value to the allocated storage at the exact moment of creation (e.g., <code>int age = 21;</code> or modern brace initialization <code>int age{21};</code>).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>5.3 Primary C++ Fundamental Types &amp; Typical Memory Sizes</h5>
    <ul>
      <li><code>int</code>: Signed integer (Typically 4 bytes, range: -2,147,483,648 to 2,147,483,647).</li>
      <li><code>float</code>: Single-precision floating point (4 bytes, IEEE 754, ~7 decimal digits of precision).</li>
      <li><code>double</code>: Double-precision floating point (8 bytes, IEEE 754, ~15 decimal digits of precision).</li>
      <li><code>char</code>: Single ASCII character (1 byte, range: -128 to 127 or 0 to 255).</li>
      <li><code>bool</code>: Boolean truth value (1 byte, evaluates strictly to <code>true</code> or <code>false</code>).</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Labeled Rental Storage Lockers</span>
  </div>
  <p>
    Think of system RAM as a giant hallway containing millions of numbered metal lockers:
    <br>&bull; <strong>The Locker Number (Address <code>0x7ffee4</code>):</strong> The physical hardware coordinate. The CPU navigates by locker numbers.
    <br>&bull; <strong>The Name Label on the Locker (Variable Name <code>"age"</code>):</strong> A human-friendly sticker you slap on the door so you don't have to memorize hexadecimal numbers.
    <br>&bull; <strong>The Locker Size (Data Type <code>int</code> = 4 lockers wide):</strong> A <code>char</code> rents 1 small locker slot; a <code>double</code> rents an extra-wide 8-slot locker.
    <br>&bull; <strong>The Contents inside (Value <code>21</code>):</strong> Whatever items you store inside. You can open the door tomorrow, take out 21, and put in 22—the locker address and label stay the same!
  </p>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++</span>
    <span class="code-desc">Investigating Variable Addresses, Sizes, and Mutations in Memory</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>

<span class="c-type">int</span> main() {
    <span class="c-comment">// Variable Declarations and Initializations</span>
    <span class="c-type">int</span> studentRoll = <span class="c-number">101</span>;
    <span class="c-type">double</span> examGpa = <span class="c-number">9.42</span>;
    <span class="c-type">char</span> gradeLetter = <span class="c-string">'A'</span>;
    <span class="c-type">bool</span> isEnrolled = <span class="c-keyword">true</span>;

    std::cout &lt;&lt; <span class="c-string">"=== Variable State &amp; Memory Layout ===\\n"</span>;
    std::cout &lt;&lt; <span class="c-string">"Roll: "</span> &lt;&lt; studentRoll 
              &lt;&lt; <span class="c-string">" | Size: "</span> &lt;&lt; <span class="c-keyword">sizeof</span>(studentRoll) &lt;&lt; <span class="c-string">" bytes"</span>
              &lt;&lt; <span class="c-string">" | Address (&amp;): "</span> &lt;&lt; &amp;studentRoll &lt;&lt; <span class="c-string">"\\n"</span>;

    std::cout &lt;&lt; <span class="c-string">"GPA:  "</span> &lt;&lt; examGpa 
              &lt;&lt; <span class="c-string">" | Size: "</span> &lt;&lt; <span class="c-keyword">sizeof</span>(examGpa) &lt;&lt; <span class="c-string">" bytes"</span>
              &lt;&lt; <span class="c-string">" | Address (&amp;): "</span> &lt;&lt; &amp;examGpa &lt;&lt; <span class="c-string">"\\n"</span>;

    std::cout &lt;&lt; <span class="c-string">"Grade: "</span> &lt;&lt; gradeLetter 
              &lt;&lt; <span class="c-string">" | Size: "</span> &lt;&lt; <span class="c-keyword">sizeof</span>(gradeLetter) &lt;&lt; <span class="c-string">" byte"</span>
              &lt;&lt; <span class="c-string">" | Address (&amp;): "</span> &lt;&lt; (<span class="c-type">void</span>*)&amp;gradeLetter &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-comment">// Demonstrating Mutation of Value at the Same Memory Address</span>
    studentRoll = <span class="c-number">102</span>; <span class="c-comment">// New value overwritten into existing memory location</span>
    std::cout &lt;&lt; <span class="c-string">"\\n[After Mutation] Updated Roll: "</span> &lt;&lt; studentRoll 
              &lt;&lt; <span class="c-string">" | Address Remains Same: "</span> &lt;&lt; &amp;studentRoll &lt;&lt; <span class="c-string">"\\n"</span>;

    <span class="c-keyword">return</span> <span class="c-number">0</span>;
}</code></pre>
</div>

<div class="diagram-box">
  <div class="diagram-header">
    <span class="diagram-title">Visual Architecture: Variable Abstraction Mapped to Physical RAM Cells</span>
  </div>
  <div class="svg-diagram">
    <svg viewBox="0 0 760 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <!-- High-Level Code Plane -->
      <g transform="translate(60, 40)">
        <rect width="260" height="170" rx="8" fill="var(--bg-elevated)" stroke="#38bdf8" stroke-width="2"/>
        <text x="130" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Programmer's Code Level</text>
        <rect x="20" y="50" width="220" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="30" y="72" fill="var(--text-primary)" font-family="monospace" font-size="12">int age = 21;</text>
        <rect x="20" y="95" width="220" height="35" rx="4" fill="var(--bg-card)"/>
        <text x="30" y="117" fill="var(--text-primary)" font-family="monospace" font-size="12">double gpa = 9.42;</text>
        <text x="130" y="155" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Symbolic Identifier • Abstract Type</text>
      </g>

      <!-- Binding Arrow -->
      <path d="M 320 125 L 420 125" stroke="#10b981" stroke-width="3" marker-end="url(#arrow-flow)"/>
      <text x="370" y="115" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Binding</text>

      <!-- Physical Memory Plane -->
      <g transform="translate(430, 30)">
        <rect width="270" height="190" rx="8" fill="var(--bg-elevated)" stroke="#10b981" stroke-width="2"/>
        <text x="135" y="25" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Physical RAM Stack Frame</text>
        
        <!-- Cell 1: age -->
        <rect x="20" y="45" width="230" height="55" rx="4" fill="var(--bg-card)" stroke="#38bdf8"/>
        <text x="30" y="65" fill="#38bdf8" font-size="11" font-weight="bold">Address: 0x7ffd98b0</text>
        <text x="30" y="85" fill="var(--text-primary)" font-family="monospace" font-size="12">Value: [ 00000000 ... 00010101 ] (21)</text>

        <!-- Cell 2: gpa -->
        <rect x="20" y="115" width="230" height="55" rx="4" fill="var(--bg-card)" stroke="#c084fc"/>
        <text x="30" y="135" fill="#c084fc" font-size="11" font-weight="bold">Address: 0x7ffd98b4</text>
        <text x="30" y="155" fill="var(--text-primary)" font-family="monospace" font-size="12">Value: [ IEEE-754 64-bit bits ] (9.42)</text>
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
    <li><span class="check-box"></span> What are the 4 fundamental properties of every variable in C++? (Name, Type, Address, Value).</li>
    <li><span class="check-box"></span> Distinguish between variable declaration and variable definition.</li>
    <li><span class="check-box"></span> Which C++ operator retrieves the physical hexadecimal memory address of a variable? (Address-of operator <code>&amp;</code>).</li>
    <li><span class="check-box"></span> How many bytes do typical <code>int</code>, <code>double</code>, and <code>char</code> occupy on 64-bit systems? (4, 8, 1).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> Quantum explicitly asks: <em>"Explain the memory concept of a variable."</em> Always write: <em>"A variable is a symbolic name associated with a memory location where its value is stored as binary bits. Its address remains fixed during its scope lifetime while its stored value can mutate."</em>
</div>
"""
    sections.append({
        "id": "u4-sec-5",
        "number": 5,
        "part": "PART 1 — C++ BASICS",
        "title": "5. Variables & Memory Allocation Concepts",
        "subtitle": "Symbolic Memory Association, L-Value vs R-Value, Fundamental Data Types & Physical RAM Cell Mapping",
        "content": sec5_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit4_part1_sections()
    print(f"generate_unit4_part1.py compiled {len(secs)} sections successfully.")
