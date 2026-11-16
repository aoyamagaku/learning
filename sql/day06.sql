-- Вывести: название страны и сумму всех платежей клиентов из неё.
-- Условие: только 10 стран с самой большой суммой.
-- Сортировка: от большей суммы к меньшей.
-- Таблицы и связи, цепочка из пяти таблиц:
-- payment → customer по customer_id;
-- customer → address по address_id;
-- address → city по city_id;
-- city → country по country_id.
-- Где данные: сумма — payment.amount, название страны — country.country.
-- Проверка: ровно 10 строк, суммы по убыванию,
-- на первом месте India.
-- Новое здесь только длина цепочки.
-- Каждый JOIN пишется так же, как в задаче с категориями,
-- просто их четыре подряд.

select country, sum(payment.amount) as biggest_sum
from country
join city on city.country_id = country.country_id
join address on address.city_id = city.city_id
join customer on customer.address_id = address.address_id
join payment on payment.customer_id = customer.customer_id
group by country
order by biggest_sum desc
limit 10