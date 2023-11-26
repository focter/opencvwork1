from sklearn.datasets import load_breast_cancer
import pandas as pd
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("数据集内容：")
print(df.head())

print("\n数据集形状（行，列）：", df.shape)
