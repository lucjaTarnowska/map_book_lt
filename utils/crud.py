def read_friends(users: list) -> None:
    print("informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

def add_user(lista: list) -> None:
    imie = input("podaj imie: ")
    nazwisko = input("podaj nazwisko: ")
    liczba_postow = int(input("podaj liczbe postów użytkownika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow, }
    lista.append(new_user)

def search_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            print(user)

def remove_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            users.remove(user)

