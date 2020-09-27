import numpy as np
import pandas 
import sklearn 
from sklearn.decomposition import PCA #主成分分析
import matplotlib.pyplot as plt 
import tkinter as tk

df=pandas.read_csv(r"G:\マイドライブ\プログラミング\PCA\nigiru.csv")

# 主成分分析実行
pca = PCA()
feature = pca.fit(df)

# データを主成分空間に写像
feature = pca.transform(df)

#第2主成分まででプロット

plt.figure(figsize=(6, 6))
plt.scatter(feature[:, 0], feature[:, 1],alpha=0.8, c="b")

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid()
pc1 = pca.explained_variance_ratio_[0]
pc2 = pca.explained_variance_ratio_[1]
ans = (pc1+pc2)*100
plt.title('contribution ratio:%i'%ans)
#寄与率表示
print("主成分の分散説明率")
print(pca.explained_variance_ratio_)

plt.show()



