import pandas as pd
import numpy as np
import math

data = {
    'age': [25, 35, 50, 60, 70],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'disease': ['Flu', 'Heart Attack', 'Diabetes', 'Flu', 'Stroke'],
    'comorbidity': [0, 1, 2, 0, 3],
    'severity': ['Mild', 'Severe', 'Moderate', 'Mild', 'Critical'],
    'length_of_stay': [2, 7, 5, 3, 10]
}

df = pd.DataFrame(data)

# Map categorical data to numbers
gender_map = {'M': 0, 'F': 1}
disease_map = {'Flu': 0, 'Heart Attack': 1, 'Diabetes': 2, 'Stroke': 3}
severity_map = {'Mild': 0, 'Moderate': 1, 'Severe': 2, 'Critical': 3}

df['gender'] = df['gender'].map(gender_map)
df['disease'] = df['disease'].map(disease_map)
df['severity'] = df['severity'].map(severity_map)

def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

def InfoGain(data, split_attribute_name, target_name="length_of_stay"):
    total_entropy = entropy(data[target_name])
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    Weighted_Entropy = np.sum([ (counts[i]/np.sum(counts)) * entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name]) for i in range(len(vals))])
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

def ID3(data, original_data, features, target_attribute_name="length_of_stay", parent_node_class=None):
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name])[np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])]
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]
        item_values = [InfoGain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        
        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]
        
        for value in np.unique(data[best_feature]):
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = ID3(sub_data, original_data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree
            
        return tree

features = list(df.columns[:-1])
decision_tree = ID3(df, df, features)

def predict(query, tree, default=1):
    for key in list(query.keys()):
        if key in list(tree.keys()):
            try:
                result = tree[key][query[key]] 
            except:
                return default
            result = tree[key][query[key]]
            if isinstance(result, dict):
                return predict(query, result)
            else:
                return result

# Example prediction for a new patient
new_patient = {'age': 45, 'gender': 1, 'disease': 1, 'comorbidity': 1, 'severity': 2}
prediction = predict(new_patient, decision_tree)
print(f'Predicted length of stay: {prediction} days')
