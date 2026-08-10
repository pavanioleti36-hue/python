pswd= input("enter password:-")
valid=True
#not empty
if pswd == "":
    print("password must be not empty ")
    valid= False
#atleast have 8 characters
if len(pswd)<8:
    print("password must have atleast 8 characters") 
    valid= False 
#must include atleast one uppercase letter  
if not any(ch.isupper() for ch in pswd):
    print("password must have one upper letter")
    valid= False
#must inlcude atleast one lowercase letter    
if not any(ch.islower() for ch in pswd):
    print("password must have one lower letter") 
    valid= False
#must not same as email
if ".com" in pswd:
    print("password must not equal to email")
    valid= False
#must  not include any spaces     
if " " in pswd:
    print("password must not contains any spaces")
    valid= False
#must start and end with a letter or digit   
if not(pswd[0].isalnum()) and not(pswd[-1].isalnum()):
    print("password must start and end with a letter or digit")
    valid= False
if valid:
    print("password is perfect")        