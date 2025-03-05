with names as (
    select * from {{source('raw','json_names')}}
)
select * from names
