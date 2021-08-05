import re

##First name and name format check
while True:
    FirstName = input("\nPlease enter your First Name: ")

    check = re.fullmatch(r"[A-Z][a-z]+", FirstName)

    if check == None:
        print("Format invalid! Please try again.")
        continue
    else:
        break

##Last name and name format check
while True:
    LastName = input("\nPlease enter your Last Name: ")

    check = re.fullmatch(r"[A-Z][a-z]+", LastName)

    if check == None:
        print("Format invalid! Please try again.")
        continue
    else:
        break

##DOB and format check
while True:
    DOB = input("\nPlease enter your Date of Birth (mm/dd/yyyy): ")

    check = re.fullmatch(r"^(0[1-9]|1[0-2])\/(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/(200[2-9]|20[1-9][0-9])", DOB)

    if check == None:
        print("Format invalid! Please try again.")
        continue
    else:
        break

##email address and format check
while True:
    email = input("\nPlease enter your Email Address: ")

    check = re.fullmatch(r"(.+[A-Z]*|[a-z]*|[0-9]*|_+|\.+)(\@[a-z]+\.\w{2,4})", email)

    if check == None:
        print("Format invalid! Please try again.")
        continue
    else:
        break

#Username and format check
while True:
    user = input("\nPlease enter a Username: ")

    check = re.fullmatch(r"([A-Z]|[a-z]|[0-9]|\_){6,12}", user)

    if check == None:
        print("Format invalid! Please try again.")
        continue
    else:
        break

#Password and format check
while True:
    password = input("\nPlease enter a Password: ")

    check = re.fullmatch(r"^[a-z](?=.{7,})(?=.*[A-Z])(?=.*\d)(?=.*[!$%&?])[A-Za-z0-9!$%&?]+$", password)

    if check == None:
        print( "Format invalid! Please try again.")
        continue
    else:
        break

#CC and format check
while True:
    ccnum = input("\nPlease enter your Credit Card Number (no spaces): ")

    check = re.fullmatch(r"(4|5)\d{15}", ccnum)

    if check == None:
        print("Invalid format! Please try again.")
        continue
    else:
        break

#CC date and format check
while True:
    ccdat = input("\nPlease enter your Credit Card Expiration Date (mm/yy): ")

    check = re.fullmatch(r"(0[5-9]|1[0-2])/24|(0[1-9]|1[0-2])/(2[5-9]|[3-9]|[0-9])", ccdat)

    if check == None:
        print("Invalid format! Please try again.")
        continue
    else:
        break

#CCCVC and format check
while True:
    cccvc = input("\nPlease enter your Credit Card Verification Code: ")

    check = re.fullmatch(r"\d{3}", cccvc)

    if check == None:
        print("Invalid format! Please try again.")
        continue
    else:
        break

userinfo = ["First Name: " + FirstName,
            "Last Name: " + LastName,
            "DOB: " + DOB,
            "Email address: " +email,
            "Username: " + user,
            "Password: " + password,
            "CC number: " + ccnum,
            "Expiration date: " + ccdat,
            "CVC: " + cccvc]

string = "\n".join(userinfo)

print("This is your user account information: \n\n" + string)

    
        
