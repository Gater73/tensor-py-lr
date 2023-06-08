
# tensor-py-lr
Linear Regression AI that calculates a student's G1 based on G2, G3, studytime, failures and absences using TensorFlow, Keras, Numpy and Pandas.

## Dependencies
- tensorflow==2.6.2
- keras==2.6.0
- pandas==1.1.5
- numpy==1.19.5
- scikit-learn==0.24.2

## Installation
- Create a conda environment with python 3.6
- Activate the environment
- Use pip to install all the dependencies above
- Put the dataset and the main.py in the same folder
- Run main.py with python 3.6

## Sample Workflow

### Terminal

    $ python3 main.py
    Using TensorFlow backend.
    Enter the students G2: 15
	Enter the students G3: 15
	Enter the students studytime: 3
	Enter the students failures: 0
	Enter the students absences: 0
	Information used to predict stops here
	Enter the students actual G1 number: 15
	With a accuracy of 73.95% the AI predicted a value of [14.2819377] for G1 using [G2=15, G3=15,
	studytime=3, failures=0, absences=0] and the actual G1 number was 15.

	Process finished with exit code 0

Using the data [G2=15, G3=15, studytime=3, failures=0, absences=0] the AI was able to predict the number 14.2819377 and the expected number was 15, the model had a 73.95% accuracy.
    

Source code under [GPL v3](https://www.gnu.org/licenses/gpl-3.0.pt-br.html)
