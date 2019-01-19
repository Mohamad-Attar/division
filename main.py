def division_function(n):
    list = n.split()
    list.reverse()
    # 1 is a neutral number for division
    result = 1
    for number in list:
        if number.isdigit():
            result = int(number) / result
    return result


if __name__ == "__main__":
    numbers = input("please enter your numbers\n")
    division = division_function(numbers)
    print (division)