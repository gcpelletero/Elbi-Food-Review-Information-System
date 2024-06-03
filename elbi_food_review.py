import sys

import mysql.connector #For connecting to mariaDB

mariaDBConnect = mysql.connector.connect(
  host="localhost",  
  user="root",  
  password="ilovecmsc127",  
  database="elbi_food_review"
)

cursor = mariaDBConnect.cursor()

global userLoggedInUserName
global foodEstabLoggedInID

    

def horizontalLine():
    print("~-~-~-~-~-~-~-~-")


def signUp():
    horizontalLine()
    print("SIGN UP to ELBI FOOD REVIEW")
    print("Choose Account Type:")
    print("[1] Sign up as User")
    print("[2] Sign up as Food Establishment")
    print("[3] Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        signUpAsUser()
    elif choice == 2:
        signUpAsFoodEstab()
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        signUp()
    login()

def signUpAsUser():
# +-------------+---------------+------+-----+---------+-------+
# | Field       | Type          | Null | Key | Default | Extra |
# +-------------+---------------+------+-----+---------+-------+
# | Username    | varchar(16)   | NO   | PRI | NULL    |       |
# | Email       | varchar(30)   | NO   |     | NULL    |       |
# | Password    | varchar(50)   | NO   |     | NULL    |       |
# | Bio         | varchar(1000) | YES  |     | NULL    |       |
# | Birthday    | date          | NO   |     | NULL    |       |
# | Age         | int(3)        | NO   |     | NULL    |       |
# | First_name  | varchar(50)   | NO   |     | NULL    |       |
# | Middle_name | varchar(50)   | NO   |     | NULL    |       |
# | Last_name   | varchar(50)   | NO   |     | NULL    |       |
# +-------------+---------------+------+-----+---------+-------+
    print("Sign Up as User")
    username = input("Enter Username: ")
    first_name = input("Enter First Name: ")
    middle_name = input("Enter Middle Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    bio = input("Enter Bio (optional): ")
    birthday = input("Enter Birthday (YYYY-MM-DD): ")
    age = int(input("Enter Age: "))
    cursor.execute("INSERT INTO Users (Username, Email, Password, Bio, Birthday, Age, First_name, Middle_name, Last_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (username, email, password, bio, birthday, age, first_name, middle_name, last_name))
    mariaDBConnect.commit()    
        


def signUpAsFoodEstab():
# +------------------+-----------------------------------------------------+------+-----+---------+----------------+
# | Field            | Type                                                | Null | Key | Default | Extra          |
# +------------------+-----------------------------------------------------+------+-----+---------+----------------+
# | restoname        | varchar(16)                                         | NO   | UNI | NULL    |                |
# | pin              | varchar(50)                                         | NO   |     | NULL    |                |
# | Establishment_id | int(3)                                              | NO   | PRI | NULL    | auto_increment |
# | Name             | varchar(100)                                        | NO   |     | NULL    |                |
# | Description      | varchar(1000)                                       | NO   |     | NULL    |                |
# | Capacity         | int(3)                                              | NO   |     | NULL    |                |
# | Type             | enum('Food Truck','Fine Dining','Cafe','Fast Food') | NO   |     | NULL    |                |
# | Average_rating   | decimal(1,1)                                        | NO   |     | NULL    |                |
# +------------------+-----------------------------------------------------+------+-----+---------+----------------+
    print("Sign Up as Food Establishment");
    restoname = input("Enter Restaurant Username: ")
    pin = input("Enter PIN: ")
    name = input("Enter Restaurant Name: ")

# MariaDB [elbi_food_review]> desc food_establishment_contact;
# +------------------+-------------+------+-----+---------+-------+
# | Field            | Type        | Null | Key | Default | Extra |
# +------------------+-------------+------+-----+---------+-------+
# | Establishment_id | int(3)      | NO   | PRI | NULL    |       |
# | Contact          | varchar(15) | NO   | PRI | NULL    |       |
# +------------------+-------------+------+-----+---------+-------+
# 2 rows in set (0.015 sec)

# MariaDB [elbi_food_review]> desc food_establishment_location;
# +------------------+-------------+------+-----+---------+-------+
# | Field            | Type        | Null | Key | Default | Extra |
# +------------------+-------------+------+-----+---------+-------+
# | Establishment_id | int(3)      | NO   | PRI | NULL    |       |
# | City             | varchar(50) | NO   | PRI | NULL    |       |
# | Province         | varchar(50) | NO   | PRI | NULL    |       |
# +------------------+-------------+------+-----+---------+-------+
# 3 rows in set (0.005 sec)

# MariaDB [elbi_food_review]> desc food_establishment_social_media_link;
# +-------------------+--------------+------+-----+---------+-------+
# | Field             | Type         | Null | Key | Default | Extra |
# +-------------------+--------------+------+-----+---------+-------+
# | Establishment_id  | int(3)       | NO   | PRI | NULL    |       |
# | Social_media_link | varchar(100) | NO   | PRI | NULL    |       |
# +-------------------+--------------+------+-----+---------+-------+
# 2 rows in set (0.004 sec)
  
        
    description = input("Enter Description: ")
    capacity = int(input("Enter Capacity: "))
    print("Choose Type:")
    print("[1] Food Truck")
    print("[2] Fine Dining")
    print("[3] Cafe")
    print("[4] Fast Food")
    choice = int(input("Enter choice: "))
    if choice == 1:
        type = "Food Truck"
    elif choice == 2:
        type = "Fine Dining"
    elif choice == 3:
        type = "Cafe"
    elif choice == 4:
        type = "Fast Food"
    else:
        print("Invalid choice. Please try again.")
        signUpAsFoodEstab()
    average_rating = 0
    cursor.execute("INSERT INTO Food_Establishment (restoname, pin, Name, Description, Capacity, Type, Average_rating) VALUES (%s, %s, %s, %s, %s, %s, %s)", (restoname, pin, name, description, capacity, type, average_rating))
    mariaDBConnect.commit()


    while True:
        print("Location ")
        city = input("Enter City: ")
        province = input("Enter Province: ")
        cursor.execute("INSERT INTO Food_Establishment_Location (Establishment_id, City, Province) VALUES (LAST_INSERT_ID(), %s, %s)", (city, province))
        mariaDBConnect.commit()
        print("Do you want to add another location?")
        print("[1] Yes")
        print("[2] No")
        choice = int(input("Enter choice: "))
        if choice == 2:
            break

    print("More Information")
    print("Do you want to add social media links?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        while True:
            social_media_link = input("Enter Social Media Link: ")
            cursor.execute("INSERT INTO Food_Establishment_Social_Media_Link (Establishment_id, Social_media_link) VALUES (LAST_INSERT_ID(), %s)", (social_media_link,))
            mariaDBConnect.commit()
            print("Do you want to add another social media link?")
            print("[1] Yes")
            print("[2] No")
            choice = int(input("Enter choice: "))
            if choice == 2:
                break
    
    print("Do you want to add contact numbers?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        while True:
            contact = input("Enter Contact Number: ")
            cursor.execute("INSERT INTO Food_Establishment_Contact (Establishment_id, Contact) VALUES (LAST_INSERT_ID(), %s)", (contact,))
            mariaDBConnect.commit()
            print("Do you want to add another contact number?")
            print("[1] Yes")
            print("[2] No")
            choice = int(input("Enter choice: "))
            if choice == 2:
                break
    
    

def reviewShower(reviews):

    if reviews == []:
        print("No reviews found.")
    for review in reviews:
        print("----------------------------------------------------------------------")
        print("Username: ", review[0])
        print("Review Date: ", review[2])
        print("Comment: ", review[3])
        print("Rating: ", review[4])
      
def viewReviewsResto(restoId):
    
    print("\n")
    print("Select the date range of the reviews you want to see.")
    print("[1] All")
    print("[2] Custom")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("\n")
        smallHorizontalLine()
        cursor.execute("SELECT * FROM Food_Establishment WHERE Establishment_id = %s", (restoId,))
        foodEstab = cursor.fetchall()
        print("REVIEWS FOR ", foodEstab[0][3])
        smallHorizontalLine()
        print("\n")

        cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Establishment_id = %s", (restoId,))
        reviews = cursor.fetchall()
        reviewShower(reviews)
        
        
    
      
    if choice == 2:
        startDate = input("Enter Start Date (YYYY-MM-DD): ")
        endDate = input("Enter End Date (YYYY-MM-DD): ")
        cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Establishment_id = %s AND Review_date BETWEEN %s AND %s", (restoId, startDate, endDate))
        reviews = cursor.fetchall()
        
        print("\n")
        smallHorizontalLine()
        cursor.execute("SELECT * FROM Food_Establishment WHERE Establishment_id = %s", (restoId,))
        foodEstab = cursor.fetchall()
        print("REVIEWS FOR ", foodEstab[0][3])
        smallHorizontalLine()
        print("\n")
        
        reviewShower(reviews)

    cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s", (restoId,))
    foodReviews = cursor.fetchall()
    if foodReviews != []:
        viewFoodReviewsFromResto(restoId)

def viewFoodReviewsFromResto(restoId):
    print("\n")
    print("Do you want to see the reviews for food items for this restaurant?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("View by:")
        print("[1] View All")
        print("[2] Search Keyword")
    
        choice = int(input("Enter choice: "))
        if choice == 1:
            viewFoodReviewsForAResto(restoId)
        elif choice == 2:
            viewFoodRevieSearch(restoId)
       
        

def viewFoodRevieSearch(restoId):
    keyword = input("Enter Keyword: ")
    cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s AND Comment LIKE %s", (restoId, '%' + keyword + '%'))
    reviews = cursor.fetchall()
    reviewShower(reviews)



def viewRestoReviewSearch(restoId):
    print("Do you want to serach using keyword or by rating?");
    print("[1] Search by Keyword")
    print("[2] Search by Rating")
    choice = int(input("Enter choice: "))
    if choice == 1:
        keyword = input("Enter Keyword: ")
        cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Establishment_id = %s AND Comment LIKE %s", (restoId, '%' + keyword + '%'))
        reviews = cursor.fetchall()
        reviewShower(reviews)
    elif choice == 2:
        print("Tier of Rating:")
        print("[1] 0-2 *")
        print("[2] 2-3 **")
        print("[3] 3-4 ***")
        print("[4] 4-5 ****")
        choice = int(input("Enter choice: "))
        if choice == 1:
            ratingLower = 0
            ratingUpper = 2
        elif choice == 2:
            ratingLower = 2
            ratingUpper = 3
        elif choice == 3:
            ratingLower = 3
            ratingUpper = 4
        elif choice == 4:
            ratingLower = 4
            ratingUpper = 5
        else:
            print("Invalid choice. Please try again.")
            viewRestoReviewSearch(restoId)
        cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Establishment_id = %s AND Rating BETWEEN %s AND %s", (restoId, ratingLower, ratingUpper))
        reviews = cursor.fetchall()
        reviewShower(reviews)


def viewFoodReviewsForAResto(restoId):
    cursor.execute("Select * from is_food_reviewed_by where Establishment_id = %s", (restoId,))
    reviews = cursor.fetchall()
    if reviews == []:
        print("No reviews found.")
        return
    
    print("\n")
    smallHorizontalLine()
    cursor.execute("SELECT * FROM Food_Establishment WHERE Establishment_id = %s", (restoId,))
    foodEstab = cursor.fetchall()
    print("FOOD REVIEWS FOR ", foodEstab[0][3])
    smallHorizontalLine()
    print("\n")

    print("Do you want to search for reviews or filter by date")
    print("[1] Search or Filter Criteria")
    print("[2] Filter by Date")
    print("[3] View All")
    choice = int(input("Enter choice: "))
    if choice == 1:
        viewRestoReviewSearch(restoId)
    elif choice == 2:
        print("Select the date range of the reviews you want to see.")
        print("[1] All")
        print("[2] Custom")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Arrange by:")
            print("[1] Ascending")
            print("[2] Descending")
            choice = int(input("Enter choice: "))
            if choice == 1:
                cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s ORDER BY Review_date ASC", (restoId,))
                reviews = cursor.fetchall()
                reviewShower(reviews)
            elif choice == 2:
                cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s ORDER BY Review_date DESC", (restoId,))
                reviews = cursor.fetchall()
                reviewShower(reviews)
        if choice == 2:
            startDate = input("Enter Start Date (YYYY-MM-DD): ")
            endDate = input("Enter End Date (YYYY-MM-DD): ")
            print("Arrange by:")
            print("[1] Ascending")
            print("[2] Descending")
            choice = int(input("Enter choice: "))
            if choice == 1:
                cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s AND Review_date BETWEEN %s AND %s ORDER BY Review_date ASC", (restoId, startDate, endDate))
                reviews = cursor.fetchall()
                reviewShower(reviews)
            elif choice == 2:
                cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s AND Review_date BETWEEN %s AND %s ORDER BY Review_date DESC", (restoId, startDate, endDate))
                reviews = cursor.fetchall()
                reviewShower(reviews)
    elif choice == 3:
        cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s", (restoId,))
        reviews = cursor.fetchall()
        reviewShower(reviews)

def justFoodEstablishmentShower():
    cursor.execute("SELECT * FROM Food_Establishment")
    foodEstabs = cursor.fetchall()
    if foodEstabs == []:
        print("No food establishments found.")
    print("ID\tName")
    for foodEstablishment in foodEstabs:
    
        print("%s\t%s" % (foodEstablishment[2], foodEstablishment[3]))

def establishmentShower(establishments):
# +------------------+-----------------------------------------------------+------+-----+---------+----------------+
# | Field            | Type                                                | Null | Key | Default | Extra          |
# +------------------+-----------------------------------------------------+------+-----+---------+----------------+
# | restoname        | varchar(16)                                         | NO   | UNI | NULL    |                |
# | pin              | varchar(50)                                         | NO   |     | NULL    |                |
# | Establishment_id | int(3)                                              | NO   | PRI | NULL    | auto_increment |
# | Name             | varchar(100)                                        | NO   |     | NULL    |                |
# | Description      | varchar(1000)                                       | NO   |     | NULL    |                |
# | Capacity         | int(3)                                              | NO   |     | NULL    |                |
# | Type             | enum('Food Truck','Fine Dining','Cafe','Fast Food') | NO   |     | NULL    |                |
# | Average_rating   | decimal(4,2)                                        | NO   |     | NULL    |                |
# +------------------+-----------------------------------------------------+------+-----+---------+----------------+
    if establishments == []:
        print("No establishments found.")
    else:
        print("\n")
        smallHorizontalLine()
        print("ALL THE ESTABLISMENTS")
        smallHorizontalLine()
        print("\n")
    for establishment in establishments:
        
        smallHorizontalLine()
        print("Establishment ID: ", establishment[2])
        print("Name: ", establishment[3])
        print("Description: ", establishment[4])
        print("Capacity: ", establishment[5])
        print("Type: ", establishment[6])
        
        print("Average Rating of the Facilities: ", establishment[7])

        cursor.execute("SELECT AVG(Rating) FROM is_food_reviewed_by WHERE Establishment_id = %s", (establishment[2],))
        averageRatingFoodResult = cursor.fetchone()
        
        if averageRatingFoodResult is not None:
            averageRatingFood = averageRatingFoodResult[0]
            print("Average Food Rating: ", averageRatingFood)
        else:
            print("No average food rating found.")
        smallHorizontalLine()
        print("\n")
        

def foodAverageRatUpdater(food_id):
    cursor.execute("SELECT AVG(Rating) FROM is_food_reviewed_by WHERE Food_id = %s", (food_id,))
    averageRatingResult = cursor.fetchone()
    if averageRatingResult is not None:
        averageRating = averageRatingResult[0]
        cursor.execute("UPDATE Food SET Average_rating = %s WHERE Food_id = %s", (averageRating, food_id))
        mariaDBConnect.commit()

def restoAverageRatUpdater(establishment_id):
    cursor.execute("SELECT AVG(Rating) FROM is_resto_reviewed_by WHERE Establishment_id = %s", (establishment_id,))
    averageRatingResult = cursor.fetchone()
    if averageRatingResult is not None:
        averageRating = averageRatingResult[0]
        cursor.execute("UPDATE Food_Establishment SET Average_rating = %s WHERE Establishment_id = %s", (averageRating, establishment_id))
        mariaDBConnect.commit()

def viewFoodEstabsAll():
    cursor.execute("SELECT * FROM Food_Establishment")
    foodEstabs = cursor.fetchall()
    establishmentShower(foodEstabs)

    print("Do you want to see the reviews for a restaurant?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose which establishment")
        justFoodEstablishmentShower()
        restoid = int(input("Enter Establishment ID: "))
        viewReviewsResto(restoid)

def viewFoodEstabsSearch():
    print("Search Food Establishments")
    print("Choose search criteria:")
    print("[1] Name")
    print("[2] Type")
    print("[3] Average Rating")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        cursor.execute("SELECT * FROM Food_Establishment WHERE Name LIKE %s", ('%' + name + '%',))
        foodEstabs = cursor.fetchall()
        establishmentShower(foodEstabs)

    elif choice == 2:
        print("Choose Type:")
        print("[1] Food Truck")
        print("[2] Fine Dining")
        print("[3] Cafe")
        print("[4] Fast Food")
        choice = int(input("Enter choice: "))
        if choice == 1:
            type = "Food Truck"
        elif choice == 2:
            type = "Fine Dining"
        elif choice == 3:
            type = "Cafe"
        elif choice == 4:
            type = "Fast Food"
        else:
            print("Invalid choice. Please try again.")
            viewFoodEstabsSearch()
        cursor.execute("SELECT * FROM Food_Establishment WHERE Type = %s", (type,))
        foodEstabs = cursor.fetchall()
        establishmentShower(foodEstabs)

    elif choice == 3:
        print("Tier of Rating:")
        print("[1] 0-2 *")
        print("[2] 2-3 **")
        print("[3] 3-4 ***")
        print("[4] 4-5 ****")
        choice = int(input("Enter choice: "))
        if choice == 1:
            ratingLower = 0
            ratingUpper = 2
        elif choice == 2:
            ratingLower = 2
            ratingUpper = 3

        elif choice == 3:
            ratingLower = 3
            ratingUpper = 4
        elif choice == 4:
            ratingLower = 4
            ratingUpper = 5
        else:
            print("Invalid choice. Please try again.")
            viewFoodEstabsSearch()
        cursor.execute("SELECT * FROM Food_Establishment WHERE Average_rating BETWEEN %s AND %s", (ratingLower, ratingUpper))
        foodEstabs = cursor.fetchall()
        establishmentShower(foodEstabs)
        
    
def rateResto():
# MariaDB [elbi_food_review]> desc is_resto_reviewed_by;
# +------------------+---------------+------+-----+---------+-------+
# | Field            | Type          | Null | Key | Default | Extra |
# +------------------+---------------+------+-----+---------+-------+
# | Username         | varchar(50)   | NO   | PRI | NULL    |       |
# | Establishment_id | int(3)        | NO   | PRI | NULL    |       |
# | Review_date      | date          | NO   |     | NULL    |       |
# | Comment          | varchar(1000) | NO   |     | NULL    |       |
# | Rating           | decimal(1,1)  | NO   |     | NULL    |       |
# +------------------+---------------+------+-----+---------+-------+
    
    print("First, choose which restaurant you want to rate.")
    justFoodEstablishmentShower()
    establishment_id = int(input("Enter Establishment ID You want to Rate: "))
    cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Establishment_id = %s AND Username = %s", (establishment_id, userLoggedInUserName))
    if cursor.fetchone() is not None:
        print("You have already rated this restaurant.")
        print("Do you want to update your rating?")
        print("[1] Yes")
        print("[2] No")
        choice = int(input("Enter choice: "))
        if choice == 1:
            editComments()
    else:
        comment = input("Enter Comment: ")
        rating = float(input("Enter Rating: "))
        cursor.execute("INSERT INTO is_resto_reviewed_by (Username, Establishment_id, Review_date, Comment, Rating) VALUES (%s, %s, CURDATE(), %s, %s)", (userLoggedInUserName, establishment_id, comment, rating))
        mariaDBConnect.commit()
        restoAverageRatUpdater(establishment_id)

def rateRestoForFood():
# MariaDB [elbi_food_review]> desc is_resto_reviewed_by;
# +------------------+---------------+------+-----+---------+-------+
# | Field            | Type          | Null | Key | Default | Extra |
# +------------------+---------------+------+-----+---------+-------+
# | Username         | varchar(50)   | NO   | PRI | NULL    |       |
# | Establishment_id | int(3)        | NO   | PRI | NULL    |       |
# | Review_date      | date          | NO   |     | NULL    |       |
# | Comment          | varchar(1000) | NO   |     | NULL    |       |
# | Rating           | decimal(1,1)  | NO   |     | NULL    |       |
# +------------------+---------------+------+-----+---------+-------+
    
    print("Rate Restaurant")
    justFoodEstablishmentShower()
    establishment_id = int(input("Enter Establishment ID whos Food You want to Rate: "))
    cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Establishment_id = %s AND Username = %s", (establishment_id, userLoggedInUserName))
    if cursor.fetchone() is not None:
        print("You have already rated this restaurant.")
        print("Do you want to update your rating?")
        print("[1] Yes")
        print("[2] No")
        choice = int(input("Enter choice: "))
        if choice == 1:
            editComments()
    else:
        comment = input("Enter Comment: ")
        rating = float(input("Enter Rating: "))
        cursor.execute("INSERT INTO is_resto_reviewed_by (Username, Establishment_id, Review_date, Comment, Rating) VALUES (%s, %s, CURDATE(), %s, %s)", (userLoggedInUserName, establishment_id, comment, rating))
        mariaDBConnect.commit()
        restoAverageRatUpdater(establishment_id)
    print("Now, rate the food item of the restaurant.")
    return establishment_id

def smallHorizontalLine():
    print("~-~-~-~-~-")

def foodItemShower(foodItems):
    if foodItems == []:
        print("No food items found.")

    for foodItem in foodItems:
        print("\n")
        horizontalLine()
        print("Food ID: ", foodItem[0])
        print("Name: ", foodItem[1])
        cursor.execute("SELECT * FROM Food_Establishment WHERE Establishment_id = %s", (foodItem[6],))
        establishment = cursor.fetchall()
        print("From Restaurant: ", establishment[0][3])
        print("Price: ", foodItem[2])
        cursor.execute("SELECT AVG(Rating) FROM is_food_reviewed_by WHERE Food_id = %s", (foodItem[0],))
        averageRatingResult = cursor.fetchone()
        print("Average Rating: ", averageRatingResult[0])
        cursor.execute("SELECT * FROM Meat WHERE Food_id = %s", (foodItem[0],))
        meatDetails = cursor.fetchall()
        
        if meatDetails:
            smallHorizontalLine()
            meatDetails = meatDetails[0]

            if meatDetails[1] is not None:
                print("Type of Meat: ", meatDetails[1])
            if meatDetails[2] is not None:
                print("Doneness: ", meatDetails[2])
            if meatDetails[3] is not None:
                print("Part of Animal: ", meatDetails[3])
        cursor.execute("SELECT * FROM Fruit WHERE Food_id = %s", (foodItem[0],))
        fruitDetails = cursor.fetchall()
        if fruitDetails:
            smallHorizontalLine()
            fruitDetails = fruitDetails[0]
            if fruitDetails[1] is not None:
                print("Ripeness: ", fruitDetails[1])
            if fruitDetails[2] is not None:
                print("Fruit Category: ", fruitDetails[2])
            if fruitDetails[3] is not None:
                print("Size: ", fruitDetails[3])
        cursor.execute("SELECT * FROM Vegetable WHERE Food_id = %s", (foodItem[0],))
        vegetableDetails = cursor.fetchall()
        if vegetableDetails:
            smallHorizontalLine()
            vegetableDetails = vegetableDetails[0]
            if vegetableDetails[1] is not None:
                print("Type of Vegetable: ", vegetableDetails[1])
            
            
        cursor.execute("SELECT * FROM Drink WHERE Food_id = %s", (foodItem[0],))
        drinkDetails = cursor.fetchall()

# +----------------+--------------+------+-----+---------+-------+
# | Field          | Type         | Null | Key | Default | Extra |
# +----------------+--------------+------+-----+---------+-------+
# | Food_id        | int(3)       | NO   | PRI | NULL    |       |
# | Sugar_level    | decimal(4,2) | YES  |     | NULL    |       |
# | Alcohol_level  | decimal(4,2) | YES  |     | NULL    |       |
# | Caffeine_level | decimal(4,2) | YES  |     | NULL    |       |
# | Volume         | decimal(6,2) | YES  |     | NULL    |       |
# +----------------+--------------+------+-----+---------+-------+
# 5 rows in set (0.003 sec)
        if drinkDetails:
            smallHorizontalLine()
            drinkDetails = drinkDetails[0]
            if drinkDetails[1] is not None:
                print("Sugar Level: ", drinkDetails[1])
            if drinkDetails[2] is not None:
                print("Alcohol Level: ", drinkDetails[2])
            if drinkDetails[3] is not None:
                print("Caffeine Level: ", drinkDetails[3])
            if drinkDetails[4] is not None:
                print("Volume: ", drinkDetails[4])
         

def justFoodItemShowerFromEstab(establishment_id):
    cursor.execute("SELECT * FROM Food WHERE Establishment_id = %s", (establishment_id,))
    foodItems = cursor.fetchall()

    if foodItems == []:
        print("No food items found.")
    else:
        print("Food ID\tName")
        for foodItem in foodItems:
            print("%s\t%s" % (foodItem[0], foodItem[1]))
    


def rateFoodItem():
# MariaDB [elbi_food_review]> desc is_food_reviewed_by;
# +------------------+---------------+------+-----+---------+-------+
# | Field            | Type          | Null | Key | Default | Extra |
# +------------------+---------------+------+-----+---------+-------+
# | Username         | varchar(50)   | NO   | PRI | NULL    |       |
# | Establishment_id | int(3)        | NO   | PRI | NULL    |       |
# | Food_id          | int(3)        | NO   | PRI | NULL    |       |
# | Review_date      | date          | NO   |     | NULL    |       |
# | Comment          | varchar(1000) | NO   |     | NULL    |       |
# | Rating           | decimal(1,1)  | NO   |     | NULL    |       |
# +------------------+---------------+------+-----+---------+-------+
    print("For this, you are going to rate a food item from the restaurant.")

    establishment_id = rateRestoForFood()
    print("Eto pinili mo", establishment_id)
    cursor.execute("SELECT * from Food where Establishment_id = %s", (establishment_id,))  
    foodItems = cursor.fetchall()

    if foodItems == []:
        print("There is no food to comment for this restaurant.")
        return

    justFoodItemShowerFromEstab(establishment_id)
    print("Choose the food item you want to rate.")
    food_id = int(input("Enter Food ID: "))

    cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Establishment_id = %s AND username = %s AND food_id = %s", (establishment_id, userLoggedInUserName, food_id))
    if cursor.fetchone() is not None:
        print("You have already rated this food item from this restaurant.")
        print("Do you want to update your rating?")
        print("[1] Yes")
        print("[2] No")
        choice = int(input("Enter choice: "))

        if choice == 1:
            editComments()
    else:
        comment = input("Enter Comment: ")
        rating = float(input("Enter Rating: "))
        cursor.execute("INSERT INTO is_food_reviewed_by (Username, Establishment_id, Food_id, Review_date, Comment, Rating) VALUES (%s, %s, %s, CURDATE(), %s, %s)", (userLoggedInUserName, establishment_id, food_id, comment, rating))
        mariaDBConnect.commit()
        foodAverageRatUpdater(food_id)

def viewFoodItemsAll():
    cursor.execute("SELECT * FROM Food")
    foodItems = cursor.fetchall()

    foodItemShower(foodItems)
    print("Do you want to rate this food and its restaurant?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))

    if choice == 1:
        rateFoodItem()

def viewFoodItemsSearch():
    print("Search results by:")
    print("[1] Rating")
    print("[2] Price")
    print("[3] Type")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Tier of Rating:")
        print("[1] 0-2 *")
        print("[2] 2-3 **")
        print("[3] 3-4 ***")
        print("[4] 4-5 ****")
        choice = int(input("Enter choice: "))
        if choice == 1:
            ratingLower = 0
            ratingUpper = 2
        elif choice == 2:
            ratingLower = 2
            ratingUpper = 3
        elif choice == 3:
            ratingLower = 3
            ratingUpper = 4
        elif choice == 4:
            ratingLower = 4
            ratingUpper = 5
        else:
            print("Invalid choice. Please try again.")
            viewFoodItemsSearch()
        cursor.execute("SELECT * FROM Food WHERE Average_rating BETWEEN %s AND %s", (ratingLower, ratingUpper))
        foodItems = cursor.fetchall()
     
        foodItemShower(foodItems)
        
    elif choice == 2:
        print("View by order or by range?")
        print("[1] Order")
        print("[2] Range")

        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Choose Order:")
            print("[1] Ascending")
            print("[2] Descending")
            choice = int(input("Enter choice: "))
            if choice == 1:
                cursor.execute("SELECT * FROM Food ORDER BY Price ASC")
            elif choice == 2:
                cursor.execute("SELECT * FROM Food ORDER BY Price DESC")
            foodItems = cursor.fetchall()
            
            foodItemShower(foodItems)
        elif choice == 2:
            price = float(input("Enter Price: "))
            degreesOfFreedom = float(input("Enter a +- range: "))
            cursor.execute("SELECT * FROM Food WHERE Price BETWEEN %s AND %s", (price - degreesOfFreedom, price + degreesOfFreedom))
            foodItems = cursor.fetchall()
           
            foodItemShower(foodItems)
            
    elif(choice == 3):
        print("Choose Type:")
        print("[1] Meat")
        print("[2] Fruit")
        print("[3] Vegetable")
        print("[4] Drink")
        choice = int(input("Enter choice: "))
        if choice == 1:
            cursor.execute("SELECT * FROM Meat")
            meatDetails = cursor.fetchall()
            foodItems = []
            for meatDetail in meatDetails:
                food_id = meatDetail[0]
                cursor.execute("SELECT * FROM Food WHERE Food_id = %s", (food_id,))
                foodItem = cursor.fetchone()
                foodItems.append(foodItem)
        elif choice == 2:
            cursor.execute("SELECT * FROM Fruit")
            fruitDetails = cursor.fetchall()
            foodItems = []
            for fruitDetail in fruitDetails:
                food_id = fruitDetail[0]
                cursor.execute("SELECT * FROM Food WHERE Food_id = %s", (food_id,))
                foodItem = cursor.fetchone()
                foodItems.append(foodItem)
        elif choice == 3:
            cursor.execute("SELECT * FROM Vegetable")
            vegetableDetails = cursor.fetchall()
            foodItems = []
            for vegetableDetail in vegetableDetails:
                food_id = vegetableDetail[0]
                cursor.execute("SELECT * FROM Food WHERE Food_id = %s", (food_id,))
                foodItem = cursor.fetchone()
                foodItems.append(foodItem)
        elif choice == 4:
            cursor.execute("SELECT * FROM Drink")
            drinkDetails = cursor.fetchall()
            foodItems = []
            for drinkDetail in drinkDetails:
                food_id = drinkDetail[0]
                cursor.execute("SELECT * FROM Food WHERE Food_id = %s", (food_id,))
                foodItem = cursor.fetchone()
                foodItems.append(foodItem)
        else:
            print("Invalid choice. Please try again.")
            viewFoodItemsSearch()

        foodItemShower(foodItems)

def viewFoodItem():
    print("Do you want to see all or search?")
    print("[1] All")
    print("[2] Search")
    choice = int(input("Enter choice: "))
    if choice == 1:
        viewFoodItemsAll()
    elif choice == 2:
        viewFoodItemsSearch()

def viewFoodEstabs():
    print("Do you want to see all or search?")
    print("[1] All")
    print("[2] Search")
    choice = int(input("Enter choice: "))
    if choice == 1:
        viewFoodEstabsAll()
    elif choice == 2:
        viewFoodEstabsSearch()
    else:
        print("Invalid choice. Please try again.")
        viewFoodEstabs()

def editUserProfile():
    global userLoggedInUserName
   
    print("userLoggedInUserName: ", userLoggedInUserName)
    print("marker")
    print("Edit Profile")
    print("Current Profile: ")
    cursor.execute("SELECT * FROM Users WHERE Username = %s", (userLoggedInUserName,))
    user = cursor.fetchone()
    print("Username: ", user[0])
    print("Email: ", user[1])
    print("Password: ", user[2])
    print("Bio: ", user[3])
    print("Birthday: ", user[4])
    print("Age: ", user[5])
    print("First Name: ", user[6])
    print("Middle Name: ", user[7])
    print("Last Name: ", user[8])


    print("Choose what to edit:")
    print("(Cannot Change) Username")
    print("[1] Email")
    print("[2] Password")
    print("[3] Bio")
    print("[4] Birthday")
    print("[5] Age")
    print("[6] First Name")
    print("[7] Middle Name")
    print("[8] Last Name")
    choice = int(input("Enter choice: "))
    if choice == 1:
        newEmail = input("Enter new Email: ")
        cursor.execute("UPDATE Users SET Email = %s WHERE Username = %s", (newEmail, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 2:
        newPassword = input("Enter new Password: ")
        cursor.execute("UPDATE Users SET Password = %s WHERE Username = %s", (newPassword, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 3:
        newBio = input("Enter new Bio: ")
        cursor.execute("UPDATE Users SET Bio = %s WHERE Username = %s", (newBio, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 4:
        newBirthday = input("Enter new Birthday (YYYY-MM-DD): ")
        cursor.execute("UPDATE Users SET Birthday = %s WHERE Username = %s", (newBirthday, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 5:
        newAge = int(input("Enter new Age: "))
        cursor.execute("UPDATE Users SET Age = %s WHERE Username = %s", (newAge, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 6:
        newFirstName = input("Enter new First Name: ")
        cursor.execute("UPDATE Users SET First_name = %s WHERE Username = %s", (newFirstName, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 7:
        newMiddleName = input("Enter new Middle Name: ")
        cursor.execute("UPDATE Users SET Middle_name = %s WHERE Username = %s", (newMiddleName, userLoggedInUserName))
        mariaDBConnect.commit()
    elif choice == 8:
        newLastName = input("Enter new Last Name: ")
        cursor.execute("UPDATE Users SET Last_name = %s WHERE Username = %s", (newLastName, userLoggedInUserName))
        mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        editUserProfile()

def foodReviewShower(foodReviews):
    if foodReviews == []:
        print("No reviews found.")
    for foodReview in foodReviews:
        print("----------------------------------------------------------------------")
        print("Food ID: ", foodReview[2])
        cursor.execute("SELECT Name FROM Food WHERE Food_id = %s", (foodReview[2],))
        foodName = cursor.fetchone()[0]
        print("Food Name: ", foodName)
        print("Establishment ID: ", foodReview[1])
        print("Review Date: ", foodReview[3])
        print("Comment: ", foodReview[4])
        print("Rating: ", foodReview[5])

def restoReviewShower(restoReviews):
    if restoReviews == []:
        print("No reviews found.")
    for restoReview in restoReviews:
        print("----------------------------------------------------------------------")
        print("Establishment ID: ", restoReview[1])
        cursor.execute("SELECT Name FROM Food_Establishment WHERE Establishment_id = %s", (restoReview[1],))
        restoName = cursor.fetchone()[0]
        print("Establishment Name: ", restoName)
        print("Review Date: ", restoReview[2])
        print("Comment: ", restoReview[3])
        print("Rating: ", restoReview[4])

def editComments():
    print("Edit Comments")
    print("Choose what to edit:")
    print("[1] Edit Comment for Food Item")
    print("[2] Edit Comment for Restaurant")
    choice = int(input("Enter choice: "))
    if choice == 1:
        cursor.execute("SELECT * FROM is_food_reviewed_by WHERE Username = %s", (userLoggedInUserName,))
        foodReviews = cursor.fetchall()
        foodReviewShower(foodReviews)
    
        print("Do you want to edit or delete? ")
        print("[1] Edit")
        print("[2] Delete")
        choice = int(input("Enter choice: "))
        if choice == 1:
            food_id = int(input("Enter Food ID to edit comment: "))
            estab_id = int(input("Enter Establishment ID to edit comment: "))
            newComment = input("Enter new Comment: ")
            cursor.execute("UPDATE is_food_reviewed_by SET Comment = %s WHERE Username = %s AND Food_id = %s AND establishment_id", (newComment, userLoggedInUserName, food_id, estab_id))
            mariaDBConnect.commit()

            newRating = float(input("Enter new Rating: "))
            cursor.execute("UPDATE is_food_reviewed_by SET Rating = %s WHERE Username = %s AND Food_id = %s AND establishment_id", (newRating, userLoggedInUserName, food_id, estab_id))
            mariaDBConnect.commit()
        if choice == 2:
            food_id = int(input("Enter Food ID to delete comment: "))
            estab_id = int(input("Enter Establishment ID to delete comment: "))
            cursor.execute("DELETE FROM is_food_reviewed_by WHERE Username = %s AND Food_id = %s AND establishment_id", (userLoggedInUserName, food_id, estab_id))
            mariaDBConnect.commit()
    elif choice == 2:
        cursor.execute("SELECT * FROM is_resto_reviewed_by WHERE Username = %s", (userLoggedInUserName,))
        restReviews = cursor.fetchall()
        restoReviewShower(restReviews)
        print("Do you want to edit or delete? ")
        print("[1] Edit")
        print("[2] Delete")
        choice = int(input("Enter choice: "))
        if choice == 1:
            establishment_id = int(input("Enter Establishment ID to edit comment: "))
            newComment = input("Enter new Comment: ")
            cursor.execute("UPDATE is_resto_reviewed_by SET Comment = %s WHERE Username = %s AND Establishment_id = %s", (newComment, userLoggedInUserName, establishment_id))
            mariaDBConnect.commit()

            newRating = float(input("Enter new Rating: "))
            cursor.execute("UPDATE is_resto_reviewed_by SET Rating = %s WHERE Username = %s AND Establishment_id = %s", (newRating, userLoggedInUserName, establishment_id))
            mariaDBConnect.commit()
        if choice == 2:
            establishment_id = int(input("Enter Establishment ID to delete comment: "))
            cursor.execute("DELETE FROM is_resto_reviewed_by WHERE Username = %s AND Establishment_id = %s", (userLoggedInUserName, establishment_id))
            mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        editComments()     

def bruteLogout():
    global userLoggedInUserName
    global foodEstabLoggedInID
    userLoggedInUserName = ""
    establishment_id = 0

def menuUser():
    print("\n")
    print("Hi, @", userLoggedInUserName, "!")
    while True:
        menuHeader()
        print("Choose an option:")
        print("[1] View Food Establishments")
        print("[2] View Food Items")
        print("[3] Rate Food Item and Restaurant")
        print("[4] Rate Restaurant only")
        print("[5] Edit Your Comments")
        print("[6] Edit Profile")
        print("[0] Logout")
        choice = int(input("Enter choice: "))
        if choice == 1:
            viewFoodEstabs()
        elif choice == 2:
            viewFoodItem()
        elif choice == 3:
            rateFoodItem()
        elif choice == 4:
            rateResto()
        elif choice == 5:
            editComments()
        elif choice == 6:
            editUserProfile()
        elif choice == 0:
            logout()
        else:
            print("Invalid choice. Please try again.")
            menuUser()
        print("\n")
    

def loginAsUser():
    print("\n")
    print("Login as User")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    cursor.execute("SELECT * FROM Users WHERE Username = %s AND Password = %s", (username, password))
    isPresent = cursor.fetchall()
    if isPresent:
        
        cursor.execute("SELECT username FROM Users WHERE Username = %s AND Password = %s", (username, password))
        global userLoggedInUserName
        userLoggedInUserName = cursor.fetchone()[0] 
        print("Login successful!")
        menuUser()
    else:
        print("Login failed. Please try again.")
        loginAsUser()

def loginAsFoodEstab():
    print("\n")
    print("Login as Food Establishment")
    restoname = input("Enter Restaurant Username: ")
    pin = input("Enter PIN: ")
    print("marker1")
    cursor.execute("SELECT * FROM Food_Establishment WHERE restoname = %s AND pin = %s", (restoname, pin))
    isPresent = cursor.fetchall()
    print("marker2")
    if isPresent:
        cursor.execute("SELECT Establishment_id FROM Food_Establishment WHERE restoname = %s AND pin = %s", (restoname, pin))
        global foodEstabLoggedInID 
        foodEstabLoggedInID = cursor.fetchone()[0] 
        menuFoodEstab()
    else:
        print("Login failed. Please try again.")
        loginAsFoodEstab()

################################
#All about Establishement

def addMeat(food_id):  
    # +----------------+-------------------------------------------------+------+-----+---------+-------+
# | Field          | Type                                            | Null | Key | Default | Extra |
# +----------------+-------------------------------------------------+------+-----+---------+-------+
# | Food_id        | int(3)                                          | NO   | PRI | NULL    |       |
# | Type_of_meat   | enum('Beef','Pork','Poultry','Seafood')         | NO   |     | NULL    |       |
# | Doneness       | enum('Rare','Medium Rare','Medium','Well Done') | YES  |     | NULL    |       |
# | Part_of_animal | enum('Leg','Breast','Thigh','Wing')             | YES  |     | NULL    |       |
# +----------------+-------------------------------------------------+------+-----+---------+-------+
        print("Choose Type of Meat:")
        print("[1] Beef")
        print("[2] Pork")
        print("[3] Poultry")
        print("[4] Seafood")
        choice = int(input("Enter choice: "))
        if choice == 1:
            type_of_meat = "Beef"

        elif choice == 2:
            type_of_meat = "Pork"
        elif choice == 3:
            type_of_meat = "Poultry"
        elif choice == 4:
            type_of_meat = "Seafood"
        else:
            print("Invalid choice. Please try again.") 
        print("Choose Doneness:")
        print("[1] Rare")
        print("[2] Medium Rare")
        print("[3] Medium")
        print("[4] Well Done")
        choice = int(input("Enter choice: "))
        if choice == 1:
            doneness = "Rare"
        elif choice == 2:
            doneness = "Medium Rare"
        elif choice == 3:
            doneness = "Medium"
        elif choice == 4:
            doneness = "Well Done"
        else:
            print("Invalid choice. Please try again.")
        
        print("Choose Part of Animal:")
        print("[1] Leg")
        print("[2] Breast")
        print("[3] Thigh")
        print("[4] Wing")
        choice = int(input("Enter choice: "))
        if choice == 1:
            part_of_animal = "Leg"
        elif choice == 2:
            part_of_animal = "Breast"
        elif choice == 3:
            part_of_animal = "Thigh"
        elif choice == 4:
            part_of_animal = "Wing"
        else:
            print("Invalid choice. Please try again.")
        
        cursor.execute("INSERT INTO Meat (Food_id, Type_of_meat, Doneness, Part_of_animal) VALUES (%s, %s, %s, %s)", (food_id, type_of_meat, doneness, part_of_animal))
        mariaDBConnect.commit()

def addFruit(food_id):
    # +----------------+-----------------------------------+------+-----+---------+-------+
# | Field          | Type                              | Null | Key | Default | Extra |
# +----------------+-----------------------------------+------+-----+---------+-------+
# | Food_id        | int(3)                            | NO   | PRI | NULL    |       |
# | Ripeness       | enum('Raw','Ripe','Overripe')     | YES  |     | NULL    |       |
# | Fruit_category | enum('Citrus','Tropical','Berry') | YES  |     | NULL    |       |
# | Size           | enum('Small','Medium','Large')    | YES  |     | NULL    |       |
# +----------------+-----------------------------------+------+-----+---------+-------+
        print("Choose Ripeness:")
        print("[1] Raw")
        print("[2] Ripe")
        print("[3] Overripe")
        choice = int(input("Enter choice: "))
        if choice == 1:
            ripeness = "Raw"
        elif choice == 2:
            ripeness = "Ripe"
        elif choice == 3:
            ripeness = "Overripe"
        else:
            print("Invalid choice. Please try again.")
        
        print("Choose Fruit Category:")
        print("[1] Citrus")
        print("[2] Tropical")
        print("[3] Berry")
        choice = int(input("Enter choice: "))
        if choice == 1:
            fruit_category = "Citrus"
        elif choice == 2:
            fruit_category = "Tropical"
        elif choice == 3:
            fruit_category = "Berry"
        else:
            print("Invalid choice. Please try again.")

        print("Choose Size:")
        print("[1] Small")
        print("[2] Medium")
        print("[3] Large")
        choice = int(input("Enter choice: "))
        if choice == 1:
            size = "Small"
        elif choice == 2:
            size = "Medium"
        elif choice == 3:
            size = "Large"
        else:
            print("Invalid choice. Please try again.")

        cursor.execute("INSERT INTO Fruit (Food_id, Ripeness, Fruit_category, Size) VALUES (%s, %s, %s, %s)", (food_id, ripeness, fruit_category, size))
        mariaDBConnect.commit()

def addVegetable(food_id):

# +------------------+------------------------------------+------+-----+---------+-------+
# | Field            | Type                               | Null | Key | Default | Extra |
# +------------------+------------------------------------+------+-----+---------+-------+
# | Food_id          | int(3)                             | NO   | PRI | NULL    |       |
# | Vegetable_family | enum('Leafy','Root','Bulb','Stem') | YES  |     | NULL    |       |
# +------------------+------------------------------------+------+-----+---------+-------+
        print("Choose Vegetable Family:")
        print("[1] Leafy")
        print("[2] Root")
        print("[3] Bulb")
        print("[4] Stem")
        choice = int(input("Enter choice: "))
        if choice == 1:
            vegetable_family = "Leafy"
        elif choice == 2:
            vegetable_family = "Root"
        elif choice == 3:
            vegetable_family = "Bulb"
        elif choice == 4:
            vegetable_family = "Stem"
        else:
            print("Invalid choice. Please try again.")
        cursor.execute("INSERT INTO Vegetable (Food_id, Vegetable_family) VALUES (%s, %s)", (food_id, vegetable_family))
        mariaDBConnect.commit()

def addDrink(food_id):
    # +----------------+--------------+------+-----+---------+-------+
# | Field          | Type         | Null | Key | Default | Extra |
# +----------------+--------------+------+-----+---------+-------+
# | Food_id        | int(3)       | NO   | PRI | NULL    |       |
# | Sugar_level    | decimal(2,2) | YES  |     | NULL    |       |
# | Alcohol_level  | decimal(2,2) | YES  |     | NULL    |       |
# | Caffeine_level | decimal(2,2) | YES  |     | NULL    |       |
# | Volume         | decimal(4,2) | YES  |     | NULL    |       |
# +----------------+--------------+------+-----+---------+-------+
        sugar_level = float(input("Enter Sugar Level: "))
        alcohol_level = float(input("Enter Alcohol Level: "))
        caffeine_level = float(input("Enter Caffeine Level: "))
        volume = float(input("Enter Volume: "))
        cursor.execute("INSERT INTO Drink (Food_id, Sugar_level, Alcohol_level, Caffeine_level, Volume) VALUES (%s, %s, %s, %s, %s)", (food_id, sugar_level, alcohol_level, caffeine_level, volume))
        mariaDBConnect.commit()

def addFoodItem():
# +------------------+---------------+------+-----+---------+----------------+
# | Field            | Type          | Null | Key | Default | Extra          |
# +------------------+---------------+------+-----+---------+----------------+
# | Food_id          | int(3)        | NO   | PRI | NULL    | auto_increment |
# | Name             | varchar(60)   | NO   |     | NULL    |                |
# | Description      | varchar(1000) | NO   |     | NULL    |                |
# | Caloric_count    | int(3)        | NO   |     | NULL    |                |
# | Price            | decimal(4,2)  | NO   |     | NULL    |                |
# | Average_rating   | decimal(1,1)  | NO   |     | NULL    |                |
# | Establishment_id | int(3)        | NO   | MUL | NULL    |                |
# +------------------+---------------+------+-----+---------+----------------+
    print("Add Food Item")
    name = input("Enter Name: ")
    description = input("Enter Description: ")
    caloric_count = int(input("Enter Caloric Count: "))
    price = float(input("Enter Price: "))
    average_rating = 0
    print("Food Establishment ID:", foodEstabLoggedInID)
    cursor.execute("INSERT INTO Food (Name, Description, Caloric_count, Price, Average_rating, Establishment_id) VALUES (%s, %s, %s, %s, %s, %s)", (name, description, caloric_count, price, average_rating, foodEstabLoggedInID))
    mariaDBConnect.commit()
    food_id = cursor.lastrowid

# +------------+-------------+------+-----+---------+-------+
# | Field      | Type        | Null | Key | Default | Extra |
# +------------+-------------+------+-----+---------+-------+
# | Food_id    | int(3)      | NO   | PRI | NULL    |       |
# | Ingredient | varchar(50) | NO   | PRI | NULL    |       |
# +------------+-------------+------+-----+---------+-------+

    print("Add Ingredients")
    numberOfIngredients = int(input("Enter number of ingredients: "))
    for i in range(numberOfIngredients):
        ingredient = input("Enter Ingredient: ")
        cursor.execute("INSERT INTO Food_Ingredient (Food_id, Ingredient) VALUES (%s, %s)", (food_id, ingredient))
        mariaDBConnect.commit()
    addType = True
    while addType:
    #Drink, Fruit, Meat, Vegetable
        print("Choose Type:")
        print("[1] Meat")
        print("[2] Fruit")
        print("[3] Vegetable")
        print("[4] Drink")
        choice = int(input("Enter choice: "))
        if choice == 1:
            addMeat(food_id)
        elif choice == 2:
            addFruit(food_id)
        elif choice == 3:
            addVegetable(food_id)
        elif choice == 4:
            addDrink(food_id)
        else:
            print("Invalid choice. Please try again.")

        print("Do you wish to add another type?")
        print("[1] Yes")
        print("[2] No")
        choice = int(input("Enter choice: "))
        if choice == 1:
            addType = True
        elif choice == 2:
            addType = False
        else:
            print("Invalid choice. Please try again.")
            addType = True
    
def viewFoodItemsForEstab(food_etabID):
    cursor.execute("SELECT * FROM Food WHERE Establishment_id = %s", (food_etabID,))
    foodItems = cursor.fetchall()
    foodItemShower(foodItems)

def updateMeat(food_id):
    print("Current Meat Details:")
    cursor.execute("SELECT * FROM Meat WHERE Food_id = %s", (food_id,))
    meatDetails = cursor.fetchall()
    if meatDetails:
        print("Type of Meat:", meatDetails[0][1])
        print("Doneness:", meatDetails[0][2])
        print("Part of Animal:", meatDetails[0][3])
    print("Choose what to update:")
    print("[1] Type of Meat")
    print("[2] Doneness")
    print("[3] Part of Animal")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose Type of Meat:")
        print("[1] Beef")
        print("[2] Pork")
        print("[3] Poultry")
        print("[4] Seafood")
        choice = int(input("Enter choice: "))
        if choice == 1:
            type_of_meat = "Beef"
        elif choice == 2:
            type_of_meat = "Pork"
        elif choice == 3:
            type_of_meat = "Poultry"
        elif choice == 4:
            type_of_meat = "Seafood"
        else:
            print("Invalid choice. Please try again.")
            updateMeat(food_id)
        cursor.execute("UPDATE Meat SET Type_of_meat = %s WHERE Food_id = %s", (type_of_meat, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        print("Choose Doneness:")
        print("[1] Rare")
        print("[2] Medium Rare")
        print("[3] Medium")
        print("[4] Well Done")
        choice = int(input("Enter choice: "))
        if choice == 1:
            doneness = "Rare"
        elif choice == 2:
            doneness = "Medium Rare"
        elif choice == 3:
            doneness = "Medium"
        elif choice == 4:
            doneness = "Well Done"
        else:
            print("Invalid choice. Please try again.")
            updateMeat(food_id)
        cursor.execute("UPDATE Meat SET Doneness = %s WHERE Food_id = %s", (doneness, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        print("Choose Part of Animal:")
        print("[1] Leg")
        print("[2] Breast")
        print("[3] Thigh")
        print("[4] Wing")
        choice = int(input("Enter choice: "))
        if choice == 1:
            part_of_animal = "Leg"
        elif choice == 2:
            part_of_animal = "Breast"
        elif choice == 3:
            part_of_animal = "Thigh"
        elif choice == 4:
            part_of_animal = "Wing"
        else:
            print("Invalid choice. Please try again.")
            updateMeat(food_id)
        cursor.execute("UPDATE Meat SET Part_of_animal = %s WHERE Food_id = %s", (part_of_animal, food_id))
        mariaDBConnect.commit()

def updateFruit(food_id):
    print("Current Fruit Details:")
    cursor.execute("SELECT * FROM Fruit WHERE Food_id = %s", (food_id,))
    fruitDetails = cursor.fetchall()
    if fruitDetails:
        print("Ripeness:", fruitDetails[0][1])
        print("Fruit Category:", fruitDetails[0][2])
        print("Size:", fruitDetails[0][3])
    print("Choose what to update:")
    print("[1] Ripeness")
    print("[2] Fruit Category")
    print("[3] Size")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose Ripeness:")
        print("[1] Raw")
        print("[2] Ripe")
        print("[3] Overripe")
        choice = int(input("Enter choice: "))
        if choice == 1:
            ripeness = "Raw"
        elif choice == 2:
            ripeness = "Ripe"
        elif choice == 3:
            ripeness = "Overripe"
        else:
            print("Invalid choice. Please try again.")
            updateFruit(food_id)
        cursor.execute("UPDATE Fruit SET Ripeness = %s WHERE Food_id = %s", (ripeness, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        print("Choose Fruit Category:")
        print("[1] Citrus")
        print("[2] Tropical")
        print("[3] Berry")
        choice = int(input("Enter choice: "))
        if choice == 1:
            fruit_category = "Citrus"
        elif choice == 2:
            fruit_category = "Tropical"
        elif choice == 3:
            fruit_category = "Berry"
        else:
            print("Invalid choice. Please try again.")
            updateFruit(food_id)
        cursor.execute("UPDATE Fruit SET Fruit_category = %s WHERE Food_id = %s", (fruit_category, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        print("Choose Size:")
        print("[1] Small")
        print("[2] Medium")
        print("[3] Large")
        choice = int(input("Enter choice: "))
        if choice == 1:
            size = "Small"
        elif choice == 2:
            size = "Medium"
        elif choice == 3:
            size = "Large"
        else:
            print("Invalid choice. Please try again.")
            updateFruit(food_id)
        cursor.execute("UPDATE Fruit SET Size = %s WHERE Food_id = %s", (size, food_id))
        mariaDBConnect.commit()
    
def updateVegetable(food_id):
    print("Current Vegetable Details:")
    cursor.execute("SELECT * FROM Vegetable WHERE Food_id = %s", (food_id,))
    vegetableDetails = cursor.fetchall()
    if vegetableDetails:
        print("Vegetable Family:", vegetableDetails[0][1])
    print("Choose what to update:")
    print("[1] Vegetable Family")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose Vegetable Family:")
        print("[1] Leafy")
        print("[2] Root")
        print("[3] Bulb")
        print("[4] Stem")
        choice = int(input("Enter choice: "))
        if choice == 1:
            vegetable_family = "Leafy"
        elif choice == 2:
            vegetable_family = "Root"
        elif choice == 3:
            vegetable_family = "Bulb"
        elif choice == 4:
            vegetable_family = "Stem"
        else:
            print("Invalid choice. Please try again.")
            updateVegetable(food_id)
        cursor.execute("UPDATE Vegetable SET Vegetable_family = %s WHERE Food_id = %s", (vegetable_family, food_id))
        mariaDBConnect.commit()

def updateDrink(food_id):
    print("Current Drink Details:")
    cursor.execute("SELECT * FROM Drink WHERE Food_id = %s", (food_id,))
    drinkDetails = cursor.fetchall()
    if drinkDetails:
        print("Sugar Level:", drinkDetails[0][1])
        print("Alcohol Level:", drinkDetails[0][2])
        print("Caffeine Level:", drinkDetails[0][3])
        print("Volume:", drinkDetails[0][4])
    print("Choose what to update:")
    print("[1] Sugar Level")
    print("[2] Alcohol Level")
    print("[3] Caffeine Level")
    print("[4] Volume")
    choice = int(input("Enter choice: "))
    if choice == 1:
        sugar_level = float(input("Enter Sugar Level: "))
        cursor.execute("UPDATE Drink SET Sugar_level = %s WHERE Food_id = %s", (sugar_level, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        alcohol_level = float(input("Enter Alcohol Level: "))
        cursor.execute("UPDATE Drink SET Alcohol_level = %s WHERE Food_id = %s", (alcohol_level, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        caffeine_level = float(input("Enter Caffeine Level: "))
        cursor.execute("UPDATE Drink SET Caffeine_level = %s WHERE Food_id = %s", (caffeine_level, food_id))
        mariaDBConnect.commit()
    elif choice == 4:
        volume = float(input("Enter Volume: "))
        cursor.execute("UPDATE Drink SET Volume = %s WHERE Food_id = %s", (volume, food_id))
        mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        updateDrink(food_id)
    
def editMeat(food_id):
    print("Edit Meat")
    print("Current Meat Details:")
    cursor.execute("SELECT * FROM Meat WHERE Food_id = %s", (food_id,))
    meatDetails = cursor.fetchall()
    if meatDetails:
        print("Type of Meat:", meatDetails[0][1])
        print("Doneness:", meatDetails[0][2])
        print("Part of Animal:", meatDetails[0][3])
    print("Choose what to update:")
    print("[1] Type of Meat")
    print("[2] Doneness")
    print("[3] Part of Animal")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose Type of Meat:")
        print("[1] Beef")
        print("[2] Pork")
        print("[3] Poultry")
        print("[4] Seafood")
        choice = int(input("Enter choice: "))
        if choice == 1:
            type_of_meat = "Beef"
        elif choice == 2:
            type_of_meat = "Pork"
        elif choice == 3:
            type_of_meat = "Poultry"
        elif choice == 4:
            type_of_meat = "Seafood"
        else:
            print("Invalid choice. Please try again.")
            editMeat(food_id)
        cursor.execute("UPDATE Meat SET Type_of_meat = %s WHERE Food_id = %s", (type_of_meat, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        print("Choose Doneness:")
        print("[1] Rare")
        print("[2] Medium Rare")
        print("[3] Medium")
        print("[4] Well Done")
        choice = int(input("Enter choice: "))
        if choice == 1:
            doneness = "Rare"
        elif choice == 2:
            doneness = "Medium Rare"
        elif choice == 3:
            doneness = "Medium"
        elif choice == 4:
            doneness = "Well Done"
        else:
            print("Invalid choice. Please try again.")
            editMeat(food_id)
        cursor.execute("UPDATE Meat SET Doneness = %s WHERE Food_id = %s", (doneness, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        print("Choose Part of Animal:")
        print("[1] Leg")
        print("[2] Breast")
        print("[3] Thigh")
        print("[4] Wing")
        choice = int(input("Enter choice: "))
        if choice == 1:
            part_of_animal = "Leg"
        elif choice == 2:
            part_of_animal = "Breast"
        elif choice == 3:
            part_of_animal = "Thigh"
        elif choice == 4:
            part_of_animal = "Wing"
        else:
            print("Invalid choice. Please try again.")
            editMeat(food_id)
        cursor.execute("UPDATE Meat SET Part_of_animal = %s WHERE Food_id = %s", (part_of_animal, food_id))
        mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        editMeat(food_id)

def editFruit(food_id):
    print("Edit Fruit")
    print("Current Fruit Details:")
    cursor.execute("SELECT * FROM Fruit WHERE Food_id = %s", (food_id,))
    fruitDetails = cursor.fetchall()
    if fruitDetails:
        print("Ripeness:", fruitDetails[0][1])
        print("Fruit Category:", fruitDetails[0][2])
        print("Size:", fruitDetails[0][3])
    print("Choose what to update:")
    print("[1] Ripeness")
    print("[2] Fruit Category")
    print("[3] Size")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose Ripeness:")
        print("[1] Raw")
        print("[2] Ripe")
        print("[3] Overripe")
        choice = int(input("Enter choice: "))
        if choice == 1:
            ripeness = "Raw"
        elif choice == 2:
            ripeness = "Ripe"
        elif choice == 3:
            ripeness = "Overripe"
        else:
            print("Invalid choice. Please try again.")
            editFruit(food_id)
        cursor.execute("UPDATE Fruit SET Ripeness = %s WHERE Food_id = %s", (ripeness, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        print("Choose Fruit Category:")
        print("[1] Citrus")
        print("[2] Tropical")
        print("[3] Berry")
        choice = int(input("Enter choice: "))
        if choice == 1:
            fruit_category = "Citrus"
        elif choice == 2:
            fruit_category = "Tropical"
        elif choice == 3:
            fruit_category = "Berry"
        else:
            print("Invalid choice. Please try again.")
            editFruit(food_id)
        cursor.execute("UPDATE Fruit SET Fruit_category = %s WHERE Food_id = %s", (fruit_category, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        print("Choose Size:")
        print("[1] Small")
        print("[2] Medium")
        print("[3] Large")
        choice = int(input("Enter choice: "))
        if choice == 1:
            size = "Small"
        elif choice == 2:
            size = "Medium"
        elif choice == 3:
            size = "Large"
        else:
            print("Invalid choice. Please try again.")
            editFruit(food_id)
        cursor.execute("UPDATE Fruit SET Size = %s WHERE Food_id = %s", (size, food_id))

def editVegetable(food_id):
    print("Edit Vegetable")
    print("Current Vegetable Details:")
    cursor.execute("SELECT * FROM Vegetable WHERE Food_id = %s", (food_id,))
    vegetableDetails = cursor.fetchall()
    if vegetableDetails:
        print("Vegetable Family:", vegetableDetails[0][1])
    print("Choose what to update:")
    print("[1] Vegetable Family")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Choose Vegetable Family:")
        print("[1] Leafy")
        print("[2] Root")
        print("[3] Bulb")
        print("[4] Stem")
        choice = int(input("Enter choice: "))
        if choice == 1:
            vegetable_family = "Leafy"
        elif choice == 2:
            vegetable_family = "Root"
        elif choice == 3:
            vegetable_family = "Bulb"
        elif choice == 4:
            vegetable_family = "Stem"
        else:
            print("Invalid choice. Please try again.")
            editVegetable(food_id)
        cursor.execute("UPDATE Vegetable SET Vegetable_family = %s WHERE Food_id = %s", (vegetable_family, food_id))
        mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        editVegetable(food_id)
    
def editDrink(food_id):
    print("Edit Drink")
    print("Current Drink Details:")
    cursor.execute("SELECT * FROM Drink WHERE Food_id = %s", (food_id,))
    drinkDetails = cursor.fetchall()
    if drinkDetails:
        print("Sugar Level:", drinkDetails[0][1])
        print("Alcohol Level:", drinkDetails[0][2])
        print("Caffeine Level:", drinkDetails[0][3])
        print("Volume:", drinkDetails[0][4])
    print("Choose what to update:")
    print("[1] Sugar Level")
    print("[2] Alcohol Level")
    print("[3] Caffeine Level")
    print("[4] Volume")
    choice = int(input("Enter choice: "))
    if choice == 1:
        sugar_level = float(input("Enter Sugar Level: "))
        cursor.execute("UPDATE Drink SET Sugar_level = %s WHERE Food_id = %s", (sugar_level, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        alcohol_level = float(input("Enter Alcohol Level: "))
        cursor.execute("UPDATE Drink SET Alcohol_level = %s WHERE Food_id = %s", (alcohol_level, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        caffeine_level = float(input("Enter Caffeine Level: "))
        cursor.execute("UPDATE Drink SET Caffeine_level = %s WHERE Food_id = %s", (caffeine_level, food_id))
        mariaDBConnect.commit()
    elif choice == 4:
        volume = float(input("Enter Volume: "))
        cursor.execute("UPDATE Drink SET Volume = %s WHERE Food_id = %s", (volume, food_id))
        mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        editDrink(food_id)


    
def updateTypeRelatedDetails(food_id):
    print("Current Type of Food:")
    cursor.execute("SELECT * FROM Meat WHERE Food_id = %s", (food_id,))
    meatDetails = cursor.fetchall()
    if meatDetails:
        print("Meat")
    cursor.execute("SELECT * FROM Fruit WHERE Food_id = %s", (food_id,))
    fruitDetails = cursor.fetchall()
    if fruitDetails:
        print("Fruit")
    cursor.execute("SELECT * FROM Vegetable WHERE Food_id = %s", (food_id,))
    vegetableDetails = cursor.fetchall()
    if vegetableDetails:
        print("Vegetable")
    cursor.execute("SELECT * FROM Drink WHERE Food_id = %s", (food_id,))
    drinkDetails = cursor.fetchall()
    if drinkDetails:
        print("Drink")
    print("Choose what to update:")
    print("[1] Meat")
    print("[2] Fruit")
    print("[3] Vegetable")
    print("[4] Drink")
    choice = int(input("Enter choice: "))
    if choice == 1:
        editMeat(food_id)
    elif choice == 2:
        editFruit(food_id)
    elif choice == 3:
        editVegetable(food_id)
    elif choice == 4:
        editDrink(food_id)
    else:
        print("Invalid choice. Please try again.")
        updateTypeRelatedDetails(food_id)
    
    print("Do you want to edit again?")
    print("[1] Yes")
    print("[2] No")
    if editagain == 1:
        updateTypeRelatedDetails(food_id)
       

        


def updateFoodItem():
    print("Update Food Item")
    viewFoodItemsForEstab(foodEstabLoggedInID)
    food_id = int(input("Enter Food ID to update: "))
    print("Choose what to update:")
    print("[1] Name")
    print("[2] Description")
    print("[3] Caloric Count")
    print("[4] Price")
    print("[5] Type Related Details")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        name = input("Enter Name: ")
        cursor.execute("UPDATE Food SET Name = %s WHERE Food_id = %s", (name, food_id))
        mariaDBConnect.commit()
    elif choice == 2:
        description = input("Enter Description: ")
        cursor.execute("UPDATE Food SET Description = %s WHERE Food_id = %s", (description, food_id))
        mariaDBConnect.commit()
    elif choice == 3:
        caloric_count = int(input("Enter Caloric Count: "))
        cursor.execute("UPDATE Food SET Caloric_count = %s WHERE Food_id = %s", (caloric_count, food_id))
        mariaDBConnect.commit()
    elif choice == 4:
        price = float(input("Enter Price: "))
        cursor.execute("UPDATE Food SET Price = %s WHERE Food_id = %s", (price, food_id))
        mariaDBConnect.commit()
    elif choice == 5:
        updateTypeRelatedDetails(food_id)
    else:
        print("Invalid choice. Please try again.")
        updateFoodItem()
    
 #ITO YUNG EDITEDDDD
def deleteFoodItemAllfoodEstabLoggedInID():
    cursor.execute("SELECT * FROM Food WHERE Establishment_id = %s", (foodEstabLoggedInID,))
    foodItems = cursor.fetchall()
    for foodItem in foodItems:
        if foodItem:
            food_id = foodItem[0]
            cursor.execute("DELETE FROM Meat WHERE Food_id = %s", (food_id,))
            mariaDBConnect.commit()
            cursor.execute("DELETE FROM Fruit WHERE Food_id = %s", (food_id,))
            mariaDBConnect.commit()
            cursor.execute("DELETE FROM Vegetable WHERE Food_id = %s", (food_id,))
            mariaDBConnect.commit()
            cursor.execute("DELETE FROM Drink WHERE Food_id = %s", (food_id,))
            mariaDBConnect.commit()
            cursor.execute("DELETE FROM Food_Ingredient WHERE Food_id = %s", (food_id,))
            mariaDBConnect.commit()

            cursor.execute("DELETE From is_food_reviewed_by WHERE Food_id = %s", (food_id,))
            mariaDBConnect.commit()
            cursor.execute("DELETE FROM Food WHERE Food_id = %s", (food_id,))
          
            mariaDBConnect.commit()
    


def deleteFoodItem():

    cursor.execute("SELECT * FROM Food WHERE Establishment_id = %s", (foodEstabLoggedInID,))
    foodItems = cursor.fetchall()
    if foodItems == []:
        print("No food items to delete.")
        return
    
    print("Delete Food Item")
    viewFoodItemsForEstab(foodEstabLoggedInID)

    food_id = int(input("Enter Food ID to delete: "))
    cursor.execute("DELETE FROM Meat WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()
    cursor.execute("DELETE FROM Fruit WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()
    cursor.execute("DELETE FROM Vegetable WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()
    cursor.execute("DELETE FROM Drink WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()
    cursor.execute("DELETE FROM Food_Ingredient WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()

    cursor.execute("DELETE From is_food_reviewed_by WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()
    
    cursor.execute("DELETE FROM Food WHERE Food_id = %s", (food_id,))
    mariaDBConnect.commit()

    print("Food Item deleted successfully!")
    
def editRestaurantProfile():
    print("Edit Restaurant Profile")
    print("Current Restaurant Profile:")
    cursor.execute("SELECT * FROM Food_Establishment WHERE Establishment_id = %s", (foodEstabLoggedInID,))
    foodEstabDetails = cursor.fetchall()
    if foodEstabDetails:
        print("Name:", foodEstabDetails[0][2])
        print("Description:", foodEstabDetails[0][3])
        print("Capacity:", foodEstabDetails[0][4])
        print("Type:", foodEstabDetails[0][5])

        print("Branch Locations")
        cursor.execute("SELECT * FROM Food_Establishment_Location WHERE Establishment_id = %s", (foodEstabLoggedInID,))
        locations = cursor.fetchall()
        for location in locations:
            print(location[1])
        

        cursor.execute("SELECT * FROM Food_Establishment_Social_Media_Link WHERE Establishment_id = %s", (foodEstabLoggedInID,))
        social_media_links = cursor.fetchall()
        print("Social Media Links:")
        for social_media_link in social_media_links:
            print(social_media_link[1])
        cursor.execute("SELECT * FROM Food_Establishment_Contact WHERE Establishment_id = %s", (foodEstabLoggedInID,))
        contact_numbers = cursor.fetchall()
        print("Contact Numbers:")
        for contact_number in contact_numbers:
            print(contact_number[1])

    print("Choose what to update:")
    print("[1] Name")
    print("[2] Description")
    print("[3] Capacity")
    print("[4] Type")
    print("[5] Social Media Links")
    print("[6] Contact Numbers")
    print("[7] Location")

    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        cursor.execute("UPDATE Food_Establishment SET Name = %s WHERE Establishment_id = %s", (name, foodEstabLoggedInID))
        mariaDBConnect.commit()
    elif choice == 2:
        description = input("Enter Description: ")
        cursor.execute("UPDATE Food_Establishment SET Description = %s WHERE Establishment_id = %s", (description, foodEstabLoggedInID))
        mariaDBConnect.commit()
    elif choice == 3:
        capacity = int(input("Enter Capacity: "))
        cursor.execute("UPDATE Food_Establishment SET Capacity = %s WHERE Establishment_id = %s", (capacity, foodEstabLoggedInID))
        mariaDBConnect.commit()
    elif choice == 4:
        print("Choose Type:")
        print("[1] Food Truck")
        print("[2] Fine Dining")
        print("[3] Cafe")
        print("[4] Fast Food")
        choice = int(input("Enter choice: "))
        if choice == 1:
            type = "Food Truck"
        elif choice == 2:
            type = "Fine Dining"
        elif choice == 3:
            type = "Cafe"
        elif choice == 4:
            type = "Fast Food"
        else:
            print("Invalid choice. Please try again.")
            editRestaurantProfile()
        cursor.execute("UPDATE Food_Establishment SET Type = %s WHERE Establishment_id = %s", (type, foodEstabLoggedInID))
        mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
    
    editAgain = input("Do you want to edit again?")
    print("[1] Yes")
    print("[2] No")
    if editAgain == 1:
        editRestaurantProfile()

def deleteRestaurantProfile():
    print("Delete Restaurant Profile")
    print("Are you sure you want to delete your restaurant profile?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        deleteFoodItemAllfoodEstabLoggedInID()
        cursor.execute("DELETE from FOOD_ESTABLISHMENT_CONTACT where Establishment_id = %s", (foodEstabLoggedInID,))    
        mariaDBConnect.commit()
        cursor.execute("DELETE from FOOD_ESTABLISHMENT_LOCATION where Establishment_id = %s", (foodEstabLoggedInID,))
        mariaDBConnect.commit()
        cursor.execute("DELETE from food_establishment_social_media_link where Establishment_id = %s", (foodEstabLoggedInID,))
        mariaDBConnect.commit()

        cursor.execute("DELETE from is_resto_reviewed_by where Establishment_id = %s", (foodEstabLoggedInID,))
        mariaDBConnect.commit()

        cursor.execute("DELETE FROM Food_Establishment WHERE Establishment_id = %s", (foodEstabLoggedInID,))
        mariaDBConnect.commit()
        print("Restaurant Profile deleted successfully!")
        login()
    elif choice == 2:
        print("Restaurant Profile not deleted.")

def logout():
    global userLoggedInUserName
    global foodEstabLoggedInID
    print("Logout")
    print("Are you sure you want to logout?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Logout successful!")
        userLoggedInUserName = ""
        foodEstabLoggedInID = 0
        login()
    else:
        print("Invalid choice. Please try again.")
        logout()

def menuHeader():

    smallHorizontalLine()
    print("╔╦╗┌─┐┌┐┌┬ ┬")
    print("║║║├┤ ││││ │")
    print("╩ ╩└─┘┘└┘└─┘")
    smallHorizontalLine()

def menuFoodEstab():
    while True:
        menuHeader()
        print("Menu for Food Establishment")
        print("[1] Add Food Item")
        print("[2] Update Food Item")
        print("[3] Delete Food Item")
        print("[4] View Food Items")
        print("[5] View Reviews")
        print("[6] Edit Restaurant Profile")
        print("[7] Delete Restaurant Profile")
        print("[0] Log Out")
        choice = int(input("Enter choice: "))
        if choice == 1:
            addFoodItem()
        elif choice == 2:
            updateFoodItem()
        elif choice == 3:
            deleteFoodItem()
        elif choice == 4:
            viewFoodItemsForEstab(foodEstabLoggedInID)
        elif choice == 5:
            viewReviewsResto(foodEstabLoggedInID)
        elif choice == 6:
            editRestaurantProfile()
        elif choice == 7:
            deleteRestaurantProfile()
        elif choice == 0:
            logout()
        else:
            print("Invalid choice. Please try again.")
            menuFoodEstab()
        print("\n")



    
################################


def login():
    horizontalLine()
    print("LOGIN to ELBI FOOD REVIEW")
    print("[1] Login as User")
    print("[2] Login as Food Establishment")
    print("[3] Sign Up Instead")
    print("[4] Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        loginAsUser()
    elif choice == 2:
        loginAsFoodEstab()
    elif choice == 3:
        signUp()
    elif choice == 4:
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        login()

def header():
  header_print = '''
  ┏┓┓┓ •  ┏┓     ┓  ┳┓    •
  ┣ ┃┣┓┓  ┣ ┏┓┏┓┏┫  ┣┫┏┓┓┏┓┏┓┓┏┏
  ┗┛┗┗┛┗  ┻ ┗┛┗┛┗┻  ┛┗┗ ┗┛┗┗ ┗┻┛
  '''
  print(header_print)



def configTesting():
    horizontalLine()
    print("CONFIGURE YOURSELF AS A TESTER")
    horizontalLine()
    print("Is this your first time using the system?")
    print("[1] Yes")
    print("[2] No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        with open('database_initializer.sql', 'r') as file:
            sql_script = file.read()

        # Split the script into individual statements
        sql_statements = sql_script.split(';')

        # Execute each statement
        for statement in sql_statements:
            if statement.strip():
                cursor.execute(statement)
        mariaDBConnect.commit()
            
    elif choice == 2:
        print("Do you want to clear all data?")
        print("[1] Yes")
        print("[2] No")
        choice = int(input("Enter choice: "))
        if choice == 1:
            with open('database_resetter.sql', 'r') as file:
                sql_script = file.read()
        
            sql_statements = sql_script.split(';')

            for statement in sql_statements:
                if statement.strip():
                    cursor.execute(statement)
            mariaDBConnect.commit()
    else:
        print("Invalid choice. Please try again.")
        configTesting()
    

        
def main():
    try:
        configTesting()
        header()
        login()
    except Exception as e:
        print("\n")
        horizontalLine()
        print("An error occurred:", e)
        horizontalLine()
        bruteLogout()
        print("\n")
        print("Do you want to exit?")
        print("[1] Yes")
        print("[2] No (Restart the Application)")
        choice = int(input("Enter choice: "))

        if choice == 2:
            print("\n")
            print("Restarting the Application...")
            print("\n")
            main()
        


        
    finally:
        cursor.close()
        print("Server closed.")
        sys.exit()
  


if __name__ == "__main__":

    main()
