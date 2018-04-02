small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])

print("create frozenset by small_primes = frozenset([2, 3, 5, 7])"
      "\nsmall_primes:", small_primes)
print("create frozenset by bigger_primes = frozenset([5, 7, 11])"
      "\nbigger_primes:", bigger_primes)
print("try to add 11 to small_primes by small_primes.add(11)")
# small_primes.add(11)
print("it can not be done, as frozenset is immutable")
print("----------------")
print("try to remove 2 from small_primes by small_primes.remove(2)")
# small_primes.remove(2)
print("it can not be done, as frozenset is immutable")
print("----------------")
print("intersection of small_primes and bigger_primes by"
      "\nsmall_primes & bigger_primes\n",
      small_primes & bigger_primes)
print("\nintersect, union, etc. are allowed")
