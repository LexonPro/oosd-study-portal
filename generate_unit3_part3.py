# generate_unit3_part3.py: Part 3 - Object-Oriented Methodologies & Principles (Sections 20 to 28)

def get_unit3_part3_sections():
    return [
        {
            "id": "u3-sec-20",
            "number": "20",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Object-Oriented Programming Style",
            "subtitle": "Writing Elegant, Maintainable Code, High Cohesion, Loose Coupling & The Law of Demeter",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Software Craftsmanship</div>
    <h3>The Philosophy of Good OO Programming Style</h3>
    <p>Good object-oriented programming style is not merely about using classes; it is the discipline of structuring software so that it is <strong>readable, understandable, verifiable, and easily modified</strong> by other engineers.</p>
    <p>Clean OO code exhibits high cohesion (each class has a single, focused responsibility), loose coupling (minimal dependencies between subsystems), and respects the <strong>Principle of Least Knowledge (Law of Demeter)</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Paperboy &amp; The Customer's Wallet</div>
  <p>When a paperboy comes to your front porch to collect $2 for the Sunday newspaper, he does not say: <em>"Turn around while I reach into your jacket pocket, pull out your leather wallet, open the card flap, and take out a two-dollar bill."</em> That would be a catastrophic violation of personal privacy (and encapsulation)!</p>
  <p>Instead, the paperboy asks: <em>"That will be $2, please."</em> You open your own wallet and hand him the money. <strong>That is the Law of Demeter:</strong> Talk only to your immediate friends, never reach into strangers' pockets!</p>
</div>

<div class="subtopics-container">
  <h4>Key Principles of Superior OO Style</h4>

  <div class="detail-block">
    <h5>1. The Law of Demeter (Principle of Least Knowledge)</h5>
    <p>A method <code>M</code> of an object <code>O</code> should only invoke operations on:</p>
    <ul>
      <li><code>O</code> itself (its own methods).</li>
      <li>Parameters passed into <code>M</code>.</li>
      <li>Any objects instantiated or created within <code>M</code>.</li>
      <li>Direct member components of <code>O</code>.</li>
    </ul>
    <p><strong>Anti-Pattern to Avoid:</strong> Train-wreck method chains like <code>order.getCustomer().getWallet().getCard().charge(50);</code>. Instead, delegate: <code>order.processPayment(50);</code>.</p>
  </div>

  <div class="detail-block">
    <h5>2. High Cohesion &amp; Low Coupling</h5>
    <ul>
      <li><strong>High Cohesion:</strong> All methods and attributes inside a class are intimately related to a single, well-defined business concept.</li>
      <li><strong>Low Coupling:</strong> Classes interact through minimal, clean abstract interfaces rather than concrete internal structures.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Small, Focused Methods &amp; Naming Conventions</h5>
    <p>Methods should be brief (typically under 20-30 lines), perform exactly one task, and have intention-revealing names using active verbs (e.g., <code>calculateNetPay()</code> rather than <code>doData()</code>).</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Law of Demeter: Anti-Pattern vs Clean Style)</span>
    <span class="code-desc">Eliminating train-wreck dot chains with proper behavioral delegation</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-comment">/* --- Component Classes --- */</span>
<span class="c-keyword">class</span> <span class="c-type">Wallet</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">double</span> funds;
<span class="c-keyword">public:</span>
    Wallet(<span class="c-type">double</span> f) : funds(f) {}
    
    <span class="c-type">bool</span> deduct(<span class="c-type">double</span> amount) {
        <span class="c-keyword">if</span> (funds &gt;= amount) {
            funds -= amount;
            <span class="c-keyword">return true</span>;
        }
        <span class="c-keyword">return false</span>;
    }
    <span class="c-type">double</span> getBalance() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> funds; }
};

<span class="c-keyword">class</span> <span class="c-type">Customer</span> {
<span class="c-keyword">private:</span>
    std::string name;
    <span class="c-type">Wallet</span> wallet;
<span class="c-keyword">public:</span>
    Customer(std::string n, <span class="c-type">double</span> cash) : name(n), wallet(cash) {}

    <span class="c-comment">/* Clean OO Style: Encapsulated delegation adhering to Law of Demeter */</span>
    <span class="c-type">bool</span> pay(<span class="c-type">double</span> amount) {
        std::cout &lt;&lt; <span class="c-string">"["</span> &lt;&lt; name &lt;&lt; <span class="c-string">"] Opening personal wallet to pay $"</span> &lt;&lt; amount &lt;&lt; std::endl;
        <span class="c-keyword">return</span> wallet.deduct(amount);
    }
};

<span class="c-keyword">class</span> <span class="c-type">Paperboy</span> {
<span class="c-keyword">public:</span>
    <span class="c-type">void</span> collectPayment(<span class="c-type">Customer</span>&amp; customer, <span class="c-type">double</span> fee) {
        <span class="c-comment">/* ✅ DEMETER COMPLIANT: Paperboy talks only to his immediate client (Customer) */</span>
        <span class="c-type">bool</span> paid = customer.pay(fee);
        <span class="c-keyword">if</span> (paid) {
            std::cout &lt;&lt; <span class="c-string">"[Paperboy] Payment received! Delivered newspaper."</span> &lt;&lt; std::endl;
        } <span class="c-keyword">else</span> {
            std::cout &lt;&lt; <span class="c-string">"[Paperboy] Insufficient funds! No newspaper."</span> &lt;&lt; std::endl;
        }
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">Customer</span> john(<span class="c-string">"John Doe"</span>, 25.0);
    <span class="c-type">Paperboy</span> sam;
    sam.collectPayment(john, 2.50);
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The Law of Demeter Boundary Shield</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Caller: Client -->
      <rect x="50" y="90" width="140" height="70" rx="8" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
      <text x="120" y="122" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Paperboy</text>
      <text x="120" y="140" fill="#93c5fd" font-size="10" text-anchor="middle">(Caller Object)</text>

      <!-- Permitted Call Vector -->
      <path d="M 190 125 L 335 125" stroke="#34d399" stroke-width="3" marker-end="url(#green-arrow)"/>
      <text x="262" y="112" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">customer.pay()</text>
      <text x="262" y="140" fill="#a7f3d0" font-size="9" text-anchor="middle">✅ Allowed (Friend)</text>

      <!-- Immediate Friend: Customer -->
      <rect x="340" y="70" width="180" height="110" rx="8" fill="#065f46" stroke="#34d399" stroke-width="2"/>
      <text x="430" y="105" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Customer</text>
      <text x="430" y="125" fill="#a7f3d0" font-size="10" text-anchor="middle">Immediate Friend</text>
      <text x="430" y="150" fill="#e2e8f0" font-size="9" text-anchor="middle">Owns: Wallet wallet</text>

      <!-- Internal Delegation Vector -->
      <path d="M 520 125 L 635 125" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#cyan-demeter-arrow)"/>
      <text x="577" y="115" fill="#38bdf8" font-size="10" text-anchor="middle">internal call</text>

      <!-- Stranger Object: Wallet -->
      <rect x="640" y="80" width="160" height="90" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="720" y="115" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Wallet</text>
      <text x="720" y="135" fill="#cbd5e1" font-size="10" text-anchor="middle">Stranger to Paperboy</text>

      <!-- Prohibited Direct Bypass Vector (Red Arc) -->
      <path d="M 170 85 C 280 15, 520 15, 650 75" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6" marker-end="url(#red-demeter-arrow)"/>
      <text x="410" y="32" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">❌ FORBIDDEN: paperboy -&gt; customer.getWallet().deduct()</text>

      <defs>
        <marker id="green-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
        <marker id="cyan-demeter-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="red-demeter-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#ef4444"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2013-14):</strong> <em>"Explain the characteristics of good object-oriented programming style. Discuss the Law of Demeter with an example."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Cite the Law of Demeter (talk only to your immediate friends, never invoke methods on objects returned by another method). Explain the paperboy/wallet example. List High Cohesion, Low Coupling, and Small Focused Methods.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-21",
            "number": "21",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Reusability",
            "subtitle": "Code Reuse vs Design Reuse, Frameworks vs Libraries & Favoring Composition Over Inheritance",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Engineering Productivity</div>
    <h3>The Concept &amp; Benefits of Reusability</h3>
    <p><strong>Reusability</strong> is the software engineering principle where pre-existing source code, architectures, or design components are leveraged to implement new functionality with slight or no modification.</p>
    <p>Reusability dramatically <strong>reduces development cost, eliminates repetitive bug fixes, and accelerates time to market</strong>. In object-oriented software engineering, reusability operates at two distinct levels: <em>Code Reuse</em> and <em>Design Reuse</em>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Lego Bricks vs Heavy Cast Iron Mold</div>
  <p><strong>Inheritance-heavy reuse is like a heavy cast iron mold:</strong> If you mold an entire toy truck out of iron, you can't easily turn it into an airplane without melting and re-forging the entire mold.</p>
  <p><strong>Composition-based reuse is like Lego bricks:</strong> You have standard, modular blocks (wheels, cockpit, wings, motors). If you want an airplane, you assemble wings and wheels; if you want a submarine, you detach the wings and attach a propeller. <em>"Favor object composition over class inheritance!"</em></p>
</div>

<div class="subtopics-container">
  <h4>Rules &amp; Mechanisms of Effective Reusability</h4>

  <div class="detail-block">
    <h5>1. Code Reuse vs Design Reuse</h5>
    <ul>
      <li><strong>Code Reuse:</strong> Direct incorporation of compiled binary libraries or source classes (e.g., C++ STL <code>std::vector</code>, <code>std::map</code>, or Apache Commons).</li>
      <li><strong>Design Reuse:</strong> Reusing proven architectural patterns, frameworks, and abstract interactions (e.g., Gang of Four Design Patterns like Observer, Strategy, and Factory).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Rumbaugh's 8 Golden Rules for Reusability (AKTU Question 3.23)</h5>
    <ol>
      <li><strong>Keep methods coherent:</strong> Perform a single, well-defined mathematical or logical function.</li>
      <li><strong>Keep methods small:</strong> Decompose monolithic routines so smaller pieces can be individually reused.</li>
      <li><strong>Keep methods consistent:</strong> Use uniform naming and argument order across all classes.</li>
      <li><strong>Separate policy from implementation:</strong> High-level business decision logic should be detached from low-level data structure operations.</li>
      <li><strong>Provide uniform coverage:</strong> If you implement <code>add()</code>, also provide <code>remove()</code>, <code>contains()</code>, and <code>clear()</code>.</li>
      <li><strong>Broaden the method:</strong> Make parameter types general rather than overly narrow.</li>
      <li><strong>Avoid global information:</strong> Eliminate dependencies on global variables or hidden state.</li>
      <li><strong>Avoid modes:</strong> Avoid boolean mode flags that change the fundamental behavior of a routine.</li>
    </ol>
  </div>

  <div class="detail-block">
    <h5>3. Frameworks vs Libraries (Inversion of Control)</h5>
    <ul>
      <li><strong>Library:</strong> A collection of helper functions where <em>your code calls the library</em> (you retain control of the main loop).</li>
      <li><strong>Framework:</strong> A complete architectural skeleton where <em>the framework calls your code</em> via callbacks and hook methods (the "Hollywood Principle": <em>Don't call us, we'll call you</em>).</li>
    </ul>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Composition Over Inheritance)</span>
    <span class="code-desc">Strategy pattern demonstrating flexible, reusable component composition</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;memory&gt;</span>

<span class="c-comment">/* Reusable Strategy Interface 1: Attack Behavior */</span>
<span class="c-keyword">class</span> <span class="c-type">AttackBehavior</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">virtual</span> ~AttackBehavior() = <span class="c-keyword">default</span>;
    <span class="c-keyword">virtual void</span> attack() = 0;
};

<span class="c-comment">/* Concrete Reusable Strategy Components */</span>
<span class="c-keyword">class</span> <span class="c-type">LaserAttack</span> : <span class="c-keyword">public</span> <span class="c-type">AttackBehavior</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> attack() <span class="c-keyword">override</span> { std::cout &lt;&lt; <span class="c-string">"Firing high-power Plasma Laser! ⚡"</span> &lt;&lt; std::endl; }
};

<span class="c-keyword">class</span> <span class="c-type">PunchAttack</span> : <span class="c-keyword">public</span> <span class="c-type">AttackBehavior</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> attack() <span class="c-keyword">override</span> { std::cout &lt;&lt; <span class="c-string">"Delivering Heavy Titanium Punch! 🥊"</span> &lt;&lt; std::endl; }
};

<span class="c-comment">/* Context Class: Assembled via COMPOSITION rather than inheritance */</span>
<span class="c-keyword">class</span> <span class="c-type">BattleRobot</span> {
<span class="c-keyword">private:</span>
    std::string modelName;
    std::unique_ptr&lt;<span class="c-type">AttackBehavior</span>&gt; attackStyle; <span class="c-comment">/* Pluggable component */</span>

<span class="c-keyword">public:</span>
    BattleRobot(std::string name, std::unique_ptr&lt;<span class="c-type">AttackBehavior</span>&gt; style)
        : modelName(name), attackStyle(std::move(style)) {}

    <span class="c-comment">/* Runtime Swappability: Swap behaviors dynamically without modifying class! */</span>
    <span class="c-type">void</span> setAttackBehavior(std::unique_ptr&lt;<span class="c-type">AttackBehavior</span>&gt; newStyle) {
        attackStyle = std::move(newStyle);
    }

    <span class="c-type">void</span> performAction() {
        std::cout &lt;&lt; <span class="c-string">"["</span> &lt;&lt; modelName &lt;&lt; <span class="c-string">"] "</span>;
        attackStyle-&gt;attack();
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">/* Reusing LaserAttack component in robot 1 */</span>
    <span class="c-type">BattleRobot</span> warrior(<span class="c-string">"Mech-X"</span>, std::make_unique&lt;<span class="c-type">LaserAttack</span>&gt;());
    warrior.performAction();

    <span class="c-comment">/* Hot-swapping to PunchAttack at runtime! */</span>
    warrior.setAttackBehavior(std::make_unique&lt;<span class="c-type">PunchAttack</span>&gt;());
    warrior.performAction();

    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Rigid Inheritance vs Flexible Composition</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Left Box: Inheritance Explosion -->
      <rect x="40" y="25" width="360" height="230" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
      <text x="220" y="52" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle">❌ Rigid Inheritance (Class Explosion)</text>

      <rect x="145" y="70" width="150" height="35" rx="4" fill="#0f172a" stroke="#64748b"/>
      <text x="220" y="92" fill="#ffffff" font-size="11" text-anchor="middle">Robot (Base)</text>

      <path d="M 180 105 L 100 145" stroke="#64748b" stroke-width="1.5"/>
      <path d="M 260 105 L 340 145" stroke="#64748b" stroke-width="1.5"/>

      <rect x="50" y="145" width="110" height="35" rx="4" fill="#334155"/>
      <text x="105" y="167" fill="#cbd5e1" font-size="10" text-anchor="middle">FlyingRobot</text>

      <rect x="280" y="145" width="110" height="35" rx="4" fill="#334155"/>
      <text x="335" y="167" fill="#cbd5e1" font-size="10" text-anchor="middle">SwimmingRobot</text>

      <path d="M 105 180 L 220 205" stroke="#ef4444" stroke-width="1.5"/>
      <path d="M 335 180 L 220 205" stroke="#ef4444" stroke-width="1.5"/>

      <rect x="130" y="205" width="180" height="35" rx="4" fill="#7f1d1d" stroke="#ef4444"/>
      <text x="220" y="227" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">FlyingSwimmingLaserRobot?!</text>

      <!-- Right Box: Pluggable Composition -->
      <rect x="440" y="25" width="360" height="230" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="620" y="52" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">✅ Pluggable Composition (High Reuse)</text>

      <!-- Context Robot -->
      <rect x="460" y="80" width="140" height="70" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
      <text x="530" y="112" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Robot Context</text>
      <text x="530" y="130" fill="#a7f3d0" font-size="9" text-anchor="middle">has-a strategy</text>

      <!-- Pluggable Arrow -->
      <path d="M 600 115 L 660 115" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#cyan-reuse-arrow)"/>

      <!-- Reusable Strategy Box -->
      <rect x="660" y="70" width="130" height="170" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="725" y="95" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">&lt;&lt;Strategy&gt;&gt;</text>

      <rect x="670" y="110" width="110" height="30" rx="3" fill="#1e293b" stroke="#475569"/>
      <text x="725" y="129" fill="#e2e8f0" font-size="9" text-anchor="middle">LaserAttack</text>

      <rect x="670" y="150" width="110" height="30" rx="3" fill="#1e293b" stroke="#475569"/>
      <text x="725" y="169" fill="#e2e8f0" font-size="9" text-anchor="middle">PunchAttack</text>

      <rect x="670" y="190" width="110" height="30" rx="3" fill="#1e293b" stroke="#475569"/>
      <text x="725" y="209" fill="#e2e8f0" font-size="9" text-anchor="middle">MissileAttack</text>

      <defs>
        <marker id="cyan-reuse-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2011-12):</strong> <em>"Explain the concept of reusability in reference to object-oriented programming style. Discuss the rules for reusability."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Memorize Rumbaugh's rules: <em>Keep methods coherent, small, consistent; separate policy from implementation; provide uniform coverage; avoid global state and modes</em>. Differentiate Code Reuse from Design Reuse, and state the GoF principle: <em>Favor object composition over inheritance</em>.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-22",
            "number": "22",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Extensibility",
            "subtitle": "The Open-Closed Principle (OCP), Designing for Future Growth & Polymorphic Hook Architectures",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Architectural Scalability</div>
    <h3>Meaning &amp; Value of Extensibility</h3>
    <p><strong>Extensibility</strong> is a system design principle and a measure of the software's ability to easily accept new functionality, adapt to changing business requirements, or scale without impairing or modifying existing system functions.</p>
    <p>The hallmark of an extensible architecture is that developers can add completely new features simply by <strong>plugging in new subclasses or modules</strong>, without having to edit or recompile pre-existing core source code.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Universal Wall Electrical Outlet</div>
  <p>Consider the standard 3-prong electrical wall socket in your home. When Dyson invents a brand-new futuristic vacuum cleaner or Apple releases a new fast charger, the power company <strong>does not need to dig up your front yard or rewire your house</strong>. The wall socket is <em>closed for modification</em> (the wiring stays untouched) but <em>open for extension</em> (any new electrical appliance adhering to the 3-prong plug standard works immediately)!</p>
</div>

<div class="subtopics-container">
  <h4>The Pillars of Extensible OO Architecture</h4>

  <div class="detail-block">
    <h5>1. The Open-Closed Principle (OCP)</h5>
    <p>Formulated by Bertrand Meyer and popularized by Robert C. Martin (SOLID principles):</p>
    <blockquote>
      <em>"Software entities (classes, modules, functions) should be <strong>open for extension</strong>, but <strong>closed for modification</strong>."</em>
    </blockquote>
    <p>You should be able to extend class behavior without touching the class's existing source code.</p>
  </div>

  <div class="detail-block">
    <h5>2. The Pivotal Role of Polymorphism</h5>
    <p>Polymorphism allows high-level coordination classes to call methods on an abstract interface (e.g., <code>PaymentGateway-&gt;process()</code>). When a new payment provider (e.g., Apple Pay) is introduced, we simply create a new derived class. The coordinator class handles it automatically without a single <code>if-else</code> branch modification!</p>
  </div>

  <div class="detail-block">
    <h5>3. Hook Methods &amp; Plugin Architectures</h5>
    <p>Frameworks provide empty or default <strong>hook methods</strong> inside base classes (Template Method Pattern). Subclasses can selectively override these hooks to inject customized behavior at strategic execution points.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Open-Closed Principle: Pluggable Notification Engine)</span>
    <span class="code-desc">Adding new notification channels with ZERO changes to existing dispatch engine</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;memory&gt;</span>

<span class="c-comment">/* 1. Abstract Interface: Open for extension via subclassing */</span>
<span class="c-keyword">class</span> <span class="c-type">MessageSender</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">virtual</span> ~MessageSender() = <span class="c-keyword">default</span>;
    <span class="c-keyword">virtual void</span> send(<span class="c-keyword">const</span> std::string&amp; recipient, <span class="c-keyword">const</span> std::string&amp; text) = 0;
};

<span class="c-comment">/* 2. Concrete Provider A: Email */</span>
<span class="c-keyword">class</span> <span class="c-type">EmailSender</span> : <span class="c-keyword">public</span> <span class="c-type">MessageSender</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> send(<span class="c-keyword">const</span> std::string&amp; recipient, <span class="c-keyword">const</span> std::string&amp; text) <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[EMAIL] Sending to "</span> &lt;&lt; recipient &lt;&lt; <span class="c-string">": "</span> &lt;&lt; text &lt;&lt; std::endl;
    }
};

<span class="c-comment">/* 3. Concrete Provider B: SMS */</span>
<span class="c-keyword">class</span> <span class="c-type">SmsSender</span> : <span class="c-keyword">public</span> <span class="c-type">MessageSender</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> send(<span class="c-keyword">const</span> std::string&amp; recipient, <span class="c-keyword">const</span> std::string&amp; text) <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[SMS] Texting "</span> &lt;&lt; recipient &lt;&lt; <span class="c-string">": "</span> &lt;&lt; text &lt;&lt; std::endl;
    }
};

<span class="c-comment">/* --- 4. NEW EXTENSION: Added months later without modifying AlertService! --- */</span>
<span class="c-keyword">class</span> <span class="c-type">SlackSender</span> : <span class="c-keyword">public</span> <span class="c-type">MessageSender</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> send(<span class="c-keyword">const</span> std::string&amp; recipient, <span class="c-keyword">const</span> std::string&amp; text) <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[SLACK] Posting to channel #"</span> &lt;&lt; recipient &lt;&lt; <span class="c-string">": "</span> &lt;&lt; text &lt;&lt; std::endl;
    }
};

<span class="c-comment">/* 5. Core Engine: CLOSED FOR MODIFICATION */</span>
<span class="c-keyword">class</span> <span class="c-type">AlertService</span> {
<span class="c-keyword">private:</span>
    std::vector&lt;std::shared_ptr&lt;<span class="c-type">MessageSender</span>&gt;&gt; channels;
<span class="c-keyword">public:</span>
    <span class="c-type">void</span> registerChannel(std::shared_ptr&lt;<span class="c-type">MessageSender</span>&gt; channel) {
        channels.push_back(channel);
    }

    <span class="c-type">void</span> broadcastAlert(<span class="c-keyword">const</span> std::string&amp; target, <span class="c-keyword">const</span> std::string&amp; message) {
        <span class="c-keyword">for</span> (<span class="c-keyword">auto</span>&amp; channel : channels) {
            channel-&gt;send(target, message); <span class="c-comment">/* Polymorphic dynamic dispatch */</span>
        }
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">AlertService</span> alerts;
    alerts.registerChannel(std::make_shared&lt;<span class="c-type">EmailSender</span>&gt;());
    alerts.registerChannel(std::make_shared&lt;<span class="c-type">SmsSender</span>&gt;());
    
    <span class="c-comment">/* Seamlessly plug in brand-new Slack provider! */</span>
    alerts.registerChannel(std::make_shared&lt;<span class="c-type">SlackSender</span>&gt;());

    alerts.broadcastAlert(<span class="c-string">"dev-ops"</span>, <span class="c-string">"Server CPU threshold exceeded 90%!"</span>);
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Open-Closed Principle (OCP) Structure</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Closed Component (Left) -->
      <rect x="50" y="40" width="240" height="190" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
      <rect x="70" y="55" width="200" height="30" rx="4" fill="#1d4ed8"/>
      <text x="170" y="75" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLOSED FOR MODIFICATION</text>
      
      <rect x="70" y="105" width="200" height="50" rx="4" fill="#0f172a" stroke="#60a5fa"/>
      <text x="170" y="128" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">AlertService Engine</text>
      <text x="170" y="145" fill="#cbd5e1" font-size="9" text-anchor="middle">Never recompiled or edited</text>

      <!-- Connection Arrow to Interface -->
      <path d="M 290 130 L 375 130" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#blue-ext-arrow)"/>

      <!-- The Extension Point: Abstract Interface -->
      <rect x="380" y="80" width="160" height="100" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
      <text x="460" y="110" fill="#c084fc" font-size="10" font-weight="bold" text-anchor="middle">&lt;&lt;Interface&gt;&gt;</text>
      <text x="460" y="130" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">MessageSender</text>
      <line x1="395" y1="145" x2="525" y2="145" stroke="#a855f7" stroke-width="1.5"/>
      <text x="460" y="165" fill="#a855f7" font-size="10" text-anchor="middle">+send(msg)</text>

      <!-- Extension Branches to Derived Classes -->
      <path d="M 540 130 L 610 80" stroke="#34d399" stroke-width="2"/>
      <path d="M 540 130 L 610 130" stroke="#34d399" stroke-width="2"/>
      <path d="M 540 130 L 610 180" stroke="#34d399" stroke-width="2"/>

      <!-- Pluggable Implementations (Right) -->
      <rect x="610" y="60" width="180" height="40" rx="4" fill="#065f46" stroke="#34d399"/>
      <text x="700" y="85" fill="#ffffff" font-size="11" text-anchor="middle">EmailSender (Original)</text>

      <rect x="610" y="110" width="180" height="40" rx="4" fill="#065f46" stroke="#34d399"/>
      <text x="700" y="135" fill="#ffffff" font-size="11" text-anchor="middle">SmsSender (Original)</text>

      <rect x="610" y="160" width="180" height="40" rx="4" fill="#047857" stroke="#22c55e" stroke-dasharray="4" stroke-width="2"/>
      <text x="700" y="182" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">SlackSender (New Plugin!)</text>
      <text x="700" y="195" fill="#86efac" font-size="8" text-anchor="middle">Open for Extension</text>

      <defs>
        <marker id="blue-ext-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#60a5fa"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2014-15):</strong> <em>"Explain extensibility with reference to object-oriented programming style. Give a suitable example."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define extensibility as the ease of adding new capabilities without breaking existing software. Quote the <strong>Open-Closed Principle</strong> word-for-word. Explain how polymorphism enables extensibility by allowing new subclasses to be introduced at runtime.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-23",
            "number": "23",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Robustness",
            "subtitle": "Defensive Programming, Invariant Enforcement, Exception Handling & Graceful Degradation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">System Reliability</div>
    <h3>Meaning &amp; Principles of Software Robustness</h3>
    <p>A software component or method is <strong>robust</strong> if it executes reliably and does not crash or terminate abnormally, even when it receives improper parameters, encounters unanticipated user actions, or experiences hardware/network glitches.</p>
    <p>While robustness against internal bugs may sometimes be traded off for raw execution speed, <strong>robustness against external user errors must never be sacrificed</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The ABS Brakes &amp; Airbags in a Car</div>
  <p>If a panicked driver slams the brakes on a sheet of black ice, a fragile car locks its wheels and spins into a ditch. A <strong>robust car equipped with ABS (Anti-lock Braking System)</strong> pulses the brakes automatically, prevents wheel lockup, and maintains steering control. Even when user input is extreme, improper, or erroneous, the robust system absorbs the shock and maintains integrity!</p>
</div>

<div class="subtopics-container">
  <h4>Rumbaugh's 5 Cardinal Rules for Robustness (AKTU Question 3.23)</h4>

  <div class="detail-block">
    <h5>1. Protect Against Errors (Never Crash on Bad Input)</h5>
    <p>Incorrect, malicious, or malformed user input must always be captured at the boundary and reported via user-friendly error messages or exceptions. A software system must never crash or suffer buffer overruns from invalid input.</p>
  </div>

  <div class="detail-block">
    <h5>2. Optimize After the Program Runs</h5>
    <p><em>"Premature optimization is the root of all evil"</em> (Donald Knuth). Build clean, verifiable, robust code first. Profile the system to locate genuine bottlenecks before optimizing.</p>
  </div>

  <div class="detail-block">
    <h5>3. Rigorously Validate External Arguments</h5>
    <p>Every public method exported to external callers must validate all preconditions (checking for null pointers, negative amounts, out-of-bound indexes, and buffer limits) before executing core business logic.</p>
  </div>

  <div class="detail-block">
    <h5>4. Avoid Predefined Fixed Limits</h5>
    <p>Never use hard-coded fixed arrays (e.g., <code>char name[50];</code> or <code>int items[100];</code>) that can overflow when large datasets arrive. Use dynamic data structures (e.g., <code>std::vector</code>, <code>std::string</code>) that scale dynamically.</p>
  </div>

  <div class="detail-block">
    <h5>5. Instrument Code for Debugging &amp; Performance</h5>
    <p>Embed diagnostics, structured audit logs, and assertions (<code>assert</code>) to verify class invariants and internal state health during development and staging.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Robust Class with RAII &amp; Exception Handling)</span>
    <span class="code-desc">Defensive validation, RAII dynamic memory, custom exceptions, and invariants</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdexcept&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;cassert&gt;</span>

<span class="c-comment">/* Custom Exception Class */</span>
<span class="c-keyword">class</span> <span class="c-type">InsufficientFundsException</span> : <span class="c-keyword">public</span> std::runtime_error {
<span class="c-keyword">public:</span>
    InsufficientFundsException(<span class="c-type">double</span> bal, <span class="c-type">double</span> req)
        : std::runtime_error(<span class="c-string">"Withdrawal failed: requested $"</span> + std::to_string(req) +
                             <span class="c-string">", but balance is only $"</span> + std::to_string(bal)) {}
};

<span class="c-keyword">class</span> <span class="c-type">RobustBankAccount</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">int</span> accountNumber;
    <span class="c-type">double</span> balance;
    std::vector&lt;std::string&gt; auditLog; <span class="c-comment">/* Dynamic: No predefined limits! */</span>

    <span class="c-comment">/* Invariant Checker: Class state must always satisfy business rules */</span>
    <span class="c-type">void</span> checkInvariants() <span class="c-keyword">const</span> {
        assert(balance &gt;= 0.0 &amp;&amp; <span class="c-string">"Invariant Broken: Balance cannot be negative!"</span>);
        assert(accountNumber &gt; 0 &amp;&amp; <span class="c-string">"Invariant Broken: Account number must be positive!"</span>);
    }

<span class="c-keyword">public:</span>
    RobustBankAccount(<span class="c-type">int</span> accNo, <span class="c-type">double</span> initialDep) : accountNumber(accNo), balance(initialDep) {
        <span class="c-comment">/* Rule 3: Validate external arguments */</span>
        <span class="c-keyword">if</span> (accNo &lt;= 0 || initialDep &lt; 0.0) {
            <span class="c-keyword">throw</span> std::invalid_argument(<span class="c-string">"Invalid account number or initial deposit"</span>);
        }
        auditLog.push_back(<span class="c-string">"Account created"</span>);
        checkInvariants();
    }

    <span class="c-type">void</span> withdraw(<span class="c-type">double</span> amount) {
        <span class="c-comment">/* Defensive check against invalid input */</span>
        <span class="c-keyword">if</span> (amount &lt;= 0.0) {
            <span class="c-keyword">throw</span> std::invalid_argument(<span class="c-string">"Withdrawal amount must be strictly positive"</span>);
        }
        <span class="c-keyword">if</span> (amount &gt; balance) {
            <span class="c-keyword">throw</span> InsufficientFundsException(balance, amount);
        }

        balance -= amount;
        auditLog.push_back(<span class="c-string">"Withdrew: $"</span> + std::to_string(amount));
        checkInvariants(); <span class="c-comment">/* Verify integrity post-mutation */</span>
    }

    <span class="c-type">double</span> getBalance() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> balance; }
};

<span class="c-type">int</span> main() {
    <span class="c-keyword">try</span> {
        <span class="c-type">RobustBankAccount</span> acc(1001, 500.0);
        std::cout &lt;&lt; <span class="c-string">"Initial Balance: $"</span> &lt;&lt; acc.getBalance() &lt;&lt; std::endl;

        <span class="c-comment">/* Attempting improper transaction */</span>
        std::cout &lt;&lt; <span class="c-string">"Attempting to withdraw $800..."</span> &lt;&lt; std::endl;
        acc.withdraw(800.0);
    } <span class="c-keyword">catch</span> (<span class="c-keyword">const</span> <span class="c-type">InsufficientFundsException</span>&amp; ex) {
        <span class="c-comment">/* Graceful Recovery: System handles error smoothly without crashing */</span>
        std::cerr &lt;&lt; <span class="c-string">"[Safe Recovery] "</span> &lt;&lt; ex.what() &lt;&lt; std::endl;
    } <span class="c-keyword">catch</span> (<span class="c-keyword">const</span> std::exception&amp; ex) {
        std::cerr &lt;&lt; <span class="c-string">"[General Error] "</span> &lt;&lt; ex.what() &lt;&lt; std::endl;
    }

    std::cout &lt;&lt; <span class="c-string">"Program execution continues uninterrupted!"</span> &lt;&lt; std::endl;
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The Multi-Layer Robustness Defensive Shield</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Input Stream -->
      <rect x="30" y="100" width="120" height="60" rx="6" fill="#1e293b" stroke="#64748b"/>
      <text x="90" y="125" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Untrusted</text>
      <text x="90" y="142" fill="#94a3b8" font-size="10" text-anchor="middle">Input Stream</text>

      <path d="M 150 130 L 205 130" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#amber-rob-arrow)"/>

      <!-- Shield 1: Input Validation Gate -->
      <rect x="210" y="60" width="150" height="140" rx="8" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
      <text x="285" y="85" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">1. Validation Gate</text>
      <text x="285" y="110" fill="#fef3c7" font-size="9" text-anchor="middle">• Null checks</text>
      <text x="285" y="128" fill="#fef3c7" font-size="9" text-anchor="middle">• Range limits</text>
      <text x="285" y="146" fill="#fef3c7" font-size="9" text-anchor="middle">• Type sanitization</text>
      <text x="285" y="175" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">Throws Exception if Bad</text>

      <path d="M 360 130 L 415 130" stroke="#34d399" stroke-width="2.5" marker-end="url(#green-rob-arrow)"/>

      <!-- Shield 2: Invariants & Core State -->
      <rect x="420" y="60" width="160" height="140" rx="8" fill="#065f46" stroke="#34d399" stroke-width="2"/>
      <text x="500" y="85" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">2. Core Invariants</text>
      <text x="500" y="110" fill="#a7f3d0" font-size="9" text-anchor="middle">• assert(balance &gt;= 0)</text>
      <text x="500" y="128" fill="#a7f3d0" font-size="9" text-anchor="middle">• Dynamic vector size</text>
      <text x="500" y="146" fill="#a7f3d0" font-size="9" text-anchor="middle">• RAII Resource lock</text>
      <text x="500" y="175" fill="#6ee7b7" font-size="9" font-weight="bold" text-anchor="middle">Guaranteed State Health</text>

      <path d="M 580 130 L 635 130" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#cyan-rob-arrow)"/>

      <!-- Shield 3: Catch & Graceful Degradation -->
      <rect x="640" y="60" width="160" height="140" rx="8" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
      <text x="720" y="85" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">3. Safe Recovery</text>
      <text x="720" y="110" fill="#bae6fd" font-size="9" text-anchor="middle">• Catch blocks</text>
      <text x="720" y="128" fill="#bae6fd" font-size="9" text-anchor="middle">• Diagnostic logging</text>
      <text x="720" y="146" fill="#bae6fd" font-size="9" text-anchor="middle">• Fallback service</text>
      <text x="720" y="175" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Zero System Crashes!</text>

      <defs>
        <marker id="amber-rob-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
        <marker id="green-rob-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
        <marker id="cyan-rob-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2011-12):</strong> <em>"What do you mean by robustness in object-oriented programming style? Explain the various rules for robustness."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Define a robust method as one that never crashes even on bad inputs. Detail Rumbaugh's rules: <em>Protect against errors, optimize after running, validate external arguments, avoid predefined fixed limits, instrument for debugging</em>. Mention exception handling and assertions.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-24",
            "number": "24",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Programming in the Large",
            "subtitle": "Modularization, Package Design, Namespace Management, Visibility & Large-Scale Systems",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Enterprise Software Engineering</div>
    <h3>Meaning of Programming in the Large</h3>
    <p><strong>Programming in the Large</strong> refers to the engineering, architectural, and organizational methodologies required to develop, test, and maintain <strong>massive, multi-million-line software systems</strong> built by multiple distributed engineering teams over several years.</p>
    <p>It stands in sharp contrast to <em>"Programming in the Small"</em> (where a single developer writes algorithms or scripts). In large-scale systems, the primary challenge shifts from writing lines of code to <strong>managing architectural complexity, subsystem boundaries, namespace collisions, and dependency graphs</strong>.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Building a Doghouse vs Building a 100-Story Skyscraper</div>
  <p><strong>Programming in the Small is like building a doghouse:</strong> One carpenter can go to the backyard with wood, a saw, and a box of nails. No formal blueprints or building permits are needed; if a piece is too long, you just saw it off.</p>
  <p><strong>Programming in the Large is constructing a 100-story skyscraper:</strong> You cannot just start hammering. You require civil engineers, architects, zoning permits, stress simulations, crane schedules, and clear structural interfaces between plumbing, HVAC, and electrical systems. Without rigid modularization, the skyscraper collapses under its own weight!</p>
</div>

<div class="subtopics-container">
  <h4>Key Architectural Mechanisms for Large-Scale Software</h4>

  <div class="detail-block">
    <h5>1. Modularity &amp; Package Design</h5>
    <p>Large systems are partitioned into hierarchical <strong>Packages or Modules</strong>. Packages group closely related classes into cohesive units. High-quality packaging adheres to the <em>Acyclic Dependencies Principle (ADP)</em>: the dependency graph between packages must contain no circular loops.</p>
  </div>

  <div class="detail-block">
    <h5>2. Namespaces &amp; Visibility Control</h5>
    <p>When hundreds of developers commit code, naming conflicts are inevitable (e.g., team A creates <code>Logger</code> and team B creates <code>Logger</code>). Namespaces (C++ <code>namespace</code>, Java <code>package</code>) partition global symbol tables, preventing name collisions.</p>
  </div>

  <div class="detail-block">
    <h5>3. Managing Subsystem Dependencies &amp; API Contracts</h5>
    <p>Subsystems must communicate strictly through published <strong>API contracts (Interfaces)</strong>. Implementation details inside a subsystem remain completely hidden, allowing teams to refactor internal classes independently without breaking other subsystems.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Enterprise Modular Namespaces &amp; API Packaging)</span>
    <span class="code-desc">Organizing large-scale software into decoupled namespaces and service boundaries</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;memory&gt;</span>

<span class="c-comment">/* ======================================================= */</span>
<span class="c-comment">/* SUBSYSTEM 1: Enterprise Payment Gateway Namespace      */</span>
<span class="c-comment">/* ======================================================= */</span>
<span class="c-keyword">namespace</span> Enterprise::Finance::Payment {
    <span class="c-comment">/* Public Interface Contract */</span>
    <span class="c-keyword">class</span> <span class="c-type">IPaymentService</span> {
    <span class="c-keyword">public:</span>
        <span class="c-keyword">virtual</span> ~IPaymentService() = <span class="c-keyword">default</span>;
        <span class="c-keyword">virtual bool</span> charge(<span class="c-type">int</span> customerId, <span class="c-type">double</span> amount) = 0;
    };

    <span class="c-comment">/* Subsystem Implementation */</span>
    <span class="c-keyword">class</span> <span class="c-type">CreditCardService</span> : <span class="c-keyword">public</span> <span class="c-type">IPaymentService</span> {
    <span class="c-keyword">public:</span>
        <span class="c-keyword">bool</span> charge(<span class="c-type">int</span> customerId, <span class="c-type">double</span> amount) <span class="c-keyword">override</span> {
            std::cout &lt;&lt; <span class="c-string">"[Finance::Payment] Debited $"</span> &lt;&lt; amount 
                      &lt;&lt; <span class="c-string">" from Customer #"</span> &lt;&lt; customerId &lt;&lt; std::endl;
            <span class="c-keyword">return true</span>;
        }
    };
}

<span class="c-comment">/* ======================================================= */</span>
<span class="c-comment">/* SUBSYSTEM 2: Enterprise Order Fulfillment Namespace     */</span>
<span class="c-comment">/* ======================================================= */</span>
<span class="c-keyword">namespace</span> Enterprise::Fulfillment::OrderProcessing {
    <span class="c-keyword">using</span> Enterprise::Finance::Payment::IPaymentService;

    <span class="c-keyword">class</span> <span class="c-type">OrderCoordinator</span> {
    <span class="c-keyword">private:</span>
        std::shared_ptr&lt;<span class="c-type">IPaymentService</span>&gt; paymentGateway; <span class="c-comment">/* Depends only on contract */</span>

    <span class="c-keyword">public:</span>
        OrderCoordinator(std::shared_ptr&lt;<span class="c-type">IPaymentService</span>&gt; gateway)
            : paymentGateway(gateway) {}

        <span class="c-type">void</span> completeOrder(<span class="c-type">int</span> orderId, <span class="c-type">int</span> customerId, <span class="c-type">double</span> total) {
            std::cout &lt;&lt; <span class="c-string">"[Fulfillment::Order] Processing Order #"</span> &lt;&lt; orderId &lt;&lt; std::endl;
            <span class="c-type">bool</span> success = paymentGateway-&gt;charge(customerId, total);
            <span class="c-keyword">if</span> (success) {
                std::cout &lt;&lt; <span class="c-string">"[Fulfillment::Order] Order fulfilled and dispatched!"</span> &lt;&lt; std::endl;
            }
        }
    };
}

<span class="c-type">int</span> main() {
    <span class="c-comment">/* Dependency Injection across subsystem namespaces */</span>
    <span class="c-keyword">auto</span> paymentSys = std::make_shared&lt;<span class="c-type">Enterprise::Finance::Payment::CreditCardService</span>&gt;();
    <span class="c-type">Enterprise::Fulfillment::OrderProcessing::OrderCoordinator</span> coordinator(paymentSys);

    coordinator.completeOrder(9001, 42, 129.99);
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Layered Packaging &amp; Subsystem Modularity</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Tier 1: Presentation Layer -->
      <rect x="50" y="30" width="740" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="90" y="62" fill="#38bdf8" font-size="12" font-weight="bold">UI &amp; API Layer</text>
      <rect x="220" y="42" width="160" height="30" rx="4" fill="#0284c7"/>
      <text x="300" y="62" fill="#ffffff" font-size="10" text-anchor="middle">REST Controllers</text>
      <rect x="420" y="42" width="160" height="30" rx="4" fill="#0284c7"/>
      <text x="500" y="62" fill="#ffffff" font-size="10" text-anchor="middle">GraphQL Endpoints</text>

      <!-- Dependency Arrow -->
      <path d="M 420 85 L 420 110" stroke="#60a5fa" stroke-width="2" marker-end="url(#blue-large-arrow)"/>

      <!-- Tier 2: Business Logic Subsystems -->
      <rect x="50" y="115" width="740" height="65" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="90" y="152" fill="#c084fc" font-size="12" font-weight="bold">Domain Logic</text>
      
      <rect x="200" y="127" width="180" height="40" rx="4" fill="#6d28d9"/>
      <text x="290" y="147" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Order Fulfillment Package</text>
      <text x="290" y="160" fill="#e9d5ff" font-size="8" text-anchor="middle">Enterprise::Fulfillment</text>

      <rect x="440" y="127" width="180" height="40" rx="4" fill="#6d28d9"/>
      <text x="530" y="147" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Billing &amp; Payment Package</text>
      <text x="530" y="160" fill="#e9d5ff" font-size="8" text-anchor="middle">Enterprise::Finance</text>

      <!-- Dependency Arrow -->
      <path d="M 420 180 L 420 205" stroke="#60a5fa" stroke-width="2" marker-end="url(#blue-large-arrow)"/>

      <!-- Tier 3: Infrastructure / Persistence -->
      <rect x="50" y="210" width="740" height="50" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
      <text x="90" y="240" fill="#34d399" font-size="12" font-weight="bold">Infrastructure</text>
      <rect x="230" y="220" width="150" height="30" rx="4" fill="#065f46"/>
      <text x="305" y="239" fill="#ffffff" font-size="10" text-anchor="middle">SQL Database Adapter</text>
      <rect x="430" y="220" width="150" height="30" rx="4" fill="#065f46"/>
      <text x="505" y="239" fill="#ffffff" font-size="10" text-anchor="middle">Redis Cache Gateway</text>

      <defs>
        <marker id="blue-large-arrow" viewBox="0 0 10 10" refX="5" refY="6" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 1 0 L 5 8 L 9 0 z" fill="#60a5fa"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2013-14, 2016-17):</strong> <em>"What do you understand by 'Programming in the Large'? What are the major challenges and solutions?"</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Distinguish Programming in the Large (multi-team, large scale) from Programming in the Small (single developer, algorithms). List key solutions: <strong>Packages/Modules</strong>, <strong>Namespaces</strong> to prevent collision, <strong>Acyclic Dependency Principle</strong>, and <strong>Interface Contracts</strong>.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-25",
            "number": "25",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Procedural vs Object-Oriented Programming",
            "subtitle": "Algorithm-Centric vs Data-Centric Paradigms: Comprehensive 10-Point Comparison Matrix",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Paradigm Shift</div>
    <h3>The Fundamental Architectural Divide</h3>
    <p>The transition from <strong>Procedural Programming (POP)</strong> to <strong>Object-Oriented Programming (OOP)</strong> represents one of the most significant paradigm shifts in computer science history.</p>
    <p>While Procedural programming organizes code around <em>algorithms, functions, and top-down step-by-step procedures</em> acting upon passive shared data, Object-Oriented programming organizes code around <em>autonomous real-world objects</em> encapsulating their own private state and behavior.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Cooking a Recipe vs The Restaurant Ecosystem</div>
  <p><strong>Procedural Programming is like cooking from a single recipe card:</strong> Step 1: Chop onions; Step 2: Heat olive oil; Step 3: Fry garlic; Step 4: Stir soup. If step 2 burns the pot, the whole sequence crashes. The recipe is a list of sequential instructions executed on passive food ingredients.</p>
  <p><strong>Object-Oriented Programming is like a bustling restaurant:</strong> You have autonomous, specialized agents &mdash; the <code>Customer</code>, the <code>Waiter</code>, the <code>Chef</code>, and the <code>Cashier</code>. The customer does not tell the chef how to hold the knife; the customer sends an <code>orderFood()</code> message to the waiter, who forwards it to the chef. Each entity manages its own private responsibilities!</p>
</div>

<div class="comparison-table-wrapper">
  <h4>Comprehensive 10-Point Comparison Matrix: POP vs OOP</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Comparison Dimension</th>
        <th>Procedural Programming (POP)</th>
        <th>Object-Oriented Programming (OOP)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Core Philosophy</strong></td>
        <td><strong>Algorithm-centric:</strong> Focuses on <em>HOW</em> tasks are done step-by-step</td>
        <td><strong>Data-centric:</strong> Focuses on <em>WHO</em> owns the data and responsibilities</td>
      </tr>
      <tr>
        <td><strong>2. Program Structure</strong></td>
        <td>Program is divided into functions, subroutines, and procedures</td>
        <td>Program is partitioned into classes and collaborating objects</td>
      </tr>
      <tr>
        <td><strong>3. Data Security &amp; Hiding</strong></td>
        <td><strong>Low:</strong> Data moves freely; global data can be altered by any function</td>
        <td><strong>High:</strong> Data is encapsulated inside objects using access modifiers</td>
      </tr>
      <tr>
        <td><strong>4. Design Approach</strong></td>
        <td><strong>Top-Down:</strong> Main function decomposes into smaller subroutines</td>
        <td><strong>Bottom-Up:</strong> Primitive classes are composed into complex systems</td>
      </tr>
      <tr>
        <td><strong>5. Code Reusability</strong></td>
        <td>Limited to function calls; sharing requires copying source code</td>
        <td><strong>Extensive:</strong> Achieved through Inheritance, Polymorphism &amp; Generics</td>
      </tr>
      <tr>
        <td><strong>6. Modifiability &amp; Ripple Effects</strong></td>
        <td>Changing a data structure breaks all functions accessing it</td>
        <td>Internal class changes do not affect external client code</td>
      </tr>
      <tr>
        <td><strong>7. Overloading &amp; Polymorphism</strong></td>
        <td>Not supported; function names must be globally unique</td>
        <td>Fully supported (Method overloading, operator overloading, dynamic dispatch)</td>
      </tr>
      <tr>
        <td><strong>8. Real-World Mapping</strong></td>
        <td>Unnatural; forces real-world problems into sequential function steps</td>
        <td><strong>Natural:</strong> Models domain entities (Customer, Account, Invoice) directly</td>
      </tr>
      <tr>
        <td><strong>9. Ideal Use Cases</strong></td>
        <td>Compilers, OS kernels, device drivers, pure mathematical computation</td>
        <td>Enterprise business apps, GUIs, simulations, game development, microservices</td>
      </tr>
      <tr>
        <td><strong>10. Representative Languages</strong></td>
        <td>C, Pascal, Fortran, Basic, COBOL</td>
        <td>C++, Java, C#, Python, Ruby, Swift</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">Side-by-Side: Procedural C vs Object-Oriented C++</span>
    <span class="code-desc">Contrasting fragile procedural global data with robust encapsulated objects</span>
  </div>
  <pre class="code-block"><code><span class="c-comment">/* ========================================================== */</span>
<span class="c-comment">/* APPROACH A: PROCEDURAL C (Global state, loose functions)  */</span>
<span class="c-comment">/* ========================================================== */</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdio.h&gt;</span>

<span class="c-type">double</span> g_balance = 500.0; <span class="c-comment">/* DANGEROUS: Global data exposed to entire program! */</span>

<span class="c-type">void</span> depositMoney(<span class="c-type">double</span> amt) {
    g_balance += amt; <span class="c-comment">/* Any rogue subroutine can corrupt this */</span>
}

<span class="c-comment">/* ========================================================== */</span>
<span class="c-comment">/* APPROACH B: OBJECT-ORIENTED C++ (Encapsulated state)       */</span>
<span class="c-comment">/* ========================================================== */</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">SecureAccount</span> {
<span class="c-keyword">private:</span>
    <span class="c-type">double</span> balance; <span class="c-comment">/* PROTECTED: Invisible and inaccessible to outside world */</span>

<span class="c-keyword">public:</span>
    SecureAccount(<span class="c-type">double</span> initial) : balance(initial &gt; 0 ? initial : 0) {}

    <span class="c-type">void</span> deposit(<span class="c-type">double</span> amount) {
        <span class="c-keyword">if</span> (amount &gt; 0) {
            balance += amount; <span class="c-comment">/* Validated update within class boundary */</span>
        }
    }

    <span class="c-type">double</span> getBalance() <span class="c-keyword">const</span> { <span class="c-keyword">return</span> balance; }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">/* In C: g_balance = -999999; // Silent data corruption possible! */</span>

    <span class="c-comment">/* In C++: Airtight encapsulation */</span>
    <span class="c-type">SecureAccount</span> myAcc(500.0);
    myAcc.deposit(250.0);
    <span class="c-comment">/* myAcc.balance = -999; // ❌ COMPILE-TIME ERROR: 'balance' is private! */</span>
    
    std::cout &lt;&lt; <span class="c-string">"OO Account Balance: $"</span> &lt;&lt; myAcc.getBalance() &lt;&lt; std::endl;
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Procedural (POP) vs Object-Oriented (OOP) Paradigm</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Left: Procedural Paradigm -->
      <rect x="40" y="25" width="360" height="230" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="220" y="52" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">Procedural Paradigm (POP)</text>
      
      <!-- Exposed Global Data in center -->
      <circle cx="220" cy="140" r="40" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
      <text x="220" y="137" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">SHARED</text>
      <text x="220" y="152" fill="#fef3c7" font-size="10" text-anchor="middle">GLOBAL DATA</text>

      <!-- Functions modifying global data -->
      <rect x="60" y="80" width="85" height="35" rx="4" fill="#334155"/>
      <text x="102" y="102" fill="#e2e8f0" font-size="10" text-anchor="middle">Function A()</text>

      <rect x="295" y="80" width="85" height="35" rx="4" fill="#334155"/>
      <text x="337" y="102" fill="#e2e8f0" font-size="10" text-anchor="middle">Function B()</text>

      <rect x="175" y="205" width="90" height="35" rx="4" fill="#334155"/>
      <text x="220" y="227" fill="#e2e8f0" font-size="10" text-anchor="middle">Function C()</text>

      <!-- Access arrows to global data -->
      <path d="M 145 105 L 185 125" stroke="#f59e0b" stroke-width="1.5"/>
      <path d="M 295 105 L 255 125" stroke="#f59e0b" stroke-width="1.5"/>
      <path d="M 220 205 L 220 180" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="220" y="250" fill="#94a3b8" font-size="9" text-anchor="middle">Data is passive, exposed &amp; unshielded</text>

      <!-- Right: Object-Oriented Paradigm -->
      <rect x="440" y="25" width="360" height="230" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="620" y="52" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Object-Oriented Paradigm (OOP)</text>

      <!-- Autonomous Object 1 -->
      <rect x="460" y="85" width="140" height="90" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <rect x="470" y="95" width="120" height="30" rx="4" fill="#0369a1"/>
      <text x="530" y="115" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Object 1: Customer</text>
      <text x="530" y="145" fill="#38bdf8" font-size="9" text-anchor="middle">Methods (Public)</text>
      <text x="530" y="162" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">[Data: Private]</text>

      <!-- Autonomous Object 2 -->
      <rect x="640" y="85" width="140" height="90" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
      <rect x="650" y="95" width="120" height="30" rx="4" fill="#0369a1"/>
      <text x="710" y="115" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Object 2: Account</text>
      <text x="710" y="145" fill="#38bdf8" font-size="9" text-anchor="middle">Methods (Public)</text>
      <text x="710" y="162" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">[Data: Private]</text>

      <!-- Message Passing vector -->
      <path d="M 600 120 L 640 120" stroke="#a855f7" stroke-width="2.5" marker-end="url(#purple-pop-arrow)"/>
      <path d="M 640 145 L 600 145" stroke="#a855f7" stroke-width="2.5" marker-end="url(#purple-pop-arrow-rev)"/>
      <text x="620" y="112" fill="#c084fc" font-size="8" text-anchor="middle">Message</text>
      <text x="620" y="160" fill="#c084fc" font-size="8" text-anchor="middle">Response</text>

      <text x="620" y="220" fill="#e2e8f0" font-size="10" text-anchor="middle">Autonomous Encapsulated Entities</text>
      <text x="620" y="240" fill="#34d399" font-size="9" text-anchor="middle">Data is bundled with methods; zero global leaks</text>

      <defs>
        <marker id="purple-pop-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
        <marker id="purple-pop-arrow-rev" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#a855f7"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11, 2012-13, 2015-16):</strong> <em>"Differentiate between Procedural and Object-Oriented Programming with suitable examples."</em> [10 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Strategy:</strong> Always reproduce the 10-point comparison table above. Highlight the contrast between <strong>Algorithm-Centric (Top-down)</strong> and <strong>Data-Centric (Bottom-up)</strong>, and demonstrate how global data leaks in C are resolved via class encapsulation in C++.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-26",
            "number": "26",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Object-Oriented Language Features",
            "subtitle": "Dynamic Binding, Polymorphism, Generics, Memory Management & C++ vs Java Comparison",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Language Mechanics</div>
    <h3>Core Capabilities of Modern OO Languages</h3>
    <p>Object-oriented programming languages provide native syntactic features that transform conceptual designs directly into executable reality. The defining pillars of an OO language include <strong>Dynamic Binding (Late Binding), Subtype Polymorphism, Parametric Polymorphism (Generics/Templates), and Managed Memory</strong>.</p>
    <p>These features decouple high-level architectural policies from concrete implementation types, enabling runtime flexibility and type-safe reusability.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Universal Remote Control</div>
  <p>Pressing the <strong>"Power" button</strong> on a universal remote control sends the exact same signal. If the target receiver is a Samsung TV, it illuminates the OLED screen; if the receiver is a Yamaha Soundbar, it wakes up the audio amplifiers; if the receiver is a motorized projector, it lowers the ceiling screen.</p>
  <p>The remote does not need a different button for every device brand. <strong>That is Polymorphism and Dynamic Binding:</strong> One uniform interface message (<code>powerOn()</code>), dynamically dispatched to invoke the specific behavior of the target receiver at runtime!</p>
</div>

<div class="subtopics-container">
  <h4>Key Advanced Features of OO Languages</h4>

  <div class="detail-block">
    <h5>1. Dynamic Binding (Late Binding) vs Static Binding</h5>
    <ul>
      <li><strong>Static (Early) Binding:</strong> Method address is resolved by the compiler and linker at compile time (fast, default in C++ for non-virtual methods).</li>
      <li><strong>Dynamic (Late) Binding:</strong> Method address is resolved at runtime based on the actual type of the instantiated object using a Virtual Table (<code>vtable</code>) lookup.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Polymorphism Varieties</h5>
    <ul>
      <li><strong>Compile-Time Polymorphism:</strong> Function overloading and operator overloading resolved at compile time.</li>
      <li><strong>Run-Time Polymorphism:</strong> Subtype polymorphism via virtual method overriding.</li>
      <li><strong>Parametric Polymorphism:</strong> Generics (Java/C#) and Templates (C++) allowing classes and algorithms to operate across any type safely.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>3. Memory Management: Automatic GC vs Deterministic RAII</h5>
    <ul>
      <li><strong>Automatic Garbage Collection (Java, C#, Python):</strong> A background runtime thread identifies unreachable objects and reclaims heap memory automatically. Eliminates dangling pointers, but introduces unpredictable GC pause times.</li>
      <li><strong>Deterministic RAII (C++):</strong> Resource Acquisition Is Initialization. Objects manage their own resources via constructors and destructors. Memory is reclaimed deterministically the exact microsecond an object leaves scope (via smart pointers like <code>std::unique_ptr</code>).</li>
    </ul>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Comparison of Two Leading OO Languages: C++ vs Java (AKTU Question 3.22)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Feature / Dimension</th>
        <th>C++</th>
        <th>Java</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Platform Independence</strong></td>
        <td>Platform dependent; compiled to native machine binary</td>
        <td><strong>Platform independent;</strong> compiled to bytecode executed by JVM</td>
      </tr>
      <tr>
        <td><strong>Compilation Model</strong></td>
        <td>Purely compiled (ahead-of-time)</td>
        <td>Compiled (to bytecode) + Interpreted / JIT compiled</td>
      </tr>
      <tr>
        <td><strong>Memory Management</strong></td>
        <td>Manual or deterministic RAII (<code>new</code> / <code>delete</code> / smart pointers)</td>
        <td><strong>Automatic Garbage Collection (GC)</strong></td>
      </tr>
      <tr>
        <td><strong>Multiple Inheritance</strong></td>
        <td>Directly supported for classes (with virtual base classes)</td>
        <td>Not supported for classes; achieved via multiple <code>interfaces</code></td>
      </tr>
      <tr>
        <td><strong>Pointers &amp; Low-Level Memory</strong></td>
        <td>Direct pointer arithmetic and address manipulation</td>
        <td>No raw pointers; all objects manipulated via references</td>
      </tr>
      <tr>
        <td><strong>Virtual Methods by Default</strong></td>
        <td>No; methods are non-virtual by default (requires <code>virtual</code>)</td>
        <td><strong>Yes;</strong> all non-static, non-final methods are virtual by default</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Dynamic Binding &amp; Generic Templates)</span>
    <span class="code-desc">Demonstrating virtual dynamic dispatch and type-safe generic templates</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;vector&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;memory&gt;</span>

<span class="c-comment">/* Feature 1: Parametric Polymorphism (Templates / Generics) */</span>
<span class="c-keyword">template</span> &lt;<span class="c-keyword">typename</span> <span class="c-type">T</span>&gt;
<span class="c-type">void</span> printContainerSummary(<span class="c-keyword">const</span> std::vector&lt;<span class="c-type">T</span>&gt;&amp; vec) {
    std::cout &lt;&lt; <span class="c-string">"Container holds "</span> &lt;&lt; vec.size() &lt;&lt; <span class="c-string">" elements."</span> &lt;&lt; std::endl;
}

<span class="c-comment">/* Feature 2: Subtype Polymorphism &amp; Dynamic Binding */</span>
<span class="c-keyword">class</span> <span class="c-type">AudioDevice</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">virtual</span> ~AudioDevice() = <span class="c-keyword">default</span>;
    <span class="c-comment">/* Pure virtual function: enforces dynamic binding in subclasses */</span>
    <span class="c-keyword">virtual void</span> playSound() <span class="c-keyword">const</span> = 0;
};

<span class="c-keyword">class</span> <span class="c-type">Headphones</span> : <span class="c-keyword">public</span> <span class="c-type">AudioDevice</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> playSound() <span class="c-keyword">const override</span> {
        std::cout &lt;&lt; <span class="c-string">"Playing spatial audio through Headphones 🎧"</span> &lt;&lt; std::endl;
    }
};

<span class="c-keyword">class</span> <span class="c-type">Loudspeaker</span> : <span class="c-keyword">public</span> <span class="c-type">AudioDevice</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">void</span> playSound() <span class="c-keyword">const override</span> {
        std::cout &lt;&lt; <span class="c-string">"Blasting high-bass audio through Loudspeakers 🔊"</span> &lt;&lt; std::endl;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-comment">/* Polymorphic collection of devices managed via RAII smart pointers */</span>
    std::vector&lt;std::unique_ptr&lt;<span class="c-type">AudioDevice</span>&gt;&gt; soundSystem;
    soundSystem.push_back(std::make_unique&lt;<span class="c-type">Headphones</span>&gt;());
    soundSystem.push_back(std::make_unique&lt;<span class="c-type">Loudspeaker</span>&gt;());

    printContainerSummary(soundSystem);

    <span class="c-comment">/* Dynamic Late Binding: Calls correct derived method at runtime */</span>
    <span class="c-keyword">for</span> (<span class="c-keyword">const auto</span>&amp; dev : soundSystem) {
        dev-&gt;playSound(); <span class="c-comment">/* Dispatched via vtable pointer */</span>
    }

    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Dynamic Binding via VTable Pointer Indirection</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Base Pointer -->
      <rect x="50" y="90" width="160" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="130" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Base Pointer</text>
      <text x="130" y="133" fill="#38bdf8" font-size="10" text-anchor="middle">AudioDevice* dev</text>

      <!-- Arrow to Object -->
      <path d="M 210 120 L 285 120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#cyan-lang-arrow)"/>

      <!-- Actual Instantiated Object (Headphones) -->
      <rect x="290" y="65" width="190" height="110" rx="8" fill="#0f172a" stroke="#60a5fa" stroke-width="2"/>
      <text x="385" y="90" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">Headphones Instance</text>

      <rect x="305" y="105" width="160" height="30" rx="4" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="385" y="125" fill="#c7d2fe" font-size="10" font-weight="bold" text-anchor="middle">vptr (8 Bytes)</text>

      <rect x="305" y="140" width="160" height="25" rx="4" fill="#334155"/>
      <text x="385" y="157" fill="#cbd5e1" font-size="9" text-anchor="middle">internal fields...</text>

      <!-- Arrow to VTable -->
      <path d="M 465 120 L 545 120" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#amber-lang-arrow)"/>
      <text x="505" y="110" fill="#fbbf24" font-size="9" text-anchor="middle">vptr</text>

      <!-- VTable Box -->
      <rect x="550" y="60" width="240" height="120" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <text x="670" y="85" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Headphones VTable</text>

      <rect x="565" y="100" width="210" height="30" rx="4" fill="#312e81"/>
      <text x="670" y="120" fill="#c7d2fe" font-size="9" text-anchor="middle">slot[0]: &amp;Headphones::~Headphones</text>

      <rect x="565" y="135" width="210" height="35" rx="4" fill="#065f46" stroke="#34d399"/>
      <text x="670" y="155" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">slot[1]: &amp;Headphones::playSound</text>

      <text x="420" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">Dynamic Binding executes method corresponding to exact runtime object type</text>

      <defs>
        <marker id="cyan-lang-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
        </marker>
        <marker id="amber-lang-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2010-11):</strong> <em>"Describe the various features of object-oriented languages. Also compare any two object-oriented languages."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Describe Encapsulation, Polymorphism (compile-time vs runtime), Inheritance, and Dynamic Binding. Reproduce the <strong>C++ vs Java comparison table</strong> (platform independence, compiled vs interpreted/bytecode, manual vs garbage-collected memory, multiple inheritance).
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-27",
            "number": "27",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Abstraction",
            "subtitle": "Selective Focus, Complexity Suppression, Data vs Process Abstraction & Abstract Base Classes",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational Pillar</div>
    <h3>Meaning &amp; Definition of Abstraction</h3>
    <p><strong>Abstraction</strong> is the selective examination of certain aspects of a problem. It is the fundamental mental and software modeling mechanism of <strong>focusing on essential, relevant details while intentionally suppressing and ignoring irrelevant, accidental complexities</strong>.</p>
    <p>Abstraction is always goal-oriented: what is essential for one purpose may be completely trivial for another. By exposing only what a component <em>does</em> while hiding <em>how it does it</em>, abstraction manages intellectual complexity.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: Driving a Modern Automobile</div>
  <p>To drive a car, you sit behind the steering wheel and interact with three simple controls: the <strong>steering wheel</strong>, the <strong>accelerator pedal</strong>, and the <strong>brake pedal</strong>. This is the <em>driving abstraction</em>.</p>
  <p>You do not need to understand valve timing, piston compression ratios, fuel-injector milliseconds, or CAN bus electrical voltages. If drivers had to manage fuel injection manually, 99% of people could never drive. <strong>Abstraction creates a simplified mental interface over immense mechanical complexity!</strong></p>
</div>

<div class="subtopics-container">
  <h4>Types &amp; Levels of Abstraction</h4>

  <div class="detail-block">
    <h5>1. Data Abstraction vs Process (Control) Abstraction</h5>
    <ul>
      <li><strong>Data Abstraction:</strong> Creating Abstract Data Types (ADTs) where the internal storage representation is concealed behind clean behavioral methods (e.g., a <code>Stack</code> provides <code>push()</code> and <code>pop()</code>; whether it is backed by an array, linked list, or memory buffer is hidden).</li>
      <li><strong>Process / Control Abstraction:</strong> Hiding intricate algorithmic steps behind high-level declarative function calls (e.g., calling <code>database.connect()</code> hides socket handshakes, TLS certificates, and IP routing).</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Abstract Base Classes (ABC) &amp; Pure Virtual Interfaces</h5>
    <p>In C++, an abstract class contains at least one <strong>pure virtual function</strong> (<code>virtual void method() = 0;</code>). An abstract class cannot be instantiated directly; it serves as a pure architectural blueprint that obligates concrete derived subclasses to implement the required interface.</p>
  </div>

  <div class="detail-block">
    <h5>3. Levels of Abstraction in System Architecture</h5>
    <p>Systems are designed in concentric abstraction layers: <em>Domain/Business Level</em> &rarr; <em>Subsystem/Service Level</em> &rarr; <em>Class Interface Level</em> &rarr; <em>Hardware/OS Layer</em>. Each layer relies only on the layer directly beneath it.</p>
  </div>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Abstract Base Class &amp; Pure Virtual Interface)</span>
    <span class="code-desc">Clean payment gateway abstraction hiding vendor API complexity</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;memory&gt;</span>

<span class="c-comment">/* Abstract Base Class: Defines WHAT payment processing does, not HOW */</span>
<span class="c-keyword">class</span> <span class="c-type">PaymentProcessor</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">virtual</span> ~PaymentProcessor() = <span class="c-keyword">default</span>;

    <span class="c-comment">/* Pure Virtual Function: Defines interface contract */</span>
    <span class="c-keyword">virtual bool</span> processTransaction(<span class="c-type">double</span> amount) = 0;
};

<span class="c-comment">/* Concrete Implementation 1: Hides Stripe REST API complexity */</span>
<span class="c-keyword">class</span> <span class="c-type">StripeProcessor</span> : <span class="c-keyword">public</span> <span class="c-type">PaymentProcessor</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">bool</span> processTransaction(<span class="c-type">double</span> amount) <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[Stripe] Establishing HTTPS TLSv1.3 connection..."</span> &lt;&lt; std::endl;
        std::cout &lt;&lt; <span class="c-string">"[Stripe] Charged $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">" via Credit Card API."</span> &lt;&lt; std::endl;
        <span class="c-keyword">return true</span>;
    }
};

<span class="c-comment">/* Concrete Implementation 2: Hides Cryptocurrency Blockchain complexity */</span>
<span class="c-keyword">class</span> <span class="c-type">CryptoProcessor</span> : <span class="c-keyword">public</span> <span class="c-type">PaymentProcessor</span> {
<span class="c-keyword">public:</span>
    <span class="c-keyword">bool</span> processTransaction(<span class="c-type">double</span> amount) <span class="c-keyword">override</span> {
        std::cout &lt;&lt; <span class="c-string">"[Crypto] Broadcasting signed transaction to Mempool..."</span> &lt;&lt; std::endl;
        std::cout &lt;&lt; <span class="c-string">"[Crypto] Transferred $"</span> &lt;&lt; amount &lt;&lt; <span class="c-string">" equivalent in Bitcoin."</span> &lt;&lt; std::endl;
        <span class="c-keyword">return true</span>;
    }
};

<span class="c-comment">/* Client Application: Interacts STRICTLY with the high-level Abstraction */</span>
<span class="c-type">void</span> checkoutShoppingCart(<span class="c-type">PaymentProcessor</span>&amp; gateway, <span class="c-type">double</span> total) {
    std::cout &lt;&lt; <span class="c-string">"=== CHECKOUT INITIATED ==="</span> &lt;&lt; std::endl;
    <span class="c-type">bool</span> success = gateway.processTransaction(total);
    <span class="c-keyword">if</span> (success) {
        std::cout &lt;&lt; <span class="c-string">"Purchase Confirmed! Receipt issued.\\n"</span> &lt;&lt; std::endl;
    }
}

<span class="c-type">int</span> main() {
    <span class="c-type">StripeProcessor</span> stripe;
    <span class="c-type">CryptoProcessor</span> crypto;

    <span class="c-comment">/* Client checkout handles both uniformly through the abstraction */</span>
    checkoutShoppingCart(stripe, 99.50);
    checkoutShoppingCart(crypto, 250.00);

    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: Concentric Onion Layers of Abstraction</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Outer Ring: Client / User Domain -->
      <circle cx="420" cy="130" r="115" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="420" y="38" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Level 1: Client Application (Simple Verbs: checkout(), deposit())</text>

      <!-- Middle Ring: Clean Abstract Interface -->
      <circle cx="420" cy="130" r="75" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
      <text x="420" y="78" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Level 2: Abstract Interface</text>
      <text x="420" y="93" fill="#e9d5ff" font-size="9" text-anchor="middle">(PaymentProcessor)</text>

      <!-- Inner Core: Complex Implementation Details -->
      <circle cx="420" cy="130" r="35" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="420" y="128" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Level 3: Core</text>
      <text x="420" y="140" fill="#fca5a5" font-size="8" text-anchor="middle">Hidden Detail</text>

      <!-- Annotations Left and Right -->
      <rect x="50" y="80" width="170" height="90" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="135" y="105" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">What Client Sees</text>
      <text x="135" y="125" fill="#e2e8f0" font-size="9" text-anchor="middle">• Simple pure interface</text>
      <text x="135" y="142" fill="#e2e8f0" font-size="9" text-anchor="middle">• Zero internal state</text>
      <text x="135" y="159" fill="#34d399" font-size="9" text-anchor="middle">• Minimal cognitive load</text>

      <rect x="620" y="80" width="170" height="90" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="705" y="105" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">What Is Suppressed</text>
      <text x="705" y="125" fill="#e2e8f0" font-size="9" text-anchor="middle">• TLS handshake crypto</text>
      <text x="705" y="142" fill="#e2e8f0" font-size="9" text-anchor="middle">• Blockchain hashing</text>
      <text x="705" y="159" fill="#e2e8f0" font-size="9" text-anchor="middle">• Database SQL queries</text>

      <text x="420" y="260" fill="#94a3b8" font-size="10" text-anchor="middle">Abstraction suppresses irrelevant details to expose only essential operations</text>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2011-12, 2015-16):</strong> <em>"Define Abstraction. Explain its significance and discuss data abstraction vs process abstraction."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> State Rumbaugh's exact definition: <em>"Abstraction is the selective examination of certain aspects of a problem, isolating essential features and suppressing unimportant ones."</em> Differentiate Data Abstraction (ADTs like Stack/Queue) from Process Abstraction. Give the car driving analogy.
  </div>
</div>
"""
        },
        {
            "id": "u3-sec-28",
            "number": "28",
            "part": "Part 3 — OO Methodologies & Principles",
            "title": "Encapsulation",
            "subtitle": "Information Hiding, Access Specifiers, Class Invariants & Deep Comparison: Abstraction vs Encapsulation",
            "content": """
<div class="topic-grid">
  <div class="card overview-card">
    <div class="card-badge">Foundational Pillar</div>
    <h3>Meaning &amp; Definition of Encapsulation</h3>
    <p><strong>Encapsulation</strong> is the fundamental object-oriented mechanism of <strong>bundling data attributes and the operations (methods) that manipulate that data into a single unified container (the class)</strong>, while strictly restricting direct external access to internal state.</p>
    <p>Encapsulation provides <strong>Information Hiding</strong>. It erects an inviolable protective perimeter around an object's memory, ensuring that internal state can only be accessed or modified through authorized public methods that validate business invariants.</p>
  </div>
</div>

<div class="analogy-card">
  <div class="analogy-header">💡 Real-Life Analogy: The Gelatin Medical Capsule</div>
  <p>Think of a medicinal antibiotic capsule. The active chemical medicines are loose powders inside (the data attributes). The capsule's dissolvable gelatin shell encases and seals the medicine inside (<strong>Encapsulation</strong>). The patient swallows the smooth capsule without tasting the bitter chemicals or spilling the powder (<strong>Information Hiding</strong>).</p>
  <p>If you swallowed loose powder, an incorrect dosage could burn your esophagus. The capsule guarantees safe, controlled ingestion through a standardized interface!</p>
</div>

<div class="subtopics-container">
  <h4>The Mechanics of Encapsulation</h4>

  <div class="detail-block">
    <h5>1. The 3 Access Specifiers</h5>
    <ul>
      <li><code>private</code>: Members accessible strictly within the member functions of the declaring class. Completely hidden from the outside world and derived classes.</li>
      <li><code>protected</code>: Members accessible within the declaring class and its derived subclasses, but invisible to external client code.</li>
      <li><code>public</code>: The open interface through which external client code interacts with the object.</li>
    </ul>
  </div>

  <div class="detail-block">
    <h5>2. Enforcing Class Invariants</h5>
    <p>A <strong>Class Invariant</strong> is a condition that must always remain true for an object to be in a valid state (e.g., <code>balance &gt;= 0</code>, <code>month &gt;= 1 &amp;&amp; month &lt;= 12</code>). Direct public variable access allows outside code to bypass validation rules (e.g., setting <code>acc.balance = -50000;</code>). Encapsulation prevents this corruption.</p>
  </div>
</div>

<div class="comparison-table-wrapper">
  <h4>Comprehensive Comparison: Abstraction vs Encapsulation (AKTU Question 3.24)</h4>
  <table class="styled-table">
    <thead>
      <tr>
        <th>Comparison Dimension</th>
        <th>Abstraction</th>
        <th>Encapsulation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Core Concept</strong></td>
        <td>Process of <strong>gaining &amp; simplifying information</strong></td>
        <td>Process or method to <strong>contain &amp; protect information</strong></td>
      </tr>
      <tr>
        <td><strong>2. Lifecycle Level</strong></td>
        <td>Problems are solved at the <strong>design or interface level</strong></td>
        <td>Problems are solved at the <strong>implementation or code level</strong></td>
      </tr>
      <tr>
        <td><strong>3. Primary Goal</strong></td>
        <td>Hiding <em>unwanted complexity</em> ("WHAT" it does)</td>
        <td>Hiding <em>internal data representations</em> ("HOW" it stores it)</td>
      </tr>
      <tr>
        <td><strong>4. Implementation Tool</strong></td>
        <td>Implemented using <strong>Abstract classes &amp; Interfaces</strong></td>
        <td>Implemented using <strong>Access Specifiers</strong> (<code>private</code>, <code>public</code>)</td>
      </tr>
      <tr>
        <td><strong>5. Focus Point</strong></td>
        <td>Outer appearance / external view of an entity</td>
        <td>Inner protective packaging / internal boundaries</td>
      </tr>
      <tr>
        <td><strong>6. Mutual Relationship</strong></td>
        <td>Objects that provide abstraction are encapsulated</td>
        <td>Objects that result in encapsulation need not be abstracted</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="code-example-card">
  <div class="code-header">
    <span class="code-lang">C++ (Airtight Encapsulation &amp; Invariant Protection)</span>
    <span class="code-desc">Encapsulated Bank Account with validated accessors and audit logging</span>
  </div>
  <pre class="code-block"><code><span class="c-keyword">#include</span> <span class="c-string">&lt;iostream&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;string&gt;</span>
<span class="c-keyword">#include</span> <span class="c-string">&lt;stdexcept&gt;</span>

<span class="c-keyword">class</span> <span class="c-type">EncapsulatedAccount</span> {
<span class="c-comment">/* 1. PRIVATE SECTION: Hidden internal state (Encapsulation Shell) */</span>
<span class="c-keyword">private:</span>
    std::string accountNumber;
    <span class="c-type">double</span> balance;
    <span class="c-type">int</span> pinHash;

    <span class="c-comment">/* Private helper method: Internal verification only */</span>
    <span class="c-type">bool</span> verifyPin(<span class="c-type">int</span> enteredPin) <span class="c-keyword">const</span> {
        <span class="c-keyword">return</span> (enteredPin * 31 + 7) == pinHash; <span class="c-comment">/* Simple hash check */</span>
    }

<span class="c-comment">/* 2. PUBLIC SECTION: Controlled Access Gateway */</span>
<span class="c-keyword">public:</span>
    EncapsulatedAccount(std::string accNo, <span class="c-type">double</span> initialDep, <span class="c-type">int</span> pin)
        : accountNumber(accNo), balance(initialDep &gt; 0 ? initialDep : 0.0), pinHash(pin * 31 + 7) {}

    <span class="c-comment">/* Controlled Mutator (Setter): Enforces business invariants */</span>
    <span class="c-type">bool</span> withdraw(<span class="c-type">double</span> amount, <span class="c-type">int</span> pin) {
        <span class="c-keyword">if</span> (!verifyPin(pin)) {
            std::cout &lt;&lt; <span class="c-string">"Security Alert: Incorrect PIN! Transaction rejected."</span> &lt;&lt; std::endl;
            <span class="c-keyword">return false</span>;
        }
        <span class="c-keyword">if</span> (amount &lt;= 0 || amount &gt; balance) {
            std::cout &lt;&lt; <span class="c-string">"Transaction Rejected: Invalid amount or insufficient balance."</span> &lt;&lt; std::endl;
            <span class="c-keyword">return false</span>;
        }

        balance -= amount; <span class="c-comment">/* State updated safely */</span>
        std::cout &lt;&lt; <span class="c-string">"Withdrawal Successful! Dispensed: $"</span> &lt;&lt; amount &lt;&lt; std::endl;
        <span class="c-keyword">return true</span>;
    }

    <span class="c-comment">/* Controlled Accessor (Getter): Read-only view */</span>
    <span class="c-type">double</span> getBalance(<span class="c-type">int</span> pin) <span class="c-keyword">const</span> {
        <span class="c-keyword">if</span> (!verifyPin(pin)) {
            <span class="c-keyword">throw</span> std::runtime_error(<span class="c-string">"Unauthorized balance inquiry!"</span>);
        }
        <span class="c-keyword">return</span> balance;
    }
};

<span class="c-type">int</span> main() {
    <span class="c-type">EncapsulatedAccount</span> myAcc(<span class="c-string">"SB-5099"</span>, 1200.0, 4321);

    <span class="c-comment">/* Attempting unauthorized withdrawal with wrong PIN */</span>
    myAcc.withdraw(200.0, 9999);

    <span class="c-comment">/* Authorized withdrawal with correct PIN */</span>
    myAcc.withdraw(200.0, 4321);

    <span class="c-comment">/* Inspecting balance securely */</span>
    std::cout &lt;&lt; <span class="c-string">"Remaining Balance: $"</span> &lt;&lt; myAcc.getBalance(4321) &lt;&lt; std::endl;

    <span class="c-comment">/* myAcc.balance = 5000000; // ❌ COMPILE ERROR: Direct field access forbidden! */</span>
    <span class="c-keyword">return</span> 0;
}</code></pre>
</div>

<div class="svg-card">
  <div class="svg-header">
    <span class="svg-title">📐 Architecture Diagram: The Encapsulation Security Capsule</span>
  </div>
  <div class="svg-container">
    <svg viewBox="0 0 840 280" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="100%" fill="#0f172a" rx="12"/>
      
      <!-- Outer Protective Capsule Barrier -->
      <rect x="180" y="30" width="480" height="200" rx="35" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="420" y="58" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">ENCAPSULATION BOUNDARY (Class Shield)</text>

      <!-- Access Gateway Ports (Public Methods) -->
      <rect x="220" y="80" width="180" height="35" rx="5" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
      <text x="310" y="102" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">+ withdraw(amount, pin)</text>

      <rect x="440" y="80" width="180" height="35" rx="5" fill="#065f46" stroke="#34d399" stroke-width="1.5"/>
      <text x="530" y="102" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">+ getBalance(pin)</text>

      <!-- Inner Vault: Private Attributes -->
      <rect x="240" y="135" width="360" height="75" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
      <text x="420" y="158" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">🔒 PRIVATE PROTECTED VAULT (Hidden State)</text>
      <text x="420" y="178" fill="#cbd5e1" font-size="10" text-anchor="middle">- double balance  |  - string accountNumber  |  - int pinHash</text>
      <text x="420" y="195" fill="#f59e0b" font-size="9" text-anchor="middle">Inaccessible to outside world; zero direct tampering</text>

      <!-- External Callers -->
      <rect x="30" y="80" width="110" height="35" rx="4" fill="#0284c7"/>
      <text x="85" y="102" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Client Code</text>

      <!-- Authorized Message Vector -->
      <path d="M 140 97 L 210 97" stroke="#34d399" stroke-width="2" marker-end="url(#green-enc-arrow)"/>
      <text x="175" y="88" fill="#34d399" font-size="9" text-anchor="middle">public call</text>

      <!-- Direct Access Attempt (Blocked) -->
      <path d="M 140 170 L 230 170" stroke="#ef4444" stroke-width="2" stroke-dasharray="4" marker-end="url(#red-enc-arrow)"/>
      <text x="185" y="162" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">Direct Edit</text>
      <circle cx="235" cy="170" r="8" fill="#ef4444"/>
      <text x="235" y="174" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">×</text>

      <defs>
        <marker id="green-enc-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#34d399"/>
        </marker>
        <marker id="red-enc-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#ef4444"/>
        </marker>
      </defs>
    </svg>
  </div>
</div>

<div class="exam-corner">
  <div class="exam-title">🎓 University Exam Corner (AKTU Reference)</div>
  <p><strong>PYQ (AKTU 2015-16):</strong> <em>"Compare Abstraction and Encapsulation with suitable examples."</em> [5 Marks]</p>
  <div class="tip-box">
    <strong>Key Scoring Points:</strong> Always present the 6-point comparison table directly from the AKTU Quantum booklet. Key distinctions: <em>Abstraction is at the design/interface level (what); Encapsulation is at the implementation level (how); Abstraction uses abstract classes/interfaces; Encapsulation uses access modifiers (private/protected)</em>.
  </div>
</div>
"""
        }
    ]
