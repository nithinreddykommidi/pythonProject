f = open('names.txt','r')

print(f.read())
f.close()

fw = open('wr.txt','w')
fw.write('written_file')
fw.close()

fa = open('wr.txt','a')
fa.writelines( '/n new_line /n' )
fw.close()

