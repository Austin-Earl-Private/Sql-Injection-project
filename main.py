import re

valid = [("test", "test")]
tautology = [("test", "' or 1=1 --")]
union = [("test", "' union select * from secrets --")]
add_stm = [("test", "'; delete * from users where ''='")]
comment = [("test ' --", "")]

# all generate queries must accept two values.
def generate_user_query(username, password):
    return f"select * from users where username='{username}' and password='{password}';"


# value1 and value 2 will go into the query. Sanitizer only sanitizes one element at a time
def test_query(value1, value2, sanitizer, query):
    print(f"\tQuery before sanitization:  {query(value1, value2)}")
    print(f"\tQuery after sanitization:  {query(sanitizer(value1), sanitizer(value2))}")
    print("")

# input has bad elements removed and then after being cleaned is returned
def sanitize(value):
    return value


def automated_tests():
    print("Testing Valid Queries:")
    for set in valid:
        test_query(set[0], set[1], sanitize,generate_user_query)
    print("Testing Tautology Queries:")
    for set in tautology:
        test_query(set[0], set[1], sanitize,generate_user_query)
    print("Testing Union Queries:")
    for set in union:
        test_query(set[0], set[1], sanitize,generate_user_query)
    print("Testing Added Statement Queries:")
    for set in add_stm:
        test_query(set[0], set[1], sanitize,generate_user_query)
    print("Testing Comment Queries:")
    for set in comment:
        test_query(set[0], set[1], sanitize,generate_user_query)


def manual_test():
    username = input("What Username would you like use? ")
    password = input("What Password would you like to use? ")
    test_query(username, password, sanitize)


def menu():
    while (True):
        print("Types of tests:")
        print("\t 1: Automated Tests")
        print("\t 2: Manual Test")
        test_type = int(input("Type which test to run: "))
        if test_type == 1 or test_type == 2:
            return test_type
        else:
            print("Invalid input\n")
            continue


if __name__ == "__main__":
    type = menu()
    if type == 1:
        automated_tests()
    else:
        manual_test()
