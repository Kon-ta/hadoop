import sys

argvs = sys.argv
argc = len(argvs)
val=[]
for line in sys.stdin:
    num=0
    items = line.split("||")

    for x in items:

        x_name,x_ele = x.strip("\n").split("=")
        for y in range(1,argc):
            if x_name == argvs[y]:
                    val.append(x_ele)
    for x in val:
        print(x),
    print(": 1")
    val=[]
