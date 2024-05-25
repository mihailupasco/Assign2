CREATE TABLE Person (
    id INT NOT NULL,
	name VARCHAR(255),
	age UNSIGNED INT NOT NULL CHECK (age > 0 AND age < 130),
	username VARCHAR(255),
    password VARCHAR(255),
	PRIMARY KEY(id)
);