import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sb
import matplotlib as plt


 
data = load_iris()
df = pd.DataFrame(data.data, columns= data.feature_names)
df['target'] = data.target
df.target.unique()
df = df[df['target'].isin([1,0])]
df.target.unique()
print(df.columns)

fig, axs = plt.subplot(2, 2)
axs[0, 0].scatter(df['sepal length (cm)'], df['sepal width (cm)'], c = df['target'])

axs[1, 1].scatter(df['petal length (cm)'], df['petal width (cm)'], c = df['target'])
axs[0, 1].scatter(df['sepal length (cm)'], df['sepal width (cm)'], c = df['target'])
axs[1, 0].scatter(df['sepal length (cm)'], df['petal length (cm)'], c = df['target'])
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'])
plt.show()

x_train, x_test, y_trein, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]], test_size=0.2, random_state=1)

model = LogisticRegression()
model.fit(x_train, y_trein)
y_pred = model.predict(x_test)
class_report = classification_report(y_test, y_pred)
print(class_report)
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(sb.heatmap(confusion_matrix(y_test, y_pred), annot=True, cbar=False))

