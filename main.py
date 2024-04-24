import time

tokens = []
special_chars = [" ", "+", "-", "*", "/", "(", ")"]

def tokenize(string_to_tokenize):
    current_token = ""
    for x in range(len(string_to_tokenize)):
        if special_chars.__contains__(string_to_tokenize[x]):
            tokens.append(current_token)
            tokens.append(string_to_tokenize[x])
            current_token = ""
        else:
            current_token += string_to_tokenize[x]
    tokens.append(current_token)
    print_result()

def print_result():
    string = ""
    for y in range(len(tokens)):
        string += tokens[y]
    print(str(eval(string)))
    tokens.clear()

while True:
    equation = input("Enter an equation: ")
    print()
    print("The answer is: ")
    time.sleep(0.5)
    tokenize(equation)
    print()
