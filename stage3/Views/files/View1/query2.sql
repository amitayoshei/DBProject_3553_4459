SELECT 
    EXTRACT(MONTH FROM expiration_date) AS expiration_month,
    COUNT(contract_number) AS total_active_contracts,
    SUM(total_cost) AS total_value
FROM vw_active_subscriptions
GROUP BY EXTRACT(MONTH FROM expiration_date)
ORDER BY expiration_month;