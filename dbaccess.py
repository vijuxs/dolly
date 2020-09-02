
import mysql.connector

class Connection:
    
    def __init__(self):
        self.connection = None

    
    def get_connection(self):
        
        if self.connection == None:
            try:
                self.connection = mysql.connector.connect(
                    host = "localhost",
                    user = "username",
                    password = "password",
                    database = "desk_assist"
                    )
                if self.connection.is_connected():
                    print("Connected successfully!!")
                else:
                    print("Error connecting")

                return self.connection

            except Exception:
                print("Error connecting to the database")
        else:
            return self.connection
    
    def close_connection(self):
        print(self.connection)
        
        if self.connection != None:
            self.connection.close()
            print("Connection closed")
        else:
            print("Connection object None")


