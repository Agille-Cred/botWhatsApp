import sys

def import_texto():
    try:
      file = open('texto.txt', 'r')
    except:
      sys.exit(0)