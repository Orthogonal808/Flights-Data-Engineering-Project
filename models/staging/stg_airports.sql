with source as (
    select * from {{ source('raw', 'airport_info') }}
)

select
    airport_id,
    airport_name,
    city,
    state,
    country
from source
