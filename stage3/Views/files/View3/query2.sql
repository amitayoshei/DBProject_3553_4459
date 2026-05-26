SELECT locker_id, occupant_name, email, rental_end_date
FROM vw_locker_utilization
WHERE rental_end_date < DATE '2024-01-01'
  AND occupant_name IS NOT NULL;