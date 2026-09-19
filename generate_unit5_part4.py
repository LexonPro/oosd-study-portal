# -*- coding: utf-8 -*-
"""
generate_unit5_part4.py: Generates Sections 18 to 24 for Unit 5
Topics:
  18. Polymorphism (Concept, Compile-time vs Runtime Classification, Benefits)
  19. Pointers in C++ (Memory Addresses, Indirection, Dereferencing, Dynamic Allocation)
  20. Pointers and Objects (Arrow Operator ->, Base-Class Pointers to Derived Objects)
  21. this Pointer (Implicit Identity, Parameter Shadowing Resolution, Method Chaining)
  22. Virtual Functions (Dynamic Dispatch, Late Binding, vtable and vptr Mechanics)
  23. Pure Virtual Functions and Abstract Classes (Interface Contracts, Mandatory Overriding)
  24. Implementing Polymorphism: Complete Pipeline Architecture (Static vs Dynamic Synthesis)
"""

def get_unit5_part4_sections():
    sections = []

    # =========================================================================
    # SECTION 18: Polymorphism
    # =========================================================================
    sec18_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4</div>
    <h3 class="card-title">18. Polymorphism: Single Interface, Multiple Manifestations</h3>
  </div>

  <div class="detail-block">
    <h5>18.1 Etymology and Core Philosophy</h5>
    <p>
      <strong>Polymorphism</strong> is derived from the ancient Greek words <em>Poly</em> (meaning "many") and <em>Morph</em> (meaning "forms"). In Object-Oriented Programming, polymorphism represents the ability of a single common interface, message, or function call to adapt its behavior and produce different outcomes depending on the specific type of object executing it at runtime or compile-time.
    </p>
    <p>
      The golden tenet of polymorphism is: <strong>"One Interface, Multiple Implementations"</strong>. A consumer module simply instructs an entity to perform an action (e.g. <code>draw()</code> or <code>calculateTax()</code>), and the underlying object autonomously determines how to fulfill that request based on its concrete type.
    </p>
  </div>

  <div class="detail-block">
    <h5>18.2 The Two Grand Taxonomies of Polymorphism</h5>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Dimension</th>
            <th>Compile-Time (Static Binding / Early Binding)</th>
            <th>Run-Time (Dynamic Binding / Late Binding)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Binding Moment</strong></td>
            <td>Function addresses resolved during program compilation.</td>
            <td>Function addresses resolved at execution time via memory lookup tables.</td>
          </tr>
          <tr>
            <td><strong>Primary Mechanisms</strong></td>
            <td>Function Overloading, Operator Overloading, Templates.</td>
            <td>Virtual Functions, Pure Virtual Functions (Abstract Classes).</td>
          </tr>
          <tr>
            <td><strong>Execution Speed</strong></td>
            <td>Ultra-fast. Direct function CALL machine instruction with zero runtime lookup cost.</td>
            <td>Slight overhead due to indirect function pointer table (vtable) resolution.</td>
          </tr>
          <tr>
            <td><strong>Flexibility</strong></td>
            <td>Static and rigid. Types must be fully known during compilation.</td>
            <td>Highly flexible, dynamic, and extensible. New derived classes plug in seamlessly.</td>
          </tr>
          <tr>
            <td><strong>Memory Overhead</strong></td>
            <td>Zero additional memory overhead per object instance.</td>
            <td>Each object with virtual functions carries a <code>vptr</code> (8 bytes on 64-bit systems).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Universal "Play" Button</span>
  </div>
  <p>
    Consider a modern multimedia entertainment center featuring a universal remote with a single physical <strong>[PLAY]</strong> button:
  </p>
  <ul>
    <li>When you select an <strong>Audio MP3 file</strong> and press <code>Play</code>, the sound card initializes digital audio decoders and activates the stereo speakers.</li>
    <li>When you select a <strong>4K Ultra-HD Movie</strong> and press <code>Play</code>, the graphics pipeline spins up video decoders, scales pixels to 3840x2160, and coordinates Dolby Atmos audio.</li>
    <li>When you select an <strong>Interactive Video Game</strong> and press <code>Play</code>, the 3D rendering engine boots the GPU physics pipeline and loads game textures.</li>
  </ul>
  <p>
    You press the exact same button (<code>play()</code>) on the universal interface, but the action manifests in completely diverse forms depending on the underlying media object. That is polymorphism in action!
  </p>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 18.1: Comprehensive Taxonomy of C++ Polymorphism</div>
  <svg viewBox="0 0 900 380" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="900" height="380" fill="#0b1120" rx="12"/>
    
    <!-- Root Node -->
    <rect x="330" y="25" width="240" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="450" y="48" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">POLYMORPHISM</text>
    <text x="450" y="68" fill="#94a3b8" font-size="12" text-anchor="middle">"One Interface &bull; Many Forms"</text>
    
    <!-- Branch Lines -->
    <path d="M 400 80 L 220 140" stroke="#64748b" stroke-width="2" fill="none"/>
    <path d="M 500 80 L 680 140" stroke="#64748b" stroke-width="2" fill="none"/>
    
    <!-- Left Branch: Compile-Time -->
    <rect x="90" y="140" width="260" height="60" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
    <text x="220" y="165" fill="#818cf8" font-size="14" font-weight="bold" text-anchor="middle">Compile-Time Polymorphism</text>
    <text x="220" y="185" fill="#94a3b8" font-size="11" text-anchor="middle">Static / Early Binding &bull; Resolved at Compile</text>
    
    <!-- Left Sub-leaves -->
    <line x1="160" y1="200" x2="160" y2="245" stroke="#475569" stroke-width="1.5"/>
    <rect x="60" y="245" width="200" height="42" rx="6" fill="#0f172a" stroke="#818cf8" stroke-dasharray="3,3"/>
    <text x="160" y="271" fill="#e2e8f0" font-size="12" text-anchor="middle">Function Overloading</text>

    <line x1="280" y1="200" x2="280" y2="245" stroke="#475569" stroke-width="1.5"/>
    <rect x="180" y="245" width="200" height="42" rx="6" fill="#0f172a" stroke="#818cf8" stroke-dasharray="3,3"/>
    <text x="280" y="271" fill="#e2e8f0" font-size="12" text-anchor="middle">Operator Overloading</text>

    <rect x="110" y="305" width="220" height="42" rx="6" fill="#0f172a" stroke="#818cf8" stroke-dasharray="3,3"/>
    <text x="220" y="331" fill="#c7d2fe" font-size="11" text-anchor="middle">Templates (Generic Programming)</text>

    <!-- Right Branch: Run-Time -->
    <rect x="550" y="140" width="260" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="680" y="165" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">Run-Time Polymorphism</text>
    <text x="680" y="185" fill="#94a3b8" font-size="11" text-anchor="middle">Dynamic / Late Binding &bull; Resolved at Runtime</text>
    
    <!-- Right Sub-leaves -->
    <line x1="620" y1="200" x2="620" y2="245" stroke="#475569" stroke-width="1.5"/>
    <rect x="520" y="245" width="200" height="42" rx="6" fill="#0f172a" stroke="#34d399" stroke-dasharray="3,3"/>
    <text x="620" y="271" fill="#e2e8f0" font-size="12" text-anchor="middle">Virtual Functions</text>

    <line x1="740" y1="200" x2="740" y2="245" stroke="#475569" stroke-width="1.5"/>
    <rect x="640" y="245" width="200" height="42" rx="6" fill="#0f172a" stroke="#34d399" stroke-dasharray="3,3"/>
    <text x="740" y="271" fill="#e2e8f0" font-size="12" text-anchor="middle">Pure Virtual Functions</text>

    <rect x="570" y="305" width="220" height="42" rx="6" fill="#0f172a" stroke="#34d399" stroke-dasharray="3,3"/>
    <text x="680" y="331" fill="#a7f3d0" font-size="11" text-anchor="middle">Abstract Base Classes / Interfaces</text>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>Compile-Time Polymorphism via Function Overloading</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

// Class demonstrating Compile-Time (Static) Polymorphism
class VolumeCalculator {
public:
    // Form 1: Volume of a Cube (1 parameter)
    double volume(double side) {
        cout &lt;&lt; "[Compile-Time Dispatch] Cube volume executed." &lt;&lt; endl;
        return side * side * side;
    }

    // Form 2: Volume of a Cylinder (2 parameters)
    double volume(double radius, double height) {
        cout &lt;&lt; "[Compile-Time Dispatch] Cylinder volume executed." &lt;&lt; endl;
        return 3.14159 * radius * radius * height;
    }

    // Form 3: Volume of a Rectangular Box (3 parameters)
    double volume(double length, double width, double height) {
        cout &lt;&lt; "[Compile-Time Dispatch] Box volume executed." &lt;&lt; endl;
        return length * width * height;
    }
};

int main() {
    VolumeCalculator calc;

    // The compiler checks argument count and types AT COMPILE TIME
    // and binds each call directly to its specific function address!
    cout &lt;&lt; "Cube Vol: " &lt;&lt; calc.volume(5.0) &lt;&lt; endl;
    cout &lt;&lt; "Cylinder Vol: " &lt;&lt; calc.volume(3.0, 7.0) &lt;&lt; endl;
    cout &lt;&lt; "Box Vol: " &lt;&lt; calc.volume(2.0, 4.0, 6.0) &lt;&lt; endl;

    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>[Compile-Time Dispatch] Cube volume executed.
Cube Vol: 125
[Compile-Time Dispatch] Cylinder volume executed.
Cylinder Vol: 197.92
[Compile-Time Dispatch] Box volume executed.
Box Vol: 48</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> What is the literal meaning of Polymorphism? (Many forms: one interface, multiple behaviors).</li>
    <li><span class="check-box"></span> What are the two types of polymorphism in C++? (Compile-time / Early binding vs Run-time / Late binding).</li>
    <li><span class="check-box"></span> Which polymorphism type has zero runtime execution overhead? (Compile-time polymorphism).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"What is polymorphism? Differentiate between compile-time and run-time polymorphism with suitable C++ examples."</em> is a regular 10-mark question. Draw Figure 18.1 taxonomy tree, present the comparison table, and provide function overloading and virtual function code snippets.
</div>
"""
    sections.append({
        "id": "u5-sec-18",
        "number": 18,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "18. Polymorphism: Concept & Classification",
        "subtitle": "Single Interface Multiple Forms, Static Early Binding vs Dynamic Late Binding Taxonomy",
        "content": sec18_content
    })

    # =========================================================================
    # SECTION 19: Pointers in C++
    # =========================================================================
    sec19_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4</div>
    <h3 class="card-title">19. Pointers in C++: Memory Addresses, Indirection &amp; Allocation</h3>
  </div>

  <div class="detail-block">
    <h5>19.1 What is a Pointer?</h5>
    <p>
      A <strong>pointer</strong> in C++ is a specialized variable that stores the physical or virtual <em>memory address</em> of another variable rather than storing a direct data value. Pointers provide the underlying infrastructure for dynamic memory management, efficient array handling, complex data structures (trees, graphs, linked lists), and dynamic polymorphic dispatch.
    </p>
    <ul>
      <li><strong>Address-of Operator (<code>&amp;</code>):</strong> A unary operator that extracts the hexadecimal memory address of an existing variable.</li>
      <li><strong>Dereference / Indirection Operator (<code>*</code>):</strong> A unary operator that accesses, reads, or modifies the actual value residing at the address stored inside the pointer.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>19.2 Syntax and Memory Layout</h5>
    <div class="code-box">
      <code>int count = 42;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Regular variable storing value 42<br>
int* ptr = &amp;count;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Pointer variable storing the memory address of count<br>
cout &lt;&lt; *ptr;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Dereferencing: outputs 42<br>
*ptr = 99;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Modifies count indirectly to 99!</code>
    </div>
  </div>

  <div class="detail-block">
    <h5>19.3 Dynamic Memory Management (<code>new</code> and <code>delete</code>)</h5>
    <p>
      C++ provides dynamic memory allocation from the system <strong>Heap</strong> at runtime:
    </p>
    <ul>
      <li><code>new</code>: Allocates memory on the heap and returns the address of the newly allocated storage.</li>
      <li><code>delete</code>: Releases single-object memory back to the heap to prevent memory leaks.</li>
      <li><code>delete[]</code>: Releases dynamically allocated array memory back to the operating system.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: Street Address vs The Physical House</span>
  </div>
  <p>
    Imagine writing <em>"221B Baker Street, London"</em> on a slip of paper:
  </p>
  <ul>
    <li>The slip of paper is the <strong>pointer variable</strong>. It doesn't contain bricks, furniture, or rooms; it merely holds the coordinates (address) of where the house exists.</li>
    <li>The physical building at that coordinate is the <strong>actual data variable</strong>.</li>
    <li>Traveling to 221B Baker Street, opening the front door, and sitting on the sofa is <strong>dereferencing (<code>*ptr</code>)</strong>.</li>
    <li>If someone paints the door green at that address, anyone visiting via that address sees a green door (indirect mutation).</li>
  </ul>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 19.1: Physical Memory Address Layout &amp; Dereferencing Mechanics</div>
  <svg viewBox="0 0 850 300" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="850" height="300" fill="#0b1120" rx="12"/>

    <!-- Pointer Variable Box -->
    <rect x="80" y="80" width="220" height="130" rx="8" fill="#1e293b" stroke="#818cf8" stroke-width="2"/>
    <text x="190" y="110" fill="#818cf8" font-size="14" font-weight="bold" text-anchor="middle">Pointer: int* ptr</text>
    <rect x="105" y="125" width="170" height="40" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="190" y="150" fill="#38bdf8" font-size="14" font-family="monospace" font-weight="bold" text-anchor="middle">0x7ffee4b2a890</text>
    <text x="190" y="195" fill="#94a3b8" font-size="11" text-anchor="middle">Own Address: 0x7ffee4b2a900</text>

    <!-- Arrow from pointer to target -->
    <path d="M 280 145 C 360 145, 420 145, 490 145" stroke="#38bdf8" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    
    <!-- Target Variable Box -->
    <rect x="510" y="80" width="240" height="130" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="630" y="110" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">Target Variable: int count</text>
    <rect x="545" y="125" width="170" height="40" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="630" y="152" fill="#34d399" font-size="20" font-family="monospace" font-weight="bold" text-anchor="middle">42</text>
    <text x="630" y="195" fill="#94a3b8" font-size="11" text-anchor="middle">Memory Address: 0x7ffee4b2a890</text>

    <!-- Marker definition -->
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
      </marker>
    </defs>

    <!-- Bottom Explanatory Caption -->
    <text x="425" y="260" fill="#94a3b8" font-size="13" text-anchor="middle">
      Dereferencing (*ptr) follows the stored address 0x7ffee4b2a890 to read or modify the integer value 42.
    </text>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>Pointers and Dynamic Memory Allocation</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

int main() {
    // 1. Stack pointer referencing stack variable
    int originalVal = 100;
    int* ptr = &amp;originalVal;

    cout &lt;&lt; "Value of originalVal: " &lt;&lt; originalVal &lt;&lt; endl;
    cout &lt;&lt; "Address of originalVal (&amp;originalVal): " &lt;&lt; &amp;originalVal &lt;&lt; endl;
    cout &lt;&lt; "Address held by ptr (ptr): " &lt;&lt; ptr &lt;&lt; endl;
    cout &lt;&lt; "Dereferenced value (*ptr): " &lt;&lt; *ptr &lt;&lt; endl;

    // Mutating through pointer indirection
    *ptr = 250;
    cout &lt;&lt; "After *ptr = 250, originalVal is: " &lt;&lt; originalVal &lt;&lt; endl;

    cout &lt;&lt; "\n--- Dynamic Heap Allocation ---" &lt;&lt; endl;
    // 2. Dynamic Memory allocation on the Heap
    int* heapPtr = new int(500); // Allocates single integer initialized to 500
    cout &lt;&lt; "Heap integer value: " &lt;&lt; *heapPtr &lt;&lt; endl;

    // Deallocate memory to prevent resource leaks
    delete heapPtr;
    heapPtr = nullptr; // Clear dangling pointer

    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>Value of originalVal: 100
Address of originalVal (&amp;originalVal): 0x7ffee4b2a890
Address held by ptr (ptr): 0x7ffee4b2a890
Dereferenced value (*ptr): 100
After *ptr = 250, originalVal is: 250

--- Dynamic Heap Allocation ---
Heap integer value: 500</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> What does the address-of operator <code>&amp;</code> return? (The memory address of a variable).</li>
    <li><span class="check-box"></span> What does the dereference operator <code>*</code> do? (Accesses the value stored at the memory address pointed to).</li>
    <li><span class="check-box"></span> What is a memory leak? (Failing to deallocate heap memory using <code>delete</code>).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> When asked about <em>"Pointers in C++ and their applications"</em>, mention: 1) Dynamic memory management (new/delete), 2) Efficient data passing by address, 3) Base class pointers to derived objects for runtime polymorphism.
</div>
"""
    sections.append({
        "id": "u5-sec-19",
        "number": 19,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "19. Pointers in C++",
        "subtitle": "Memory Addresses (&), Indirection (*), Dynamic Allocation (new/delete) & Memory Safety",
        "content": sec19_content
    })

    # =========================================================================
    # SECTION 20: Pointers and Objects
    # =========================================================================
    sec20_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4</div>
    <h3 class="card-title">20. Pointers and Objects: Arrow Operator &amp; Base Pointers</h3>
  </div>

  <div class="detail-block">
    <h5>20.1 Pointers to Class Objects</h5>
    <p>
      Just as we can declare pointers to primitive types (<code>int*</code>, <code>double*</code>), we can declare pointers to user-defined class objects. An <strong>object pointer</strong> stores the starting memory address of an object instance in RAM.
    </p>
    <ul>
      <li><strong>Dot Operator via Dereferencing:</strong> <code>(*ptr).memberFunction()</code>. Parentheses are strictly mandatory because the dot operator (<code>.</code>) has higher precedence than the dereference operator (<code>*</code>).</li>
      <li><strong>Arrow Member Access Operator (<code>-&gt;</code>):</strong> Modern C++ syntactic sugar that automatically dereferences the pointer and accesses the member: <code>ptr-&gt;memberFunction()</code>.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>20.2 Base Class Pointer Pointing to Derived Class Object</h5>
    <p>
      One of the most foundational principles of C++ Object-Oriented Architecture states:
      <br>
      <mark><strong>A pointer of Base Class type can legally and safely store the memory address of any Derived Class object!</strong></mark>
    </p>
    <p>
      This capability stems from the fundamental <strong>"Is-A"</strong> relationship. Because every Derived object contains a complete Base class sub-object within its memory layout, a Base pointer can point to that starting boundary without violation of type safety.
    </p>
  </div>

  <div class="detail-block">
    <h5>20.3 The Static Binding Conundrum (Without Virtual)</h5>
    <p>
      By default, C++ employs <strong>Early / Static Binding</strong> based on the <em>type of the pointer</em>, not the actual object it points to:
    </p>
    <ul>
      <li>If <code>Base* bPtr = new Derived();</code> is executed, the compiler inspects <code>bPtr</code>, sees that its declared type is <code>Base*</code>, and will <strong>only permit access to members defined in the Base class</strong>.</li>
      <li>If both Base and Derived have a function named <code>show()</code> (non-virtual), executing <code>bPtr-&gt;show()</code> will execute <strong>Base::show()</strong>, completely ignoring the specialized Derived version!</li>
      <li>This limitation directly necessitates <strong>Virtual Functions</strong> (explored in Section 22).</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Universal Remote Control</span>
  </div>
  <p>
    Think of a <strong>Base Class Pointer</strong> as a standard <em>Universal Television Remote</em>, and the <strong>Derived Object</strong> as an ultra-modern <em>8K Smart OLED TV</em>:
  </p>
  <ul>
    <li>The universal remote has basic buttons: <code>Power()</code>, <code>VolumeUp()</code>, <code>Mute()</code> (Base class members).</li>
    <li>The 8K Smart TV has those basic capabilities, plus advanced features: <code>streamNetflix4K()</code> and <code>activateVoiceAssistant()</code> (Derived-only members).</li>
    <li>You can point your universal remote at the Smart TV, and the basic buttons will work perfectly!</li>
    <li>However, the universal remote has no buttons for <code>streamNetflix4K()</code>. From the perspective of the remote, those derived-only features are invisible!</li>
  </ul>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 20.1: Base Pointer Pointing to Derived Object in Memory</div>
  <svg viewBox="0 0 850 330" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="850" height="330" fill="#0b1120" rx="12"/>

    <!-- Base Pointer Box -->
    <rect x="50" y="90" width="220" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="160" y="125" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Base* bPtr</text>
    <rect x="75" y="145" width="170" height="38" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="160" y="169" fill="#38bdf8" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">0x8000 (Address of d)</text>

    <!-- Memory layout of Derived Object -->
    <rect x="420" y="45" width="370" height="230" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="605" y="75" fill="#c084fc" font-size="15" font-weight="bold" text-anchor="middle">Derived Object: d (starts at 0x8000)</text>

    <!-- Base Sub-object slice -->
    <rect x="440" y="90" width="330" height="80" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="605" y="120" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Base Sub-Object Segment [Visible to bPtr]</text>
    <text x="605" y="145" fill="#94a3b8" font-size="12" text-anchor="middle">int base_data | void displayBase()</text>

    <!-- Derived Specific slice -->
    <rect x="440" y="180" width="330" height="80" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="605" y="210" fill="#f43f5e" font-size="13" font-weight="bold" text-anchor="middle">Derived-Specific Segment [Invisible to bPtr]</text>
    <text x="605" y="235" fill="#94a3b8" font-size="12" text-anchor="middle">int derived_data | void specialDerived()</text>

    <!-- Connecting Arrow -->
    <path d="M 270 164 C 340 164, 380 130, 435 130" stroke="#38bdf8" stroke-width="2.5" fill="none" marker-end="url(#arrow-blue)"/>

    <defs>
      <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
      </marker>
    </defs>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>Base Pointer to Derived Object (Static Early Binding Demo)</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
using namespace std;

class Base {
public:
    int baseVal;
    Base() : baseVal(100) {}

    void display() {
        cout &lt;&lt; "[Base::display] baseVal = " &lt;&lt; baseVal &lt;&lt; endl;
    }
};

class Derived : public Base {
public:
    int derivedVal;
    Derived() : derivedVal(999) {}

    // Overridden function (non-virtual)
    void display() {
        cout &lt;&lt; "[Derived::display] baseVal = " &lt;&lt; baseVal 
             &lt;&lt; ", derivedVal = " &lt;&lt; derivedVal &lt;&lt; endl;
    }

    void specialFeature() {
        cout &lt;&lt; "[Derived::specialFeature] Exclusive derived feature!" &lt;&lt; endl;
    }
};

int main() {
    Derived dObj;

    // 1. Pointer of Base type pointing to Derived object
    Base* bPtr = &amp;dObj;

    // Invoking display() through Base pointer:
    // Without 'virtual', C++ binds to Base::display at COMPILE TIME!
    cout &lt;&lt; "Calling display() via Base* pointer:" &lt;&lt; endl;
    bPtr-&gt;display(); 

    // bPtr-&gt;specialFeature(); 
    // ERROR! Base class has no member named 'specialFeature'.

    // 2. Accessing through Derived pointer directly
    cout &lt;&lt; "\nCalling display() via Derived* pointer:" &lt;&lt; endl;
    Derived* dPtr = &amp;dObj;
    dPtr-&gt;display();
    dPtr-&gt;specialFeature(); // Valid!

    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>Calling display() via Base* pointer:
[Base::display] baseVal = 100

Calling display() via Derived* pointer:
[Derived::display] baseVal = 100, derivedVal = 999
[Derived::specialFeature] Exclusive derived feature!</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> Why is <code>(*ptr).func()</code> equivalent to <code>ptr-&gt;func()</code>? (The arrow operator dereferences and accesses in one step).</li>
    <li><span class="check-box"></span> Can a Base class pointer point to a Derived class object? (Yes, legally and safely).</li>
    <li><span class="check-box"></span> Without <code>virtual</code>, which function is executed via a Base pointer pointing to a Derived object? (The Base class version, due to static early binding).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"What happens when a base class pointer points to a derived class object? Can it access derived-specific members?"</em> Answer: It can ONLY access members declared in the base class. It cannot access derived-specific members without a cast.
</div>
"""
    sections.append({
        "id": "u5-sec-20",
        "number": 20,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "20. Pointers and Objects",
        "subtitle": "Arrow Operator (->), Dynamic Object Lifecycles & Base Class Pointer Mechanics",
        "content": sec20_content
    })

    # =========================================================================
    # SECTION 21: this Pointer
    # =========================================================================
    sec21_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4</div>
    <h3 class="card-title">21. The this Pointer: Current Object Identity &amp; Chaining</h3>
  </div>

  <div class="detail-block">
    <h5>21.1 Meaning and Mechanics of the <code>this</code> Pointer</h5>
    <p>
      In C++, <strong><code>this</code></strong> is an implicit, hidden pointer passed automatically as the first hidden parameter to every non-static member function. It holds the hexadecimal memory address of the specific object instance for which the member function was invoked.
    </p>
    <ul>
      <li><strong>Type Signature:</strong> Inside class <code>ClassName</code>, the type of <code>this</code> is <code>ClassName* const this</code> (a constant pointer pointing to the invoking object). It cannot be reassigned (e.g. <code>this = &amp;otherObj;</code> is a compiler error).</li>
      <li><strong>Unavailable in Static Functions:</strong> Static member functions do not belong to any individual object instance; hence, <code>this</code> does not exist inside static member functions.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>21.2 The Three Indispensable Uses of <code>this</code></h5>
    <ol>
      <li>
        <strong>Resolving Parameter Name Shadowing:</strong> When constructor or member function arguments have identical names to the class data members, <code>this-&gt;member</code> cleanly disambiguates the member variable from the local parameter:
        <br><code>this-&gt;age = age;</code>
      </li>
      <li>
        <strong>Method Chaining (Cascade Calling):</strong> By returning <code>*this</code> (a reference to the current invoking object) from member functions, multiple calls can be chained together on a single line:
        <br><code>account.deposit(500).applyInterest(0.05).printBalance();</code>
      </li>
      <li>
        <strong>Passing Self Reference:</strong> An object can pass <code>*this</code> or <code>this</code> to an external logging framework, event listener, or peer object to register itself for callbacks.
      </li>
    </ol>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The First-Person Pronoun "I / Me / My"</span>
  </div>
  <p>
    Consider human dialogue in an office meeting:
  </p>
  <ul>
    <li>When <strong>Alice</strong> stands up and says, <em>"My employee ID is 101, and I am working on project Apollo,"</em> the word "My" refers directly to Alice.</li>
    <li>When <strong>Bob</strong> stands up two minutes later and repeats the exact same sentence, <em>"My employee ID is 202, and I am working on project Hermes,"</em> the word "My" now refers directly to Bob.</li>
    <li>The speech script (function code in the text segment) is identical, but the personal pronoun (<code>this</code> pointer) points to whichever human is currently speaking!</li>
  </ul>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 21.1: The Hidden this Pointer Binding During Member Function Invocations</div>
  <svg viewBox="0 0 880 320" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="880" height="320" fill="#0b1120" rx="12"/>

    <!-- Object 1 -->
    <rect x="50" y="50" width="220" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="160" y="80" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Object 1: emp1</text>
    <text x="160" y="105" fill="#94a3b8" font-size="12" text-anchor="middle">id = 101 | Address: 0x1000</text>
    <text x="160" y="125" fill="#38bdf8" font-size="11" font-family="monospace" text-anchor="middle">emp1.display()</text>

    <!-- Object 2 -->
    <rect x="50" y="180" width="220" height="90" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="160" y="210" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">Object 2: emp2</text>
    <text x="160" y="235" fill="#94a3b8" font-size="12" text-anchor="middle">id = 202 | Address: 0x2000</text>
    <text x="160" y="255" fill="#f59e0b" font-size="11" font-family="monospace" text-anchor="middle">emp2.display()</text>

    <!-- Shared Code Function in RAM -->
    <rect x="500" y="70" width="340" height="180" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="670" y="105" fill="#34d399" font-size="15" font-weight="bold" text-anchor="middle">Shared Code: Employee::display()</text>
    <rect x="520" y="120" width="300" height="105" rx="6" fill="#0f172a" stroke="#475569"/>
    <text x="535" y="145" fill="#e2e8f0" font-size="12" font-family="monospace">// Hidden translation by C++ compiler:</text>
    <text x="535" y="170" fill="#a7f3d0" font-size="12" font-family="monospace">void display(Employee* const this) {</text>
    <text x="555" y="195" fill="#38bdf8" font-size="12" font-family="monospace">cout &lt;&lt; this-&gt;id &lt;&lt; endl;</text>
    <text x="535" y="215" fill="#a7f3d0" font-size="12" font-family="monospace">}</text>

    <!-- Connecting Arrows -->
    <path d="M 270 95 C 380 95, 410 130, 495 130" stroke="#38bdf8" stroke-width="2.5" fill="none" marker-end="url(#arrow-blue)"/>
    <text x="375" y="115" fill="#38bdf8" font-size="11" text-anchor="middle">this = 0x1000</text>

    <path d="M 270 225 C 380 225, 410 180, 495 180" stroke="#f59e0b" stroke-width="2.5" fill="none" marker-end="url(#arrow-amber)"/>
    <text x="375" y="210" fill="#f59e0b" font-size="11" text-anchor="middle">this = 0x2000</text>

    <defs>
      <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/>
      </marker>
    </defs>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>The this Pointer: Shadowing Resolution &amp; Method Chaining</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;string&gt;
using namespace std;

class BankAccount {
private:
    string owner;
    double balance;

public:
    // 1. Resolving Parameter Shadowing:
    // Local parameters 'owner' and 'balance' have identical names to member variables
    BankAccount(string owner, double balance) {
        this-&gt;owner = owner;       // this-&gt;owner refers to member; owner refers to parameter
        this-&gt;balance = balance;   // this-&gt;balance refers to member; balance refers to parameter
    }

    // 2. Method Chaining: Returning *this by reference
    BankAccount&amp; deposit(double amount) {
        this-&gt;balance += amount;
        cout &lt;&lt; "[Deposit] Added $" &lt;&lt; amount &lt;&lt; endl;
        return *this; // Returns reference to the current invoking object
    }

    BankAccount&amp; withdraw(double amount) {
        if (amount &lt;= this-&gt;balance) {
            this-&gt;balance -= amount;
            cout &lt;&lt; "[Withdraw] Deducted $" &lt;&lt; amount &lt;&lt; endl;
        } else {
            cout &lt;&lt; "[Error] Insufficient funds!" &lt;&lt; endl;
        }
        return *this; // Returns reference to self
    }

    void display() const {
        cout &lt;&lt; "Account Owner: " &lt;&lt; this-&gt;owner 
             &lt;&lt; " | Final Balance: $" &lt;&lt; this-&gt;balance &lt;&lt; endl;
    }
};

int main() {
    // Instantiate account
    BankAccount acc("Vikram", 1000.0);

    // Fluent API / Method Chaining using 'return *this'
    cout &lt;&lt; "--- Executing Chained Transactions ---" &lt;&lt; endl;
    acc.deposit(500.0)
       .withdraw(200.0)
       .deposit(750.0);

    cout &lt;&lt; "\n--- Account Summary ---" &lt;&lt; endl;
    acc.display();

    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>--- Executing Chained Transactions ---
[Deposit] Added $500
[Withdraw] Deducted $200
[Deposit] Added $750

--- Account Summary ---
Account Owner: Vikram | Final Balance: $2050</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> What is the exact type of <code>this</code> inside a class named <code>Car</code>? (<code>Car* const this</code>).</li>
    <li><span class="check-box"></span> Can a static member function use the <code>this</code> pointer? (No, static functions have no object context).</li>
    <li><span class="check-box"></span> How does a function enable method chaining? (By returning <code>*this</code> by reference).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"Explain the significance of the this pointer with examples illustrating parameter shadowing and returning reference."</em> Always write: 1) Definition, 2) Disambiguation example (<code>this-&gt;x = x</code>), 3) Cascade method chaining (<code>return *this</code>).
</div>
"""
    sections.append({
        "id": "u5-sec-21",
        "number": 21,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "21. this Pointer",
        "subtitle": "Implicit Object Identity, Parameter Shadowing Disambiguation & Fluent Method Chaining",
        "content": sec21_content
    })

    # =========================================================================
    # SECTION 22: Virtual Functions
    # =========================================================================
    sec22_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4</div>
    <h3 class="card-title">22. Virtual Functions: Runtime Polymorphism &amp; Dynamic Dispatch</h3>
  </div>

  <div class="detail-block">
    <h5>22.1 What is a Virtual Function?</h5>
    <p>
      A <strong>Virtual Function</strong> is a member function declared within a Base Class using the keyword <code>virtual</code> and re-defined (overridden) in one or more Derived Classes.
    </p>
    <p>
      When a function is declared virtual, C++ implements <strong>Late Binding (Dynamic Binding)</strong>: when that function is invoked through a <strong>Base Class pointer or reference</strong>, C++ determines at <em>runtime</em> which version of the function to execute based on the actual type of the object pointed to, rather than the static type of the pointer!
    </p>
  </div>

  <div class="detail-block">
    <h5>22.2 Internal Mechanics: The vtable and vptr Architecture</h5>
    <p>
      How does C++ achieve runtime dynamic dispatch under the hood with near-zero overhead? It utilizes two compiler-generated structures:
    </p>
    <ul>
      <li><strong>Virtual Table (<code>vtable</code>):</strong> A static array of function pointers created by the compiler for every class that contains at least one virtual function. Each entry in the <code>vtable</code> points to the most-derived implementation of the virtual function for that class.</li>
      <li><strong>Virtual Table Pointer (<code>vptr</code>):</strong> A hidden pointer automatically inserted by the compiler into every object instance of a class with virtual functions. <code>vptr</code> points directly to that class's <code>vtable</code>.</li>
    </ul>
    <p>
      When executing <code>bPtr-&gt;draw()</code>, the processor:
      <br>1. Follows <code>bPtr</code> to the object in memory.
      <br>2. Reads the object's hidden <code>vptr</code>.
      <br>3. Indexes into the corresponding <code>vtable</code> to retrieve the function address.
      <br>4. Jumps to and executes that specific function!
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Emergency Hospital Triage Dispatcher</span>
  </div>
  <p>
    Imagine an emergency room incoming dispatch console:
  </p>
  <ul>
    <li>The chief medical dispatcher receives a radio call: <em>"Inbound critical casualty, initiate standard resuscitation protocol (<code>bPtr-&gt;treat()</code>)!"</em></li>
    <li>The chief dispatcher does not perform the surgery herself; she glances at the active duty schedule board (<strong>vtable</strong>).</li>
    <li>If the patient is a pediatric cardiac trauma victim (<strong>Derived Object</strong>), the schedule board routes the order directly to the Pediatric Heart Surgeon.</li>
    <li>If the patient is a severe burn victim, the board routes the order to the Plastic Reconstructive Team.</li>
    <li>The radio protocol is identical (Base interface), but the duty schedule board (vtable) dynamically dispatches the right specialist at the exact moment of arrival!</li>
  </ul>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 22.1: Architectural Layout of vptr, vtable, and Dynamic Dispatch</div>
  <svg viewBox="0 0 920 370" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="920" height="370" fill="#0b1120" rx="12"/>

    <!-- Object in Memory -->
    <rect x="50" y="80" width="240" height="180" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="110" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Derived Object in RAM</text>
    
    <!-- vptr hidden member -->
    <rect x="70" y="130" width="200" height="42" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="170" y="156" fill="#f59e0b" font-size="13" font-family="monospace" font-weight="bold" text-anchor="middle">vptr (8 bytes)</text>

    <!-- Regular member data -->
    <rect x="70" y="185" width="200" height="50" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="170" y="215" fill="#94a3b8" font-size="12" text-anchor="middle">int radius (data members)</text>

    <!-- Connecting Arrow from vptr to vtable -->
    <path d="M 270 151 C 340 151, 370 110, 420 110" stroke="#f59e0b" stroke-width="2.5" fill="none" marker-end="url(#arrow-amber)"/>

    <!-- vtable of Derived Class -->
    <rect x="430" y="60" width="220" height="150" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="540" y="90" fill="#fbbf24" font-size="14" font-weight="bold" text-anchor="middle">Derived::vtable</text>
    <rect x="450" y="110" width="180" height="35" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="540" y="132" fill="#e2e8f0" font-size="11" font-family="monospace" text-anchor="middle">&amp;Derived::draw()</text>
    <rect x="450" y="155" width="180" height="35" rx="4" fill="#0f172a" stroke="#475569"/>
    <text x="540" y="177" fill="#e2e8f0" font-size="11" font-family="monospace" text-anchor="middle">&amp;Derived::area()</text>

    <!-- Connecting Arrow from vtable entry to code segment -->
    <path d="M 630 127 C 675 127, 690 127, 720 127" stroke="#34d399" stroke-width="2.5" fill="none" marker-end="url(#arrow-green)"/>

    <!-- Code Segment in Memory -->
    <rect x="730" y="80" width="150" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="805" y="115" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Text Segment</text>
    <text x="805" y="145" fill="#e2e8f0" font-size="12" font-family="monospace" text-anchor="middle">Derived::draw()</text>

    <defs>
      <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
      </marker>
    </defs>

    <text x="460" y="300" fill="#94a3b8" font-size="12" text-anchor="middle">
      1. Base* bPtr points to Object &bull; 2. bPtr reads vptr &bull; 3. vptr indexes into Derived::vtable &bull; 4. Derived::draw() is executed!
    </text>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>Virtual Functions and Dynamic Polymorphism</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;vector&gt;
using namespace std;

// Base Class with Virtual Function
class Shape {
public:
    // Virtual destructor is ESSENTIAL when dealing with polymorphic base classes!
    virtual ~Shape() {
        cout &lt;&lt; "[Destructor] Shape destroyed." &lt;&lt; endl;
    }

    // Declaring function virtual enables dynamic late binding
    virtual void draw() const {
        cout &lt;&lt; "[Base Shape] Drawing generic shape." &lt;&lt; endl;
    }
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}

    // Overriding the virtual function
    void draw() const override {
        cout &lt;&lt; "[Circle] Drawing circle with radius = " &lt;&lt; radius &lt;&lt; endl;
    }

    ~Circle() override {
        cout &lt;&lt; "[Destructor] Circle destroyed." &lt;&lt; endl;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}

    void draw() const override {
        cout &lt;&lt; "[Rectangle] Drawing rectangle " &lt;&lt; width &lt;&lt; "x" &lt;&lt; height &lt;&lt; endl;
    }

    ~Rectangle() override {
        cout &lt;&lt; "[Destructor] Rectangle destroyed." &lt;&lt; endl;
    }
};

int main() {
    // Array of Base class pointers pointing to diverse derived objects
    Shape* shapes[2];
    shapes[0] = new Circle(5.5);
    shapes[1] = new Rectangle(4.0, 8.0);

    cout &lt;&lt; "--- Executing Dynamic Dispatch Loop ---" &lt;&lt; endl;
    for (int i = 0; i &lt; 2; i++) {
        // At runtime, C++ follows vptr -&gt; vtable to invoke the exact derived method!
        shapes[i]-&gt;draw();
    }

    cout &lt;&lt; "\n--- Polymorphic Cleanup ---" &lt;&lt; endl;
    for (int i = 0; i &lt; 2; i++) {
        delete shapes[i]; // Correctly calls Derived then Base destructor due to virtual ~Shape()
    }

    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>--- Executing Dynamic Dispatch Loop ---
[Circle] Drawing circle with radius = 5.5
[Rectangle] Drawing rectangle 4x8

--- Polymorphic Cleanup ---
[Destructor] Circle destroyed.
[Destructor] Shape destroyed.
[Destructor] Rectangle destroyed.
[Destructor] Shape destroyed.</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> Can a constructor be declared <code>virtual</code>? (No, memory and vptr do not exist yet).</li>
    <li><span class="check-box"></span> Why must a base class destructor be declared <code>virtual</code>? (To ensure the derived destructor executes when deleting through a base pointer).</li>
    <li><span class="check-box"></span> What are <code>vtable</code> and <code>vptr</code>? (vtable is the array of function pointers; vptr is the object's hidden pointer to its class vtable).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"Explain virtual functions, late binding, and the working of vtable and vptr with a diagram."</em> This is the #1 most frequently repeated question in Unit 5. Draw Figure 22.1 and trace how <code>bPtr-&gt;draw()</code> resolves via <code>vptr</code>.
</div>
"""
    sections.append({
        "id": "u5-sec-22",
        "number": 22,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "22. Virtual Functions",
        "subtitle": "Runtime Polymorphism, Dynamic Dispatch, vtable Function Array & vptr Indirection",
        "content": sec22_content
    })

    # =========================================================================
    # SECTION 23: Pure Virtual Functions and Abstract Classes
    # =========================================================================
    sec23_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4</div>
    <h3 class="card-title">23. Pure Virtual Functions &amp; Abstract Classes: Interface Contracts</h3>
  </div>

  <div class="detail-block">
    <h5>23.1 What is a Pure Virtual Function?</h5>
    <p>
      A <strong>Pure Virtual Function</strong> (or abstract function) is a virtual function declared inside a base class that has <em>no implementation</em> within that base class. It is denoted by the pure specifier syntax <code>= 0</code>:
    </p>
    <div class="code-box">
      <code>virtual void functionName() = 0;&nbsp;&nbsp;// Pure virtual function declaration</code>
    </div>
    <p>
      A pure virtual function acts as an uncompromisable <strong>architectural contract</strong>: it commands all non-abstract derived classes to provide their own concrete implementation of this function.
    </p>
  </div>

  <div class="detail-block">
    <h5>23.2 What is an Abstract Class?</h5>
    <p>
      An <strong>Abstract Class</strong> in C++ is any class that contains <em>at least one</em> pure virtual function.
    </p>
    <ul>
      <li><strong>Instantiation Prohibited:</strong> You CANNOT instantiate an object of an abstract class (e.g. <code>AbstractClass obj;</code> will trigger a compilation error).</li>
      <li><strong>Pointers and References Permitted:</strong> You CAN declare pointers and references of abstract class type (e.g. <code>AbstractClass* ptr;</code> is 100% valid and represents the cornerstone of polymorphic interface architecture).</li>
      <li><strong>Concrete Classes:</strong> A derived class that overrides and implements ALL pure virtual functions from its abstract base class is called a <em>Concrete Class</em>, and can be instantiated freely.</li>
      <li><strong>Pure Abstract Class (Interface):</strong> A class containing ONLY pure virtual functions and no data members is equivalent to a Java/C# Interface.</li>
    </ul>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The ISO Wall Socket Specification</span>
  </div>
  <p>
    Consider the international regulatory standards committee that designs the specification for electrical wall sockets:
  </p>
  <ul>
    <li>The standard document defines: <em>"Any electrical appliance plug must have a ground pin, line pin, and neutral pin, and must implement <code>connectPower()</code>."</em></li>
    <li>You cannot plug the regulatory paper document (Abstract Class) into the wall to power your laptop; it is merely an architectural specification.</li>
    <li>A manufacturer creates a physical Indian 3-pin plug or a British Type-G plug (Concrete Derived Class). That physical plug strictly satisfies every specification clause and can be plugged in and instantiated!</li>
  </ul>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 23.1: Abstract Class Contract &amp; Concrete Implementations</div>
  <svg viewBox="0 0 880 340" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="880" height="340" fill="#0b1120" rx="12"/>

    <!-- Abstract Base Class -->
    <rect x="300" y="30" width="280" height="110" rx="8" fill="#1e293b" stroke="#ec4899" stroke-width="2.5"/>
    <text x="440" y="58" fill="#f472b6" font-size="13" font-style="italic" text-anchor="middle">&lt;&lt;Abstract Class&gt;&gt;</text>
    <text x="440" y="78" fill="#ec4899" font-size="16" font-weight="bold" text-anchor="middle">PaymentGateway</text>
    <line x1="300" y1="90" x2="580" y2="90" stroke="#ec4899" stroke-width="1.5"/>
    <text x="440" y="112" fill="#fda4af" font-size="12" font-family="monospace" text-anchor="middle">+ virtual void pay(double) = 0</text>
    <text x="440" y="130" fill="#94a3b8" font-size="11" text-anchor="middle">[Cannot Instantiate Directly]</text>

    <!-- Branch Lines -->
    <path d="M 370 140 L 200 210" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrow-inherit)"/>
    <path d="M 510 140 L 680 210" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrow-inherit)"/>

    <!-- Concrete Derived 1 -->
    <rect x="80" y="210" width="250" height="95" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="205" y="235" fill="#34d399" font-size="14" font-weight="bold" text-anchor="middle">PayPalGateway</text>
    <text x="205" y="255" fill="#94a3b8" font-size="11" text-anchor="middle">[Concrete Class &bull; Instantiable]</text>
    <line x1="80" y1="265" x2="330" y2="265" stroke="#334155" stroke-width="1"/>
    <text x="205" y="285" fill="#a7f3d0" font-size="12" font-family="monospace" text-anchor="middle">+ void pay(double) override</text>

    <!-- Concrete Derived 2 -->
    <rect x="550" y="210" width="250" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="675" y="235" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">CreditCardGateway</text>
    <text x="675" y="255" fill="#94a3b8" font-size="11" text-anchor="middle">[Concrete Class &bull; Instantiable]</text>
    <line x1="550" y1="265" x2="800" y2="265" stroke="#334155" stroke-width="1"/>
    <text x="675" y="285" fill="#bae6fd" font-size="12" font-family="monospace" text-anchor="middle">+ void pay(double) override</text>

    <defs>
      <marker id="arrow-inherit" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <polygon points="0,0 10,5 0,10" fill="none" stroke="#64748b" stroke-width="1.5"/>
      </marker>
    </defs>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>Pure Virtual Functions and Abstract Classes in C++</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;string&gt;
using namespace std;

// Abstract Base Class: Cannot be instantiated!
class PaymentGateway {
protected:
    string merchantId;
public:
    PaymentGateway(string mId) : merchantId(mId) {}

    virtual ~PaymentGateway() {
        cout &lt;&lt; "[Destructor] PaymentGateway base cleaned up." &lt;&lt; endl;
    }

    // Pure Virtual Function: Defines obligatory contract
    virtual void processTransaction(double amount) = 0;

    // Normal non-virtual or virtual function with shared logic
    void logTransaction(double amount) {
        cout &lt;&lt; "[Audit Log] Merchant " &lt;&lt; merchantId 
             &lt;&lt; " registered transaction of $" &lt;&lt; amount &lt;&lt; endl;
    }
};

// Concrete Derived Class 1
class PayPal : public PaymentGateway {
private:
    string paypalEmail;
public:
    PayPal(string mId, string email) : PaymentGateway(mId), paypalEmail(email) {}

    // Mandatory concrete implementation
    void processTransaction(double amount) override {
        cout &lt;&lt; "[PayPal] Routing $" &lt;&lt; amount 
             &lt;&lt; " via secure token for account: " &lt;&lt; paypalEmail &lt;&lt; endl;
    }
};

// Concrete Derived Class 2
class CryptoPay : public PaymentGateway {
private:
    string walletAddress;
public:
    CryptoPay(string mId, string wallet) : PaymentGateway(mId), walletAddress(wallet) {}

    // Mandatory concrete implementation
    void processTransaction(double amount) override {
        cout &lt;&lt; "[CryptoPay] Broadcasting $" &lt;&lt; amount 
             &lt;&lt; " transaction to blockchain address: " &lt;&lt; walletAddress &lt;&lt; endl;
    }
};

int main() {
    // PaymentGateway pg("MERCH_01"); // COMPILATION ERROR! Cannot instantiate abstract class!

    // Using Abstract Base Class Pointers for true polymorphic decoupling
    PaymentGateway* gateway = nullptr;

    int userChoice = 1; // 1 for PayPal, 2 for Crypto
    if (userChoice == 1) {
        gateway = new PayPal("MERCH_99", "checkout@store.com");
    } else {
        gateway = new CryptoPay("MERCH_99", "0x7F2A...3B");
    }

    gateway-&gt;logTransaction(149.99);
    gateway-&gt;processTransaction(149.99); // Dynamic dispatch to PayPal::processTransaction

    delete gateway; // Polymorphic destruction
    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>[Audit Log] Merchant MERCH_99 registered transaction of $149.99
[PayPal] Routing $149.99 via secure token for account: checkout@store.com
[Destructor] PaymentGateway base cleaned up.</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> What is the syntax of a pure virtual function? (<code>virtual void func() = 0;</code>).</li>
    <li><span class="check-box"></span> Can you instantiate an abstract class? (No, direct instantiation is a compilation error).</li>
    <li><span class="check-box"></span> Can you create pointers to an abstract class? (Yes, abstract class pointers are essential for polymorphic interfaces).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> <em>"What is an abstract class? What is the role of pure virtual functions in achieving abstraction?"</em> State: 1) Abstract class contains ≥ 1 pure virtual function (<code>= 0</code>), 2) Cannot be instantiated, 3) Mandates derived classes to provide concrete definitions, 4) Provides pure interface contracts.
</div>
"""
    sections.append({
        "id": "u5-sec-23",
        "number": 23,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "23. Pure Virtual Functions & Abstract Classes",
        "subtitle": "Interface Contracts (= 0), Mandatory Derived Overrides & Polymorphic Decoupling",
        "content": sec23_content
    })

    # =========================================================================
    # SECTION 24: Implementing Polymorphism: Complete Pipeline Architecture
    # =========================================================================
    sec24_content = """
<div class="concept-card">
  <div class="card-header">
    <div class="card-badge">AKTU Quantum Core &bull; Unit 5 Part 4 (Capstone)</div>
    <h3 class="card-title">24. Implementing Polymorphism: Complete Pipeline &amp; Architectural Synthesis</h3>
  </div>

  <div class="detail-block">
    <h5>24.1 Unified Architectural Comparison Matrix</h5>
    <p>
      Mastering Object-Oriented Software Development requires understanding the exact mechanical trade-offs between Compile-Time and Run-Time polymorphism:
    </p>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Criterion</th>
            <th>Compile-Time (Static) Polymorphism</th>
            <th>Run-Time (Dynamic) Polymorphism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Resolution Time</strong></td>
            <td>During Compilation (Symbol table lookup &amp; name mangling).</td>
            <td>During Program Execution (Dynamic vtable pointer lookup).</td>
          </tr>
          <tr>
            <td><strong>Language Tools</strong></td>
            <td>Function Overloading, Operator Overloading, C++ Templates.</td>
            <td>Virtual Functions, Pure Virtual Functions, Abstract Classes.</td>
          </tr>
          <tr>
            <td><strong>Inheritance Needed?</strong></td>
            <td>No. Can be implemented inside a single class or globally.</td>
            <td>Yes. Requires an inheritance hierarchy with base pointers/references.</td>
          </tr>
          <tr>
            <td><strong>Performance Cost</strong></td>
            <td>Zero runtime penalty. Direct hardware <code>CALL &lt;address&gt;</code>.</td>
            <td>Minor runtime indirect jump penalty (dereference <code>vptr</code> + index <code>vtable</code>).</td>
          </tr>
          <tr>
            <td><strong>Memory Overhead</strong></td>
            <td>None.</td>
            <td>+8 bytes per object for <code>vptr</code>; 1 static <code>vtable</code> array per class.</td>
          </tr>
          <tr>
            <td><strong>Architectural Power</strong></td>
            <td>High-speed mathematical libraries, container templates (STL).</td>
            <td>Extensible enterprise plugins, game engines, device driver abstractions.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="detail-block">
    <h5>24.2 Complete Pipeline Architecture Flowchart</h5>
    <p>
      How a modern C++ compiler and runtime engine process polymorphic expressions:
    </p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">
    <span class="analogy-icon">💡</span>
    <span>Real-Life Analogy: The Global Intermodal Freight Container Hub</span>
  </div>
  <p>
    Consider the international freight shipping system that powers modern global commerce:
  </p>
  <ul>
    <li>A manufacturing exporter packages goods inside a standard ISO steel container and signs a universal freight manifest: <code>IntermodalFreight* cargo = new ElectronicsContainer(); cargo-&gt;dispatch();</code>. The exporter needs to know only the universal manifest interface!</li>
    <li>At the transshipment port, the dynamic dispatch system (<strong>vtable lookup</strong>) inspects the cargo tag:</li>
    <li>If destined for maritime transport, heavy dock gantry cranes load it onto a 20,000-TEU container ship (<strong>Derived::dispatch via OceanCarrier</strong>).</li>
    <li>If destined for transcontinental land transport, high-speed rail cranes mount it onto electrified freight trains (<strong>Derived::dispatch via RailFreight</strong>).</li>
    <li>The container specification and bill of lading (Base Interface) remain 100% unified, but the underlying transportation machinery adapts dynamically to move the goods across oceans, tracks, and roads seamlessly!</li>
  </ul>
</div>

<div class="diagram-wrapper">
  <div class="diagram-title">Figure 24.1: The Unified Compilation &amp; Execution Pipeline of Polymorphic C++ Code</div>
  <svg viewBox="0 0 940 400" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; font-family:'Segoe UI',sans-serif;">
    <rect width="940" height="400" fill="#0b1120" rx="12"/>

    <!-- Source Code Box -->
    <rect x="30" y="160" width="160" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="110" y="190" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Source Code</text>
    <text x="110" y="210" fill="#94a3b8" font-size="11" text-anchor="middle">invokes obj-&gt;action()</text>

    <!-- Arrow to Compiler Decision -->
    <line x1="190" y1="195" x2="260" y2="195" stroke="#64748b" stroke-width="2" marker-end="url(#arrow-slate)"/>

    <!-- Decision Diamond -->
    <polygon points="350,140 440,195 350,250 260,195" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="350" y="192" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Is action()</text>
    <text x="350" y="208" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">virtual?</text>

    <!-- Branch NO -> Compile-Time Path -->
    <path d="M 350 140 L 350 70 L 480 70" stroke="#818cf8" stroke-width="2" fill="none" marker-end="url(#arrow-indigo)"/>
    <text x="365" y="105" fill="#818cf8" font-size="11" font-weight="bold">NO (Static)</text>

    <rect x="490" y="45" width="220" height="55" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="600" y="68" fill="#818cf8" font-size="12" font-weight="bold" text-anchor="middle">Static Signature Binding</text>
    <text x="600" y="86" fill="#94a3b8" font-size="10" text-anchor="middle">Name mangling &bull; Direct CALL emitted</text>

    <line x1="710" y1="70" x2="760" y2="70" stroke="#818cf8" stroke-width="2" marker-end="url(#arrow-indigo)"/>
    <rect x="770" y="45" width="140" height="55" rx="6" fill="#0f172a" stroke="#818cf8"/>
    <text x="840" y="70" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle">Direct Execution</text>
    <text x="840" y="88" fill="#94a3b8" font-size="9" text-anchor="middle">Zero runtime lookup</text>

    <!-- Branch YES -> Runtime Path -->
    <path d="M 350 250 L 350 320 L 480 320" stroke="#34d399" stroke-width="2" fill="none" marker-end="url(#arrow-green)"/>
    <text x="365" y="285" fill="#34d399" font-size="11" font-weight="bold">YES (Dynamic)</text>

    <rect x="490" y="295" width="220" height="55" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="600" y="318" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Dynamic Dispatch Pipeline</text>
    <text x="600" y="336" fill="#94a3b8" font-size="10" text-anchor="middle">Emit: CALL *(bPtr-&gt;vptr[slot])</text>

    <line x1="710" y1="320" x2="760" y2="320" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <rect x="770" y="295" width="140" height="55" rx="6" fill="#0f172a" stroke="#34d399"/>
    <text x="840" y="320" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">Runtime vtable</text>
    <text x="840" y="338" fill="#94a3b8" font-size="9" text-anchor="middle">Dispatches to Derived</text>

    <defs>
      <marker id="arrow-slate" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
      </marker>
      <marker id="arrow-indigo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#818cf8"/>
      </marker>
      <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
      </marker>
    </defs>
  </svg>
</div>

<div class="code-example-card">
  <div class="card-header">
    <span class="code-icon">💻</span>
    <h4>Complete Enterprise Synthesis: Autonomous Cloud Storage Engine</h4>
  </div>
  <pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;string&gt;
using namespace std;

// 1. Abstract Base Class establishing the architectural contract
class StorageEngine {
protected:
    string bucketName;
    size_t totalBytesUploaded;

public:
    StorageEngine(string bName) : bucketName(bName), totalBytesUploaded(0) {
        cout &lt;&lt; "[Base Constructor] Initialized Storage Engine for bucket: " &lt;&lt; bucketName &lt;&lt; endl;
    }

    // Virtual destructor is vital for polymorphic cleanup!
    virtual ~StorageEngine() {
        cout &lt;&lt; "[Base Destructor] Storage Engine for " &lt;&lt; bucketName &lt;&lt; " shut down." &lt;&lt; endl;
    }

    // Pure Virtual Functions (Contract)
    virtual void uploadFile(const string&amp; filename, size_t fileSize) = 0;
    virtual void downloadFile(const string&amp; filename) = 0;

    // Common non-virtual utility
    void displayMetrics() const {
        cout &lt;&lt; "  --&gt; [Metrics] Bucket: " &lt;&lt; bucketName 
             &lt;&lt; " | Total Uploaded: " &lt;&lt; totalBytesUploaded &lt;&lt; " KB" &lt;&lt; endl;
    }
};

// 2. Concrete Implementation 1: AWS S3 Connector
class AWSS3Engine : public StorageEngine {
private:
    string region;
public:
    AWSS3Engine(string bName, string reg) 
        : StorageEngine(bName), region(reg) {}

    void uploadFile(const string&amp; filename, size_t fileSize) override {
        totalBytesUploaded += fileSize;
        cout &lt;&lt; "[AWS S3 - " &lt;&lt; region &lt;&lt; "] Uploaded '" &lt;&lt; filename 
             &lt;&lt; "' (" &lt;&lt; fileSize &lt;&lt; " KB) to S3 bucket '" &lt;&lt; bucketName &lt;&lt; "'." &lt;&lt; endl;
    }

    void downloadFile(const string&amp; filename) override {
        cout &lt;&lt; "[AWS S3 - " &lt;&lt; region &lt;&lt; "] Fetching object '" &lt;&lt; filename &lt;&lt; "' via HTTPS GET." &lt;&lt; endl;
    }

    ~AWSS3Engine() override {
        cout &lt;&lt; "[Derived Destructor] Closed AWS S3 TLS connection pool." &lt;&lt; endl;
    }
};

// 3. Concrete Implementation 2: Google Cloud Storage Connector
class GoogleCloudStorageEngine : public StorageEngine {
private:
    string projectId;
public:
    GoogleCloudStorageEngine(string bName, string proj) 
        : StorageEngine(bName), projectId(proj) {}

    void uploadFile(const string&amp; filename, size_t fileSize) override {
        totalBytesUploaded += fileSize;
        cout &lt;&lt; "[GCS - " &lt;&lt; projectId &lt;&lt; "] Chunked streaming upload for '" 
             &lt;&lt; filename &lt;&lt; "' (" &lt;&lt; fileSize &lt;&lt; " KB) to GCS bucket '" &lt;&lt; bucketName &lt;&lt; "'." &lt;&lt; endl;
    }

    void downloadFile(const string&amp; filename) override {
        cout &lt;&lt; "[GCS - " &lt;&lt; projectId &lt;&lt; "] Streaming file '" &lt;&lt; filename &lt;&lt; "' via gRPC stream." &lt;&lt; endl;
    }

    ~GoogleCloudStorageEngine() override {
        cout &lt;&lt; "[Derived Destructor] Closed GCS gRPC channel." &lt;&lt; endl;
    }
};

// Enterprise Manager operating strictly on Base Class Pointers (Polymorphism)
int main() {
    cout &lt;&lt; "=== CLOUD STORAGE ARCHITECTURE SYSTEM BOOT ===" &lt;&lt; endl;

    // Vector of polymorphic Base Class pointers
    vector&lt;StorageEngine*&gt; storageBackends;
    storageBackends.push_back(new AWSS3Engine("fintech-prod-s3", "us-east-1"));
    storageBackends.push_back(new GoogleCloudStorageEngine("analytics-lake-gcs", "gcp-corp-542"));

    cout &lt;&lt; "\n=== EXECUTING POLYMORPHIC STORAGE DISPATCH ===" &lt;&lt; endl;
    for (StorageEngine* engine : storageBackends) {
        // Dynamic dispatch routes to AWSS3Engine or GoogleCloudStorageEngine transparently!
        engine-&gt;uploadFile("transaction_log_2026.csv", 4500);
        engine-&gt;downloadFile("master_config.json");
        engine-&gt;displayMetrics();
        cout &lt;&lt; "------------------------------------------------" &lt;&lt; endl;
    }

    cout &lt;&lt; "=== RELEASING SYSTEM RESOURCES VIA VIRTUAL DESTRUCTORS ===" &lt;&lt; endl;
    for (StorageEngine* engine : storageBackends) {
        delete engine; // Properly triggers Derived then Base destructors!
    }

    return 0;
}</code></pre>
  <div class="terminal-output">
    <div class="terminal-header">Terminal Execution Output</div>
    <pre>=== CLOUD STORAGE ARCHITECTURE SYSTEM BOOT ===
[Base Constructor] Initialized Storage Engine for bucket: fintech-prod-s3
[Base Constructor] Initialized Storage Engine for bucket: analytics-lake-gcs

=== EXECUTING POLYMORPHIC STORAGE DISPATCH ===
[AWS S3 - us-east-1] Uploaded 'transaction_log_2026.csv' (4500 KB) to S3 bucket 'fintech-prod-s3'.
[AWS S3 - us-east-1] Fetching object 'master_config.json' via HTTPS GET.
  --&gt; [Metrics] Bucket: fintech-prod-s3 | Total Uploaded: 4500 KB
------------------------------------------------
[GCS - gcp-corp-542] Chunked streaming upload for 'transaction_log_2026.csv' (4500 KB) to GCS bucket 'analytics-lake-gcs'.
[GCS - gcp-corp-542] Streaming file 'master_config.json' via gRPC stream.
  --&gt; [Metrics] Bucket: analytics-lake-gcs | Total Uploaded: 4500 KB
------------------------------------------------
=== RELEASING SYSTEM RESOURCES VIA VIRTUAL DESTRUCTORS ===
[Derived Destructor] Closed AWS S3 TLS connection pool.
[Base Destructor] Storage Engine for fintech-prod-s3 shut down.
[Derived Destructor] Closed GCS gRPC channel.
[Base Destructor] Storage Engine for analytics-lake-gcs shut down.</pre>
  </div>
</div>

<div class="checklist-card">
  <div class="checklist-header">
    <span class="checklist-icon">📋</span>
    <span>Self-Recall Checklist &amp; Exam Quick-Prep</span>
  </div>
  <ul class="checklist-items">
    <li><span class="check-box"></span> How does C++ dispatch a function call when it is declared <code>virtual</code>? (Via the object's <code>vptr</code> indexing into the class <code>vtable</code> at runtime).</li>
    <li><span class="check-box"></span> Why is compile-time polymorphism faster than run-time polymorphism? (Direct machine instruction CALL vs indirect pointer dereference).</li>
    <li><span class="check-box"></span> What is the role of virtual destructors in polymorphism? (Guarantees derived destructors run when deleting through base pointers, avoiding memory leaks).</li>
  </ul>
</div>

<div class="exam-tip">
  <strong>AKTU Exam Tip:</strong> In the comprehensive 10-mark capstone question <em>"Discuss how polymorphism is achieved in C++ through compile-time and run-time mechanisms"</em>, summarize all 5 architectural tenets: classes, constructors, inheritance, virtual functions, and abstract interfaces. Present the complete pipeline diagram (Figure 24.1).
</div>
"""
    sections.append({
        "id": "u5-sec-24",
        "number": 24,
        "part": "PART 4 — POLYMORPHISM AND POINTERS",
        "title": "24. Implementing Polymorphism: Complete Pipeline",
        "subtitle": "Synthesis of Compile-Time vs Runtime Dispatch, Enterprise Architecture & Capstone Systems",
        "content": sec24_content
    })

    return sections

if __name__ == "__main__":
    secs = get_unit5_part4_sections()
    print(f"generate_unit5_part4.py compiled {len(secs)} sections successfully.")
