import random
words = ["python", "java", "swift", "javascript", "nigger"]
wins = 0
loses = 0


def counter_of(list1):
    counter1 = list1.count("-")
    if counter1 == 0:
        return True
    elif counter1 != 0:
        return False


def is_english(s):
    return s.isascii() and s.isalpha()


def letter_check(a):
    truers = 0
    if len(a) == 1:
        truers += 1
    else:
        print("Please, input a single letter.")
        pass
    if is_english(a):
        if a.lower() == a:
            truers += 1
        else:
            print("Please, enter a lowercase letter from the English alphabet.")
    else:
        print("Please, enter a lowercase letter from the English alphabet.")
    if truers == 2:
        return True


print(f"H A N G M A N  # 8 attemps")
while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    answer = input()
    if answer == "exit":
        break
    elif answer == "results":
        print(f"""You won: {wins} times.
        You lost: {loses} times.""")
    elif answer == "play":
        attempts = 8
        guess_set = set()
        get_index = 0
        get_index1 = 0
        guessed_set = set()
        exit_flag = False
        new_word = ""
        list_of = []
        guess = random.choice(words)
        for i in range(0, len(guess)):
            list_of.append("-")
            guess_set.add(guess[i])
        new_word = "".join(list_of)
        while True:
            if attempts == 0:
                print("You lost!")
                loses += 1
                break
            else:
                print("".join(list_of))
                print("Input a letter:", end='')
                the_players_letter = input()
                if the_players_letter in guessed_set:
                    print("You've already guessed this letter.")
                    print("".join(list_of))
                    continue
                else:
                    b = the_players_letter
                    if letter_check(b) and the_players_letter not in guessed_set:
                        print(f"# {attempts} attempts\r")
                        guessed_set.add(the_players_letter)
                        if the_players_letter in guess_set:
                            get_index = guess.index(the_players_letter)
                            if list_of[get_index] == guess[get_index]:
                                print("No improvements.")
                                attempts -= 1
                            else:
                                list_of[get_index] = guess[get_index]
                                if counter_of(list_of):
                                    print(f"""You guessed the word {guess}!
                                    You survived!""")
                                    wins += 1
                                    break
                                else:
                                    pass
                            while True:
                                try:
                                    get_index1 = guess.index(the_players_letter, get_index + 1)
                                    list_of[get_index1] = guess[get_index1]
                                    if counter_of(list_of):
                                        print(f"""You guessed the word {guess}!
                                        You survived!""")
                                        wins += 1
                                        exit_flag = True
                                        break
                                    else:
                                        pass
                                    print("".join(list_of))
                                    break
                                except ValueError:
                                    print("".join(list_of))
                                    break

                        else:
                            print("That letter doesn't appear in the word.")
                            print("".join(list_of))
                            attempts -= 1
                            continue
                    else:
                        print("".join(list_of))
                        continue
            if exit_flag:
                break
