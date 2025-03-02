# Flights Data Engineering Project

A data pipeline that transforms raw US domestic flight data (T-100) into analytics-ready models using modern data engineering techniques.

## Technologies Used
- PostgreSQL (database)
- dbt (data transformation)
- Python (data processing)
- Git (version control)

## Data Source
This project uses the Bureau of Transportation Statistics' T-100 Domestic Market data, which contains monthly domestic non-stop segment data reported by US carriers. The dataset includes information on:
- Carriers (airlines)
- Origins and destinations
- Aircraft types
- Passengers, seats, and payload data

## Data Structure
The project follows a modern analytics engineering approach with three distinct layers:
- **Staging models**: Clean interfaces to source data 
- **Intermediate models**: Business logic and metrics calculations
- **Mart models**: Analytics-ready tables organized by domain

## Key Features
- Calculates flight performance metrics (load factors)
- Creates relationship between flights and airports
- Categorizes flights by distance (short/medium/long haul)
- Implements a star schema design for efficient analytics
