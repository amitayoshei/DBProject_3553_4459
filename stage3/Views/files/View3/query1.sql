SELECT locker_id, location_zone
FROM vw_locker_utilization
WHERE occupant_name IS NULL 
  AND location_zone = 'Pool Area';