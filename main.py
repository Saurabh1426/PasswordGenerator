import string
import random

ch = input("Which type of Password you want \n 1) Random Password 2) Your secure password")
if(ch == "1"):
 if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = string.whitespace

    plen = int(input("Enter  Password Length : \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    random.shuffle(s)
    print("Your Password Is : ")
    print("".join(s[0:plen]))


elif(ch == "2"):
    SECURE = (('s', '$'), ('and', '&'),
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password\n")
    password = securePassword(password)
    print(f"Your secure password is {password}")


else:
    print("Invalid Number")

