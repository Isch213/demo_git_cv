with names as (
    select
    name
    from {{ ref('s_names') }}
    where name in ('Max','Debra')
)
 
select count(name) as ct_name
from names
group by name
having count(*)>5
