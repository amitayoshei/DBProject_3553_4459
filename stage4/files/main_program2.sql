DO $$
DECLARE
    v_ref        refcursor;
    v_row        RECORD;
    v_row_count  INT := 0;
    v_target_user_id INT := 1;
    v_trend TEXT;
BEGIN
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running procedure: proc_award_achieved_goals';
    RAISE NOTICE '========================================';

    CALL public.proc_award_achieved_goals();

    RAISE NOTICE '';
    RAISE NOTICE '========================================';
    RAISE NOTICE 'Running function: fn_trainee_progress_cursor for user_id = %', v_target_user_id;
    RAISE NOTICE '========================================';

    BEGIN
        v_ref := public.fn_trainee_progress_cursor(v_target_user_id);

        LOOP
            FETCH v_ref INTO v_row;
            EXIT WHEN NOT FOUND;

            v_row_count := v_row_count + 1;

            IF v_row.weight_delta IS NULL THEN
                v_trend := 'FIRST RECORD';
            ELSIF v_row.weight_delta < 0 THEN
                v_trend := 'LOSING';
            ELSIF v_row.weight_delta > 0 THEN
                v_trend := 'GAINING';
            ELSE
                v_trend := 'STABLE';
            END IF;

            -- התיקון בוצע כאן: Fat: % %%
            RAISE NOTICE '[Row %] Date: % | Weight: % kg | Fat: % %% | BMI: % | Delta: % kg | Trend: %',
                v_row_count,
                v_row.measurement_date,
                v_row.weight_kg,
                v_row.fat_percentage,
                v_row.bmi_score,
                COALESCE(v_row.weight_delta::TEXT, 'N/A'),
                v_trend;
        END LOOP;

        CLOSE v_ref;

    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE 'Error while processing refcursor for user %: %', v_target_user_id, SQLERRM;
    END;

    IF v_row_count = 0 THEN
        RAISE NOTICE 'No body measurements found for user_id %.', v_target_user_id;
    ELSE
        RAISE NOTICE 'Total measurement rows processed: %', v_row_count;
    END IF;

    RAISE NOTICE '========================================';
    RAISE NOTICE 'main_program2 finished successfully.';
END;
$$;
