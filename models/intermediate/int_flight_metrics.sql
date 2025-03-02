with segments as (
    select * from {{ ref('stg_segment_data') }}
),
carriers as (
    select * from {{ ref('stg_carriers') }}
)

select 
    segments.flight_id,
    segments.carrier_id,
    carriers.carrier_name,
    segments.origin_airport_id,
    segments.dest_airport_id,
    segments.flight_date,
    segments.year,
    segments.month,
    segments.passengers,
    segments.seats,
    segments.payload_weight,
    segments.distance,
    -- Calculate metrics
    (segments.passengers / nullif(segments.seats, 0))::float as load_factor,
    case 
        when segments.seats = 0 then 0 
        when segments.passengers/segments.seats > 0.9 then 1 
        else 0 
    end as is_full_flight
from segments
left join carriers on segments.carrier_id = carriers.carrier_id
