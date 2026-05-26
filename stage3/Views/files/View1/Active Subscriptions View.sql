CREATE OR REPLACE VIEW vw_active_subscriptions AS
SELECT 
    cu.user_id,
    cu.first_name || ' ' || cu.last_name AS full_name,
    cu.phone_number,
    s.contract_number,
    s.purchase_date,
    s.expiration_date,
    s.total_cost,
    (s.expiration_date - DATE '2024-01-01') AS days_remaining
FROM public.core_user cu
JOIN public.subscription s ON cu.user_id = s.user_id
WHERE s.expiration_date >= DATE '2024-01-01';