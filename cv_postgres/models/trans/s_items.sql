with items as (
    select * from {{source('raw','items')}}
)

select 
item
,nr_in_store
,to_date(date,'dd.mm.yyyy') as date
 from items