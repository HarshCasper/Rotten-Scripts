from pg import DB, InternalError


class Database:
    def __init__(self):
        status = False
        maximumRetry = 3
        count = 0
        self.database = None
        while count < maximumRetry and self.database is None:
            try:
                count += 1
                self.database = DB(
                    dbname="dbName"
                    host="host"
                    port="port"
                    user="username"
                    passwd="password"
                )
                if self.database is not None:
                    status = True
                    break
            except InternalError:
                print("Trying to reconnect with the database")
            except Exception as err:
                print(err)
        if status:
            print("Connected with the database successfully.")
        else:
            print("Connection with the database was Unsucessful!")

