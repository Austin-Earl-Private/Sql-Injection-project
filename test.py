import re

#Generates base query
def genQuery(uName, password):
   print("TEST")

#run valid test cases
def testValid():
   print("TEST")

#run tautology test cases
def testTautology():
   print("TEST")

#run union test cases
def testUnion():
   print("TEST")

#run additional statement test cases
def testAddState():
   print("TEST")

#run comment test cases
def testComment():
   print("TEST")

#generates queries with weak mitigation techniques
def genQueryWeak():
   print("TEST")

#generates queries with strong mitigation techniques
def genQueryStrong():
   print("TEST")

#sanitize string following rule "username and the password consist of letters, numbers, and underscores"
def sanitizeString(string):
   print("TEST")

def manual_test():
    username = input("What Username would you like use? ")
    password = input("What Password would you like to use? ")
    sanitizer = genQuery
    while(True):
        san = input("What type of Sanitizer would you like to use? Strong or Weak (s/w)")
        if san.lower() =="strong" or san.lower() =="s":
            sanitizer = genQueryStrong
            break
        elif san.lower() =="weak" or san.lower() =="w":
            sanitizer = genQueryWeak
            break
        else:
            print("Invalid input")
            continue

def run_Tests():
   print("TEST")

#basic menu function
def menu():
    while (True):
        print("Types of tests:")
        print("\t 1: Base Query Results")
        print("\t 2: Weak Mitigation Results")
        print("\t 3: Strong Mitigation Results")
        print("\t 2: Manual Input")
        test_type = int(input("Type which test to run: "))


#program run point
if __name__ == "__test__":
   menu()