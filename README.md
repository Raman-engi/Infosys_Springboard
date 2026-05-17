# CodeGenie 🤖

<p align="center">
  <img src="https://raw.githubusercontent.com/Raman-engi/Infosys_Springboard/main/screenshots/banner.gif?v=2" width="800"/>
</p>

<p align="center">
  <b>AI-Powered Code Generation & Explanation Platform</b>
  <br>
  <em>Built during Infosys Springboard Internship</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/transformers-%F0%9F%A4%97-orange?style=for-the-badge"/>
</p>

<div align="center">

---

## 🎯 Quick Navigation

| 🔗 Quick Links | 🚀 Features | 📞 Support |
|----------------|-------------|------------|
| [📹 Demo Video](#-demo-video) | [🧠 AI Code Analysis](#-ai-code-analysis) | [🐛 Report Bug](#-report-bug) |
| [🐳 Docker Setup](#-docker-deployment) | [📊 Admin Dashboard](#-admin-dashboard) | [💡 Request Feature](#-request-feature) |
| [🛠 Installation](#-installation) | [🔐 Secure Auth](#-secure-authentication) | [🤝 Contributing](#-contributing) |

---

</div>

## 🌟 Featured In

<p align="center">
  <img src="screenshots/infosys.png" width="220">
  <br/>
  <strong>Infosys Springboard Internship Program</strong>
</p>



---

## 📹 Demo Video

<div align="center">

[![CodeGenie Demo](https://img.shields.io/badge/WATCH_DEMO-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://drive.google.com/file/d/1mtrmlc1ouGJ4K7M5yiGghkx9IHeG_yps/view)

*Click above to watch the full platform walkthrough*

</div>

---

## 🚀 What Makes CodeGenie Special?

<div align="center">

| 🤔 Traditional AI Assistants | 🎯 CodeGenie Approach |
|------------------------------|----------------------|
| ❌ Generic code explanations | ✅ **AST-powered** structural analysis |
| ❌ Surface-level understanding | ✅ **Deep context-aware** reasoning |
| ❌ One-size-fits-all responses | ✅ **Language-specific** model optimization |
| ❌ No project awareness | ✅ **Modular architecture** understanding |

</div>

---

## 🏗 System Architecture

### 🎯 Architecture Highlights

<table>
<tr>
<td width="50%">

#### 🎨 Frontend Layer
```python
Streamlit UI Components:
├── Real-time Chat Interface
├── Code Editor with Syntax Highlighting
├── Interactive Dashboard
├── Responsive Design
└── Theme Support (Light/Dark)
```

</td>
<td width="50%">

#### 🔧 Backend Services
```python
Python Backend Modules:
├── JWT Authentication
├── AST Parsing Engine
├── Model Orchestration
├── SQLite Database Layer
└── SMTP Email Service
```

</td>
</tr>
</table>

---

## 🛠 Tech Stack Deep Dive

<div align="center">

| Layer | Technology | Purpose |
|-------|------------|---------|
| 🎨 **Frontend** | `Streamlit` | Interactive UI Framework |
| ⚙️ **Backend** | `Python 3.10+` | Core Application Logic |
| 🧠 **AI/ML** | `HuggingFace Transformers` | Model Inference |
| 🔍 **Analysis** | `Python AST` | Code Structure Parsing |
| 💾 **Database** | `SQLite` | Data Persistence |
| 🔐 **Auth** | `JWT + Bcrypt` | Secure Authentication |
| 📧 **Email** | `SMTP (Gmail)` | OTP Recovery |
| 🐳 **Deployment** | `Docker` | Containerization |

</div>

---

## 🤖 AI Models & HuggingFace Integration

### 🔗 HuggingFace API Models

<table>
<tr>
<th>Model</th>
<th>Task</th>
<th>HuggingFace ID</th>
<th>Performance</th>
</tr>

<tr>
<td>🧠 <b>DeepSeek-Coder</b></td>
<td>Code Generation</td>
<td>
<code>deepseek-ai/deepseek-coder-1.3b</code>
</td>
<td>⭐️⭐️⭐️⭐️⭐️</td>
</tr>

<tr>
<td>💬 <b>Microsoft Phi-2</b></td>
<td>General Reasoning</td>
<td>
<code>microsoft/phi-2</code>
</td>
<td>⭐️⭐️⭐️⭐️☆</td>
</tr>

<tr>
<td>🦙 <b>gemma</b></td>
<td>Multi-language Code</td>
<td>
<code>gemma/gemma</code>
</td>
<td>⭐️⭐️⭐️⭐️⭐️</td>
</tr>
</table>

### 🔑 HuggingFace API Configuration

```python
# Environment Configuration (.env)
HUGGINGFACE_API_KEY="hf_your_api_key_here"
MODEL_CACHE_DIR="./model_cache"

# API Usage Example
from huggingface_hub import InferenceClient
client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))
```

---

## 🎯 Key Features

### 👤 User Features

<div align="center">

| Feature | Icon | Status | Description |
|---------|------|--------|-------------|
| **Secure Authentication** | 🔐 | ✅ | JWT tokens + OTP recovery |
| **AST Code Analysis** | 🧠 | ✅ | Structural code understanding |
| **Multi-language Support** | 🌐 | ✅ | Python, JavaScript, SQL |
| **Code Generation** | ✍️ | ✅ | Text-to-code transformation |
| **Interactive Chat** | 💬 | ✅ | AI-powered programming assistant |
| **History Tracking** | 🕘 | ✅ | Complete session logging |
| **Feedback System** | ⭐ | ✅ | Ratings & comments |
| **Theme Customization** | 🎨 | ✅ | Light/Dark mode |

</div>

### 🛠 Admin Features

<table>
<tr>
<td width="33%">

#### 👥 User Management
- Role-based access control
- Admin promotion/demotion
- Account suspension
- User analytics

</td>
<td width="33%">

#### 📊 Analytics Dashboard
- User growth metrics
- Model usage statistics
- Activity heatmaps
- Language popularity

</td>
<td width="33%">

#### 🔍 System Monitoring
- Real-time logs
- Performance metrics
- Security auditing
- Data export capabilities

</td>
</tr>
</table>

---

## 📂 Project Structure

```bash
CodeGenie/
│
├── notebooks/
│   └── CodeGenie_Colab_Complete.ipynb      # Your prototype / experimental code
│
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── model_loader.py                 # Load / switch models (GPT, LLaMA, CodeGemma)
│   │   ├── code_generator.py               # Generate code
│   │   ├── code_explainer.py               # Explain code
│   │   ├── evaluator.py                    # Evaluate quality, run tests
│   │   └── utils.py                        # Common helper utilities
│   │
│   ├── pipelines/
│   │   ├── codegen_pipeline.py             # Full flow: prompt → model → code → summary
│   │   └── explain_pipeline.py             # Full flow: code → explanation → complexity
│   │
│   ├── storage/
│   │   ├── history_manager.py              # Store attempts, runs, logs
│   │   ├── cache_manager.py                # Cache model outputs
│   │   └── db.sqlite3                      # Local DB (if needed)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── server.py                       # FastAPI / Flask backend
│   │   ├── routes_codegen.py               # /generate endpoint
│   │   └── routes_explain.py               # /explain endpoint
│   │
│   └── ui/
│       ├── web/
│       │   ├── index.html
│       │   ├── styles.css
│       │   └── app.js
│       └── streamlit/
│           ├── main.py                     # Streamlit frontend (if you use it)
│           ├── components.py
│           └── theme.json
│
├── config/
│   ├── settings.yaml                       # App config (model, temperature, API keys)
│   ├── logging.conf                        # Logging setup
│   └── prompts/                            # Reusable model prompts
│       ├── codegen_prompt.txt
│       └── explain_prompt.txt
│
├── tests/
│   ├── test_codegen.py
│   ├── test_explainer.py
│   └── test_api.py
│
├── data/
│   ├── examples/                           # Example code snippets for testing
│   └── logs/
│       └── history.json                    # Execution history
│
├── requirements.txt
├── README.md
├── LICENSE
└── run.py                                  # Entry point to start the app
```

---

## 🚀 Installation & Setup

### 📋 Prerequisites

<div align="center">

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Python | 3.10+ | `python --version` |
| Git | Latest | `git --version` |
| Docker | Optional | `docker --version` |

</div>

### ⚡ Quick Installation

```bash
# 1. Clone Repository
git clone https://github.com/Raman-engi/Infosys_Springboard
cd Infosys_Springboard_V.0

# 2. Install Dependencies
pip install -r requirements.txt

# 3. Setup Environment
cp .env.example .env
# Edit .env with your configurations
```

### 🔑 Environment Configuration

```bash
# Authentication
JWT_SECRET_KEY=your_super_secure_secret_key_here
ADMIN_INITIAL_USER=admin@codegenie.com
ADMIN_INITIAL_PASS=admin123

# HuggingFace API
HUGGINGFACE_API_KEY=hf_your_actual_api_key_here
MODEL_CACHE_DIR=./model_cache

# Email Service (OTP)
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_specific_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
```

### 🐳 Docker Deployment

```bash
# Build and run with Docker
docker build -t codegenie .
docker run -p 8501:8501 --env-file .env codegenie

# Or use docker-compose
docker-compose up -d
```

---

## 📱 Usage Guide

### 🎮 Getting Started

<table>
<tr>
<td width="50%">

#### 1. **Authentication**
```python
# Sign up with email
# Verify via OTP
# Secure JWT login
```

#### 2. **Choose Mode**
- 🧠 Code Explanation
- ✍️ Code Generation
- 💬 AI Chat

</td>
<td width="50%">

#### 3. **Select Language**
- Python 🐍
- JavaScript 🌐
- SQL 🗃

#### 4. **Get Results**
- Structured output
- AST analysis
- Rate & feedback

</td>
</tr>
</table>

### 🎯 Use Case Examples

<details>
<summary>🔍 <b>Code Explanation</b></summary>

```python
# Input Code
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# CodeGenie Analysis:
📊 Structure: Recursive function
🎯 Purpose: Calculate Fibonacci sequence
⚡ Complexity: O(2^n) - Exponential
💡 Suggestion: Use memoization for optimization
```
</details>

<details>
<summary>⚡ <b>Code Generation</b></summary>

```python
# User Prompt:
"Create a Python function to validate email addresses"

# Generated Code:
import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```
</details>

---

## 📸 UI Showcase

<div align="center">

### 🎨 User Interface Gallery

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
| **🔐 Login Page**<br><img src="screenshots/login_page.png" width="200"> | **📝 Sign Up**<br><img src="screenshots/sign_up .png" width="200"> | **🤖 AI Chat**<br><img src="screenshots/ai_chat.png" width="200"> |
| **🧠 Code Explainer**<br><img src="screenshots/code_explainer.png" width="200"> | **⚡ Code Generator**<br><img src="screenshots/code_generator.png" width="200"> | **📊 History**<br><img src="screenshots/history_page.png" width="200"> |
| **👤 Profile**<br><img src="screenshots/profile_page.png" width="200"> | **🔒 Password Recovery**<br><img src="screenshots/password_recovery.png" width="200"> | **🛠 Admin Dashboard**<br><img src="screenshots/admin_dashboard.png" width="200"> |

</div>

---

## 🛠 Advanced Configuration

### 🤖 Model Configuration

```python
# Model selection based on task
MODEL_CONFIG = {
    "code_generation": {
        "primary": "deepseek-ai/deepseek-coder-1.3b",
        "fallback": "google/gemma-2b"
    },
    "explanation": {
        "python": "microsoft/phi-2",
        "javascript": "google/gemma-2b",
        "sql": "google/gemma-2b"
    },
    "chat": {
        "primary": "microsoft/phi-2",
        "fallback": "google/gemma-2b"
    }
}
```

### ⚡ Performance Optimization

```python
# Enable 4-bit quantization for faster inference
model_config = {
    "load_in_4bit": True,
    "bnb_4bit_use_double_quant": True,
    "bnb_4bit_quant_type": "nf4",
    "bnb_4bit_compute_dtype": torch.bfloat16
}
```

---

## 🧭 Development Roadmap

<div align="center">

| Status | Feature | Timeline |
|--------|---------|----------|
| ✅ | **Core Platform** | Completed |
| ✅ | **Docker Support** | Completed |
| ✅ | **HuggingFace Integration** | Completed |
| ✅ | **VS Code Extension** | Completed |
| ✅ | **Visual AST Explorer** |Completed|
| ✅ | **GitHub Integration** | Completed |
| ✅ | **PDF Export** | Completed |
| ✅ | **Multi-repo Analysis** | Completed |

</div>

---

## 🤝 Contributing:- 

### 🐛 Report a Bug
1. Check existing [issues](https://github.com/Raman-engi/Infosys_Springboard/issues)
2. Create new issue with detailed description
3. Include screenshots if possible

### 💡 Request a Feature
1. Describe the feature clearly
2. Explain the use case
3. Suggest implementation approach

### 🔧 Development Setup
```bash
# 1. Fork repository
# 2. Create feature branch
git checkout -b feature/amazing-feature

# 3. Commit changes
git commit -m 'Add amazing feature'

# 4. Push to branch
git push origin feature/amazing-feature

# 5. Create Pull Request
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Acknowledgments

- **Infosys Springboard** for the internship opportunity
- **HuggingFace** for the amazing transformer models
- **Streamlit** for the incredible UI framework
- **Python AST** module for code structure analysis

---

<div align="center">

## 💫 Made with ❤️ during Infosys Springboard Internship

<p align="center">
  <img src="screenshots/infosys.png" width="220">width="150"/>
</p>

**CodeGenie** - Transforming how developers understand and write code, one AI-powered insight at a time.

[⬆ Back to Top](#codegenie-)

</div>
