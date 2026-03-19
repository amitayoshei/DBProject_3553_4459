-- ==========================================
-- 1. NUTRITION_MENU (טבלת אב)
-- ==========================================
INSERT INTO NUTRITION_MENU (Menu_ID, Issue_Date, Total_Daily_Calories, Protein_Grams, Carbs_Grams, Fats_Grams, Water_Target_Liters, Breakfast_Details, Lunch_Details, Dinner_Details) VALUES
(1, '2024-01-01', 2000, 150, 200, 65, 3.0, 'Oatmeal & Eggs', 'Chicken Breast & Rice', 'Salmon & Salad'),
(2, '2024-01-02', 2500, 180, 250, 80, 3.5, 'Protein Shake & Toast', 'Beef & Sweet Potato', 'Tuna Salad'),
(3, '2024-01-03', 1800, 140, 150, 70, 2.5, 'Greek Yogurt', 'Turkey Sandwich', 'Grilled Chicken'),
(4, '2024-01-04', 3000, 200, 350, 90, 4.0, 'Pancakes & Eggs', 'Pasta & Meatballs', 'Steak & Potatoes'),
(5, '2024-01-05', 2200, 160, 220, 75, 3.0, 'Cereal & Milk', 'Chicken Wrap', 'White Fish & Quinoa'),
(6, '2024-01-06', 1900, 150, 160, 70, 2.5, 'Smoothie Bowl', 'Lentil Soup', 'Tofu Stir-fry'),
(7, '2024-01-07', 2600, 185, 270, 85, 3.5, 'Eggs & Bacon', 'Burger (No Bun)', 'Chicken & Broccoli'),
(8, '2024-01-08', 2100, 155, 190, 80, 3.0, 'Protein Bar', 'Chicken Salad', 'Turkey Meatballs'),
(9, '2024-01-09', 2800, 190, 300, 90, 4.0, 'Oats & Whey', 'Rice & Beans', 'Beef Stir-fry'),
(10, '2024-01-10', 1700, 130, 140, 60, 2.5, 'Fruit Salad', 'Grilled Cheese', 'Soup & Salad'),
(11, '2024-01-11', 2400, 170, 240, 85, 3.0, 'Eggs on Toast', 'Chicken Pasta', 'Salmon & Asparagus'),
(12, '2024-01-12', 2300, 165, 230, 80, 3.0, 'Yogurt & Nuts', 'Turkey Wrap', 'Chicken & Rice'),
(13, '2024-01-13', 2700, 180, 290, 90, 3.5, 'Protein Pancakes', 'Beef Bowl', 'Fish Tacos'),
(14, '2024-01-14', 1950, 145, 180, 70, 2.5, 'Avocado Toast', 'Quinoa Salad', 'Chicken Skewers'),
(15, '2024-01-15', 3100, 210, 380, 95, 4.0, 'Mass Gainer Shake', 'Double Chicken Rice', 'Steak & Pasta'),
(16, '2024-01-16', 1600, 120, 130, 65, 2.5, 'Boiled Eggs', 'Tuna Salad', 'Grilled Veggies'),
(17, '2024-01-17', 2250, 160, 210, 85, 3.0, 'Oatmeal', 'Chicken Sandwich', 'Beef & Broccoli'),
(18, '2024-01-18', 2050, 155, 190, 75, 3.0, 'Protein Shake', 'Turkey Bowl', 'Salmon & Quinoa'),
(19, '2024-01-19', 2550, 175, 260, 90, 3.5, 'Eggs & Sausage', 'Pasta Bake', 'Chicken Fajitas'),
(20, '2024-01-20', 1850, 140, 160, 70, 2.5, 'Fruit & Yogurt', 'Chicken Soup', 'Tofu & Rice');

-- ==========================================
-- 2. TRAINEE_PROFILE
-- ==========================================
INSERT INTO TRAINEE_PROFILE (Trainee_ID, Date_Of_Birth, Join_Date, Gender, Main_Goal, Menu_ID) VALUES
(1, '1995-05-12', '2023-11-01', 'Male', 'Hypertrophy', 1),
(2, '1998-08-20', '2023-11-05', 'Female', 'Fat Loss', 3),
(3, '1990-02-15', '2023-11-10', 'Male', 'Strength', 4),
(4, '2001-11-30', '2023-11-12', 'Male', 'Hypertrophy', 2),
(5, '1985-07-08', '2023-11-15', 'Female', 'Endurance', 6),
(6, '1992-04-25', '2023-11-20', 'Male', 'Fat Loss', 8),
(7, '1997-09-14', '2023-11-22', 'Female', 'Hypertrophy', 5),
(8, '1988-12-05', '2023-12-01', 'Male', 'Strength', 9),
(9, '2000-03-18', '2023-12-05', 'Female', 'Fat Loss', 10),
(10, '1994-06-22', '2023-12-10', 'Male', 'Maintenance', 12),
(11, '1991-10-10', '2023-12-12', 'Female', 'Strength', 7),
(12, '1989-01-30', '2023-12-15', 'Male', 'Hypertrophy', 11),
(13, '1996-08-08', '2024-01-02', 'Female', 'Hypertrophy', 13),
(14, '1993-05-19', '2024-01-05', 'Male', 'Fat Loss', 14),
(15, '2002-02-28', '2024-01-10', 'Male', 'Hypertrophy', 15),
(16, '1987-11-11', '2024-01-15', 'Female', 'Fat Loss', 16),
(17, '1999-07-24', '2024-01-20', 'Male', 'Strength', 17),
(18, '1995-04-03', '2024-01-25', 'Female', 'Maintenance', 18),
(19, '1990-09-09', '2024-02-01', 'Male', 'Hypertrophy', 19),
(20, '1986-12-12', '2024-02-05', 'Female', 'Fat Loss', 20);

-- ==========================================
-- 3. MUSCLE_GROUP (טבלת אב לתרגילים)
-- ==========================================
INSERT INTO MUSCLE_GROUP (Muscle_Group_ID, Group_Name, Description, Recovery_Time_Hours) VALUES
(1, 'Chest', 'Pectoral muscles', 48),
(2, 'Back', 'Latissimus dorsi and rhomboids', 48),
(3, 'Legs', 'Quadriceps, hamstrings, glutes', 72),
(4, 'Shoulders', 'Deltoids', 48),
(5, 'Arms - Biceps', 'Front of upper arm', 24),
(6, 'Arms - Triceps', 'Back of upper arm', 24),
(7, 'Core', 'Abdominals and obliques', 24),
(8, 'Calves', 'Lower leg muscles', 24),
(9, 'Forearms', 'Lower arm muscles', 24),
(10, 'Neck', 'Neck and upper traps', 24);

-- ==========================================
-- 4. EXERCISE
-- ==========================================
INSERT INTO EXERCISE (Exercise_ID, Exercise_Name, Equipment_Needed, Instructions, Calories_Burned_Per_Minute, Muscle_Group_ID) VALUES
(1, 'Bench Press', 'Barbell, Bench', 'Lower bar to chest, press up', 6, 1),
(2, 'Pull-ups', 'Pull-up Bar', 'Pull body up until chin is over bar', 8, 2),
(3, 'Squats', 'Barbell, Squat Rack', 'Bend knees, keep back straight', 9, 3),
(4, 'Overhead Press', 'Barbell', 'Press bar straight up overhead', 6, 4),
(5, 'Bicep Curls', 'Dumbbells', 'Curl weight towards shoulders', 4, 5),
(6, 'Tricep Extensions', 'Cable Machine', 'Push cable down, isolate triceps', 4, 6),
(7, 'Plank', 'Mat', 'Hold body in straight line', 3, 7),
(8, 'Calf Raises', 'Step', 'Raise heels off edge of step', 3, 8),
(9, 'Incline Dumbbell Press', 'Dumbbells, Bench', 'Press dumbbells on incline bench', 6, 1),
(10, 'Barbell Rows', 'Barbell', 'Pull bar to stomach, back parallel to floor', 7, 2),
(11, 'Leg Press', 'Leg Press Machine', 'Push platform away with legs', 7, 3),
(12, 'Lateral Raises', 'Dumbbells', 'Raise arms to sides', 4, 4),
(13, 'Hammer Curls', 'Dumbbells', 'Curl with neutral grip', 4, 5),
(14, 'Skull Crushers', 'EZ Bar, Bench', 'Lower bar to forehead, extend triceps', 4, 6),
(15, 'Crunches', 'Mat', 'Curl torso towards knees', 4, 7),
(16, 'Deadlifts', 'Barbell', 'Lift bar from floor, extend hips', 10, 3),
(17, 'Push-ups', 'Bodyweight', 'Lower body, push up', 5, 1),
(18, 'Lat Pulldowns', 'Cable Machine', 'Pull bar down to chest', 5, 2),
(19, 'Lunges', 'Dumbbells', 'Step forward, bend both knees', 7, 3),
(20, 'Face Pulls', 'Cable Machine', 'Pull rope towards face', 4, 4);

-- ==========================================
-- 5. TRAINING_PROGRAM
-- ==========================================
INSERT INTO TRAINING_PROGRAM (Program_ID, Program_Name, Workout_Type, Creation_Date, Difficulty_Level, Estimated_Duration_Minutes) VALUES
(1, 'Beginner Full Body', 'Full Body', '2023-10-01', 1, 45),
(2, 'Intermediate Split A', 'Upper Body', '2023-10-05', 3, 60),
(3, 'Intermediate Split B', 'Lower Body', '2023-10-05', 3, 60),
(4, 'Advanced Push', 'Push', '2023-10-10', 4, 75),
(5, 'Advanced Pull', 'Pull', '2023-10-10', 4, 75),
(6, 'Advanced Legs', 'Legs', '2023-10-10', 4, 75),
(7, 'Core Crusher', 'Core', '2023-10-15', 2, 30),
(8, 'HIIT Cardio', 'Cardio', '2023-10-20', 4, 40),
(9, 'Strength 5x5', 'Full Body', '2023-11-01', 5, 90),
(10, 'Hypertrophy Chest & Back', 'Split', '2023-11-05', 3, 65),
(11, 'Hypertrophy Arms & Shoulders', 'Split', '2023-11-05', 3, 60),
(12, 'Hypertrophy Legs & Core', 'Split', '2023-11-05', 3, 70),
(13, 'Endurance Builder', 'Full Body', '2023-11-10', 2, 55),
(14, 'Powerlifting Prep', 'Strength', '2023-11-15', 5, 100),
(15, 'Recovery Day', 'Mobility', '2023-11-20', 1, 30),
(16, 'Dumbbell Only Home Workout', 'Full Body', '2023-12-01', 2, 45),
(17, 'Bodyweight Basics', 'Calisthenics', '2023-12-05', 1, 40),
(18, 'Kettlebell Flow', 'Functional', '2023-12-10', 3, 50),
(19, '30-Minute Express', 'Full Body', '2023-12-15', 3, 30),
(20, 'Elite Athlete Conditioning', 'Mixed', '2024-01-01', 5, 80);

-- ==========================================
-- 6. BODY_MEASUREMENT (תלוי ב-Trainee)
-- ==========================================
INSERT INTO BODY_MEASUREMENT (Measurement_ID, Measurement_Date, Weight_Kg, Fat_Percentage, Muscle_Mass_Kg, Waist_Circumference_cm, Shoulder_Circumference_cm, BMI_Score, Height_cm, Trainee_ID) VALUES
(1, '2024-02-01', 75.5, 18.2, 35.0, 85.0, 110.0, 24.1, 177, 1),
(2, '2024-02-01', 62.0, 22.5, 25.5, 72.0, 95.0, 22.8, 165, 2),
(3, '2024-02-02', 85.0, 15.0, 42.0, 88.0, 120.0, 26.2, 180, 3),
(4, '2024-02-02', 78.0, 19.5, 36.5, 86.5, 112.0, 24.6, 178, 4),
(5, '2024-02-03', 58.5, 24.0, 24.0, 70.0, 92.0, 21.5, 165, 5),
(6, '2024-02-03', 92.0, 28.0, 40.0, 105.0, 118.0, 29.7, 176, 6),
(7, '2024-02-04', 65.0, 20.0, 27.0, 74.0, 98.0, 23.3, 167, 7),
(8, '2024-02-04', 88.0, 14.5, 43.5, 87.0, 122.0, 25.4, 186, 8),
(9, '2024-02-05', 60.0, 26.5, 23.5, 75.0, 94.0, 24.0, 158, 9),
(10, '2024-02-05', 77.0, 17.5, 37.0, 84.0, 115.0, 23.8, 180, 10),
(11, '2024-02-06', 68.0, 21.0, 28.5, 76.0, 100.0, 23.5, 170, 11),
(12, '2024-02-06', 82.0, 16.5, 40.0, 86.0, 119.0, 25.3, 180, 12),
(13, '2024-02-07', 63.5, 19.5, 26.0, 71.5, 96.0, 22.0, 170, 13),
(14, '2024-02-07', 89.5, 25.0, 41.0, 98.0, 117.0, 28.2, 178, 14),
(15, '2024-02-08', 76.0, 15.5, 38.0, 82.0, 114.0, 24.2, 177, 15),
(16, '2024-02-08', 59.0, 23.5, 24.5, 71.0, 93.0, 21.7, 165, 16),
(17, '2024-02-09', 84.0, 13.0, 43.0, 83.0, 121.0, 25.9, 180, 17),
(18, '2024-02-09', 61.5, 21.5, 25.0, 73.0, 95.0, 22.6, 165, 18),
(19, '2024-02-10', 80.0, 17.0, 39.0, 85.0, 116.0, 24.7, 180, 19),
(20, '2024-02-10', 57.0, 25.0, 23.0, 69.0, 90.0, 22.3, 160, 20);

-- ==========================================
-- 7. WORKOUT_LOG (תלוי ב-Trainee וב-Program)
-- ==========================================
INSERT INTO WORKOUT_LOG (Log_ID, Log_Date, Duration_Minutes, Total_Calories_Burned, Average_Heart_Rate, Trainee_Feedback_Rating, Coach_Notes, Program_ID, Trainee_ID) VALUES
(1, '2024-02-20', 50, 450, 135, 8, 'Good energy today', 1, 1),
(2, '2024-02-20', 65, 520, 142, 9, 'Felt strong on squats', 2, 2),
(3, '2024-02-21', 45, 380, 128, 7, 'A bit tired, adjusted weights', 3, 3),
(4, '2024-02-21', 75, 600, 150, 10, 'Personal best on deadlift!', 4, 4),
(5, '2024-02-22', 60, 480, 138, 8, 'Consistent pace', 5, 5),
(6, '2024-02-22', 55, 410, 130, 6, 'Struggled with pull-ups', 6, 6),
(7, '2024-02-23', 70, 550, 145, 9, 'Great pump', 10, 7),
(8, '2024-02-23', 80, 650, 155, 8, 'Heavy session, good form', 14, 8),
(9, '2024-02-24', 40, 320, 125, 7, 'Quick session', 7, 9),
(10, '2024-02-24', 60, 490, 140, 9, 'Felt good throughout', 11, 10),
(11, '2024-02-25', 50, 430, 132, 8, 'Solid effort', 12, 11),
(12, '2024-02-25', 65, 540, 148, 10, 'Crushed it', 9, 12),
(13, '2024-02-26', 55, 460, 136, 7, 'Normal session', 13, 13),
(14, '2024-02-26', 45, 400, 145, 8, 'High intensity', 8, 14),
(15, '2024-02-27', 75, 580, 144, 9, 'Good volume', 10, 15),
(16, '2024-02-27', 30, 200, 110, 6, 'Active recovery', 15, 16),
(17, '2024-02-28', 85, 700, 152, 10, 'Very strong today', 14, 17),
(18, '2024-02-28', 50, 420, 134, 8, 'Maintained pace', 16, 18),
(19, '2024-03-01', 65, 510, 140, 9, 'Good form on bench', 4, 19),
(20, '2024-03-01', 40, 350, 130, 7, 'Basic workout completed', 17, 20);

-- ==========================================
-- 8. HAS_PROGRAM (קשר M:N)
-- ==========================================
INSERT INTO HAS_PROGRAM (Program_ID, Trainee_ID) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (10, 7), (14, 8), (7, 9), (11, 10),
(12, 11), (9, 12), (13, 13), (8, 14), (10, 15),
(15, 16), (14, 17), (16, 18), (4, 19), (17, 20);

-- ==========================================
-- 9. INCLUDES (קשר M:N תרגילים לתוכניות)
-- ==========================================
INSERT INTO INCLUDES (Exercise_ID, Program_ID, Reps_Count, Sets_Count) VALUES
(1, 1, 10, 3), (3, 1, 10, 3), (10, 1, 10, 3),
(1, 4, 8, 4), (4, 4, 8, 4), (9, 4, 10, 3),
(2, 5, 8, 4), (10, 5, 8, 4), (18, 5, 12, 3),
(3, 6, 6, 5), (11, 6, 10, 4), (19, 6, 12, 3),
(5, 11, 12, 3), (6, 11, 12, 3), (12, 11, 15, 3),
(7, 7, 60, 3), (15, 7, 20, 3),
(16, 9, 5, 5), (3, 9, 5, 5), (1, 9, 5, 5);

-- ==========================================
-- 10. LOCKER (תלוי ב-Trainee)
-- ==========================================
INSERT INTO LOCKER (Locker_ID, Location_Zone, Rental_End_Date, Trainee_ID) VALUES
(1, 'Zone A - Men', '2024-12-31', 1),
(2, 'Zone B - Women', '2024-11-30', 2),
(3, 'Zone A - Men', '2024-10-15', 3),
(4, 'Zone A - Men', '2025-01-01', 4),
(5, 'Zone B - Women', '2024-08-01', 5),
(6, 'Zone C - VIP', '2025-05-20', 6),
(7, 'Zone B - Women', '2024-09-10', 7),
(8, 'Zone A - Men', '2024-12-01', 8),
(9, 'Zone B - Women', '2024-07-30', 9),
(10, 'Zone A - Men', '2024-11-15', 10),
(11, 'Zone B - Women', '2024-12-31', 11),
(12, 'Zone C - VIP', '2025-01-10', 12),
(13, 'Zone B - Women', '2024-10-05', 13),
(14, 'Zone A - Men', '2024-09-25', 14),
(15, 'Zone A - Men', '2025-02-28', 15),
(16, 'Zone B - Women', '2024-08-15', 16),
(17, 'Zone C - VIP', '2025-03-01', 17),
(18, 'Zone B - Women', '2024-11-20', 18),
(19, 'Zone A - Men', '2024-12-10', 19),
(20, 'Zone B - Women', '2025-01-15', 20);

-- ==========================================
-- 11. HEALTH_DECLARATION (תלוי ב-Trainee)
-- ==========================================
INSERT INTO HEALTH_DECLARATION (Declaration_ID, Issue_Date, Expiry_Date, Doctor_Name, Limitations_Notes, Is_Valid, Trainee_ID) VALUES
(1, '2023-11-01', '2024-11-01', 'Dr. Cohen', 'None', true, 1),
(2, '2023-11-05', '2024-11-05', 'Dr. Levi', 'Asthma - mild', true, 2),
(3, '2023-11-10', '2024-11-10', 'Dr. Klein', 'None', true, 3),
(4, '2023-11-12', '2024-11-12', 'Dr. Avraham', 'Previous shoulder injury', true, 4),
(5, '2023-11-15', '2024-11-15', 'Dr. Bar', 'None', true, 5),
(6, '2023-11-20', '2024-11-20', 'Dr. Cohen', 'None', true, 6),
(7, '2023-11-22', '2024-11-22', 'Dr. Levi', 'Knee sensitivity', true, 7),
(8, '2023-12-01', '2024-12-01', 'Dr. Shapira', 'None', true, 8),
(9, '2023-12-05', '2024-12-05', 'Dr. Klein', 'None', true, 9),
(10, '2023-12-10', '2024-12-10', 'Dr. Avraham', 'None', true, 10),
(11, '2023-12-12', '2024-12-12', 'Dr. Bar', 'Lower back pain', true, 11),
(12, '2023-12-15', '2024-12-15', 'Dr. Cohen', 'None', true, 12),
(13, '2024-01-02', '2025-01-02', 'Dr. Levi', 'None', true, 13),
(14, '2024-01-05', '2025-01-05', 'Dr. Shapira', 'Avoid heavy deadlifts', true, 14),
(15, '2024-01-10', '2025-01-10', 'Dr. Klein', 'None', true, 15),
(16, '2024-01-15', '2025-01-15', 'Dr. Avraham', 'None', true, 16),
(17, '2024-01-20', '2025-01-20', 'Dr. Bar', 'None', true, 17),
(18, '2024-01-25', '2025-01-25', 'Dr. Cohen', 'None', true, 18),
(19, '2024-02-01', '2025-02-01', 'Dr. Levi', 'None', true, 19),
(20, '2024-02-05', '2025-02-05', 'Dr. Shapira', 'None', true, 20);

-- ==========================================
-- 12. TRAINEE_GOAL (תלוי ב-Trainee)
-- ==========================================
INSERT INTO TRAINEE_GOAL (Goal_ID, Creation_Date, Target_Date, Target_Weight_Kg, Target_Fat_Percentage, Is_Achieved, Trainee_ID) VALUES
(1, '2023-11-01', '2024-05-01', 80.0, 15.0, false, 1),
(2, '2023-11-05', '2024-04-01', 58.0, 18.0, false, 2),
(3, '2023-11-10', '2024-06-01', 90.0, 14.0, false, 3),
(4, '2023-11-12', '2024-05-15', 82.0, 16.0, false, 4),
(5, '2023-11-15', '2024-03-01', 56.0, 20.0, false, 5),
(6, '2023-11-20', '2024-08-01', 85.0, 18.0, false, 6),
(7, '2023-11-22', '2024-05-01', 68.0, 17.0, false, 7),
(8, '2023-12-01', '2024-07-01', 92.0, 12.0, false, 8),
(9, '2023-12-05', '2024-06-01', 55.0, 19.0, false, 9),
(10, '2023-12-10', '2024-06-15', 77.0, 15.0, false, 10),
(11, '2023-12-12', '2024-04-01', 70.0, 18.0, false, 11),
(12, '2023-12-15', '2024-08-15', 86.0, 14.0, false, 12),
(13, '2024-01-02', '2024-07-01', 65.0, 16.0, false, 13),
(14, '2024-01-05', '2024-09-01', 82.0, 15.0, false, 14),
(15, '2024-01-10', '2024-10-01', 80.0, 13.0, false, 15),
(16, '2024-01-15', '2024-06-01', 56.0, 20.0, false, 16),
(17, '2024-01-20', '2024-11-01', 88.0, 12.0, false, 17),
(18, '2024-01-25', '2024-05-01', 60.0, 19.0, false, 18),
(19, '2024-02-01', '2024-12-01', 84.0, 14.0, false, 19),
(20, '2024-02-05', '2024-08-01', 54.0, 18.0, false, 20);

-- ==========================================
-- 13. EXERCISE_VIDEO_URL (תלוי ב-Exercise)
-- ==========================================
INSERT INTO EXERCISE_VIDEO_URL (Video_URL, Exercise_ID) VALUES
('https://youtube.com/watch?v=bench1', 1),
('https://youtube.com/watch?v=pullups1', 2),
('https://youtube.com/watch?v=squats1', 3),
('https://youtube.com/watch?v=ohp1', 4),
('https://youtube.com/watch?v=curls1', 5),
('https://youtube.com/watch?v=tricep1', 6),
('https://youtube.com/watch?v=plank1', 7),
('https://youtube.com/watch?v=calves1', 8),
('https://youtube.com/watch?v=incline1', 9),
('https://youtube.com/watch?v=rows1', 10),
('https://youtube.com/watch?v=legpress1', 11),
('https://youtube.com/watch?v=lateral1', 12),
('https://youtube.com/watch?v=hammer1', 13),
('https://youtube.com/watch?v=skull1', 14),
('https://youtube.com/watch?v=crunch1', 15),
('https://youtube.com/watch?v=deadlift1', 16),
('https://youtube.com/watch?v=pushup1', 17),
('https://youtube.com/watch?v=latpull1', 18),
('https://youtube.com/watch?v=lunges1', 19),
('https://youtube.com/watch?v=facepull1', 20);