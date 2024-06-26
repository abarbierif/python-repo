class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age
    
    def change_gender(self, new_gender):
        self.gender = new_gender

    def dog_age(self):
        dog_age = 0
        if self.age <= 1:
            dog_age = 15*self.age
        elif self.age <= 2:
            dog_age = 15 + 9*(self.age-1)
        else:
            dog_age = 15 + 9 + 5*(self.age-2)

        return dog_age

if __name__ == '__main__':
    p = Person(input('name: '), float(input('age: ')), input('gender: '))
    print(f"dog age: {p.dog_age()}")
    print('name:', p.name)
    p.change_name(input('enter new name: '))
    print('new name:', p.name)
    print('age:', p.age)
    p.change_age(input('enter new age: '))
    print('new age:', p.age)
    print('gender:', p.gender)
    p.change_gender(input('enter new gender: '))
    print('new gender:', p.gender)

