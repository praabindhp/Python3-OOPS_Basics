class person:

    # name = ['Kevin', 'Henry']
    name = 'Praabindh'
    age = 20
    # name = [24, 25]

    def __init__(self, name = 'Praabindh', age = 24):
        self.name = name
        self.age = age

    def show_name(self):
        # print('Name : ' + self.name)
        # print('Age : ' + self.age)
        print('Name : %s \nAge : %s' % (self.name, self.age))

# p = person(person.name, person.age)
# p = person(name = 'Sam', age = 25)
p = person(name = 'Sam')
p = person(age = 20)
p.show_name()