# Azerbaijan Sign Language (AzSL)
## AzSL Alphabet Recognition System

<h2> About the project </h2>

<p>
A real-time Azerbaijani Sign Language (AzSL) to text translation system, based on the finger-spelling. The system consists of both statistical and probabilistic models, which are used in the sign recognition and sequence generation phases. The proposed work reviews the specifics of AzSL, evaluates the feature selection strategies and suggests a robust model for the translation of the hand signs. The model that consists of two-staged recognition uses both statistical and probabilistic methods for delivering the high accuracy during the real-time inference. An AzSL dataset of 14,144 samples collected from
221 volunteers has been described in detail and made publicly available for the SLR community.
</p>

<h2>Data Collection</h2>
You can find the working version of the Telegram bot which was used in the data collection phase under the folder "Telegram Bot". 
The Telegram bot called JestDiliBot that used dialogue interface to collect the data: a user is asked to select a letter, then receives a sample image or video based on the selection and is suggested to capture the similar data and submit. After the successfull submission, the bot shows the ten letters with the least sample counts (this counting function checks on counts every three hours and updates the minimum ten elements) and suggests contributing with these letters. Such an approach helped keep our dataset balanced.

<h2>Machine Learning Model and its components</h2>
You can find the final version of the source code for the model under the folder "Source Codes". The recognition algorithm has been developed in Python and you can find the following files in this folder:

<h4>FeatureAnalysis.ipynb</h4> 
Analysis of various features for the hand gesture recognition.

<h4>MediaPipe.ipynb</h4> 
Jupyter notebook file which is responsible for extracting hand landmarks of frames which is used in training.

<h4>model.h5</h4>
This is our pre-trained model which recognizes 32 letters of AzSL Alphabet

<h4>lexicon.txt</h4>
This is the text file used for Lexicon Verification

<h4>Beam Search + Lexicon Verification.ipynb</h4>
This main program which takes input from camera, makes predictions, applies Beam Search and Lexicon Verification.


<h2>TeknoFest Azerbaijan 2022</h2>
<div style="display: flex; justify-content: space-between;">
  <img src="/images/Team.JPG" height="440" >
  <img src="/images/Stage.JPG" height="440" >
</div>
<br />

The initial prototype of the Azerbaijani Sign Language project won the first place on the <b>Social Technologies branch in TeknoFest Azerbaijan 2022</b> - Aerospace and Technology Festival. During 3 days in a row all the team members demonstrated the first working version of the project based on all of the letters of the Azerbaijani alphabet with 96% accuracy. The feedback from the community gave the team many different ideas about integration of the model to different applications and officies of government agencies.
