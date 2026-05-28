CREATE OR REPLACE FUNCTION public.fn_trainee_progress_cursor(p_user_id INT)
RETURNS refcursor
LANGUAGE plpgsql
AS $$
DECLARE
    v_ref refcursor := 'trainee_progress_cursor';
    v_meas_rec  RECORD;
    v_explicit_cursor CURSOR FOR
        SELECT measurement_id, measurement_date, weight_kg
        FROM public.body_measurement
        WHERE user_id = p_user_id
        ORDER BY measurement_date;
BEGIN
    FOR v_meas_rec IN v_explicit_cursor LOOP
        IF v_meas_rec.weight_kg > 100 THEN
            RAISE NOTICE 'Measurement % on % is heavy: % kg',
                v_meas_rec.measurement_id,
                v_meas_rec.measurement_date,
                v_meas_rec.weight_kg;
        END IF;
    END LOOP;

    OPEN v_ref FOR
        SELECT
            bm.measurement_date,
            bm.weight_kg,
            bm.fat_percentage,
            bm.muscle_mass_kg,
            bm.bmi_score,
            bm.waist_circumference_cm,
            LAG(bm.weight_kg) OVER (ORDER BY bm.measurement_date) AS prev_weight,
            ROUND(bm.weight_kg - LAG(bm.weight_kg) OVER (ORDER BY bm.measurement_date), 2) AS weight_delta
        FROM public.body_measurement bm
        WHERE bm.user_id = p_user_id
        ORDER BY bm.measurement_date;

    RETURN v_ref;
END;
$$;
