name=['Aero','Aranga']
password=["Aero@1602","Aero@1234"]
p=0
n=0
count=1
Input=input("Want to (Signin/Signup) ").lower()
if(count >= 1):
    if(Input=='signin'):
        Uname=input("Enter the user name: ")
        Upas=input("Enter the pasword : ")
        if Uname in name:
            n=1
            print(Uname)
        if Upas in password:
                p=1
                print(Upas)
            
        
    else:
        Nname=input("Enter the name: ")
        Npass=input("Enter the pass: ")
        CNpass=input("Retype the pasword: ")
        if(Npass == CNpass):
            name.append(Nname)
            password.append(Npass)
            print("Account Created Successfully")
        Input1=input("Want to 'signin': ").lower()
        if(Input1=='yes'):
            count+=1

if(p==1 and n==1):
    print("Login successful")  
else:
    print("NOt ")


    
      