from game_data import data
import random
from art import logo,vs


def format_account(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr},from {account_country}"

def check_answer(user_guess,a_account,b_account):
    if a_account > b_account:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
should_continue = True
score = 0
account_b = random.choice(data)

while should_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

        print(f"compare a :{format_account(account_a)}")
        print(vs)
        print(f"against b :{format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n"*20)
        print(logo)

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        is_check = check_answer(guess,a_follower_count,b_follower_count)

        if is_check:
            score+=1
            print(f"you guessed it right{guess}")
        else:
            print(f"your answer is wrong your current score is {score}")
            should_continue = False

