# 🏦 AI Engineering Team Agent  
**Multi-Agent System for Simulating a Stock Trading Platform (UI + Backend)**

---

## 📌 Overview

This project implements a **multi-agent engineering system** that simulates a simplified **stock trading platform**, including:

- Buying and selling shares  
- Portfolio tracking  
- Profit/Loss calculation  
- Transaction history  
- Interactive UI using Gradio  

The system combines **backend business logic** with a **user-facing interface**, demonstrating how AI agents can assist in building full-stack applications.

---

## 🧠 Agent & Task Architecture

```mermaid
flowchart TD
    A[User Input: Requirements] --> B[Engineering Team Crew]

    B --> C[Engineering Lead]
    C --> D[Design Task]
    D --> E[System Design Output]

    E --> F[Backend Engineer]
    F --> G[Code Task]
    G --> H[accounts.py]

    H --> I[Frontend Engineer]
    I --> J[Frontend Task]
    J --> K[app.py]

    H --> L[Test Engineer]
    L --> M[Test Task]
    M --> N[test_accounts.py]

````

---

## ⚙️ Execution Flow

```mermaid
flowchart LR
    A[Design Task] --> B[Code Task]
    B --> C[Frontend Task]
    B --> D[Test Task]
```

---

## 🧩 Agent Responsibilities

### 👨‍💼 Engineering Lead

* Converts high-level requirements into a **detailed system design**
* Defines:

  * classes
  * methods
  * module structure

📄 Design output → `accounts.py_design.md` 

---

### 🧑‍💻 Backend Engineer

* Implements the full system in **one Python module**
* Ensures:

  * business logic correctness
  * validation rules (no negative balance, etc.)
  * UI-compatible outputs (important fix)

📄 Output → `accounts.py` 

---

### 🎨 Frontend Engineer

* Builds a **Gradio UI**
* Connects UI actions to backend methods
* Demonstrates system functionality

📄 Output → `app.py` 

---

### 🧪 Test Engineer

* Writes **unit tests** for backend module
* Validates:

  * transactions
  * holdings
  * edge cases

📄 Output → `test_accounts.py` 

---

## 🔄 Task Pipeline

The system follows a **sequential pipeline with context passing**:

1. **Design Task**

   * Creates system architecture
2. **Code Task**

   * Implements backend using design
3. **Frontend Task**

   * Builds UI using backend
4. **Test Task**

   * Validates backend correctness

📄 Defined in: 

---

## 🧠 Key Design Pattern

This system uses a **role-based multi-agent engineering workflow**:

* Separation of concerns (design / backend / frontend / testing)
* Sequential execution ensures dependency correctness
* Context passing between tasks improves consistency
* Each agent focuses on a **single responsibility**

---

## 🏗️ Architecture Summary

The system is structured into three layers:

### 1. Agent Layer

* Engineering Lead
* Backend Engineer
* Frontend Engineer
* Test Engineer

### 2. Task Layer

* Design → Code → Frontend → Test

### 3. Output Layer

* Design doc
* Backend module
* UI app
* Test suite

---

## 📌 Why This Architecture Matters

* Mimics real-world engineering teams
* Enforces structured development lifecycle
* Reduces errors through staged execution
* Improves maintainability and extensibility


---

## ⚙️ How It Works

### 🖥️ User Interface (Gradio)

* Provides an interactive dashboard
* Allows users to:

  * Buy/Sell stocks
  * View holdings
  * Track performance

---

### 💼 Account System

Maintains:

* Account balance
* Stock holdings
* Transaction history

Handles all business logic for trading operations.

---

### 📈 Core Operations

#### Buy Shares

* Deducts balance
* Adds to holdings
* Records transaction

#### Sell Shares

* Validates ownership
* Updates balance
* Removes shares
* Records transaction

#### Deposit / Withdraw

* Updates account balance
* Logs activity

---

### 📊 Reporting Features

* **Portfolio Value** → Total worth of holdings
* **Profit/Loss** → Net gain or loss
* **Holdings** → Current stock positions
* **Transactions** → Full activity history

---

## 🛠️ Output Screenshots

<img width="1920" height="988" alt="image" src="https://github.com/user-attachments/assets/f5001e0f-fd95-4b86-a1ab-012acf115d04" />

<img width="1919" height="994" alt="image" src="https://github.com/user-attachments/assets/a366df26-1b95-4268-bdb1-0d8e42befe1c" />

<img width="1920" height="995" alt="image" src="https://github.com/user-attachments/assets/04103719-d81c-4890-8e80-4561c6da7aa7" />

---

## 🛠️ Tech Stack

* Python
* Gradio (UI)
* CrewAI (agent structure)
* Pydantic
* YAML configuration

---

## 📂 Project Structure

```bash
engineering-team-agent/
│
├── src/
│   ├── accounts.py          # Core account logic
│   ├── app.py               # Gradio UI
│   ├── crew.py              # Agent orchestration
│   ├── main.py              # Entry point
│   └── config/
│       ├── agents.yaml
│       └── tasks.yaml
│
├── output/
├── README.md
```

---

## ▶️ Setup & Run

### 1. Install dependencies

```bash
pip install uv
crewai install
```

---

### 2. Run the application

```bash
python app.py
```

---

### 3. Open UI

```
http://127.0.0.1:7860
```

---

## 📊 Example Workflow

1. Deposit money into account
2. Buy shares (e.g., AAPL, GOOGL)
3. Sell shares
4. View:

   * Holdings
   * Transactions
   * Profit/Loss

---

## 🧩 Key Features

* Full trading workflow simulation
* Persistent transaction tracking
* Clean UI interaction with backend logic
* Modular and extensible architecture
* Real-time feedback in UI

---

## 🔮 Future Improvements

* Real-time stock price integration (API)
* Multi-user support
* Database persistence (PostgreSQL)
* Authentication system
* Advanced analytics dashboard
* Risk analysis module

---

## ⚠️ Note

This project is a simulation and does **not use real financial data**.
It is intended for **learning system design and agent-based development**.

---

## ⭐ Summary

This project demonstrates:

* Full-stack system design (UI + backend)
* Business logic implementation
* State management (balance, holdings, transactions)
* Agent-assisted software development
* Clean modular architecture

