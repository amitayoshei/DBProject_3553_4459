DO $$
DECLARE
    v_stats_rec RECORD;
    v_target_user_id INT := 1;
    v_label TEXT;
BEGIN
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running procedure: proc_extend_expiring_lockers';
    RAISE NOTICE '========================================';

    CALL public.proc_extend_expiring_lockers();

    RAISE NOTICE '';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running function: fn_user_workout_stats for user_id = %', v_target_user_id;
    RAISE NOTICE '========================================';

    SELECT * INTO v_stats_rec
    FROM public.fn_user_workout_stats(v_target_user_id);

    IF v_stats_rec.total_sessions = 0 THEN
        v_label := 'INACTIVE';
    ELSIF v_stats_rec.total_sessions < 5 THEN
        v_label := 'BEGINNER';
    ELSIF v_stats_rec.total_sessions < 20 THEN
        v_label := 'REGULAR';
    ELSE
        v_label := 'VETERAN';
    END IF;

    RAISE NOTICE 'User % Workout Summary:', v_target_user_id;
    RAISE NOTICE '  Status         : %', v_label;
    RAISE NOTICE '  Total Sessions : %', v_stats_rec.total_sessions;
    RAISE NOTICE '  Total Minutes  : %', v_stats_rec.total_minutes;
    RAISE NOTICE '  Total Calories : %', v_stats_rec.total_calories;
    RAISE NOTICE '  Avg Heart Rate : %', v_stats_rec.avg_heart_rate;
    RAISE NOTICE '  Avg Rating     : %', v_stats_rec.avg_rating;
    RAISE NOTICE '  Best Rating    : %', v_stats_rec.best_rating;
    RAISE NOTICE '  Last Workout   : %', v_stats_rec.most_recent_log;
    RAISE NOTICE '========================================';
    RAISE NOTICE 'main_program1 finished successfully.';
END;
$$;
