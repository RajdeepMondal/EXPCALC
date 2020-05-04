In order to run the application, go to the directory where the codes are saved.

######################################################################################################################################################################################################################
Ensure that both Java 8 SDK and Python 3.6 are installed on your computer and can be run from the command line itself.
Dependencies:
 	1) Python 
		1.1: NumPy
		1.2: OpenCV
		1.3: Imutils
 	2) Java
		2.1: Swing
		2.2: AWT
The required Java packages are already available in the Java software.
	1.	In order to install the librariesin Python, go to the directory where the folder Python36 is located and open the Scripts folder available under the Python36 folder.
	2.	Open Command Prompt in this directory and type in:
			pip install
		followed by the name of the library
	3.	If you have an older version of the above mentioned libraries, type in
			pip --upgrade
		follwed by the name of the library 
######################################################################################################################################################################################################################

STEPS:
1. Open calc_mode.py and set the path to where the codes are saved, thus:
	sys.path.insert(0,parent_directory_path)

2. Open Command Prompt and type in the following commands one by one:
	>> javac Test.java
	>> java Test

3. In the Welcome screen select the mode you want to avail

4. If you select Child Mode,
	4.1) A random number in the range 0 to 9 will be generated and displayed at the top of the screen
	4.2) Holding down the left mouse button, drag and draw the number in the space provided.
	4.3) Click on SUBMIT.
	4.4) If you wrote the number correctly (and if the neural network recognizes it correctly!), CORRECT will be displayed in the lower white space. Otherwise, WRONG!
	4.5) Click on NEW to try out a new digit

5. If you select Calculator Mode,
	5.1) You can write zero or any positive integer in the space provided using the same way as above. Since the calculator employs multiple digit recognition, the positive integer can have any number of digits.
	5.2) Click on SUBMIT.
	5.3) Select an operator from any of the options provided.
	5.4) In case you make an error, click on the CLEAR button to start from the beginning
	5.5) Click on "=" to get your expression evaluated.
	5.6) The calculator follows BODMAS rule and the expression can be of any length. Also the division operation is basically a floor division operation. So be careful!
	5.7) The recognized expression and the calculated result will be displayed at the bottom of the screen.
	5.8) Click on CLEAR to make a new expression.

                                  #################################################################
                                  #     BEWARE THE CALCULATOR DOES NOT RECOGNIZE 8 VERY WELL!!    #
			          #################################################################
ENJOY!! 