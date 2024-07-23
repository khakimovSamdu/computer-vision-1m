# from math import gcd
# n, m = map(int, input().split())
# df = gcd(n, m)
# fh = n*m
# print(abs(fh)//df)

# s = input()
# if s.isalpha():
#     if s.isupper():
#         print(s.lower())
#     else:
#         print(s.upper())
# else:
#     print(s)

# def count_circles(n):
#     dic = {
#         '0': 1, '1': 0, '2': 0, '3': 0, '4': 0,
#         '5': 0, '6': 1, '7': 0, '8': 2, '9': 1
#     }
#     c = 0
#     for i in n:
#         c += dic[i]
#     return c
# n = input().strip()
# print(count_circles(n))

# s = input()
# u, l, d = 0, 0, 0
# for i in s:
#     if i.isupper():
#         u+=1
#     if i.islower():
#         l += 1
#     if i.isdigit():
#         d += 1
# if len(s)>=12 and u>0 and l>0 and d>0:
#     print('Yes')
# else:
#     print('No')

# s = input()
# c = 0
# ls = []
# for i in range(len(s)-1):
#     if s[i]=='0' and s[i+1]=="0":
#         c+=1
#     else:
#         ls.append(c)
#         c = 0
# ls.append(c)
# if len(s)>1 and ls[-1]=='0' and ls[-2]=='0':
#     ls[-1]+=1
# print(max(ls)+1)

# def nol_number(s):
#     ma = 0
#     c = 0
#     for i in s:
#         if i == '0':
#             c += 1
#         else:
#             if c > ma:
#                 ma = c
#             c = 0
#     if c > ma:
#         ma = c
#     return ma
# print(nol_number(input()))

# s = input()
# ls = s.split('.')
# c = 0
# for i in ls:
#     if int(i)>=0 and int(i)<=255:
#         c+=1
# if len(ls)==4 and c==4:
#     print('Good')
# else:
#     print('Bad')

# def is_valid_ip(ip: str):
#     ls = ip.split('.')
#     if len(ls) != 4:
#         return False
#     for item in ls:
#         if not item.isdigit():
#             return False
#         if not (0 > int(item)) and not (int(item)< 255):
#             return False
#         if len(item) > 1 and item[0] == '0':
#             return False
#     return True
# s = input()
# df = is_valid_ip(s)
# if df:
#     print('Good')
# else:
#     print('Bad')
# print('00'.isdigit())

# s = input()
# ls = s.split()
# a1 = int(ls[1])

# s = input().strip()
# a, operator, b, equal_sign, c = s
# if a == 'x':
#     if operator == '+':
#         x = int(c) - int(b)
#     elif operator == '-':
#         x = int(c) + int(b)
# elif b == 'x':
#     if operator == '+':
#         x = int(c) - int(a)
#     elif operator == '-':
#         x = int(a) - int(c)
# elif c == 'x':
#     if operator == '+':
#         x = int(a) + int(b)
#     elif operator == '-':
#         x = int(a) - int(b)
# print(x)
# n = int(input())
# l = 'G'
# c = 'C'
# r = 'V'
# for day in range(n):
#     temp = r
#     r = c
#     c = temp
    
#     temp = l
#     l = c
#     c = temp

# order = l + c + r
# print(order)

# e = 2.7182818284590452353602875
# n = int(input())
# fd = f"{e:.{n}f}"
# print(fd)

# n = int(input())
# df = '{:b}'.format(n)
# print(str(df).count('1'))


# def convert_to_base(n, k):
#     digits = []
#     while n > 0:
#         digits.append(n % k)
#         n //= k
#     digits.reverse()  
#     return digits
# def product_of_digits(digits):
#     product = 1
#     for digit in digits:
#         product *= digit
#     return product
# def sum_of_digits(digits):
#     return sum(digits)
# n, k = map(int, input().strip().split())
# digits = convert_to_base(n, k)
# product = product_of_digits(digits)
# summation = sum_of_digits(digits)
# difference = product - summation
# print(difference)

# def reverse_binary(m):
#     bin_m = bin(m)[2:]
#     rev_m = bin_m[::-1]
#     n = int(rev_m, 2)
#     return n
# n = int(input())
# print(reverse_binary(n))

# def calculate_phone_bill(A, B, C, T):
#     if T <= A:
#         return T * B
#     else:
#         return A * B + (T - A) * C
# a, b, c, t = map(int, input().split())
# print(calculate_phone_bill(a, b, c, t))

# def is_uchburchak(a, b, c):
#     if a+b>c and b+c>a and a+c>b:
#         return True
#     else:
#         return False
# a, b, c = map(int, input().split())
# data = is_uchburchak(a, b, c)
# if data:
#     print("YES")
# else:
#     print("NO")


