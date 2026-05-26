INSERT INTO public.nutrition_menu (menu_id, issue_date, total_daily_calories, protein_grams, carbs_grams, fats_grams, water_target_liters, breakfast_details, lunch_details, dinner_details)
SELECT 
    menu_id, 
    issue_date::DATE, 
    total_daily_calories, 
    protein_grams, 
    carbs_grams, 
    fats_grams, 
    water_target_liters, 
    breakfast_details, 
    lunch_details, 
    dinner_details 
FROM public.temp_nutrition_menu;


INSERT INTO public.employee (employee_id, first_name, last_name, job_title, hire_date)
SELECT 
    employee_id, 
    first_name, 
    last_name, 
    job_title, 
    hire_date::DATE 
FROM public.temp_employee;


INSERT INTO public.training_program (program_id, program_name, workout_type, creation_date, difficulty_level, estimated_duration_minutes)
SELECT 
    program_id, 
    program_name, 
    workout_type, 
    creation_date::DATE, 
    difficulty_level, 
    estimated_duration_minutes 
FROM public.temp_training_program;


INSERT INTO public.supplier SELECT * FROM public.temp_supplier;
INSERT INTO public.facility_zone SELECT * FROM public.temp_facility_zone;
INSERT INTO public.spare_part SELECT * FROM public.temp_spare_part;
INSERT INTO public.muscle_group SELECT * FROM public.temp_muscle_group;


INSERT INTO public.core_user (user_id, first_name, last_name, phone_number, email, join_date)
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.phone_number,
    c.email,
    CURRENT_DATE
    COALESCE(
        (SELECT MIN(purchase_date::DATE) FROM public.temp_subscription s WHERE s.customer_id = c.customer_id),
        tp.join_date::DATE,
        CURRENT_DATE
    ) AS join_date
FROM public.temp_customer c
INNER JOIN public.temp_trainee_profile tp ON c.customer_id = tp.trainee_id;


INSERT INTO public.trainee_metadata (user_id, date_of_birth, gender, main_goal, menu_id)
SELECT 
    tp.trainee_id, 
    tp.date_of_birth::DATE,
    tp.gender,
    tp.main_goal,
    tp.menu_id
FROM public.temp_trainee_profile tp
WHERE tp.trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.subscription (contract_number, purchase_date, expiration_date, total_cost, user_id)
SELECT 
    contract_number, 
    purchase_date::DATE, 
    expiration_date::DATE, 
    total_cost, 
    floor(random() * 500 + 1)::int AS user_id
FROM public.temp_subscription;


INSERT INTO public.health_declaration (declaration_id, issue_date, expiry_date, doctor_name, limitations_notes, is_valid, user_id)
SELECT 
    declaration_id, 
    issue_date::DATE, 
    expiry_date::DATE, 
    doctor_name, 
    limitations_notes, 
    is_valid, 
    trainee_id 
FROM public.temp_health_declaration
WHERE trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.body_measurement (measurement_id, measurement_date, weight_kg, fat_percentage, muscle_mass_kg, waist_circumference_cm, shoulder_circumference_cm, bmi_score, height_cm, user_id)
SELECT 
    measurement_id, 
    measurement_date::DATE, 
    weight_kg, 
    fat_percentage, 
    muscle_mass_kg, 
    waist_circumference_cm, 
    shoulder_circumference_cm, 
    bmi_score, 
    height_cm, 
    trainee_id 
FROM public.temp_body_measurement
WHERE trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.trainee_goal (goal_id, creation_date, target_date, target_weight_kg, target_fat_percentage, is_achieved, user_id)
SELECT 
    goal_id, 
    creation_date::DATE, 
    target_date::DATE, 
    target_weight_kg, 
    target_fat_percentage, 
    is_achieved, 
    trainee_id 
FROM public.temp_trainee_goal
WHERE trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.has_program (program_id, user_id)
SELECT 
    program_id, 
    trainee_id 
FROM public.temp_has_program
WHERE trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.workout_log (log_id, log_date, duration_minutes, total_calories_burned, average_heart_rate, trainee_feedback_rating, coach_notes, program_id, user_id)
SELECT 
    log_id, 
    log_date::DATE, 
    duration_minutes, 
    total_calories_burned, 
    average_heart_rate, 
    trainee_feedback_rating, 
    coach_notes, 
    program_id, 
    trainee_id 
FROM public.temp_workout_log
WHERE trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.locker (locker_id, location_zone, rental_end_date, user_id)
SELECT 
    locker_id, 
    location_zone, 
    rental_end_date::DATE, 
    trainee_id 
FROM public.temp_locker
WHERE trainee_id IS NULL OR trainee_id IN (SELECT user_id FROM public.core_user);


INSERT INTO public.exercise (exercise_id, exercise_name, equipment_needed, instructions, calories_burned_per_minute, muscle_group_id)
SELECT 
    exercise_id, 
    exercise_name, 
    equipment_needed, 
    instructions, 
    calories_burned_per_minute, 
    muscle_group_id 
FROM public.temp_exercise;


INSERT INTO public.fitness_machine (serial_number, manufacturer, model, machine_status, purchase_date, zone_code)
SELECT 
    serial_number, 
    manufacturer, 
    model, 
    machine_status, 
    purchase_date::DATE, 
    zone_code
FROM public.temp_fitness_machine;


INSERT INTO public.purchase_order (order_number, order_date, supplier_id, employee_id)
SELECT 
    order_number, 
    order_date::DATE, 
    supplier_id, 
    employee_id
FROM public.temp_purchase_order;


INSERT INTO public.payment (receipt_number, payment_amount, payment_date, payment_method, contract_number)
SELECT 
    receipt_number, 
    payment_amount, 
    payment_date::DATE, 
    payment_method, 
    contract_number
FROM public.temp_payment;


INSERT INTO public.maintenance_ticket (ticket_number, open_date, issue_description, ticket_status, serial_number, supplier_id)
SELECT 
    ticket_number, 
    open_date::DATE, 
    issue_description, 
    ticket_status, 
    serial_number, 
    supplier_id
FROM public.temp_maintenance_ticket;


INSERT INTO public.exercise_video_url (video_url, exercise_id)
SELECT 
    video_url, 
    exercise_id
FROM public.temp_exercise_video_url;


INSERT INTO public.includes (reps_count, sets_count, exercise_id, program_id)
SELECT 
    reps_count, 
    sets_count, 
    exercise_id, 
    program_id
FROM public.temp_includes;


INSERT INTO public.order_item (ordered_quantity, order_number, part_number)
SELECT 
    ordered_quantity, 
    order_number, 
    part_number
FROM public.temp_order_item;


-- ========================================================
-- 1. Insert 10 trainers into the system (starting from ID 511)
-- ========================================================
INSERT INTO public.employee (employee_id, first_name, last_name, job_title, hire_date)
VALUES 
(511, 'Yossi', 'Cohen', 'Trainer', '2020-05-15'),
(512, 'Dana', 'Levi', 'Coach', '2021-03-10'),
(513, 'Avi', 'Israel', 'Fitness Instructor', '2019-11-20'),
(514, 'Michal', 'Avraham', 'Trainer', '2022-01-05'),
(515, 'Ron', 'Ben-David', 'Coach', '2018-08-14'),
(516, 'Noa', 'Golan', 'Fitness Instructor', '2023-06-22'),
(517, 'Eli', 'Katz', 'Trainer', '2017-09-30'),
(518, 'Tamar', 'Shalom', 'Coach', '2020-12-01'),
(519, 'Omer', 'Peleg', 'Fitness Instructor', '2021-07-18'),
(520, 'Maya', 'Nir', 'Trainer', '2019-04-25');

-- ========================================================
-- 2. Add columns and foreign keys (allows NULL for historical data)
-- ========================================================
ALTER TABLE public.training_program
ADD COLUMN employee_id INT,
ADD CONSTRAINT fk_program_employee 
  FOREIGN KEY (employee_id) 
  REFERENCES public.employee(employee_id);

ALTER TABLE public.workout_log
ADD COLUMN employee_id INT,
ADD CONSTRAINT fk_workout_employee 
  FOREIGN KEY (employee_id) 
  REFERENCES public.employee(employee_id);

-- ========================================================
-- 3. Create the logic function to verify the "Trainer" role
-- ========================================================
CREATE OR REPLACE FUNCTION check_if_employee_is_trainer()
RETURNS TRIGGER AS $$
DECLARE
    v_job_title VARCHAR;
BEGIN
    -- The check only runs if a trainer was actually assigned (allows NULL for past trainees)
    IF NEW.employee_id IS NOT NULL THEN
        
        -- Retrieve the employee's job title
        SELECT job_title INTO v_job_title
        FROM public.employee
        WHERE employee_id = NEW.employee_id;

        -- Check if the role is valid
        IF v_job_title NOT IN ('Trainer', 'Coach', 'Fitness Instructor') THEN
            RAISE EXCEPTION 'Action denied: Employee ID % is defined as %, and therefore cannot be assigned to a program or workout.', NEW.employee_id, v_job_title;
        END IF;
        
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ========================================================
-- 4. Attach the function as a trigger to both tables
-- ========================================================
-- A. Trigger for training_program
CREATE TRIGGER trg_enforce_trainer_role_program
BEFORE INSERT OR UPDATE ON public.training_program
FOR EACH ROW
EXECUTE FUNCTION check_if_employee_is_trainer();

-- B. Trigger for workout_log
CREATE TRIGGER trg_enforce_trainer_role_workout
BEFORE INSERT OR UPDATE ON public.workout_log
FOR EACH ROW
EXECUTE FUNCTION check_if_employee_is_trainer();


-- ========================================================
-- 1. Randomly distribute existing NULL training programs among trainers (IDs 511-520)
-- ========================================================
UPDATE public.training_program
SET employee_id = floor(random() * (520 - 511 + 1) + 511)::int
WHERE employee_id IS NULL;

-- ========================================================
-- 2. Enforce NOT NULL constraint on training_program.employee_id
-- ========================================================
ALTER TABLE public.training_program 
ALTER COLUMN employee_id SET NOT NULL;