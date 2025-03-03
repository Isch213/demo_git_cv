with dates as (
    select * from {{ref("s_dates")}}
)
,holidays as (
    select * from {{ref("s_holidays")}}
)
,joined as (
    select d.*
    ,h.holidayname as by_holidayname
    from dates d
    left join holidays h
    on d.dates = h.dates
)
select * from joined