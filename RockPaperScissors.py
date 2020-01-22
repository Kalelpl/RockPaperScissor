print('User 1, please choose rock, paper and scissors')
user1 = input()
print('User 2, please choose rock, paper and scissors')
user2 = input()


if user1 == user2:
    print('We have a draw')
elif user1 == 'rock':
    if user2 == 'paper':
        print('Paper beats rock, User 2 wins')
    else:
        print('Rock beats scissors, User 1 wins')
elif user1 == 'paper':
    if user2 == 'rock':
        print('Paper beats rock, User 1 wins')
    else:
        print('Rock beats scissors, User 2 wins')
elif user1 == 'scissors':
    if user2 == 'rock':
        print('Rock beats scissors, User 1 wins')
    else:
        print('Paper beats rock, User 2 wins')
else:
    print('Please type one of the words given')

