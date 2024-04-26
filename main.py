#!/usr/bin/env python3

def main():
    score = 0

    ans = input("do you want to play my game\n")
    if ans=="yes":
        print("let's begin")
        q1=input("what is 3+9\n")
        if q1=="12" or q1=="twelve":
            print("correct")
            score+=1
        else:
            print("not correct")
            score-=0.25

        q2=input("what is the colour of the sky?\n")
        if q2=="blue":
            print("correct")
            score+=1
        else:
            print("not correct")
            score-=0.25
    else:
        print("okay bye")
    print("your score is %d" % score)
if __name__ == "__main__":
    main()

