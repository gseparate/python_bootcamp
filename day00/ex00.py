import sys

if(len(sys.argv) != 2):
    print("index out of range", len(sys.argv))
    sys.exit(0)
for i in range(int(sys.argv[1])):
    try:
        str = input()
        if(len(str) == 32 and str[:5] == '0' * 5 and str[5] != '0'):
            print(str)
    except EOFError:
        print("end of file")
        break
