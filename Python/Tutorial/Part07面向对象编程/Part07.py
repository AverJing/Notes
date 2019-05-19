#Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

aj = Student('Aver Jing', 92)
lisa = Student('Lisa', 88)

aj.age=18

print(aj.age)
lisa.print_score()
'''


'''
class Student(object):
    def __init__(self, name):
        self.__name = name
    name = "Student"#类属性

lisa = Student('Lisa')
lisa.name = 'aaaa'#实例属性
print(lisa.name)

print(Student.name)
'''