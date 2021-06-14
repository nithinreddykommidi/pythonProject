

fh = open('names.txt', 'r')

## To open a file from another path
#fw = open(r'C:\Users\smellamput001\Desktop\BACKUP_EPRO\RRR.txt', 'r')



## Using read we can read entire file data and return in string format
#fdata = fh.read()
#print(fdata)



## To read the first five characters
#fdata = fh.read(5)
#print(fdata)



## Using readline we can read only one line and return in string format
# line  = fh.readline()
# print(' 1 :: ', line)

# line  = fh.readline()
# print(' 2 :: ', line)

# line  = fh.readline()
# print(' 3 :: ', line)


## Using readlines we can read total lines in a file and  return in list format
lines  = fh.readlines()
print(' READ LINES ', lines[4])

# To close a file
fh.close()
