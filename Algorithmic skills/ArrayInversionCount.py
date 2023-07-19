 #https://app.codility.com/programmers/trainings/4/array_inversion_count/

def solution(array):

    new_list = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                new_list.append((array[i], array[j]))

    return len(new_list)

 # Total score by codility - 63%