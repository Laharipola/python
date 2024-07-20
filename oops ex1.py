class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def display(self):
        print("name is",self.name)
        print("roll is",self.roll)
        print("branch is",self.branch)
        print("address is",self.address)
        print("emial is",self.email)
s1=Student('lahari','5h5','cse','house','l@gmail.com')
s1.display()
    