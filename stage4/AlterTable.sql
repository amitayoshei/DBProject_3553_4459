UPDATE public.workout_log wl
SET log_date = GREATEST(DATE '2024-01-01', cu.join_date) + 
               ((wl.log_date - DATE '2020-01-01')::int % 365) * INTERVAL '1 day'
FROM public.core_user cu
WHERE wl.user_id = cu.user_id
  AND (wl.log_date < DATE '2024-01-01' OR wl.log_date < cu.join_date);

UPDATE public.body_measurement bm
SET measurement_date = GREATEST(DATE '2024-01-01', cu.join_date) + 
                       ((bm.measurement_date - DATE '2020-01-01')::int % 365) * INTERVAL '1 day'
FROM public.core_user cu
WHERE bm.user_id = cu.user_id
  AND (bm.measurement_date < DATE '2024-01-01' OR bm.measurement_date < cu.join_date);

UPDATE public.trainee_goal tg
SET creation_date = GREATEST(DATE '2024-01-01', cu.join_date),
    target_date   = GREATEST(DATE '2024-01-01', cu.join_date) + INTERVAL '180 days'
FROM public.core_user cu
WHERE tg.user_id = cu.user_id
  AND (tg.creation_date < DATE '2024-01-01' OR tg.creation_date < cu.join_date);

WITH height_anchor AS (
    SELECT
        user_id,
        ROUND(AVG(height_cm), 1) AS stable_height
    FROM public.body_measurement
    GROUP BY user_id
)
UPDATE public.body_measurement bm
SET height_cm = ha.stable_height
FROM height_anchor ha
WHERE bm.user_id = ha.user_id
  AND bm.height_cm <> ha.stable_height;

WITH ordered_measurements AS (
    SELECT
        measurement_id,
        user_id,
        measurement_date,
        weight_kg,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY measurement_date) AS rn,
        FIRST_VALUE(weight_kg) OVER (PARTITION BY user_id ORDER BY measurement_date) AS first_weight
    FROM public.body_measurement
),
smoothed AS (
    SELECT
        measurement_id,
        ROUND(
            first_weight * POWER(0.997, rn - 1)::numeric,
            2
        ) AS smoothed_weight
    FROM ordered_measurements
)
UPDATE public.body_measurement bm
SET weight_kg = s.smoothed_weight
FROM smoothed s
WHERE bm.measurement_id = s.measurement_id
  AND bm.weight_kg <> s.smoothed_weight;

UPDATE public.body_measurement
SET bmi_score = ROUND(
    weight_kg / POWER(height_cm / 100.0, 2),
    1
)
WHERE height_cm > 0
  AND bmi_score IS DISTINCT FROM ROUND(
    weight_kg / POWER(height_cm / 100.0, 2),
    1
  );
