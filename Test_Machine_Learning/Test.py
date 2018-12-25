from sklearn import tree
import pandas_datareader.data as web
import datetime as dt
'''features = [[140, "smooth"],
            [130, "smooth"],
            [150, "bumpy"],
            [170, "bumpy"]]
            '''

features = [[140, 1],
            [130, 1],
            [150, 0],
            [170, 0]]


'#labels = ["apple", "apple", "orange", "orange"]'
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

'bumpy'
#print(clf.predict([[150, 0]]))
#print(dt.date.today())
df = web.DataReader('TAL1T', 'av-daily', start=dt.date.today())
print(df)