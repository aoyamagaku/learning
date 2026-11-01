-- select title,
--        rental_rate,
--        replacement_cost,
--        replacement_cost / rental_rate AS "До окупаемости"
-- from film
-- order by "До окупаемости" desc;

-- select first_name, last_name,
--        create_date,
--        'old client' AS segment,
--        2026 AS check_year,
--        True AS is_checked
-- from customer
-- where create_date < DATE '2023-03-01';
--
-- select min(create_date), max(create_date)
-- from customer;
--
-- 'Значения' "Объекты"

-- select INITCAP(first_name || ' ' || last_name) as full_name,
--        length(first_name || ' ' || last_name) as name_length
-- from actor
-- order by name_length desc;

-- select email, split_part(email, '@', 2) as domain
-- from customer;

-- select distinct rating
-- from film;

-- select distinct rating, rental_duration
-- from film
-- order by rating, rental_duration;

-- select title, length, rating
-- from film
-- where length > 120 AND
--         (rating = 'G' or rating = 'PG');