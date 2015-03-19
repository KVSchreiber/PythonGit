#Improve the function ask_number() so that the function can be called with a step value.
#Make the default value of step 1.

def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

ask_number("Choose a number 0-50 that is divisible by 5", 0, 50, 5)
