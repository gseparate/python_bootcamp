import random
def turrets_generator():
    actions = ['shoot', 'search', 'talk']
    person_traits = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']
    person_traits_values = [0 for i in person_traits]
    for i in range(0, len(person_traits_values)):
        person_traits_values[i] = random.randint(0, 100-sum(person_traits_values)) if i != len(person_traits_values) - 1 else 100-sum(person_traits_values)
    while True:
        yield type('Turret', (), {i : lambda x = i: print(x) for i in actions} | dict(zip(person_traits, person_traits_values)))

l = [next(turrets_generator()) for i in range(0,10)]
for i in range(0,10):
    print(l[i].__name__)
    print(l[i].conscientiousness, l[i].neuroticism, l[i].openness, l[i].extraversion, l[i].agreeableness)
