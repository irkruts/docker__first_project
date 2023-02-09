from faker import Faker

faker = Faker()


def generate_some_mes():
    list_of_users = []
    bl = True
    while bl:
        list_of_users.append(faker.name())
        if len(list_of_users) == 10:
            bl = False
    return list_of_users
