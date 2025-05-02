Start

Create a dictionary called coin_values:
    "penny" → 0.01
    "nickel" → 0.05
    "dime" → 0.10
    "quarter" → 0.25

Set total to 0

Split the input sentence into parts using "and" as the separator

For each part in the list:
    Remove extra spaces
    Split the part into quantity and coin_name
    If coin_name ends with "s":
        Remove the "s" to make it singular
    Look up coin_name in coin_values
    Multiply quantity by the coin value
    Add the result to total

Round total to two decimal places

Display or return total

End
