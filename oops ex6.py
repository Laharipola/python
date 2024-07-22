class Student:
    def __init__(self,name,role,result):
        self.name=name
        self.role=role
        self.__result=result      #private data
    def get_result(self):     #public method and data is private
        return self.__result
    def Studisplay(self):      #public method
        print(self.name,self.role)
class College(Student):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def Clgdisplay(self):
        print(self.cname,self.loc)
    def _admission(self):     #protected method
        print('admissions for cse')
cobj=College('sridevi','vatinagullapally')
sobj=Student('lahari','stu',99)
sobj.Studisplay()
print(cobj._admission())
