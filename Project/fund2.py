import re 
from getpass import getpass 
from cc import Project 
class User:
    def init(self):
        self.fname = None
        self.lname = None
        self.password = None 
        self.id = None
        self.email= None
        self.phone= None 
        

    def registration(self):
        self.user_id()
        self.Fname()
        self.Lname()  
        self.Email()
        self.phone_number()
        self.check_password()
        self.confirm_password()
        self.save_to_file()
        
    def user_id(self):
     with open("reg.txt", 'r') as reg_file:
        self.id = len(reg_file.readlines())
        return self.id +1
    def Fname(self):
        pattern1 = r'^[a-zA-Z]+$'
        while True:
            self.fname = input("Enter your first name: ")
            if re.match(pattern1, self.fname):
                print("Valid first name.")
                break
            else:
                print("Invalid first name. Please try again.")
                
    def Lname(self):
        pattern3 = r'^[a-zA-Z]+$'
        while True:
            self.lname = input("Enter your last name: ")
            if re.match(pattern3, self.lname):
                print("Valid last name.")
                break
            else:
                print("Invalid last name. Please try again.")
              
    def Email(self):
        pattern2 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        while True:
            self.email = input("Enter your email: ")
            if re.match(pattern2, self.email):
                print("Valid email.")
                break
            else:
                print("Invalid email. Please try again.")
                
    def phone_number(self):
        pattern5 = r'^01[0125][0-9]{8}$'
        while True:
            self.phone = input("Enter your phone_number: ")
            if re.match(pattern5, self.phone):
                print("Valid phone_number.")
                break
            else:
                print("Invalid phone_number. Please try again.")
                
    def check_password(self):
        pattern4 =r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        while True:
            print("Password should contain capital and small letters, numbers, and special characters.")
            self.password = getpass("Create password: ")
            if re.match(pattern4, self.password):
                print("Valid password.")
                break
            else:
                print("Invalid password. Please try again.")
    def confirm_password(self):
      while True:
        confirm_password = getpass("Confirm your password: ")
        if self.password == confirm_password:
            print("Password confirmed.")
            return self.password
        else:
            print("Passwords do not match. Please try again.")
                
    def save_to_file(self):
        try:
            with open('reg.txt', 'a') as reg_file:
                reg_file.write(f'{self.fname} ---> {self.lname} --->  {self.email} ---> {self.phone} --->  {self.password} --->  {self.id} \n')
                print("Account created.")
                reg_file.close()
        except IOError:
            print("Failed to create account.")
    def login(self):
        while True:
            email = input("Enter Your email : ")
            password = getpass("Enter Password: ")
            file = open('reg.txt' , 'r')
            reg_file= file.read()
            if email and password in reg_file :
                print('Welcome')
                file.seek(0)
                pro1= Project()
                choice=input("enter create or view or delete or edit or donate : ")
                if choice == "create" :
                  pro1.creat_pro(email)
                elif choice == "edit" :  
                  pro1.edit(email)
                elif choice == "delete" :
                 pro1.delete(email)
                elif choice == "view" :
                    pro1.view()
                elif choice == "donate" :
                    pro1.donate()
                else :
                    print("invalid choice")
                file.close()
                file = open('reg.txt' , 'w')
                file.write(reg_file) 
                file.close()
                break 
            else:
                print('Invalid username or password. Please try again.')
                print (" or if you don't make registration , you should register firstly")
        




user1= User()
#user1.registration()
#user2=User()
user1.login()






