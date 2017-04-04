#New Globe Text


#declare a dictionary so we can store key/value pairs
#store a pair for each question set.
#Code used from other people, already kept.
a = {}
b=raw_input('What time do you have work from?')

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