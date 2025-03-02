with flight_metrics as (
    select * from {{ ref('int_flight_metrics') }}
),
airports as (
    select * from {{ ref('stg_airports') }}
)

select
    flight_metrics.flight_id,
    flight_metrics.carrier_id,
    flight_metrics.carrier_name,
    flight_metrics.origin_airport_id,
    origin.city as origin_city,
    origin.state as origin_state,
    flight_metrics.dest_airport_id,
    dest.city as dest_city,
    dest.state as dest_state,
    flight_metrics.flight_date,
    flight_metrics.year,
    flight_metrics.month,
    flight_metrics.passengers,
    flight_metrics.seats,
    flight_metrics.load_factor,
    flight_metrics.is_full_flight,
    flight_metrics.distance,
    -- Additional metrics
    case
        when flight_metrics.distance < 500 then 'Short haul'
        when flight_metrics.distance < 1500 then 'Medium haul'
        else 'Long haul'
    end as flight_type
from flight_metrics
left join airports as origin on flight_metrics.origin_airport_id = origin.airport_id
left join airports as dest on flight_metrics.dest_airport_id = dest.airport_id
