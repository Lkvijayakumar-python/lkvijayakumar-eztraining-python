q1=""" who is top 2 batsmen in ipl 2022?
a.rithuraj gaikwad
b.jos butler
c.faf duplesis
d.kl rahul"""

q2="""whos your favourite Batsmen?
a.Shreyas iyer
b.virat kohli
c.rohit sharma
d.SKY"""

q3="""which team won the most number of  ICC worldcups wins in cricket?
a.Newzeland
b.England
c.India
d.Australia"""

q4="""which team  has won the more number of IPL trophies?
a.Chennai super kings
b.Mumbai indians
c.sunrisers hyderabad
d.delhi capitals"""

q5=""" find the value of [5*(5+3)-8+10+(7*6)-14-(10*7)+2*4]
a.2
b.0
c.4
d.8"""

questions={q1:"d",q2:"a",q3:"d",q4:"b",q5:"d"}

name=input(" Hi whats ur name")
print("Hello","welcome to the quiz",name)
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question (yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter ur answer")
    if ans==questions[i]:
        print("wow!! you got one point")
        score=score+1
        print("your current score is: ",score)
    else:
        print("wrong answer,u lost one mare")
        score=score-1
        print("ur current score is: ",score)
    flag2=input("Do you want to quit?type(yes/no)")
    if flag2=="yes":
        break
print("ur total score is:",score)
