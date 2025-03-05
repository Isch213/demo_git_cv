{% test col_len(model, column_name,testlen) %}

with varcharcast as (
    select cast({{ column_name }} as varchar) as column_name
    from {{ model }}
)
    select *
    from varcharcast
    where length(column_name) > {{testlen}}

{% endtest %}