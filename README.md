# Autonomous AI Data Analyst 🤖📊

An enterprise-grade, multi-agent AI system designed for autonomous dataset ingestion, automated data profiling, natural language Text-to-SQL generation, exploratory data analysis (EDA), automated machine learning (AutoML), and interactive AI-driven analytics dashboards.

---

## 🌟 Key Features & Functionalities

### 📥 1. Multi-Format Data Ingestion
* Supports **CSV**, **Excel** (`.xlsx`, `.xls`), **Parquet**, **JSON**, **SQLite**, and **SQL** database files.
* Powered by **Polars** lazy-loading and **DuckDB** zero-copy memory registration for high-speed analysis over multi-gigabyte datasets without heavy memory overhead.

### 🔍 2. Automated Data Profiling & Quality Scoring
* Computes summary statistics, null/missing value percentages, unique cardinalities, and data types automatically upon dataset upload.
* Infers semantic column classification (**categorical**, **numerical**, **datetime**, **boolean**).
* Calculates an automated **Data Quality Score** out of 100 based on completeness and data health heuristics.

### 💬 3. Natural Language Text-to-SQL Engine
* Translates user questions into optimized **DuckDB SQL** queries using **Google Gemini** (`gemini-1.5-pro`, `gemini-1.5-flash`) or **Groq** LLM providers.
* Includes intelligent rule-based fallbacks to ensure query execution even when LLM APIs are unreachable.
* Returns raw generated SQL, execution latency (ms), column metadata, and structured result sets.

### 🤖 4. Multi-Agent AI Workflow (LangGraph)
* Built on **LangGraph StateGraph** to orchestrate specialized AI agents:
  * **Orchestrator Agent**: Analyzes user intent, dataset schemas, and routes tasks.
  * **SQL Agent**: Formulates and executes schema-aware analytical SQL queries.
  * **Reflection Agent**: Evaluates execution outputs, verifies results, and synthesizes natural language insights.
* Tracks step-by-step agent thoughts, actions taken, and output summaries in real-time.

### 🤖 5. Automated Machine Learning (AutoML) & Tracking
* Automatic problem type detection (**Classification** vs **Regression**).
* Trains state-of-the-art models (**Random Forest**, **XGBoost**, **LightGBM**, **CatBoost**).
* Integrates **Optuna** for hyperparameter optimization and **SHAP** for feature importance explainability.
* Logs models, metrics, and parameters seamlessly to **MLflow**.

### 💻 6. Modern Interactive Dashboard UI
* Built with **React 18**, **TypeScript**, **Vite**, and **Tailwind CSS**.
* Interactive data visualization via **Plotly.js** (`react-plotly.js`).
* Responsive sidebar navigation and drag-and-drop file uploader.
* Dynamic state management powered by **Zustand** and **TanStack React Query**.

---

## 🛠️ Architecture & Technology Stack

| Layer | Technologies & Tools |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, Lucide React, Plotly.js, Zustand, TanStack Query |
| **Backend API** | Python 3.10+, FastAPI, Pydantic v2, Structlog, Uvicorn |
| **Data & Query Engine** | DuckDB, Polars, Pandas, PyArrow, SQLAlchemy, AsyncPG |
| **AI / Multi-Agent Core** | LangChain, LangGraph, Google Gemini API (`langchain-google-genai`), Groq API (`langchain-groq`) |
| **AutoML & MLOps** | Scikit-Learn, XGBoost, LightGBM, CatBoost, SHAP, Optuna, MLflow |
| **Task Queue & Cache** | Celery, Redis |
| **Database** | PostgreSQL (Metadata persistence) |
| **DevOps & Containerization** | Docker, Docker Compose, Nginx |

---

## 📁 Project Directory Structure

```text
Automated_AI_Data_Analyst/
├── backend/
│   ├── app/
│   │   ├── agents/          # Multi-agent implementations (Orchestrator, SQL, Reflection)
│   │   ├── core/            # App configurations, security, logging, exceptions
│   │   ├── database/        # DuckDB engine manager & PostgreSQL connections
│   │   ├── graphs/          # LangGraph state graph workflow builders
│   │   ├── models/          # SQLAlchemy database models
│   │   ├── repositories/    # Data layer abstraction repositories
│   │   ├── routers/         # FastAPI V1 API endpoints (upload, profile, sql, chat, clean)
│   │   ├── schemas/         # Pydantic request/response validation schemas
│   │   ├── services/        # Ingestion, Data Engine, LLM Factory, ML Services
│   │   ├── tasks/           # Celery background tasks
│   │   └── main.py          # FastAPI application entry point
│   ├── tests/               # Pytest unit and integration test suites
│   └── requirements.txt     # Python backend dependencies
├── frontend/
│   ├── src/                 # React UI source code (Components, API client, Store)
│   ├── package.json         # Node.js dependencies & scripts
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   └── vite.config.ts       # Vite bundler configuration
├── configs/                 # YAML configuration files (agent, ML, app settings)
├── docker/                  # Dockerfiles and docker-compose orchestration
│   ├── Dockerfile.backend
│   ├── Dockerfile.celery
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
└── .env.example             # Example environment variables template
```

---

## ⚙️ Environment Configuration

1. Copy `.env.example` to create your working `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```

2. Configure your secret keys and LLM API Credentials in `.env`:
   ```env
   PROJECT_NAME="Autonomous AI Data Analyst"
   
   # Database Configurations
   POSTGRES_USER=analyst_user
   POSTGRES_PASSWORD=analyst_password_secret
   POSTGRES_DB=autonomous_analyst_db
   
   # LLM API Credentials (Required for AI Agents & Text-to-SQL)
   GOOGLE_API_KEY=your_google_gemini_api_key
   GROQ_API_KEY=your_groq_api_key
   DEFAULT_LLM_PROVIDER=google
   DEFAULT_MODEL_NAME=gemini-1.5-pro
   FAST_MODEL_NAME=gemini-1.5-flash
   ```

---

## 🚀 How to Run the Project

### Option A: Using Docker Compose (Recommended)

Run the entire application stack (PostgreSQL, Redis, FastAPI Backend, Celery Worker, React Frontend, and MLflow) with a single command:

```bash
# 1. Build and start all services in detached mode
docker-compose -f docker/docker-compose.yml up --build -d

# 2. View running logs
docker-compose -f docker/docker-compose.yml logs -f
```

#### Access Application Endpoints:
* 🌐 **Frontend Application**: `http://localhost:3000`
* 🔌 **Backend REST API Docs (Swagger)**: `http://localhost:8000/docs`
* 📈 **MLflow Tracking Dashboard**: `http://localhost:5000`

To stop all running services:
```bash
docker-compose -f docker/docker-compose.yml down
```

---

### Option B: Local Manual Setup (Development Mode)

If you prefer to run the backend and frontend separately for development:

#### 1. Backend Setup (FastAPI & Python)

```bash
# Navigate to backend directory
cd backend

# Create and activate a Python virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Launch FastAPI development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
> The API will be available at `http://localhost:8000` (Swagger UI at `/docs`).

#### 2. Frontend Setup (React & Vite)

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start Vite dev server
npm run dev
```
> The UI will be available at `http://localhost:5173`.

---

## 🧪 Running Tests

To execute the backend unit and integration test suite:

```bash
cd backend
pytest
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.