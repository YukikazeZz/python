#!/usr/bin/python

def  display_inventory(inventory):
    for val,key in inventory.iteritems():
        print(key,val)
    print('Total number of items:',sum(inventory.values()))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item,0)
        inventory[item]+=1
    return inventory

inv= {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot= ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
display_inventory(inv)
inv= add_to_inventory(inv, dragon_loot)
display_inventory(inv)
