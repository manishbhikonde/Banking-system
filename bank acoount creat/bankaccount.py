import json
import string
import random

class Bank:
    database = "bank.json"
    data = []
    
    try:
        with open(database) as fs:
            data = json.loads(fs.read())      
    except Exception as err:
        print(err)
    
    
    @classmethod
    def updatedata(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))
    
    
    @classmethod
    def randomifsc(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        number = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=2)
        id = alpha + number + spchar
        random.shuffle(id)
        return "".join(id)
    @classmethod
    def createaccount(cls):
        info = {
            "name":input("enter your name "),
        "email" :input("enter your email"), 
        "number" : input("enter your number"),
        "accountno.":cls.randomifsc(),
        "pin":int(input("please tell your pin")),
        "balance": 0,
        }
        print("Your account has been successfully created.")
        cls.data.append(info)
        cls.updatedata()
        
     
    @classmethod   
    def depositemoney(cls):
        an = input("please tell your account number")
        pin = int(input("please enter your pin"))
        
        user = [i for i in cls.data if i["accountno."] == an and i["pin"] ==pin]
        
        if not user:
            print("no user found")    
        else:
            print(f"your current balance :{user[0] ['balance']}")
            amt = int(input("how much money you want to deposit"))
            if amt >9999:
                print("sorry you can not deposit this much")
            else:
                user[0]["balance"] += amt
                print("amount added successfully")
                Bank.updatedata()        
    @classmethod
    def withdramoney(cls):
        an = input("please enter your account number")
        pin = int(input("enter your pin"))
         
        user = [i for i in cls.data if i["accountno."]==an and i["pin"]==pin]
         
        if not user:
            print("sorry no user found")
             
        else:
            print(f"your current balance :{user[0] ['balance']}")
            amt = input("how much money you want to withdraw")
            if amt > 9999 or amt > user[0] ["balance"]:
                print("sorry you cannot withdraw this amounnt")
                 
            else:
                user[0]["balance"] -= amt
                print(f"balance left: {user[0]['balance']}")
                print("withdraw successfully")
     
    
    @classmethod
    def updateinfo(cls):
        an = input("please enter your account number")
        pin = int(input("enter your pin"))
        
        user = [i for i in cls.data if i["accountno."]== an and i["pin"]==pin]
        
        if not user:
            print("sorry no user found")
        else:
            print("you cannot change the account number and balance")
            print("press enter to skip and fill the field if you want to change")
            
            newdata= {
                "name":input("press enter to skip or write your new name "),
                "email":input("press enter to skip or write your new email"),
                "pin":input("press enter to skip or write your new pin"),
                "number":input("press enter to skip or write your new number")
            }
            
            if newdata["name"] == "":
                newdata["name"] = user[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = user[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = user[0]["pin"]
            if newdata["number"] =="":
                newdata["number"] = user[0]["number"]
                
            for i in newdata:
                user[0][i] = newdata[i]
                
            cls.updatedata()
            print("your details have been updated successfully")  
    
    @classmethod
    def displaydetails(cls):
        an = input("please enter your account number")
        pin = int(input("enter your pin"))
        
        user = [i for i in cls.data if i["accountno."]== an and i["pin"]==pin]
        
        if user:
            print("Account Holder Name:", user[0]["name"])
            print("Account Balance:", user[0]["balance"])
        else:
            print("Invalid account number or PIN.")
        
        
         
while True:
    print("press 1 for creating account")                    
    print("press 2 for deposite money")
    print("press 3 for withdrawmoney")
    print("press 4 for updateinfo")
    print("press 5 for display your account details")
    print("press 0 to exit")
    check = input("tell your response")

    if check == "1":
        Bank.createaccount()
    elif check == "2":
        Bank.depositemoney()
    elif check == "3":
        Bank.withdramoney()
    elif check =="4":
        Bank.updateinfo()
    elif check =="5":
        Bank.displaydetails()
        
    elif check =="0":
        print("Thank you for using our servise.Goodbye!")
        break
    else:
        print("Invalid choice.Please try again")  







