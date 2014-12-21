fw = open('sample.txt', 'w')
fw.write('Writing stuff on my file \n')
fw.write('This is another line! Cool!')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print (text)
fr.close()