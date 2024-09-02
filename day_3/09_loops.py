# loops is used to repeat a block of code
# there are two types of loops
# 1. while loop
# 2. for loop

# while loop
# while loop is used to execute a block of code as long as a certain condition is true
# while loop is used to execute a block of code until a certain condition is true

# while loop
# x = 0
# while(x<5):
#     print(x)
#     x = x+1


# for loop

# for loop is used to execute a block of code for a certain number of times
# for loop is used to execute a block of code for a certain range of numbers

# for loop
for x in range(5):
    print(x)


# for loop with range
for x in range(5,10):
    print(x)

# for loop with step
for x in range(0,10,2):
    print(x)

# for loop with list
for x in [0,1,2,3,4,5]:
    print(x)

days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
for x in days:
    print(x)

# for loop with string
for x in "Noor":
    print(x)

# for loop with tuple
for x in (0,1,2,3,4,5):
    print(x)
    # tuple means it is not changeable
    # tuple is different from list because it is not changeable


# for loop with dictionary
for x in {"a":1,"b":2,"c":3}:
    print(x)
    