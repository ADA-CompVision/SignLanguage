# Azerbaijan Sign Language (AzSL)
## AzSL Alphabet Recognition System
<br>

#### Folder 1: Telegram Bot
This folder contains the source code of the implemented Telegram bot where dataset has been collected.

#### Folder 2: Source Codes
In this folder, there are python codes of recognition algorithm. There are 5 files in this folder:

<b>MediaPipe.ipynb</b> : Jupyter notebook file which is responsible for extracting hand landmarks of frames which is used in training.
<br>
<b>model.h5</b> : This is our pre-trained model which recognizes 32 letters of AzSL Alphabet
<br>
<b>lexicon.txt</b> : This is the text file used for Lexicon Verification
<br>
<b>Beam Search + Lexicon Verification.ipynb</b> : This main program which takes input from camera, makes predictions, applies Beam Search and Lexicon Verification.
<br>
