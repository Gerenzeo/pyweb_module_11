from datetime import datetime, timedelta

contacts = [
    {"id":1,"first_name":"Alex","last_name":"Mrorn","birthday":"1994-09-11","email":"alex1994@example.com","phone":"380501884433","favorite":True,"created_at":"2023-09-10T11:52:23.423764","updated_at":"2023-09-10T11:52:23.423764"},
    {"id":4,"first_name":"Alex","last_name":"Mrorn","birthday":"1994-09-10","email":"alex1994@example.com","phone":"380501884433","favorite":True,"created_at":"2023-09-10T11:52:23.423764","updated_at":"2023-09-10T11:52:23.423764"},
    {"id":5,"first_name":"Test","last_name":"Test","birthday":"2023-09-10","email":"user@example.com","phone":"380501884455","favorite":True,"created_at":"2023-09-10T12:10:04.659684","updated_at":"2023-09-10T12:10:04.659684"},
    {"id":6,"first_name":"Martin","last_name":"Fitzgerald","birthday":"1997-06-16","email":"Martin.Fitzgerald@mail.com","phone":"380633421479","favorite":False,"created_at":"2023-09-10T15:56:18.025295","updated_at":"2023-09-10T15:56:18.025300"},
    {"id":7,"first_name":"Maria","last_name":"Martin","birthday":"1999-05-07","email":"Maria.Martin@mail.com","phone":"380683321145","favorite":False,"created_at":"2023-09-10T15:56:18.026840","updated_at":"2023-09-10T15:56:18.026843"},{"id":8,"first_name":"Jessica","last_name":"Aguirre","birthday":"2000-12-14","email":"Jessica.Aguirre@gmail.com","phone":"380506724765","favorite":True,"created_at":"2023-09-10T15:56:18.027226","updated_at":"2023-09-10T15:56:18.027228"},{"id":9,"first_name":"Eric","last_name":"King","birthday":"1998-06-23","email":"Eric.King@school.com","phone":"380985558753","favorite":False,"created_at":"2023-09-10T15:56:18.027600","updated_at":"2023-09-10T15:56:18.027601"},{"id":10,"first_name":"Benjamin","last_name":"Jackson","birthday":"1997-09-20","email":"Benjamin.Jackson@school.com","phone":"380987306592","favorite":True,"created_at":"2023-09-10T15:56:18.027965","updated_at":"2023-09-10T15:56:18.027966"}]

today = datetime.now()
days = today


for _ in range(7):
    print(days.date())
    
    for contact in contacts:
        birthday = datetime.strptime(contact['birthday'], '%Y-%m-%d').date()

        if birthday.day == days.day and birthday.month == days.month:
            print(contact)

    days += timedelta(1)
    
