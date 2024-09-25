W = {
    "rock": ["lizard", "scissors"],
    "paper": ["spock", "rock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}
def rpsls(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 not in W or p2 not in W:
        return "Please select an option"
    if p2 in W[p1]:
        return "Player 1 Won!"
    if p1 in W[p2]:
        return "Player 2 Won!"

    return "Draw!"
print(rpsls("SCISSORS",'PAPER'))