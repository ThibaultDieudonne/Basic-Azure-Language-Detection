# OC-Projet1
First project - AI Engineer 

"Detect.py" script originally comes from Text-Translation-API-V3-Python.

"labels.csv" file is from the WiLI database.

# How to use
First, add your Azure API credentials in the batch scripts and install python requirements

Language detector can be used manually by running "run.bat".

"texts.txt" contains sentences in various languages from the most used 5. "languages.txt" are the associated languages codes.
This files were made using "Extract.py" on the "x_train.txt" and "y_train.txt" files frome the WiLI database.

To perform a full test over the extracted sentences, run "checkout.bat" (current accuracy is 98.5%).