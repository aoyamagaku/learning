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

-- select count(rental_id)
-- from rental;

-- select title, rating
-- from film
-- where rating not IN ('G', 'PG-13', 'PG');

-- select count(*)
-- from rental
-- where return_date is NULL;

-- select first_name, last_name
-- from actor
-- where last_name like 'S%N';
--
-- select first_name, last_name
-- from actor
-- where first_name like '____';

-- select title
-- from film
-- where lower(title) like '%love%';

-- create or replace function customer_tier(p_customer_id INT)
-- returns varchar
-- language plpgsql
-- as $$
-- declare
--     rental_count INT;
-- begin
--     select count(*)
--     into rental_count
--     from rental
--     where customer_id = p_customer_id
--
--     if rental_count >= 30 then
--         return 'Gold';
--     elsif rental_count >= 20 then
--         return 'Silver';
--     else
--         return 'Bronze';
--     end if;
-- end;
-- $$;

-- create or replace function film_length_category(p_film_id INT)
-- returns varchar
-- language plpgsql
-- as $$
-- declare
--     film_length INT;
-- begin
--     select length
--     into film_length
--     from film
--     where film_id = p_film_id;
--
--     return case
--         when film_length < 60 then 'Short'
--         when film_length <= 120 then 'Medium'
--         else 'Long'
--     end;
-- end;
-- $$;

-- select title
-- from film
-- where title ~ '^[A-Z]+ [A-Z]+$';

-- select last_name, first_name
-- from actor
-- where last_name ~ '([A-Z])\1';

-- select rental_id, rental_date, return_date
-- from rental
-- order by return_date is null desc , rental_date desc;