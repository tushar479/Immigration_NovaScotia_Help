"""
===================
Isotonic Regression
===================

An illustration of the isotonic regression on generated data. The
isotonic regression finds a non-decreasing approximation of a function
while minimizing the mean squared error on the training data. The benefit
of such a model is that it does not assume any form for the target
function such as linearity. For comparison a linear regression is also
presented.

"""
print(__doc__)

# Author: Nelle Varoquaux <nelle.varoquaux@gmail.com>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
# License: BSD

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

import pandas as pd

print("Please Enter Data in the form of two columns, first column being String(e.g: Name), and the Second Column being Value (e.g: Integer)")
filename = raw_input("Enter Dataset File path: ")

#Create a dataframe holding the data fetched from file
df = pd.read_csv(filename)

#create an empty array and loop through each row of data.
String = {}
for row in df.values:
    if row[0] in String:
        String[row[0]] += [row]
    else:
        String[row[0]] = [row]


for key, value in String.iteritems():
    pass_var = False
    for v in value:
        if v[2] < 5:
            pass_var = True
    if not pass_var:
        predict_years = 3
        n = 4
	    x = np.arange(n)
	    y = [v[2] for v in value]
	    print y

       ###############################################################################
        # Fit IsotonicRegression and LinearRegression models

       ir = IsotonicRegression()
        ir = ir.fit(x, y)

       lr = LinearRegression()
        lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression

       next_years = []
        for nx in range(n, n+predict_years):
            next_years.append(lr.predict(nx)[0])
        x = np.concatenate( (x, np.arange(n,n+predict_years)) )
        y += next_years

