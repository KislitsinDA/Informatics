friends = {}


def add_friends(name_of_person, list_of_friends):
    friends[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in friends.get(name_of_person1):
        return True
    return False


def print_friends(name_of_person):
    friends.get(name_of_person).sort()
    return friends.get(name_of_person)


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))