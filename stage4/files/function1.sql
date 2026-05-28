CREATE OR REPLACE FUNCTION public.fn_user_workout_stats(p_user_id INT)
RETURNS TABLE(
    total_sessions     INT,
    total_minutes      numeric(10,2),
    total_calories     BIGINT,
    avg_heart_rate     numeric(6,2),
    avg_rating         numeric(4,2),
    best_rating        INT,
    most_recent_log    DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_total_sessions  INT;
    v_total_minutes   numeric(10,2);
    v_total_calories  BIGINT;
    v_avg_heart_rate  numeric(6,2);
    v_avg_rating      numeric(4,2);
    v_best_rating     INT;
    v_most_recent     DATE;
BEGIN
    SELECT
        COUNT(*)::INT,
        COALESCE(SUM(duration_minutes), 0),
        COALESCE(SUM(total_calories_burned)::BIGINT, 0),
        COALESCE(ROUND(AVG(average_heart_rate), 2), 0),
        COALESCE(ROUND(AVG(trainee_feedback_rating), 2), 0),
        COALESCE(MAX(trainee_feedback_rating), 0),
        MAX(log_date)
    INTO
        v_total_sessions,
        v_total_minutes,
        v_total_calories,
        v_avg_heart_rate,
        v_avg_rating,
        v_best_rating,
        v_most_recent
    FROM public.workout_log
    WHERE user_id = p_user_id;

    IF v_total_sessions = 0 THEN
        RAISE NOTICE 'No workout logs found for user_id %.', p_user_id;
    END IF;

    total_sessions  := v_total_sessions;
    total_minutes   := v_total_minutes;
    total_calories  := v_total_calories;
    avg_heart_rate  := v_avg_heart_rate;
    avg_rating      := v_avg_rating;
    best_rating     := v_best_rating;
    most_recent_log := v_most_recent;

    RETURN NEXT;
END;
$$;
