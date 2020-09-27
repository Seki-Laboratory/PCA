#PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
#GUI
import os, tkinter, tkinter.filedialog, tkinter.messagebox

#"""GUIの開始"""#

# ファイル選択ダイアログの表示

root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('筋電実効値_主成分分析','処理ファイルを選択してください！')
csvfile = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

# 処理ファイル名の出力
tkinter.messagebox.showinfo('筋電実効値_主成分分析',csvfile)



df = pd.read_csv(csvfile) #desktopPC

df.columns=['emg1', 'emg2', 'emg3', 'emg4', 'emg5', 'emg6', 'emg7', 'emg8', 'class']

X = df.iloc[:,0:8].values
y = df.iloc[:,8].values

#-1 - 1の範囲にする
X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components=2) 

principalComponents = pca.fit_transform(X_std) 

principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2']) 



print("主成分の分散説明率")
print(pca.explained_variance_ratio_)
print("固有ベクトル")
print(pca.components_)

finalDf = pd.concat([principalDf, df[['class']]], axis = 1)


plt.figure(figsize = (8,6))

plt.xlabel('Principal Component 1', fontsize = 15)
plt.ylabel('Principal Component 2', fontsize = 15)


targets = ['nigiru', 'hiraku', 'syoukutu','haikutu','toukutu','mudousa']
colors = ['r', 'g', 'b','y','m','k']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['class'] == target
    plt.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']

               , c = color
               , s = 50)

pc1 = pca.explained_variance_ratio_[0]
pc2 = pca.explained_variance_ratio_[1]
ans = (pc1+pc2)*100
plt.title('contribution ratio: %i percent'%ans,fontsize = 20)

plt.legend(targets)
plt.grid()
plt.show()
