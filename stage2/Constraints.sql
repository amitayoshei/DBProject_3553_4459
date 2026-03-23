ALTER TABLE Locker
ADD CONSTRAINT CHK_Locker_Rental CHECK (
    (Trainee_ID IS NULL AND Rental_End_Date IS NULL) 
    OR 
    (Trainee_ID IS NOT NULL AND Rental_End_Date IS NOT NULL)
);

ALTER TABLE Trainee_Profile
ADD CONSTRAINT CHK_Trainee_Age 
CHECK (Join_Date >= Date_Of_Birth + INTERVAL '14 years');