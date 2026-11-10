-- Creates the table second_table and adds four records
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Adds the record for John
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
-- Adds the record for Alex
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
-- Adds the record for Bob
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
-- Adds the record for George
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
