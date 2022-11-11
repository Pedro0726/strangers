# Interactions Between Functions Practice #2
# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the elements can be changed.

# For example, if given the list [1,2,15,7,2] it should return [1,2,7].

# Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values. It should return the result (a float), without printing it.
numbers = [1,2,15,7,2]
def reduce_list(numbers):
  list2 = [*set(numbers)]
  list2.remove(max(numbers))
  return list2

def average(reduce_list):
  list3 = sum(reduce_list(numbers)) / len(reduce_list(numbers))
  return list3
  