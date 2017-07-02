id=int(input("sr"))
id_list=[]
while 1>0:
    id_list.append(id%10)
    id = id // 10
    if (id-9)<=0:
        id_list.append(id)
        break
# e=(d[0]*2+d[1]*4+d[2]*8+d[3]*5+d[4]*10+d[5]*9+d[6]*7+d[7]*3+d[8]*6+d[9]*1+d[10]*2+d[11]*4+d[12]*8+d[13]*5+d[14]*10+d[15]*9+d[16]*7)%11
jiaoyan=[2,4,8,5,10,9,7,3,6,1,2,4,8,5,10,9,7]
last_number=0
for i in range(17):
    last_number+=id_list[i]*jiaoyan[i]
dict={0:1,1:0,2:'x',3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:20}
print(dict[last_number%11])