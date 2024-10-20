import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    password="Bedswamp25!",
    database="Fitness_db"
)



mycursor = mydb.cursor()



def add_member():
    sql = "INSERT INTO Members (first_name, last_name) VALUES (%s, %s)"
    val = ("John", "Doe")
    
    mycursor.execute(sql, val) 

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

add_member()


def add_workout_session():
    sql = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)"
    val = (3, '2024-05-01', '10:00AM', 'Boxing')
    mycursor.execute(sql, val) 

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

add_workout_session()



def update_member_age():
    sql = "UPDATE Members SET age = %s WHERE id = %s"

    val = (27, 1)

    mycursor.execute(sql, val) 

    mydb.commit()

    print(mycursor.rowcount, "record(s) updated.")


update_member_age()



def delete_workout_session():
    sql = "DELETE FROM WorkoutSessions WHERE member_id = %s"
    val = (1,)
    mycursor.execute(sql, val) 

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


delete_workout_session()




def get_members_in_age_range(start_age, end_age):
        sql = "SELECT * FROM Members WHERE age BETWEEN %s and %s"
        # val = (3, '2024-05-01', '10:00AM', 'Boxing')
        mycursor.execute(sql, (start_age, end_age)) 
        members = mycursor.fetchall()
        print(members)


get_members_in_age_range(20, 45)
