
DROP DATABASE IF EXISTS elbi_food_review;

CREATE DATABASE elbi_food_review;

use elbi_food_review;

CREATE TABLE FOOD_ESTABLISHMENT(
    restoname VARCHAR(16) NOT NULL UNIQUE,
    pin VARCHAR(50) NOT NULL,
    Establishment_id INT(3) NOT NULL AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(1000) NOT NULL,
    Capacity INT(3) NOT NULL,
    Type ENUM('Food Truck', 'Fine Dining', 'Cafe', 'Fast Food') NOT NULL,
    Average_rating DECIMAL(4,2) NOT NULL,
CONSTRAINT FOOD_ESTABLISHMENT_pk PRIMARY KEY(Establishment_id)
);

CREATE TABLE FOOD_ESTABLISHMENT_CONTACT(
    Establishment_id INT(3) NOT NULL,
    Contact VARCHAR(15) NOT NULL,
    CONSTRAINT FOOD_ESTABLISHMENT_CONTACT_Establishment_id_Contact_pk PRIMARY KEY(Establishment_id, Contact),
    CONSTRAINT FOOD_ESTABLISHMENT_CONTACT_Establishment_id_fk FOREIGN KEY(Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id)
);


CREATE TABLE FOOD_ESTABLISHMENT_LOCATION(
    Establishment_id INT(3) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Province VARCHAR(50) NOT NULL,
    CONSTRAINT FOOD_ESTABLISHMENT_CONTACT_Establishment_id_City_Province_pk PRIMARY KEY(Establishment_id, City, Province),
    CONSTRAINT FOOD_ESTABLISHMENT_LOCATION_Establishment_id_fk FOREIGN KEY(Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id)
);

CREATE TABLE FOOD_ESTABLISHMENT_SOCIAL_MEDIA_LINK(
    Establishment_id INT(3) NOT NULL,
    Social_media_link VARCHAR(100) NOT NULL,
    CONSTRAINT FoodEstab_socmed_link_pk PRIMARY KEY(Establishment_id, Social_media_link),
    CONSTRAINT FoodEstab_socmed_link_estabId_fk FOREIGN KEY(Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id)
);

CREATE TABLE FOOD(
    Food_id INT(3) NOT NULL AUTO_INCREMENT,
    Name VARCHAR(60) NOT NULL,
    Description VARCHAR(1000) NOT NULL,
    Caloric_count INT(3) NOT NULL,
    Price DECIMAL(6,2) NOT NULL,
    Average_rating DECIMAL(4,2) NOT NULL,
    Establishment_id INT(3) NOT NULL,
    CONSTRAINT FOOD_Food_id_pk PRIMARY KEY(Food_id),
    CONSTRAINT FOOD_Establishment_id_fk FOREIGN KEY(Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id)
);


CREATE TABLE FOOD_INGREDIENT(
    Food_id INT(3) NOT NULL,
    Ingredient VARCHAR(50) NOT NULL,
    CONSTRAINT FOOD_INGREDIENT_Food_id_ingredient_pk PRIMARY KEY(Food_id, Ingredient),
    CONSTRAINT FOOD_INGREDIENT_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD(Food_id)
);

CREATE TABLE MEAT(
    Food_id INT(3) NOT NULL,
    Type_of_meat ENUM('Beef', 'Pork', 'Poultry', 'Seafood') NOT NULL,
    Doneness ENUM('Rare', 'Medium Rare', 'Medium', 'Well Done'),
    Part_of_animal ENUM('Leg', 'Breast', 'Thigh', 'Wing'),
    CONSTRAINT MEAT_Food_id_pk  PRIMARY KEY(Food_id),
    CONSTRAINT MEAT_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD(Food_id)
);

CREATE TABLE VEGETABLE(
    Food_id INT(3) NOT NULL,
    Vegetable_family ENUM('Leafy', 'Root', 'Bulb', 'Stem'),
    CONSTRAINT VEGETABLE_Food_id_pk PRIMARY KEY(Food_id),
    CONSTRAINT VEGETABLE_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD(Food_id)
);

CREATE TABLE FRUIT(
    Food_id INT(3) NOT NULL,
    Ripeness ENUM('Raw', 'Ripe', 'Overripe'),
    Fruit_category ENUM('Citrus', 'Tropical', 'Berry'),
    Size ENUM('Small', 'Medium', 'Large'),
    CONSTRAINT FRUIT_Food_id_pk  PRIMARY KEY(Food_id),
    CONSTRAINT FRUIT_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD(Food_id)
);

CREATE TABLE DRINK(
    Food_id INT(3) NOT NULL,
    Sugar_level DECIMAL(4,2),
    Alcohol_level DECIMAL(4,2),
    Caffeine_level DECIMAL(4,2),
    Volume DECIMAL(6,2),
    CONSTRAINT DRINK_Food_id_pk PRIMARY KEY(Food_id),
    CONSTRAINT DRINK_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD(Food_id)
);

CREATE TABLE USERS(
    Username VARCHAR(16) NOT NULL UNIQUE,
    Email VARCHAR(30) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Bio VARCHAR(1000),
    Birthday DATE NOT NULL,
    Age INT(3) NOT NULL,
    First_name VARCHAR(50) NOT NULL,
    Middle_name VARCHAR(50) NOT NULL,
    Last_name VARCHAR(50) NOT NULL,
CONSTRAINT USER_Username_pk PRIMARY KEY(Username)
);

CREATE TABLE IS_RESTO_REVIEWED_BY(
    Username VARCHAR(50) NOT NULL,
    Establishment_id INT(3) NOT NULL,
    Review_date DATE NOT NULL,
    Comment VARCHAR(1000) NOT NULL,
    Rating DECIMAL(4,2) NOT NULL,
    CONSTRAINT IS_RESTO_REVIEWED_BY_Username_Establishment_id_pk PRIMARY KEY(Username, Establishment_id),
    CONSTRAINT IS_RESTO_REVIEWED_BY_Username_fk FOREIGN KEY(Username) REFERENCES USERS(Username),
    CONSTRAINT IS_RESTO_REVIEWED_BY_Establishment_id_fk FOREIGN KEY(Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id)
);

CREATE TABLE IS_FOOD_REVIEWED_BY(
    Username VARCHAR(50) NOT NULL,
    Establishment_id INT(3) NOT NULL,
    Food_id INT(3) NOT NULL,
    Review_date DATE NOT NULL,
    Comment VARCHAR(1000) NOT NULL,
    Rating DECIMAL(4,2) NOT NULL,
    CONSTRAINT IS_FOOD_REVIEWED_Username_Establishment_id_Food_id_pk  PRIMARY KEY(Username, Establishment_id, Food_id),
    CONSTRAINT IS_FOOD_REVIEWED_Username_fk FOREIGN KEY(Username) REFERENCES USERS(Username),
    CONSTRAINT IS_FOOD_REVIEWED_BY_Establishment_id_fk FOREIGN KEY(Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id),
    CONSTRAINT IS_FOOD_REVIEWED_BY_Food_id_fk FOREIGN KEY(Food_id) REFERENCES FOOD(Food_id)
);


--For number 1, it could be more conveniently done through a view.
CREATE VIEW ALL_FOOD_ESTABLISHMENTS AS SELECT Name as "Food Place", Description as "Description" FROM FOOD_ESTABLISHMENT; 
