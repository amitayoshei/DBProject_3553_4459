CREATE VIEW vw_locker_utilization AS
SELECT 
    l.locker_id,
    l.location_zone,
    l.rental_end_date,
    cu.user_id,
    cu.first_name || ' ' || cu.last_name AS occupant_name,
    cu.email
FROM public.locker l
LEFT JOIN public.core_user cu ON l.user_id = cu.user_id;