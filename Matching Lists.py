# --- Baby name lists --- #
baby_names = ["Emma", "Olivia", "Noah", "Liam", "Ava", "Sophia", "William", "Mason", "James", "Isabella"]
baby_numbers = [19414, 19246, 19015, 18138, 16237, 16070, 15668, 15192, 14776, 14722]

# --- Print intro --- #
print("Here are the most popular baby names of the year 2016,")
print("with how many babies were named each.")

# --- Print lines --- #
for i in range(len(baby_names)):
    output = str(i + 1) + "."
    output += baby_names[i]
    output += " - "
    output += str(baby_numbers[i])
    print(output)
