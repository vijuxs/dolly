
import dbaccess

def add_user(userid, username, password):

    db = dbaccess.Connection()
    try:
        connection = db.get_connection()
        if connection.is_connected():

            query = 'insert into users(user_id, username, password) values (%s, %s, %s)'
            cursor = connection.cursor()
            cursor.execute(query, (userid, username, password))
            cursor.close()
            connection.commit()
            db.close_connection()
        else:
            print("Could not connect")
    except Exception as e:
        print(e)
        db.close_connection()
        
def get_all_users():
    
    db = dbaccess.Connection()
    try:
        connection = db.get_connection()

        if connection.is_connected():
            query = 'select user_id, username, password from users'

            cursor = connection.cursor()
            cursor.execute(query)

            for (user_id, username, password) in cursor:
                print('{} {} {}'.format(user_id, username, password))
            cursor.close()
        else:
            print("Could not connect")
    except Exception as e:
        print(e)
        db.close_connection()

