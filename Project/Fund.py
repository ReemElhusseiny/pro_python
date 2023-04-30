import re 
from getpass import getpass 

from getpass import getpass 

class User:
   
    def __init__(self):
        self.username = None
        self.password = None 
        self.id = None
    def registeration(self):
        self.user_id()
        self.check_username()
        self.check_password()
        self.save_to_file()
    
    def user_id(self):
     with open("reg.txt", 'r') as reg_file:
        self.id = len(reg_file.readlines())
        return self.id +1 
    
      
    #  while True : 
    #      reg_file = open('reg.txt' , 'r')
    #      users= reg_file.readlines()
    #      print(users)
    #      for user in users : 
    #        line = user.strip("\n")
    #        lineinfo = line.split("--->")
    #        print(lineinfo)
    #        print(lineinfo[2])
    #        if self.code == lineinfo[2] :
    #            self.code= input("code exists , enter again ")
         
    #        else :
    #            break  
     
   
        
   
    def check_username(self):
        pattern = r'^[a-zA-Z]+$'
        while True:
            username = input("Enter Your UserName: ")
            if re.match(pattern, username):
                self.username = username
                print("Valid username.")
                break
            else:
                print("Invalid username. Please try again.")

    def check_password(self):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#])[A-Za-z\d@#]{8,}$'
        while True:
            print("Password should contain capital and small letters, numbers, and special characters.")
            password = getpass("Create Password: ")
            if re.match(pattern, password):
                self.password = password
                print("Valid password.")
                break
            else:
                print("Invalid password. Please try again.")

    def save_to_file(self):
        try:
            with open('reg.txt', 'a') as reg_file:
                reg_file.write(f' {self.username} ---> {self.password} ---> {self.id} \n')
                print("Account created.")
        except IOError:
            print("Failed to create account .")
      
    def login(self):
        while True:
            username = input("Enter Your UserName: ")
            password = getpass("Enter Password: ")
            reg_file = open('reg.txt' , 'r').read()
            if username and password in reg_file :
                print('Welcome')
                #self.view()
                
            else:
                print('Invalid username or password. Please try again.')
                print (" or if you don't make registration , you should register firstly")
    
    def view (self):
        with open('pro_desc.txt', 'r') as pro_file:
               print(pro_file.read())
    
    
    def edit (self) : 
      
      pro_name = input("Enter name of project: ")
      old = input("Enter the old word: ")
      new = input("Enter the new word: ")
      with open("pro_desc.txt", "r") as file:
         lines = file.readlines()
      with open("pro_desc.txt", "w") as file:
        replaced = False
        for line in lines:
            if pro_name in line:
                if old in line:
                    replaced_line = line.replace(old, new)
                    file.write(replaced_line)
                    replaced = True
                else :
                    file.write(line)
                    if not replaced:
                        print("{old}  not found.")
            else:
                file.write(line)
        if not replaced:
            print("Project name not found.")
      
    
       
    



# user2 = User()  #soha ---> Password: SOha123@
# #user2.login()
user1= User()
user1.registeration() 
#user1.login() 
#user1.view()
#user1.edit()
#user1.delete() 

# arr = []

class Project:
    def _init_(self):
        self.username = None
        self.title = None
        self.details = None
        self.total_target = None 
        
    def create_pro(self):
        self.username = input("enter your username: ")
         
        self.title = input("Enter title of project: ")
        self.details = input("Enter details of project: ")
        self.total_target = input("Enter total target of project: ")
        
     
        # while True:
        #     self.code = input("Enter your owner code: ")
        #     if self.code in arr:
        #         print("Code already used. Please try another one.")
        #     else:
        #         arr.append(self.code)
        #         break

    def start_date(self):
        pattern1 = r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        while True:
            start_date = input("Enter start time for the campaign of project with format dd/mm/yyyy : ")
            if re.match(pattern1, start_date):
                self.start_date = start_date
                print("Valid start date.")
                break
            else:
                print("Invalid start date. Please try again.")
    def end_date(self):
        pattern2 = r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        while True:
            end_date = input("Enter end_date for the campaign of project with format dd/mm/yyyy : ")
            if re.match(pattern2, end_date):
                self.end_date = end_date
                print("Valid end date.")
                break
            else:
                print("Invalid end date. Please try again.")
    def save_to_file(self):
        try:
           with open('pro_desc.txt', 'a') as pro_file:
                pro_file.write(f'title: {self.title} ---> details: {self.details} ---> total_target: {self.total_target} ---> start_date: {self.start_date} ---> end_date: {self.end_date} ---> code: {self.code} \n')
                print("data inserted successfully.")
        except IOError:
            print("Failed to insert data .")

# proj = Project()
# proj.desc()
# proj.start_date()
# proj.end_date()
# proj.save_to_file()
# proj2 = Project()
# proj2.desc()
# proj2.start_date()
# proj2.end_date()
# proj2.save_to_file()


           
# print()
#                 def create project 
#                 input = ("enter id") 
#                 for lines pass user id 
#                     break 
#                  create project 
#                     pro1.project(id) 
#                       store , id , title 
                       
#                      id in file  
#                 break


reem ---> yass --->  reem ---> 01012345678 --->  reem --->  0 
nada ---> nada --->  n ---> 01012345678 --->  nada --->  1 
mariam ---> mariam --->  m ---> 01112345678 --->  mariam --->  2 


 reem ---> school ---> llllll --->  320000 --->  1/2/2024 ---> 1/2/2025
 nada ---> hospital ---> llllll --->  430000 --->  1/4/2025 ---> 1/5/2027




 reem ---> school ---> l --->  320000 --->  1/2/2024 ---> 1/2/2025
 nada ---> hospital ---> llllll --->  430000 --->  1/4/2025 ---> 1/5/2027
 reem ---> schoohh ---> hh --->  320000 --->  1/2/2024 ---> 1/2/2025
 reem ---> nnn ---> hhh --->  8888 --->  1/2/2026 ---> 1/2/2027  
 reem ---> dd ---> gg --->  66 --->  1/2/2022 ---> 1/2/2023 ---> reem@yahoo  
 reem ---> dd ---> uuu --->  66 --->  1/2/2022 ---> 1/2/2023 ---> reem@yahoo  


reem ---> dd ---> mariam --->  66 --->  1/2/2022 ---> 1/2/2023 ---> reem@yahoo  
nada---> hh ---> uuu --->  666 --->  1/2/2022 ---> 1/2/2023 ---> nada@yahoo 

reem ---> school ---> fff --->  10000 --->  1/2/2023 ---> 1/2/2024 ---> reem@yahoo  