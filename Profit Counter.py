class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])
            print("Investment: "+str(array[idx])+"; Profit: "+str(profit))
            self.print(array,idx+1)
        else:
            return
 

    def calcProfit(self,investment):
        if investment <= 25000:
            return float(0)
        if investment <= 100000 and investment >= 25000:
            return float(3375)
        return float(800 + self.calcProfit(investment-10000))
        
 

#Tester
array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)