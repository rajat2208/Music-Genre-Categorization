import sys
import os
import sox

# Store the directory where all the audio files are saved
genre_dirs = ['C:/Users/MAHE/Downloads/Audio-Genre-Classification-master/Audio-Genre-Classification-master/rock'
]
for genre_dir in genre_dirs:
	# change directory to genre_dir
	os.chdir(genre_dir)

	# echo contents before altering
	print('Contents of ' + genre_dir + ' before conversion: ')
	os.system("ls")

	# loop through each file in current dir
	for file in os.listdir(genre_dir):
		# SOX
		os.system("sox " + str(file) + " " + str(file[:-3]) + ".wav")
	
	# delete .au from current dir
	os.system("rm *.au")
	# echo contents of current dir
	print('After conversion:')
	os.system("ls")
	print('\n')

print("Conversion complete. Check respective directories.")