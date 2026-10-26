output = [ i for i in range(1,101) if str("{:b}".format(i)).count("0") == 1 ]

for i in output :
    print(f"{i} : {"{:b}".format(i)}")

print("합계 : ", sum(output))

numbers=[273,132,1,3,2313,12,31,3213,231]

for num in numbers:
    if num < 10 :
        length = 1
    if num < 100 :
        length = 2
    if num < 1000 :
        length = 3
    if num < 10000 :
        length = 4
    print(num,  "는",  length,  "자릿수입니다." )

