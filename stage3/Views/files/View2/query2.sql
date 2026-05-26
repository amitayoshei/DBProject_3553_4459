SELECT user_id, first_name, last_name, limitations_notes
FROM vw_trainee_fitness_profile
WHERE medical_clearance = 0 OR medical_clearance IS NULL;