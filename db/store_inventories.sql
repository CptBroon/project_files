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

-- DUMMY CONTENT FOR DB

-- Categories
INSERT INTO category (name) VALUES ('Dog');
INSERT INTO category (name) VALUES ('Cat');
INSERT INTO category (name) VALUES ('Reptile');

INSERT INTO subcategory (name, category_id) VALUES ('Large dog', 1);
INSERT INTO subcategory (name, category_id) VALUES ('Small dog', 1);
INSERT INTO subcategory (name, category_id) VALUES ('Haired cat', 2);
INSERT INTO subcategory (name, category_id) VALUES ('Hairless cat', 2);
INSERT INTO subcategory (name, category_id) VALUES ('Snake', 3);
INSERT INTO subcategory (name, category_id) VALUES ('Pogona', 3);
INSERT INTO subcategory (name, category_id) VALUES ('Gecko', 3);

INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Labrador', 'Beginner', 3, 500, 800, TRUE, 1);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Husky', 'Expert', 1, 700, 1000, TRUE, 1);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Chihuahua', 'Intermediate', 1, 450, 750, TRUE, 2);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Dachshund', 'Beginner', 2, 600, 900, TRUE, 2);

INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Persian', 'Beginner', 2, 900, 1500, TRUE, 3);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Bengal', 'Expert', 1, 1200, 1700, TRUE, 3);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Sphynx', 'Intermediate', 1, 1000, 1600, TRUE, 4);

INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Boa', 'Intermediate', 5, 20, 50, TRUE, 5);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Bearded Dragon', 'Beginner', 6, 25, 80, TRUE, 6);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Crested Gecko', 'Intermediate', 3, 30, 75, TRUE, 7);
INSERT INTO species (name, difficulty, stock_no, buying_price, selling_price, active, subcategory_id) VALUES ('Leopard Gecko', 'Intermediate', 2, 30, 75, TRUE, 7);
