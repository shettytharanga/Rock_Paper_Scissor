import random
def play():
    user = input("Do you want to choose rock(r) , paper(p) or scissors(s) ???")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It's a tie."
    if is_win(user,computer):
        return "You Win."
    return "you lost."
def is_win(player,computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
print(play())