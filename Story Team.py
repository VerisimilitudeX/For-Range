people = int(input("How many people will play "))

words = []

players_word = ""
playernum = 0
while players_word != "The end.":

    for i in range(people):

        print()

        if playernum < 4:
            playernum += 1
        else:
            playernum = 1
        players_word = input("It's player " + str(playernum) + "'s turn. Enter a word ('The end.' to quit): ")

        words.append(players_word)

        if players_word == "The end.":
            break

story = ""

for word in words:
    story += word + " "

print()
print(story)
