name1=input("enter:").lower()
name2=input("enter:").lower()
name1=name1.replace(" "," ")
name2=name2.replace(" "," ")
print(name1)
print(name2)
for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,'',1)
            name2=name2.replace(j,'',1)
count=len(name1+name2)
print(count)
if count>0:
    list=["friends","lovers","affectionate","enemies","sidilings"]
    while (len(list)>1):
        c=count%len(list)
        s_index=c-1
#slicing
        if s_index>0:
            left=list[:s_index]
            right=list[s_index+1:]
            list =right+left
        else:
            list=list[:len(list)-1]
    print("relationship:",list[0])
else:
    print("enter different names")
