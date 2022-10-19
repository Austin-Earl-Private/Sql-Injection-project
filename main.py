import re

# f"select * from test where username= '{}' and password = '{}'"
test_strings = ["""select * from test where username="test" and password = "hacked" """]
comment = "' OR 1=1 and ''='\\"




def sanitize(value):
    # No " union " no " or " no "'" no "--" no ";"
    result= re.sub(r"\bunion\b|\bor\b|'|--|;|\\","",value,flags=re.IGNORECASE,count=0)
    # print(result)
    print(result)
    return result

if __name__ == "__main__":
    print(f"select * from test where username='{sanitize(comment)}' and password = '{sanitize('test;')}';")
    # print()