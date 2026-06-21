sales=0
sreturns=0
purchace=0
preturns=0
def netSales():
     print('--- Enter 0 to stop looping ---')  
     global sales,sreturns
     sales=0
     sreturns=0
     while True:
        sal=float(input('Enter the value of sale:'))
        if (sal==0):
             break
        sales=sales+sal

     n=int(input('Is there any returns (yes=1 or no=0):'))
     if (n==1):
         while True:
             ret=float(input('Enter the amount of returns:'))
             if(ret==0):
                break
             sreturns=sreturns+ret
     nsales=sales-sreturns
     return nsales
     
def netPurchase():
     print('---Enter 0 to stop looping ---')
     global purchace,preturns
     purchace=0
     preturns=0
     while True:
        pur=float(input('Enter the value of purchace:'))
        if (pur==0):
            break
        purchace=purchace+pur

     q=int(input('Is there any returns(yes=1 or no=0):'))
     if (q==1):
        while True:
             ret=float(input('Enter the value of return:'))
             if (ret==0):
                 break
             preturns=preturns+ret
     npurchase=purchace-preturns
     return npurchase

def coGs():
     ss=float(input('Enter the amount of starting stocks(if no enter "00"):'))
     es=float(input('Enter the amount of final stocks(if no enter "0"):'))
     global netpurchase
     npurch=netPurchase()
     costofgoods=ss+npurch-es
     return costofgoods

def grossPROFIT():
     global netSales,coGs
     tsales=netSales()
     costofsales=coGs()
     gp=tsales-costofsales
     return gp