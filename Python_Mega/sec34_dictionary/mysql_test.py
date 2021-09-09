import mysql.connector


conn = mysql.connector.Connect(
    username="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = conn.cursor()
user_input = input('Enter something: ')

select_query = cursor.execute(
    "SELECT Definition "
    "FROM Dictionary "
    "WHERE Expression = '%s';" % user_input
)

results = cursor.fetchall()

# print all columns  (in case SELECT *)
print(results)

# iterate over all tuple items, and return them as string
if results:
    for item in results:
        print(" ".join(item))
else:
    print('No word found')

# or we could filter our query of course..


# for exp in results:
#     print("".join(exp))







