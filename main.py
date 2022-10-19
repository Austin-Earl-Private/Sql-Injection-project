import re

valid = [("test", "test")]
tautology = [("test", "' or 1=1 --")]
union = [("test", "' union select * from secrets --")]
add_stm = [("test", "'; delete * from users where ''='")]
comment = [("test ' --", "")]


def generate_query(username, password):
    return f"select * from users where username='{username}' and password='{password}';"


def test_query(username, password, sanitizer):
    print(f"\tQuery before sanitization:  {generate_query(username, password)}")
    print(f"\tQuery after sanitization:  {generate_query(sanitizer(username), sanitizer(password))}")
    print("")


def sanitize(value):
    return value


def automated_tests():
    print("Testing Valid Queries:")
    for set in valid:
        test_query(set[0], set[1], sanitize)
    print("Testing Tautology Queries:")
    for set in tautology:
        test_query(set[0], set[1], sanitize)
    print("Testing Union Queries:")
    for set in union:
        test_query(set[0], set[1], sanitize)
    print("Testing Added Statement Queries:")
    for set in add_stm:
        test_query(set[0], set[1], sanitize)
    print("Testing Comment Queries:")
    for set in comment:
        test_query(set[0], set[1], sanitize)


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
            continue


if __name__ == "__main__":
    type = menu()
    if type == 1:
        automated_tests()
    else:
        manual_test()
