def calculator(first_number,second_number,operation):
    if operation=="+":
        return first_number+second_number
    elif operation=="-":
        return first_number-second_number
    elif operation=="*":
        return first_number*second_number
    elif operation=="/":
        return first_number/second_number

first_number=int(input())
second_number=int(input())
operation=input()
result=calculator(first_number,second_number,operation)
print("Result:",result)
