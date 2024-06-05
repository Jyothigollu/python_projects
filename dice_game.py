import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
#value=roll()
#print(value)


while True:
    players=input("Enter the number of players (1-4): ")
    if players.isdigit():
        players=int(players)
        if 1<=players<=4:
            break
        else:
            print("must be between 1-4 players")
    else:
        print("Invalid,Try again")


max_score=50
players_score=[0 for _ in range(players)]
#print(players_score)


while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nplayer",player_idx+1,"trun has just started!")
        print("your total score is:",players_score[player_idx],"\n")

        current_score=0
        while True:
            should_roll=input("would you like to roll (y/n) ? ")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("you rolled a 1! Trun down")
                current_score=0
                break
            else:
                current_score+=value
                print("you rolled a",value)
            print("your score is:",current_score)
        players_score[player_idx]+=current_score
        print("your total score is:",players_score[player_idx])
max_score=max(players_score)
winning_index=players_score.index(max_score)
print("player number",winning_index+1,"is the winner with score of :",max_score)

