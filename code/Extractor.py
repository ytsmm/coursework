import csv
from mysql.connector import connect, Error

"""
Функция производит выборку необходимых для работы данных из базы данных
@:param type: {str}, user - имя пользователя
@:param type: {str}, pswd - пароль пользователя
@:param type: {str}, dbName - название базы данных пользователя
"""
def ExportDB(user='', pswd='', dbName=''):
    try:
        with connect(
                host="localhost",
                user=user,
                password=pswd,
                database=dbName,
        ) as connection:
            try:
                filename = 'Extractor.sql'
                with open(filename, 'r', encoding='utf-8') as file:
                    data = file.read()
                    with connection.cursor() as cursor:
                        cursor.execute(data, multi=True)
                        result = cursor.fetchall()
                with open("articles.csv", 'w', encoding='utf-8', newline='') as resultFile:
                    wr = csv.writer(resultFile, delimiter=';')
                    wr.writerows(result)
                    print("The data is extracted successfully. Close the window.")
            except Error as e:
                print(e)
    except Error as e:
        print(e)

