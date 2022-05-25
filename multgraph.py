import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
import time

def epoch_to_date_ipi(epoch_date):
    epoch_date = epoch_date / 1000
    my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_date))
    #print(my_time)
    return(my_time)
def epoch_to_date_aranet(epoch_date):
    my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_date)))
    return(my_time)
def date_to_epoch(h_date):
    time_format = '%d/%m/%Y %I:%M:%S %p'
    epoch_date = int(time.mktime(time.strptime(h_date,time_format)))
    return epoch_date
def spacing():
    print('*\n*\n*')

#Variables
dfname_ls = []
device_name = []
x_val = []
y_val = []
epoch_ls = []
folder_path = '/home/tony/multgraph_python/data_csv/'

while True:
    file_name = input("Input the csv file names (ext included) you want to plot together, input 'no' when done: ")
    if(file_name == 'no'):
        break
    file_type = input("Input the type of file (IPIE, Aranet): ")
    
    
    dfname_ls.append((file_name, file_type))
event_name = input("Input file name for the figure: ")
spacing()
print("The following dataframes' data will be plotted together: ", dfname_ls, '\n')
plt.figure(figsize=(20,10)) #width, height
plt.title("CO2 vs Time")
plt.xlabel("fecha y hora")
plt.ylabel("ppm")
plt.xticks(rotation=25)
plt.grid()

for dfname in dfname_ls:
    try:
        df = pd.read_csv(folder_path + dfname[0])
    except:
        print("======== Error: unable to find csv file ", dfname[0], ' ========')
    if (dfname[1] == "IPIE"):
        for epoch in df["Tiempo"]:
            x_val.append(epoch_to_date_ipi(float(epoch)))
        datenum = md.date2num(x_val)
        y_val = df['CO2']
        ax = plt.gca()
        xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
        ax.xaxis.set_major_formatter(xfmt)
        plt.plot(datenum, y_val, label='IPIE')
    elif(dfname[1] == "Aranet"):
        for date in df['Time(dd/mm/yyyy)']:
            epoch_ls.append(date_to_epoch(date))
        for epoch in epoch_ls:
            x_val.append(epoch_to_date_aranet(epoch))
        datenum = md.date2num(x_val)
        y_val = df['Carbon dioxide(ppm)']
        ax = plt.gca()
        xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
        ax.xaxis.set_major_formatter(xfmt)
        plt.plot(datenum, y_val, label = 'Aranet')
    x_val.clear()
    epoch_ls.clear()
    
plt.legend()
plt.savefig('/home/tony/multgraph_python/figures/' + event_name + '.png', bbox_inches = 'tight')

    


