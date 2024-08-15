# InforceTestTask

## Overview

This project demonstrates a simple ETL (Extract, Transform, Load) process using Python, PostgreSQL, and Docker. The ETL pipeline consists of three main steps:

1. **Data Generation**: Generates a CSV file with synthetic data.
2. **Data Transformation**: Cleans and transforms the data.
3. **Data Loading**: Loads the transformed data into a PostgreSQL database.

## Project Structure

```plaintext
InforceTestTask/
├── config/
│   └── db_config.py            # Database configuration
├── data/
│   ├── data.csv                # Generated CSV file (input)
│   └── transformed_data.csv    # Transformed CSV file (output)
├── queries/
│   ├── query1.sql              
│   ├── query2.sql              
│   ├── query3.sql              
│   ├── query4.sql              
│   └── query5.sql              
├── scripts/
│   ├── etl.py                  # Script to run the entire ETL process
│   ├── generate.py             # Script to generate synthetic data
│   ├── load.py                 # Script to load data into PostgreSQL
│   └── transform.py            # Script to transform data
├── sql/
│   ├── create_db.sql           # SQL script to create the database
│   └── create_table.sql        # SQL script to create tables
├── .env                        # Environment variables
├── docker-compose.yml          # Docker Compose file
├── Dockerfile                  # Dockerfile for the ETL application
└── requirements.txt            # Python dependencies
```
## Prerequisites
1. Install **Docker** on your machine.


## Setup Instructions
1. **Clone the Repository**: 
    ```bash
    git clone <repository-url>
    cd InforceTestTask
   ```
2. **Configure Environment Variables**:
    - Create a new file named `.env` in the root directory.
    - Add the following environment variables to the `.env` file:
        ```plaintext
        POSTGRES_USER=your_username
        POSTGRES_PASSWORD=your_password
        POSTGRES_DB=your_database
        POSTGRES_HOST=db
        POSTGRES_PORT=5432
        ```
3. **Build and start the Docker containers**:
    ```bash
    docker-compose up --build
    ```
4. **Stop the Docker containers**:
    ```bash
    docker-compose down
    ```
   

## Usage
1. **You can run individual scripts of ETL process**:
    - Generate data:
        ```bash
        docker-compose run etl python scripts/generate.py
        ```
    - Transform data:
        ```bash
        docker-compose run etl python scripts/transform.py
        ```
    - Load data into PostgreSQL database:
        ```bash
        docker-compose run etl python scripts/load.py
        ```
2. **You can run queries from the `queries` directory**:
    ```bash
    docker-compose run etl psql -U $POSTGRES_USER -d $POSTGRES_DB -f queries/query1.sql
    ```