import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

dt = pd.read_csv("./Tempreture_1901_2016_Pakistan -.csv")
X = dt["Year"].values.reshape(-1,1)
y = dt["Temp"].values.reshape(-1,1)

lin_reg = LinearRegression()
lin_reg.fit(X,y)
plt.scatter(X,y)
y_pred = lin_reg.predict(X)
plt.plot(X, y_pred, color="red")
plt.title("Температура Афганистана в апреле 1950-2016")
plt.xlabel('Год')
plt.ylabel('Температура')
plt.show()
##################################################################

poly_reg = PolynomialFeatures(degree=5)

lin_reg2 = LinearRegression()
lin_reg2.fit(poly_reg.fit_transform(X),y)

X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y)
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)))
plt.title("Температура Афганистана в апреле 1950-2016")
plt.xlabel('Год')
plt.ylabel('Температура')
plt.show()