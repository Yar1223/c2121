import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()


pytania = input("1(вхід) чи 2(реєстрація): ")
print(pytania)
if pytania == "1":
    user = input("Login : ")
    cur.execute(f"SELECT rowid, name FROM LOGINS WHERE name='{user}'")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        print("Такого логіну нема!")
    else:
        passw = input("Password : ")
        q = cur.execute(f"SELECT rowid, name FROM LOGINS WHERE name='{passw}'")
        connection.commit()
        if len(res) == 0:
            print("Такого паролю нема!")
        else:
            print("Ви війшли в гугл!")

if pytania == "2":
    user = input("Login : ")
    cur.execute(f"SELECT rowid, name FROM LOGINS WHERE name='{user}'")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 1:
        print("Такий логін вже є!")
    else:
        passw = input("Password : ")
        cur.execute(f"INSERT INTO LOGINS (name, password) VALUES ('{user}', '{passw}');")
        connection.commit()




#===== CREATE =======
#cur.execute("CREATE TABLE LOGINS (name TEXT, password TEXT);")
#connection.commit()

#cur.execute("CREATE TABLE USERS (name TEXT);")
#===== INSERT =========

# user = input("Username  : ")
# passw = input("Password : ")
# cur.execute(f"INSERT INTO LOGINS (name, password) VALUES ('{user}', '{passw}');")
# connection.commit()

#user = input("Username: ")
#cur.execute(f"INSERT INTO USERS (name) VALUES ('{user}', '{passw}');")

#connection.commit()
#===== SELECT =======
#user = input("Username  : ")
# cur.execute(f"SELECT rowid, name FROM USERS WHERE name='{user}'")
#cur.execute(f"SELECT rowid, name FROM USERS")
#connection.commit()
#res = cur.fetchall()
#print(res)
# if len(res) == 0:
#     print("User not found!")
# else:
#     print(res[0][1])
# ===== UPDATE ======
# cur.execute(f"UPDATE USERS SET name='Katerina' WHERE rowid=3")
# connection.commit()
#==== DELETE ========
# cur.execute(f"DELETE FROM USERS WHERE rowid=1")
# connection.commit()

connection.close()