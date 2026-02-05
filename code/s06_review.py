# for i in range(4):
#     print("Iteration:", i+1)
#     print("Square:", (i+1) * i)


# def double(number):
#     """Return double the input number"""
#     return number * 2

# print(double(5)) #Should print 10
# print(double("5")) #Should print 5, two times to get 55 or "5" "5"

a = 5 #Int is immutable
b = a
a = 10
print(b)
print(a)

a = [1, 2, 3]
b = a
a.append(4)
print(b) #Prints 1, 2, 3, 4
print(a) #Prints 1, 2, 3, 4

x = 10

def foo():
    message = "Hello"
    x = 5
    return x

print(foo())
print(x)
#print(message)

# def draw_square(size):
#     for i in range(size):
#         #print("🧱" * size)
#         for j in range(size):
#             print("🧱" * end = "")
#         print()

# draw_square(4)

# print("Hi", end = "")
# print("Hello")

# def draw_triangle():
#     for i in range(1, 5):
#         print("🧱" * i)

# draw_triangle()



#In row i, how many spaces are there? how many #s are there?

# def draw_reverse_triangle(size):
#     for i in range(size):
#         print(" " * (size - i - 1) + "#" * (i+1))

# draw_reverse_triangle(5)


# def draw_reverse_triangle(size):
#     for i in range(size):
#         print(" " * (size - i - 1) + "#" * (i+1))

# draw_reverse_triangle(5)


"""
Draw a Triangle

            i    s              #
    #       0    4  5-0-1 = 4   1  (0*2)+1 = 1 
   ###      1    3  5-1-1 = 3   3  (1*2)+1 = 3
  #####     2    2  5-2-1 = 2   5  (2*2)+1 = 5
 #######    3    1  5-3-1 = 1   7  (3*2)+1 = 7
"""

def draw_pyramid(size):
    for i in range(size):
        print(" " * (size - i - 1) + "#" * ((i*2)+1))

draw_pyramid(5)

