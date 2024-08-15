CREATE TABLE IF NOT EXISTS public.Users
(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    signup_date DATE,
    domain VARCHAR(255)
);
