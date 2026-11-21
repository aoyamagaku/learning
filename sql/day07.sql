-- select  count(staff.store_id)
-- from staff

-- select  count(store.store_id)
-- from store;

-- select last_name, first_name, s.store_id
-- from staff, store as s
-- where s.store_id = staff.store_id; --2 строки как у стафа

select last_name, first_name, store.store_id
from store
join staff on staff.store_id = store.store_id;