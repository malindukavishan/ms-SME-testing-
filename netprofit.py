additionalincomes=0
transport=0
administration=0
finacial=0
other=0    
def Transportexp():
    print("\n---Enter '0' for stop loop---")
    global transport
    while True:
         trnsprt=float(input('Enter the value of transport cost:'))
         if (trnsprt==0):
             break
         transport=transport+trnsprt
    return transport

def Adminexp():
    print("\n---Enter '0' for stop loop---")
    global administration
    while True:
         admn=float(input('Enter the value of Administration cost:'))
         if (admn==0):
             break
         administration=administration+admn
    return administration

def Financialexp():
    print("\n---Enter '0' for stop loop---")
    global finacial
    while True:
         finance=float(input('Enter the value of Financial cost:'))
         if (finance==0):
             break
         finacial=finacial+finance
    return finacial

def Otherexp():
    print("\n---Enter '0' for stop loop---")
    global other
    while True:
         othr=float(input('Enter the value of Other cost:'))
         if (othr==0):
             break
         other=other+othr
    return other

def Totalexp():
    global additionalincomes,transport,administration,finacial,other
    ai=addiINC()
    tr=Transportexp()
    ad=Adminexp()
    fi=Financialexp()
    ot=Otherexp()
    texp=tr+ad+fi+ot
    return texp

def addiINC():
    print("\n---Enter '0' for stop loop---")
    global additionalincomes
    while True:
         incomes=float(input('Enter the value of additional incomes:'))
         if (incomes==0):
             break
         additionalincomes=additionalincomes+incomes
    return additionalincomes