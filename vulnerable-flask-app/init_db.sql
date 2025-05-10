-- SQL script to initialize the database schema and seed data for the vulnerable Flask application

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    bio TEXT
);

-- Insert sample data into the users table
INSERT INTO users (name, bio) VALUES 
('hung', 'I love beautiful girls'),
('thai', 'I love bep thoi'),
('bep', 'I enjoy hiking'),
('thoi', 'I love painting');