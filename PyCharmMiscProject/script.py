import numpy as np
import matplotlib.pyplot as plt
#Cau 1
def print_name(string):
    for i in string:
        print(i, end="")
    print('\n')

#Cau 2
def print_odd():
    for num in range(1,10):
        if num%2==1:
            print('Odd numbers: ', num)

#Cau 3a
def sum_numbers_in_2():
    sum=0
    for num in range(1, 11):
        if num % 2 == 1:
            sum=sum+num
    return sum

#Cau 3b
def sum_numbers():
    sum=0
    for num in range(1,7):
        sum=sum+num
    return sum

#Cau 4
def print_dict(type):
    mydict = {'a': 1,'b':2,'c':3,'d':4}
    if type=='keys':
        print(mydict.keys())
    if type=='values':
        print(mydict.values())
    if type=='items':
        print(mydict.items())

#Cau 5
def print_sequence():
    courses = [131, 141, 142, 212]
    names = ['Maths', 'Physics', 'Chem', 'Bio']
    zipped = zip(courses, names)
    for course, rank in zipped:
        print(course, rank)

#Cau 6
def print_num_consonants(type):
    sum=0
    vowels = "aeiou"
    if type=='non_con':
        for char in "jabbawocky":
            if char in vowels:
                sum+=1
    if type == 'con':
        for char in "jabbawocky":
            if char not in vowels:
                continue
        sum += 1
    print(sum, "consonants found")

#Cau 7
def print_try_ex():
    for a in range(-2, 3):
        try:
            print(10 / a)
        except ZeroDivisionError:
            print("Can't divide by zero!")

#Cau 8
def print_lambda():
    ages = [23, 10, 80]
    names = ["Hoa", "Lam", "Nam"]
    data = zip(ages, names)
    print(sorted(data, key=lambda x: x[0]))

#Cau 9
def readinfile(type):
    if type=='non_read':
        input_file = open("firstname.txt")
        for line in input_file:
            print(line, end='')
        input_file.close()
    if type == 'read':
        input_file = open("firstname.txt")
        first_names = input_file.read()
        input_file.close()
        print(first_names)

#Define
#Cau 1
def sum_int(a,b):
    return a+b

#Cau 2
def matrix():
    M = np.arange(1,10).reshape((3, 3))
    v=np.arange(1,4)
    print('Matrix M = ', M)
    print('Vector v = ', v)

#Cau 3
def matrix_new():
    M = np.arange(1, 10).reshape((3, 3))+3
    print('Matrix M = ', M)

#Cau 4
def matrix_transpose():
    M = np.arange(1, 10).reshape((3, 3))
    v = np.arange(1, 4)
    M_transpose=M.transpose()
    v_transpose=v.transpose()
    print(M_transpose)
    print(v_transpose)

#Cau 5
def norm_vector():
    x=np.array([2,7])
    x_norm=np.linalg.norm(x)
    print(x_norm)
    print(x/x_norm)

#Cau 6
def compute_matrix():
    a = np.array([10,1])
    b = np.array([8,2])
    c = np.array([1,2,3])
    try:
        print(a+b)
    except ValueError:
        print('Can`t work')
    try:
        print(a-b)
    except ValueError:
        print('Can`t work')
    try:
        print(a-c)
    except ValueError:
        print('Can`t work')

#Cau 7
def dot_product():
    a = np.array([10, 1])
    b = np.array([8, 2])
    dot = np.dot(a, b)
    print("Dot Product of Vector_a and Vector_b:", dot)

#Cau 8
def matr():
    A =np.array([[2, 4, 9], [3, 6, 7]]).reshape(2,3)
    print(A[1,2])
    return(A[:,1])

#Cau 9
def ran_matr():
    x = np.random.randint(-10,10, size=(3, 3))
    print(x)

#Cau 10
def iden_mat():
    x=np.eye(3,3)
    print(x)

#Cau 11
def trac_mar():
    x = np.random.randint(1, 10, size=(3, 3))
    trace_x=np.trace(x)
    print('With the command: ', trace_x)
    trace_sum=0
    for i in range(3):
        trace_sum+=x[i,i]
    print('Without the command: ', trace_sum)

#Cau 12
def diagmo():
    a = np.matrix([1, 2, 3])
    a_diag = np.diag(a)
    print(a_diag)

#Cau 13
def det_matr():
    A =np.array([[1, 1, 2], [2, 4, -3], [3, 6, -5]])
    A_det=np.linalg.det(A)
    print(A_det)

#Cau 14
def stack_col():
    a1 =np.array([1, -2, -5])
    a2 =np.array([2, 5, 6])
    a=np.column_stack((a1,a2))
    print(a)

#Cau 15
def Simply_plot():
    y=np.arange(-5,6)
    y=y**2
    plt.plot(y, marker='d', color='blue')
    plt.title("Waveform")
    plt.ylabel('Amplitude')
    plt.xlabel("Time")
    plt.savefig("waveform.png")
    plt.show()

if __name__ == '__main__':
    print('Cau 1: \n')
    print_name('Hoang Minh Hiep')
    print('Cau 2: \n')
    print_odd()
    print('Cau 3a: \n')
    print('Sum of the 2/: ', sum_numbers_in_2())
    print('Cau 3b: \n')
    print('Sum from 1 to 6: ', sum_numbers())
    print('Cau 4a: \n')
    print_dict('key')
    print('Cau 4b: \n')
    print_dict('values')
    print('Cau 4c: \n')
    print_dict('items')
    print('Cau 5: \n')
    print_sequence()
    print('Cau 6a: \n')
    print_num_consonants('non_con')
    print('Cau 6b: \n')
    print_num_consonants('con')
    print('Cau 7: \n')
    print_try_ex()
    print('Cau 8: \n')
    print_lambda()
    print('Cau 9a: \n')
    readinfile('read')
    print('Cau 9b: \n')
    readinfile('non_read')
    print('Cau 1: \n')
    print(sum_int(3,4))
    print('Cau 2: \n')
    matrix()
    print('Cau 3: \n')
    matrix_new()
    print('Cau 4: \n')
    matrix_transpose()
    print('Cau 5: \n')
    norm_vector()
    print('Cau 6: \n')
    compute_matrix()
    print('Cau 7: \n')
    dot_product()
    print('Cau 8: \n')
    print(matr())
    print('Cau 9: \n')
    ran_matr()
    print('Cau 10: \n')
    iden_mat()
    print('Cau 11: \n')
    trac_mar()
    print('Cau 12: \n')
    diagmo()
    print('Cau 13: \n')
    det_matr()
    print('Cau 14: \n')
    stack_col()
    print('Cau 15: \n')
    Simply_plot()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
