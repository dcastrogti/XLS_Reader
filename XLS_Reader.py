#XLS_Reader for WaveForms
class XLSReader:
    
    def __init__(read, title, folder, name, sheet_name):
        read.title = title
        read.folder = folder
        read.name = name
        read.sheet_name = sheet_name
        
        read.data = pandas.read_excel(read.folder + "/" + read.name+".xlsx",sheet_name = read.sheet_name) 
        
    def read_xls(read): 
        return (read.data)
    def graph_voltage(read, t1,t2,y1,y2):
        
        
        plt.figure(figsize=(9,4))
        plt.plot(read.data["Time (s)"],read.data["Channel 1 (V)"],c = "blue")
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.title(read.title + " - Voltage")
        plt.ylim(y1, y2)
        plt.xlim(t1,t2)
    def graph_fft(read, f1,f2,db1,db2):
        plt.figure(figsize=(9,4))
        plt.plot(read.data["Frequency (Hz)"],read.data["Channel 1 (dBṼ)"],c = "blue")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Channel 1 (dBṼ)")
        plt.title(read.title+ " - FFT")
        plt.ylim(db1, db2)
        plt.xlim(f1, f2)
# Examples:        
# XLSReader(Title, Folder_Location, Name_Of_File, Sheet_Number)
#     r1 = XLSReader( "Title" ,"11_10_2022","Buried_And_Shed_Test(11-10)","Sheet1")
# graph_voltage(time_start, time_end, voltage_min, voltage_max)
#     r1.graph_voltage(-.5,.5,-10,10)
# graph_fft(freq_start, freq_end, dbV_min,dbV_max)     
#      r1.graph_fft(0,2000,-140,20)