import sys

argvs = sys.argv
argc = len(argvs)
val=[]
for line in sys.stdin:

    items = line.split("||")
    Flag=True
    for x in items:
        try:
            x_name,x_ele = x.strip("\n").split("=")
            if x_name == "SOURCE_PORT":
                try:
                    if int(x_ele)<1024:
                        Flag=False
                        break
                except:
                    pass

            if x_name == "SOURCE_IP":
                try:
                    ip_1,ip_2,ip_3,ip_4 = x_ele.split(".")
                    ip_4 = "0"
                    x_ele = ".".join([ip_1,ip_2,ip_3,ip_4])
                except:
                    pass    

            for y in argvs:
                if x_name == y:
                    val.append(x_ele)
        except:
            pass
    if len(val) !=0:
        val.append("=1")
        if Flag == True:
            print "   ".join(val)
    val=[]
