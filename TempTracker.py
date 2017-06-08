class TempTracker:

    def __init__(self):
        self.temps=[]

    def insert(self,temp):
        self.temps.append(temp)
        
    def getMax(self):
        print("Max is: ",sorted(self.temps)[-1])

    def getMin(self):
        print("Min is: ",sorted(self.temps)[0])

    def getMean(self):
        cur_tot,avg=0,0
        no_of_vals = len(self.temps)-1
        for num in self.temps:
            cur_tot+=num

        avg = float(cur_tot)/no_of_vals
        print("Meadian is :", avg)
               
    
    def getMode(self):
        cur_index=0
        count=1
        for i in range(len(self.temps)):
            if(count==0):
                cur_index=i
                count=1
            elif(self.temps[i]==cur_index):
                count+=1
            else:
                count-=1

        print("Mode is: ", self.temps[cur_index])
        

t1 = TempTracker()
t1.insert(90)
t1.insert(14)
t1.insert(87)
t1.insert(162)
t1.insert(84)
t1.insert(109)
t1.getMax()
t1.getMin()
t1.getMean()
t1.getMode()
