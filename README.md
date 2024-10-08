## Diabetes Prediction App(https://diabetes-prediction-app-qvg7.onrender.com)

This is a Flask application that predicts whether someone has diabetes based on a set of user-provided medical features.

**Features:**

* User interface for entering medical data.
* Prediction based on a trained machine learning model.
* Dynamic result display with color highlighting (green for "No Diabetes", red for "Diabetes").

**Requirements:**

* Python 3.10.0
* Flask
* NumPy
* Pandas
* scikit-learn (or other machine learning library) - for loading the model
* Pickle - for loading the trained model
* matplotlib
* seaborn
  

**Installation:**

1. Clone this repository.
2. Install the required dependencies: `pip install -r requirements.txt` (assuming you have a `requirements.txt` file listing the dependencies).
3. Download your trained diabetes prediction model (`.pkl` file) and place it in the same directory as your application files.

**Usage:**

1. Run the application: `python app.py`
2. Open http://127.0.0.1:5000/ in your web browser.
3. Enter your medical data in the form fields.
4. Click the "Predict" button.
5. The application will display the predicted outcome ("No Diabetes" or "Diabetes") with a corresponding color highlight.

**Files:**

* `app.py`: Contains the Flask application logic, handles user input, prediction, and renders the templates.
* `index.html`: The user interface for entering medical data.
* `result.html`: The template for displaying the prediction result.
* `style.css` (optional): Provides styles for the user interface (optional).
* `requirements.txt`: Lists the required Python libraries.
* `diabetes_analysis_model.pkl`: The trained diabetes prediction model (needs to be downloaded separately).

**Contributing:**

Feel free to fork this repository and contribute improvements or add new features. 

**License:**

This project is licensed under the MIT License (see LICENSE file).

Copyright (c) 2024 Suhal Samad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
