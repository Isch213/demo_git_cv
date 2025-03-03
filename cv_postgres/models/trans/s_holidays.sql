with dates as (
    select * from {{source('raw','de_holidays')}}
)
,casts as (
    select
    date::date as dates
    ,holidayname::varchar(50) as holidayname
    ,subcountry::varchar(2) as subcountry

    from dates
)
select * from casts