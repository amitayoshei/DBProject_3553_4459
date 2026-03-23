-- ==========================================
-- PART 1: SELECT QUERIES
-- ==========================================

-- ------------------------------------------
-- Query 1: Get the latest body measurement
-- ------------------------------------------
-- Method A: Using a Subquery
SELECT Weight_Kg, BMI_Score, Fat_Percentage, Measurement_Date 
FROM BODY_MEASUREMENT 
WHERE Trainee_ID = 1 
  AND Measurement_Date = (
      SELECT MAX(Measurement_Date) 
      FROM BODY_MEASUREMENT 
      WHERE Trainee_ID = 1
  );

-- Method B: Using ORDER BY and LIMIT
SELECT Weight_Kg, BMI_Score, Fat_Percentage, Measurement_Date 
FROM BODY_MEASUREMENT 
WHERE Trainee_ID = 1 
ORDER BY Measurement_Date DESC 
LIMIT 1;

-- ------------------------------------------
-- Query 2: List of exercises and equipment for a specific program
-- ------------------------------------------
-- Method A: Using JOIN
SELECT E.Exercise_Name, E.Equipment_Needed 
FROM EXERCISE E 
JOIN INCLUDES I ON E.Exercise_ID = I.Exercise_ID 
WHERE I.Program_ID = 1;

-- Method B: Using IN with a Subquery
SELECT Exercise_Name, Equipment_Needed 
FROM EXERCISE 
WHERE Exercise_ID IN (
    SELECT Exercise_ID 
    FROM INCLUDES 
    WHERE Program_ID = 1
);

-- ------------------------------------------
-- Query 3: Active trainees in February 2024
-- ------------------------------------------
-- Method A: Using JOIN and DISTINCT
SELECT DISTINCT T.Trainee_ID, T.Gender, T.Join_Date 
FROM TRAINEE_PROFILE T 
JOIN WORKOUT_LOG W ON T.Trainee_ID = W.Trainee_ID 
WHERE EXTRACT(MONTH FROM W.Log_Date) = 2 
  AND EXTRACT(YEAR FROM W.Log_Date) = 2024;

-- Method B: Using EXISTS
SELECT Trainee_ID, Gender, Join_Date 
FROM TRAINEE_PROFILE T 
WHERE EXISTS (
    SELECT 1 
    FROM WORKOUT_LOG W 
    WHERE W.Trainee_ID = T.Trainee_ID 
      AND EXTRACT(MONTH FROM W.Log_Date) = 2 
      AND EXTRACT(YEAR FROM W.Log_Date) = 2024
);

-- ------------------------------------------
-- Query 4: Compare current weight to target weight
-- ------------------------------------------
-- Method A: Using JOIN
SELECT M.Measurement_Date, M.Weight_Kg, G.Target_Weight_Kg 
FROM BODY_MEASUREMENT M 
JOIN TRAINEE_GOAL G ON M.Trainee_ID = G.Trainee_ID 
WHERE M.Trainee_ID = 1;

-- Method B: Using a Correlated Subquery
SELECT M.Measurement_Date, M.Weight_Kg, 
       (SELECT G.Target_Weight_Kg 
        FROM TRAINEE_GOAL G 
        WHERE G.Trainee_ID = M.Trainee_ID LIMIT 1) AS Target_Weight_Kg
FROM BODY_MEASUREMENT M 
WHERE M.Trainee_ID = 1;

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
  AND EXTRACT(YEAR FROM Log_Date) = 2024 
GROUP BY EXTRACT(MONTH FROM Log_Date) 
ORDER BY Workout_Month;

-- ------------------------------------------
-- Query 6: Program details (over 45 mins) by muscle group
-- ------------------------------------------
SELECT 
    P.Program_Name, 
    M.Group_Name, 
    COUNT(I.Exercise_ID) AS Total_Exercises 
FROM TRAINING_PROGRAM P 
JOIN INCLUDES I ON P.Program_ID = I.Program_ID 
JOIN EXERCISE E ON I.Exercise_ID = E.Exercise_ID 
JOIN MUSCLE_GROUP M ON E.Muscle_Group_ID = M.Muscle_Group_ID 
WHERE P.Estimated_Duration_Minutes > 45 
GROUP BY P.Program_Name, M.Group_Name 
ORDER BY Total_Exercises DESC;

-- ------------------------------------------
-- Query 7: Weight fluctuations (Max vs Min difference > 2kg)
-- ------------------------------------------
SELECT 
    T.Trainee_ID, 
    T.Gender, 
    MAX(M.Weight_Kg) AS Max_Weight, 
    MIN(M.Weight_Kg) AS Min_Weight, 
    (MAX(M.Weight_Kg) - MIN(M.Weight_Kg)) AS Weight_Fluctuation 
FROM TRAINEE_PROFILE T 
JOIN BODY_MEASUREMENT M ON T.Trainee_ID = M.Trainee_ID 
GROUP BY T.Trainee_ID, T.Gender 
HAVING (MAX(M.Weight_Kg) - MIN(M.Weight_Kg)) > 2 
ORDER BY Weight_Fluctuation DESC;

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

-- ==========================================
-- PART 2: COMPLEX UPDATE QUERIES
-- ==========================================

-- ------------------------------------------
-- UPDATE 1: Mark goal as achieved if a measurement reached the target
-- Non-trivial: Uses a subquery with JOIN to check measurements against goals.
-- ------------------------------------------
UPDATE TRAINEE_GOAL
SET Is_Achieved = true
WHERE Trainee_ID IN (
    SELECT G.Trainee_ID
    FROM TRAINEE_GOAL G
    JOIN BODY_MEASUREMENT M ON G.Trainee_ID = M.Trainee_ID
    WHERE M.Weight_Kg <= G.Target_Weight_Kg 
      AND G.Is_Achieved = false
);

-- ------------------------------------------
-- UPDATE 2: e=Ensuring that male trainees are moved to the Men's Locker Room and female trainees are moved to the Women's Locker Room.
-- Non-trivial: Updates locker table
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
-- UPDATE 3: Increase difficulty of programs with high average duration
-- Non-trivial: Uses GROUP BY and HAVING in a subquery to find hard programs.
-- ------------------------------------------
UPDATE TRAINING_PROGRAM
SET Difficulty_Level = 5
WHERE Program_ID IN (
    SELECT Program_ID
    FROM WORKOUT_LOG
    GROUP BY Program_ID
    HAVING AVG(Duration_Minutes) > 70
) AND Difficulty_Level < 5;

-- ==========================================
-- PART 3: COMPLEX DELETE QUERIES
-- ==========================================

-- ==========================================
-- PART 4: COMPLEX DELETE QUERIES
-- ==========================================

-- ------------------------------------------
-- DELETE 1: Remove workout logs from January 2024
-- Non-trivial: Uses date extraction functions to filter logs by a specific month and year.
-- ------------------------------------------
DELETE FROM WORKOUT_LOG
WHERE EXTRACT(MONTH FROM Log_Date) = 1 
  AND EXTRACT(YEAR FROM Log_Date) = 2024;

-- ------------------------------------------
-- DELETE 2: Remove high weight measurements for male trainees
-- Non-trivial: Filters measurements based on weight and checks the trainee's gender via a subquery.
-- ------------------------------------------
DELETE FROM BODY_MEASUREMENT
WHERE Weight_Kg > 119
  AND Trainee_ID IN (
      SELECT Trainee_ID
      FROM TRAINEE_PROFILE
      WHERE Gender = 'Male'
  );

-- ------------------------------------------
-- DELETE 3: Delete body measurements for trainees who already achieved their goal
-- Non-trivial: Clears old data based on goal status in another table.
-- ------------------------------------------
DELETE FROM BODY_MEASUREMENT
WHERE Trainee_ID IN (
    SELECT Trainee_ID
    FROM TRAINEE_GOAL
    WHERE Is_Achieved = 1
);
