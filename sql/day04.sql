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