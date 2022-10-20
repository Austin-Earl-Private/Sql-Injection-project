import re

#Generates base query
def genQuery(uName, password):
   print("TEST")

#generates queries with weak mitigation techniques
def genQueryWeak(uName, password):
   print("TEST")

#generates queries with strong mitigation techniques
def genQueryStrong(uName, password):
   print("TEST")

#sanitize string following rule "username and the password consist of letters, numbers, and underscores"
def sanitizeString(string):
   print("TEST")

#run valid test cases
def testValid(queryGen):
   valid = [["test", "test"],
   [],
   [],
   [],
   []]

#run tautology test cases
def testTautology(queryGen):
   tautology = [["test", "' or 1=1 --"],
   [],
   [],
   [],
   []]

#run union test cases
def testUnion(queryGen):
   union = [["test", "' union select * from secrets --"],
   [],
   [],
   [],
   []]

#run additional statement test cases
def testAddState(queryGen):
   add_stm = [["test", "'; delete * from users where ''='"],
   [],
   [],
   [],
   []]

#run comment test cases
def testComment(queryGen):
   comment = [["test ' --", ""],
   [],
   [],
   [],
   []]

#manual test option
def manual_test():
    username = input("What Username would you like use? ")
    password = input("What Password would you like to use? ")
    while(True):
        san = input("What type of Sanitizer would you like to use? Strong or Weak (s/w)")
        if san.lower() =="strong" or san.lower() =="s":
            genQueryStrong(username, password)
            break
        elif san.lower() =="weak" or san.lower() =="w":
            genQueryWeak(username, password)
            break
        else:
            print("Invalid input")
            continue
    
#run tests through query generator
def run_Tests(queryGen):
   testValid(queryGen)
   testTautology(queryGen)
   testUnion(queryGen)
   testAddState(queryGen)
   testComment(queryGen)

#basic menu function
def menu():
   while (True):
      print("Types of tests:")
      print("\t 1: Base Query Results")
      print("\t 2: Weak Mitigation Results")
      print("\t 3: Strong Mitigation Results")
      print("\t 2: Manual Input")
      test_type = int(input("Type which test to run: "))
      if test_type == 1:
         run_Tests(genQuery)
      elif test_type == 2:
         run_Tests(genQueryWeak)
      elif test_type == 3:
         run_Tests(genQueryStrong)
      elif test_type == 4:
         manual_test
      else:
         print("Invalid input\n")
         continue

menu()

#program run point
if __name__== "__test__":
   menu()