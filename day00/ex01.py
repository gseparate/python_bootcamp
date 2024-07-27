import sys

if(len(sys.argv) != 2):
    print("index out of range", len(sys.argv))
    sys.exit(0)
for i in range(len(sys.argv[1])):
    if(i == 0 or sys.argv[1][i-1] == " " or sys.argv[1][i-1] == "\n"):
        print(sys.argv[1][i].capitalize(), end="")
print()