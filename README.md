![ToyRMS Banner](assets/banner.svg)

# Toy RMS

A toy model for risk management system (RMS) using Python.

## Features

- data orchestration using Dagster
- simulated ingestion of external data sources (XML trade data payloads, CSV market data, Yahoo Finance API)
- data storage using DuckDB and MongoDB
- data validation, processing, and transformation using Pydantic and Polars
- financial instruments pricing using QuantLib
- Mark to Market (MtM) calculations for traded securities
- pricing OTC derivatives using QuantLib and market implied parameters
- sensitivities calculations
- risk metrics calculations (VaR, CVaR, etc.)
- risk reporting using Quarto

## Roadmap

- [ ] Set up Dagster for data orchestration
- [ ] Simulate data ingestion from external sources
- [ ] Implement data storage with DuckDB and MongoDB
