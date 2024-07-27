error = -1
result = True
for i in range(4):
    try:
        str = input()
        if((len(str) != 5)):
            error = 1
            break
        if((i == 0 and (str.count(str[0]) != 2 or str[0] != str[-1])) or
            (i == 1 and (str.count(str[0]) != 4 or str[0] == str[2])) or
            (i == 2 and (str.count(str[0]) != 3 or str[0] != str[-1] != str[2]))):
            result = False
    except EOFError:
        error += 1

if(error):
    print("error")
    exit(0)
print(result)

