# Exception handling:

try:
    # n = 9

    # result = n / 0

    # print(result)

    fruits = ["apple", "banana", "cherry"]
    #            0         1         2

    print(fruits[1])

except ZeroDivisionError as e:
    print("An error occurred: ", e)
except IndexError as e:
    print("An error occurred: ", e)
except Exception as e:
    print("An unexpected error occurred: ", e)
else:
    print("No errors occurred.")
finally:
    print("Done!")