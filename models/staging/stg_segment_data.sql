with source as (
    select * from {{ source('raw', 'segment_data') }}
)

select
    flight_id,
    carrier_id,
    origin_airport_id,
    dest_airport_id,
    aircraft_type_id,
    year,
    month,
    flight_date,
    passengers,
    seats,
    payload_weight,
    distance
from source
where flight_date is not null
