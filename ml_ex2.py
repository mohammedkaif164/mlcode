import pandas as pd
from math import log2
data=pd.read_csv("tennis.csv")
print(data)
def entropy(col):
    values = col.unique()
    ent=0
    for v in values:
        p=col.value_counts()[v]/len(col)
        ent -=p*log2(p)
    return ent
def info_gain(data,feature,target):
    total_entropy=entropy(data[target])
    vals=data[feature].unique()
    weighted_entropy=0
    for v in vals:
        subset =data[data[feature]==v]
        weighted_entropy+=(len(subset)/len(data))*entropy(subset[target])
        return total_entropy - weighted_entropy
target="playtennis"
features=data.columns[:-1]
print("\n entropy of dataset:",entropy(data[target]))
for f in features:
    print("information gain of",f,"=",info_gain(data,f,target))
best_feature=max(features,key=lambda x:info_gain(data,x,target))
print("\n best feature (root node):",best_feature)
