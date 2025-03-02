import pandas as pd
import os

# Path to your downloaded CSV (update this to your actual filename)
input_file = 'T_T100_SEGMENT_ALL_CARRIER.csv'  # Update with your actual filename
output_directory = 'processed_data'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Read the raw data
print("Reading CSV file...")
df = pd.read_csv(input_file)

# Clean column names (make lowercase)
print("Cleaning data...")
df.columns = [c.lower() for c in df.columns]

# Extract segment data with your available columns
segment_data = df[['unique_carrier', 'origin', 'dest', 'aircraft_type', 
                   'year', 'month', 'passengers', 'seats', 'payload']]

# Create a date column
segment_data['flight_date'] = pd.to_datetime(
    segment_data['year'].astype(str) + '-' + 
    segment_data['month'].astype(str) + '-01'
)

# Rename columns to match our schema
segment_data = segment_data.rename(columns={
    'unique_carrier': 'carrier_id',
    'origin': 'origin_airport_id',
    'dest': 'dest_airport_id',
    'aircraft_type': 'aircraft_type_id',
    'payload': 'payload_weight'
})

# Add distance if missing
if 'distance' not in df.columns:
    segment_data['distance'] = 0  # Placeholder, we'll calculate this in dbt

# Extract unique carriers
carriers = df[['unique_carrier', 'unique_carrier_name']].drop_duplicates()
carriers = carriers.rename(columns={
    'unique_carrier': 'carrier_id',
    'unique_carrier_name': 'carrier_name'
})
# Add placeholder columns for carrier_type and region
carriers['carrier_type'] = 'Unknown'
carriers['region'] = 'USA'

# Extract unique airports
airports = pd.concat([
    df[['origin', 'origin_city_name', 'origin_state_abr']].rename(
        columns={'origin': 'airport_id', 'origin_city_name': 'city', 'origin_state_abr': 'state'}
    ),
    df[['dest', 'dest_city_name', 'dest_state_abr']].rename(
        columns={'dest': 'airport_id', 'dest_city_name': 'city', 'dest_state_abr': 'state'}
    )
]).drop_duplicates()

airports['airport_name'] = airports['airport_id'] + ' Airport'
airports['country'] = 'USA'

# Save to CSV files
print("Saving files...")
segment_data.to_csv(f'{output_directory}/segment_data.csv', index=False)
carriers.to_csv(f'{output_directory}/carrier_info.csv', index=False)
airports.to_csv(f'{output_directory}/airport_info.csv', index=False)

print("Done! Files saved to", output_directory)
