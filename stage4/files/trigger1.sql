CREATE OR REPLACE FUNCTION public.trg_func_locker_rental_future_date()
RETURNS trigger
LANGUAGE plpgsql
AS $$
DECLARE
    v_join_date DATE;
BEGIN
    IF NEW.user_id IS NOT NULL AND NEW.rental_end_date IS NOT NULL THEN
        SELECT join_date INTO v_join_date
        FROM public.core_user
        WHERE user_id = NEW.user_id;

        IF v_join_date IS NULL THEN
            RAISE EXCEPTION 'Locker assignment failed: user_id % does not exist in core_user.', NEW.user_id;
        END IF;

        IF NEW.rental_end_date <= DATE '2024-01-01' THEN
            RAISE EXCEPTION 'Locker assignment failed: rental_end_date (%) must be after the system anchor date 2024-01-01.', NEW.rental_end_date;
        END IF;

        IF NEW.rental_end_date <= v_join_date THEN
            RAISE EXCEPTION 'Locker assignment failed: rental_end_date (%) cannot be on or before the user join_date (%).', NEW.rental_end_date, v_join_date;
        END IF;
    END IF;

    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_locker_rental_future_date ON public.locker;

CREATE TRIGGER trg_locker_rental_future_date
BEFORE INSERT OR UPDATE ON public.locker
FOR EACH ROW
EXECUTE FUNCTION public.trg_func_locker_rental_future_date();
