#Money Global 1.1
month = float(700)
bills = float(-550)
start = float(1000)
A = {}
B=raw_input('How much do you earn per month?')
def monthlyExpenses():  
    global start      
    global bills
    global month
    start = start + bills
    print 'You now have','$',start     
        
def add():
    global start
    global month
    global A
    global B
    
    print '$', start
    A['bank'] = float(B)
    start = start + A['bank']
    print 'You now have','$',start  
    
def spend(b):
    global start
    start = start - float(b)
    print '$', start
    
def money():
    global start
    start = start - 50
    print '$', float(start)
    
def cash():
    global start
    start = start +25
    print '$', float(start)