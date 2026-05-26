SELECT full_name, phone_number, days_remaining
FROM vw_active_subscriptions
WHERE days_remaining <= 30 AND days_remaining >= 0
ORDER BY days_remaining ASC;