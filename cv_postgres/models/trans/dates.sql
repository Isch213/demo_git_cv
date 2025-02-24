with dates as (
    select * from {{source('raw','lis_dates')}}
)
,casts as (
    select dates::date as dates
    from dates
)
,add_columns as (
    select *
    ,extract(year from dates)::int as years
    ,extract(month from dates)::int as months
    ,extract(day from dates)::int as days
    ,extract(year from dates)*100 + extract(month from dates) as yearmonths
    from casts
)
select *
from add_columns

