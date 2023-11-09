import random
import sys
import pyperclip

# while True:
print('your piperclip contains ', pyperclip.paste())
pyperclip.copy(random.randint(1, 999999999999999))
print('and now '+pyperclip.paste())
sys.exit()