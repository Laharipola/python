class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name},{self.age}'
class Students(person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        res=super().__str__()
        return f'{res},{self.roll},{self.branch}'
class AnuallDay(Students):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studetails=super().__str__()
        return f'{studetails},{self.program}'
    
sobj=Students('lahari',20,'h5','cse')
print(sobj)


