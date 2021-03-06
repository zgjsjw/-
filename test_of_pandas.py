import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

data_in = './data/online_retail.xlsx'
data_out = './output/result.csv'

def show_datainfo(data_file):
    print('***************')
    print(data_file.head())

def clean_data(datafile):
    adatafile = datafile.dropna()
    #print(datafile.shape)
    #print(adatafile.shape)
    bdatadile = adatafile.drop_duplicates()
    #print(bdatadile.shape)
    bdatadile.to_csv(data_out,index=False,encoding='utf-8')
    return bdatadile

def show_pic(datafile):
    customer_per_country = datafile['Country'].value_counts()

    print(customer_per_country)
    #print(customer_per_country_df)
    #customer_per_country
    #sns.barplot(customer_per_country_df)
    customer_per_country_count = customer_per_country[customer_per_country.index != 'United Kingdom']
    print(customer_per_country_count)
    customer_per_country_count.plot(kind='bar')
    #plt.xticks(rotation = 90)
    plt.xlabel('Country')
    plt.ylabel('Customer_count')
    plt.tight_layout()
    plt.show()

def show_pic2(datadile):
    data1 = datadile['Country'] != 'United Kingdom'
    data2 = ~datadile['InvoiceNo'].str.startswith('C')
    valid_data = datadile[data1 & data2].copy()
    valid_data['total_cost'] = valid_data['Quantity'] * valid_data['UnitPrice']
    cost_per_country = valid_data.groupby('Country')['total_cost'].sum()
    print(cost_per_country)
    cost_per_country.sort_values(ascending=False).plot(kind='bar')
    plt.tight_layout()
    plt.show()

def show_pic3(datafile):
    country = ['Germany', 'France', 'Spain', 'Belgium', 'Switzerland']
    valid_data = datafile[datafile['Country'].isin(country)].copy()
    #print(valid_data.info())
    #print(valid_data.head())
    valid_data['InvoiceDate'] = pd.to_datetime(valid_data['InvoiceDate'])
    valid_data['year'] = valid_data['InvoiceDate'].dt.year.astype(str)
    valid_data['month'] = valid_data['InvoiceDate'].dt.month.astype(str)
    valid_data['year-month'] = valid_data['year'].str.cat(valid_data['month'],sep = '-')
    #print(valid_data.head())
    month_country_count = valid_data.groupby(['year-month', 'Country'])['StockCode'].count()
    #print(month_country_count)

    month_country_count_pf = month_country_count.unstack()
    month_country_count_pf.index = pd.to_datetime(month_country_count_pf.index).to_period('M')
    month_country_count_pf.sort_index(inplace = True)
    print(month_country_count_pf)
    month_country_count_pf.plot(kind='bar',stacked=True)
    plt.tight_layout()
    plt.show()

def main():
    if not os.path.exists(data_out):

        read_data = pd.read_excel(data_in)
        #show_datainfo(read_data)
        tem_data = clean_data(read_data)
        print('清洗加工数据')
    else:
        tem_data = pd.read_csv(data_out)
        print('读取加工数据')

    #show_pic(tem_data)
    #show_pic2(tem_data)
    show_pic3(tem_data)
    #print(os.getcwd())
    #print('{}'.format('1'))

if __name__ == '__main__':
    main()
