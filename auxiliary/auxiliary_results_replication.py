import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from IPython.display import display_html, HTML

from auxiliary_descriptive_replication import *



def color_highly_significant(value):

    if value == " ":
        color = "black"
        
    elif value < 0.01 and value > 0:
        color = "#4B088A"

    else:
        color = "black"

    return "color: %s" % color



def color_pvalues(value):

    if value == " ":
        color = "black"
        
    elif value < 0.01 and value > 0:
        color= "#8A0808"
        
    elif value < 0.05 and value > 0:
        color = "#088A08"
        
    elif value < 0.1 and value > 0:
        color = "#4B088A"
    
    else:
        color = "black"

    return "color: %s" % color


def color_negative_red(val):
 
    color = 'red' if val < -.05 else 'black'
    return 'color: %s' % color
    
     
def restriction_of_data(df=data_set()):

    df_re1 = df[(df["accreditation"].isna() == True)|(df["reference"].isna() == True) | (df["legal"].isna() == True) | (df["listedaccreditation"].isna() == True)]
    
    df_re2 = df[(df["accreditation"].isna() == False) & (df["reference"].isna() == False) & (df["legal"].isna() == False)]
    
    return df_re1, df_re2
    
    
    
def recall(df = data_set()):
    
    df_re = df[df["fall_data"] == 0].dropna(axis=1)
    mean_re = df_re[df_re["type"] == 0]["callback"].mean()
    
    return mean_re
    
    
    
def data_restriction(df=data_set()):
    
    return df[(df["reference"].isna()==True) | (df["listedaccreditation"].isna()==True) |
              (df["legal"].isna()==True) | (df["accreditation"].isna()==True)]


def fourth_table():
    
    df = data_restriction()
    dfg = data_set()
    
   # df = [rest["fall_data"] == 0]
   # dfg = [full["fall_data"] == 0]
    
    arr = [np.array(["Type 0"]), np.array(["Callback Rates"])]
    names = ["Indian", "Chinese", "Chn-Cdn", "Pakistani", "British", "Greek"]

    t0 = []
    while len(t0) < 7:
        t0.append(recall())
    df0 = pd.DataFrame([t0], columns=range(1,8), index=arr)

    dfI = df[df.name_ethnicity == "Indian"]
    dfP = df[df.name_ethnicity == "Pakistani"]
    dfCh = df[df.name_ethnicity == "Chinese"]
    dfCC = df[df.name_ethnicity == "Chn-Cdn"]
    dfB = df[df.name_ethnicity == "British"]
    dfG = dfg[dfg.name_ethnicity == "Greek"]
    dfIPC = df[(df.name_ethnicity == "Indian") | (df.name_ethnicity == "Pakistani") | 
               (df.name_ethnicity == "Chinese")]

    col = [np.array(["Type 1", "Type 1", "Type 1",
                       "Type 2","Type 2", "Type 2",
                      "Type 3","Type 3", "Type 3",
                      "Type 4","Type 4", "Type 4"]),
             np.array(["Callback Rates", "Difference compared to Type 0", "P-Value",
                      "Callback Rates", "Difference compared to Type 0", "P-Value",
                      "Callback Rates", "Difference compared to Type 0", "P-Value",
                      "Callback Rates", "Difference compared to Type 0", "P-Value"])]
    
    coefI, coefP, coefCh, coefCC, coefG, coefB, coefIPC =  [], [], [], [], [], [], []
    I, P, Ch, CC, G, B, IPC = [], [], [], [], [], [], []

    rsltI = smf.ols('callback ~ C(type)', data=dfI).fit().params
    pvaluesI = smf.ols('dfI["callback"]~C(dfI["type"])', data=dfI).fit().pvalues
    coefI.append([rsltI[0],rsltI[0]+rsltI[1],rsltI[0]+rsltI[2],rsltI[0]+rsltI[3]])

    rsltP = smf.ols('dfP["callback"]~C(dfP["type"])', data=dfP).fit().params
    pvaluesP = smf.ols('dfP["callback"]~C(dfP["type"])', data=dfP).fit().pvalues
    coefP.append([rsltP[0],rsltP[0]+rsltP[1],rsltP[0]+rsltP[2],rsltP[0]+rsltP[3]])
    
    rsltCh = smf.ols(formula='callback~C(type)', data=dfCh).fit().params
    pvaluesCh = smf.ols(formula='callback~C(type)', data=dfCh).fit().pvalues
    coefCh.append([rsltCh[0],rsltCh[0]+rsltCh[1],rsltCh[0]+rsltCh[2],rsltCh[0]+rsltCh[3]])
    
    rsltCC = smf.ols(formula='callback~C(type)', data=dfCC).fit().params
    pvaluesCC = smf.ols(formula='callback~C(type)', data=dfCC).fit().pvalues
    coefCC.append([rsltCC[0],rsltCC[0]+rsltCC[1],rsltCC[0]+rsltCC[2],rsltCC[0]+rsltCC[3]])
    
    rsltG = smf.ols(formula='callback~C(type)', data=dfG).fit().params
    pvaluesG = smf.ols(formula='callback~C(type)', data=dfG).fit().pvalues
    coefG.append([rsltG[0]])
    
    rsltB = smf.ols(formula='callback~C(type)', data=dfB).fit().params
    pvaluesB = smf.ols(formula='callback~C(type)', data=dfB).fit().pvalues
    coefB.append([rsltB[0],rsltB[0]+rsltB[1],rsltB[0]+rsltB[2]])
    
    rsltIPC = smf.ols('callback~C(type)', data=dfIPC).fit().params
    pvaluesIPC = smf.ols('callback~C(type)', data=dfIPC).fit().pvalues
    coefIPC.append([rsltIPC[0],rsltIPC[0]+rsltIPC[1],rsltIPC[0]+rsltIPC[2],rsltIPC[0]+rsltIPC[3]])

    I.append([rsltI[0],coefI[0][0]-t0[0],pvaluesI[0],
                 rsltI[0]+rsltI[1],coefI[0][1]-t0[0],pvaluesI[1],
                 rsltI[0]+rsltI[2],coefI[0][2]-t0[0],pvaluesI[2],
                 rsltI[0]+rsltI[3],coefI[0][3]-t0[0], pvaluesI[3]])
    
    P.append([rsltP[0],coefP[0][0]-t0[1],pvaluesP[0],
                 rsltP[0]+rsltP[1],coefP[0][1]-t0[1],pvaluesP[1],
                 rsltP[0]+rsltP[2],coefP[0][2]-t0[1],pvaluesP[2],
                 rsltP[0]+rsltP[3],coefP[0][3]-t0[1], pvaluesP[3]])
    
    Ch.append([rsltCh[0],coefCh[0][0]-t0[2],pvaluesCh[0],
                 rsltCh[0]+rsltCh[1],coefCh[0][1]-t0[2],pvaluesCh[1],
                 rsltCh[0]+rsltCh[2],coefCh[0][2]-t0[2],pvaluesCh[2],
                 rsltCh[0]+rsltCh[3],coefCh[0][3]-t0[2], pvaluesCh[3]])
    
    CC.append([rsltCC[0],coefCC[0][0]-t0[3],pvaluesCC[0],
                 rsltCC[0]+rsltCC[1],coefCC[0][1]-t0[3],pvaluesCC[1],
                 rsltCC[0]+rsltCC[2],coefCC[0][2]-t0[3],pvaluesCC[2],
                 rsltCC[0]+rsltCC[3],coefCC[0][3]-t0[3], pvaluesCC[3]])
    
    G.append([rsltG[0], coefG[0][0]-t0[4],pvaluesG[0]])
    while len(G[0]) < 12:
        G[0].append(" ")
        
    B.append([" ", " ", " ", 
              rsltB[0],coefB[0][0]-t0[5],pvaluesB[0],
                 rsltB[0]+rsltB[1],coefCC[0][1]-t0[5],pvaluesB[1],
                 rsltB[0]+rsltB[2],coefB[0][2]-t0[5],pvaluesB[2]])
    
    IPC.append([rsltIPC[0],coefIPC[0][0]-t0[6],pvaluesIPC[0],
                 rsltIPC[0]+rsltIPC[1],coefIPC[0][1]-t0[6],pvaluesIPC[1],
                 rsltIPC[0]+rsltIPC[2],coefIPC[0][2]-t0[6],pvaluesIPC[2],
                 rsltIPC[0]+rsltIPC[3],coefIPC[0][3]-t0[6], pvaluesIPC[3]])
   
    pd.options.display.float_format = '{:,.3f}'.format

    dfI = pd.DataFrame(I[0],columns=["Indian"], index=col)
    dfP = pd.DataFrame(P[0],columns=["Pakistani"], index=col)
    dfCh = pd.DataFrame(Ch[0],columns=["Chinese"], index=col)
    dfCC = pd.DataFrame(CC[0],columns=["Chinese with English first name"], index=col)
    dfB = pd.DataFrame(B[0], columns=["English-British"], index=col)
    dfG = pd.DataFrame(G[0], columns=["Greek"], index=col)
    dfIPC = pd.DataFrame(IPC[0],columns=["Indian/Pakistan/Chinese"], index=col)

    D = pd.concat([dfI,dfP,dfCh, dfCC, dfG, dfB, dfIPC],axis=1)
    D = D.style.set_caption("Result 1 — Estimated Callback Rates by Resume Type and Ethnic Origin").applymap(color_highly_significant)
    return D



def callback_graph():
    
    df = data_set()
    
    sns.set_palette("cubehelix", 5)
    sns.set_style("whitegrid")

    fig = sns.catplot(x="callback", hue="type", data=df, kind="count")
    plt.xlabel("Callback")
    plt.ylabel("Frequency")
    plt.title("Frequency of Callbacks among Types") 
    plt.show(fig)
    
    
def mean_callback_by_types():

    df = data_set()
    cb0 = df[df.type == 0]["callback"].mean()
    cb1 = df[df.type == 1]["callback"].mean()
    cb2 = df[df.type == 2]["callback"].mean()
    cb3 = df[df.type == 3]["callback"].mean()
    cb4 = df[df.type == 4]["callback"].mean()

    print("In general, the callback rate equals {:3.3f} for Type 0, {:3.3f} for Type 1, {:3.3f} for Type 2, {:3.3f} for Type 3 and {:3.3f} for Type 4 resumes".format(cb0,cb1,cb2,cb3,cb4))

    
def callback_types_ols(df=data_set()):
    
    df_s = df
    rslt = smf.ols('callback ~ C(type)', data=df_s).fit() 
    print(rslt.summary(title= "Panel A1: Callback Rate Differences without controls"))

    
def show_graph_callback_type():
    
    df_s = data_set()
    sns.set_style("darkgrid")
    plt.figure(figsize=(8,5))

    params = smf.ols('callback ~ C(type)', data=df_s).fit().params
    sd = smf.ols('callback ~ C(type)', data=df_s).fit().bse

    plt.plot([0,1,2,3,4], [params[0], params[1]+params[0],params[2]+params[0],params[3]+params[0],
                           params[4]+params[0]],label="$Y=bT$", ls="--", lw=2)
    plt.plot([0,4], [params[0], params[4]+params[0]], label="Mean Value", lw=2, ls="dotted")

    for i in [1,2,3,4]:
        plt.vlines(x=i,ymin=params[0]+params[i]-sd[i],ymax=params[0]+params[i]+sd[i], color="y")

    plt.legend()
    plt.xlabel("Type")
    plt.ylabel("Callback Rate")
    plt.title("Linearity between Type And Callback Rate")
    plt.show()
    
    
def callback_types_ols_conditioning(df = data_set()):
    
    characteristics = ["additional_credential", "language_skills", "accreditation","reference", "legal",
                      "listedaccreditation", "ma", "ba_quality", "exp_highquality",
                      "extracurricular_skills"]
    
    for c in characteristics:
        for k in ["skillsocialper", "skillspeaking", "skillwriting"]:
            dfc = df[(df[c] == 1) & (df[k] >=60) & (df[k] < 80)]

    print(smf.ols("callback~C(type)", data=dfc).fit().summary(title="Panel A2: Callback Rate Differences with controls"))

    
def corr_map():
    
    plt.figure(figsize=(8,4))
    pd.options.display.float_format = '{:,.3f}'.format


    df = data_set()
    sns.heatmap(df[['callback', 'interview', 'type', 'skillspeaking',
                              'skillsocialper', 'skillwriting', 'ma', 'ba_quality', "extracurricular_skills",
                   "exp_highquality"]].corr(),annot=True, fmt='.1g', linewidths=.2)
    plt.title("Correlation Characteristics")
    plt.show()
    
    
def fifth_table():
    
    df=data_set().sample(7000)
    index = [np.array(["Resume characteristic female", "Resume characteristic female",
                        "Top 200 world ranking university", "Top 200 world ranking university",
                        "List extra curricular activities", "List extra curricular activities",
                        "Fluent in French and other languages", "Fluent in French and other languages",
                       "Canadian master degree", "Canadian master degree",
                       "Multinational firm work experience", "Multinational firm work experience", 
                      "List Canadian references", "List Canadian references",
                      "Accreditation of foreign education","Accreditation of foreign education",
                      "Permanent resident indicated","Permanent resident indicated" ]),
              np.array(["Coef", "P-Value", "Coef", "P-Value", "Coef", "P-Value", "Coef", "P-Value",
                        "Coef", "P-Value", "Coef", "P-Value", "Coef", "P-Value", "Coef", "P-Value", 
                        "Coef", "P-Value"])]

    coef1, p_value1 = [], []
    coef2, p_value2 = [], []
    coef3, p_value3 = [], []
    coef4, p_value4 = [], []
    coef5, p_value5 = [], []
    coef6, p_value6 = [], []
    coef7, p_value7 = [], []
    coef8, p_value8 = [], []
    coef9, p_value9 = [], []

    for t in [0,1,2,3,4]:

        df_t = df[df["type"] == t]

        rslt1 = smf.ols('df_t["callback"] ~ C(df_t["female"])', data=df_t).fit()
        rslt2 = smf.ols('df_t["callback"] ~ C(df_t["ba_quality"])', data=df_t).fit()
        rslt3 = smf.ols('df_t["callback"] ~ C(df_t["extracurricular_skills"])', data=df_t).fit()
        rslt4 = smf.ols('df_t["callback"] ~ C(df_t["language_skills"])', data=df_t).fit()
        rslt5 = smf.ols('df_t["callback"] ~ C(df_t["ma"])', data=df_t).fit()
        rslt6 = smf.ols('df_t["callback"] ~ C(df_t["exp_highquality"])', data=df_t).fit()
        rslt7 = smf.ols('df_t["callback"] ~ C(df_t["reference"])', data=df_t).fit()
        rslt8 = smf.ols('df_t["callback"] ~ C(df_t["accreditation"])', data=df_t).fit()
        rslt9 = smf.ols('df_t["callback"] ~ C(df_t["legal"])', data=df_t).fit()

        coef1.append(rslt1.params[1])
        p_value1.append(rslt1.pvalues[1])

        coef2.append(rslt2.params[1])
        p_value2.append(rslt2.pvalues[1])

        coef3.append(rslt3.params[1])
        p_value3.append(rslt3.pvalues[1])

        coef4.append(rslt4.params[1])
        p_value4.append(rslt4.pvalues[1])

        coef6.append(rslt6.params[1])
        p_value6.append(rslt6.pvalues[1])

        if t == 4:
            coef5.append(" ") 
            p_value5.append(" ")
        else:
            coef5.append(rslt5.params[1])
            p_value5.append(rslt5.pvalues[1])

        if t < 3:
            coef7.append(" ") 
            p_value7.append(" ")
        else:
            coef7.append(rslt7.params[1])
            p_value7.append(rslt7.pvalues[1])

        if t < 2:
            coef8.append(" ") 
            p_value8.append(" ")
        else:
            coef8.append(rslt8.params[1])
            p_value8.append(rslt8.pvalues[1])

        if t < 2:
            coef9.append(" ") 
            p_value9.append(" ")
        else:
            coef9.append(rslt9.params[1])
            p_value9.append(rslt9.pvalues[1])

    pd.options.display.float_format = '{:,.3f}'.format
    
    result = pd.DataFrame([coef1,p_value1,coef2,p_value2,coef3,p_value3,coef4,p_value4,coef5,p_value5,
                               coef6,p_value6, coef7,p_value7, coef8, p_value8, coef9, p_value9],index=index)
    result.set_axis(["Type 0","Type 1","Type 2","Type 3","Type 4"], axis="columns",inplace=True)

    return result.style.set_caption("Result 2 — Estimated Effects on the Probability of Callback from the Inclusion of Specific Resume Characteristics").applymap(color_highly_significant)



def get_skill_differences():
    
    df = data_set().sample(6000)
    df = df[(df.skillspeaking > 10) & (df.skillsocialper > 10) & (df.skillwriting > 10)]
    sns.set_palette("Set2")
    sns.set_style("darkgrid")

    fig, axes = plt.subplots(1, 3, figsize=(16,5))
    sns.boxplot(x = "type", y = "skillspeaking", hue="callback", data=df, ax=axes[0],
                flierprops = dict(markerfacecolor = '0.50', markersize = 2))
    
    sns.boxplot(x = "type", y = "skillsocialper", hue="callback", data=df, 
                ax=axes[1],flierprops = dict(markerfacecolor = '0.50', markersize = 2))
                
    sns.boxplot(x = "type", y = "skillwriting", hue="callback", data=df, ax=axes[2], 
               flierprops = dict(markerfacecolor = '0.50', markersize = 2))

    for (i,j) in zip([0,1,2],["Speaking skill", "Social skill", "Writing skill"]):
        
        axes[i].set_xlabel("Type")
        axes[i].set_ylim(15,105)
        axes[i].set_ylabel(j)
        axes[i].set_title("Average " + j)
        
        if i > 0:
            axes[i].get_legend().set_visible(False)
    
    axes[0].legend(loc='upper center', bbox_to_anchor=(1.7,1.18), ncol=2, fancybox=True, shadow=True)
    plt.show()

def quant_skill_req(df = data_set()):
    
    restr = df.groupby("occupation_type")[["skillwriting", "skillsocialper", "skillspeaking"]].mean()
    restr["Sum of all skills"] = (restr["skillwriting"] + restr["skillsocialper"] + restr["skillspeaking"])/3
    quant = restr["Sum of all skills"].quantile([.1, .2, .3, .4,.5,.6,.7,.8,.9]).to_list()
    
    return quant, restr

def which_occupations():
    
    quant, restr = quant_skill_req()
    
    skill1 = restr[(restr["Sum of all skills"] <= quant[0])].index.to_list()
    skill2 = restr[(restr["Sum of all skills"] <= quant[1]) & (restr["Sum of all skills"] > quant[0])].index.to_list()
    skill3 = restr[(restr["Sum of all skills"] <= quant[2]) & (restr["Sum of all skills"] > quant[1])].index.to_list()
    skill4 = restr[(restr["Sum of all skills"] <= quant[3]) & (restr["Sum of all skills"] > quant[2])].index.to_list()
    skill5 = restr[(restr["Sum of all skills"] <= quant[4]) & (restr["Sum of all skills"] > quant[3])].index.to_list()
    skill6 = restr[(restr["Sum of all skills"] <= quant[5]) & (restr["Sum of all skills"] > quant[4])].index.to_list()
    skill7 = restr[(restr["Sum of all skills"] <= quant[6]) & (restr["Sum of all skills"] > quant[5])].index.to_list()
    skill8 = restr[(restr["Sum of all skills"] <= quant[7]) & (restr["Sum of all skills"] > quant[6])].index.to_list()
    skill9 = restr[(restr["Sum of all skills"] <= quant[8]) & (restr["Sum of all skills"] > quant[7])].index
    skill10 = restr[(restr["Sum of all skills"] > quant[8])].index.to_list()
    
    return skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8, skill9, skill10 #for example

def sixth_table():

    df = data_set()
    
    df1 = df[(df.occupation_type=="Electrical Engineer")|
             (df.occupation_type=="Maintenance Technician")|
             (df.occupation_type=="Programmer")]
    df2 = df[(df.occupation_type=="Civil Engineer")|
             (df.occupation_type=="Technology")]
    df3 = df[(df.occupation_type=="Accounting")|
             (df.occupation_type=="Media and Arts")]
    df4 = df[(df.occupation_type=="Executive Assisstant")|
             (df.occupation_type=="Executive Assistant")]
    df5 = df[(df.occupation_type=="Administrative")|
             (df.occupation_type=="Finance")]
    df6 = df[(df.occupation_type=="Food Services Managers")|
             (df.occupation_type=="Production")]
    df7 = df[(df.occupation_type=="Ecommerce")|
             (df.occupation_type=="Retail")]
    df8 = df[(df.occupation_type=="Clerical")|
             (df.occupation_type=="Human Resources Payroll")]
    df9 = df[(df.occupation_type=="Insurance")|
             (df.occupation_type=="Marketing and Sales")]
    df10 = df[(df.occupation_type=="Biotech and Pharmacy")|
             (df.occupation_type=="Education")|
             (df.occupation_type== "Social Worker")]
    
    coef0, coef1 = [], []
    pvalue0, pvalue1 = [], []
    for data in [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10]:

        coef0.append(smf.ols("callback~C(type)", data=data).fit().params[0])
        coef1.append(smf.ols("callback~C(type)", data=data).fit().params[1])

        pvalue0.append(smf.ols("callback~C(type)", data=data).fit().pvalues[0])
        pvalue1.append(smf.ols("callback~C(type)", data=data).fit().pvalues[1])
        
    pd.options.display.float_format = '{:,.3f}'.format

    index = [np.array(["Type 0", "Type 1","Type 1"]),np.array(["Callback Rate","Callback diff.", "P-Value"])]

    mc = [(1,"EE, MT, P"),(2,"CE, Tec"),(3,"Acc, MA"),(4,"EA"),(5,"Adm, F"),(6,"FSM, Pr"),
          (7,"EcR, R"),(8,"Cl, HR"),(9,"In, MS"),(10,"BPh, Ed, SW")]

    DF = pd.DataFrame([coef0,coef1, pvalue1], index=index, columns=mc)

    DF.columns = pd.MultiIndex.from_tuples(DF.columns, 
                                           names=['Requirement decile','Occupation Sample'])

    DF = DF.style.apply(lambda x: ["background: yellow" if v > 0 and v <= 0.005 else "" for v in x], axis = 1).applymap(color_negative_red).set_caption("Result 3 - Callback Rate Differences for Resumes Sent to Jobs with Different Language and Social Skill Requirements")

    return DF
























