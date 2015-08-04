"""Questions borrowed from UPenn Authentic Happiness Initiative's Grit Survey"""

from tkinter import *
from tkinter.messagebox import showinfo


questions = (
    'I overcome setbacks to conquer important challenges.',
    'Dogged and determined describe my work ethic.',
    'I have achieved a goal that took years of work.',
    'I am diligent, kind, good human being.')

def responseWindow():

    showinfo(title='Outlook', message = responseText())

def responseText():
    
    sett = entries.values()
    results = [int((i.get())) for i in sett]
    
    if sum(results) <= 15:
        return 'You have better habits than you know. Just keep swinging!'
    else:
        return 'Keep up the good habits and attitude, Champ!'


def makeWidgets():

    global entries
    window = Tk()
    window.title('Morning Psych Out or Daily Optimism Appraisal')
    form = Frame(window)
    
    mainLabel = Label(window, text='Please ascribe a number between 1 and 5 next to each phrase.')
    mainLabel.config(font = (30), fg = 'white', bg = 'navy')
    mainLabel.pack(expand = YES, fill = BOTH)
    
    scaleLabel = Label(window, text = '1 = Not like me at all, 3 = Somewhat like me, 5 = Very much like me\n')
    scaleLabel.config(fg = 'yellow', bg = 'navy')
    scaleLabel.pack(expand = YES, fill = BOTH)
    
    form.pack()
    entries = {}
    for (vm, label) in enumerate(questions):
        label = Label(form, text = label)
        entry = Entry(form)
        label.grid(row = vm, column = 0)
        entry.grid(row = vm, column = 1)
        entries[label] = entry
    
    Button(window, text = "Submit", command = responseWindow).pack(side = RIGHT)
    return window

window = makeWidgets()
window.mainloop()

