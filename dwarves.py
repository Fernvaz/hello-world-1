import sys                                                  #Brings in the sys and re modules. 
import re

suits = {
    'Bashful':'yellow', 'Sneezy':'brown', 'Doc':'orange', 'Grumpy':'red', 'Dopey':'green', 'Happy':'blue', 'Sleepy','taupe'
    }                                                       #Stores suits as key/value to each dwarf.
pattern = re.compile("(%s)" % sys.argv[1])

for dwarf, color in suits.items():                          #Runs the code for as many values there are, per-key.
  if pattern.search(dwarf) or pattern.search(color):
    print("%s's dwarf suit is %s." %
      (pattern.sub(r"_\1_", dwarf), pattern.sub(r"_\1_", color))        #Prints each one with underscores surrounding groups of vowels.
      break
  else:
    print("No dwarves or dwarf suits matched the pattern.")
