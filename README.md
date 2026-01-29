# AI-Based Stock Market Simulation (Multi-Agent System)

This project simulates a stock market environment using multiple autonomous agents that make decisions based on market conditions, financial constraints, and LLM-driven reasoning.

## 🎯 Motivation
Most stock market simulations rely on fixed rules or hard-coded strategies.
This project explores how **LLM-powered autonomous agents** behave under
financial constraints, uncertainty, and imperfect information — closer to
real-world market dynamics.

## 🚀 Features
- Multi-agent stock market simulation
- AI-driven decision making (buy / sell / loan planning)
- Loan management with interest & repayment cycles
- Market price fluctuation and trading sessions
- Robust validation to prevent invalid agent actions
- Detailed logging and experiment tracking
  
## 🧪 Key Challenges Solved
- Prevented invalid or hallucinated AI actions using strict output validation
- Designed agents to safely skip actions instead of breaking the simulation
- Managed loan constraints so agents cannot exceed initial net worth
- Handled inconsistent LLM responses without crashing the system


## 🧠 Tech Stack
- Python
- Large Language Models (LLM APIs)
- Object-Oriented Design
- Simulation-based Modeling
- Git & GitHub

## 📁 Project Structure
- `agent.py` – Agent logic and decision-making
- `main.py` – Simulation runner
- `stock.py` – Stock price & market behavior
- `secretary.py` – Output validation & constraint enforcement
- `record.py` – Experiment logging
- `procoder/` – Prompt construction utilities
- `prompt/` – LLM prompts

## ▶️ How to Run

1. Clone the repository
```
git clone https://github.com/Subhadeep07/stock-market-simulation.git
cd stock-market-simulation
```
2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Run the simulation
```
python main.py
```
## 💡 What This Project Demonstrates
- Applied multi-agent system design in a financial simulation
- Practical use of LLMs beyond chatbots
- Defensive programming against unreliable AI outputs
- Clean modular Python architecture

This project was built to explore **AI reasoning under constraints**, not to
maximize trading profit.

