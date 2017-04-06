month = float(700)
bills = float(-550)
start = float(1000)
A = {}
B=raw_input('How much do you earn per month?')
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
#Each key can be specified, through str('x')
#Each key is different, and anything can be kept through it
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
#This adds whatever we set in the dictionary of 'bank' to start. User sets up the value.    
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
    