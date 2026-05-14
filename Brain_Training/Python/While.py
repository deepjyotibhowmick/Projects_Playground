# i = 1
# while i < 10:
#     print("Now: ", i, "I love you Moni")
#
#     i = i + 1
# print("Loop completed")

your_tru_love = "moni"
your_love = ""
guess_count = 0
guess_limit = 3
limit_crossed = 0

while your_love != your_tru_love and guess_count < guess_limit:
    your_love = input("Enter your love name:")
    guess_count += 1
    # print(your_love,guess_count,guess_limit)
    if guess_count == guess_limit and your_love != your_tru_love:
        limit_crossed = 1


if limit_crossed == 0:
    print("You found your love. Congrats")
else:
    print("You failed to find")
