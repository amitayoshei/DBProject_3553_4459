-- ROLLBACK:

-- Before update
SELECT Trainee_ID, Date_Of_Birth 
FROM Trainee_Profile 
WHERE Trainee_ID = 1;

BEGIN;

UPDATE Trainee_Profile 
SET Date_Of_Birth = '2001-01-01' 
WHERE Trainee_ID = 1;

-- After update
SELECT Trainee_ID, Date_Of_Birth 
FROM Trainee_Profile 
WHERE Trainee_ID = 1;

ROLLBACK;

-- After Rollback
SELECT Trainee_ID, Date_Of_Birth 
FROM Trainee_Profile 
WHERE Trainee_ID = 1;


-- COMMIT:

-- Before update
SELECT Trainee_ID, Join_Date 
FROM Trainee_Profile 
WHERE Trainee_ID = 2;

BEGIN;

UPDATE Trainee_Profile 
SET Join_Date = '2025-01-01' 
WHERE Trainee_ID = 2;

-- After update
SELECT Trainee_ID, Join_Date 
FROM Trainee_Profile 
WHERE Trainee_ID = 2;

COMMIT;

-- After Commit
SELECT Trainee_ID, Join_Date 
FROM Trainee_Profile 
WHERE Trainee_ID = 2;