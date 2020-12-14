# DataMiningProject
Rating Prediction using Naive Bayes:

Given a review for the board game, goal is to predict rating. Using Naive Bayes here because it is good for text classification

Dataset: https://www.kaggle.com/jvanelteren/boardgamegeek-reviews

Technology Stack: Python, Apache Flask, PythonAnywhere

How to execute:

	1. Open up command prompt and navigate to the folder where you want to save the project and do $git clone https://github.com/NandhimandalamLakshmi/DataMiningProject
	2. Size of multinominalNB.pickle was large so I have Zipped it. After cloning Unzip multinominalNB.pickle
	3. Install Flask
	4. Make sure main.py, NaiveBayes.py, multinominalNB.pickle, TfidfVec.pickle files are present in the desired folder. Also there must be templates folder and inside it, index.html and result.html must be present
	5. Execute $python main.py
	6. You must be able to see a webpage opened up in your local host. Enter your review in the text box, and click on Submit button. Your result will be displayed in separate html file
	7. To deploy Flask app on webserver, we are using PythonAnywhere
	8. Create an account in pythonanywhere and Sign In.
	9. Go to Files Tab and upload all files as mentioned in step 4 maintaining the same folder structure
	10. Go to Web Tab and under the Code section, you can find WSGI configuration file-click on it
	11. Under #import flask app repplace the code with this 'from main import app as application' and save
	12. Click on Reload and when its done open your pythonanywhere url
	13. A webpage is open on server and you can enter your review to get the rating!!!
	

References:

https://scikit-learn.org/stable/modules/naive_bayes.html
https://pythonspot.com/flask-web-app-with-python/
https://stackoverflow.com/questions/4530611/saving-and-loading-objects-and-using-pickle/47381298
	
