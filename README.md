# Azerbaijan Sign Language (AzSL)
## AzSL Alphabet Recognition System
<br>

#### Folder 1: Telegram Bot
This folder contains the source code of the implemented Telegram bot where dataset has been collected.

#### Folder 2: Source Codes
In this folder, there are python codes of recognition algorithm. There are 5 files in this folder:

MediaPipe.ipynb : Jupyter notebook file which is responsible for extracting hand landmarks of frames.
<br>
model.h5 : This is our pre-trained model which recognizes 32 letters of AzSL Alphabet
<br>
lexicon.txt : This is the text file used for Lexicon Verification
<br>
Beam Search + Lexicon Verification.ipynb : This main program which takes input from camera, makes predictions, applies Beam Search and Lexicon Verification.
<br>
