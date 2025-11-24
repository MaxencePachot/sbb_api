# SBB & Weather Data Pipeline - Zug, Switzerland

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/Azure-Data_Lake-blue)](https://azure.microsoft.com/)
[![Databricks](https://img.shields.io/badge/Databricks-PySpark-orange)](https://databricks.com/)

## Overview

This project collects and processes **SBB train data** for **Zug, Switzerland** along with **weather data**. The goal is to create a pipeline from **data ingestion to predictive modeling** using **Azure, ADLS, Databricks and PySpark**.

![project_presentation](assets/project_presentation.png)

---

## Workflow

1. **Data Ingestion**
   - Retrieve SBB train data for Zug via API.
   - Retrieve weather data (snow, rain, temperature, etc.).
   - Store JSON files securely in **Azure Data Lake Storage (ADLS)**.

2. **Databricks Pipeline**
   - Load data from ADLS into Databricks.
   - Apply **Bronze → Silver → Gold** architecture:
     - **Bronze**: raw ingested files
     - **Silver**: cleaned and enriched datasets
     - **Gold**: aggregated tables for analytics and modeling

---

## Key Technologies

- **Python**: data ingestion scripts  
- **Azure Data Lake Storage (ADLS)**: secure cloud storage  
- **Databricks / PySpark**: scalable ETL pipelines

---

## ⚠️ Project Context & Constraints (Must Read)

This project was developed within a **30-day Azure Free Trial window**. As a result, certain architectural decisions favored rapid prototyping over strict production standards.

### Known Limitations & Production Roadmap
*If this project were to be moved to a production environment, the following changes would be prioritized:*

### 1. Code Structure & Testing
* **Current State:** Logic resides primarily in Databricks Notebooks (`.ipynb`) for interactive development.
* **Production Target:** Core transformation logic would be extracted into **Python modules (`.py` / `src/`)** packaged as Wheels (`.whl`).
    * *Why:* To enable **Unit Testing** (pytest) and proper **CI/CD** pipelines, keeping Notebooks only for orchestration and visualization.

### 2. Security & Secrets Management
* **Current State:** Secrets are managed via local environment variables or excluded config files (not committed).
* **Production Target:** Integration with **Azure Key Vault** linked to **Databricks Secret Scopes**.
    * *Note:* Direct integration between Key Vault and Databricks requires the *Premium Tier* workspace, which was outside the budget of this prototype.

### 3. Infrastructure as Code (IaC)
* **Current State:** Resources created via Azure Portal (ClickOps).
* **Production Target:** Infrastructure (ADLS containers, Databricks Workspaces, Clusters) defined in **Terraform** or **Azure Bicep** for reproducible deployments.

### 4. Orchestration
* **Current State:** Manual triggers / Notebook execution.
* **Production Target:** End-to-end pipeline orchestration using **Azure Data Factory (ADF)** or **Databricks Workflows** to schedule ingestion -> bronze -> silver -> gold jobs.

---

## 📂 Repository Structure

```bash
├── adls_connection.py         # Utility for ADLS connectivity (Mounting/Auth)
├── bronze_notebook_sbb.ipynb  # Raw ingestion to Bronze Layer (Trains)
├── silver_notebook_sbb.ipynb  # Cleaning & Schema enforcement (Trains)
├── bronze_notebook_weather.ipynb # Raw ingestion to Bronze Layer (Weather)
├── silver_notebook_weather.ipynb # Cleaning & Schema enforcement (Weather)
├── main.py                    # Local ingestion script entry point
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

## 🚀 How to Run (Concept)

> **Note:** This project requires an active Azure Subscription and a Databricks Workspace.

1. **Setup Environment**
```bash
   pip install -r requirements.txt
```

2. **Configure Credentials**  
   Create a `secrets/` folder (gitignored) or set environment variables for:
   * `SBB_API_KEY`
   * `AZURE_STORAGE_ACCOUNT_KEY`

3. **Run Ingestion**  
   Execute the python script to fetch data and push to ADLS Landing zone:
```bash
   python main.py
```

4. **Run Pipeline**  
   Import the notebooks into Databricks and execute in order:
   1. `bronze_notebook_*.ipynb`
   2. `silver_notebook_*.ipynb`

## 👤 Author

Maxence Pachot
[![My site]]([https://databricks.com/](https://pachotmaxence.com/))
[![Linkedin]](https://www.linkedin.com/in/maxence-pachot-6801761b7/)
