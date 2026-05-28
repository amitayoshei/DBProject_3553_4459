CREATE OR REPLACE FUNCTION public.trg_func_workout_log_date_check()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
    v_join_date DATE;
    v_user_rec  RECORD;
BEGIN
    SELECT user_id, join_date INTO v_user_rec
    FROM public.core_user
    WHERE user_id = NEW.user_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Workout log rejected: user_id % does not exist.', NEW.user_id;
    END IF;

    v_join_date := v_user_rec.join_date;

    IF NEW.log_date < v_join_date THEN
        RAISE EXCEPTION 'Workout log rejected: log_date (%) is before the user join_date (%) for user_id %.', NEW.log_date, v_join_date, NEW.user_id;
    END IF;

    IF NEW.log_date < DATE '2024-01-01' THEN
        RAISE EXCEPTION 'Workout log rejected: log_date (%) is before the system anchor date 2024-01-01.', NEW.log_date;
    END IF;

    IF NEW.trainee_feedback_rating < 1 OR NEW.trainee_feedback_rating > 10 THEN
        RAISE EXCEPTION 'Workout log rejected: trainee_feedback_rating (%) must be between 1 and 10.', NEW.trainee_feedback_rating;
    END IF;

    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_workout_log_date_check ON public.workout_log;

CREATE TRIGGER trg_workout_log_date_check
BEFORE INSERT OR UPDATE ON public.workout_log
FOR EACH ROW
EXECUTE FUNCTION public.trg_func_workout_log_date_check();
