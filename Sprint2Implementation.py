# coin values in dollars
coin_values = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}

# convert sentence to dollar amount
def parse_coin_sentence(sentence):
    total = 0.0
    parts = sentence.lower().split(" and ")
    for part in parts:
        tokens = part.strip().split()
        if len(tokens) != 2:
            continue
        quantity = int(tokens[0])
        denomination = tokens[1].rstrip('s')  # singular form
        if denomination in coin_values:
            total += quantity * coin_values[denomination]
    return round(total, 2)

# ask the user to type a sentence
user_input = input("Enter a sentence with coins: ")
print(parse_coin_sentence(user_input))
