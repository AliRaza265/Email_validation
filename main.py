
try:
    with open("mail.txt", "x") as f:
        print("file is created")
except:
  print("file is already exist")

mail = input("Enter your Email ID: ")
with open("mail.txt", "r") as file_read:
    for line in file_read:
        if mail in line:
            print("The mail is already exist")   
            exit()
if len(mail) > 10:
    print("The length is matched ✓")
    if mail[-4:] == ".com":
        print("The domain('.com') is matched ✓")
        if mail[-9:-4] == "gmail":
            print("The domain('gmail') is matched ✓")
            if "@" in mail:
                print("The @ is matched ✓")
                mailname = mail.split("@")
                if len(mailname[0]) > 3:
                    print("username  ✓")
                    with open("mail.txt",'a') as file_writer:
                        file_writer.write(mail + "\n")
                else:
                    print("short username ✕")
            else:
                print("The @ is no matched ✕")
        else:
            print("The domain('gmail') is no matched ✕")
    else :
        print("The domain('.com') is no matched ✕")
else: 
        print("The length is no matched ✕")
