#!/usr/bin/python
#filename: while.py
num=123
running=True
while running:
    guess=int(raw_input('Enter an integer:'))

    if guess==num:
        print('Congratulations,you	guessed	it.')
        print('but you do not win any prizes!')
        running=False
    elif guess > num:
        print 'NO, it is a little higger than that'
    else:
        print 'NO, it is a little lower than that'

else:
    print 'The while loop is over'

print 'Done'
