![ToyRMS Banner](assets/banner.svg)

# Toy RMS

A toy, end-to-end Financial Risk Management System (RMS) built in Python — covering the full lifecycle from automated vendor data ingestion to interactive dashboards for traders and risk managers.

## Ideas for Features & Tech Stack

### Infrastructure & DevOps

- **Containerization**: **Docker & Docker Compose** for ecosystem orchestration.
- **Infrastructure as Code**: **Terraform** for defining reproducible environments.
- **CI/CD & Dev Environments**: **GitHub Actions** for automated builds, **Nox** for multi-environment testing, and **pre-commit** hooks for local code quality.
- **Observability**: Structured logging via **Loguru** and system health monitoring.

### Data Pipeline & Orchestration

- **Orchestration**: Fully managed pipelines using **Dagster**.
- **Ingestion**: High-concurrency fetching using **asyncio** from free market data sources (**yfinance**, **marketdata.app**) and simulated **JSON** trade payloads.
- **Caching**: Performance optimization via **Redis** for market data and pricing result persistence.
- **Schema Contracts & Processing**: Strict schema enforcement between systems using **Pydantic** and dataframe validation via **Pandera**, with lightning-fast transformations using **Polars**.
- **Historization**: ACID-compliant snapshots and "Time Travel" using **Delta Lake** (via **delta-rs**) for reliable T-n auditability.
- **Storage**: High-performance, in-memory storage using **DuckDB** and **SQLite**, with **MongoDB** for persistent OTC trade storage and **DVC** for data versioning.


### Pricing & Risk Engine

- **Core Engine**: Full-featured **OTC trade pricing** using **QuantLib**.
- **Performance**: Compute-heavy components like IV calculation implemented in **Rust** (via **PyO3**/**Maturin**) and **C++** (via **nanobind**/**litgen**) for maximum efficiency.
- **Analytics**: Mark-to-Market (MtM), Greeks/Sensitivities, and Risk Metrics (VaR, CVaR).
- **Stress Testing**: **Scenario Analysis** for historical market crashes and custom portfolio shocks.

### Results Access & Visualization

- **API**: High-performance REST interface using **FastAPI** to expose risk metrics on demand.
- **AI Risk Analyst**: Agentic analysis using **Pydantic AI** for natural language querying of portfolio risk and automated "plain-English" explanations of VaR breaches.
- **Interactive Dashboards**: Built with **Streamlit**, featuring:
  - **Zero-Latency Analytics**: SQL querying directly in the browser using **DuckDB-WASM**.
  - **Financial Charting**: Dynamic **Plotly**-based yield curves, risk heatmaps, and P&L attribution.
  - **Portfolio Explorer**: Hierarchical "slice-and-dice" views to aggregate risk by desk, asset class, or counterparty.
  - **Hedging Simulator**: **"What-if" analysis** to test hedging strategies and visualize their impact on portfolio risk.
- **Reporting**: Professional, static risk reports generated via **Quarto**, with automated deployment of example pages to **GitHub Pages**.
