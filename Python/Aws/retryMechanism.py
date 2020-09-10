"""
The following code sample demonstrates how to use the pg module to connect to a PostgreSQL database. 
Replace USERNAME with the PostgreSQL database username, PASSWORD with the database user's password, 
and DBNAME with the database name.
"""

import pg #pg module is used to connect to PostgreSQL.


class Database:
    def __init__(self):
        status = False
        maximumRetry = 3
        count = 0
        self.conn = None
        while count < maximumRetry and self.conn is None:
            try:
                count += 1
                self.conn = pg.DB(
                    host="localhost",
                    user="USERNAME",
                    passwd="PASSWORD",
                    dbname="DBNAME",
                )
                if self.conn is not None:
                    status = True
                    break
            except pg.InternalError:
                print("Trying to reconnect with the database")
            except Exception as err:
                print(err)
        if status:
            print("Connected with the database successfully.")
            result = self.conn.query("SELECT fname, lname FROM employee")

            for firstname, lastname in result.getresult():
                print(firstname, lastname)

            self.conn.close()
        else:
            print("Connection with the database was Unsucessful!")

"""
This example creates a Connection object that opens the PostgreSQL database using the specified parameters. 
Once you have a Connection object associated with the database,you can query the database directly using raw 
SQL statements (in this case, a SELECT query on a table named employee)
"""
