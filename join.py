import mysql.connector
host="localhost",
username="root",
password="",
database="join"

mydb = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)
# Creating a cursor object
mycursor = mydb.cursor()

mycursor.execute("""
   CREATE TABLE IF NOT EXISTS EX (
      ID_NUMBER INT(10),
      USER_NAME VARCHAR (20),
      PRODUCTS_NAME VARCHAR
);
""")


'''sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)'''



















'''import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        user_data =data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]

        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        print(f"username:{username} \n  country:{country}")
        pass
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main() '''
