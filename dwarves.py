import sys
import re

suits = {
    'Bashful':'yellow', 'Sneezy':'brown', 'Doc':'orange', 'Grumpy':'red', 'Dopey':'green', 'Happy':'blue', 'Sleepy','taupe'
    }
pattern = re.compile("(%s)" % sys.argv[1])

for dwarf, color in suits.items():
  if pattern.search(dwarf) or pattern.search(color):
    print("%s's dwarf suit is %s." %
      (pattern.sub(r"_\1_", dwarf), pattern.sub(r"_\1_", color))
      break
  else:
    print("No dwarves or dwarf suits matched the pattern.")
