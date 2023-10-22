# Nicholas Heaton

# This code allows a dice game to be performed in a few different ways. first a person can choose to play a game with a
# computer, where the first one to reach 100 points wins. There is also a mode where the computer can play a solo game
# where it will keep rolling until reaching 100 then printing amount of turns and score for each turn.
# Finally, the last mode allows two computers to play a certain amount of games. The winner in this case is whichever
# computer won the most games.


# I certify that this code is mine, and mine alone, in accordance with GVSU academic honesty policy.

# 10/21/2023


import random


# roll_dice() provides two separate dice, rolling random numbers between 1 and 6 whenever the function is called on.

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def computer_turn(game_score, goal):
    turn_total = 0
    # while the turn_total is less than the goal total then the loop will continue until you roll both dice as 1's
    # setting game_score to 0. If that passes then it checks for a single occurrence of 1 in the dice, setting the
    # current score to 0. If no 1's are present then the dice totals are added up and printed.
    while turn_total < goal:
        computer_roll = roll_dice()
        if computer_roll.count(1) == 2:
            return 0
        elif 1 in computer_roll:
            return game_score
        else:
            turn_total += sum(computer_roll)
            print("computer rolled ", computer_roll, "Turn total ", turn_total)
    return game_score + turn_total


def human_turn(game_score):
    turn_total = 0
    roll_again = "y"
    while "y" == roll_again:
        human_roll = roll_dice()
        if human_roll.count(1) == 2:
            return 0
        elif 1 in human_roll:
            return game_score
        else:
            turn_total += sum(human_roll)
            print("You rolled ", human_roll, "Turn total ", turn_total)
        if game_score + turn_total >= 100:
            return game_score
        else:
            validate_response("roll_again(y/n)?", 'y', 'n')
    return game_score + turn_total


def validate_response(prompt, response_1, response_2):
    prompt = input(prompt).lower()
    while prompt != response_1 and prompt != response_2:
        print(f'Response not valid, try {response_1} or {response_2}.')
        prompt = input().lower()
    return prompt, response_1, response_2


def human_vs_computer():
    human_score = 0
    computer_score = 0
    while human_score < 100 and computer_score < 100:
        human_score = human_turn(human_score)
        computer_score = computer_turn(computer_score, 20)
        print("You:", human_score, "Computer:", computer_score)
    if human_score >= 100:
        print("You win!")
    else:
        print("Computer wins :(")


def computer_solo(goal):
    score = 0
    turns = 0
    while score < 100:
        score = computer_turn(score, goal)
        turns += 1
        print('Turn:', turns, 'Score:', score)
        if score > 100:
            print('Turns:', turns)
            return turns


def world_championship(games, goal_1, goal_2):
    game_total = games
    totes_not_robot = 0
    swear_im_human = 0
    computer1_wins = 0
    computer2_wins = 0
    while game_total != 0:
        if totes_not_robot > 100:
            computer1_wins += 1
            game_total -= 1
            print("totes_not_robot:", totes_not_robot, "swear_im_human:", swear_im_human)
            swear_im_human -= swear_im_human
            totes_not_robot -= totes_not_robot
        elif swear_im_human > 100:
            computer2_wins += 1
            game_total -= 1
            print("totes_not_robot:", totes_not_robot, "swear_im_human:", swear_im_human)
            swear_im_human -= swear_im_human
            totes_not_robot -= totes_not_robot
        totes_not_robot = computer_turn(totes_not_robot, goal_1)
        swear_im_human = computer_turn(swear_im_human, goal_2)
    print("totes_not_robot:", computer1_wins, "Wins", "swear_im_human:", computer2_wins, "Wins")
    return computer1_wins, computer2_wins


if __name__ == '__main__':
    pass
    #human_vs_computer()
    #human_turn(10)
    #validate_response("Does this work (t/f)?",'t','f')
