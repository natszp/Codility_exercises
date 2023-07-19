  # https://app.codility.com/programmers/trainings/4/str_symmetry_point/

def solution(str):

    str_length = len(str)

    if str_length == 0 or str_length == 1:
        return 0

    if str_length % 2 == 0:
        return -1

    if str == str[::1]:
        return str_length//2


# Total score by Codility 50%