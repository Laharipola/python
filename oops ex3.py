class Student:
    def __init__(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    '''def display(self):
        print("name is",self.name)
        print("roll is",self.roll)
        print("branch is",self.branch)
        print("address is",self.address)
        print("emial is",self.email)'''
    def __str__(self):
        return f'{self.name} {self.roll} {self.branch}'
s1=Student('lahari',101,'cse')
s2=Student('alekya',102,'cse')
print(s1)
print(s2)
