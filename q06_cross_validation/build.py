from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge,LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data

np.random.seed(9)

data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')

Rmodel = Ridge(alpha= 0.1)
model = Rmodel.fit(X_train, y_train)
def cross_validation(model,X_train, y_train):
    scores = cross_val_score(model,X_train,y_train, scoring="neg_mean_squared_error", cv=5)
    return scores.mean()
