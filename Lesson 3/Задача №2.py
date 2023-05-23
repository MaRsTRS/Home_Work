
def user_data(name, surname, year, city, mail, phone):
    return ' , '.join([name, surname, year, city, mail, phone])

result = user_data(name='Name', surname='Surname', year='2023',
                   city='Unknown_CIT', mail='ff@jt.net', phone='+78889471232')
print(result)
