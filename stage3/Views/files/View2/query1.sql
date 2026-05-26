SELECT first_name, last_name, age, main_goal
FROM vw_trainee_fitness_profile
WHERE age >= 40 
  AND main_goal = 'Weight Loss'
  AND medical_clearance = 1;