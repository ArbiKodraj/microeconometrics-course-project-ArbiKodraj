import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



from IPython.display import display_html, HTML

from auxiliary_descriptive_replication import *




def filled_data_set():
    
    pd.set_option('display.max_columns', None)
    df = pd.read_stata("oreopoulos resume study replication data file.dta")
    fill_values = {'chinese': 0, 'indian': 0, "british":0, 'pakistani': 0, 'pakistani':0, "Chn_Cdn":0, "same_exp":0}
    df.fillna(value=fill_values, inplace=True)
    return df

    
       ################################################################################################################   
######################################################## KNN Method ######################################################### 
       ################################################################################################################
    
def train_test_split_method():
    
    df = filled_data_set().sample(9000)

    target = "callback"                                                       
    columns = list(df.columns)                                               

    l1 = list(df.select_dtypes(include=['object']).columns)                   
    l2 = ["firmid", 'interview', 'second_callback',"female", "chinese",
          "indian","british","pakistani","Chn_Cdn", "same_exp", "skillsocialper",
         "skillwriting", "skillspeaking", "callback"]

    exp_var = []                                                            

    for col in columns:                                                 
        if col in l1 or col in l2:
            continue
        else:
            exp_var.append(col)

    df_cleaned_col = df[exp_var].dropna(axis=1, how="any", inplace=False)  

    scaler = StandardScaler()  
    scal_features = scaler.fit(df_cleaned_col)
    scal_features = scaler.transform(df_cleaned_col)
    df_features = pd.DataFrame(scal_features) 

    X_train, X_test, y_train, y_test = train_test_split(df_features, df[target], test_size=0.33, random_state=42)
   
    return X_train, X_test, y_train, y_test
    
    
def knn_method():

    X_train, X_test, y_train, y_test = train_test_split_method()
    
    knn = KNeighborsClassifier(n_neighbors=7).fit(X_train,y_train)
    pred = knn.predict(X_test)

    print(classification_report(y_test,pred))
    

def knn_method_type():
    
    df = filled_data_set().sample(9000)
    
    X = np.array(df["type"]).reshape(-1,1)
    y = df["callback"]
    
    scaler = StandardScaler()  
    scal_features = scaler.fit(X)
    scal_features = scaler.transform(X)
    X = pd.DataFrame(scal_features)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    
    knn = KNeighborsClassifier(n_neighbors=7).fit(X_train,y_train)
    pred = knn.predict(X_test)
    
    print(classification_report(y_test,pred))
   
          
def error_term():
    
    sns.set_style("whitegrid")
    
    X_train, X_test, y_train, y_test = train_test_split_method()
    
    error = []
    
    for i in range(1,22):

        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train,y_train)
        pred_i = knn.predict(X_test)
        error.append((pred_i != y_test).mean())
    
    plt.figure(figsize=(7,5))
    plt.plot(range(1,22),error, marker="o", ls = "--", lw = 1, ms=7, color="k", mfc = "yellow", label="Error")
    plt.title("Error Terms for certain neighbors")
    plt.hlines(min(error), xmin=0,xmax=22,colors="b", lw=1, ls="--", label="Error Minimum")
    plt.legend()
    plt.show()
    
    
def prediction_true_vis():    
    
    df = filled_data_set().sample(8000)
    X = np.array(df["type"]).reshape(-1,1)
    y = df["callback"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=123)

    knnreg = KNeighborsRegressor(n_neighbors=6, weights="uniform",algorithm="ball_tree").fit(X_train,y_train)
    y_pred = knnreg.predict(X_test)

    plt.grid()
    plt.scatter(X_test, y_pred, color='navy', label='prediction')
    #plt.scatter(X_test, y_test, color='red', label='true')
    plt.xlabel("Type")
    plt.ylabel("Callback")
    plt.axis('tight')
    plt.legend()
    plt.title("True versus Prediction")
    plt.tight_layout()
    plt.show() 
    
    t = []
    
    for (i,j) in zip(y_pred,y_test):  
        
        if i != j:
            t.append(i)
    accuracy = len(t)/len(y_pred)
    
    print(f"The accuracy of the KNN-Regression is {accuracy:.5f}")

    
    ############################################################################################################
    
def cond_uncond(df = filled_data_set()):
    
    df_cond = df[(df["additional_credential"] == 1) & (df["language_skills"]) == 1  & 
                 (df["legal"] == 1)  & (df["certificate"] == 1) & (df["ba_quality"] == 1) 
                 & (df["exp_highquality"] == 1) & (df["extracurricular_skills"] == 1)].sample(250)
    
    df_uncond = df[(df["additional_credential"] == 0) & (df["language_skills"] == 0) & (df["reference"] == 0) & 
                 (df["legal"] == 0) & (df["ma"] == 0) & (df["certificate"] == 0) & (df["ba_quality"] == 0) &
                   (df["exp_highquality"] == 0) & (df["extracurricular_skills"] == 0)].sample(250)

    return df_cond, df_uncond
    

def plot_cond_uncond():
    
    df_cond, df_uncond = cond_uncond()
    
    fig, ax = plt.subplots(1,1)
    
    sns.set_style("whitegrid")
    rslt = df_cond.groupby("type")["callback"].mean().to_dict()
    x, y = rslt.keys(), rslt.values()
    ax.plot(list(x), list(y), label="Conditional")
    
    rslt = df_uncond.groupby("type")["callback"].mean().to_dict()
    x, y = rslt.keys(), rslt.values()
    ax.plot(list(x), list(y), label="Unconditional")
    
    ax.set_title("Conditional Expectations")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_ylim([0.0, 0.28])
    ax.set_xlabel("Type")
    ax.set_ylabel("Callbackrate")
    ax.legend()
    
    plt.show()
    
    naive = df_uncond[df_uncond.type == 0]["callback"].mean() - df_uncond[df_uncond.type == 1]["callback"].mean()
    true = df_cond[df_cond.type==0]["callback"].mean()-df_cond[df_cond.type == 1]["callback"].mean()
    
    print("The naive estimation for the name discrimination equals {0:.2f}, while the true name discrimination equals {1:.2f}".format(naive,true))


    
   

    
    
    
    
    
    
    
    
