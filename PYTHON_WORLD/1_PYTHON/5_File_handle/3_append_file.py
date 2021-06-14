'''
1. To do append operation on file we have to open a file with 'a' mode
2. If you open a file with append mode if file is not exist it will crate file, if file is exist it will add new data after old data.

'''

fw = open('SSSS.txt', 'a')

# To write data into file
fw.write('\nHi BALU')
fw.write('How are you')

# To close a file
fw.close()