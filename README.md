
# 🤖 Prompty Learning Path

A hands-on learning project that progressively teaches you how to build AI applications using [Prompty](https://prompty.ai) — from simple completions to agents with tool calling and evaluation.

## 📖 What is Prompty?

[Prompty](https://prompty.ai/getting-started/concepts/) is a **micro-orchestrator** for LLM invocations that provides:

- **Specification** — A `.prompty` file format for defining prompts as reusable assets
- **Tooling** — VS Code extension for creating, managing, and testing prompts
- **Runtime** — Python/C# libraries to execute prompts in your applications

Think of Prompty as sitting one level above raw API calls, letting you configure models, engineer prompts, and shape data — all in a clean, declarative format.

## 🎯 Learning Path

This project is structured as a progressive tutorial with four modules:

| Module | Topic | Description |
|--------|-------|-------------|
| `1-simple/` | **Basic Completion** | Your first Prompty — load and execute a simple prompt |
| `2-chat/` | **Interactive Chat** | Build a conversational chat loop with message history |
| `3-agent/` | **Tool Calling** | Create an agent that uses function tools |
| `4-eval/` | **Evaluation** | Evaluate AI responses for groundedness |

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- Azure OpenAI resource (or modify connection settings for other providers)
- [Prompty VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.prompty) (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/sethjuarez/agent-app.git
cd agent-app

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root with your Azure OpenAI credentials:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key
```

## 📁 Project Structure

```text
agent-app/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies: prompty[azure], colorama
├── pyproject.toml          # Project configuration
│
├── 1-simple/               # Module 1: Basic Prompty
│   ├── run.py              # Async execution example
│   ├── completion.prompty  # Simple completion prompt
│   ├── function.prompty    # Function-style prompt
│   ├── structured.prompty  # Structured output prompt
│   └── products.json       # Sample data
│
├── 2-chat/                 # Module 2: Chat Interface
│   ├── run.py              # Interactive chat loop
│   ├── chat.prompty        # Chat prompt with history
│   └── products.json       # Sample data
│
├── 3-agent/                # Module 3: Agentic Patterns
│   ├── agent.py            # Agent with tool calling
│   └── agent.prompty       # Agent prompt with tool definitions
│
└── 4-eval/                 # Module 4: Evaluation
    ├── eval.py             # Evaluation pipeline
    ├── groundedness.prompty # Groundedness evaluation metric
    └── information.prompty  # Information extraction prompt
```

## 📚 Module Details

### 1️⃣ Simple Completion (`1-simple/`)

Learn the basics of loading and executing a Prompty file:

```python
import prompty
import prompty.azure

# Load and execute a prompty file
p = await prompty.load_async("completion.prompty")
result = await prompty.execute_async(
    p, 
    inputs={"question": "What kind of tents do you sell?"}, 
    merge_sample=True
)
```

**Key Concepts:**

- `.prompty` file structure (frontmatter + template)
- Model configuration (API type, connection, deployment)
- Input definitions with types, defaults, and samples
- Jinja2 templating for dynamic prompts

### 2️⃣ Interactive Chat (`2-chat/`)

Build a conversational interface with message history:

```python
p = prompty.load("chat.prompty")
while (prompt := input("user> ")) != "exit":
    result = prompty.execute(p, inputs={"query": prompt}, merge_sample=True)
    print(f"agent> {result}")
```

**Key Concepts:**

- The `![thread]` marker for conversation history
- Synchronous execution with `prompty.execute()`
- Building interactive CLI applications

### 3️⃣ Agent with Tools (`3-agent/`)

Create an agent that can call external functions:

```python
def get_current_weather(city: str, unit: str = "Celsius"):
    return f"The weather in {city} is 32 {unit}"

p = prompty.load("agent.prompty")
p.set_tool_value("get_current_weather", get_current_weather)
result = prompty.execute(p, inputs={"question": "What's the weather in Tokyo?"})
```

**Key Concepts:**

- `api: agent` model configuration
- Tool definitions in the prompty frontmatter
- Binding Python functions to tools
- Multi-step reasoning with tool results

### 4️⃣ Evaluation (`4-eval/`)

Evaluate AI responses using LLM-as-judge patterns:

```python
# Get a response from your AI
response = await get_information(question, context)

# Evaluate groundedness
result = await prompty.execute_async(
    "groundedness.prompty",
    inputs={"query": question, "context": context, "response": response}
)
```

**Key Concepts:**

- Evaluation metrics (groundedness, relevance, etc.)
- Structured outputs for scoring (1-5 scale)
- Building evaluation pipelines
- RAG scenario evaluation

## 🔍 Observability & Tracing

All modules include tracing support for debugging:

```python
from prompty.tracer import Tracer, trace, PromptyTracer

tracy = PromptyTracer()
Tracer.add("prompty", tracy.tracer)

@trace
def my_function():
    # Your code here - automatically traced!
    pass
```

This generates trace files you can inspect to debug prompt execution and understand the flow of data through your application.

## 🛠️ Running the Examples

```bash
# Module 1: Simple completion
cd 1-simple && python run.py

# Module 2: Interactive chat (type 'exit' to quit)
cd 2-chat && python run.py

# Module 3: Agent with tools
cd 3-agent && python agent.py

# Module 4: Evaluation
cd 4-eval && python eval.py
```

## 📖 Resources

- [Prompty Documentation](https://prompty.ai)
- [Prompty Concepts](https://prompty.ai/getting-started/concepts/)
- [Prompty Specification](https://prompty.ai/specification/page/)
- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.prompty)
- [GitHub Repository](https://github.com/microsoft/prompty)

## 📝 License

This project is for educational purposes. See the LICENSE file for details.
