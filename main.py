import random
class Rooms():
    def __init__(self, name):
        self.state = 0
        self.name = name
    
    def cleaning(self, state):
        self.state = state

class Robot():
    
    def __init__(self):
        self.location=""
        self.l=[]


    def temizle(self, oda):
        if self.location==oda.name:
            if oda.state == 1:
                self.l.append(oda.name)
                self.l.append("dirty")
                print("Kirli Oda Temizleniyor")
                oda.cleaning(0)
                self.l.append("clean")
                return "cleaning"
                
            else:   
                self.l.append(oda.name)
                self.l.append("clean")
                print("Oda temiz")
                return ""

    def git(self, oda):
        self.location=oda.name
        return self.temizle(oda)
        


def main():
    a=Rooms("a")
    b=Rooms("b")
    robot=Robot()
    aState=0
    bState=0
    while (True):
        if(a.state==0):
            aState=random.randint(0,1)
        if(b.state==0):
            bState=random.randint(0,1)
        #print(aState,"  ", bState)
        a.cleaning(aState)
        b.cleaning(bState)
        rGit=random.randint(0,1)
        if(rGit==0):
            c=robot.git(a)
            print("A odasina Git")
        else:
            c=robot.git(b)
            print("B odasina Git")
        
        

        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye.. Bye..")
