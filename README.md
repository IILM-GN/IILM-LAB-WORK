# 📚 IILM University — Laboratory Work & Practicals

A curated repository housing laboratory experiments, practical assignments, and coursework implementations for the **Department of Computer Science & Engineering** at **IILM University, Greater Noida**.

---

## 📌 Repository Overview

This repository documents hands-on practical implementations across multiple core computer science disciplines, specifically focused on 3rd Semester coursework:

- **CPP (C++ & Standard Template Library)**: Modern C++ implementations exploring sequential containers (`std::vector`, `std::array`), associative containers (`std::map`), and standard algorithms with lambdas.
- **DCN (Data Communication and Networks)**: Network protocol simulations, bit-level error detection schemes (parity checks), and communication algorithms.
- **DSA (Data Structures & Algorithms)**: Fundamental and advanced data structure implementations in C and C++, including singly/doubly linked lists, stacks, overflow/underflow handling, and memory management.
- **DVA (Data Visualization & Analytics)**: Python data science workflows with Pandas and NumPy covering data cleaning, handling missing values/outliers, attribute classification, and dataset transformation.

---

## 🗂️ Directory Structure

```text
IILM-LAB-WORK/
├── 3RD SEM/
│   ├── CPP/
│   │   ├── 004_Sequential_Containers.cpp   # std::array & std::vector with student marks calculation
│   │   ├── 005_Assosiative_Container.cpp   # std::map word-meaning dictionary implementation
│   │   └── 006_STL_Algorithms.cpp          # Sorting with lambdas and std::find_if predicate search
│   ├── DCN/
│   │   └── Error_Detection.py              # Even parity check error detection simulation
│   ├── DSA/
│   │   ├── double_linked-list.c            # Doubly linked list operations
│   │   ├── linkedlist.c                    # Singly linked list in C
│   │   ├── linkedlist.cpp                  # Singly linked list in C++
│   │   ├── singly_linked_list.c            # Singly linked list operations and traversal
│   │   ├── stack10.c                       # Stack operations (push, pop, size, boundary checks)
│   │   └── stack_class.c                   # Stack class and structure implementations
│   └── DVA/
│       ├── 003_Attributes.py               # Data attributes classification (Nominal, Ordinal, Numeric)
│       ├── 003_students.py                 # Data cleaning & preprocessing pipeline using Pandas
│       ├── students.csv                    # Raw student dataset
│       └── students_clean.csv              # Processed & cleaned student dataset
├── .gitignore                              # Git ignore rules for compiled binaries & cache
└── README.md                               # Repository documentation
```

---

## 🔬 Course Modules & Experiments

### 1. Object-Oriented Programming with C++ (`CPP`)
| File | Topic | Description |
| :--- | :--- | :--- |
| `004_Sequential_Containers.cpp` | Sequential Containers | Demonstrates `std::array` and `std::vector` for dynamic student score aggregation and average calculation. |
| `005_Assosiative_Container.cpp` | Associative Containers | Implements key-value pairs utilizing `std::map` for dictionary lookup. |
| `006_STL_Algorithms.cpp` | STL Algorithms | Implements custom lambda-based descending sort and `std::find_if` predicate search for even numbers. |

### 2. Data Communication & Networks (`DCN`)
| File | Topic | Description |
| :--- | :--- | :--- |
| `Error_Detection.py` | Parity Check Simulation | Implements even parity generation at sender and error detection verification at receiver. |

### 3. Data Structures & Algorithms (`DSA`)
| File | Topic | Description |
| :--- | :--- | :--- |
| `singly_linked_list.c` | Singly Linked List | Node creation, insertion, and traversal in C. |
| `double_linked-list.c` | Doubly Linked List | Bidirectional pointer navigation and node management. |
| `stack10.c` | Stack Operations | Fixed-capacity stack implementing push, pop, overflow/underflow checks, and element inspection. |

### 4. Data Visualization & Analytics (`DVA`)
| File | Topic | Description |
| :--- | :--- | :--- |
| `003_Attributes.py` | Attribute Classification | Categorization of dataset features into Nominal, Ordinal, Binary, and Numeric (Discrete vs. Continuous). |
| `003_students.py` | Preprocessing Pipeline | Comprehensive data cleaning pipeline handling missing values, standardizing IDs/classes, and normalising student records. |
| `students.csv` / `students_clean.csv` | Dataset | Input dirty dataset and the resulting preprocessed CSV output. |

---

## 🚀 Getting Started & Execution

### Prerequisites
- **C/C++ Compiler**: GCC / Clang / MSVC (`g++` / `gcc` supporting C++17 or newer)
- **Python**: Python 3.8+ with `pandas` and `numpy`

### Running C / C++ Programs
```bash
# Example: Compile and run C++ STL experiment
g++ "3RD SEM/CPP/004_Sequential_Containers.cpp" -o containers
./containers

# Example: Compile and run C DSA experiment
gcc "3RD SEM/DSA/stack10.c" -o stack
./stack
```

### Running Python Scripts
```bash
# Install required dependencies
pip install pandas numpy

# Run DVA Data Preprocessing Pipeline
python "3RD SEM/DVA/003_students.py"

# Run DCN Parity Check Simulation
python "3RD SEM/DCN/Error_Detection.py"
```

---

## 👨‍💻 Contributor

- **Harsh** ([@hix-001](https://github.com/hix-001))
- **Institution**: IILM University, Greater Noida

---

## 📄 License & Academic Note

This repository is maintained for educational and academic reference purposes as part of the IILM University engineering curriculum.
