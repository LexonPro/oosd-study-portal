# OOSD Unit 1 — Complete Study Notes (AKTU KCS-054)

---

# PART 1: Object-Oriented Concepts & Principles

---

## Topic 1 — Object-Oriented Approach & Meaning of Object Orientation
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2012-13 (5 Marks), AKTU 2013-14 (5 Marks)

### 1. Simple Meaning
In traditional programming, you write functions that act on loose data. In the Object-Oriented (OO) approach, software is built by combining data and the functions that operate on that data into single units called **objects**. It models software after real-world things to make large systems easier to build, maintain, and modify.

### 2. One-Line Definition
The Object-Oriented approach is a software development methodology that organizes a system as a collection of interacting objects combining both data (attributes) and behavior (methods).

### 3. Easy Example
Think of a **Student** in a college. A student has details like name and roll number, and actions like studying or taking an exam. Instead of keeping the details and actions separate, we pack them together into one entity.

### 4. Technical Example
- **Real Life:** A student has a name and attends lectures.
- **OOSD:** `name` and `rollNo` are **attributes** (data), and `attendLecture()` is a **method** (behavior) inside a `Student` object.

### 5. Simple Diagram
```text
        +-------------------------+
        |      Student Object     |
        +-------------------------+
        |  Data:                  |
        |    - name               |
        |    - rollNo             |
        +-------------------------+
        |  Behavior:              |
        |    + attendLecture()    |
        |    + writeExam()        |
        +-------------------------+
```

### 6. Simple C++ Example
```cpp
#include <iostream>
using namespace std;

class Student {
public:
    string name;
    int rollNo;

    void display() {
        cout << "Name: " << name << ", Roll No: " << rollNo << endl;
    }
};

int main() {
    Student s1;              // Creating an object
    s1.name = "Aman";
    s1.rollNo = 101;
    s1.display();            // Calling behavior
    return 0;
}
```
**Explanation:**
- `Student`: The class (blueprint).
- `s1`: The object created from the class.
- `name`, `rollNo`: Attributes holding data.
- `display()`: Method defining behavior.

### 7. What to Remember
- Combines data and functions into small, modular units.
- Bridges the gap between the real-world problem and software solution.
- **Main Benefits:** Reusability of code, easier maintenance, lower change cost, and simpler integration of large systems.

### 8. AKTU Exam Answer
**Q. Explain the Object-Oriented approach and state its benefits.**
1. **Meaning:** The Object-Oriented approach focuses on capturing the structure (data) and behavior (operations) of an information system into interacting modules called objects.
2. **Key Elements:** Objects, Attributes, Methods, Classes, and Messages.
3. **Core Benefits:**
   - *Low-cost changes:* Local changes do not break other parts of the system.
   - *Code Reusability:* Classes can be reused across multiple projects.
   - *Easy Integration:* Modular components simplify configuring large software.
   - *Maintainability:* Centralized code structure makes upgrades and bug fixing direct.

### 9. Quick Check
1. What does an object combine?
2. Mention two main benefits of the object-oriented approach.

---

## Topic 2 — Elements of an Object-Oriented System
**Exam Priority:** MEDIUM

### 1. Simple Meaning
An object-oriented system is made up of six basic building blocks: objects, classes, attributes, behavior, methods, and messages.

### 2. One-Line Definition
The elements of an OO system are the foundational components—objects, classes, attributes, behavior, methods, and messages—used to construct object-oriented models.

### 3. Easy Example
In a college management system:
- **Class:** `Student` (the template for all students).
- **Object:** Rahul (a real, specific student).
- **Attributes:** Rahul's name, branch, roll number.
- **Behavior / Methods:** Registering for courses, paying fees.
- **Message:** The college portal calling `payFee()` on Rahul's account.

### 4. Technical Breakdown of Elements
1. **Object:** A tangible or intangible entity in the problem domain that has state and behavior.
2. **Class:** A blueprint or template that groups objects sharing identical attributes, operations, and semantics.
3. **Attributes:** Named data properties describing the state of an object.
4. **Behavior:** The set of operations an object can perform or undergo.
5. **Methods:** The actual implementation code for an operation within a class.
6. **Message:** A function or procedure call sent from one object to another to invoke a method.

### 5. Simple Diagram
```text
  [Object A] ------ Message: getDetails() ------> [Object B: Student]
                                                  | - name: "Rahul"
                                                  | + getDetails()
```

### 6. What to Remember
- **Object:** Instance of a class.
- **Class:** Blueprint / type definition.
- **Attribute:** Data variable inside an object.
- **Method:** Code that executes an action.
- **Message:** Communication request between objects.

### 7. AKTU Exam Answer
**Q. Describe the elements of an object-oriented system.**
1. **Object:** An instance representing a real-world entity with state and behavior.
2. **Class:** A template grouping objects with common properties and operations.
3. **Attributes:** Data fields holding information about the object.
4. **Behavior:** Defines what the object can do.
5. **Methods:** Executable procedures that implement the object's behavior.
6. **Message:** Information passed between objects to trigger methods.

### 8. Quick Check
1. What is the difference between a method and a message?
2. Is a bank account an object or a class?

---

## Topic 3 — Procedural vs Object-Oriented Programming (Structured vs OO Approach)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2012-13 (5 Marks), AKTU 2013-14 (5 Marks)

### 1. Simple Meaning
Procedural programming focuses on **actions** (verbs/functions) where data moves freely. Object-Oriented programming focuses on **entities** (nouns/objects) that protect their own data.

### 2. One-Line Definition
Procedural programming is a function-centric, top-down approach, whereas Object-Oriented programming is a data-centric, bottom-up approach combining data and operations into secure objects.

### 3. Easy Example
- **Procedural (e.g., C):** You write a standalone function `calculateInterest(balance, rate)` and pass raw balance variables around.
- **Object-Oriented (e.g., C++):** You create a `BankAccount` object that stores its own `balance` securely and provides a `calculateInterest()` method.

### 4. Common Confusion / Comparison Table

| Feature | Procedural Oriented (POP) | Object-Oriented (OOP) |
|---|---|---|
| **Core Focus** | Functions / Algorithms | Data / Objects |
| **Approach** | Top-Down | Bottom-Up |
| **Data Security** | Low (data moves openly across functions) | High (data hidden via access specifiers) |
| **Access Specifiers**| Not available | `private`, `public`, `protected` |
| **Reusability** | Difficult | High (via Inheritance) |
| **Overloading** | Not supported | Supported (Function & Operator) |
| **Adding New Data** | Difficult (requires modifying many functions)| Easy (add new classes or attributes) |
| **Real-World Mapping**| Poor (unreal model of problems) | Strong (models real-world entities) |
| **Examples** | C, Pascal, FORTRAN | C++, Java, Python, C# |

### 5. What to Remember
- POP = Function-first, Top-down, Open data.
- OOP = Data-first, Bottom-up, Protected data.

### 6. AKTU Exam Answer
**Q. Compare Procedural Programming with Object-Oriented Programming.**
- Write the definition of both paradigms.
- Present the comparison table above (focusing on Approach, Data Security, Modularity, Reusability, and Examples).
- **Conclusion:** OOP is preferred for large, evolving systems because it prevents ripple effects and allows component reuse.

### 7. Quick Check
1. Which approach follows a bottom-up design?
2. Why is OOP more secure than procedural programming?

---

## Topic 4 — Object-Oriented Technology (OOT): Pros and Cons
**Exam Priority:** MEDIUM  
**PYQ mentioned in uploaded material:** AKTU 2011-12 (10 Marks), AKTU 2012-13 (10 Marks)

### 1. Simple Meaning
Object-Oriented Technology is the broader practice of using object-oriented principles across analysis, design, and coding to manage software development efficiently.

### 2. One-Line Definition
Object-Oriented Technology (OOT) is a systematic approach to program organization and software development that solves the maintenance and scalability issues of conventional structured techniques.

### 3. Pros and Cons

#### Pros (Advantages)
1. **Parallel Development:** Teams can work on independent classes simultaneously once interfaces are agreed upon.
2. **High Reusability:** Well-designed modular classes can be plugged into other applications.
3. **Easier Maintenance:** Changes are localized inside classes, preventing ripple bugs across the system.
4. **Improved Data Security:** Validation inside methods protects critical internal data from corruption.

#### Cons (Disadvantages)
1. **Runtime Overhead:** Object creation, dynamic binding, and message passing can consume more CPU and memory.
2. **Steeper Learning Curve & Design Complexity:** Designing proper class hierarchies requires significant upfront planning.
3. **Overhead of Code Bloat:** Uncontrolled inheritance and wrappers can lead to unnecessarily large codebases.

### 4. What to Remember
- Pros: Parallel teamwork, reusability, easy maintenance.
- Cons: Performance overhead, potential code bloat, design complexity.

### 5. AKTU Exam Answer
**Q. What is Object-Oriented Technology? Discuss its pros and cons.**
- Define OOT as a language-independent methodology for organizing systems into modular objects.
- List 3 key Pros (Parallel development, Reusability, Maintainability).
- List 3 key Cons (Runtime overhead, Design complexity, Code bloat).

### 6. Quick Check
1. Why does OOT support parallel team development?
2. Name one performance drawback of OOT.

---

## Topic 5 — Object Identity
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2013-14 (5 Marks)

### 1. Simple Meaning
Object identity means that every single object is unique and distinct from every other object in memory, even if two objects contain the exact same data values.

### 2. One-Line Definition
Object identity is an inherent property of an object in an OO data model by which it is uniquely identified and distinguished from all other objects through an internal identifier (such as its memory address), independent of its attribute values.

### 3. Easy Example
Two students, Aman and Amit, might have the exact same marks (95%) and attend the same course, but they are two distinct human beings. In software, their identity is distinct even if all their data fields match.

### 4. Technical Example
In C++, an object's memory address (`&object`) serves as its unique identity. Testing object identity is done by comparing pointer addresses (`ptr1 == ptr2`), not by comparing field values.

### 5. Simple Diagram
```text
  Object A [Address: 0x1000]          Object B [Address: 0x2000]
  +------------------------+          +------------------------+
  | name: "Aman"           |          | name: "Aman"           |
  | marks: 95              |          | marks: 95              |
  +------------------------+          +------------------------+
  Values are IDENTICAL, but Identities are DIFFERENT (0x1000 != 0x2000).
```

### 6. Simple C++ Example
```cpp
#include <iostream>
using namespace std;

class Student {
public:
    string name;
};

int main() {
    Student s1;
    Student s2;

    s1.name = "Aman";
    s2.name = "Aman"; // Same attribute value

    if (&s1 == &s2) {
        cout << "Same Object" << endl;
    } else {
        cout << "Different Objects (Unique Identities)" << endl;
    }
    return 0;
}
```
**Output:** `Different Objects (Unique Identities)`

### 7. What to Remember
- Value equality $\neq$ Identity equality.
- Identity is assigned automatically by the system runtime (e.g., memory address in C++).
- Identity allows objects to be linked, compared, and referenced without relying on changing attribute values.

### 8. AKTU Exam Answer
**Q. What do you understand by Object Identity? Explain with an example.**
1. **Definition:** Object identity is the characteristic that distinguishes an object from all other objects regardless of its attribute contents.
2. **Mechanism:** OO languages assign an implicit internal identifier (e.g., memory address in C++ using `&`).
3. **Usage:** Used to establish relationships (links) and perform fast pointer comparisons.
4. **Example:** Two objects `s1` and `s2` having identical names still reside at different memory addresses, proving distinct identity.

### 9. Quick Check
1. Can two objects have identical attribute values but different identities?
2. In C++, which operator reveals the physical identity of an object?

---

## Topic 6 — Encapsulation & Message Passing
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11 (5 Marks), AKTU 2012-13 (5 Marks)

### 1. Simple Meaning
Encapsulation means wrapping data and related methods together into a protective single unit and restricting outside access to internal data so that only approved methods can modify it.

### 2. One-Line Definition
Encapsulation is the mechanism that binds code and the data it manipulates into a single unit, separating the external public interface from the internal implementation details.

### 3. Easy Example
A **Bank Account** stores a `balance`. The balance is kept private inside the account. You cannot directly modify the balance variable from outside; you must send a request via `deposit()` or `withdraw()` methods.

### 4. Technical Example (Message Passing role)
Other objects interact with a `BankAccount` object solely by sending **messages** (invoking public member functions like `deposit(500)`). The internal data is never touched directly, ensuring valid state transitions.

### 5. Simple Diagram
```text
               +--------------------------------------+
               |          BankAccount Object          |
               |                                      |
               |   [Private Data]                     |
               |      double balance;                 |
               |                                      |
  Message ---->|   [Public Methods (Interface)]       |
  deposit()    |      + deposit(amount)               |
               |      + withdraw(amount)              |
               |      + getBalance()                  |
               +--------------------------------------+
```

### 6. Simple C++ Example
```cpp
#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance; // Hidden data

public:
    BankAccount() { balance = 0.0; }

    void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    double getBalance() {
        return balance;
    }
};

int main() {
    BankAccount acc;
    acc.deposit(1000);
    // acc.balance = 5000; // ERROR: balance is private
    cout << "Balance: " << acc.getBalance() << endl;
    return 0;
}
```

### 7. What to Remember
- Bundles data + methods together.
- Uses `private` for data and `public` for methods.
- Message passing ensures external code only talks to the public interface.
- Prevents ripple effects when internal code changes.

### 8. AKTU Exam Answer
**Q. Explain Encapsulation and how message passing enforces it.**
1. **Definition:** Encapsulation binds data and functions together into a single unit (class) while shielding internal data from direct external access.
2. **Role of Message Passing:** External entities cannot manipulate internal variables directly. They send messages (method calls with valid signatures) to the object's interface.
3. **Benefits:** Prevents unintended data corruption, localizes bugs, and allows modifying internal algorithms without breaking client code.

### 9. Quick Check
1. Which C++ access specifier is typically used for encapsulated data?
2. What is the benefit of accessing data only through methods?

---

## Topic 7 — Information Hiding
**Exam Priority:** MEDIUM

### 1. Simple Meaning
Information hiding is the design principle of intentionally concealing the internal design and algorithm details of a module so that other parts of the program do not depend on how it works inside.

### 2. One-Line Definition
Information hiding is the principle of segregating design decisions that are likely to change behind stable interfaces, exposing only what is necessary to use the component.

### 3. Easy Example
When you use a TV remote to change channels, you only interact with the channel buttons. You do not know or care whether the internal circuitry uses an analog frequency tuner or a modern digital chip.

### 4. Encapsulation vs Information Hiding

| Feature | Encapsulation | Information Hiding |
|---|---|---|
| **What it is** | A language mechanism / packaging technique | A design principle / goal |
| **Focus** | Bundling data and functions together | Concealing internal algorithms and design choices |
| **Relationship** | Encapsulation is the primary technique used to achieve Information Hiding |

### 5. What to Remember
- Focuses on hiding **implementation details** and **change-prone decisions**.
- Decouples client code from the inner workings of an object.
- Makes software easy to evolve, optimize, or fix without breaking dependencies.

### 6. AKTU Exam Answer
**Q. Write a short note on Information Hiding.**
1. **Definition:** Information hiding is the practice of hiding the internal workings and data structures of an object behind a clean, public interface.
2. **Implementation:** Achieved primarily through encapsulation and access control specifiers (`private`/`protected`).
3. **Primary Advantages:**
   - *Decoupling:* Calling code does not depend on internal data formats.
   - *Flexibility:* Internal algorithms can be upgraded or replaced without altering caller code.

### 7. Quick Check
1. What is the main difference between encapsulation and information hiding?
2. Why does information hiding make programs easier to modify?

---

## Topic 8 — Polymorphism (Ad-hoc vs Universal)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11 (5 Marks), AKTU 2012-13 (5 Marks), AKTU 2014-15 (5 Marks)

### 1. Simple Meaning
Polymorphism literally means **"many forms"**. It allows a single operation name or message to behave differently depending on the object that is receiving it.

### 2. One-Line Definition
Polymorphism is the ability of different objects to respond to the same message or operation in their own unique, class-specific way.

### 3. Easy Example
Consider the command `speak()`. If you send `speak()` to a `Dog`, it barks. If you send `speak()` to a `Cat`, it meows. The command name is identical, but the outcome depends on the receiver.

### 4. Technical Classification (Ad-hoc vs Universal)
```text
                      Polymorphism
                            |
             -------------------------------
             |                             |
      Ad-hoc Polymorphism         Universal Polymorphism
             |                             |
     -----------------             -----------------
     |               |             |               |
  Function        Operator     Parametric      Inclusion /
Overloading      Overloading  (Generics/       Subtyping
                              Templates)     (Virtual Functions)
```
1. **Ad-hoc Polymorphism:** Applies functions to arguments of different specific types (e.g., function overloading, operator overloading). It exists in both traditional and OO languages.
2. **Universal Polymorphism:** Functions/types are written universally without hardcoding one specific type:
   - **Parametric:** Code is written generically using type parameters (e.g., C++ Templates).
   - **Subtyping (Inclusion):** An operation defined in a base class is overridden in subclasses and bound dynamically at runtime (e.g., virtual functions in C++).

### 5. Simple Diagram
```text
                     [Shape Base Class]
                     | + draw()       |
                     +----------------+
                            ^
              -------------   -------------
              |                           |
     [Circle Subclass]           [Rectangle Subclass]
     | + draw() -> draws O |     | + draw() -> draws [] |
```

### 6. Simple C++ Example
```cpp
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() { // Virtual function enables runtime polymorphism
        cout << "Animal makes a sound" << endl;
    }
};

class Dog : public Animal {
public:
    void speak() override {
        cout << "Dog barks" << endl;
    }
};

int main() {
    Animal* a = new Dog();
    a->speak(); // Outputs: Dog barks
    delete a;
    return 0;
}
```

### 7. What to Remember
- Polymorphism = Many forms.
- Shares the same external interface across different internal implementations.
- **Two broad categories:** Ad-hoc (overloading) and Universal (templates / inheritance-based subtyping).
- Subtyping requires dynamic binding (virtual functions in C++).

### 8. AKTU Exam Answer
**Q. Define Polymorphism. Is this concept only applicable to object-oriented systems?**
1. **Definition:** Polymorphism is the capability of a single message or operation to take on different behaviors across different classes.
2. **Applicability:**
   - **No, it is not strictly limited to OO systems.**
   - *Ad-hoc polymorphism* (such as function/operator overloading) is supported in both non-OO (traditional) and OO systems.
   - *Universal polymorphism* (parametric templates and runtime subtype polymorphism via inheritance) is characteristic of object-oriented systems.
3. **Example:** Base class `Shape` with virtual method `draw()`, specialized by `Circle` and `Rectangle`.

### 9. Quick Check
1. What are the two main kinds of universal polymorphism?
2. Is function overloading an example of ad-hoc or universal polymorphism?

---

## Topic 9 — Generosity (Generics / Parameterized Classes)
**Exam Priority:** LOW / MEDIUM  
**PYQ mentioned in uploaded material:** AKTU 2014-15 (Paper mention)

### 1. Simple Meaning
Generosity (commonly called **Generics** or Parameterized Classes) allows you to write a class or function without fixing the exact data type in advance. The data type is passed as a parameter when creating the object.

### 2. One-Line Definition
Generosity is an object-oriented feature that enables classes and methods to be defined with generic type parameters, allowing the same logic to work safely with any data type.

### 3. Easy Example
Think of a **Storage Box**. The box logic (storing, retrieving, counting items) is identical whether you store books, toys, or clothes inside it. You do not need to build three separate types of boxes.

### 4. Technical Example
In C++, generosity is implemented using **Templates**. In Java, it is implemented using **Generics** (`ArrayList<T>`).

### 5. Simple C++ Example
```cpp
#include <iostream>
using namespace std;

// Template demonstrating Generosity (Generic Class)
template <typename T>
class Box {
private:
    T item;
public:
    void setItem(T val) { item = val; }
    T getItem() { return item; }
};

int main() {
    Box<int> intBox;
    intBox.setItem(50);
    cout << "Integer in Box: " << intBox.getItem() << endl;

    Box<string> strBox;
    strBox.setItem("OOSD Notes");
    cout << "String in Box: " << strBox.getItem() << endl;
    return 0;
}
```

### 6. What to Remember
- Parameterizes classes and functions with data types.
- Promotes maximum code reusability and type safety.
- Implemented via `template <typename T>` in C++.

### 7. AKTU Exam Answer
**Q. What is Generosity in Object-Oriented Systems?**
- **Definition:** Generosity is the mechanism of parameterizing software components (classes/methods) with types, creating generic templates.
- **Purpose:** Avoids writing duplicate code for different data types.
- **Example:** C++ class templates (`template<typename T>`) where a single `Stack<T>` class works for `int`, `float`, or user-defined objects.

### 8. Quick Check
1. What C++ feature implements generosity?
2. What is the primary advantage of generic classes?

---

# PART 1: EXAM PREPARATION & QUICK REVISION

### 2-Mark Preparation
- **Object:** Instance of a class containing data attributes and behavior methods.
- **Class:** A blueprint grouping objects with common attributes, operations, and semantics.
- **Object Identity:** Inherent property distinguishing an object via unique identifier (memory address).
- **Encapsulation:** Mechanism binding data and methods while restricting direct external access.
- **Information Hiding:** Design principle of concealing internal algorithm and representation details.
- **Polymorphism:** Ability of an operation or message to take multiple forms across classes.
- **Generosity:** Writing classes/functions with type parameters (templates/generics).

### 5-Mark Preparation
- Differences between Procedural (POP) and Object-Oriented Programming (OOP).
- Features of Object-Oriented Languages (Encapsulation, Inheritance, Polymorphism, Abstraction).
- Role of message passing in enforcing encapsulation.
- Classification of Polymorphism (Ad-hoc vs Universal).

### Long Answer (10-Mark) Preparation
- Object-Oriented Technology: Complete definition, pros, cons, and structural elements.

---

## PART 1 — QUICK REVISION TABLE

| Concept | Key Exam Formula / Core Meaning | Priority |
|---|---|---|
| **Object Orientation** | System = Interacting objects bundling data + process | HIGH |
| **OO Elements** | Object, Class, Attribute, Behavior, Method, Message | MEDIUM |
| **POP vs OOP** | Top-down / function-first vs Bottom-up / data-first | HIGH |
| **OOT Pros & Cons** | Reusable, maintainable, parallel dev vs overhead, complexity | MEDIUM |
| **Object Identity** | Unique ID/address ($\neq$ attribute values) | HIGH |
| **Encapsulation** | Shell combining data + methods, access via public interface | HIGH |
| **Information Hiding** | Concealing internal algorithms to decouple caller | MEDIUM |
| **Polymorphism** | Same interface, multiple implementations (Ad-hoc & Universal) | HIGH |
| **Generosity** | Type parameterization (C++ templates) | LOW |

### Self-Test (Part 1)
1. Differentiate between identity equality and value equality.
2. How does message passing protect encapsulated data?
3. List 4 core differences between procedural and OO programming.
4. What is the difference between ad-hoc and universal polymorphism?
5. State two advantages and two disadvantages of OOT.

---

# PART 2: Modelling & Object-Oriented Modelling (OOM / OMT)

---

## Topic 10 — Importance & Purposes of Modelling
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12 (5 Marks), AKTU 2013-14 (5 Marks)

### 1. Simple Meaning
A model is a simplified blueprint of a system created before actually building it. We build models to understand complex systems, test them early, fix flaws cheaply, and communicate clearly with clients.

### 2. One-Line Definition
A model is an abstraction of a real-world system created to visualize, specify, construct, document, and understand the system before committing to implementation.

### 3. Easy Example
Before constructing a large college building, architects make a 3D miniature scale model or blueprint. If a room layout is wrong, fixing the drawing costs almost nothing compared to breaking concrete walls later.

### 4. Four Purposes Served by Models (As per Syllabus)
1. **Testing Physical / System Entities Early:** Simulating a model helps catch design flaws cheaply before building the final product (e.g., wind tunnel testing of scale airplane models).
2. **Communication with Customers:** Demonstration mock-ups and wireframes show users how the system will work to confirm requirements.
3. **Visualization:** Like storyboards in movie making, models help designers see how system elements interact and flow.
4. **Reduction of Complexity:** Leaves out non-essential details so engineers can focus on critical problem logic.

### 5. Simple Diagram
```text
  Real-World Problem  ===(Abstraction)===>  Model (Simplified Blueprint)
                                                      |
                                              [Understand & Test]
                                                      |
                                                      v
                                            Final Software System
```

### 6. What to Remember
- Abstraction: Keeps essential details, drops non-essentials.
- Cheaper to test and modify than real code.
- Primary purposes: Testing, Communication, Visualization, Complexity Reduction.

### 7. AKTU Exam Answer
**Q. What is modelling? Discuss the purposes served by models.**
- **Definition:** Modelling is the process of creating concise abstractions of a system to understand requirements and architecture prior to construction.
- **Four Purposes:**
  1. *Testing:* Inexpensive verification of system behavior before full implementation.
  2. *Customer Communication:* Uses mock-ups to validate client expectations.
  3. *Visualization:* Provides clear graphical views of component flows.
  4. *Complexity Reduction:* Manages cognitive load by hiding implementation trivia.

### 8. Quick Check
1. What is an abstraction?
2. Name two purposes of modelling.

---

## Topic 11 — Principles of Modelling
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2013-14 (5 Marks), AKTU 2014-15 (5 Marks)

### 1. Simple Meaning
When designing software models, you must follow four foundational rules to ensure the models are accurate, practical, and useful.

### 2. Four Basic Principles of Modelling (Authoritative List)

```text
                     4 Principles of Modelling
                                 |
     +---------------------------+---------------------------+
     |                           |                           |
1. Choice of Models         2. Levels of Precision      3. Connected to Reality
(Shapes solution)           (High-level vs detailed)   (Reflects real world)
                                 |
                    4. Multiple Independent Models
                    (No single model is sufficient)
```

1. **The choice of what models to create has a profound influence on how a problem is attacked and how a solution is shaped:**
   - Picking the right model directs the entire solution path. An incorrect model makes simple problems hard.
2. **Every model may be expressed at different levels of precision:**
   - A client needs a high-level overview; a developer needs a detailed specification with types and algorithms.
3. **The best models are connected to reality:**
   - Models must reflect real-world constraints and business logic accurately without impossible assumptions.
4. **No single model is sufficient; every non-trivial system is best approached through a small set of nearly independent models:**
   - A complete system requires multiple orthogonal views (e.g., structural, dynamic, and functional) to represent the whole picture.

### 3. What to Remember
- Choice of model shapes the solution.
- Models exist at multiple levels of detail/precision.
- Models must be grounded in reality.
- No single model is enough (need multiple views).

### 4. AKTU Exam Answer
**Q. Explain the basic principles of modelling.**
- State and explain the 4 principles with 1-2 explanatory sentences each:
  1. *Choice of model shapes solution:* Dictates approach and architecture.
  2. *Different levels of precision:* High-level for management, precise for coders.
  3. *Connected to reality:* Grounded in practical problem-domain constraints.
  4. *Multiple independent models:* Non-trivial systems require structural, behavioral, and architectural views.

### 5. Quick Check
1. Why is a single model insufficient for a software system?
2. How does the choice of a model affect the final solution?

---

## Topic 12 — Steps of Object-Oriented Design / OOM Process
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11 (5 Marks), AKTU 2015-16 (10 Marks)

### 1. Simple Meaning
Building an object-oriented system follows four sequential stages: understand the problem domain, architect the subsystems, detail the classes and data structures, and finally write clean code.

### 2. The 4 Stages of the OOM / OOD Process

```text
  [1. System Analysis]  ===> Understand real-world domain (What to do)
           |
           v
  [2. System Design]    ===> Subsystem partitioning & architecture strategy
           |
           v
  [3. Object Design]    ===> Data structures, algorithms, internal details
           |
           v
  [4. Implementation]   ===> Coding classes & mapping to target language
```

1. **System Analysis:**
   - Formulates the problem statement and builds a concise real-world domain model.
   - Focuses on *what* the system must do, using terms understandable to domain experts without coding jargon.
2. **System Design:**
   - Establishes the high-level architecture.
   - Partitions the system into subsystems and allocates resources, protocols, and performance priorities.
3. **Object Design:**
   - Adds computer-domain implementation details to the analysis model.
   - Determines the specific data structures, algorithms, and method implementations for each class.
4. **Final Implementation:**
   - Translates designed classes, relationships, and algorithms into a programming language (e.g., C++) using good software engineering practices.

### 3. Application Example (Light Bulb Filament vs Airplane Wire)
*This classic OMT abstraction example from the uploaded material illustrates how requirements shape object design:*
- **Application 1: Light bulb filament wire:** The critical properties are extreme heat resistance and high melting point (Tungsten is chosen despite brittleness).
- **Application 2: Airplane electrical wire:** The critical properties are lightweight construction, vibration/chafe-resistant insulation, and non-flammability.
- *Lesson:* The environment and design phase dictate which attributes and constraints must be prioritized.

### 4. What to Remember
- **Analysis:** Domain concepts (*What*).
- **System Design:** Subsystems & architecture.
- **Object Design:** Data structures & algorithms (*How*).
- **Implementation:** Coding & testing.

### 5. AKTU Exam Answer
**Q. Describe the various steps involved in the Object-Oriented Modelling (OOM) process.**
- Define OOM as the construction of systems using abstractions of domain objects.
- Detail the 4 steps:
  1. *System Analysis:* Problem formulation and domain class modeling.
  2. *System Design:* Partitioning into subsystems and setting performance goals.
  3. *Object Design:* Selecting concrete algorithms and data structures.
  4. *Implementation:* Writing maintainable, traceable source code.

### 6. Quick Check
1. Which phase of OOM decides the data structures and algorithms for a class?
2. What is the difference between System Analysis and Object Design?

---

## Topic 13 — OMT: Three Models of Object-Oriented Systems
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12 (5 Marks), AKTU 2014-15 (10 Marks)

### 1. Simple Meaning
The Object Modeling Technique (OMT), created by James Rumbaugh, models software from three distinct, orthogonal perspectives: static structure (Object Model), behavior over time (Dynamic Model), and data computations (Functional Model).

### 2. The Three OMT Models

```text
                         OMT Methodology
                                |
     +--------------------------+--------------------------+
     |                          |                          |
[Object Model]           [Dynamic Model]           [Functional Model]
  - Static structure       - Temporal behavior       - Data transformations
  - Classes & Relations    - States & Events         - DFD (Inputs -> Outputs)
  - Class Diagram          - State Diagram           - Data Flow Diagram
```

1. **Object Model:**
   - **What it shows:** The static structure of the system—identifies classes, attributes, operations, and relationships.
   - **Artifact used:** Class Diagram.
   - **Focus:** *Structure.*
2. **Dynamic Model:**
   - **What it shows:** System behavior over time, control flows, events, and state changes of objects.
   - **Artifact used:** Statechart / State Diagram.
   - **Focus:** *Sequencing & Control.*
3. **Functional Model:**
   - **What it shows:** What calculations and transformations happen to data values (inputs to outputs) without specifying how or when.
   - **Artifact used:** Data Flow Diagram (DFD).
   - **Focus:** *Computation.*

### 3. Comparison of the Three OMT Models

| Model | Primary Focus | Diagram Used | Key Elements |
|---|---|---|---|
| **Object Model** | Static structure | Class Diagram | Classes, attributes, operations, inheritance, association |
| **Dynamic Model** | Temporal behavior & control | State Diagram | States, events, transitions, actions |
| **Functional Model** | Data transformation | Data Flow Diagram (DFD) | Processes, data flows, actors, data stores |

### 4. What to Remember
- Object Model = Static Structure (Class diagram).
- Dynamic Model = Control & States over time (Statechart).
- Functional Model = Data transformations (DFD).
- Together they provide a complete, orthogonal specification of the system.

### 5. AKTU Exam Answer
**Q. What are the different models used in OMT? Explain their relationships.**
- Define OMT as a methodology combining three orthogonal views.
- Explain the **Object Model** (static structure, class diagrams).
- Explain the **Dynamic Model** (time-sequenced events, state diagrams).
- Explain the **Functional Model** (data transformations, DFDs).
- Draw the 3-model summary diagram and comparison table.

### 6. Quick Check
1. Which OMT model represents the static structure of a system?
2. Which diagram is used to represent the dynamic model?

---

## Topic 14 — Elements of Functional Modeling (Data Store, Actors, Control Flow)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2015-16 (15 Marks)

### 1. Simple Meaning
Inside an OMT Data Flow Diagram (Functional Model), data moves between active sources/destinations (**actors**), transformation steps (**processes**), passive storage areas (**data stores**), and conditional triggers (**control flow**).

### 2. Definitions and Notations

```text
  [ Actor ] ======= Data Flow ======> ( Process ) <=======> | Data Store |
                                          :
                                    Control Flow (Boolean)
                                          :
```

1. **Data Store:**
   - **Meaning:** A passive entity that stores data for later access. It does not generate actions on its own; it only responds to requests to store or retrieve values.
   - **Notation:** Drawn as a pair of parallel horizontal lines: `= Store Name =`.
   - **Arrows:** Incoming arrow = write/insert/update; Outgoing arrow = read/retrieve.
2. **Actors:**
   - **Meaning:** An active entity (outside or boundary of the system) that drives the data flow by producing input data or consuming output results (e.g., User, Sensor, Thermostat).
   - **Notation:** Drawn as a rectangle containing the actor's name.
3. **Control Flow:**
   - **Meaning:** A boolean decision value or signal that enables or disables the execution of a process. It is a control trigger, *not* an input value to the calculation.
   - **Notation:** Drawn as a dashed/dotted arrow line ending at a process circle.

### 3. What to Remember
- **Actor:** Active source/sink (drawn as rectangle).
- **Data Store:** Passive storage (drawn as parallel lines).
- **Control Flow:** Boolean process activator (drawn as dotted line).

### 4. AKTU Exam Answer
**Q. Write short notes on: (a) Data store, (b) Actors, (c) Control flow.**
- **(a) Data Store:** Passive repository for holding state between operations. Represented by two parallel lines. Allows out-of-sequence data access.
- **(b) Actors:** External active objects that produce or consume values to initiate data flows. Represented by a rectangle.
- **(c) Control Flow:** Dotted arrow representing a boolean signal determining whether a process is evaluated.

### 5. Quick Check
1. Does a data store initiate operations on its own?
2. How is a control flow graphically distinguished from a standard data flow?

---

## Topic 15 — Link and Association
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2012-13 (5 Marks)

### 1. Simple Meaning
An **association** is the general relationship between two classes (a concept). A **link** is the actual physical connection between two specific objects (a runtime instance).

### 2. One-Line Definitions
- **Association:** A description of a group of links with common structure and semantics connecting two or more classes.
- **Link:** A physical or conceptual connection between individual object instances; a link is an instance of an association.

### 3. Easy Example
- **Association (Class Level):** `Student` is enrolled in `Course`.
- **Link (Object Level):** `Aman` (an instance of Student) is linked to `CS101` (an instance of Course).

### 4. Comparison: Link vs Association

| Feature | Link | Association |
|---|---|---|
| **Level** | Object level (Runtime instance) | Class level (Model blueprint) |
| **Definition** | Connection between specific objects | Relationship between classes |
| **Diagram** | Appears in Object Diagrams | Appears in Class Diagrams |
| **Multiplicity** | Connects specific individual instances | Shows general multiplicity (`*`, `1..*`, `0..1`) |

### 5. Simple Diagrams
```text
Class Diagram (Association):
+----------+                     +----------+
|  Person  | * --------------- * | Company  |
+----------+      OwnsStock      +----------+

Object Diagram (Links):
( Aman:Person ) ----------------- ( TCS:Company )
( Aman:Person ) ----------------- ( Infosys:Company )
( Priya:Person ) ---------------- ( TCS:Company )
```

### 6. What to Remember
- Association = Class level.
- Link = Object level (Instance of association).
- Both are represented with lines connecting boxes in UML.

### 7. AKTU Exam Answer
**Q. Define Link and Association. Discuss their role in Object Modelling with examples.**
1. **Definitions:**
   - *Link:* A concrete connection between individual objects.
   - *Association:* A structural relationship describing a set of links between classes.
2. **Role:** Associations define possible static relationships in the domain; links reflect actual runtime configurations.
3. **Example & Diagrams:** Draw the `Person` - `Company` (Class Association) vs `Aman` - `TCS` (Object Link) diagrams shown above.

### 8. Quick Check
1. Is a link an instance of an association?
2. In which diagram do links appear?

---

# PART 2: EXAM PREPARATION & QUICK REVISION

### 2-Mark Preparation
- **Model:** Simplified abstraction to understand a system before building it.
- **Link:** Instance of an association between specific objects.
- **Association:** Structural relationship between classes.
- **Actor:** Active object that produces/consumes data flow.
- **Data Store:** Passive repository in a DFD (parallel lines).
- **Control Flow:** Dotted line carrying boolean control signal to a process.

### 5-Mark Preparation
- 4 Purposes of Modelling (Testing, Communication, Visualization, Complexity reduction).
- 4 Principles of Modelling (Choice of model, Precision levels, Connected to reality, Multiple views).
- 4 Steps of Object-Oriented Design (System Analysis, System Design, Object Design, Implementation).
- Link vs Association comparison and diagram.

### Long Answer (10/15-Mark) Preparation
- Three OMT Models: Object Model, Dynamic Model, Functional Model (Comparison, diagrams, roles).
- Functional Modeling elements: Data stores, actors, control flow (detailed notes with diagrams).

---

## PART 2 — QUICK REVISION TABLE

| Concept | Key Exam Formula / Core Meaning | Priority |
|---|---|---|
| **Modelling Purposes** | Test early, communicate, visualize, reduce complexity | HIGH |
| **4 Principles of Modelling**| Model choice shapes solution; multiple precision levels; grounded in reality; multiple orthogonal models | HIGH |
| **4 Steps of OOM** | Analysis (*What*) $\rightarrow$ System Design (Architecture) $\rightarrow$ Object Design (Data structs/algos) $\rightarrow$ Implementation (Coding) | HIGH |
| **3 OMT Models** | Object (Static), Dynamic (State/Control), Functional (DFD/Computations) | HIGH |
| **DFD Elements** | Actors (Rectangles), Data Stores (Parallel lines), Control Flow (Dotted boolean) | HIGH |
| **Link vs Association** | Link = Object instance connection; Association = Class relationship | HIGH |

### Self-Test (Part 2)
1. List the 4 principles of modelling.
2. What are the four stages of the OOM process?
3. Differentiate between an Actor and a Data Store in a DFD.
4. Compare the Object Model and the Dynamic Model in OMT.
5. Draw a simple class association and its corresponding object link diagram.

---

# PART 3: Introduction to UML & Architecture

---

## Topic 16 — Introduction to UML (Meaning, Need, Pros & Cons)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12 (5 Marks), AKTU 2012-13 (5 Marks), AKTU 2014-15 (5 Marks), AKTU 2015-16 (2 Marks)

### 1. Simple Meaning
UML (Unified Modeling Language) is a standard visual language used to draw blueprints for software systems. It uses standard symbols (boxes, lines, arrows) so that analysts, developers, and clients all understand the system design clearly.

### 2. One-Line Definition
UML (Unified Modeling Language) is an industry-standard, general-purpose visual modeling language used to specify, visualize, construct, and document the artifacts of a software system.

### 3. Why is UML Required? (Core Tasks)
1. **Visualizing:** Allows developers to see the system structure clearly.
2. **Specifying:** Builds precise, unambiguous models of system requirements and design.
3. **Constructing:** Enables forward engineering (generating code from diagrams) and reverse engineering.
4. **Documenting:** Preserves architectural decisions and design requirements across the project lifecycle.

### 4. Pros and Cons of UML

| Advantages (Pros) | Limitations (Cons) |
|---|---|
| **Wide Acceptance:** Universal standard across the software industry | **Large & Complex:** UML has numerous diagrams and rules that take time to learn |
| **Better Communication:** Bridges gaps between clients, analysts, and developers | **Synchronization Overhead:** Difficult to keep diagrams updated when code changes rapidly |
| **Supports OOAD:** Directly aligns with object-oriented analysis and design methods | **Tool Costs:** Professional UML modeling tools can be expensive |
| **Easy for Non-Programmers:** Visual diagrams are readable without code knowledge | **Limited Detail:** Cannot represent every branching edge case or complex runtime logic |

### 5. What to Remember
- UML = Unified Modeling Language (Standardized visual language).
- Used for: Visualizing, Specifying, Constructing, Documenting.
- It is a **modeling** language, not a programming language.

### 6. AKTU Exam Answer
**Q. What is UML? Why is it required? Discuss its pros and cons.**
1. **Definition:** UML is a standard visual modeling language for visualizing, specifying, constructing, and documenting software system artifacts.
2. **Why Required:** Provides standard blueprints for architecture design, simulation, and multi-tier documentation.
3. **Pros:** Universal industry standard, supports OOAD, understandable by non-programmers.
4. **Cons:** Complex feature set, diagram-to-code synchronization overhead, tool licensing costs.

### 7. Quick Check
1. What does UML stand for?
2. Is UML a programming language?

---

## Topic 17 — Conceptual Model of UML
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12 (5 Marks), AKTU 2012-13 (5 Marks)

### 1. Simple Meaning
Before drawing any UML diagram, you must understand the conceptual rules of the language. The Conceptual Model of UML is made of three key components: the **building blocks**, the **rules** for combining them, and the **common mechanisms**.

### 2. Three Major Elements of the Conceptual Model

```text
                     Conceptual Model of UML
                                 |
     +---------------------------+---------------------------+
     |                           |                           |
1. Building Blocks          2. Rules                    3. Common Mechanisms
  - Things (Structural,       - Names, Scope,             - Specifications
    Behavioral, Grouping,       Visibility, Integrity,      - Adornments
    Annotational)               Execution                   - Common Divisions
  - Relationships                                           - Extensibility
  - Diagrams
```

1. **UML Building Blocks:**
   - **Things:** The basic abstractions (Structural like Class/Component, Behavioral like State/Interaction, Grouping like Package, Annotational like Note).
   - **Relationships:** How things connect (Dependency, Association, Generalization, Realization).
   - **Diagrams:** Collections of things and relationships showing a specific view of the system.
2. **Rules:**
   - Syntactic and semantic rules that define well-formed models (e.g., naming rules, scope, visibility, type integrity).
3. **Common Mechanisms:**
   - Standard conventions used across all diagrams (Specifications, Adornments, Common Divisions such as class vs object, and Extensibility mechanisms like stereotypes and tagged values).

### 3. Example Conceptual / Domain Model (Library System)
```text
  +-------------+ 1       * +-------------+
  |   Library   |-----------|    Item     |
  +-------------+ contains  +-------------+
         | 1                      | 1
         |                        | has_copies
         | has                    | *
         v *                    +-------------+
  +-------------+               |    Copy     |
  |    User     |               +-------------+
  +-------------+                      | *
         | *                           |
         +------------- borrows -------+
```

### 4. What to Remember
- Conceptual Model = Building Blocks + Rules + Common Mechanisms.
- Domain/Conceptual Model represents real-world entities before software implementation.

### 5. AKTU Exam Answer
**Q. Discuss the Conceptual Model of UML with a suitable diagram.**
1. **Definition:** The conceptual model defines the foundational concepts and structural organization of UML.
2. **Three Core Elements:**
   - *Building Blocks:* Things (structural, behavioral, grouping, annotational), Relationships, and Diagrams.
   - *Rules:* Well-formed rules for scope, naming, and consistency.
   - *Common Mechanisms:* Specifications, adornments, common divisions, and extensibility.
3. **Example Diagram:** Draw the simplified Library Conceptual Model (Library, User, Item, Copy) shown above.

### 6. Quick Check
1. What are the three major elements of the UML conceptual model?
2. Give one example of a grouping thing in UML.

---

## Topic 18 — UML Architecture & 4+1 View Model
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2014-15 (5 Marks)

### 1. Simple Meaning
A complex software system cannot be understood from a single perspective. The UML architecture organizes system design into **5 views** (the 4+1 View Model), where four technical views are tied together by user requirements (**Use-Case View**).

### 2. The 4+1 Architectural Views

```text
                       +----------------------+
                       |    Use-Case View     |
                       | (User Requirements)  |
                       +----------------------+
                                  |
         +------------------------+------------------------+
         |                        |                        |
         v                        v                        v
+------------------+     +------------------+     +------------------+
|   Logical View   |     |   Process View   |     | Development View |
| (Class/Structure)|     | (Threads/Perf)   |     | (Code/Packages)  |
+------------------+     +------------------+     +------------------+
                                  |
                                  v
                         +------------------+
                         |  Physical View   |
                         | (Hardware Nodes) |
                         +------------------+
```

1. **Use-Case View (The "+1" Center):**
   - **What it shows:** System functionality from the viewpoint of end users and external actors.
   - **Artifacts:** Use Case Diagrams.
   - **Role:** Drives and validates all other four views.
2. **Logical View:**
   - **What it shows:** The logical structural decomposition of the system (classes, objects, relationships).
   - **Artifacts:** Class Diagrams, Object Diagrams.
3. **Process View:**
   - **What it shows:** Concurrency, runtime processes, threads, synchronization, and system performance.
   - **Artifacts:** Activity Diagrams, Statechart Diagrams.
4. **Development (Implementation) View:**
   - **What it shows:** Organization of actual software modules, packages, source code files, and libraries.
   - **Artifacts:** Component Diagrams, Package Diagrams.
5. **Physical (Deployment) View:**
   - **What it shows:** The mapping of software components onto physical hardware nodes and communication links.
   - **Artifacts:** Deployment Diagrams.

### 3. Four Abstraction Layers of UML Architecture (Meta-model hierarchy)
The underlying architecture of UML itself is organized into 4 distinct conceptual layers:
- **$M_0$ (User Object Layer):** Runtime instances (e.g., `s1: Student`).
- **$M_1$ (Model Layer):** User-defined models and classes (e.g., `class Student`).
- **$M_2$ (Metamodel Layer):** UML language definitions (e.g., `Class`, `Attribute`, `Association`).
- **$M_3$ (Meta-metamodel Layer):** The core infrastructure language defining UML itself (MOF - Meta-Object Facility).

### 4. What to Remember
- 4+1 Architecture = Use-Case (Center) + Logical + Process + Development + Physical.
- Logical = Classes; Process = Threads; Development = Code components; Physical = Hardware nodes.
- Use-Case view ties all four technical views together.

### 5. AKTU Exam Answer
**Q. Explain the Architecture of UML (4+1 View Model).**
1. **Overview:** UML architecture organizes system modeling into 5 interrelated views to address different stakeholder concerns.
2. **The 5 Views:**
   - *Use-Case View:* Defines system behavior from user perspective; connects and drives the other 4 views.
   - *Logical View:* Represents static class structure and domain relationships.
   - *Process View:* Captures concurrency, threading, and runtime performance.
   - *Development View:* Organizes source code modules, packages, and libraries.
   - *Physical View:* Details deployment of components onto hardware nodes.
3. **Diagram:** Draw the 4+1 View architecture diagram above.

### 6. Quick Check
1. Which view connects and validates all other views in the 4+1 architectural model?
2. What does the Physical (Deployment) view represent?

---

# PART 3: EXAM PREPARATION & QUICK REVISION

### 2-Mark Preparation
- **UML:** Unified Modeling Language (Visual language for software blueprints).
- **Four Core UML Tasks:** Visualizing, Specifying, Constructing, Documenting.
- **4+1 Views:** Use-Case, Logical, Process, Development, Physical views.
- **Use-Case View:** Central view representing user requirements.
- **Physical View:** Mapping of software to physical hardware nodes.

### 5-Mark Preparation
- Why UML is required and its Pros & Cons.
- Conceptual Model of UML (Building blocks, rules, common mechanisms + Library example).
- UML 4+1 Architecture views with diagram.

---

## PART 3 — QUICK REVISION TABLE

| Concept | Key Exam Formula / Core Meaning | Priority |
|---|---|---|
| **UML Definition** | Visual modeling language to visualize, specify, construct, document | HIGH |
| **Pros & Cons of UML** | Universal, easy to read vs complex, synchronization overhead | MEDIUM |
| **Conceptual Model** | Building Blocks (Things, Relations, Diagrams) + Rules + Common Mechanisms | HIGH |
| **4+1 Architecture** | Use-Case (Center) drives Logical, Process, Development, Physical views | HIGH |
| **4 UML Layers** | $M_0$ (Instance) $\rightarrow$ $M_1$ (Model) $\rightarrow$ $M_2$ (Metamodel) $\rightarrow$ $M_3$ (Meta-metamodel) | MEDIUM |

### Self-Test (Part 3)
1. Name the four major tasks UML helps developers accomplish.
2. What are the three categories of building blocks in UML?
3. List the 5 views of the 4+1 architectural model and state what each shows.
4. Draw a simple conceptual model for a library domain.

---

# OOSD UNIT 1 — MASTER REVISION SHEET

### Master Topic Summary Table

| No. | Topic Name | One-Line Meaning | Exam Priority |
|---|---|---|---|
| 1 | **Object Orientation** | System built as interacting objects bundling data and methods | HIGH |
| 2 | **Elements of OO System** | Objects, classes, attributes, behavior, methods, and messages | MEDIUM |
| 3 | **POP vs OOP** | Function-first/top-down vs Data-first/bottom-up | HIGH |
| 4 | **OOT Pros & Cons** | Reusable and maintainable vs CPU/memory overhead | MEDIUM |
| 5 | **Object Identity** | Unique memory address/ID distinguishing objects independent of values | HIGH |
| 6 | **Encapsulation** | Packaging data + methods into a shell with restricted public access | HIGH |
| 7 | **Information Hiding** | Concealing internal implementation to decouple client code | MEDIUM |
| 8 | **Polymorphism** | Same operation name taking multiple forms (Ad-hoc & Universal) | HIGH |
| 9 | **Generosity** | Type parameterization for reusable generic templates | LOW |
| 10 | **Modelling Purposes** | Abstraction to test early, communicate, visualize, reduce complexity | HIGH |
| 11 | **Principles of Modelling** | Choice shapes solution; levels of precision; grounded in reality; multiple views | HIGH |
| 12 | **Steps of OOM / OOD** | System Analysis $\rightarrow$ System Design $\rightarrow$ Object Design $\rightarrow$ Implementation | HIGH |
| 13 | **3 OMT Models** | Object (Static), Dynamic (State/Control), Functional (Computations) | HIGH |
| 14 | **Functional Elements** | Actors (Sources/Sinks), Data Stores (Storage), Control Flow (Boolean trigger)| HIGH |
| 15 | **Link vs Association** | Link is an object-level instance; Association is a class-level relationship | HIGH |
| 16 | **UML Introduction** | Visual language to visualize, specify, construct, and document software | HIGH |
| 17 | **Conceptual Model of UML**| Building blocks + Rules + Common mechanisms | HIGH |
| 18 | **UML 4+1 Architecture** | Use-Case view integrating Logical, Process, Development, and Physical views | HIGH |

---

## 1. Most Important Definitions to Memorize
1. **Object Orientation:** An approach that models software systems as collections of modular objects combining data and operations.
2. **Object Identity:** The property of an object that distinguishes it from all other objects by a unique internal identifier (memory address), independent of its attributes.
3. **Encapsulation:** The bundling of data with the methods operating on that data, restricting direct external access to internal state.
4. **Polymorphism:** The capability of different objects to respond to the same message with their own class-specific behavior.
5. **Model:** An abstraction of a physical or software system created to understand, test, and design it prior to implementation.
6. **Association vs Link:** An association is a relationship between classes; a link is a concrete instance of an association connecting individual objects.
7. **UML:** Unified Modeling Language, a standard visual modeling language for specifying, visualizing, constructing, and documenting software artifacts.

---

## 2. Key Differences Summary Tables

### Class vs Object
| Feature | Class | Object |
|---|---|---|
| **Nature** | Abstract blueprint / data type | Concrete runtime instance |
| **Memory** | Allocates no runtime data memory | Occupies actual memory space |
| **Example** | `class Student` | `Student s1;` |

### Encapsulation vs Information Hiding
| Feature | Encapsulation | Information Hiding |
|---|---|---|
| **Type** | Programming mechanism / packaging technique | Architectural design principle |
| **Focus** | Binds data + methods into a class shell | Conceals internal algorithms and changeable designs |
| **Means** | Implemented using access specifiers (`private`) | Achieved by leveraging encapsulation |

### Association vs Link
| Feature | Association | Link |
|---|---|---|
| **Level** | Class level (Model blueprint) | Object level (Runtime instance) |
| **Shows** | General relationship & multiplicities (`*`, `1`) | Specific connections between objects |
| **Diagram** | Class Diagram | Object Diagram |

---

## 3. Core C++ Code Patterns for Unit 1

```cpp
#include <iostream>
using namespace std;

// 1. Class, Encapsulation & Information Hiding
class BankAccount {
private:
    double balance; // Encapsulated data
public:
    BankAccount(double b = 0) : balance(b) {}
    void deposit(double amt) { if (amt > 0) balance += amt; }
    double getBalance() { return balance; }
};

// 2. Inheritance & Subtype Polymorphism
class Animal {
public:
    virtual void speak() { cout << "Animal sound" << endl; } // Virtual function
};

class Dog : public Animal {
public:
    void speak() override { cout << "Dog barks" << endl; }
};

// 3. Generosity (C++ Template)
template <typename T>
T getMaximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    // Identity demonstration
    BankAccount acc1(500), acc2(500); // Same values, different addresses (&acc1 != &acc2)

    // Polymorphism demonstration
    Animal* myPet = new Dog();
    myPet->speak(); // Output: Dog barks

    delete myPet;
    return 0;
}
```

---

## 4. Authentic Exam Questions (From Uploaded Material)

### Previous Year Questions (PYQs from Uploaded Material)
- **AKTU 2010-11:**
  - Describe steps of object-oriented design. (5 Marks)
  - What do you mean by encapsulation? How does message passing help encapsulate implementation? (5 Marks)
  - Define polymorphism. Is this concept only applicable to OO systems? (5 Marks)
  - What do you understand by architectural modeling? (5 Marks)
- **AKTU 2011-12:**
  - What do you understand by object-oriented technology? Discuss pros and cons. (10 Marks)
  - What do you mean by modeling? Discuss purposes served by models with examples. (5 Marks)
  - Write short note on dynamic modeling and functional modeling. (5 Marks)
  - What do you mean by UML? Discuss conceptual model of UML with example. (5 Marks)
  - Wire characteristics question: Filament of bulb vs Airplane electrical system. (5 Marks)
- **AKTU 2012-13:**
  - Describe features of object-oriented languages. (5 Marks)
  - Compare procedural programming with object-oriented programming. (5 Marks)
  - Define link and association with suitable example. (5 Marks)
  - Describe pros and cons of UML. (5 Marks)
- **AKTU 2013-14:**
  - What do you understand by object identity? Explain with example. (5 Marks)
  - What are the principles of modeling? What is the importance of modeling? (5 Marks)
- **AKTU 2014-15:**
  - Basic principles of modeling in detail. (5 Marks)
  - Why is UML required? What is the basic architecture of UML? (5 Marks)
- **AKTU 2015-16:**
  - Write short notes on: (a) Data store, (b) Actors, (c) Control flow. (15 Marks)
  - What do you mean by OMT? Discuss various stages of OMT with example. (10 Marks)
  - What is UML? (2 Marks)

---

# 30-MINUTE OOSD UNIT 1 REVISION PLAN

- **00 – 05 min (Core OOP Ideas):**
  - Revise Object Identity (memory address $\neq$ values).
  - Revise Encapsulation (data + methods shell) and Information Hiding.
  - Revise POP vs OOP table.
- **05 – 10 min (Polymorphism & Generosity):**
  - Revise Polymorphism definition: Ad-hoc (overloading) vs Universal (parametric/subtyping).
  - Remember: Ad-hoc works in procedural too; subtype polymorphism requires virtual functions.
  - Recall Generosity = Templates/Generics.
- **10 – 15 min (Modelling & 4 Principles):**
  - 4 Purposes of modelling: Test early, Customer communication, Visualization, Complexity reduction.
  - 4 Principles: Choice shapes solution, Levels of precision, Connected to reality, Multiple independent models.
- **15 – 20 min (OOM Steps & 3 OMT Models):**
  - 4 Steps of OOM: Analysis $\rightarrow$ System Design $\rightarrow$ Object Design $\rightarrow$ Implementation.
  - 3 OMT Models: Object Model (Class diagram), Dynamic Model (Statechart), Functional Model (DFD).
  - DFD Elements: Actors (rectangles), Data Stores (parallel lines), Control Flow (dotted boolean lines).
- **20 – 25 min (Link & Association + UML Basics):**
  - Association = Class relationship; Link = Object instance connection.
  - UML Definition: Visual language to visualize, specify, construct, document.
  - Pros and Cons of UML.
- **25 – 30 min (Conceptual Model & 4+1 Architecture):**
  - UML Conceptual Model: Building blocks (Things, Relationships, Diagrams) + Rules + Common Mechanisms.
  - UML 4+1 Architecture: Use-Case view in center driving Logical, Process, Development, and Physical views.

---

# 10-MINUTE LAST-MOMENT REVISION

1. **Object Identity:** Unique internal ID/memory address (`&object`). Value equality does not mean identity equality.
2. **Encapsulation:** Bundling data and methods; access only via public methods; message passing protects internal state.
3. **POP vs OOP:** POP is Top-down/function-first; OOP is Bottom-up/data-first with access specifiers.
4. **Polymorphism:** Same interface, different behavior. Ad-hoc (overloading) + Universal (templates / virtual functions).
5. **4 Principles of Modelling:** Model choice shapes solution; Multiple precision levels; Connected to reality; Multiple independent models.
6. **4 Steps of OOM:** Analysis (What) $\rightarrow$ System Design (Architecture) $\rightarrow$ Object Design (Data structs/algorithms) $\rightarrow$ Implementation (Code).
7. **3 OMT Models:** Object (Static / Class Diagram), Dynamic (Temporal / State Diagram), Functional (Computation / DFD).
8. **DFD Elements:** Actor (Rectangle - Source/Sink), Data Store (Parallel lines - Passive), Control Flow (Dotted arrow - Boolean trigger).
9. **Link vs Association:** Association is between Classes; Link is between Objects.
10. **UML 4+1 Views:** Use-Case (Requirements/Center), Logical (Classes), Process (Concurrency/Threads), Development (Code packages), Physical (Hardware deployment nodes).
