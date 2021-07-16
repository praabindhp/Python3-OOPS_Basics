class person:

    # name = ['Kevin', 'Henry']
    name = 'Praabindh'
    age = 20
    # name = [24, 25]

    # Class Variable
    gender = 'Male'

    def __init__(self, name = 'Praabindh', age = 24):
        self.name = name
        self.age = age
        self.Person_List = []

    def show_name(self):
        # print('Name : ' + self.name)
        # print('Age : ' + self.age)
        print('Name : %s \nAge : %s' % (self.name, self.age))

    def add_value(self, value):
        self.Person_List.append(value)

# p = person(person.name, person.age)
# p = person(name = 'Sam', age = 25)
# p.show_name()

p = person(name = 'Sam')
p = person(age = 20)

p.show_name()
p.add_value('Mark')

print(p.Person_List)