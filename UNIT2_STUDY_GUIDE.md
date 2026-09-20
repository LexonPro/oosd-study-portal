# OOSD Unit 2 — Complete Study Notes (AKTU KCS-054)
## Basic Structural, Behavioral & Architectural Modeling

---

# PART 1: Basic Structural Modeling & Relationships

---

## Topic 1 — Types of Modeling in UML (Structural vs Behavioral vs Architectural)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2013-14 (5 Marks)

### A. Simple Meaning
When modeling a software system with UML, we view the system from three distinct angles: what the system is made of (Structural), how the components interact dynamically (Behavioral), and how the overall software and hardware are organized (Architectural).

### B. One-Line Definition
UML divides system modeling into three primary categories: Structural (static framework), Behavioral (dynamic interactions and state changes), and Architectural (high-level blueprint of software components and physical deployment).

### C. Easy Real-Life Example
Think of constructing a **Car**:
- **Structural:** The chassis, engine parts, wheels, and wiring diagram (static parts).
- **Behavioral:** Fuel combustion, pressing the brake pedal, gear shifting (how parts interact over time).
- **Architectural:** How the car connects to the road, fuel station networks, and embedded electronic control units (deployment topology).

### D. Technical Example
- **Structural:** Class Diagram, Object Diagram.
- **Behavioral:** Use Case Diagram, Sequence Diagram, State Machine Diagram.
- **Architectural:** Component Diagram, Deployment Diagram, Package Diagram.

### E. Simple Diagram
```text
                          UML Modeling Types
                                  |
     +----------------------------+----------------------------+
     |                            |                            |
[Structural Modeling]        [Behavioral Modeling]       [Architectural Modeling]
- Static features            - Dynamic interactions      - Overall system framework
- Class, Object diagrams     - Sequence, Statecharts     - Component, Deployment
```

### F. Comparison Table

| Modeling Type | Primary Purpose | Key Diagrams | Focus |
|---|---|---|---|
| **Structural** | Captures static skeleton/elements | Class, Object Diagrams | What elements exist |
| **Behavioral** | Captures dynamic actions and states | Use Case, Sequence, State, Activity | How elements interact |
| **Architectural**| Captures system topology and deployment | Component, Deployment, Package | How software sits on hardware |

### G. Key Points
- Structural models never describe dynamic behavior.
- Behavioral models describe time-sequenced interactions and object state transitions.
- Architectural models combine structural and physical deployment elements.

### H. Exam Answer
**Q. Explain different types of modeling in Object-Oriented System Design.**
1. **Structural Modeling:** Captures the static building blocks and relationships of the system (Class and Object diagrams).
2. **Behavioral Modeling:** Describes the dynamic behavior, message interactions, workflows, and state transitions over time (Sequence, Activity, State Machine, and Use Case diagrams).
3. **Architectural Modeling:** Represents the high-level organization, packaging, runtime components, and hardware deployment topology (Component and Deployment diagrams).

### I. Quick Check
1. Which modeling type captures the static features of a system?
2. Which category does a Sequence Diagram belong to?

---

## Topic 2 — Relationships in UML (Dependency, Association, Generalization, Realization)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2011-12, 2012-13 (5 Marks)

### A. Simple Meaning
Classes and objects do not exist in isolation. Relationships describe how different model elements connect, share data, inherit behavior, or depend on one another.

### B. One-Line Definition
A UML relationship is a semantic connection between model elements that defines structural, behavioral, or dependency links within a software architecture.

### C. The Four Core UML Relationships

```text
1. Dependency:      Client -----------> Supplier (dashed arrow)
2. Association:     ClassA ------------ ClassB (solid line)
3. Generalization:  Child  ----------—▷ Parent (solid line with hollow triangle)
4. Realization:     Class  - - - - - -▷ Interface (dashed line with hollow triangle)
```

1. **Dependency (`- - - ->`):**
   - A using relationship where a change in one element (supplier) affects another (client).
   - *Example:* A `PrinterService` depends on a `Document` parameter passed into a method.
2. **Association (`——`):**
   - A structural relationship describing links between objects with multiplicity (`1`, `*`, `0..1`).
   - *Example:* A `Student` enrolls in a `Course`.
3. **Generalization (`——▷`):**
   - An inheritance relationship connecting a subclass to a generalized superclass ("is-a" relationship).
   - *Example:* `Car` is a kind of `Vehicle`.
4. **Realization (`- - - ▷`):**
   - A relationship where a class implements the operations specified by an interface.
   - *Example:* `MySQLDatabase` realizes the `DatabaseDriver` interface.

### D. Simple C++ Example
```cpp
#include <iostream>
using namespace std;

// 1. Generalization (Inheritance)
class Vehicle {
public:
    void start() { cout << "Vehicle started" << endl; }
};

class Car : public Vehicle { // Car "is-a" Vehicle
public:
    void drive() { cout << "Car driving" << endl; }
};

int main() {
    Car myCar;
    myCar.start();
    myCar.drive();
    return 0;
}
```

### E. What to Remember
- Dependency = Uses a (`- - ->`).
- Association = Has a / Related to (`——`).
- Generalization = Is a (`——▷`).
- Realization = Implements interface (`- - -▷`).

### F. AKTU Exam Answer
**Q. Explain relationships and their types in UML.**
- Define relationship as a semantic connection between model elements.
- Detail the 4 notations:
  1. *Dependency:* Dashed arrow; change in independent element impacts dependent element.
  2. *Association:* Solid line; structural connection with multiplicity.
  3. *Generalization:* Solid line with hollow arrowhead; represents inheritance hierarchy.
  4. *Realization:* Dashed line with hollow arrowhead; represents class implementing an interface contract.

### G. Quick Check
1. Which arrow notation represents generalization in UML?
2. What does a dashed arrow indicate in UML?

---

## Topic 3 — Generalization, Specialization, and Aggregation
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2011-12, 2012-13 (5 Marks)

### A. Simple Meaning
- **Generalization:** Taking common features from specific classes and creating a general parent class (bottom-up).
- **Specialization:** Taking a general class and creating specific child classes with added features (top-down).
- **Aggregation:** A "part-of" relationship where a whole object is composed of smaller parts, but the parts can exist independently.

### B. Definitions
- **Generalization:** An "is-a-kind-of" relationship where subclasses share attributes and operations of a higher-level superclass.
- **Specialization:** The reverse of generalization, creating specialized subclasses from a broader superclass.
- **Aggregation:** A specialized association representing a "has-a" or "part-of" relationship between a composite whole and its components (represented by a hollow diamond `◇`).

### C. Simple Diagram
```text
           [Vehicle Superclass]          <--- Generalization (Bottom-up)
                   |
     +-------------+-------------+
     |                           |
[LandVehicle]               [WaterVehicle]
     |                           |
   [Car]                       [Ship]    <--- Specialization (Top-down)

Aggregation:
[House] ◇-------- [Door]
        ◇-------- [Window]
```

### D. Relationship Classification Practice (From Uploaded Material)
1. **"A country has a capital city":**
   - *Classification:* **Association** (or Aggregation). Country and City are distinct independent entities; a city is located in and associated with a country.
2. **"Files contain records":**
   - *Classification:* **Aggregation**. Records are constituent parts contained inside a file; operations on the file propagate to its records.

### E. Key Points
- Generalization = Specific to Generic ("is-a").
- Specialization = Generic to Specific.
- Aggregation = Whole-Part ("has-a", hollow diamond `◇`).
- Composition = Strong whole-part where parts cannot exist without the whole (filled diamond `◆`).

### F. AKTU Exam Answer
**Q. Define Generalization, Specialization, and Aggregation.**
1. **Generalization:** Bottom-up process of combining common attributes and methods of multiple classes into a common superclass ("is-a-kind-of" hierarchy).
2. **Specialization:** Top-down process of deriving specialized subclasses from an existing parent class with additional distinctive behaviors.
3. **Aggregation:** A "has-a" association where a complex object is made of constituent parts (e.g., a House composed of Rooms and Roofs).

### G. Quick Check
1. Is generalization a top-down or bottom-up modeling process?
2. What symbol is used to represent aggregation in UML?

---

## Topic 4 — UML Extensibility Mechanisms (Stereotypes, Tagged Values, Constraints)
**Exam Priority:** MEDIUM

### A. Simple Meaning
UML provides built-in extension mechanisms so developers can customize or add new semantics, properties, and rules to UML diagrams without altering the core language standard.

### B. The 3 Extensibility Mechanisms

```text
1. Stereotype:    <<interface>>, <<utility>>, <<broadcast>> (Extends vocabulary)
2. Tagged Value:  {author = "Aman", version = 2.0}          (Extends properties)
3. Constraint:    {balance >= 0}, {ordered}                 (Extends rules/logic)
```

1. **Stereotypes (`<<name>>`):**
   - Extends UML vocabulary by creating new building blocks derived from existing ones.
   - *Notation:* Guillemets `<< >>`.
   - *Example:* `<<interface>>`, `<<actor>>`, `<<signal>>`.
2. **Tagged Values (`{key = value}`):**
   - Extends properties of a UML element by attaching arbitrary metadata or documentation.
   - *Notation:* Curly braces `{tag = value}`.
   - *Example:* `{author = "Rahul", version = 1.2, priority = 3}`.
3. **Constraints (`{rule}`):**
   - Extends semantics by specifying conditions or assertions that must hold true.
   - *Notation:* Curly braces `{condition}`.
   - *Example:* `{lateCharge = daysOverdue * 5}`, `{ordered}`.

### C. What to Remember
- Stereotype = New model element type (`<< >>`).
- Tagged value = New property/metadata (`{key = value}`).
- Constraint = New business rule or boundary (`{condition}`).

### D. AKTU Exam Answer
**Q. Explain UML Extensibility Mechanisms.**
- Define extensibility as UML's mechanism for extending language syntax and semantics.
- List and explain the 3 tools:
  1. *Stereotypes (`<< >>`):* Introduces new domain-specific building block categories.
  2. *Tagged Values (`{ }`):* Adds new metadata key-value properties.
  3. *Constraints (`{ }`):* Adds formal conditions, rules, or boundary equations.

### E. Quick Check
1. Which extensibility mechanism uses guillemets `<< >>`?
2. How do you represent a constraint on a UML class attribute?

---

# PART 2: Class Diagrams & Object Diagrams

---

## Topic 5 — Class Diagrams (Terms, Concepts & Modeling Techniques)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12, 2012-13, 2013-14 (5 Marks)

### A. Simple Meaning
A class diagram is the primary structural blueprint in software engineering. It shows the static structure of a system by displaying its classes, attributes, operations, and relationships.

### B. One-Line Definition
A Class Diagram is a static structural UML diagram that describes the structure of a system by showing its classes, attributes, operations, and static relationships.

### C. Standard 3-Compartment Class Notation
```text
+-----------------------------------+
|            ClassName              |  <--- Top: Class Name
+-----------------------------------+
| - attribute1: Type                |  <--- Middle: Attributes (Data)
| - attribute2: Type = defaultValue |
+-----------------------------------+
| + operation1(param: Type): Return |  <--- Bottom: Operations (Methods)
| + operation2()                    |
+-----------------------------------+
Visibility Notations:
  '+' = public, '-' = private, '#' = protected, '~' = package
```

### D. Class Diagram Example (Party Composition Hierarchy)
```text
               +----------------------+
               |        Party         |
               +----------------------+
               | - location: String   |
               +----------------------+
                          ^
            --------------+--------------
            |                           |
  +--------------------+     +--------------------+
  |       Person       |     |    Organization    |
  +--------------------+     +--------------------+
  | - name: String     |     | - orgId: String    |
  +--------------------+     +--------------------+
```

### E. Key Points
- Represents the static view of the system.
- Direct mapping to object-oriented code (C++, Java).
- Contains classes, interfaces, associations, aggregations, generalizations, and constraints.

### F. Quick Check
1. What are the three compartments of a standard UML class box?
2. What does the `#` prefix indicate for an attribute?

---

## Topic 6 — Object (Instance) Diagrams & Comparison with Class Diagrams
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12, 2012-13 (10 Marks)

### A. Simple Meaning
An object diagram shows a concrete snapshot of a running system at one specific instant in time. It displays real object instances and the links connecting them.

### B. One-Line Definition
An Object Diagram is a structural diagram that captures a static snapshot of individual runtime object instances and their data attribute values at a specific point in execution.

### C. Comparison: Class Diagram vs Object (Instance) Diagram

| Feature | Class Diagram | Object (Instance) Diagram |
|---|---|---|
| **Nature** | Abstract schema / blueprint | Concrete runtime snapshot |
| **Element Shown** | Classes (`ClassName`) | Objects (`objectName: ClassName` underlined)|
| **Data Shown** | Attribute declarations and types | Specific assigned attribute values |
| **Relationships** | Associations with general multiplicities | Concrete links between instances |
| **Lifecycle** | Remains constant over system lifecycle | Changes from moment to moment |
| **Notation** | Rectangular box with plain title | Rectangular box with **underlined** name |

### D. Simple Diagram (Class vs Instance)
```text
Class Diagram:                        Object Diagram (Instance Snapshot):
+--------------------+                +------------------------------------+
|      Student       |                |           s1: Student              |
+--------------------+                +------------------------------------+
| - rollNo: int      |                | rollNo = 101                       |
| - name: String     |                | name = "Aman"                      |
+--------------------+                +------------------------------------+
```

### E. Domain Class Modeling Examples (From Uploaded Material)

#### 1. Newspaper Layout System:
- *Expected Classes:* `Page`, `Column`, `Line`, `Headline`, `Paragraph`, `Picture`.

#### 2. Catalog Store Order Entry System:
- *Expected Classes:* `Customer`, `Order`, `OrderItem`, `Store`, `CatalogItem`.

#### 3. Family Tree Class Diagram from Instance Diagram:
```text
               +--------------------+
               |       Person       |
               +--------------------+
               | - name: String     |
               +--------------------+
                  | 0..1 (husband)
                  | 0..1 (wife)
               [Mate]
                  |
                  | 2 (parents)
                  v
               * (children)
```

### F. AKTU Exam Answer
**Q. Differentiate between a Class Diagram and an Instance Diagram with examples.**
1. **Class Diagram:** Defines the general schema, attributes, methods, and associations of a system. Exists as an abstract model.
2. **Instance (Object) Diagram:** Captures a point-in-time runtime snapshot showing concrete objects, exact variable values, and physical links.
3. Draw the comparison table and the `Student` class vs `s1:Student` instance box above.

### G. Quick Check
1. How is an object's name formatted inside an object diagram box?
2. Which diagram is used to document specific test cases or scenarios?

---

# PART 3: Collaboration (Communication) Diagrams

---

## Topic 7 — Collaboration Diagrams (Terms, Concepts & Depicting Messages)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2011-12, 2013-14 (5 Marks)

### A. Simple Meaning
A collaboration diagram (called a **Communication Diagram** in modern UML) shows how objects interact by passing numbered messages along structural links, emphasizing the structural layout of objects.

### B. One-Line Definition
A Collaboration Diagram is an interaction diagram that illustrates structural connections and dynamic interactions among objects using numbered message arrows along links.

### C. Key Elements
1. **Objects:** Rectangles containing `objectName: ClassName`.
2. **Actors:** External entities initiating the interaction.
3. **Links:** Solid lines connecting objects along which messages can travel.
4. **Messages:** Numbered arrows above/below links indicating calling order and direction (e.g., `1: verify()`, `2: process()`).

### D. Simple Diagram
```text
  [Actor: Clerk] ------ 1: getTotalPay() ------> [ :MonthlyPayPrint ]
                                                          |
                                           2: calculatePay()
                                                          v
                                               [ :FullTimeEmployee ]
```

### E. What to Remember
- Emphasizes **object organization** and structural layout.
- Uses **sequence numbers** on message arrows to indicate time ordering.
- Semantically equivalent to Sequence Diagrams.

### F. Quick Check
1. What does the number prefix on a message arrow indicate?
2. What is another name for a collaboration diagram?

---

## Topic 8 — Polymorphism, Iterated Messages & Self Messages in Collaboration Diagrams
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2011-12, 2013-14 (5 Marks)

### A. Polymorphism in Collaboration Diagrams
- Polymorphism allows a sender object to dispatch the exact same message signature (e.g., `calculatePay()`) to different receiver objects without needing to know their specific derived classes.
- *Classic Example (Employee Payroll):*
  - Caller `MonthlyPayPrint` sends `calculatePay()` to:
    - `:FullTimeEmployee` (computes salary based on grade).
    - `:PartTimeEmployee` (computes salary based on hours worked).
    - `:TemporaryEmployee` (computes salary without pension deductions).

### B. Iterated and Conditional Messages
1. **Iterated Messages (`*`):**
   - Represents a message that runs repeatedly in a loop.
   - *Notation:* Sequence number prefixed with `*` or an iteration expression (e.g., `* [i := 1..n]: calculate()`).
2. **Conditional Messages (`[condition]`):**
   - The message is executed only if a guard condition evaluates to true.
   - *Notation:* `1.1 [balance >= amount]: withdraw(amount)`.

### C. Self Messages (Use of Self)
- An object can invoke its own internal private operations by sending a message to itself.
- *Notation:* A message arrow looping from an object box back to the same object box.

### D. Simple Diagram
```text
             +-----------------------+
             |   MonthlyPayPrint     |
             +-----------------------+
               |        |         |
  2a: calcPay()|        |2b: calcPay()  | 2c: calcPay()
               v        v         v
         [ :FullTime ] [ :PartTime ] [ :TempEmployee ]

Self-Message:
       +------------------+
       |   :OrderManager  | <----+
       +------------------+      | 1.1: validateOrder()
               |                 |
               +-----------------+
```

### E. AKTU Exam Answer
**Q. Explain Polymorphism, Iterated Messages, and Use of Self in Collaboration Diagrams.**
1. **Polymorphism:** A client object sends a uniform message signature to multiple polymorphic supplier objects without knowing their internal calculation logic.
2. **Iterated Messages:** Message sequence numbers prefixed with `*` or loop conditions to show repetitions.
3. **Use of Self:** An object sending a message to itself, depicted by a reflexive loop arrow to invoke internal routines.

### F. Quick Check
1. What symbol is used to denote an iterated message in a collaboration diagram?
2. How is a self-message graphically drawn?

---

# PART 4: Sequence Diagrams & Advanced Interaction Mechanisms

---

## Topic 9 — Sequence Diagrams (Terms, Concepts & Symbols)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12, 2013-14 (10 Marks)

### A. Simple Meaning
A Sequence Diagram is an interaction diagram that shows how objects talk to each other step-by-step, ordered strictly from **top to bottom along a vertical time axis**.

### B. One-Line Definition
A Sequence Diagram is an interaction diagram that emphasizes the chronological, time-ordered sequence of message exchanges among interacting object lifelines.

### C. Core Terms and Symbols
1. **Participant / Object:** Top rectangle labeled `object: Class`.
2. **Lifeline:** Vertical dashed line extending downward from an object representing its existence over time.
3. **Activation Bar (Focus of Control):** Thin vertical rectangle on a lifeline showing when the object is actively executing a task.
4. **Synchronous Message (`——▶` solid arrowhead):** Sender pauses and waits for the operation to complete and return.
5. **Asynchronous Message (`——>` open/half arrowhead):** Sender dispatches the message and immediately continues executing without waiting.
6. **Return Message (`- - - >` dashed arrow):** Data returned to caller from a synchronous call.
7. **Object Destruction (`<<destroy>>` / `X`):** The lifeline ends with a large 'X' when the object is deallocated from memory.

### D. Simple Diagram
```text
   Caller: Client                  Server: Database
         |                                |
         | --- 1: queryData() ---------> | [Activation]
         |                                |
         | < - - - 2: returnResult - - - |
         |                                |
         | --- 3: closeConnection() ---> |
         |                                X (Destroyed)
```

### E. Comparison: Sequence vs Collaboration Diagram

| Feature | Sequence Diagram | Collaboration Diagram |
|---|---|---|
| **Primary Focus** | Explicit time ordering (top-to-bottom) | Structural layout of objects and links |
| **Time Representation**| Vertical Y-axis | Numbered sequence labels (`1`, `1.1`, `2`) |
| **Object Layout** | Horizontal X-axis | Freeform 2D layout |
| **Best Used For** | Complex multi-step chronological flows | Visualizing structural object relationships |

### F. Quick Check
1. Which axis represents time in a sequence diagram?
2. What symbol represents the termination of an object's lifeline?

---

## Topic 10 — Asynchronous Messages, Priority Queues, Broadcast & Callback Mechanisms
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2011-12, 2012-13, 2013-14 (10 Marks)

### A. Asynchronous Messages (With & Without Priority)
1. **Without Priority:**
   - The sender dispatches a message with an open arrowhead (`——>`) and continues working concurrently.
   - *Example (Door Entry System):* `holdOpen()` triggers concurrent operations: `doorPlayer.operate()` (plays audio) and `doorSign.operate()` (lights sign) in parallel.
2. **With Priority:**
   - In concurrent systems, incoming messages land in prioritized queues (High, Medium, Low).
   - *Notation:* Annotated with tagged property `{priority = n}`. The target object processes high-priority messages before low-priority ones.

### B. Broadcast Messages (`<<broadcast>>`)
- A single event is sent to **all objects in the system** simultaneously.
- *Notation:* Stereotype `<<broadcast>>` on the message arrow to a general `:(Object)` class.
- *Example:* Emergency system shutdown signal or a `StartUpSequencer` broadcasting `load()` to all active subsystems.

### C. Callback Mechanism
- A subscriber registers its interest in a future event with a listener. When the event occurs, the listener "calls back" the subscriber.
- *Workflow:*
  1. `userSession` sends `registerNewEMailEvent(urgencyThreshold)` to `EMailListener`.
  2. `userSession` continues running without blocking.
  3. When an urgent email arrives, `EMailListener` asynchronously invokes `newEMailReceived(urgency)` on `userSession`.

### D. Simple Sequence Diagrams
```text
Asynchronous with Priority:
  [Sender] --------- transmitMsg() {priority = 1} --------> [Target: Port]

Callback Pattern:
  userSession: Session               eMailListener: EMailListener
        |                                       |
        | --- 1: registerNewEMailEvent() -----> |  (Subscriber registers)
        |                                       |
        | [userSession continues work...]      |  (Monitors in background)
        |                                       |
        | <--- 2: newEMailReceived() ---------- |  (Callback triggered!)
        |                                       |
```

### E. AKTU Exam Answer
**Q. Discuss the significance of Sequence Diagrams. Explain (i) Asynchronous messages with/without priority, (ii) Broadcast messages, (iii) Callback mechanism.**
1. **Significance:** Sequence diagrams validate runtime scenarios and visualize concurrent workflows along a chronological axis.
2. **Asynchronous Messages:** Half-arrow line; allows non-blocking execution. When prioritized, tagged with `{priority = k}` and queued into parallel priority buffers.
3. **Broadcast Message:** Stereotyped with `<<broadcast>>` to dispatch an event to all existing system objects.
4. **Callback Mechanism:** Event subscription pattern where a listening object notifies the registered caller asynchronously when an event condition is satisfied.

### F. Quick Check
1. How is an asynchronous message visually distinguished from a synchronous one?
2. In a callback mechanism, what does the subscriber object send first?

---

# PART 5: Basic Behavioral Modeling

---

## Topic 11 — Use Case Diagrams & Utility in System Design
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2013-14, 2014-15 (5 Marks)

### A. Simple Meaning
A Use Case Diagram captures what the system does from the viewpoint of outside users (actors). It specifies user requirements without revealing internal software algorithms.

### B. One-Line Definition
A Use Case Diagram is a behavioral UML diagram that models system functionality by depicting interactions between external actors and distinct use cases within a system boundary.

### C. Key Elements
1. **Actor (Stick Figure):** An external user or external system that interacts with the application.
2. **Use Case (Ellipse):** A complete unit of meaningful business functionality provided to an actor.
3. **System Boundary (Rectangle Box):** The boundary separating the internal system from external actors.
4. **Relationships:**
   - **Association (`——`):** Connects an actor to a use case.
   - **`<<include>>` (`- - ->`):** Mandatory shared sub-task (e.g., `Order` includes `ValidatePayment`).
   - **`<<extend>>` (`- - ->`):** Optional behavior triggered under specific conditions (e.g., `Order` extended by `ApplyDiscount`).

### D. Simple Diagram (Vending Machine System)
```text
+-------------------------------------------------------+
|                   Vending Machine                     |
|                                                       |
|   (( Buy Beverage )) <------------------ Customer     |
|           ^                                           |
|           |                                           |
|   (( Load Items )) <-------------------- Stock Clerk  |
|                                                       |
|   (( Scheduled Maintenance )) <--------- Technician   |
|                                                       |
|   (( Make Repairs )) <------------------ Technician   |
+-------------------------------------------------------+
```

### E. Utility of Use Case Diagrams in System Design
1. Gathers high-level functional requirements from users.
2. Defines system boundaries and external interfaces.
3. Serves as the basis for test case generation and user acceptance testing.
4. Drives the construction of all other UML design models (in the 4+1 View Model).

### F. AKTU Exam Answer
**Q. What is a Use Case Diagram? Explain its utility in system design with an example.**
- Define Use Case Diagram (Actors + Use cases inside system boundary).
- Draw the Vending Machine diagram above.
- List 4 utilities: Requirements capture, scope definition, basis for test cases, and communication with non-technical stakeholders.

### G. Quick Check
1. Does an actor reside inside or outside the system boundary?
2. What is the difference between `<<include>>` and `<<extend>>`?

---

## Topic 12 — Activity Diagrams
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2014-15 (5 Marks)

### A. Simple Meaning
An activity diagram is essentially an advanced object-oriented flowchart. It shows the step-by-step workflow of activities, including branching decisions and parallel concurrent operations.

### B. One-Line Definition
An Activity Diagram is a behavioral UML diagram that depicts dynamic workflows, sequential activities, decision branches, and concurrent execution paths within a system.

### C. Core Notations
1. **Initial State (Start):** Solid filled black circle `●`.
2. **Activity State:** Rounded rectangle representing an action.
3. **Transition Arrow:** Direction of flow between activities.
4. **Decision / Merge Diamond (`◇`):** Guarded alternate branches (`[yes]`, `[no]`).
5. **Fork and Join Bars (Solid Horizontal/Vertical Bar):**
   - **Fork:** One incoming flow splits into multiple parallel concurrent flows.
   - **Join:** Multiple parallel flows synchronize into a single outgoing flow.
6. **Final State (End):** Bullseye symbol (solid circle inside an outer ring `⦿`).

### D. Simple Diagram
```text
        ● (Initial State)
        |
        v
  [ Enter Details ]
        |
        v
       / \
      /   \  [valid]
     <     > -----------> [ Process Payment ]
      \   /                      |
       \ /                       v
        | [invalid]       [ Print Receipt ]
        v                        |
  [ Show Error ]                 |
        |                        |
        +------------> ⦿ (Final State)
```

### E. What to Remember
- Initial State = `●`.
- Final State = `⦿`.
- Decision Diamond = `◇`.
- Fork/Join Bar = Parallel execution split / synchronization.

### F. Quick Check
1. What does a solid filled circle represent in an activity diagram?
2. What is the role of a Fork bar in an activity diagram?

---

## Topic 13 — State Machine Diagrams & Telephone Call Lifecycle
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2014-15 (5 Marks)

### A. Simple Meaning
A state machine diagram shows the different states an individual object passes through during its lifetime in response to external events.

### B. One-Line Definition
A State Machine Diagram models the dynamic lifecycle of a single object by showing its states, state transitions, and responses to discrete events.

### C. Key Elements
1. **State (Rounded Box):** A condition or situation in the life of an object (e.g., `Idle`, `Dialing`, `Connected`).
2. **Event / Trigger:** An occurrence that causes a transition (e.g., `liftReceiver`, `digit(n)`).
3. **Transition Arrow (`——>`):** Movement from source state to target state.
4. **Guard Condition (`[condition]`):** Boolean condition required for transition.
5. **Action (`/action`):** Executable computation performed during transition.

### D. State Machine Diagram: Telephone Call Lifecycle (Classic AKTU Question)
```text
  ● (Start)
  |
  v
[ Idle ] -------- liftReceiver --------> [ Dial Tone ]
                                              |
                                           digit(n)
                                              v
[ Ringing ] <------- validNumber ------- [ Dialing ]
    |                                         |
    | receiverAnswers                         | invalidNumber
    v                                         v
[ Connected ]                           [ Recorded Message ]
    |                                         |
    | callerHangsUp                           | timeout
    v                                         v
[ Disconnected ] ----------------------> ⦿ (End)
```

### E. AKTU Exam Answer
**Q. Define State Machine. Draw a state machine diagram for answering a telephone call.**
1. **Definition:** A state machine diagram specifies the sequence of states an object goes through in response to events throughout its lifetime.
2. **Elements:** States, Initial/Final pseudo-states, Transitions, Events, Actions.
3. Draw the complete Telephone Call state transition diagram above.

### F. Quick Check
1. Does a state machine diagram model the entire system or a single object?
2. What is the syntax of a transition label? (`event [guard] / action`)

---

## Topic 14 — Events and Signals (Signal, Time, and Change Events)
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2014-15 (5 Marks)

### A. Simple Meaning
An event is an instantaneous occurrence in time that triggers a reaction or state transition in an object.

### B. The 3 Most Common Types of Events

```text
1. Signal Event:  <<signal>> TrainDeparture(trainNo, time)  (Explicit message)
2. Time Event:    after(30 seconds), when(date = Jan 1)     (Time elapsed/reached)
3. Change Event:  when(temperature > 100)                   (Boolean condition met)
```

1. **Signal Event:**
   - The sending or receiving of an explicit named asynchronous signal from one object to another.
   - *Notation:* Stereotype `<<signal>>` with attributes.
   - *Example:* `<<signal>> TrainDeparture(trainNo, city, date)`.
2. **Time Event:**
   - An event triggered by the passage of a time interval or reaching an absolute timestamp.
   - *Notation:* Keywords `after(...)` or `when(...)`.
   - *Example:* `after(30 seconds)` (timeout) or `when(time = 12:00 PM)`.
3. **Change Event:**
   - An event triggered when a boolean expression continuously evaluated transitions from `false` to `true`.
   - *Notation:* Keyword `when(booleanExpression)`.
   - *Example:* `when(cabinTemperature > maxSafeLimit)`.

### C. What to Remember
- Signal Event = Asynchronous message receipt (`<<signal>>`).
- Time Event = Elapsed time (`after(...)`) or exact clock time (`when(...)`).
- Change Event = State variable boolean check (`when(x > y)`).

### D. AKTU Exam Answer
**Q. What is an Event? Explain the types of events with examples.**
- **Definition:** An event is an instantaneous occurrence in time that triggers state transitions.
- **Three Types:**
  1. *Signal Event:* Receipt of an explicit asynchronous communication object.
  2. *Time Event:* Triggered by elapsed duration (`after 10s`) or absolute date.
  3. *Change Event:* Triggered when a monitored condition becomes true (`when (temp > 80)`).

### E. Quick Check
1. Does an event have duration?
2. Which keyword represents a time interval event?

---

## Topic 15 — Timing Diagrams & Package Diagrams
**Exam Priority:** MEDIUM  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2013-14, 2014-15 (5 Marks)

### A. Timing (Time) Diagrams
1. **Meaning:** A specialized interaction diagram where the primary axis is continuous linear time. It shows exact waveforms of object state changes and duration constraints.
2. **Utility:** Essential in real-time embedded systems, telecommunications, and hardware interface controllers to verify timing requirements (e.g., verifying a signal holds high for at least $30\,\text{ms}$).

### B. Package Diagrams
1. **Meaning:** Structural diagrams used to organize large systems into hierarchical, folder-like modules called **Packages**.
2. **Notation:** Drawn as a tabbed folder box containing a package name.
3. **Utility:** Reduces complexity in large software by grouping related classes, managing dependencies, and establishing high-level architectural namespaces.

### C. Simple Diagram
```text
Package Notation:
+-------------------+
|  OrderProcessing  |
+-------------------+--------------------+
|  - Class Order                         |
|  - Class Payment                       |
|  - Class Invoice                       |
+----------------------------------------+
```

### D. Quick Check
1. What does the tabbed folder icon represent in UML?
2. In which domain are Timing diagrams most useful?

---

# PART 6: Architectural Modeling (Component & Deployment Diagrams)

---

## Topic 16 — Component Diagrams
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2010-11, 2012-13 (5 Marks)

### A. Simple Meaning
A component diagram shows how physical software modules (source code files, DLLs, libraries, executables, databases) fit together using clean plug-and-play interfaces.

### B. One-Line Definition
A Component Diagram is an architectural UML diagram that describes the organization, interfaces, and dependencies among modular software implementation components.

### C. Key Elements
1. **Component (Rectangle with 2 left tabs or `<<component>>` icon):** A modular, replaceable physical piece of software implementing a set of interfaces (e.g., `AuthModule.dll`, `payment_engine.jar`).
2. **Interface (Lollipop `—○` or Box `<<interface>>`):** A collection of operations specifying a contract of services provided or required.
3. **Dependency (`- - ->`):** Shows one component relying on another component's interface.

### D. Simple Diagram
```text
  +------------------+                    +------------------+
  |  OrderController |                    |  PaymentService  |
  +------------------+                    +------------------+
          |                                        |
          | - - - - - - ( IPayment ) <-------------+
         Uses               Realizes (Provides)
```

### E. What to Remember
- Represents the **software implementation view**.
- Focuses on executables, libraries, and code modules.
- Uses interfaces (ball and socket / lollipop notation) for loose coupling.

### F. Quick Check
1. What is a software component in UML?
2. How is a provided interface represented in a component diagram?

---

## Topic 17 — Deployment Diagrams & Difference Between Components and Nodes
**Exam Priority:** HIGH  
**PYQ mentioned in uploaded material:** AKTU 2014-15 (5 Marks)

### A. Simple Meaning
A deployment diagram shows the **hardware topology** of a system—what physical computers, servers, devices, and network links exist, and which software components run on which hardware machines.

### B. One-Line Definition
A Deployment Diagram is an architectural UML diagram that displays the physical configuration of runtime hardware nodes and the software components deployed upon them.

### C. Key Elements
1. **Node (3D 6-sided Box / Cube):** A physical computing resource or device (e.g., `Application Server`, `Database Server`, `Client PC`).
2. **Communication Path (Solid Line):** The network connection protocol linking hardware nodes (e.g., `TCP/IP`, `HTTP/REST`, `PCIe`).
3. **Artifact / Component Deployment:** Software components placed inside the hardware node cube.

### D. Simple Diagram
```text
  +-----------------------+                    +-----------------------+
  |   <<device>> Client   |                    |  <<server>> AppServer |
  |   +---------------+   |                    |   +---------------+   |
  |   |  BrowserApp   |   | ------ HTTP -----> |   |  WebServer    |   |
  |   +---------------+   |                    |   +---------------+   |
  +-----------------------+                    +-----------------------+
                                                           |
                                                          TCP
                                                           v
                                               +-----------------------+
                                               |  <<server>> DBServer  |
                                               |   +---------------+   |
                                               |   |   Oracle DB   |   |
                                               |   +---------------+   |
                                               +-----------------------+
```

### E. Comparison: Component vs Node

| Feature | Component | Node |
|---|---|---|
| **Nature** | Software entity (Code artifact) | Hardware entity (Physical device/processor) |
| **Examples** | `.dll`, `.jar`, `.exe`, source files | Web Server, Database Server, Sensor, Router |
| **Representation**| Rectangle with side tabs or `<<component>>`| 3D Cube / Six-sided box |
| **Location** | Resides and executes *inside* a Node | Houses and runs software components |

### F. AKTU Exam Answer
**Q. Explain Deployment Diagram. What is the difference between Components and Nodes?**
1. **Deployment Diagram:** Models the physical hardware architecture, showing runtime processing nodes and communication paths where software artifacts are deployed.
2. **Component vs Node Table:** Present the comparison table above.
3. Draw the 3-tier Client-Server Deployment Diagram shown above.

### G. Quick Check
1. What 3D geometric shape is used to represent a Node?
2. Can a software component reside inside a hardware node?

---

# PART-WISE REVISION & EXAM PREPARATION

### 2-Mark Preparation
- **Structural Modeling:** Models static elements (Class, Object).
- **Behavioral Modeling:** Models dynamic message flows and states (Sequence, State machine).
- **Architectural Modeling:** Models physical software components and hardware deployment (Component, Deployment).
- **Stereotype:** Extends UML vocabulary using `<< >>`.
- **Lifeline:** Vertical dashed line representing an object's presence over time.
- **Node:** Physical hardware processing unit in a deployment diagram.

### 5-Mark Preparation
- Relationships in UML (Dependency, Association, Generalization, Realization).
- Generalization vs Specialization vs Aggregation.
- Class Diagram vs Object (Instance) Diagram with domain examples.
- Polymorphism in Collaboration Diagrams (Employee pay scenario).
- Vending machine Use Case Diagram and its utility in design.
- State Machine Diagram for answering a telephone call.
- Types of Events (Signal, Time, Change) with examples.
- Component vs Deployment Diagrams and Component vs Node comparison.

### Long Answer (10/15-Mark) Preparation
- Comprehensive Sequence Diagrams: Lifelines, activations, asynchronous non-blocking calls, priority queues, broadcast signals, and callback architecture.
- Detailed Comparison of all UML Behavioral Diagrams (Use Case, Sequence, Collaboration, State Machine, Activity).

---

# UNIT 2 — MASTER REVISION SHEET

### Master Topic Summary Table

| No. | Topic Name | Core Meaning | Exam Priority |
|---|---|---|---|
| 1 | **Types of Modeling** | Structural (Static), Behavioral (Dynamic), Architectural (Topology) | HIGH |
| 2 | **UML Relationships** | Dependency (`- - ->`), Association (`——`), Generalization (`——▷`), Realization (`- - -▷`) | HIGH |
| 3 | **Generalization vs Aggregation**| "Is-a" inheritance hierarchy vs "Part-of" composite association (`◇`)| HIGH |
| 4 | **Extensibility Mechanisms**| Stereotypes (`<< >>`), Tagged Values (`{k=v}`), Constraints (`{rule}`) | MEDIUM |
| 5 | **Class Diagram** | 3-compartment static class blueprint with attributes and operations | HIGH |
| 6 | **Object Diagram** | Point-in-time runtime snapshot with underlined object names | HIGH |
| 7 | **Collaboration Diagram** | Interaction along links with numbered message arrows | HIGH |
| 8 | **Polymorphism in Interaction**| Same message signature routed to diverse subclass instances | HIGH |
| 9 | **Sequence Diagram** | Chronological top-to-bottom time-ordered interaction diagram | HIGH |
| 10 | **Async & Priority Messages** | Non-blocking execution with `{priority = n}` message buffers | HIGH |
| 11 | **Broadcast & Callback** | `<<broadcast>>` to all objects; async event notification pattern | HIGH |
| 12 | **Use Case Diagram** | External actors interacting with use cases inside system boundary | HIGH |
| 13 | **Activity Diagram** | Workflow flowchart with Initial `●`, Final `⦿`, Decisions `◇`, Fork/Join | HIGH |
| 14 | **State Machine Diagram** | Single object lifecycle states and transitions (Telephone call) | HIGH |
| 15 | **Events (3 Types)** | Signal (`<<signal>>`), Time (`after`/`when`), Change (`when(cond)`) | HIGH |
| 16 | **Package Diagram** | Tabbed folder boxes organizing classes into hierarchical modules | MEDIUM |
| 17 | **Component Diagram** | Software executables and libraries with plug-and-play interfaces | HIGH |
| 18 | **Deployment Diagram** | Hardware 3D cubes (Nodes) and network communication paths | HIGH |

---

## Authentic Exam Questions (From Uploaded Material)

### PYQs from Uploaded Material
- **AKTU 2010-11:**
  - What do you understand by architectural modeling? (5 Marks)
  - Describe generalization and specialization. (5 Marks)
  - Explain collaboration diagram and polymorphism representation. (5 Marks)
  - Write short note on use case diagram and time diagram. (5 Marks)
  - What are the two special states in an activity diagram? (5 Marks)
  - Describe component diagrams in brief. (5 Marks)
- **AKTU 2011-12:**
  - Differentiate between a class and object with examples (Newspaper layout, Catalog store). (5 Marks)
  - Polygon and Points sequence class diagram from instance diagram. (5 Marks)
  - Library book checkout system object diagram with `/lateCharge`. (5 Marks)
  - Sequence diagram terms, asynchronous messages with priority, broadcast messages. (10 Marks)
  - Basic behavioral modeling overview. (5 Marks)
- **AKTU 2012-13:**
  - Write short notes on architectural modeling. (5 Marks)
  - Define aggregation and generalization. (5 Marks)
  - Categorize relationships: Country/Capital, Files/Records. (5 Marks)
  - Difference between class diagram and instance diagram (Family tree instance diagram). (10 Marks)
  - Sequence diagram significance: Broadcast, Callback, Asynchronous messages. (10 Marks)
- **AKTU 2013-14:**
  - Different types of modeling diagrams used in UML. (5 Marks)
  - Explain class and object diagrams with examples. (5 Marks)
  - Polymorphism, Iterated messages, and use of Self in collaboration diagrams. (5 Marks)
  - Explain use case with example and package diagrams. (5 Marks)
- **AKTU 2014-15:**
  - Define package and explain package diagrams. (5 Marks)
  - Use case diagram summaries for vending machine. (5 Marks)
  - What do you mean by activity diagram? (5 Marks)
  - Define state machine and draw telephone call state diagram. (5 Marks)
  - What is an event? Explain 3 types of events. (5 Marks)
  - Explain deployment diagram and difference between Component and Node. (5 Marks)

---

# UNIT 2 — 30-MINUTE REVISION PLAN

- **00 – 05 min (Modeling Types & Relationships):**
  - Revise Structural vs Behavioral vs Architectural modeling.
  - Review the 4 UML Relationships: Dependency (`- - ->`), Association (`——`), Generalization (`——▷`), Realization (`- - -▷`).
- **05 – 10 min (Class vs Object Diagrams):**
  - Revise Class box (3 compartments) vs Object box (`underlined: Name`).
  - Review Newspaper layout & Family Tree modeling examples.
- **10 – 15 min (Collaboration & Sequence Diagrams):**
  - Collaboration: Links + Numbered message arrows + Polymorphism (Payroll example).
  - Sequence: Lifelines, Activation rectangles, Synchronous vs Asynchronous arrows.
- **15 – 20 min (Advanced Interaction Patterns):**
  - Asynchronous messages with priority queues (`{priority = 3}`).
  - Broadcast messages (`<<broadcast>>`) and Callback registration mechanism.
- **20 – 25 min (Behavioral Diagrams):**
  - Use Case: Actors, System boundary, Vending Machine diagram, `<<include>>`/`<<extend>>`.
  - Activity: Initial `●`, Final `⦿`, Decision `◇`, Fork/Join bars.
  - State Machine: States, Transitions, Telephone call diagram.
  - Events: Signal, Time (`after`), Change (`when`).
- **25 – 30 min (Architectural Diagrams):**
  - Component Diagrams (Software packages, Lollipop interfaces).
  - Deployment Diagrams (3D Hardware Nodes, Network lines).
  - Component vs Node difference table.

---

# UNIT 2 — 10-MINUTE LAST-MOMENT REVISION

1. **4 Relationships:** Dependency (`- - ->`), Association (`——`), Generalization (`——▷`), Realization (`- - -▷`).
2. **Generalization vs Aggregation:** Generalization is "Is-a" (Inheritance); Aggregation is "Has-a" (Whole-part, `◇`).
3. **Class vs Object Diagram:** Class is abstract schema; Object is concrete runtime snapshot with underlined title.
4. **Collaboration vs Sequence:** Collaboration emphasizes structural layout; Sequence emphasizes chronological time order.
5. **Lifeline & Destruction:** Lifeline is vertical dashed line; Destruction is marked with an `X`.
6. **Async Message & Callback:** Async uses half arrowhead (non-blocking); Callback uses registration + asynchronous notification.
7. **Use Case Diagram:** Actors (stick figures) + Use cases (ellipses) inside a system boundary box.
8. **Activity Diagram Symbols:** Initial state `●`, Final state `⦿`, Decision `◇`, Fork/Join solid bar.
9. **State Machine:** Models single object lifecycle; telephone call transitions from `Idle` $\rightarrow$ `Dial Tone` $\rightarrow$ `Dialing` $\rightarrow$ `Ringing` $\rightarrow$ `Connected` $\rightarrow$ `Disconnected`.
10. **Component vs Node:** Component = Software artifact (`.dll`, `.exe`); Node = Hardware device/server (3D Cube).

---

# COMMON EXAM MISTAKES

1. **Confusing Association with Generalization:** Drawing a plain arrow instead of a hollow triangle for inheritance.
2. **Forgetting Underline in Object Diagrams:** Object names must always be underlined (e.g., `s1: Student`).
3. **Mixing Synchronous and Asynchronous Arrows:** Solid filled arrowhead = Synchronous (blocking); Half open arrowhead = Asynchronous (non-blocking).
4. **Drawing Actors Inside the System Boundary:** Actors are external entities and must always be drawn *outside* the system boundary rectangle.
5. **Confusing Component and Node:** Calling a physical database server a component instead of a Node.
