use elbi_food_review;

DELETE FROM is_food_reviewed_by;
DELETE FROM is_resto_reviewed_by;

DELETE FROM food_establishment_social_media_link;
DELETE FROM food_establishment_location;
DELETE FROM food_establishment_contact;

DELETE FROM food_ingredient;
DELETE FROM drink;
DELETE FROM meat;
DELETE FROM fruit;
DELETE FROM vegetable;

DELETE FROM food;
DELETE FROM food_establishment;

DELETE FROM USERS;

INSERT INTO food_establishment VALUES ('cels_fastfood', 'cels', 3, 'Cels Fastfood', 'We are located at 10634 Demarses Subdivision Batong Malake Los Banos Laguna', 50, 'Fast Food', 0);
INSERT INTO food_establishment_contact VALUES (3, '0915 289 2880');
INSERT INTO food_establishment_location VALUES (3, 'Los Banos', 'Laguna');
INSERT INTO food_establishment_social_media_link VALUES (3, 'https://www.facebook.com/cels.fastfood.7/');
INSERT INTO food_establishment VALUES ('cadapans', 'cadapan', 2, 'Cadapan', 'We are located at 10634 Demarses Subdivision Batong Malake Los Banos Laguna', 50, 'Fast Food', 0);
INSERT INTO food_establishment_contact VALUES (2, '0915 289 2880');
INSERT INTO food_establishment_location VALUES (2, 'Los Banos', 'Laguna');
INSERT INTO food_establishment_social_media_link VALUES (2, 'https://www.facebook.com/cadapans.7/');
INSERT INTO food_establishment VALUES ('elbi_food_review', 'elbi_food_review', 1, 'Elbi Food Review', 'We are located at 10634 Demarses Subdivision Batong Malake Los Banos Laguna', 50, 'Fast Food', 0);
INSERT INTO food_establishment_contact VALUES (1, '0915 289 2880');
INSERT INTO food_establishment_location VALUES (1, 'Los Banos', 'Laguna');
INSERT INTO food_establishment_location VALUES (1, 'Alaminos', 'Laguna');
INSERT INTO food_establishment_social_media_link VALUES (1, 'https://www.facebook.com/elbi_food_review.7/');


INSERT INTO food VALUES (1, 'Beef Nilaga', 'Type of stew cooked with potatoes, carrots, and sometimes plantains.', 560, 100.00, 4.5, 3);
INSERT INTO food_ingredient VALUES (1, 'Beef Brisket');
INSERT INTO food_ingredient VALUES (1, 'Potatoes');
INSERT INTO food_ingredient VALUES (1, 'Pechay');
INSERT INTO food_ingredient VALUES (1, 'Onion');
INSERT INTO food_ingredient VALUES (1, 'Carrots');
INSERT INTO food_ingredient VALUES (1, 'Whole Pepper Corn');
INSERT INTO meat VALUES (1, 'Beef', 'Well Done', 'Breast');
INSERT INTO vegetable VALUES (1, 'Root');



INSERT INTO food VALUES (2, 'Pork BBQ', 'A dish composed of marinated pork slices that are skewered and grilled.', 622, 30.00, 4.8, 3);
INSERT INTO food_ingredient VALUES (2, 'Pork');
INSERT INTO meat VALUES (2, 'Pork', 'Well Done', 'Breast');

INSERT INTO food VALUES (3, 'Guinisang Munggo', 'A Filipino savory mung bean soup.', 232, 15.00, 4.8, 2);
INSERT INTO food_ingredient VALUES (3, 'Mung Beans');
INSERT INTO food_ingredient VALUES (3, 'Thinly Sliced Pork');
INSERT INTO meat VALUES (3, 'Poultry', NULL, 'Breast');
INSERT INTO vegetable VALUES (3, 'Root');

INSERT INTO USERS VALUES ('ramnick_francis', 'john@example.com', 'password123', 'Hello, I''m John Doe!', '1990-01-01', 31, 'John', 'Doe', 'Doe');
INSERT INTO USERS VALUES ('jane_doe', 'jane@example.com', 'password123', 'Hello, I''m Jane Doe!', '1990-01-01', 31, 'Jane', 'Doe', 'Doe');

INSERT INTO is_food_reviewed_by VALUES ('john_doe', 1, 1, '2021-01-01', 'This is a delicious dish!', 4.8);
INSERT INTO is_food_reviewed_by VALUES ('jane_doe', 1, 1, '2021-01-01', 'This is a tasty dish!', 4.7);
INSERT INTO is_food_reviewed_by VALUES ('john_doe', 1, 3, '2021-01-01', 'This is a flavorful dish!', 4.9);
INSERT INTO is_food_reviewed_by VALUES ('jane_doe', 1, 3, '2021-01-01', 'This is a mouthwatering dish!', 4.6);

INSERT INTO is_resto_reviewed_by VALUES ('john_doe', 1, '2021-01-01', 'This is a fantastic restaurant!', 4.8);
INSERT INTO is_resto_reviewed_by VALUES ('jane_doe', 1, '2021-01-01', 'This is an amazing restaurant!', 4.7);
INSERT INTO is_resto_reviewed_by VALUES ('john_doe', 2, '2021-01-01', 'This is a wonderful restaurant!', 4.9);
INSERT INTO is_resto_reviewed_by VALUES ('jane_doe', 2, '2021-01-01', 'This is a superb restaurant!', 4.6);
