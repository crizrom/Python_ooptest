#Classes & objects

class Name:
    pass

victor = Name()
maria = Name()

#object.attribute = value

victor.age = 30
victor.sex = 'male'
victor.country = 'Bolivia'

maria.age = 25
maria.sex = 'female'
maria.country = 'Mexico'

print("Victor's country is " + victor.country)
print("Maria's age is " + str(maria.age))
print("Victor's sex is " + victor.sex)
print("Maria's country is " + maria.country)