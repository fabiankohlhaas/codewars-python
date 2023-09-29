# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'

def greet(name, owner):
    return "Hello boss" if name == owner else f"Hello guest"

if __name__ == "__main__":
    print(greet('Daniel', 'Daniel'))
    print(greet('Greg', 'Daniel'))