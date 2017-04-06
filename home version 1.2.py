month = float(700)
bills = float(-550)
start = float(1000)
A = {}
B=raw_input('How much do you earn per month?')
C=raw_input('Whats the cost of your weekly expenses on average?')
#B is later used in function "add"
#declare a dictionary so we can store key/value pairs
#store a pair for each question set.
#Code used from other people, already kept.
a = {}
b=raw_input('What time do you have work from?')
print('Type help() to learn how I can help you')

def help():
    print 'Hello I am your personal helper, my list of functions include running your finaces or making a scheudle or general chatter. If you want to do your finaces type '
    'finance' 'if you want to make a scheudle with me type ''schedule'
    'if you would like to just talk type''chatter''type' 'help2(''Your keyword'')''to continue'


def help2(raw_input):
#The 'words' within that quotes keep track of the user input, if the words are in it the user's sentence then it will print ___
    if 'schedule' in raw_input:
        schedule('Whats my schedule today?') 
    if 'finance' in raw_input:
        monthlyExpenses()
    if 'chatter' in raw_input:
        chatter()
           
def schedule(raw_input):
    global a
    routine = 'schedule' and 'today'
    if routine in (raw_input):
        a['work'] = 'you have work from ' + b
    print a['work']
    
def changeSchedule(newSchedule):
    global a
    global b
    b = newSchedule
    a['work'] = 'you have work from ' + b
#use global dictionary "a" to store a schedule with a
#corresponding period
def addSchedule1(schedule, period):
    global a
#Each key can be specified, through "x"('sched')
#Each key is different, and anything can be kept through it. "index within indexes"
#Each period can be different.
    a['sched' + period] = schedule
#retrieve a schedule back based on the period
def schedule1(period):
    global a
    routine = 'sched' + period
    for key,value in a.items():
        #print key + " => " + value
        if routine == (key):
            print 'schedule: ' + value

#change the schedule for the period using the dynamic key
def changeSchedule1(newSchedule, period):
    global a
    routine = 'sched' + period
    a[routine] = newSchedule
'''
def spending(raw_input):
    global A
    yeet = 
    A['receipt' + item]
    for key,value in a.items():
        #print key + " => " + value
        if yeet == (key):
            print 'schedule: ' + value

#At the moment, this code is still being fixed.

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
    
def money():
    global start
    start = start - 50
    print '$', float(start)
    
def cash():
    global start
    start = start +25
    print '$', float(start)
    
def chatter(raw_input):
    talk = 'how' and 'are' and 'today'
    if talk in (raw_input):
        print('I am fabulous, thanks for asking')
        bad = 'sad' and 'unhappy' and 'am' and 'I'
        if bad in (raw_input):
            print('Aww, there, there')
        good = 'happy' and 'well' and 'fine' and 'good'
        if good in (raw_input):
            print('Glad to hear it')
    
