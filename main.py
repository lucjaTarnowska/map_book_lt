users: list = [

    {"name": "Julia", "surname": "Gotowiec", "posts": 1500, },
    {"name": "Hubert", "surname": "Sybilski", "posts": 123456, },
    {"name": "Adrian", "surname": "Dobrzański", "posts": 3, }
]

print("informacje o twoich znajomych: ")
for user in users:
    print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')