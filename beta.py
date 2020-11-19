'''
this file creates and opens a file for writing to which is stored as fw
then we write two lines of code to this text before closing to save memory
'''


fw = open('gettysburg.txt', 'w')
fw.write('Four score and seven years ago \n')
fw.write('our fathers brought forth on this continent a new nation')
fw.close()


'''
we then open that file for reading and save the contents in a variable fr which reads the rile
we then read use the read function on the fr variable and save this to a variable, text, which we print
'''

fr = open('gettysburg.txt', 'r')

text = fr.read()

print(text)

fr.close()
