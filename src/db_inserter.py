
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
  host=CONFIG["host"],
  user=CONFIG["user"],
  password=CONFIG["password"],
  database=CONFIG["database"]
)
my_cursor = mydb.cursor()

def insert_data():
    # Example INSERT query
    query1 = "INSERT INTO human_detections (id, Timestamp, Total_customers, Product, Activities, Length_time, Gender, Age, Bought, Camera_id, Store_place, Attractive_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values1 = (10, date.today(), 2, 'Red Shirt', 'Touch', 30, 'Male', 30, False, 1, "zone 1 - Hanging Facility", 70)
    query2 = "INSERT INTO human_detections (id, Timestamp, Total_customers, Product, Activities, Length_time, Gender, Age, Bought, Camera_id, Store_place, Attractive_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values2 = (11, date.today(), 2, 'Red Shirt', 'Touch', 30, 'Female', 29, False, 2, "zone 1 - Hanging Facility", 85)
   
    # Execute the INSERT query with the provided values
    my_cursor.execute(query1, values1)
    my_cursor.execute(query2, values2)


    # Commit the changes to the database
    mydb.commit()

    # Close the cursor and connection
    my_cursor.close()
    mydb.close()