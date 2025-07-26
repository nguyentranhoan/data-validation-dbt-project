SELECT
    customer_id,
    first_name,
    last_name,
    dob,
    email,
    phone,
    revenue
FROM
    {{ ref('raw_customer_data') }}
WHERE
    status = 'active'