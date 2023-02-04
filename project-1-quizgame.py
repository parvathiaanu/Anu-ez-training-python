

q1=""" who is not in BTS?
a.rm
b.jhope
c.jin
d.kai"""
q2=""" which is not an animal
a.cow
b.deer
c.crow
d.chinnu"""
q3="""who is not dumb
a.female lead
d.second lead
c.writer
d.kdrama lovers"""
q4="""who is stupid
a.myfrnds
b.levi
c.light
d. l"""
q5="""baku marrys who
a.deku
b.kirishima
c.me
d.todoroki"""
questions ={q1:"d",q2:"c",q3:"c",q4:"a",q5:"c"}
name=input("hi whats ur name")
print("hello",name,"welcome")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do want to skip(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter ur ans")
    if(ans==questions[i]):
        print("correct!!")
        score=score+1
        print("your current score is ",score)
    else:
        print("wrong: u lost 1 point")
        score=score-1
        print("your current score is ",score)
    flag2=input("do want to quit(yes/no)")
    if flag2=="yes":
        break
print("your final score is :",score)
    
