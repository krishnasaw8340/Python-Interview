1. Difference b/t list and tupple or list and array:
==>  List:
  list - List is mutable
  list [ 'a','b','c',1,2,3]
  list iteration is slower
  list consumes more memory
  Operation like insertion, deletion are better performed:
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)

Tuple:
tuple are immutable
tuple is also similar to list but contains immutable objects
tuples = ('a', 'b', 1,2)
tuple processing is faster than list
tuple cotains less memory
elements can be accessed better:

** We can change the value of tuple after converting into list: **
my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)


