CREATE OR REPLACE PROCEDURE public.proc_award_achieved_goals()
LANGUAGE plpgsql
AS $$
DECLARE
    v_goal_rec   RECORD;
    v_last_weight   numeric(5,2);
    v_last_fat      numeric(4,1);
    v_updated_count INT := 0;
    v_error_count   INT := 0;
BEGIN
    FOR v_goal_rec IN
        SELECT tg.goal_id, tg.user_id, tg.target_date,
               tg.target_weight_kg, tg.target_fat_percentage, tg.is_achieved
        FROM public.trainee_goal tg
        WHERE tg.is_achieved = 0
          AND tg.target_date <= DATE '2024-01-01' + INTERVAL '365 days'
    LOOP
        BEGIN
            SELECT bm.weight_kg, bm.fat_percentage
            INTO v_last_weight, v_last_fat
            FROM public.body_measurement bm
            WHERE bm.user_id = v_goal_rec.user_id
              AND bm.measurement_date <= v_goal_rec.target_date
            ORDER BY bm.measurement_date DESC
            LIMIT 1;

            IF NOT FOUND THEN
                RAISE EXCEPTION 'No measurement found for user % before target_date %',
                    v_goal_rec.user_id, v_goal_rec.target_date;
            END IF;

            IF v_last_weight <= v_goal_rec.target_weight_kg AND
               v_last_fat <= v_goal_rec.target_fat_percentage THEN
                UPDATE public.trainee_goal
                SET is_achieved = 1
                WHERE goal_id = v_goal_rec.goal_id;

                v_updated_count := v_updated_count + 1;
                -- התיקון בוצע בשורה הבאה: נוסף % עבור המשתנה לפני ה-%%
                RAISE NOTICE 'Goal % for user % ACHIEVED (weight: %, fat: % %%)',
                    v_goal_rec.goal_id, v_goal_rec.user_id, v_last_weight, v_last_fat;
            END IF;

        EXCEPTION
            WHEN OTHERS THEN
                v_error_count := v_error_count + 1;
                RAISE NOTICE 'Skipping goal % for user %: %',
                    v_goal_rec.goal_id, v_goal_rec.user_id, SQLERRM;
        END;
    END LOOP;

    RAISE NOTICE 'proc_award_achieved_goals done. Updated: %, Skipped: %.', v_updated_count, v_error_count;
END;
$$;
