from cgitb import text
from itertools import groupby

import streamlit as st
import pandas as pd
import numpy as np
import calendar
import plotly.graph_objects as go
import datetime
import plotly.express as px
import plotly as py
from plotly.graph_objs import *

st.set_page_config(layout="wide")
@st.cache(allow_output_mutation=True)
def cached_data():
    df_SA = pd.read_csv (r'df_SA.csv')
    df_salary = pd.read_csv (r'salary_sheet.csv')
    df_leave1 = pd.read_csv (r'leave.csv')
    df_hire1=pd.read_csv(r'hires.csv')
    df_st = pd.read_csv (r'Stay vs Jump.csv')
    df_attri = pd.read_csv (r'Attrition.csv')
    df_ter = pd.read_csv (r'Termination.csv')
    return df_SA,df_salary,df_leave1,df_hire1,df_st,df_attri,df_ter

df_SA,df_salary,df_leave1,df_hire1,df_st,df_attri,df_ter=cached_data()

def page1_st(): 
    rev=df_SA['Revenue'].sum()
    cp=df_SA['Cost Price'].sum()
    ep=df_SA['Expense'].sum()
    inc=df_SA['Operating Income'].sum()
    incp=(100/(df_SA['Revenue']).sum()) * (df_SA['Operating Income'].sum())
    st.markdown("<h2 style='text-align: center; color: black;'>Income Statement</h2>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:

        st.markdown("<h4 style='text-align: center; color: black;'>Revenue </h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(round(rev/1000000,2))+"M"+"</h4>", unsafe_allow_html=True)
    with col2:

        st.markdown("<h4 style='text-align: center; color: black;'>Cost to the Company </h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(round(cp/1000000,2))+"M"+"</h4>", unsafe_allow_html=True)
    with col3:
    
        st.markdown("<h4 style='text-align: center; color: black;'>Expenses </h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(round(ep/1000000,2))+"M"+"</h4>", unsafe_allow_html=True)
    with col4:
    
        st.markdown("<h4 style='text-align: center; color: black;'>Operating Income </h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(round(inc/1000000,2))+"M"+"</h4>", unsafe_allow_html=True)
    with col5:
    
        st.markdown("<h4 style='text-align: center; color: black;'>Income % </h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(round(incp,2))+"%"+"</h4>", unsafe_allow_html=True)

    list1=df_SA['Month'].tolist()
    list11=list1.append('Total')
    list2=df_SA['Operating Income'].tolist()
    list22=list2.append((df_SA['Operating Income'].sum()))


    fig = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "relative", "relative","relative","relative","relative","relative","relative","relative","total"],
        x=list1,
        textposition = "outside",
        text=list2,
        y=list2,
        connector = {"line":{"color":"rgb(63, 63, 63)"}}
    ))

    st.markdown('-------------------------------------------------')

    col1= st.columns(1)
    st.markdown("<h3 style='text-align: center; color: black;'>Operating Income In Each Month</h3>", unsafe_allow_html=True)

    fig.update_layout(
        autosize=False,
        width=1900,
        height=600,
        margin=dict(
            l=20,
            r=20,
            b=20,
            t=20,
            pad=6),xaxis_title="Month Name",
    yaxis_title="Operating Income in Million")

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig)

def page2_st():

    st.markdown("<h2 style='text-align: center; color: black;'>Financial Simulator</h2>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
    st.markdown('')
    col1, col2, col3 = st.columns(3)
    with col1:
        value1 = st.slider(
            'The company Provides the Hike',
            -100, 100,0,5) 
    with col2:
        st.markdown("<h2 style='text-align: center; color: black;'>What IF</h2>", unsafe_allow_html=True)   
    with col3:
            value2 = st.slider(
            'The company change the expense',
            -100, 100,0,5) 
    st.markdown('-------------------------------------------------')
    
    st.markdown("<h3 style='text-align: center; color: black;'>Metrics</h3>", unsafe_allow_html=True)   
    st.markdown('')
    st.markdown('')


    sec1, sec2, sec3,sec4,sec5 = st.columns(5)
    var_rev=0
    var_cp= round(((1+value1/100) * df_SA['Cost Price'].sum()) - df_SA['Cost Price'].sum())      
    var_exp=  round(((1+value2/100) * df_SA['Expense'].sum()) - df_SA['Expense'].sum())
    var_inc=var_rev-var_cp-var_exp
    var_incp= round((100/df_SA['Operating Income'].sum())* var_inc)

    with sec1:


        st.markdown("<h4 style='text-align: center; color: black;'>Revenue Varience</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(var_rev)+"</h4>", unsafe_allow_html=True)

    with sec2:
        st.markdown("<h4 style='text-align: center; color: black;'>Cost Varience</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(var_cp)+"</h4>", unsafe_allow_html=True)

    with sec3:
        st.markdown("<h4 style='text-align: center; color: black;'>Expense Varience</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(var_exp)+"</h4>", unsafe_allow_html=True)

    with sec4:
        st.markdown("<h4 style='text-align: center; color: black;'>Income Varience</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(var_inc)+"</h4>", unsafe_allow_html=True)

    with sec5:
        st.markdown("<h4 style='text-align: center; color: black;'>Income % Varience</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(var_incp)+"</h4>", unsafe_allow_html=True)

    st.markdown('-------------------------------------------------')
    st.markdown("<h3 style='text-align: center; color: black;'>Original Metrics</h3>", unsafe_allow_html=True)   
    st.markdown('')
    st.markdown('')

    seg1, seg2, seg3,seg4,seg5 = st.columns(5)

    act_rev= round(df_SA['Revenue'].sum())
    act_cp= df_SA['Cost Price'].sum()    
    act_exp=df_SA['Expense'].sum()
    act_inc=round((act_rev-act_cp-act_exp))
    act_incp=round((100/(df_SA['Revenue']).sum()) * (df_SA['Operating Income'].sum()),2)

    with seg1:
        st.markdown("<h4 style='text-align: center; color: black;'>Annual Revenue</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(act_rev)+"</h4>", unsafe_allow_html=True)

    with seg2:
        st.markdown("<h4 style='text-align: center; color: black;'>Actual Cost</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(act_cp)+"</h4>", unsafe_allow_html=True)


    with seg3:
        st.markdown("<h4 style='text-align: center; color: black;'>Actual Expense</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(act_exp)+"</h4>", unsafe_allow_html=True)

    with seg4:
        st.markdown("<h4 style='text-align: center; color: black;'>Actual Income</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(act_inc)+"</h4>", unsafe_allow_html=True)

    with seg5:
        st.markdown("<h4 style='text-align: center; color: black;'>Actual Income %</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(act_incp)+"</h4>", unsafe_allow_html=True)


    st.markdown('-------------------------------------------------')
    st.markdown("<h3 style='text-align: center; color: black;'>Resultant Metrics</h3>", unsafe_allow_html=True)   
    st.markdown('')
    st.markdown('')

    segm1, segm2, segm3,segm4,segm5 = st.columns(5)
    re_rev= var_rev+act_rev
    re_cp= var_cp+act_cp   
    re_exp=var_exp+act_exp
    re_inc=round((var_inc+act_inc),2)
    re_incp=round((100/re_rev)* re_inc,2)

    with segm1:
        st.markdown("<h4 style='text-align: center; color: black;'>Resultant Revenue</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(re_rev)+"</h4>", unsafe_allow_html=True)


    with segm2:
        st.markdown("<h4 style='text-align: center; color: black;'>Resultant Cost</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(re_cp)+"</h4>", unsafe_allow_html=True)

    with segm3:
        st.markdown("<h4 style='text-align: center; color: black;'>Resultant Expense</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(re_exp)+"</h4>", unsafe_allow_html=True)

    with segm4:
        st.markdown("<h4 style='text-align: center; color: black;'>Resultant Income</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(re_inc)+"</h4>", unsafe_allow_html=True)

    with segm5:
        st.markdown("<h4 style='text-align: center; color: black;'>Resultant Income %</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$ "+str(re_incp)+"</h4>", unsafe_allow_html=True)


    st.markdown('-------------------------------------------------')

def page3_st():
    # df_salary = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\salary_sheet.csv')
    st.markdown("<h2 style='text-align: center; color: black;'>Salary Analysis</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')

    segm1, segm2, segm3 = st.columns(3)
    avg_sal=df_salary['Salary'].mean()
    tot_sal=df_salary['Salary'].sum()
    sec1, sec2,sec3= st.columns(3)

    with sec1:

        st.markdown("<h4 style='text-align: center; color: black;'>Average Salary</h4>", unsafe_allow_html=True)   
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(round(avg_sal/1000000,2))+"M"+"</h4>", unsafe_allow_html=True)   

    with sec3:

        st.markdown("<h4 style='text-align: center; color: black;'>Total Salary</h4>", unsafe_allow_html=True)   
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(round(tot_sal/1000000000,2))+"B"+"</h4>", unsafe_allow_html=True)   
    st.markdown('-------------------------------------------------')

    segm1, segm2, segm3 = st.columns(3)

    with segm1:
        st.markdown("")
        st.markdown("")

        st.markdown("<h4 style='text-align: center; color: black;'>Average Salary By Business Unit</h4>", unsafe_allow_html=True)   

        df_avg_bu=df_salary.groupby(["Bu"],as_index=False)['Salary'].mean()
        df_avg_bu=df_avg_bu.sort_values(by='Salary')


        fig1 = px.bar(df_avg_bu, x='Salary', y='Bu',orientation='h',text=df_avg_bu['Salary']//1000000)
        fig1.update_layout(height=500,width=600,xaxis_title="Salary in Million",
        yaxis_title="Business Unit")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)
    with segm2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Total Salary By Business Unit</h4>", unsafe_allow_html=True)   
        df_avg_bu=df_salary.groupby(["Bu"],as_index=False)['Salary'].sum()
        df_avg_bu= df_avg_bu.sort_values(by='Salary')
        df_avg_bu=df_avg_bu.sort_values(by='Salary')

        fig1 = px.bar(df_avg_bu, y='Salary', x='Bu',orientation='v',text=df_avg_bu['Salary']//1000000)
        fig1.update_layout(height=500,width=600,yaxis_title="Salary in Million",
        xaxis_title="Business Unit")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)


    with segm3:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Average Salary By Year</h4>", unsafe_allow_html=True)   
    
        df_avg_bu=df_salary.groupby(["Year"],as_index=False)['Salary'].sum()

        fig = px.line(df_avg_bu, x=['2018','2019','2020','2021'],y=df_avg_bu['Salary']//1000000)    
        fig.update_layout(height=500,width=600,xaxis_title="Year",
        yaxis_title="Salary in Million")
        fig.data[0].line.color = "#0C3B5D"

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)
    with segm1:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Average Salary By Gender</h4>", unsafe_allow_html=True)   

        df_avg_bu=df_salary.groupby(["Gender"],as_index=False)['Salary'].mean()
        labels = df_avg_bu['Gender']
        values = df_avg_bu['Salary']

        colours = ["#0C3B5D","#3EC1CD"]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig.update_traces(marker=dict(colors=colours), legendgrouptitle_text="Gender")            
        fig.update_layout(height=500,width=600)
        st.plotly_chart(fig)        
    with segm2:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Average Salary By Location</h4>", unsafe_allow_html=True)   
        df_avg_bu=df_salary.groupby(["Location"],as_index=False)['Salary'].sum()
        df_avg_bu= df_avg_bu.sort_values(by='Salary')



        fig1 = px.bar(df_avg_bu, x='Salary', y='Location',orientation='h',text=df_avg_bu['Salary']//1000000)
        fig1.update_layout(height=500,width=600,xaxis_title="Salary in Million",
        yaxis_title="Location")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)

    
    with segm3:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Average Salary By Organization Level</h4>", unsafe_allow_html=True)   
        df_avg_bu=df_salary.groupby(["Organization_Level"],as_index=False)['Salary'].sum()
        

        colours = ["#0C3B5D","#3EC1CD","5584AC"]

        fig = go.Figure(data=[go.Pie(labels=df_avg_bu['Organization_Level'], values=df_avg_bu['Salary'])])
        fig.update_traces(marker=dict(colors=colours), legendgrouptitle_text="Organization_Level")            
        fig.update_layout(height=500,width=600)
        st.plotly_chart(fig)

def page4_st():
    # df_salary = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\salary_sheet.csv')
    st.markdown("<h2 style='text-align: center; color: black;'>Training</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')
    segm1, segm2, segm3, segm4, segm5 = st.columns(5)
    df_tr=df_salary.groupby(["Completed_Program"],as_index=False)['Salary'].count()
    df_ty=df_salary.groupby(["Training Type"],as_index=False)['Participants'].count()
    df_cp=df_salary.groupby(["Completed_Program"],as_index=False)['Training Cost'].sum()
    df_mon=df_salary.groupby(["Month","Month1"],as_index=False)['Hours'].sum()

    with segm1:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Training Program</h4>", unsafe_allow_html=True)   
        str1=str(df_tr['Completed_Program'].count())
        st.markdown("<h4 style='text-align: center; color: black;'>"+str1+"</h4>", unsafe_allow_html=True)   

    with segm2:
        st.markdown("")
        st.markdown("")

        st.markdown("<h4 style='text-align: center; color: black;'>Participants</h4>", unsafe_allow_html=True)   
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(df_salary['Participants'].sum())+"</h4>", unsafe_allow_html=True)   
    with segm3:
        st.markdown("")
        st.markdown("")

        st.markdown("<h4 style='text-align: center; color: black;'>Training Cost</h4>", unsafe_allow_html=True)   
        st.markdown("<h4 style='text-align: center; color: black;'>"+"$"+" "+str(df_cp['Training Cost'].sum()//1000)+"K"+"</h4>", unsafe_allow_html=True)   
    with segm4:
        st.markdown("")
        st.markdown("")
    
        st.markdown("<h4 style='text-align: center; color: black;'>Training Hours</h4>", unsafe_allow_html=True)   
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(df_mon['Hours'].sum())+"</h4>", unsafe_allow_html=True)     
    with segm5:
        st.markdown("")
        st.markdown("")

        st.markdown("<h4 style='text-align: center; color: black;'>Total days</h4>", unsafe_allow_html=True)   
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(df_salary['Date'].count())+"</h4>", unsafe_allow_html=True)     

    st.markdown("")
    st.markdown("")  
    st.markdown("-----------------------------------------------------------")  
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    sec1,sec2,sec3,sec4=st.columns(4)
    with sec1:

        st.markdown("<h4 style='text-align: center; color: black;'>Participants By Training Type</h4>", unsafe_allow_html=True)   

        labels = df_ty['Training Type']
        values = df_ty['Participants']

        colours = ["#0C3B5D","#3EC1CD"]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])

        fig.update_traces(marker=dict(colors=colours), legendgrouptitle_text="Training Type")            
        fig.update_layout(height=500,width=500)

        st.plotly_chart(fig)
    with sec2:
        st.markdown("<h4 style='text-align: center; color: black;'>Participants By Training Program</h4>", unsafe_allow_html=True)   

        df_tr=df_tr.sort_values(by=['Salary'])

        
        fig1 = px.bar(df_tr, y='Completed_Program', x='Salary',orientation='h',text=df_tr['Salary'])
        fig1.update_layout(height=500,width=600,xaxis_title="Salary in Million",
        yaxis_title="Completed Program")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)

    with sec3:
        st.markdown("<h4 style='text-align: center; color: black;'>Training Cost By Program</h4>", unsafe_allow_html=True)   

        df_cp=df_cp.sort_values(by=['Training Cost'])


        fig1 = px.bar(df_cp, y='Completed_Program', x='Training Cost',orientation='h',text=df_cp['Training Cost']/1000)
        fig1.update_layout(height=500,width=600,xaxis_title="Training Cost in Thousands",
        yaxis_title="Completed Program")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)
    with sec4:
        st.markdown("<h4 style='text-align: center; color: black;'>Training Hours By Month</h4>", unsafe_allow_html=True)   
        df_cp=df_cp.sort_values(by=['Training Cost'])

        fig1 = px.bar(df_mon, y='Hours', x='Month1',orientation='v',text=df_mon['Hours'])
        fig1.update_layout(height=500,width=600,xaxis_title="Month",
        yaxis_title="Training Hours")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)

def page5_st():
    st.markdown("<h2 style='text-align: center; color: black;'>Termination Analysis</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')
    st.markdown("")
    st.markdown("")


    df_op=df_leave1.groupby(["Gender","Business unit","Date","Organization level"],as_index=False)['Termination Id'].count()
    df_op=df_op.sort_values(by="Date")

    sec1,sec2,sec3=st.columns(3)
    seg1,seg2,seg3=st.columns(3)
    se1,se2,se3=st.columns(3)

    with sec1:
        op=df_leave1["Termination Id"].count()
        st.markdown("<h4 style='text-align: center; color: black;'>Total Termination</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(op)+"</h4>", unsafe_allow_html=True)


    with sec3:
        op=round(df_leave1["Termination Id"].count()/1024)
        st.markdown("<h4 style='text-align: center; color: black;'>Average Leaver per Day</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(op)+"</h4>", unsafe_allow_html=True)
    
    with seg1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        s_date=st.selectbox("Start Date",df_op["Date"].tolist())


    with seg2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")

        e_date=st.selectbox("End Date",df_op["Date"].tolist())



    with seg3:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        bu= st.multiselect("Select Business Unit",list(set(df_op["Business unit"].tolist())),list(set(df_op["Business unit"].tolist())))
        df_op=df_op[(df_op['Date'] > s_date) & (df_op['Date'] < e_date) ]
    df_op=df_op.sort_values(by="Date")
    st.markdown("-----------------------------------")  


    with se1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Leavers By Job Level</h4>", unsafe_allow_html=True)
        df_jl= df_op.groupby(["Gender","Organization level"],as_index=False)["Termination Id"].sum()

        colours = {
                "Female": "#0C3B5D",
                "Male": "#3EC1CD"
            }
        fig = px.histogram(
                df_jl,
                x="Organization level",
                y="Termination Id",
                color="Gender",
                barmode="group",
                orientation="v",
                color_discrete_map=colours,text_auto=True
            )
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.update_layout(height=500,width=600,xaxis_title="Organization Level",
            yaxis_title="Terminations")
            
        st.plotly_chart(fig)

    with se2:

        st.markdown("")
        st.markdown("")  
        st.markdown("")
        st.markdown("")  
        st.markdown("")
        st.markdown("")  
        st.markdown("")  
        st.markdown("")  
        st.markdown("<h4 style='text-align: center; color: black;'>Leavers Trend By Gender</h4>", unsafe_allow_html=True)

        df_tr=df_leave1.groupby(["Year","QuarterYear","Gender","Business unit"],as_index=False)["Termination Id"].count()
        df_tr=df_tr[df_tr["Business unit"].isin(bu)]  
        df_tr=df_tr.groupby(["Gender","QuarterYear"],as_index=False)["Termination Id"].sum()  
        df_tr=df_tr.sort_values(by="QuarterYear")
        colours = {
                "Female": "#0C3B5D",
                "Male": "#3EC1CD"
            }
        df = px.data.gapminder().query("continent=='Oceania'")
        fig = px.line(df, y=df_tr["Termination Id"].tolist(), x=df_tr["QuarterYear"].tolist(), color=df_tr["Gender"].tolist(),color_discrete_map=colours)
        fig.update_layout(height=450,width=600,xaxis_title="Quarter",
            yaxis_title="Terminations")
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)
    with se3:

        st.markdown("")
        st.markdown("")  
        st.markdown("")
        st.markdown("")  
        st.markdown("")
        st.markdown("")  
        st.markdown("")
        st.markdown("")

        st.markdown("<h4 style='text-align: center; color: black;'>Leavers By Business Unit</h4>", unsafe_allow_html=True)

        colours = {
                "Business unit": "#0C3B5D",
    
            }
        df_op=df_leave1.groupby(["Business unit"],as_index=False)["Termination Id"].count()
        df_op["% of leavers"]=round((df_op["Termination Id"]/df_op["Termination Id"].sum())*100)
        df_op=df_op[df_op["Business unit"].isin(bu)]  
        df_op=df_op.sort_values(by="% of leavers")
        fig1 = go.Figure(go.Bar(
                    y=df_op['Business unit'].tolist(),
                    x=df_op['% of leavers'].tolist(),
                    orientation='h',text=df_op["Termination Id"]))
        fig1.update_layout(height=500,width=600,xaxis_title="Terminations",
            yaxis_title="Business Unit")
        fig1.update_traces(marker_color="#3EC1CD")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        st.plotly_chart(fig1)
    with se1:
        st.markdown("")
        st.markdown("")

        st.markdown("<h4 style='text-align: center; color: black;'>Leavers By Age Category</h4>", unsafe_allow_html=True)

        df_op=df_leave1.groupby(["Age Range","Business unit","Gender"],as_index=False)["Termination Id"].count()
        df_op=df_op[df_op["Business unit"].isin(bu)] 
        df_op=df_op.groupby(["Age Range","Gender"],as_index=False)["Termination Id"].sum()
        df_op=df_op.sort_values(by='Age Range')

        colours = {
                "Male": "#0C3B5D",
                "Female": "#3EC1CD"
            }
        fig1 = px.bar(df_op, x="Age Range", y="Termination Id", color='Gender',orientation='v',color_discrete_map=colours,text=df_op["Termination Id"])


        fig1.update_layout(height=500,width=600,xaxis_title="Age Category",
            yaxis_title="Terminations")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)       
        st.plotly_chart(fig1)

    with se2:
        st.markdown("")
        st.markdown("")      
        st.markdown("")
        st.markdown("")      
        st.markdown("")      

        st.markdown("<h4 style='text-align: center; color: black;'>Hires Vs Leavers</h4>", unsafe_allow_html=True)

        # df_hire=pd.read_csv(r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\hires.csv')
        df_hire=df_hire1.groupby(["QuarterYear"],as_index=False)["Hire"].sum()
        df_leave=df_leave1.groupby(["QuarterYear","Date","Business unit"],as_index=False)["Termination Id"].count()
        df_leave=df_leave.groupby(["QuarterYear","Business unit"],as_index=False).sum()
        df_merg=pd.merge(df_leave,df_hire,on="QuarterYear",how='inner')
        df_merg=df_merg[df_merg["Business unit"].isin(bu)] 
        df_merg=df_merg.groupby(["QuarterYear"],as_index=False).sum() 
        colours = {
                'Termination Id': "#0C3B5D",
                'Hire': "#3EC1CD"
            }
        fig = px.line(df_merg, x='QuarterYear', y=['Termination Id', 'Hire'],color_discrete_map=colours)    
        fig.update_layout(height=450,width=650,xaxis_title="Quarter Year",
            yaxis_title="Hires and Leavers")
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(fig)
    with se3:
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Leavers By Location</h4>", unsafe_allow_html=True)

        # df_leave = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\leave.csv')
        # df_leave=df_leave1
        df_p=df_leave1.groupby(["Business unit","Country"],as_index=False)["Termination Id"].count()
        df_p=df_p[df_p["Business unit"].isin(bu)] 
        df_p=df_p.groupby(["Country"],as_index=False)["Termination Id"].sum()
        df_p=df_p.sort_values(by="Termination Id") 

        fig1 = px.bar(df_p, y='Termination Id', x='Country',text=df_p["Termination Id"])
        fig1.update_layout(height=500,width=600,xaxis_title="Country",
            yaxis_title="Terminations")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)


def page6_st():

    st.markdown("<h2 style='text-align: center; color: black;'>Attrition Summary</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')
    st.markdown("")
    st.markdown("")

    seg1,seg2,seg3,seg4,seg5,seg6,seg7,seg8,seg9,seg10,seg11,seg12,seg13,seg14,seg15,seg16=st.columns(16)
    sec1,sec2,sec3=st.columns(3)

    def vis1(vi1):

        with sec1:
            st.markdown("")
            st.markdown("")
            st.markdown("<h4 style='text-align: center; color: black;'>Attrition Rate by Distance</h4>", unsafe_allow_html=True)

            vi1["Attrition Rate"]=round(((vi1["Age"]/vi1["Age"].sum())*100),2)
    
            colours = {
                "No": "#0C3B5D",
                "Yes": "#3EC1CD"
            }
            fig = px.histogram(
                vi1,
                x="Dist Band",
                y="Attrition Rate",
                color="Attrition",
                barmode="group",
                orientation="v",
                color_discrete_map=colours,text_auto=True
            )
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            fig.update_layout(height=500,width=600,xaxis_title="Distance Band",
            yaxis_title="Attrition Rate")
            
            st.plotly_chart(fig)
    def vis2(vi2):
        with sec2:
            st.markdown("")
            st.markdown("")
            st.markdown("<h4 style='text-align: center; color: black;'>Attrition Rate by Over Time</h4>", unsafe_allow_html=True)
            vi2=vi2.groupby(["OverTime"],as_index=False).sum()
            labels = vi2['OverTime']
            values = vi2['Attrition']
            colours = ["#0C3B5D","#3EC1CD"]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
            fig.update_traces(marker=dict(colors=colours), legendgrouptitle_text="Attrition")            
            fig.update_layout(height=500,width=500)

            st.plotly_chart(fig)
    def vis3(vi1):
        with sec3:
            st.markdown("")
            st.markdown("")
            st.markdown("<h4 style='text-align: center; color: black;'>Attrition Rate by Companies Worked</h4>", unsafe_allow_html=True)
            vi1["Attrition Rate"]=round(((vi1["Age"]/vi1["Age"].sum())*100),2)
        
            colours = {
                "No": "#0C3B5D",
                "Yes": "#3EC1CD"
            }
            fig = px.histogram(
                vi1,
                x="Worked Band",
                y="Attrition Rate",
                color="Attrition",
                barmode="group",
                orientation="v",
                color_discrete_map=colours,
                labels={"Worked Band":"Companies Worked"},text_auto=True
            )
        
            fig.update_layout(height=500,width=600,xaxis_title="Companies Worked",
            yaxis_title="Attrition Rate")
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            st.plotly_chart(fig)

    def vis4(vi1):

        with sec1:
            st.markdown("<h4 style='text-align: center; color: black;'>Attrition Rate by Business Travel</h4>", unsafe_allow_html=True)
            vi1["Attrition Rate"]=round(((vi1["Age"]/vi1["Age"].sum())*100),2)
            colours = {
                "No": "#0C3B5D",
                "Yes": "#3EC1CD"
            }
            fig = px.histogram(
                vi1,
                x="Attrition Rate",
                y="BusinessTravel",
                color="Attrition",
                barmode="group",
                orientation="h",
                color_discrete_map=colours,text_auto=True
            )
        
            fig.update_layout(height=500,width=600,xaxis_title="Attrition Rate",
            yaxis_title="Business Travel")
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)            
            st.plotly_chart(fig)
    def vis5(vi1):

        with sec2:
            colours = {
                "No": "#0C3B5D",
                "Yes": "#3EC1CD"
            }

            st.markdown("<h4 style='text-align: center; color: black;'>Attrition Rate by Department</h4>", unsafe_allow_html=True)
            fig = px.bar(vi1, x="Department", y="Age", color='Attrition',color_discrete_map=colours,text=vi1["Age"])
            fig.update_layout(height=500,width=600,xaxis_title="Department",
            yaxis_title="Attrition Rate")
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            st.plotly_chart(fig)
    def vis6(vi1):

        with sec3:
            st.markdown("<h4 style='text-align: center; color: black;'>Attrition Rate by Years Spent</h4>", unsafe_allow_html=True)
            colours = {
                "No": "#0C3B5D",
                "Yes": "#3EC1CD"
            }
            vi1["Attrition Rate"]=round(((vi1["Age"]/vi1["Age"].sum())*100),2)
            fig = px.bar(vi1, x="Attrition Rate", y="Current role_Band", color='Attrition',orientation='h',color_discrete_map=colours,text='Attrition Rate')
            fig.update_layout(height=500,width=600,xaxis_title="Attririon Rate",
            yaxis_title="Years Spent")
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=False)
            st.plotly_chart(fig)



    with seg8:
        if st.button('Male'):
            df_vis1=df_attri.groupby(["Attrition","Dist Band","Gender"],as_index=False)["Age"].count()
            df_vis1=df_vis1[df_vis1["Gender"]=="Male"]
            df_vis2=df_attri.groupby(["Attrition","OverTime","Gender"],as_index=False)["Attrition"].count()
            df_vis2=df_vis2[df_vis2["Gender"]=="Male"]
            df_vis3=df_attri.groupby(["Attrition","Worked Band","Gender"],as_index=False)["Age"].count()
            df_vis3=df_vis3[df_vis3["Gender"]=="Male"]     
            df_vis4=df_attri.groupby(["Attrition","BusinessTravel","Gender"],as_index=False)["Age"].count()
            df_vis4=df_vis4[df_vis4["Gender"]=="Male"]       
            df_vis5=df_attri.groupby(["Attrition","Department","Gender"],as_index=False)["Age"].count()
            df_vis5=df_vis5[df_vis5["Gender"]=="Male"] 
            df_vis6=df_attri.groupby(["Attrition","Current role_Band","Gender"],as_index=False)["Age"].count()
            df_vis6=df_vis6[df_vis6["Gender"]=="Male"] 
            vis1(df_vis1)
            vis2(df_vis2)
            vis3(df_vis3)
            vis4(df_vis4)
            vis5(df_vis5)

            vis6(df_vis6)


    with seg9:
        if st.button('Female'):
            df_vis1=df_attri.groupby(["Attrition","Dist Band","Gender"],as_index=False)["Age"].count()
            df_vis1=df_vis1[df_vis1["Gender"]=="Female"]
            df_vis2=df_attri.groupby(["Attrition","OverTime","Gender"],as_index=False)["Attrition"].count()
            df_vis2=df_vis2[df_vis2["Gender"]=="Female"]
            df_vis3=df_attri.groupby(["Attrition","Worked Band","Gender"],as_index=False)["Age"].count()
            df_vis3=df_vis3[df_vis3["Gender"]=="Female"]    
            df_vis4=df_attri.groupby(["Attrition","BusinessTravel","Gender"],as_index=False)["Age"].count()
            df_vis4=df_vis4[df_vis4["Gender"]=="Female"]
            df_vis5=df_attri.groupby(["Attrition","Department","Gender"],as_index=False)["Age"].count()
            df_vis5=df_vis5[df_vis5["Gender"]=="Female"]
            df_vis6=df_attri.groupby(["Attrition","Current role_Band","Gender"],as_index=False)["Age"].count()
            df_vis6=df_vis6[df_vis6["Gender"]=="Female"]             
            vis1(df_vis1)
            vis2(df_vis2)
            vis3(df_vis3)
            vis4(df_vis4)
            vis5(df_vis5)

            vis6(df_vis6)
def page7_st():
    # df_attr = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\Stay vs Jump.csv')
    st.markdown("<h2 style='text-align: center; color: black;'>Stay Vs Jump</h2>", unsafe_allow_html=True)
    df_attr=df_st
    df_stay=df_attr[df_attr["Probability"]=="Likely to Stay"]['Probability'].count()
    df_jump=df_attr[df_attr["Probability"]=="Likely to Jump"]['Probability'].count()

    st.markdown("")
    st.markdown("")
    st.markdown("")
    sec1,sec2 = st.columns(2)
    with sec1:
            st.markdown("<h4 style='text-align: center; color: black;'>Likely to Stay</h4>", unsafe_allow_html=True)
            st.markdown("<h4 style='text-align: center; color: black;'>"+str(df_stay)+"</h4>", unsafe_allow_html=True)
            

    with sec2:
        st.markdown("<h4 style='text-align: center; color: black;'>Likely to Jump</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(df_jump)+"</h4>", unsafe_allow_html=True)

    st.markdown("--------------------------------------------")
    df_attr=df_attr.sort_values(by='EmployeeNumber')
    fig = go.Figure(data=[go.Table(header=dict(values=['EmployeeNumber', 'Department','JobLevel','JobRole','EducationField','Probability'],line_color='darkslategray',
                fill_color='lightskyblue',font=dict(size=18)),
                cells=dict(values=[df_attr['EmployeeNumber'].tolist(), df_attr['Department'].tolist(),df_attr['JobLevel'].tolist(),df_attr['JobRole'].tolist(),df_attr['EducationField'].tolist(),df_attr['Probability'].tolist()],line_color='darkslategray',
            fill_color='lightcyan'))
                    ])
    fig.update_traces(cells_font=dict(size = 16))

    fig.update_layout(width=2100, height=1200)
    st.plotly_chart(fig)

# def page8_st():
#     df_attri = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\Stay vs Jump.csv')

#     st.markdown("<h2 style='text-align: center; color: black;'>Risk Analysis</h2>", unsafe_allow_html=True)


#     st.markdown("")
#     st.markdown("")
#     st.markdown("")

    
#     fig = go.Figure(data=[go.Table(header=dict(values=['EmployeeNumber', 'Department','JobLevel','JobRole','EducationField']),
#                 cells=dict(values=[df_attri['EmployeeNumber'].tolist(), df_attri['Department'].tolist(),df_attri['JobLevel'].tolist(),df_attri['JobRole'].tolist(),df_attri['EducationField'].tolist()]))])
#     df_attri=df_attri.sort_values(by='EmployeeNumber')

#     fig.update_traces(cells_font=dict(size = 16))

#     fig.update_layout(width=1500, height=1200)
#     st.plotly_chart(fig)


def page9_st():

    # df_ter = pd.read_csv (r'C:\Users\Jeevanandam\Desktop\HR Analytics\HR-Dashboard\Termination.csv')

    st.markdown("<h2 style='text-align: center; color: black;'>Termination Profile</h2>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')
    st.markdown("")
    st.markdown("")

    df_op=df_ter.sort_values(by="Date")

    sec1,sec2,sec3=st.columns(3)
    se1,se2,se3=st.columns(3)
    seg1,seg2,seg3=st.columns(3)

    
    with sec2:

        st.markdown("")
        st.markdown("")

        s_date=st.selectbox("Start Date",df_op["Date"].tolist())


    with sec3:

        st.markdown("")
        st.markdown("")


        e_date=st.selectbox("End Date",df_op["Date"].tolist())
    with sec1:
        df_dt=df_op[(df_ter['Date'] > s_date) & (df_op['Date'] < e_date)]
        op=df_dt["Termination Id"].count()
        st.markdown("<h4 style='text-align: center; color: black;'>Total Termination</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: black;'>"+str(op)+"</h4>", unsafe_allow_html=True)
    st.markdown('-------------------------------------------------')

    
    with se1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")       
        df_gen=df_op.groupby(["Gender","Date"],as_index=False)["Termination Id"].count()
        df_gen=df_gen[(df_gen['Date'] > s_date) & (df_gen['Date'] < e_date)]
        df_gen=df_gen.groupby(["Gender"],as_index=False)["Termination Id"].sum()
        st.markdown("<h4 style='text-align: center; color: black;'>Termination by Gender</h4>", unsafe_allow_html=True)

        colours = ["#0C3B5D","#3EC1CD"]
        fig = go.Figure(data=[go.Pie(labels=df_gen["Gender"], values=df_gen["Termination Id"], hole=.5)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value')
        fig.update_traces(marker=dict(colors=colours), legendgrouptitle_text="Gender")            
        
        fig.update_layout(height=500,width=500)        
        st.plotly_chart(fig)

    with se2:
        st.markdown("")
        st.markdown("")      
        st.markdown("")
        st.markdown("")      
        st.markdown("")      
        st.markdown("")      
        st.markdown("")    
        st.markdown("<h4 style='text-align: center; color: black;'>Termination by Organization Level</h4>", unsafe_allow_html=True)
        df_gen=df_op.groupby(["Organization level","Date"],as_index=False)["Termination Id"].count()
        df_gen=df_gen[(df_gen['Date'] > s_date) & (df_gen['Date'] < e_date)]
        df_gen=df_gen.groupby(["Organization level"],as_index=False)["Termination Id"].sum()

        colours = ["#0C3B5D","#3EC1CD","5584AC"]
        fig = go.Figure(data=[go.Pie(labels=df_gen["Organization level"], values=df_gen["Termination Id"], hole=.5)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value')
        fig.update_traces(marker=dict(colors=colours), legendgrouptitle_text="Organization level")            
        
        fig.update_layout(height=500,width=600)        
        st.plotly_chart(fig)

    with se3:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("") 
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Termination by Age Category</h4>", unsafe_allow_html=True)

        df_p=df_op.groupby(["Age Range","Date"],as_index=False)["Termination Id"].count()
        df_p=df_p[(df_p['Date'] > s_date) & (df_p['Date'] < e_date)]

        df_p=df_p.groupby(["Age Range"],as_index=False)["Termination Id"].sum()
        df_p=df_p.sort_values(by="Termination Id")

        fig1 = px.bar(df_p, y='Termination Id', x='Age Range',text='Termination Id')
        fig1.update_layout(height=500,width=600,xaxis_title="Age Category",
        yaxis_title="No of Terminations")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)
    with seg1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("") 
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Termination by Reason</h4>", unsafe_allow_html=True)

        df_p=df_op.groupby(["Termination Reason","Date"],as_index=False)["Termination Id"].count()
        df_p=df_p[(df_p['Date'] > s_date) & (df_p['Date'] < e_date)]

        df_p=df_p.groupby(["Termination Reason"],as_index=False)["Termination Id"].sum()
        df_p=df_p.sort_values(by="Termination Id")

        fig1 = px.bar(df_p, x='Termination Id', y='Termination Reason',orientation='h',text='Termination Id')
        fig1.update_layout(height=500,width=600,xaxis_title="No of Terminations",
        yaxis_title="Reasons")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)
    with seg2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("") 
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Termination by Business Unit</h4>", unsafe_allow_html=True)

        df_p=df_op.groupby(["Business unit","Date"],as_index=False)["Termination Id"].count()
        df_p=df_p[(df_p['Date'] > s_date) & (df_p['Date'] < e_date)]

        df_p=df_p.groupby(["Business unit"],as_index=False)["Termination Id"].sum()
        df_p=df_p.sort_values(by="Termination Id")

        fig1 = px.bar(df_p, x='Termination Id', y='Business unit',orientation='h',text='Termination Id')
        fig1.update_layout(height=500,width=600,xaxis_title="No of Terminations",
        yaxis_title="Business Unit")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)
    with seg3:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("") 
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Termination by Tenure Range</h4>", unsafe_allow_html=True)

        df_p=df_op.groupby(["Tenure Range_1","Date"],as_index=False)["Termination Id"].count()
        df_p=df_p[(df_p['Date'] > s_date) & (df_p['Date'] < e_date)]

        df_p=df_p.groupby(["Tenure Range_1"],as_index=False)["Termination Id"].sum()
        df_p=df_p.sort_values(by="Termination Id")

        fig1 = px.bar(df_p, y='Termination Id', x='Tenure Range_1',orientation='v',text='Termination Id')
        fig1.update_layout(height=500,width=600,xaxis_title="Tenure Range",
        yaxis_title="No of Terminations")
        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(showgrid=False)
        fig1.update_traces(marker_color="#3EC1CD")
        st.plotly_chart(fig1)
    with seg2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("<h4 style='text-align: center; color: black;'>Termination Category by Business Unit</h4>", unsafe_allow_html=True)

        df_p=df_op.groupby(["Business unit","term catgeory"],as_index=False)["Termination Id"].count()

        m1=list(set(df_p["Business unit"].tolist()))
        m2=list(set(df_p["term catgeory"].tolist()))
        m1.extend(m2)

        fig = go.Figure(data=[go.Sankey(
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label=m1,
        color = ["#0C3B5D","#3EC1CD","#5584AC","#0C3B5D","#3EC1CD","#5584AC","#0C3B5D"]
        ),
        link = dict(
        source = [0,0,1,1,2,2,3,3,4,4,5,5],
            target = [6,7,6,7,6,7,6,7,6,7],
        value =  df_p["Termination Id"].tolist()
    ))])
        fig.update_layout(width=800,height=500)
        st.plotly_chart(fig)

page = st.sidebar.selectbox("Choose your page", ["Income Statement", "Financial Simulator",'Salary Analysis','Training','Termination Analysis','Attrition Summary',"Jump vs Stay","Termination Profile"])

if page == "Income Statement":
    page1_st()
elif page == "Financial Simulator":
    page2_st()
elif page == "Salary Analysis":
    page3_st()
elif page == "Training":
    page4_st()
elif page == "Termination Analysis":
    page5_st()
elif page == "Attrition Summary":
    page6_st()
elif page == "Jump vs Stay":
    page7_st()
# elif page == "Risk Analysis":
#     page8_st()
elif page == "Termination Profile":
    page9_st()
