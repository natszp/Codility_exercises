# https://app.codility.com/programmers/trainings/5/three_letters/


import random
def three_letters(a, b):
    string = ''

    if a != 0 and b != 0:
        for i in range(a):
            string += 'a'
        for j in range(b):
            string += 'b'

    if len(string) > 4:
        for k in range(len(string)):
            while 'aaa' in string or 'bbb' in string:
                string = ''.join(random.sample(string, len(string)))
            return string