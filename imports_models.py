# %load imports.py
#Linear regression models

#Classification models
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#Now it would be very remarkable if any system existing in the real
#world could be exactly represented by any simple model. However,
#cunningly chosen parsimonious models often do provide remarkably useful
#approximations. For example, the law PV = RT relating pressure P, volume
#V and temperature T of an "ideal" gas via a constant R is not exactly
#true for any real gas, but it frequently provides a useful approximation
#and furthermore its structure is informative since it springs from a
#physical view of the behavior of gas molecules. For such a model there is
#no need to ask the question "Is the model true?". If "truth" is to be the
#"whole truth" the answer must be "No". The only question of interest
#is "Is the model illuminating and useful?".
