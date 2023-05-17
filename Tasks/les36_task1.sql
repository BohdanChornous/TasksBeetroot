CREATE TABLE IF NOT EXISTS people (
    id_user INT PRIMARY KEY,
    name varchar,
    surname varchar
);

ALTER TABLE people
RENAME TO second_generation;

ALTER TABLE second_generation
ADD COLUMN age int;

INSERT INTO second_generation(id_user, name, surname, age)
VALUES (1, 'Frodo', 'Baggins', 60),
       (2, 'Bilbo', 'Baggins', 105);

UPDATE second_generation
SET surname = 'torbins'
WHERE id_user = 1;

DELETE FROM second_generation
WHERE id_user = 1;
