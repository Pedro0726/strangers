# Interactions Between Functions Practice #3
# You must create a list with values and call it secret_codes.
secret_codes= [1,2,3,4,5]
# Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.
from random import randint 
def toss_coin():
  coin_toss = randint(1,2)
  if coin_toss %2 :
    coin_toss = "Heads"
  else:
    coin_toss = "Tails"
  return coin_toss
# Create a second function called luck, hat takes two arguments: the first must be the result of the coin toss. The second argument will be any list (the secret_codes variable that was created at the beginning).
def luck(toss_coin,secret_codes):
  if toss_coin() == "Tails":
    print("list will self destruct")
    secret_codes = []
    return secret_codes
  else:
    print("list was saved")
    return secret_codes 
# If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ].

# If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.

# Hint: Use the random library's choice method to choose an element at random from a sequence.