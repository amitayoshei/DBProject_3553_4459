CREATE OR REPLACE VIEW vw_trainee_fitness_profile AS
SELECT 
    cu.user_id,
    cu.first_name,
    cu.last_name,
    tm.gender,
    tm.main_goal,
    EXTRACT(YEAR FROM AGE(DATE '2024-01-01', tm.date_of_birth)) AS age,
    hd.doctor_name,
    hd.limitations_notes,
    hd.is_valid AS medical_clearance
FROM public.core_user cu
JOIN public.trainee_metadata tm ON cu.user_id = tm.user_id
LEFT JOIN public.health_declaration hd ON cu.user_id = hd.user_id;