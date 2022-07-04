import sys

import os.path



if len(sys.argv) is 1:

	filename = raw_input('Please type input file name: ') # There is no option.

else:

	filename = sys.argv[1]

while True:

	try:	

		file = open(filename, 'rb')

		break

	except:

		print '[Error] No such file: %s' % filename

		filename = raw_input('Please try again: ')

	

byteBuffer = bytearray(file.read())

file.close()



fn_ext = os.path.splitext(filename)

if fn_ext[1] == '.wav':

	out_filename = fn_ext[0] + '.pcm'

else:

	out_filename = fn_ext[0] + fn_ext[1] + '.pcm'

print 'Out file name: %s' % out_filename



out_file = open(out_filename, 'wb')

out_file.write(byteBuffer[44:])

out_file.close()

		

raw_input('Press Enter to exit')

exit(0)
