# --- Declare Lists --- #
items = []
prices = []

# --- User input --- #
print("Welcome to Menu Builder!")
item = ""
while item != "done":
    item = input("Enter an item (or done to end): ")
    if item == "done":
        break
    price = int(input("What is the item's price? "))
    items.append(item)
    prices.append(price)

# --- Print menu --- #
print()
print("MENU:")

for i in range(len(items)):
    output = str(i + 1) + "."
    output += items[i]
    output += " - "
    output += str(prices[i])
    print(output)
