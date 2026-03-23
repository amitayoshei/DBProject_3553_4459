-- ------------------------------------------
-- Query 1: Get the body measurement with the lowest weight
-- ------------------------------------------
-- Method A: Using a Subquery
SELECT T.Name, M.Weight_Kg, M.BMI_Score, M.Fat_Percentage, M.Measurement_Date 
FROM BODY_MEASUREMENT M
JOIN TRAINEE_PROFILE T ON M.Trainee_ID = T.Trainee_ID
WHERE M.Trainee_ID = 1 
  AND M.Weight_Kg = (
      SELECT MIN(Weight_Kg) 
      FROM BODY_MEASUREMENT 
      WHERE Trainee_ID = 1
  );

-- Method B: Using ORDER BY and LIMIT
SELECT T.Name, M.Weight_Kg, M.BMI_Score, M.Fat_Percentage, M.Measurement_Date 
FROM BODY_MEASUREMENT M
JOIN TRAINEE_PROFILE T ON M.Trainee_ID = T.Trainee_ID
WHERE M.Trainee_ID = 1 
ORDER BY M.Weight_Kg ASC 
LIMIT 1;

-- ------------------------------------------
-- Query 2: List of exercises and info for a specific program
-- ------------------------------------------
-- Method A: Using JOIN
SELECT E.Exercise_Name, E.Equipment_Needed, I.Sets_Count, I.Reps_Count 
FROM EXERCISE E 
JOIN INCLUDES I ON E.Exercise_ID = I.Exercise_ID 
WHERE I.Program_ID = 1;

-- Method B: Using IN with a Subquery
SELECT 
    E.Exercise_Name, 
    E.Equipment_Needed,
    (SELECT I.Sets_Count FROM INCLUDES I WHERE I.Exercise_ID = E.Exercise_ID AND I.Program_ID = 1) AS Sets_Count,
    (SELECT I.Reps_Count FROM INCLUDES I WHERE I.Exercise_ID = E.Exercise_ID AND I.Program_ID = 1) AS Reps_Count
FROM EXERCISE E 
WHERE E.Exercise_ID IN (
    SELECT Exercise_ID 
    FROM INCLUDES 
    WHERE Program_ID = 1
);

-- ------------------------------------------
-- Query 3: Active trainees in February 2025
-- ------------------------------------------
-- Method A: Using JOIN and DISTINCT
SELECT DISTINCT T.Trainee_ID, T.Name, T.Gender, T.Join_Date 
FROM TRAINEE_PROFILE T 
JOIN WORKOUT_LOG W ON T.Trainee_ID = W.Trainee_ID 
WHERE EXTRACT(MONTH FROM W.Log_Date) = 2 
      AND EXTRACT(YEAR FROM W.Log_Date) = 2025;

-- Method B: Using EXISTS
SELECT Trainee_ID, T.Name, Gender, Join_Date 
FROM TRAINEE_PROFILE T 
WHERE EXISTS (
    SELECT 1 
    FROM WORKOUT_LOG W 
    WHERE W.Trainee_ID = T.Trainee_ID 
      AND EXTRACT(MONTH FROM W.Log_Date) = 2 
      AND EXTRACT(YEAR FROM W.Log_Date) = 2025
)
ORDER BY Trainee_ID;

-- ------------------------------------------
-- Query 4: Total number of lockers for trainees who own at least one VIP locker
-- ------------------------------------------
-- Method A: Using JOIN, GROUP BY, and an IN subquery for filtering (Efficient)
SELECT 
    T.Trainee_ID, 
    T.Name, 
    COUNT(L.Locker_ID) AS Total_Lockers
FROM TRAINEE_PROFILE T
JOIN Locker L ON T.Trainee_ID = L.Trainee_ID
WHERE T.Trainee_ID IN (
    SELECT Trainee_ID 
    FROM Locker 
    WHERE Location_Zone = 'VIP Zone'
)
GROUP BY T.Trainee_ID, T.Name
ORDER BY T.Trainee_ID;

-- Method B: Using Correlated Subqueries in SELECT and WHERE (Inefficient)
SELECT 
    T.Trainee_ID, 
    T.Name, 
    (
        SELECT COUNT(*) 
        FROM Locker L 
        WHERE L.Trainee_ID = T.Trainee_ID
    ) AS Total_Lockers
FROM TRAINEE_PROFILE T
WHERE EXISTS (
    SELECT 1 
    FROM Locker L_VIP 
    WHERE L_VIP.Trainee_ID = T.Trainee_ID 
      AND L_VIP.Location_Zone = 'VIP Zone'
);

-- ------------------------------------------
-- Query 5: Monthly summary of calories and heart rate
-- ------------------------------------------
SELECT 
    EXTRACT(MONTH FROM Log_Date) AS Workout_Month, 
    COUNT(Log_ID) AS Total_Workouts, 
    SUM(Total_Calories_Burned) AS Total_Calories, 
    ROUND(AVG(Average_Heart_Rate), 1) AS Avg_Heart_Rate 
FROM WORKOUT_LOG 
WHERE Trainee_ID = 1 
  AND EXTRACT(YEAR FROM Log_Date) = 2026 
GROUP BY EXTRACT(MONTH FROM Log_Date) 
ORDER BY Workout_Month;

-- ------------------------------------------
-- Query 6: Trainees with expiring health declarations but active locker rentals
-- ------------------------------------------
SELECT 
    T.Trainee_ID, 
    T.Name, 
    H.expiry_date AS Health_Expiry, 
    L.Locker_ID, 
    L.Rental_End_Date,
    (L.Rental_End_Date - H.expiry_date) AS Days_At_Risk
FROM TRAINEE_PROFILE T 
JOIN HEALTH_DECLARATION H ON T.Trainee_ID = H.Trainee_ID
JOIN Locker L ON T.Trainee_ID = L.Trainee_ID 
WHERE H.expiry_date <= '2026-05-01'
  AND L.Rental_End_Date > H.expiry_date
ORDER BY Days_At_Risk;

-- ------------------------------------------
-- Query 7: Full measurement history for a specific trainee
-- ------------------------------------------
SELECT 
    T.Name, 
    M.Measurement_Date, 
    M.Weight_Kg, 
    M.BMI_Score, 
    M.Fat_Percentage 
FROM BODY_MEASUREMENT M
JOIN TRAINEE_PROFILE T ON M.Trainee_ID = T.Trainee_ID
WHERE M.Trainee_ID = 6
ORDER BY M.Measurement_Date DESC;

-- ------------------------------------------
-- Query 8: Popularity of training programs based on logs
-- ------------------------------------------
SELECT 
    P.Program_Name, 
    P.Workout_Type, 
    COUNT(W.Log_ID) AS Times_Performed, 
    COALESCE(SUM(W.Duration_Minutes), 0) AS Total_Minutes_Spent 
FROM TRAINING_PROGRAM P 
LEFT JOIN WORKOUT_LOG W ON P.Program_ID = W.Program_ID 
GROUP BY P.Program_ID, P.Program_Name, P.Workout_Type 
ORDER BY Times_Performed DESC;