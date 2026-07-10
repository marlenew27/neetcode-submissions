-- Write your query below
with customer_purchase_cte as (
    select customer_id, array_agg(distinct product_name) as products
    from orders 
    group by customer_id
)
select customer_id, customer_name
from customers
where customer_id in (
    select customer_id 
    from customer_purchase_cte 
    where 'A' = ANY(products) and 'B' = ANY(products) and NOT ('C' = ANY(products))
)
order by customer_name;