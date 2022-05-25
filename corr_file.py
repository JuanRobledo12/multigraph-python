#NEEDS WORK FOR THE HOUR 24
import pandas as pd

def eval_dates(date_ip, date_ar):
    split_date = date_ar.split()
    ipi_time = date_ip.split()
    if (ipi_time[0].find('/') != -1):
        ipidate_split = ipi_time[0].split('/')
    else:
        ipidate_split = ipi_time[0].split('-')   
    hour = split_date[1][0:4]
    day = split_date[0][0:2]
    mon = split_date[0][3:5]
    yir = split_date[0][6:10]
    n_hour = hour.split(':')
    if (n_hour[0] != '12' and split_date[2] == 'PM'):
        if (int(n_hour[0]) > 9 and int(n_hour[0]) < 12):
            hour = split_date[1][0:5]  
            n_hour = hour.split(':')
        n_hour[0] = str(int(n_hour[0]) + 12)
        hour = n_hour[0] +':'+ n_hour[1]
        #print(hour)
    if (n_hour[0] == '12' and split_date[2] == 'AM'):
        hour = split_date[1][0:5]
        n_hour = hour.split(':')
        n_hour[0] = str(int(n_hour[0]) - 12)
        hour = n_hour[0] +':'+ n_hour[1]
    if (int(n_hour[0]) < 10 and n_hour[0] != '0'):
        ipi_hour = ipi_time[1].split(':')
        ipi_time[1] = str(int(ipi_hour[0])) + ':' + ipi_hour[1]
        new_date_1 = yir + '/' + mon + '/' + day + " " + hour 
    else:
        ipi_hour = ipi_time[1].split(':')
        ipi_time[1] = str(int(ipi_hour[0])) + ':' + ipi_hour[1]
        if((split_date[2] == 'AM' and n_hour[0] != '0') or (n_hour[0] == '12' and split_date[2] == 'PM')):
            hour = split_date[1][0:5]
        new_date_1 = yir + '/' + mon + '/' + day + " " + hour
    new_date_2 = ipidate_split[0] + '/' + ipidate_split[1] + '/' + ipidate_split[2] + ' ' + ipi_time[1]
    #print(new_date_1, 'vs', new_date_2)
    if (new_date_1 == new_date_2):
        print('ARANET_DATE: ', new_date_1, ' / IPI_DATE: ', new_date_2)
        return True
    else:
        return False


df_ipie = pd.read_csv('/home/tony/multgraph_python/data_csv/explab16_18_IPIE1_co2.csv')
df_ara1 = pd.read_csv('/home/tony/multgraph_python/data_csv/DBM-D_explab16_18.csv')
df_ara2 = pd.read_csv('/home/tony/multgraph_python/data_csv/DBM-A_explab16_18.csv')
df_new = pd.DataFrame(columns=['Date','epoch', 'CO2_IPIE', 'CO2_DBM-D', 'CO2_DBM-A'])

co2_val = []

for date_ipi in df_ipie['Date']:
    val_count = 0
    for date_ara  in df_ara1['Time(dd/mm/yyyy)']:
        #if same_hour(date_ipi, date_ara):
        if eval_dates(date_ipi, date_ara):
            co2_val.append(df_ara1['Carbon dioxide(ppm)'][val_count])
            print(date_ipi)
            break
        val_count = val_count + 1
        # else:
        #     continue
df_new['CO2_DBM-D'] = co2_val
co2_val.clear()

for date_ipi in df_ipie['Date']:
    val_count = 0
    for date_ara  in df_ara2['Time(dd/mm/yyyy)']:
        if eval_dates(date_ipi, date_ara):
            co2_val.append(df_ara2['Carbon dioxide(ppm)'][val_count])
            print(date_ipi)
            break
        val_count = val_count + 1
df_new['CO2_DBM-A'] = co2_val
co2_val.clear()

df_new['Date'] = df_ipie['Date']
df_new['epoch'] = df_ipie['Tiempo']
df_new['CO2_IPIE'] = df_ipie['CO2']

df_new.to_csv('explab16_18_data.csv')