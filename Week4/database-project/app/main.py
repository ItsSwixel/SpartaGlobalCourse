import mysql.connector

print("Welcome to Python & DB App")

try:
    with mysql.connector.connect(host="localhost", user="root", password="my_secret_password", database="test_from_python_db") as conn_var:
        print(conn_var)
        cursor = conn_var.cursor()
        # cursor.execute("CREATE DATABASE test_from_python_db;")
        # cursor.execute("SHOW DATABASES;")
        # cursor.execute("SHOW TABLES;")

        # command = "CREATE TABLE app_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30), score INT);"
        name_val = "Kali"
        score_val = 10
        command = f"INSERT INTO app_table (name, score) VALUES ('{name_val}', {score_val});"
        cursor.execute(command)
        conn_var.commit()
        command = "SELECT * FROM app_table;"
        print(command)
        cursor.execute(command)
        rows = cursor.fetchall()
        for item in rows:
            print(item[0], item[1], item[2])
except Exception as e:
    raise
