# from audioop import reverse
# from calendar import firstweekday
#
#
# #task 1
# def prtxt():
#     print("""“Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”""")
#
# prtxt()
# #task2
# def pri_even(num1,num2):
#     [print(i) for i in range(num1,num2+1) if i%2==0]
#
#
# pri_even(3,10)
#
#
# #task 3
# def do_square(lenght,symb,fill=True):
#     if not fill:
#         symb=0
#     matrix=[[symb for j in range(lenght)] for i in range(lenght)]
#     for row in matrix:
#         print(row)
#
# do_square(4,"S",True)
#
#
# #task 4
# # решил для интереса сделать без мин и произвольным количеством аргументов
# def find_min(*numbers):
#     min_num= float("inf")
#     for i in  numbers:
#         if i<=min_num:
#             min_num=i
#
#     return min_num
#
# print(find_min(11,51,22,33,40,10))
#
# # второй вариант если первый не устроит
# # как по условию
#
# def min_find (num1,num2,num3,num4,num5):
#     return  min(num1,num2,num3,num4,num5)
#
#
#
# #task 5
#
#
# def get_pr_numbers(start,end):
#     pr=1
#     if end<start:
#         end,start=start,end
#     for i in range(start,end):
#         pr*=i
#     return pr
# print(get_pr_numbers(4,1))
#
# #task 6
# def get_len_numb(num):
#     return len(str(num))
# print(get_len_numb(3233))

#task 7

def check_palindrom(chislo):
    first = str(chislo)[:3]
    second = str(chislo)[3:]
    if first == second[-1::-1]:
        return True
    else: return False

print(check_palindrom(123321))


