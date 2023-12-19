numlist = eval(input("Ente a list of integers: "))
even = list(filter(lambda x: x%2==0, numlist))
print(even) 
odd = list(filter(lambda y: y%2!=0, numlist))
print(odd)
even = filter(lambda x: x%2==0, numlist)
print(even)
 #observe the result. Thus, list is required
even = list(lambda x: x%2==0 for x in numlist)
print(even)
# even = lambda x:x%2==0 for x in numlist - does not compile
#lesson: filter function is required to print the numbers, otherwise address is printed
#also, list can accept at most one argument only.
#thus, for this kind of coding, list, filter and lambda are required.