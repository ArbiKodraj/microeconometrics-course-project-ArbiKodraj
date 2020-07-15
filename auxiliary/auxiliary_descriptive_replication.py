import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


from IPython.display import display_html, HTML


def data_set():
    
    pd.set_option('display.max_columns', None)
    df = pd.read_stata("data/oreopoulos_resume_study_replication_data_file.dta")
    #fill_values = {'chinese': 0, 'indian': 0, "british":0, 'pakistani': 0, 'pakistani':0, "Chn_Cdn":0, "same_exp":0}
    #df.fillna(value=fill_values, inplace=True)
    return df


def display_side_by_side(*args):
    html_str=''
    for df in args:
        html_str+=df.to_html()
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)
    


##############################################   Section 3  ##############################################################


def second_tableA():
    
    df = data_set()
    
    x1 = df[(df["type"] == 0) & (df["female"] == 0)].groupby(["name_ethnicity", "name"]).apply(len)
    x2 = df[(df["type"] == 1) & (df["female"] == 0)].groupby(["name_ethnicity", "name"]).apply(len)
    x3 = df[(df["type"] == 2) & (df["female"] == 0)].groupby(["name_ethnicity", "name"]).apply(len)
    x4 = df[(df["type"] == 3) & (df["female"] == 0)].groupby(["name_ethnicity", "name"]).apply(len)
    x5 = df[(df["type"] == 4) & (df["female"] == 0)].groupby(["name_ethnicity", "name"]).apply(len)

    y1 = df[(df["type"] == 0) & (df["female"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y2 = df[(df["type"] == 1) & (df["female"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y3 = df[(df["type"] == 2) & (df["female"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y4 = df[(df["type"] == 3) & (df["female"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y5 = df[(df["type"] == 4) & (df["female"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)

    pd.options.display.float_format = '{:,.0f}'.format

    ma_names = np.transpose(pd.DataFrame([x1,x2,x3,x4,x5], 
                                    index=["Type 0","Type 1", "Type 2", "Type 3", "Type 4"])).fillna(value=" ")
    ma_names = ma_names.rename_axis(["Name ethnicity", "Names"])

    fe_names = np.transpose(pd.DataFrame([y1,y2,y3,y4,y5], 
                                    index=["Type 0","Type 1", "Type 2", "Type 3", "Type 4"])).fillna(value=" ")
    fe_names = fe_names.rename_axis(["Name ethnicity", "Names"])

    display_side_by_side(ma_names, fe_names)
    
    
    
def second_tableB():
    
    df = data_set()
    
    x1 = df[(df["type"] == 0) & (df["female"] == 0) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    x2 = df[(df["type"] == 1) & (df["female"] == 0) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    x3 = df[(df["type"] == 2) & (df["female"] == 0) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    x4 = df[(df["type"] == 3) & (df["female"] == 0) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    x5 = df[(df["type"] == 4) & (df["female"] == 0) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)

    y1 = df[(df["type"] == 0) & (df["female"] == 1) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y2 = df[(df["type"] == 1) & (df["female"] == 1) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y3 = df[(df["type"] == 2) & (df["female"] == 1) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y4 = df[(df["type"] == 3) & (df["female"] == 1) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)
    y5 = df[(df["type"] == 4) & (df["female"] == 1) & (df["callback"] == 1)].groupby(["name_ethnicity", "name"]).apply(len)

    pd.options.display.float_format = '{:,.0f}'.format

    ma_names = np.transpose(pd.DataFrame([x1,x2,x3,x4,x5], 
                                    index=["Type 0","Type 1", "Type 2", "Type 3", "Type 4"])).fillna(value=" ")
    ma_names = ma_names.rename_axis(["Name ethnicity", "Names"])

    fe_names = np.transpose(pd.DataFrame([y1,y2,y3,y4,y5], 
                                    index=["Type 0","Type 1", "Type 2", "Type 3", "Type 4"])).fillna(value=" ")
    fe_names = fe_names.rename_axis(["Name ethnicity", "Names"])

    display_side_by_side(ma_names, fe_names)
    


def third_table(df = data_set()):
    
    frame = [[], [], [], [], [], [], [], [], []]
    X = []

    index=["Female", "Top 200 world ranking university", "Extra curricular activities listed", 
           "Fluent in French and other languages", "Canadian master’s degree", "High quality work experience", 
           "List Canadian references", "Accreditation of foreign education", "Permanent resident indicated"]
    
    columns = ["Type 0", "Type 1", "Type 2", "Type 3", "Type 4"]

    types = [0,1,2,3,4,5]

    for i in types:
        
        if i in [0,1,2,3,4]: 
        
            frame[0].append(len(df[(df["type"] == i) & (df["female"] == 1)])/len(df[df["type"] == i]))
            frame[1].append(len(df[(df["type"] == i) & (df["ba_quality"] == 1)])/len(df[df["type"] == i]))
            frame[2].append(len(df[(df["type"] == i) & (df["extracurricular_skills"] == 1)])/len(df[df["type"] == i]))
            frame[3].append(len(df[(df["type"] == i) & (df["language_skills"] == 1)])/len(df[df["type"] == i]))
            frame[4].append(len(df[(df["type"] == i) & (df["ma"] == 1)])/len(df[df["type"] == i]))
            frame[5].append(len(df[(df["type"] == i) & (df["exp_highquality"] == 1)])/len(df[df["type"] == i]))
            frame[6].append(len(df[(df["type"] == i) & (df["reference"] == 1)])/len(df[df["type"] == i]))
            frame[7].append(len(df[(df["type"] == i) & (df["accreditation"] == 1)])/len(df[df["type"] == i]))
            frame[8].append(len(df[(df["type"] == i) & (df["legal"] == 1)])/len(df[df["type"] == i]))
        
        else:
            
            X.append(len(df[df["female"] == 1])/len(df))             
            X.append(len(df[df["ba_quality"] == 1])/len(df))              
            X.append(len(df[df["extracurricular_skills"] == 1])/len(df))              
            X.append(len(df[df["language_skills"] == 1])/len(df))                          
            X.append(len(df[df["ma"] == 1])/len(df))                            
            X.append(len(df[df["exp_highquality"] == 1])/len(df))                       
            X.append(len(df[df["reference"] == 1])/len(df))                           
            X.append(len(df[df["accreditation"] == 1])/len(df))                            
            X.append(len(df[df["legal"] == 1])/len(df))
                    
    pd.options.display.float_format = '{:,.3f}'.format

    fr1 = pd.DataFrame(frame, columns=columns, index=index)
    fr2 = pd.DataFrame(X, columns=["Full sample"], index=index)

    third_table = pd.concat([fr2,fr1], axis=1)
    third_table = third_table.rename_axis("Charactersistics of resume")
    
    
    dfp = pd.DataFrame(df["name_ethnicity"].value_counts()/len(df))
    dfp.set_axis(["Full sample"], axis="columns",inplace=True)
    
    X = []
    for t in [0,1,2,3,4]:

        X.append(df[df["type"] == t].groupby("name_ethnicity").count()["firmid"]/len(df[df["type"] == t]))

    dfd = np.transpose(pd.DataFrame(X,index=("Type 0","Type 1","Type 2","Type 3","Type 4")))
    share_name = pd.concat([dfp,dfd], axis=1)
    share_name.style.set_caption("Test")

    share_name = share_name.rename_axis("Name ethnicity")

    display_side_by_side(third_table,share_name.fillna(0))

    
def count_name_frequency():
    
    df = data_set()
    sns.set_palette("cubehelix",1)
    sns.set_style("whitegrid")
    
    plt.figure(num=None, figsize=(9,6))
    fig = sns.countplot(data=df,x="name_ethnicity", hue="female")
    plt.xlabel("Name ethnicity")
    plt.ylabel("Frequency")
    plt.title("Frequency of Names") 
    plt.show(fig)
