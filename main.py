#importing all necessary libraries
import pandas as pd
import yfinance as yf
from pandas_datareader.data import DataReader
import plotly.express as px
from datetime import datetime
import streamlit as st

#Downloading stock price data of 4 companies
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']               #The tech stocks we'll use for this analysis
end = datetime.now()                                       #assiging the current data and time to variable 'end'
start = datetime(end.year - 1, end.month, end.day)         #assiging start date as exactly one year before the end date, keeping the same month and day

for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)      #downloading data for each company in tech_list

company_list = [AAPL, GOOG, MSFT, AMZN]
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]

for company, com_name in zip(company_list, company_name):  
    company["company_name"] = com_name                      #adding a new column 'company_name' to each dataframe

df = pd.concat(company_list, axis=0)                        #concatenating the dataframes in company_list into a single dataframe df

#EDA
print(df.tail())                                            #print last 5 rows of dataframe df
print(df.shape)                                             #print number of rows and columns of dataframe df
print(df.info())                                            #print the summary of dataframe df
print(df.describe())                                        #print statistical analysis of numerical columns of dataframe df
print(df.isnull().sum())                                    #print number of missing values in each column of dataframe df

#Creating User Interface based on streamlit
st.header("Stock Price Visualization Tool", divider='rainbow')  #displays a header with the title "Stock Price Visualization Tool"    
choice=st.sidebar.radio(                                        #creates a radio button in the sidebar for selecting a company
    label ='Select a company',
    options =('APPLE','GOOGLE','MICROSOFT','AMAZON','ALL')
    )

st.subheader(f'Company Name= {choice}')                         # display the name of selected company
st.markdown(f'The stock price data is available from {start.year} to {end.year}') #display the duration for which data id available

if choice == 'ALL':                                             #assigning appropriate dataframe based on user's choice
    dataframe=df
else:
    dataframe=df[df['company_name']==choice]  #working
    

def interactive_plot(dataframe):                                #function to create interactive plot
    y_val=st.selectbox("Select a parameter",options=dataframe.columns[:-1])
    fig=px.line(dataframe,y=y_val,color='company_name',markers=True,hover_data=['Open','Close','Volume'],hover_name='company_name')
    fig.update_layout(hovermode="y unified")
    st.plotly_chart(fig)


interactive_plot(dataframe)                                      #calling interactive plot function








#fig4=px.box(df,x='company_name',y='Close',color='company_name',title="close")
#fig4.show()