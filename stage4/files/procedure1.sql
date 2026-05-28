CREATE OR REPLACE PROCEDURE public.proc_extend_expiring_lockers()
LANGUAGE plpgsql
AS $$
DECLARE
    v_locker_rec RECORD;
    v_cursor CURSOR FOR
        SELECT l.locker_id, l.user_id, l.rental_end_date, cu.join_date
        FROM public.locker l
        JOIN public.core_user cu ON l.user_id = cu.user_id
        WHERE l.rental_end_date IS NOT NULL
          AND l.rental_end_date BETWEEN DATE '2024-01-01' AND DATE '2024-01-01' + INTERVAL '90 days';
    v_count INT := 0;
    v_new_end_date DATE;
BEGIN
    OPEN v_cursor;
    LOOP
        FETCH v_cursor INTO v_locker_rec;
        EXIT WHEN NOT FOUND;

        IF v_locker_rec.rental_end_date < DATE '2024-01-01' + INTERVAL '30 days' THEN
            v_new_end_date := v_locker_rec.rental_end_date + INTERVAL '365 days';
        ELSIF v_locker_rec.rental_end_date < DATE '2024-01-01' + INTERVAL '60 days' THEN
            v_new_end_date := v_locker_rec.rental_end_date + INTERVAL '180 days';
        ELSE
            v_new_end_date := v_locker_rec.rental_end_date + INTERVAL '90 days';
        END IF;

        UPDATE public.locker
        SET rental_end_date = v_new_end_date
        WHERE locker_id = v_locker_rec.locker_id;

        v_count := v_count + 1;
        RAISE NOTICE 'Locker % (user %): extended from % to %',
            v_locker_rec.locker_id, v_locker_rec.user_id,
            v_locker_rec.rental_end_date, v_new_end_date;
    END LOOP;
    CLOSE v_cursor;

    RAISE NOTICE 'proc_extend_expiring_lockers complete: % lockers updated.', v_count;
END;
$$;
