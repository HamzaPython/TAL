import sys
import numpy

class FonctionWer:

    def __init__(self,r,h):
	self.r=r
	self.h=h

    def distance(self,r,h):

        d =numpy.zeros((len(self.r)+1)*(len(self.h)+1)).reshape((len(self.r)+1,len(self.h)+1))
        for i in range(len(self.r)+1):
            for j in range(len(self.h)+1):
                if i==0:
                    d[0][j]=j
                elif j==0:
                    d[i][0]=i
        for i in range(1,len(self.r)+1):
            for j in range(1,len(self.h)+1):
                if self.r[i-1]==self.h[j-1]:
                    d[i][j]=d[i-1][j-1]
                else:
                    substitute=d[i-1][j-1]+1
                    insert=d[i][j-1]+1
                    delete=d[i-1][j]+1
                    d[i][j]=min(substitute,insert,delete)
        return d

    def getStepList(self,r,h,d):

        x=len(self.r)
        y=len(self.h)
	self.d=self.distance(self.r,self.h)
        list=[]
        while True:
            if x==0 and y == 0:
                break
            elif (self.d[x][y]==self.d[x][y-1]) and (self.r[x-1] == self.h[y-1]) and (x>=1 and y>=1):
                list.append("e")
                x=x
                y=y-1
            elif self.d[x][y]==self.d[x][y-1]+1 and y >= 1:
                list.append("i")
                x = x
                y = y - 1
            elif self.d[x][y] == self.d[x-1][y-1]+1 and x >= 1 and y >= 1:
                list.append("s")
                x = x - 1
                y = y - 1
            else:
                list.append("d")
                x = x - 1
                y = y
        return list[::-1]

    def alignedPrint(self,list, r, h, result):

        
        for i in range(len(list)):
            if list[i]=="i":
                count =0
                for j in range(i):
                    if list[i]=="d":
                        count+=1
                index=i-count

                print("" *(len(self.h[index])));
            elif list[i]=="s":
                count1 = 0
                for j in range(i):
                    if list[j] == "i":
                            count1+=1
                index1=i-count1
                count2=0
                for j in range(i):
                    if list[j]=="d":
                        count2+=1
                index2=j-count2

              
            else:
                       count=0
                       for j in range(i):
                           if list[j]=="d" :
                               count+=1
                       index=1-count
                       
        
        for i in range(len(list)):
                       if list[i]=="d":
                           count =0
                           for j in range(i):
                               if list[j]=="i" :
                                   count+=1
                           index =i-count

                          
                       elif list[i] == "i" :
                            count1=0
                            for j in range(i):
                                if list[j] == "d":
                                   count += 1
                            index = i - count
                            
                       elif list[i] == "s":
                            count1 = 0
                            for j in range(i):
                                if list[j] == "i":
                                    count1 += 1
                            index1 = i - count1
                            count2 = 0
                            for j in range(i):
                                if list[j] == "d":
                                   count2 += 1
                            index2 = i - count2
                           
                       else :
                             count = 0
                             for j in range(i):
                                 if list[j] == "i":
                                       count += 1
                             index = i - count
                          
        print("WER: " + result);
	
    def wer(self, r, h):
        d=self.distance(self.r,self.h)
        list=self.getStepList(self.r,self.h,d)
        result = float(d[len(self.r)][len(self.h)]) / len(self.r) * 100
        result = str("%.2f" % result) + "%"
        self.alignedPrint(list, self.r, self.h, result)


 
var1="khalid is nice"
var2="khalid is beautiful"
valeur1 = var1.split()
valeur2 = var2.split()
ob=FonctionWer(valeur1, valeur2)
	#r=var1
        #h=var2
ob.wer(valeur1,valeur2)
   
              
