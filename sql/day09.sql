-- select first_name, last_name, sum(amount)
-- from customer
-- join payment on payment.customer_id = customer.customer_id
-- group by customer.customer_id
-- order by sum(amount) desc
-- limit 5;

-- select first_name, last_name, sum(amount)
-- from customer
-- join payment on payment.customer_id = customer.customer_id
-- group by customer.customer_id
-- order by sum(amount) desc
-- limit 5 offset 5;

-- select title, length
-- from film
-- where length > (select avg(length) from film)
-- order by length desc;

-- select payment_id,
--        amount,
--        round((select avg(amount)from payment),2) as avg_amount,
--        round(amount - (select avg(amount) from payment), 2) as diff
-- from payment;
