'''pwd=input("Enter the password")

try:
    assert len(pwd)==8,"Invalid password Exception, please enter password with 8 characters"

except AssertionError as obj:
    print(obj)
    

print("Password validation completed")
'''

class InvalidPasswordException(Exception):
    def __init__(self,msg):
        self.msg=msg
        print(self.msg)
        

try:
    pwd=input("Please enter the password")
    if(len(pwd)>=8):
        print("Password validation succeeded")
    else:
        raise InvalidPasswordException("The password should be more than 8 chracters length")

except InvalidPasswordException:
    print("The password should be atleast 8 characters long!")
