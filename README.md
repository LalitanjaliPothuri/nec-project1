# AI-Driven Customer Analytics Platform

An end-to-end Streamlit dashboard for customer analytics, segmentation, churn prediction, purchase forecasting, product recommendation, and inventory alerts.

## Features

- Customer segmentation with K-Means clusters
- Churn prediction for customer retention insights
- Purchase value prediction and top-product recommendations
- Inventory low-stock alerts from product data
- Interactive visualizations for demographics, spending, and segments
- Data upload and merge support for new customer datasets
- PDF report generation and updated dataset export

## Requirements

- Python 3.9+
- `streamlit`, `pandas`, `numpy`, `scikit-learn`, `plotly`, `matplotlib`, `joblib`, `fpdf`, `openpyxl`

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app.py
```

Open the local Streamlit link shown in the terminal to access the dashboard.

## Deploy on Render

1. Push this repository to a Git service such as GitHub.
2. Create a new web service on Render and connect your repository.
3. Render will use `render.yaml`, `runtime.txt`, and `requirements.txt`.
4. Build command:

```bash
pip install -r requirements.txt
```

5. Start command:

```bash
streamlit run app.py --server.port $PORT --server.enableCORS false
```

6. After deployment, Render will provide a live app URL. Use that URL to access the dashboard.

## Data

- `data/old_customers.csv` – legacy customer dataset used by the dashboard
- `data/products.csv` – product inventory dataset for alerts and recommendations

If these files are missing, the app generates sample data automatically when started.

## Output

- `outputs/updated_dataset.csv` – saved merged customer dataset after upload/merge actions
- `reports/` – generated PDF reports when the report feature is used

## Project structure

- `app.py` – Streamlit application entrypoint
- `create_dataset.py` – sample dataset generation helper
- `src/` – data processing, analytics, visualization, and report modules.