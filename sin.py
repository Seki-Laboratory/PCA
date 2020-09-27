import tkinter
import tkinter.filedialog

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('tkinter dialog trial')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.dialog_button = tkinter.Button(self, text='File Open...', command=file_open, width=120)
        self.dialog_button.pack(anchor=tkinter.NW)

        self.text_1 = tkinter.StringVar()
        self.type_label = tkinter.Label(self, textvariable=self.text_1)
        self.type_label.pack(anchor=tkinter.W)
        self.text_2 = tkinter.StringVar()
        self.content_label = tkinter.Label(self, textvariable=self.text_2)
        self.content_label.pack(anchor=tkinter.W)
        self.text_3 = tkinter.StringVar()
        self.len_label = tkinter.Label(self, textvariable=self.text_3)
        self.len_label.pack(anchor=tkinter.W)

def file_open():
    ini_dir = 'C:\Program Files\Python37'
    ret = tkinter.filedialog.askopenfilename(initialdir=ini_dir, )
    """
    app.text_1.set('Type : ' + str(type(ret)))
    app.text_2.set('Content : ' + str(ret))
    app.text_3.set('Length : ' + str(len(ret)))
    """
    return ret
"""
root = tkinter.Tk()
app = Application(master=root)
"""

#PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

#"""PCAの開始"""#
df = pd.read_csv(file_open()) #desktopPC

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




