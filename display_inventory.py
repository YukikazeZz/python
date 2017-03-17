#!/usr/bin/python

def  display_inventory(inventory):
    for val,key in inventory.iteritems():
        print(key,val)
    print('Total number of items:',sum(inventory.values()))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)
