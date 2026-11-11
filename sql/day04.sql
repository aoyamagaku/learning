-- SELECT first_name, last_name,
-- 	sum(amount) as total
-- FROM customer
-- JOIN payment ON customer.customer_id = payment.customer_id
-- GROUP BY customer.customer_id, first_name, last_name
-- ORDER BY total desc
-- LIMIT 5;

-- SELECT name, COUNT(film_id) as total
-- from category
-- JOIN film_category ON film_category.category_id = category.category_id
-- GROUP BY category.category_id, name
-- HAVING COUNT(film_id) > 60
-- order by total desc


-- SELECT last_name
-- FROM actor
-- WHERE last_name ~'(.)\1'

-- select rating, rental_duration, count(film_id) as total
-- from film
-- group by rating, rental_duration
-- order by rating, rental_duration;

-- select customer_id,
--        count(amount) as paymnets_count,
--        sum(amount) as sum_payment,
--        round(avg(amount), 2) as average,
--        min(amount) as min_payment,
--        max(amount) as max_payment
-- from payment
-- group by customer_id;

-- select count(*), count(return_date)
-- from rental;
-- --потому что не все вернули еще

-- select rental.customer_id,
--        count(rental.rental_id) as count_of_rental,
--        round(avg(amount), 2) as average_amount
-- from rental
-- join payment on payment.rental_id = rental.rental_id
-- join customer on rental.customer_id = customer.customer_id
-- where activebool = true
-- group by rental.customer_id
-- having count(rental.rental_id) > 35 and avg(amount) > 4
-- order by count_of_rental, average_amount;
-- where сразу отделяет, having, group by меньше сортирует
