import random
import keyboard

list1=['where nature allowed people to escape their disadvantages','IN fact it is the very opposite','that elites regress inexorably to the mean overtime','do little to make up for their children\'s genetic mediocrity']
list2=['in causing us not to think certain things','Once you have locked on to a decision-making problem','in order to get on with making the next incoming decision']
list3=['Rather than focus only on the biological features of a disease','as well as the behaviour of its human patients','should account for the history of infection within a population']
list4=['have found, this is not the case','ended up with less cash than their victim','whether the thief ended up better off than the victim','harming someone who had unfairly advanced']
list5=['extends into what humans call the ultrasonic','Such high-frequency sounds travel very poorly in air','For animals that interact on larger scales','reflects the varied ecologies of each species']
list6=['where few legal restrictions prevail','there is no guarantee that they will be treated well','that is missing from such debates']
list7=['call attention to differences in what is right','not if done by someone who lacks','impose the obligation to save a drowning man']
list8=['The success of science is better accounted for','Earth\'s orbit around the sun is circular','Despite the fact that the theories were false']
list9=['which he famously did best while working alone','manner reminiscent of what goes on','but might also inspire a nuanced appreciation of its rewards']
list=[list1,list2,list3,list4,list5,list6,list7,list8,list9]

boolean=True
r1=0
r2=0
string=''

OXlist=[]
templist=[]
for x in range(len(list)):
    OXlist.append(['0']*len(list[x]))








def problemNumber():
    global boolean
    global r1

    while True:
        Pnumber=input('\n문제번호 입력(랜덤 출제는 그냥 엔터키)\n')
        print(Pnumber)
        if Pnumber=='1':
            r1=int(Pnumber)-1
        elif Pnumber=='2':
            r1=int(Pnumber)-1
        elif Pnumber=='3':
            r1=int(Pnumber)-1
        elif Pnumber=='4':
            r1=int(Pnumber)-1
        elif Pnumber=='5':
            r1=int(Pnumber)-1
        elif Pnumber=='6':
            r1=int(Pnumber)-1
        elif Pnumber=='7':
            r1=int(Pnumber)-1
        elif Pnumber=='8':
            r1=int(Pnumber)-1
        elif Pnumber=='9':
            r1=int(Pnumber)-1
        elif Pnumber=='q':
            boolean=False
        elif Pnumber=='':
            r1=random.randrange(0,8,1)
        
        else:
            print('올바르지 않은 입력입니다.')
            problemNumber()
        print(r1)
        break


def makeProblem():
    global string
    global r1
    global r2

#중복 방지 알고리즘(같은 문제번호에 대해서만)
    for y in range(len(OXlist)):
        w=0
        for z in range(len(OXlist[y])):
            if OXlist[y][z]=='1':
                w+=1
                print(w)
        if w==len(OXlist[y]):
            for z in range(len(OXlist[y])):
                OXlist[y][z]='0'

#중복방지 알고리즘(전체 문제에 대하여)(아직 안 만듬)

    mainproblem_list=list[int(r1)]
    r2=random.randrange(len(mainproblem_list))

    if OXlist[r1][r2]=='0':
        string=mainproblem_list[r2]
        problem=string.split(' ')
        random.shuffle(problem)
        print(problem)

        OXlist[r1][r2]='1'
    else:
        makeProblem()




def checkAnswer():
    global string   
    global r1
    global r2

    answer=input('답 입력')
    if answer==string:
        print('\n정답!\n')
        print('정답: '+string)
        print('답안: '+answer)
    else:
        print('\n오답!\n')
        print('정답: '+string)
        print('답안: '+answer)
        print()


while boolean:
    problemNumber()
    makeProblem()
    checkAnswer()