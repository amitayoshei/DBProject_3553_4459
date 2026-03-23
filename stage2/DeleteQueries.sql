-- ------------------------------------------
-- DELETE 1: Clean up demo workout logs recorded on a day the gym was closed for renovations
-- ------------------------------------------
DELETE FROM WORKOUT_LOG
WHERE EXTRACT(DAY FROM Log_Date) = 15 
  AND EXTRACT(MONTH FROM Log_Date) = 8
  AND EXTRACT(YEAR FROM Log_Date) = 2024
  AND Trainee_ID IN (
      SELECT Trainee_ID 
      FROM TRAINEE_PROFILE 
      WHERE EXTRACT(YEAR FROM Join_Date) = 2024
  );

-- ------------------------------------------
-- DELETE 2: Remove high weight measurements for female trainees
-- ------------------------------------------
DELETE FROM BODY_MEASUREMENT
WHERE Weight_Kg > 115
  AND Trainee_ID IN (
      SELECT Trainee_ID
      FROM TRAINEE_PROFILE
      WHERE Gender = 'Female'
  );

-- ------------------------------------------
-- DELETE 3: Delete goals for inactive users (no workouts logged since the beginning of 2026)
-- ------------------------------------------
DELETE FROM TRAINEE_GOAL
WHERE Trainee_ID NOT IN (
    SELECT DISTINCT Trainee_ID 
    FROM WORKOUT_LOG 
    WHERE EXTRACT(YEAR FROM Log_Date) >= 2026
);