CREATE TABLE NUTRITION_MENU
(
  Menu_ID INT NOT NULL,
  Issue_Date DATE NOT NULL,
  Total_Daily_Calories INT NOT NULL CHECK (Total_Daily_Calories > 0),
  Protein_Grams INT NOT NULL CHECK (Protein_Grams >= 0),
  Carbs_Grams INT NOT NULL CHECK (Carbs_Grams >= 0),
  Fats_Grams INT NOT NULL CHECK (Fats_Grams >= 0),
  Water_Target_Liters NUMERIC(3, 1) NOT NULL CHECK (Water_Target_Liters >= 0),
  Breakfast_Details VARCHAR(500) NOT NULL,
  Lunch_Details VARCHAR(500) NOT NULL,
  Dinner_Details VARCHAR(500) NOT NULL,
  PRIMARY KEY (Menu_ID)
);

CREATE TABLE TRAINEE_PROFILE
(
  Trainee_ID INT NOT NULL,
  Date_Of_Birth DATE NOT NULL,
  Join_Date DATE NOT NULL,
  Gender VARCHAR(10) NOT NULL CHECK (Gender IN ('Male', 'Female', 'Other')),
  Main_Goal VARCHAR(100) NOT NULL,
  Menu_ID INT NOT NULL,
  PRIMARY KEY (Trainee_ID),
  FOREIGN KEY (Menu_ID) REFERENCES NUTRITION_MENU(Menu_ID)
);

CREATE TABLE HEALTH_DECLARATION
(
  Declaration_ID INT NOT NULL,
  Issue_Date DATE NOT NULL,
  Expiry_Date DATE NOT NULL,
  Doctor_Name VARCHAR(50) NOT NULL,
  Limitations_Notes VARCHAR(500) NOT NULL,
  Is_Valid INT NOT NULL CHECK (Is_Valid IN (0, 1)),
  Trainee_ID INT NOT NULL,
  PRIMARY KEY (Declaration_ID),
  FOREIGN KEY (Trainee_ID) REFERENCES TRAINEE_PROFILE(Trainee_ID)
);

CREATE TABLE BODY_MEASUREMENT
(
  Measurement_ID INT NOT NULL,
  Measurement_Date DATE NOT NULL,
  Weight_Kg NUMERIC(5, 2) NOT NULL CHECK (Weight_Kg > 20 AND Weight_Kg < 300),
  Fat_Percentage NUMERIC(4, 1) NOT NULL CHECK (Fat_Percentage > 0 AND Fat_Percentage < 100),
  Muscle_Mass_Kg NUMERIC(5, 2) NOT NULL CHECK (Muscle_Mass_Kg > 0),
  Waist_Circumference_cm NUMERIC(4, 1) NOT NULL CHECK (Waist_Circumference_cm > 0),
  Shoulder_Circumference_cm NUMERIC(4, 1) NOT NULL CHECK (Shoulder_Circumference_cm > 0),
  BMI_Score NUMERIC(4, 1) NOT NULL CHECK (BMI_Score > 10 AND BMI_Score < 60),
  Height_cm NUMERIC(4, 1) NOT NULL CHECK (Height_cm > 50 AND Height_cm < 250),
  Trainee_ID INT NOT NULL,
  PRIMARY KEY (Measurement_ID),
  FOREIGN KEY (Trainee_ID) REFERENCES TRAINEE_PROFILE(Trainee_ID)
);

CREATE TABLE TRAINEE_GOAL
(
  Goal_ID INT NOT NULL,
  Creation_Date DATE NOT NULL,
  Target_Date DATE NOT NULL,
  Target_Weight_Kg NUMERIC(5, 2) NOT NULL CHECK (Target_Weight_Kg > 20),
  Target_Fat_Percentage NUMERIC(4, 1) NOT NULL CHECK (Target_Fat_Percentage > 0),
  Is_Achieved INT NOT NULL CHECK (Is_Achieved IN (0, 1)),
  Trainee_ID INT NOT NULL,
  PRIMARY KEY (Goal_ID),
  FOREIGN KEY (Trainee_ID) REFERENCES TRAINEE_PROFILE(Trainee_ID)
);

CREATE TABLE MUSCLE_GROUP
(
  Muscle_Group_ID INT NOT NULL,
  Group_Name VARCHAR(50) NOT NULL,
  Description VARCHAR(500) NOT NULL,
  Recovery_Time_Hours INT NOT NULL CHECK (Recovery_Time_Hours >= 0),
  PRIMARY KEY (Muscle_Group_ID)
);

CREATE TABLE EXERCISE
(
  Exercise_ID INT NOT NULL,
  Exercise_Name VARCHAR(50) NOT NULL,
  Equipment_Needed VARCHAR(100) NOT NULL,
  Instructions VARCHAR(1000) NOT NULL,
  Calories_Burned_Per_Minute NUMERIC(5, 2) CHECK (Calories_Burned_Per_Minute >= 0),
  PRIMARY KEY (Exercise_ID)
);

CREATE TABLE TRAINING_PROGRAM
(
  Program_ID INT NOT NULL,
  Program_Name VARCHAR(50) NOT NULL,
  Workout_Type VARCHAR(50) NOT NULL,
  Creation_Date DATE NOT NULL,
  Difficulty_Level INT NOT NULL CHECK (Difficulty_Level BETWEEN 1 AND 5),
  Estimated_Duration_Minutes NUMERIC(5, 2) NOT NULL CHECK (Estimated_Duration_Minutes > 0),
  PRIMARY KEY (Program_ID)
);

CREATE TABLE WORKOUT_LOG
(
  Log_ID INT NOT NULL,
  Log_Date DATE NOT NULL,
  Duration_Minutes NUMERIC(5, 2) NOT NULL CHECK (Duration_Minutes > 0),
  Total_Calories_Burned INT NOT NULL CHECK (Total_Calories_Burned >= 0),
  Average_Heart_Rate NUMERIC(4, 1) NOT NULL CHECK (Average_Heart_Rate BETWEEN 40 AND 220),
  Trainee_Feedback_Rating INT NOT NULL CHECK (Trainee_Feedback_Rating BETWEEN 1 AND 10),
  Coach_Notes VARCHAR(500) NOT NULL,
  Program_ID INT NOT NULL,
  Trainee_ID INT NOT NULL,
  PRIMARY KEY (Log_ID),
  FOREIGN KEY (Program_ID) REFERENCES TRAINING_PROGRAM(Program_ID),
  FOREIGN KEY (Trainee_ID) REFERENCES TRAINEE_PROFILE(Trainee_ID)
);

CREATE TABLE LOCKER
(
  Locker_ID INT NOT NULL,
  Location_Zone VARCHAR(50) NOT NULL,
  Rental_End_Date DATE NOT NULL,
  Trainee_ID INT NOT NULL,
  PRIMARY KEY (Locker_ID),
  FOREIGN KEY (Trainee_ID) REFERENCES TRAINEE_PROFILE(Trainee_ID)
);

CREATE TABLE TARGETING
(
  Muscle_Group_ID INT NOT NULL,
  Exercise_ID INT NOT NULL,
  PRIMARY KEY (Muscle_Group_ID, Exercise_ID),
  FOREIGN KEY (Muscle_Group_ID) REFERENCES MUSCLE_GROUP(Muscle_Group_ID),
  FOREIGN KEY (Exercise_ID) REFERENCES EXERCISE(Exercise_ID)
);

CREATE TABLE INCLUDES
(
  Reps_Count INT NOT NULL CHECK (Reps_Count > 0),
  Sets_Count INT NOT NULL CHECK (Sets_Count > 0),
  Exercise_ID INT NOT NULL,
  Program_ID INT NOT NULL,
  PRIMARY KEY (Exercise_ID, Program_ID),
  FOREIGN KEY (Exercise_ID) REFERENCES EXERCISE(Exercise_ID),
  FOREIGN KEY (Program_ID) REFERENCES TRAINING_PROGRAM(Program_ID)
);

CREATE TABLE HAS_PROGRAM
(
  Program_ID INT NOT NULL,
  Trainee_ID INT NOT NULL,
  PRIMARY KEY (Program_ID, Trainee_ID),
  FOREIGN KEY (Program_ID) REFERENCES TRAINING_PROGRAM(Program_ID),
  FOREIGN KEY (Trainee_ID) REFERENCES TRAINEE_PROFILE(Trainee_ID)
);

CREATE TABLE EXERCISE_VIDEO_URL
(
  Video_URL VARCHAR(200) NOT NULL,
  Exercise_ID INT NOT NULL,
  PRIMARY KEY (Video_URL, Exercise_ID),
  FOREIGN KEY (Exercise_ID) REFERENCES EXERCISE(Exercise_ID)
);