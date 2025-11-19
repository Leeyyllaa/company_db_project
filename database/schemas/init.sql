
-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Set timezone
SET timezone = 'Europe/Berlin';



CREATE TABLE IF NOT EXISTS "User" (
        user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        authentik_user_uuid UUID NOT NULL UNIQUE,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        birth_date DATE,
        entry_date DATE,
        exit_date DATE,
        status VARCHAR(50),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

