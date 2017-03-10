#!/usr/bin/python
#filename: if.py
num=123
guess=int(raw_input('Enter an integer:'))

if guess==num:
    print('Congratulations,you	guessed	it.')
    print('but you do not win any prizes!')
elif guess > num:
    print 'NO, it is a little higger than that'
else:
   print 'NO, it is a little lower than that'

print 'Done'
