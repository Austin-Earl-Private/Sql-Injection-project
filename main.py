import re

#  genQuerry
#  Funtion that takes uName and Password to combine them and print them as a SQL query command
#
def genQuery(uName, password):
   print(f"SELECT * FROM users WHERE username='{uName}' and password='{password}';\n")


#  genQueryWeak
#  Function that generates queries using weak mitigation techniques
#
def genQueryWeak(uName, password):
   print("BASE QUERY")
   print(f"SELECT * FROM users WHERE username='{uName}' and password='{password}';")
   print("WEAK MITIGATION QUERY")
   #  Sanitize both name and password before building query
   cleanUname = sanitizeString(uName)
   cleanPassword = sanitizeString(password)
   print(f"SELECT * FROM users WHERE username='{cleanUname}' and password='{cleanPassword}';\n")


#  genQueryWeak
#  Function that generates queries using strong mitigation techniques
#
def genQueryStrong(uName, password):
   print("BASE QUERY")
   print(f"SELECT * FROM users WHERE username='{uName}' and password='{password}';")
   print("STRONG MITIGATION QUERY")
   #  Reducing strings to lower and sanitizing the string for added security
   sanitizedUName = str.lower(sanitizeString(uName))
   #  By changing the way the query is setup and only getting the information needed 
   #  closes a lot of holes as well as allowing passowrds to be more complex
   print(f"SELECT password FROM users WHERE username='{sanitizedUName}';\n")


#  sanitizeString
#  Function that sanitizes strings using the following order "username and the password 
#  consist of letters, numbers, and underscores"
#
def sanitizeString(string):
   cleanString = re.sub(r'[^a-zA-Z0-9_]', '', string)
   return cleanString


#  testValid
#  Function to run valid cases
#  Note: Everyone in the team needs to create a test per case
#
def testValid(queryGen):
   validTests = [["Austin", "pass123"],
   ["Fr_Ed", "SuperSecure"],
   ["_Brad", "Cray_Cray"],
   ["Daniel_", "passpass321"],
   ["Spencer", "123456789"]]
   print("----  VALID TESTS    ----\n")
   for validTest in validTests:
      queryGen(validTest[0], validTest[1])
   print("--------------------\n")


#  testTautology
#  Function that runs tautology cases
# 
def testTautology(queryGen):
   tautologyTests = [["Austin", "' or 1=1 --"],
   ["Fr_Ed", "' or 1=1 --"],
   ["_Brad", "' or 1=1 --"],
   ["Daniel_", "' or 1=1 --"],
   ["Spencer", "' or 1=1 --"]]
   print("----  TAUTOLOGY TESTS    ----\n")
   for tautologyTest in tautologyTests:
      queryGen(tautologyTest[0], tautologyTest[1])
   print("--------------------\n")


#  testUnion
#  Function that runs union test cases
# 
def testUnion(queryGen):
   unionTests = [["Austin", "' UNION SELECT * from secrets --"],
   ["Fr_Ed", "' union select * from secrets --"],
   ["_Brad", "' union select * from secrets --"],
   ["Daniel_", "' union select count(*) from master.sys.database"],
   ["Spencer", "' union select * from master.sys.server"]]
   print("----  UNION TESTS    ----\n")
   for unionTest in unionTests:
      queryGen(unionTest[0], unionTest[1])
   print("--------------------\n")


#  testAddState
#  Function that runs additional stament test cases
# 
def testAddState(queryGen):
   addStatementTests = [["Austin", "'; delete * from users where ''='"],
   ["Fr_Ed", "'; delete * from users where ''='"],
   ["_Brad", "'; delete * from users where ''='"],
   ["Daniel_", "'; delete * from users where ''='"],
   ["Spencer", "'; delete * from users where ''='"]]
   print("----  ADD STATEMENT TESTS    ----\n")
   for addStatmentTest in addStatementTests:
      queryGen(addStatmentTest[0], addStatmentTest[1])
   print("--------------------\n")


#  testComment
#  Function that runs comment test cases
# 
def testComment(queryGen):
   commentTests = [["Austin ' --", ""],
   ["Fr_Ed ' --", ""],
   ["_Brad ' --", ""],
   ["Daniel_ ' --", ""],
   ["Spencer ' --", ""]]
   print("----  COMMENT TESTS    ----\n")
   for commentTest in commentTests:
      queryGen(commentTest[0], commentTest[1])
   print("--------------------\n")


#  manual_test
#  Function that runs user inputs and test them with strong 
#  or weak mitigation techniques
# 
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
    
#  run_Tests
#  Function that runs tests through query generator
# 
def run_Tests(queryGen):
   testValid(queryGen)
   testTautology(queryGen)
   testUnion(queryGen)
   testAddState(queryGen)
   testComment(queryGen)

#  menu
#  The function that contains the menu options. The user can select an option, 
#  and then the menu will call the function according to the user's selection
# 
def menu():
   while (True):
      print("Types of tests:")
      print("\t 1: Base Query Results")
      print("\t 2: Weak Mitigation Results")
      print("\t 3: Strong Mitigation Results")
      print("\t 4: Manual Input")
      test_type = int(input("Type which test to run: "))
      if test_type == 1:
         run_Tests(genQuery)
      elif test_type == 2:
         run_Tests(genQueryWeak)
      elif test_type == 3:
         run_Tests(genQueryStrong)
      elif test_type == 4:
         manual_test()
      else:
         print("Invalid input\n")
         continue

#  menu 
#  Here is where the program starts
#
menu()