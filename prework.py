 def hello_name(user_name):
     print("Hello," + user_name.title())
hello_name("Andrew")

def odd_numbers():
    for num in range(1,100,2):
        print(num)
# print(odd_numbers())

# max number in a list

def max_num_in_list(a_list):
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max
# print(max_num_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def is_leap_year(a_year):
    a_year = int(input("Enter The Year:"))
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                print("Is a leap year")
            else:
                print("Is not a leap year")

def is_consecutive(a_list):
    i = 0
    status = True while i < len(a_list)