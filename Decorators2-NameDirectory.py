
def person_lister(f):
    def inner(people):
        sorted_list = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in sorted_list]
    return inner


