def parseemail(inputemail):
    index=inputemail.find('@')
    if index<0:
        print(f"Invalid email entry  : {inputemail}")
        return False
    else:
        name=inputemail[:index]
        domain=inputemail[(index+1):]
    dot=inputemail.find('.')
    if dot<0:
        print(f"Invalid email entry  : {inputemail}")
        return False
    else:
        extension=inputemail[(dot+1):]
    print("User name is",name)
    print("domain and extension is",domain)
    print("Extension is ", extension)
    return

parseemail("silpapravinrediffmail.com")
parseemail("silpapravin@rediffmailcom")
parseemail("silpathankaraj@gmail.com")
inputemail=input("Enter email address")
parseemail(inputemail)

############################################

