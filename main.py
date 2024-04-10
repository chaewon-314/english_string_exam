import random
import keyboard

list1=['where nature allowed people to escape their disadvantages','IN fact it is the very opposite','that elites regress inexorably to the mean overtime','do little to make up for their children\'s genetic mediocrity']
list2=['in causing us not to think certain things','Once you have locked on to a decision-making problem','in order to get on with making the next incoming decision','in order to get on with making the next incoming decision']
list3=['Rather than focus only on the biological features of a disease','as well as the behaviour of its human patients','should account for the history of infection within a population']
list4=['have found, this is not the case','ended up with less cash than their victim','whether the thief ended up better off than the victim','harming someone who had unfairly advanced']
list5=['extends into what humans call the ultrasonic','Such high-frequency sounds travel very poorly in air','For animals that interact on larger scales','reflects the varied ecologies of each species']
list6=['where few legal restrictions prevail','there is no guarantee that they will be treated well','that is missing from such debates']
list7=['call attention to differences in what is right','not if done by someone who lacks','impose the obligation to save a drowning man']
list8=['The success of science is better accounted for','Earth\'s orbit around the sun is circular','Despite the fact that the theories were false']
list9=['which he famously did best while working alone','manner reminiscent of what goes on','but might also inspire a nuanced appreciation of its rewards']
list=[list1,list2,list3,list4,list5,list6,list7,list8,list9]

boolean=True
 
while boolean:
    r1=random.randrange(1,9)
    mainlist=list[r1]
    r2=random.randrange(1,len(mainlist))
    string=mainlist[r2]
    problem=string.split(' ')
    print(problem)
    answer=input('답 입력')
    if answer==string:
        print('정답!')
    elif answer=='quit':
        boolean=False
    else:
        print('오답!')
        print(string)
        print(answer)

