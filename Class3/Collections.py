# Collections:

    # 1. List
    # 2. Tuple
    # 3. Set
    # 4. Dictionary

# 1. List:

    # fruits = ["apple", "banana", "cherry", "date", "berry"]
    #           0        1         2         3        4     --> forward indexing
    #          -5       -4        -3        -2       -1     --> backward indexing
    #                                                           Range of indexing: [1:3]

    # print(fruits)
    # print(type(fruits))
    # print(len(fruits))
    # print(fruits[0])
    # print(fruits[-3])
    # print(fruits[-3:])

    # fruits.append("grapes")
    # fruits.insert(1, "grapes")
    # fruits.extend(["grapes", "kiwi", "mango"])

    # fruits.remove("banana")
    # fruits.pop(2)
    # fruits.clear()
    # del fruits
    # print(fruits)

# 2. Tuple:

    # fruits = ("apple", "banana", "cherry", "date", "berry")

    # print(fruits)
    # print(type(fruits))
    # print(len(fruits))
    # print(fruits[0])
    # print(fruits[-3])
    # print(fruits[-3:])  


# 3. Set

    # fruits = {"apple", "banana", "cherry", "date", "berry"}

    # print(fruits)
    # print(type(fruits))
    # print(len(fruits))
    # print("banana" in fruits)


# 4. Dictionary:

    # student = {
    #     "name": "John",
    #     "age": 20,
    #     "grade": "A",
    #     "subjects": ["Math", "Science", "History"],
    #     "address": {
    #         "street": "123 Main St",
    #         "city": "Anytown",
    #     }
    # }

    # print(student)
    # print(type(student))
    # print(len(student))
    # print(student["name"])
    # print(student["subjects"])
    # print(student["address"]["city"])

    # student["age"] = 35
    # student["phone"] = "123-456-7890"
    # student.update({"age": 35, "phone": "123-456-7890"})

    # student.pop("grade")
    # student.popitem()
    # student.clear()

    # print(student)