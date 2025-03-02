with source as (
    select * from {{ source('raw', 'carrier_info') }}
)

select
    carrier_id,
    carrier_name,
    carrier_type,
    region
from source
