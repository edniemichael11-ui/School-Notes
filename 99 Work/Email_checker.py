print("NO Numbers breaks code")
Email = input("Enter your email: ")
At_Positon = Email.find("@")
Period_Position = Email.find(".")
EmailUser = Email[0:At_Positon]
EmailUser2 =EmailUser
EmailUser = EmailUser.strip().isalpha()

if EmailUser == True:
    EmailDomain = Email[At_Positon+1:Period_Position]
    Email_Domain = EmailDomain
    EmailDomain = EmailDomain.isalpha()
    if EmailDomain == True:
        EmailDomain2 = Email[Period_Position+1:]
        Email_Domain2 = EmailDomain2
        EmailDomain2 = EmailDomain2.isalpha()
        if EmailDomain2 == True:
            
            print("Email Valid")
            print(f"User: {EmailUser2}")
            print(f"Domain: {Email_Domain}.{Email_Domain2}")
        else:
            print("Invalid, Try Again")

    else:
        print("Invalid, Try Again")
    



else:
    print("Invalid, Try Again")