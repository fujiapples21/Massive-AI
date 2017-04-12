#Money Global 1.1
month = float(700)
bills = float(-550)
start = float(1000)
A = {}
B=raw_input('How much do you earn per month?')
C=raw_input('Whats the cost of your weekly expenses on average?')
'''
def spending(raw_input):
    global A
    yeet = 
    A['receipt' + item]
    for key,value in a.items():
        #print key + " => " + value
        if yeet == (key):
            print 'schedule: ' + value

def addItems(amount, item):
    global A
#Each key can be specified, through str('x')
#Each key is different, and anything can be kept through it
#Each period can be different.
    A['receipt' + item] = schedule    
'''
def changeBills(newFees):
#Change the weekly expenses to what you'd like or need
    global A
    global C
    C = newFees
    A['fees'] = ('your fees are now',float(C))    

def weeklyExpenses():  
#This function will take away money if called upon right away and will spit out result
#The expense comes from user input at beginning of running.
    global start      
    global bills
    global month
    global C
    start = start - float(C)
    print 'You now have','$',start    
    
def fixedIncome(raw_input):
    global C
    global A
    global B
    fees = 'weekly' and 'expenses'
    income = 'monthly' and 'income'
    if fees in (raw_input):
#This will spit out fees if the words weekly and expenses are within input
        print 'Your fees are $',float(C), 'per week.'
    elif income in (raw_input):
#This will spit out your income if words 'monthly' and 'income' are within input
        print 'Your income is $',float(B), 'per month.'
        
def add():
    global start
    global month
    global A
    global B
    
    print '$', start
    A['bank'] = float(B)
#The code below adds the amount of money that you earn from the key of 'bank', from the user
#to start. Start fluctuates throughout code, but it will show you how much you have at end.
    start = start + A['bank']
    print 'You now have','$',start  
    
def spend(b):
    global start
    start = start - float(b)
    print '$', start
    
def CurrentMoney():
    global start
    print '$', start
    
def cash():
    global start
    start = start +25
    print '$', float(start)
