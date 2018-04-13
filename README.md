# Music-Genre-Categorization
Categorizing songs from their WAV files to popular genres using certain features

<h3>UPDATE 1</h3>

The initial commit extracts all the necessary features from the audio after the songs have been **converted to their WAV format** by using the _convert-to-wav.py file_. 

After the conversion and **feature extraction** _(using fft-features.py and mfcc-features.py)_ is completed, a **spectogram** using _plot-spectogram.py_ is plotted afainst time and frequency of the audio sample for effective visualization. 

<h3>UPDATE 2</h3>

Added the _learn.py_ and _tester.py_ files. Use the learner script to train the dataset against multiple genres and then run the tester script to test one particular song's genre.
