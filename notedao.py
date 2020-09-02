
import dbaccess

def add_note(text, userid):

    if text == '':
        print('Blank note')
        return 

    db = dbaccess.Connection()
    if db != None: 
        try:
            connection = db.get_connection()
            query = "insert into notes(text, user_id) values(%s, %s)"
            
            cursor = connection.cursor()
            rows = cursor.execute(query, (text, userid))
            print('Added rows ', rows)
            connection.commit()

        except Exception as e:
            print(e)
            db.close_connection()
        db.close_connection()
        

def get_note_by_userid(userid):
    
    if userid == None:
        print("userid is None")
        return

    query = ("select note_id, text from notes where user_id = %s")
    db = dbaccess.Connection()
    connection = db.get_connection()

    cursor = connection.cursor()
    cursor.execute(query, (userid,))

    for (note_id, text) in cursor:
        print("{} {} ".format(note_id, text))
    cursor.close()
    db.close_connection()

def get_all_notes():

    query = ('select note_id, text, user_id from notes')
    db = dbaccess.Connection()
    connection = db.get_connection()
    
    cursor = connection.cursor()
    cursor.execute(query)

    for (note_id, text, user_id) in cursor:
        print("{}, {} by {}".format(note_id, text, user_id))

    cursor.close()
    connection.close()

