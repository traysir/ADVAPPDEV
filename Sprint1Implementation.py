coin_values = {
    'penny': 0.01,  
    'nickel': 0.05, 
    'dime': 0.10,  
    'quarter': 0.25  
}


def parse_coin_sentence(sentence):
    total = 0.0  # initialize total value to 0
    parts = sentence.split(" and ")  # split the sentence into parts by "and"
    for part in parts:
        tokens = part.split()  
        quantity = int(tokens[0])  # extract thefirst word
        coin = tokens[1]  # extract second word)
        total += quantity * coin_values[coin]  
    return total  # return

user_input = input("Type coin sentence: ")  #user's turn
print(parse_coin_sentence(user_input))  # print