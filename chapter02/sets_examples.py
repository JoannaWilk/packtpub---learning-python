small_primes = set()
print("empty set small_primes = set()")
print("small_primes:", small_primes)
small_primes.add(2)
print("add one element to the set by small_primes.add(2)")
small_primes.add(3)
print("add one element to the set by small_primes.add(3)")
small_primes.add(5)
print("add one element to the set by small_primes.add(5)")
print("small_primes:", small_primes)

print("---------------------------")
primes = {2, 3, 5, 5, 3}
print("create set by primes = {2, 3, 5, 5, 3}"
      "\nprimes:", primes)
print("---------------------------")

small_primes.add(1)
print("adding 1 by small_primes.add(1)"
      "\nsmall_primes:", small_primes)
small_primes.remove(1)
print("removing 1 by small_primes.remove(1)"
      "\nsmall_primes:", small_primes)

print("---------------------------")
print("3 in small_primes:", 3 in small_primes)
print("4 in small_primes:", 4 in small_primes)
print("4 not in small_primes:", 4 not in small_primes)

print("---------------------------")
small_primes.add(3)
print("adding another 3 by small_primes.add(3)"
      "\nsmall_primes:", small_primes,
      "\nnothing changed as duplication is not allowed")

print("---------------------------")
bigger_primes = set([5, 7, 11, 13])
print("\ncreate set by bigger_primes = set([5, 7, 11, 13])"
      "\nbigger_primes:", bigger_primes)
print("\nunion of small_primes and bigger_primes by"
      "\nsmall_primes | bigger_primes\n",
      small_primes | bigger_primes)
print("\nintersection of small_primes and bigger_primes by"
      "\nsmall_primes & bigger_primes\n",
      small_primes & bigger_primes)
print("\ndifference between small_primes and bigger_primes by"
      "\nsmall_primes - bigger_primes\n",
      small_primes - bigger_primes)
