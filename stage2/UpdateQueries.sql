-- ------------------------------------------
-- UPDATE 1: Ensuring that a log date is after the gym opened (2024-01-01), after the trainee joined, and before 2026-03-19.
-- ------------------------------------------
UPDATE WORKOUT_LOG
SET Log_Date = GREATEST('2024-01-01'::date, T.Join_Date) + 
               (random() * ('2026-03-19'::date - GREATEST('2024-01-01'::date, T.Join_Date)))::integer
FROM TRAINEE_PROFILE T
WHERE WORKOUT_LOG.Trainee_ID = T.Trainee_ID;

-- ------------------------------------------
-- UPDATE 2: Ensuring that a measurement is after the gym opened (2024-01-01), after the trainee joined, and before 2026-03-19.
-- ------------------------------------------
UPDATE BODY_MEASUREMENT
SET Measurement_Date = GREATEST('2024-01-01'::date, T.Join_Date) + 
                       (random() * ('2026-03-19'::date - GREATEST('2024-01-01'::date, T.Join_Date)))::integer
FROM TRAINEE_PROFILE T
WHERE BODY_MEASUREMENT.Trainee_ID = T.Trainee_ID;

-- ------------------------------------------
-- UPDATE 3: Ensuring that a goal was set after the gym opened (2024-01-01), after the trainee joined, and before 2026-03-19.
-- ------------------------------------------
UPDATE TRAINEE_GOAL
SET Creation_Date = GREATEST('2024-01-01'::date, T.Join_Date) + 
                 (random() * ('2026-03-19'::date - GREATEST('2024-01-01'::date, T.Join_Date)))::integer
FROM TRAINEE_PROFILE T
WHERE TRAINEE_GOAL.Trainee_ID = T.Trainee_ID;

-- ------------------------------------------
-- UPDATE 4: Set Target_Date relative to Creation_Date (30 to 365 days later)
-- ------------------------------------------
UPDATE TRAINEE_GOAL
SET Target_Date = Creation_Date + 30 + (random() * 335)::integer;

-- ------------------------------------------
-- UPDATE 5: Ensuring that male trainees are moved to the Men's Locker Room and female trainees are moved to the Women's Locker Room.
-- ------------------------------------------
UPDATE Locker
SET Location_Zone = CASE 
    WHEN Trainee_Profile.Gender = 'Male' THEN 'Men Locker Room'
    WHEN Trainee_Profile.Gender = 'Female' THEN 'Women Locker Room'
END
FROM Trainee_Profile
WHERE Locker.Trainee_ID = Trainee_Profile.Trainee_ID
  AND (
    (Trainee_Profile.Gender = 'Male' AND Locker.Location_Zone = 'Women Locker Room')
    OR 
    (Trainee_Profile.Gender = 'Female' AND Locker.Location_Zone = 'Men Locker Room')
  );

-- ------------------------------------------
-- UPDATE 6: Evaluate goals based on the latest measurement BEFORE or ON the target date
-- ------------------------------------------
UPDATE TRAINEE_GOAL G
SET Is_Achieved = COALESCE(
    (
        SELECT CASE 
                   WHEN M.Weight_Kg <= G.Target_Weight_Kg 
                    AND M.Fat_Percentage <= G.Target_Fat_Percentage 
                   THEN 1 
                   ELSE 0 
               END
        FROM BODY_MEASUREMENT M
        WHERE M.Trainee_ID = G.Trainee_ID
          AND M.Measurement_Date <= G.Target_Date
        ORDER BY M.Measurement_Date DESC
        LIMIT 1
    ), 
    0 -- Default to 0 if no valid measurement is found
);