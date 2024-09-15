class Student():
    id = 0
    name = ""
    gender = ""
    total = ""
    per = 0	
 
    def setData(self,id,name,gender,total,per):	# function to set data 
        self.id = id
        self.name = name
        self.gender = gender
        self.total = total
        self.per = per	
 
    def showData(self):	# function to get/print data
        print("Id :",self.id)
        print("Name :", self.name)
        print("Gender :", self.gender)
        print("Total :", self.total)
        print("Percentage :", self.per)
 
s = Student()
s.setData(13,'SUBRATA DATTA','Male',600,94.44)
s.showData()
