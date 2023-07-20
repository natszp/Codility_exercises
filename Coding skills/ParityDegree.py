
# https://app.codility.com/programmers/trainings/5/parity_degree/

def solution(number):
    list_of_numbers = []

    if number and type(number) == int and number > 0:
        for i in range(1, number):
            if number % 2 ** i == 0:
                list_of_numbers.append(i)

        return max(list_of_numbers)

