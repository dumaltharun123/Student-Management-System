student={
    101:{
        "name":"A",
        "marks":95
    } ,
    102:{
        "name":"B",
        'marks':90
    },
    103:{
        "name":"C",
        "marks":80
    }
}


while True:
    option=int(input("\n1.Add student\n2.Display all students Id,names and thier marks\n3.search student\n4.update marks\n5.delete student\n6.exit\nEnter the options above:"))
    if option==1:
        name=input("enter the name:")
        marks=int(input("enter the marks:"))
        ID=int(input("enter the id"))
        student[ID]={

            "name":name,
            "marks": marks
        }
        
    elif option ==2:
        for key,values in student.items():
            print(key,values["name"],values["marks"])
        
    elif option==3:
        name=input("enter the student name:")
        for i in student.values():
            if i["name"]==name:
                print("Student exits")
                break
        else:     
            print("Studen doesn't exists")

    elif option==4:
        name=input("enter the student name:")
        marks=int(input("enter the studend marks:"))
        for inner_dict in student.values():
            if inner_dict["name"]==name:
                inner_dict["marks"]=marks
                print("marks updated")
                print(student)
           
    elif option==5:
        ID=int(input("enter the id of stuent:"))
        del student[ID]
        print(student)

    elif option==6:
        break