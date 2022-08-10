import numpy as np
from scipy import linalg

# Test has 30 questions and worth 150 points
# True and false questions are worth 4 marks each
# Multiple choice are worth 9 points each

# Let x is the number of true/false questions
# Let y is the number of multiple choice questions

# (x + y = 30) 
# (4x + 9y = 150)

# uses coefficients from both equations
testQuestionVariable = np.array([[1,1],[4,9]])

# use product from both equations
testQuestionValue = np.array([30,150])

# Use linalg function of scipy
# use solve method to solve the linear equation and find the value for x and y

answer = linalg.solve(testQuestionVariable,testQuestionValue)

print(answer)
