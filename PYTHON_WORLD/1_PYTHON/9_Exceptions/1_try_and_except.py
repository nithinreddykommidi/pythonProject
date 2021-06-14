import sys

d = {'A':1,'B':2}
try:
    d['C']
    'we' + '123'
    sys.ok()
    import re
    open('2_else.py')
except ModuleNotFoundError:
    print(' Module is not defined ')
except NameError:
    print(' name is not defined please define ')
except KeyError:
    print(' KeyError ')
except FileNotFoundError as e:
    print(' Please define file ', e)
except:
    print(' Try block got failed ')


