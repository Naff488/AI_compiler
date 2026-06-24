# 🤖 AI App Compiler

An AI-powered application compiler that converts natural language prompts into a structured application blueprint.

Users can describe an application idea in plain English, and the system automatically generates:

* Application intent
* System design
* Database schema
* API schema
* UI schema
* Role-based access permissions
* Validation reports
* Runtime execution results
* Failure analysis

---

## 🚀 Overview

AI App Compiler transforms natural language into a complete application configuration pipeline.

Example:

**Input**

```
Build a CRM with login, contacts, dashboard, role-based access, and premium plan with payments. Admins can see analytics.
```

**Output**

* Intent Extraction
* System Design
* UI Pages
* Database Tables
* API Endpoints
* Authentication Rules
* Validation Results
* Failure Analysis

---

## 🏗️ Architecture

```
User Prompt
     ↓
Intent Extractor
     ↓
Normalizer
     ↓
Intent Enricher
     ↓
Failure Handler
     ↓
System Designer
     ↓
Schema Generator
     ↓
Validator
     ↓
Repair Engine
     ↓
Runtime Executor
     ↓
Final Output
```

---

## ✨ Features

* Natural language application generation
* Multi-stage AI pipeline architecture
* Automatic role generation
* System design generation
* UI schema generation
* API schema generation
* Database schema generation
* Authentication permission generation
* Validation and repair mechanism
* Failure analysis
* Interactive Streamlit interface

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini API (Gemini 2.5 Flash)

### Libraries

* Pydantic
* python-dotenv
* Google Generative AI SDK

---

## 📂 Project Structure

```
ai_internship_project/

├── backend/
│   ├── pipeline/
│   ├── runtime/
│   ├── schemas/
│   ├── utils/
│   └── pipeline_controller.py

├── frontend/
│   └── app.py

├── datasets/

├── requirements.txt

├── .env

└── README.md
```

---

## ⚙️ Installation

### Clone repository

```bash
git clone https://github.com/Naff488/AI_compiler

cd ai_internship_project
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the application

```bash
streamlit run frontend/app.py
```

---

## 📸 Example Prompt

```
Build an e-commerce platform with products, cart, payments, subscriptions and admin dashboard.
```

---

## 📊 Example Output

* Pages
* Entities
* Roles
* UI Schema
* API Schema
* Database Schema
* Authentication Permissions
* Validation Results
* Runtime Output
* Failure Analysis

---

## 🔮 Future Improvements

* Export generated schemas as JSON
* Generate frontend code automatically
* Generate backend code automatically
* Docker deployment support
* Cloud deployment support
* Multi-model AI support

---

## 👩‍💻 Author

Built by Ayshath Nafida M H

B.Tech Information Technology Student

AI Internship Project (2026)
