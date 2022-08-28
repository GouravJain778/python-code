import random
class jumble():
    def __init__(self):
        self.score=0



    def choose(self):
        words = ['rainbow', 'computer', 'science', 'programming',
                'mathematics', 'player', 'condition', 'reverse',
                'water', 'board', 'geeks']

        pick = random.choice(words)
        return pick

    def suffel_word(self,word):
        # print(word)
        j=random.sample(word,len(word))
        x="".join(j)

        print("jumble word : ",x," Please correct it!!")

        while True:
            n=input()
            if word!=n:
                self.score=self.score-1


                print('try agein',self.score)
            else:
                self.score=self.score+1
                print('correct ans!',self.score)
                break
    def write_word(self):
        score=0

        while True:
            print("Start game by type c or quit the game with q")
            n=input().lower()
            if n=='q':
                print("exit")
                break
            elif n== 'c':
                i=self.choose()
                self.suffel_word(i)
            else:
                print("worng choice")       
ob=jumble()
ob1 =jumble()
ob.write_word()
ob1.write_word()








    


        






            
