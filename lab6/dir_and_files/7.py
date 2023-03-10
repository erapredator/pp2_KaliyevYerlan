
with open(r'C:\pptxt\test.txt','r') as firstfile, open(r'C:\pptxt\test2.txt','a') as secondfile:
	for line in firstfile:
		secondfile.write(line)
