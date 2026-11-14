select name, round(avg(length),1) as avg_length
from film
join film_category on film_category.film_id = film.film_id
join category on film_category.category_id = category.category_id
group by name
having avg(length) > 115
order by avg(length) desc;