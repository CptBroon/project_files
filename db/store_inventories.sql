DROP TABLE IF EXISTS species;
DROP TABLE IF EXISTS subcategory;
DROP TABLE IF EXISTS category;

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE subcategory (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category_id INT REFERENCES category(id)
);

CREATE TABLE species (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    difficulty VARCHAR(255),
    stock_no INT,
    buying_price INT,
    selling_price INT,
    active BOOLEAN,
    subcategory_id INT REFERENCES subcategory(id)
);