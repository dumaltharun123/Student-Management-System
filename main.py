student={1:{"name":"A",
                "marks":90}}
   
id=2
while True:
 try:
     option=int(input("1.Add Student\n2.Search studen\n3.display students\n4.update student\n5.delete studen\n6.exit\nEnter the option above:"))
     
     if option==1:
        name=input("enter the name:")
        marks=int(input("enter the marks:"))
        student[id]={
            "name":name,
            "marks":marks
        }
        print(f"{student.items()}\nstudent added sucessfully!")
        id+=1
   
        print("enter valid name")
 
     if option==2:
    
        id=int(input("enter the id of student:"))
        for key in student.keys():
            if key==id:
                print("student exists!")
                break
        else:
                print("student doesn't exist!")
      
     if option==3:
  
      for key,value in student.items():
        print(key,value["name"],value["marks"])

     if option==4:
     
        id=int(input("enter the student id:"))
        marks=int(input("enter the marks:"))
        for key,value in student.items():
            if key==id:
                value["marks"]=marks
                print(f"{student}\nmarks updated sucessfully!")
       
     if option ==5:
        id=int(input("enter the student id:"))
        if id in student.keys():
          del student[id]
          print(f"{student}\nstudend deleted sucesfully!")
          
        else:
            print("id doesnt exits")
        
     if option==6:
        print("application closed!")
        break
     
 except ValueError:
        print("value error! Enter valid inputs values")