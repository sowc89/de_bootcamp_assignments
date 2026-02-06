## Module 3 - Data Warehouse Module Assignment

This project contains scripts and SQL queries for the Data Engineering Zoomcamp Module 3: Data Warehouse. The goal is to ingest NYC Yellow Taxi trip data (Jan 2024 - Jun 2024), upload it to Google Cloud Storage (GCS), and perform analysis using BigQuery.

### Project Structure

- **`load_yellow_taxi_data.py`**: Python script to download Yellow Taxi Parquet files and upload them to a GCS bucket.
- **`bigquery_hw3.sql`**: SQL script containing queries to create External Tables, Partitioned/Clustered Tables, and perform analysis.
- **`gcp.json`**:Add this file to the project directory. This is the JSON file downloaded from GCP Console with GCP Service Account credentials.

### Prerequisites

- **Python 3.12+**
- **uv**: Python package manager. [Install uv](https://github.com/astral-sh/uv).
- **GCP Account**:
  - A GCS Bucket named `sow_dezoomcamp_hw3_2025` (script handles creation if permissions allow).
  - Service Account with Storage Admin and BigQuery Admin roles.
  - Download JSON key and save as `gcp.json` in this directory.

### Setup and Execution

1.  **Initialize Environment**:
    This project uses `uv` for dependency management.
    ```bash
    uv sync
    ```

2.  **Load Data to GCS**:
    Run the loader script to download data and upload to your GCS bucket.
    ```bash
    uv run load_yellow_taxi_data.py
    ```
    *Note: Ensure `gcp.json` is present in the project directory.*

3.  **BigQuery Analysis**:

   Based on the assignment questions, the following queries are executed in BigQuery:
   1.  Create External Table from GCS parquet files.
   2.  Create a standard (non-partitioned) table.
   3.  Create a Partitioned (by `tpep_dropoff_datetime`) and Clustered (by `VendorID`) table.
   4.  Run comparison queries to observe bytes processed differences.