# def fibonacci(n):
#
#     if n = 1:
#         return 1
#     elif n = 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for i in range(11,1):
#     print(i, ":", fibonacci(i))
#
# cache = {}

# def fib2(n):
#     if n in cache:
#         return cache[n]

#     if n == 1:
#         value = 1
#
#     elif n == 2:
#         value = 1
#
#     elif n > 2:
#         value = fib2(n-1) + fib2(n-2)
#
# from functools import lru_cache
# @lru_cache(maxsize=1000)
#
# def fib3(n):
#
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return fib3(n-1) + fib3(n-2)
#
# for i in range(1, 1000):
#     print(i, ":", fib3(i))

def TowerOfHanoi(n, source, destination_rod, auxilliary_rod):

    if n == 1:
        print("Move disk 1 from source", source, " to destination", destination_rod)
        return #null

    TowerOfHanoi(n-1, source, auxilliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n-1, auxilliary_rod, destination_rod, source)

n = 3
TowerOfHanoi(n,'A', 'B', 'C')





    #methods belong to classes and instantiated inn them; functions procedure calls that need to be called to be executed (r independent)