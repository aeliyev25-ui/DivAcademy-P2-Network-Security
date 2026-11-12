-- Run ONLY in PostgreSQL demo database 'p2lab'. No real personal data here.
CREATE TABLE IF NOT EXISTS lab_records (
    id SERIAL PRIMARY KEY,
    data_class VARCHAR(20),
    description TEXT
);
-- For an empty table only:
INSERT INTO lab_records (data_class, description) VALUES
('PUBLIC', 'Public project information'),
('INTERNAL', 'Internal infrastructure documentation'),
('CONFIDENTIAL', 'FAKE-FIN-TEST-001');
