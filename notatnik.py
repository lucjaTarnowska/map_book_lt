import psycopg2 as ps


db_params = ps.connect(
    database="map_book",
    user="postgres",
    password="geoinformatyka",
    host="localhost",
    port="5432"
)

cursor = db_params.cursor()
sql_show_users = "SELECT * FROM public.users"
cursor.execute(sql_show_users)
query_result = cursor.fetchall()
for row in query_result:
	print(row[0])
	print(row[1])
	print(row[2])
	print(row[3])


# INSERT INTO public.users(
#   name, surname, posts, location, wspolrzedne)
#   VALUES ( 'Karol', 'Makowski', '10', 'Warszawa', 'SRID=4326;POINT(52.21 21.00)');