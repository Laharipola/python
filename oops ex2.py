class Student:
    branch='cse'
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        #self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print("name is",self.name)
        print("roll is",self.roll)
        print("branch is",self.branch)
        print("address is",self.address)
        print("emial is",self.email)
        print()
s1=Student('lahari','5h5','house','l@gmail.com')
s2=Student('Alekya','5h6','house','A@gmail.com')
s1.display()
s2.display()
    