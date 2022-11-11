from listreduce import reduce_list, average
from dice import roll_result, throw_dice, throw_dice2
from secretcode import toss_coin, luck


dice1 = throw_dice()
print(int(dice1))
dice2 = throw_dice2()
print(int(dice2))
result = roll_result(dice1, dice2)
print(result)

numbers = [1,2,15,7,2]
print(reduce_list(numbers))
print(average(reduce_list))

secret_codes= [1,2,3,4,5]
print(toss_coin())
print(luck(toss_coin, secret_codes))