import re 
class Project:
    def init(self):
       self.title = None
       self.details = None
       self.total_target = None
       self.fname = None 
       self.owner= None
       self.donate=None
        
    def creat_pro(self , email):
        self.fname = input("Enter your first name: ")
        with open("reg.txt", "r") as reg_file:
            lines = reg_file.readlines()
            with open("reg.txt", "a") as reg_file:
                for line in lines:
                    if self.fname in line :
                        self.title = input("Enter title of project: ")
                        self.details = input("Enter details of project: ")
                        self.total_target = int(input("Enter total target of project: "))
                        self.owner= email
                        self.start_date()
                        self.end_date()
                        self.save_to_file()
                        break
                    else:
                        print("you should register  first! ")
        
    
    
    def view (self):
        with open('pro_desc.txt', 'r') as pro_file:
               print(pro_file.read())

    def edit(self , email):
        pro_name = input("Enter name of project: ")
        old = input("Enter the old word: ")
        new= input("Enter the new word: ")
        project=open("pro_desc.txt" , "r+")
        lines=project.readlines()
        project.seek(0)
        for line in lines:
            if pro_name in line and email in line:
                if old in line:
                   
                    line = line.replace(old,new)
                    project.write(line)
                else:
                    print("Error: old word not found in line.")
                    project.write(line)
                break
               
            else:
                print("Error: project not found.")
            project.truncate()
        print("Done editing.")  


 
    def delete(self, email):
      pro_name = input("Enter name of project: ")
      with open("pro_desc.txt", "r") as project:
        lines = project.readlines()
      with open("pro_desc.txt", "w") as project:
        for line in lines:
            if not (pro_name in line and email in line):
                project.write(line)
      print("deleted successfully.")



    def donate(self):
      pro_name = input("Enter project name to donate: ")
      donate= int(input("enter nalue of money: "))
      with open('pro_desc.txt', 'r+') as pro_file:
        for line in pro_file:
           fields = line.strip().split("--->")  
           if pro_name in line  :
               x = int(fields[3]) - int(donate)
               line= line.replace(fields[3] , str(x))
               break 
            #   print(type(fields[3]))
            #   print(type(donate))
           else : 
               print("project doesn't exist") 
            
               
    #         # do something if the fourth field has the value 'value_to_check'
    #   amount_str = input(f"Enter amount to donate (maximum {Project['target'] - sum(Project['donations'])} EGP): ")
    #   amount = float(amount_str)

    #   if amount <= 0:
    #     print("Invalid amount. Please enter a positive number.")
    #     return

    #   if amount > Project['target'] - sum(Project['donations']):
    #     print("Donation amount exceeds the remaining target amount.")
    #     return

       

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
                pro_file.write(f' {self.fname} ---> {self.title} ---> {self.details} --->  {self.total_target} --->  {self.start_date} ---> {self.end_date} ---> {self.owner}  \n')
                print("data inserted successfully.")
        except IOError:
            print("Failed to insert data .")
# user1.login()

# pro=Project()
# ans=input("are ")
# if ans == "y":
#     pro.creat_pro()
    
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

# pro1= Project()
# pro1.creat_pro()