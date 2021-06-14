'''
1. Using logging module we can log based on severity level.
2. By default, there are 5 standard levels indicating the severity of events. 
3. Log levels are ==>  INFO, DEBUG, WARNING, ERROR, CRITICAL
4. The default level is WARNING
'''

import logging

print(' TEST 1 ')
print(' TEST 2 ')
print(' TEST 3 ')
print(' TEST 4 ')
print(' TEST 5 ')

logging.info(" TEST 1 ")
logging.debug(" TEST 2 ")
logging.warning(" TEST 3 ")
logging.error("   TEST 4 ")
logging.critical(" TEST 5 ")

