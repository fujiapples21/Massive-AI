#New Globe Text


#declare a dictionary so we can store key/value pairs
#store a pair for each question set.
#Code used from other people, already kept.
a = {}
b = {}

def schedule(raw_input):
    create = 'schedule' or 'today' or 'make' or 'schedule' or 'I' or 'Would'
    if create in (raw_input):
         b['asfasf']=raw_input('What time do you have work from?')
    global a
    routine = 'schedule' and 'today'
    if routine in (raw_input):
        a['work'] = 'you have work from ', b
    print a['work']


def changeSchedule(newSchedule):
    global a
    global b
    b = newSchedule
    a['work'] = 'you have work from ' + b
#use global dictionary "a" to store a schedule with a
#corresponding period




