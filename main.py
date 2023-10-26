from scipy.interpolate import interp1d
from PyQt5 import QtCore, QtGui
import os
import pandas as pd
import sys
from PyQt5.QtWidgets import QInputDialog  ,  QApplication, QMainWindow, QShortcut, QFileDialog , QSplitter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence
import numpy as np
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from sampling_studio import Ui_MainWindow  # Replace 'your_ui_file' with the actual name of your UI file

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Your Application Title")
        
      
        
        self.time = np.linspace(0, 10 , 1000)
        
        # self.orignal_signal = []
        self.signals_components = []
        self.orignal_signal = None
        self.max_ferq = None
        
        self.xData = None
        self.yData = None
        self.y_with_noise = None

        self.mixed_signal = None        
        self.mixed_signal_with_noise = None
        # self.orignal_signal_loaded = None
        # self.orignal_signal_mixed = None

        
        
        # self.loaded_signal = {
        #     "x" : [],
        #     "y" : []
        # }
        
        self.ismixed = False
        self.isloaded= False
        
        self.ui.horizontalSlider.setMinimum(1)
        self.ui.horizontalSlider.setMaximum(5)
        
        self.ui.dial.setMinimum(0)
        self.ui.dial.setMaximum(5)
        self.ui.dial.valueChanged.connect(self.add_noise_try)
        self.ui.horizontalSlider.valueChanged.connect(self.sampling)
        self.ui.pushButton.clicked.connect(self.load_signal)
        self.ui.pushButton_2.clicked.connect(self.create_signal_component)
        self.ui.pushButton_3.clicked.connect(self.remove_component)
        
        
    def load_signal(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")
        # data = np.genfromtxt(file_path, delimiter = ',')
        # self.x = data[:, 0].tolist()
        # self.y = data[:, 1].tolist()

        data = pd.read_csv(file_path)
        
        self.yData = data.values[:, 1]
        self.xData = data.values[:, 0]
        FTydata = np.fft.fft(self.yData)
        FTydata = FTydata[0:int(len(self.yData)/2)]
        FTydata = abs(FTydata)
        maxpower = max(FTydata)
        noise = (maxpower/100)
        self.fmaxtuble = np.where(FTydata > noise)
        self.maxFreq = max(self.fmaxtuble[0])
        print(self.maxFreq)
        self.ui.graphicsView_2.clear()
        self.orignal_signal = self.ui.graphicsView_2.plotItem.plot(self.xData , self.yData , pen="#ffffff")
        self.ui.graphicsView_2.plotItem.vb.setLimits(xMin= np.min(self.xData), xMax=max(self.xData), yMin=min(self.yData) , yMax=max(self.yData))
        # self.ui.graphicsView_2.getViewBox().autoRange()

        self.isloaded = True
        self.ismixed = False
        # print(self.x)
        # print(xData)

        
    
        
    def create_signal_component(self):
        amplitude =  self.ui.spinBox_2.value()
        phase = self.ui.spinBox_3.value()
        frequency = self.ui.spinBox.value()
        
        amplitude = float(amplitude)
        phase = float(phase)
        frequency = float(frequency)
        
        signal_component = {
            "amplitude" : amplitude, 
            "phase" : phase,
            "frequency" : frequency,
        }
        
        self.signals_components.append(signal_component)
        
        self.update_component_list()        
        self.plot_composed_signal()
        
    def plot_composed_signal(self):
        self.ui.graphicsView_2.clear()
        if len(self.signals_components) > 0 :
            signal = self.signals_components[0]['amplitude'] * np.sin(2 * np.pi * self.signals_components[0]['frequency']  * self.time + self.signals_components[0]['phase'])
            for component in self.signals_components[1:]:
                add_comp = component['amplitude'] * np.sin(2 * np.pi * component['frequency']  * self.time + component['phase'])
                signal += add_comp
            self.mixed_signal = signal
            self.orignal_signal = self.ui.graphicsView_2.plot( self.time , signal) 
            
            self.ismixed = True
            self.isloaded = False
            
            # self.orignal_signal = plotted_mixed_signal
            self.orignal_signal_xy = (self.time , signal )

            
            min_x =  min(self.orignal_signal.getData()[0])
            max_x =  max(self.orignal_signal.getData()[0])


            min_y =  min(self.orignal_signal.getData()[1])
            max_y =  max(self.orignal_signal.getData()[1])

            self.ui.graphicsView_2.plotItem.vb.setLimits(xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y)
        
    
    def sampling_(self):
        max_frequency = self.signals_components[0]["frequency"]
        for component in self.signals_components:
            if component["frequency"] > max_frequency:
                max_frequency = component["frequency"]

        # sampling_frequency = 2  # 100 samples per second
        sampling_frequency = self.ui.horizontalSlider_4.value() * max_frequency  # 100 samples per second
        # sampled_indices = np.arange(0, len(self.time), int(1 / (sampling_rate * (self.time[1] - self.time[0]))))
        # sampled_time = self.time[sampled_indices]
        # sampled_signal = signal[sampled_indices]





        sampling_interval = 1.0 / sampling_frequency
        
        
        sampled_points = self.mixed_signal[::int(1 / (sampling_frequency * (self.time[1] - self.time[0])))]
        sampled_time = self.time[::int(1 / (sampling_frequency * (self.time[1] - self.time[0])))]

        # Plot the original signal
        self.ui.graphicsView.plot(self.time, self.mixed_signal, pen='b', name="Original Signal")

        # Plot the sampled points on top of the original signal
        self.ui.graphicsView.plot(sampled_time, sampled_points, pen='r', symbol='o', symbolPen='r', symbolBrush='r', name="Sampled Points")


        
        sampled_points = self.mixed_signal[::int(1 / (sampling_frequency * (self.time[1] - self.time[0])))]

# Plot the original signal
        # self.ui.graphicsView.plot(self.time, self.mixed_signal, pen='b', name="Original Signal")

        # # Plot the sampled points on top of the original signal
        # self.ui.graphicsView.plot(self.time[::int(1 / (sampling_frequency * (self.time[1] - self.time[0])))], sampled_points, pen='r', symbol='o', symbolPen='r', symbolBrush='r', name="Sampled Points")

        
        # self.time = np.arange(0, 1, sampling_interval)   

        # x_data, y_data = self.plotted_signal.getData()  # Get the data from the PlotDataItem
        
        # sampled_x= []
        # sampled_y= []
        
        # # t = 0 
        # # for t in x_data:
        # #     sampled_x.append[x_data[t]]
        # #     sampled_y.append[y_data[t]]
        # #     t = t + sampling_interval
        
        # for i in range(0 , len(x_data) , (sampling_interval)):
        #    sampled_x.append(x_data[i])
        #    sampled_y.append(y_data[i])
        
        # self.ui.graphicsView_3.plot(sampled_x , sampled_y ,symbol='o' )
            
        

        # Calculate the sampling interval

       
        
        # sampled_signal_x = x_data[::int(1 / (sampling_interval / (x_data[1] - x_data[0])))]
        # sampled_signal_y = y_data[::int(1 / (sampling_interval / (x_data[1] - x_data[0])))]

        # # Create a new PlotDataItem for the sampled signal
        # sampled_plot = self.ui.graphicsView.plot(sampled_signal_x, sampled_signal_y)
        # original_signal_plot = self.ui.graphicsView_2.plot(x_data, y_data, pen=None, symbol='o')
        pass
    # def plot_composed(self):
    def update_component_list(self):
        self.ui.listWidget.clear()
        for compnent in self.signals_components:
            amplitude = compnent["amplitude"]
            frequency = compnent["frequency"]
            phase = compnent["phase"]
            self.ui.listWidget.addItem(f"{amplitude}sin(2πx({frequency}) + {phase}))")
            
            
    
    def remove_component(self):
        delete_component_indx = self.ui.listWidget.currentRow()   
        self.signals_components.pop(delete_component_indx)
        self.plot_composed_signal()
        self.update_component_list()
        # print(self.signals_components[delete_component_indx]["phase"])
    


    def add_noise_try(self):
        
        if self.isloaded:
            snr_level = self.ui.dial.value() / 10
            # self.ui.graphicsView_2.clear()
            # self.ui.graphicsView_2.plot(self.xData , self.yData  )
            y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.yData]
            self.ui.graphicsView_2.clear()
            
            self.orignal_signal = self.ui.graphicsView_2.plot(self.xData  ,y_with_noise  )
            # self.yData = y_with_noise
            # self.orignal_signal_loaded = (self.x , y_with_noise)
        
        if self.ismixed:
            
            snr_level = self.ui.dial.value()/10
            noise = np.random.normal(0, snr_level, len(self.time))
            self.mixed_signal_with_noise = self.mixed_signal + noise
            # self.ui.graphicsView_2.plot(self.mixed_signal)
            # self.ui.graphicsView_2.clear()
            self.ui.graphicsView_2.clear()
            self.orignal_signal = self.ui.graphicsView_2.plot(self.time , self.mixed_signal_with_noise )
            # self.orignal_signal_mixed = (self.time , self.mixed_signal_with_noise )
    
    
    def sampling(self):
        if self.ismixed:
            max_frequency = self.signals_components[0]["frequency"]
            for component in self.signals_components:
                if component["frequency"] > max_frequency:
                    max_frequency = component["frequency"]

            self.ui.graphicsView_2.clear()
            orginal_signal = self.ui.graphicsView_2.plot(self.orignal_signal.getData()[0] , self.orignal_signal.getData()[1] ) # dont forget to plot the orignal not only the mixed
            # orginal_signal = self.ui.graphicsView_2.plot(self.orignal_signal_mixed[0] , self.orignal_signal_mixed[1] ) # dont forget to plot the orignal not only the mixed

            
            sampling_frequency = self.ui.horizontalSlider.value() * (max_frequency)
            # sampling_frequency = 100
            sampling_interval = 1 / sampling_frequency
            x_data, y_data = orginal_signal.getData()  # Get the data from the PlotDataItem
            num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)

        # Sample the signal within the available data range
            sampled_signal_x = x_data[::int(len(x_data) / num_samples)]
            sampled_signal_y = y_data[::int(len(x_data) / num_samples)]
            sampled_plot = self.ui.graphicsView_2.plot(sampled_signal_x, sampled_signal_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
            reconstructed_data = self.sinc_interp(sampled_signal_x , sampled_signal_y , x_data)
            
            self.ui.graphicsView.clear()
            self.ui.graphicsView.plot(x_data , reconstructed_data ,pen='g')
            self.ui.graphicsView_2.plot(x_data , reconstructed_data ,pen='g')
            # self.ui.graphicsView.plotItem.vb.setLimits(0 , 10 ,max(self.ui.graphicsView_2.plot(x_data , reconstructed_data ,pen='g').getData()[1])  )

        if self.isloaded:
            sampling_rate = self.ui.horizontalSlider.value() * self.maxFreq

    # Ensure that x and y are NumPy arrays
            x = np.array(self.xData)
            y = np.array(self.yData)

            # Determine the time increment between samples
            time_increment = 1 / sampling_rate

            # Create an array to store the sampled points
            sampled_x = []
            sampled_y = []

            # Iterate through the signal and sample it
            current_time = 0
            idx = 0
            while current_time <= x[-1]:
                # Find the closest x value to the current time
                while idx < len(x) - 1 and x[idx] < current_time:
                    idx += 1

                # Linear interpolation to find the sampled y value
                if idx == 0:
                    sampled_y_value = y[0]
                elif idx == len(x) - 1:
                    sampled_y_value = y[-1]
                else:
                    x1, x2 = x[idx - 1], x[idx]
                    y1, y2 = y[idx - 1], y[idx]
                    slope = (y2 - y1) / (x2 - x1)
                    sampled_y_value = y1 + slope * (current_time - x1)

                sampled_x.append(current_time)
                sampled_y.append(sampled_y_value)
                

                current_time += time_increment
            sampled_x = np.array(sampled_x)
            self.time = np.array(self.time)
            
            self.ui.graphicsView_2.clear()
            orginal_signal = self.ui.graphicsView_2.plot(self.orignal_signal.getData()[0] , self.orignal_signal.getData()[1] ) # dont forget to plot the orignal not only the mixed
        
            x_data, y_data = orginal_signal.getData()  # Get the data from the PlotDataItem
            
            
            self.ui.graphicsView_2.plot(sampled_x, sampled_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
            reconstructed_data = self.sinc_interp(sampled_x , sampled_y , x_data)
            # x_data = x_data[:len(reconstructed_data)]
            self.ui.graphicsView.clear() 
            self.ui.graphicsView.plot(x_data , reconstructed_data ,pen='g')
            self.ui.graphicsView_2.plot(x_data , reconstructed_data ,pen='g')
            # self.ui.graphicsView.plotItem.vb.setLimits(0 , 10 ,max(self.ui.graphicsView_2.plot(x_data , reconstructed_data ,pen='g').getData()[1])  )

            

            # return sampled_x, sampled_y

            


    def sinc_interp(self, sampled_x, sampled_y, xData):
    
        if len(sampled_y) != len(sampled_x):
            raise ValueError('x and s must be the same length')

    # Find the period
        T_s = sampled_x[1] - sampled_x[0]

        sincM = np.tile(xData, (len(sampled_x), 1)) - \
            np.tile(sampled_x[:, np.newaxis], (1, len(xData)))
        reconstructed = np.dot(sampled_y, np.sinc(sincM/T_s))
        return reconstructed

        # def sample_loaded_Signal(self):
            
            
            
        # t = np.linspace(0, 1, sampling_frequency)
        # sampled_signal = np.sin(2 * np.pi * 10 * t)  # A sine wave at 10 Hz

        # # Desired sampling frequency for interpolation
        # interpolation_frequency = 1000  # Higher sampling rate for interpolation
        # t_interpolated = np.linspace(0, 1, interpolation_frequency)

        # # Initialize the interpolated signal
        # interpolated_signal = np.zeros(len(t_interpolated))

        # # Apply sinc interpolation
        # for i, t_sampled in enumerate(t):
        #     sinc_values = sampled_signal[i] * np.sinc((t_interpolated - t_sampled) * interpolation_frequency)
        #     interpolated_signal += sinc_values
        # # return(sampled_signal_x , sampled_signal_y)
        # self.ui.graphicsView_3.plot(t_interpolated, interpolated_signal)
    





        # T = 1 / sampling_frequency
        # n = np.arange(0, 0.5 / T)
        # nT = n * T
        # # sampling_t = np.arange(-1 , 1 , sampling_rate)

        # x2 = np.sin(2 * np.pi * sampling_frequency * nT)
        
        # self.ui.graphicsView_2.plot(nT, x2, symbol='o', symbolPen='r', symbolBrush='r', name='Sample Marks')
        
        
        
        
        
        
        
    
        # snr_level = self.ui.dial.value() / 10
        # x =  self.orignal_signal.getData()[0]
        # y =  self.orignal_signal.getData()[1]
        # y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.loaded_signal["y"]]
        # self.ui.graphicsView_2.clear()
        # self.orignal_signal
        # self.ui.graphicsView_2.plot( x , y_with_noise)
        
    # def sample_loaded_signal(self):
        
        
        
        
        
        # time_differences = [self.time[i] - self.time[i - 1] for i in range(1, len(self.time))]

        # # Calculate the mean time difference
        # time_difference = sum(time_differences) / len(time_differences)

        # # Calculate the sampling frequency
        # sampling_frequency = 1 / time_difference
        # max_frequency = sampling_frequency / 2
        # time_sampling = np.arange(0, max(self.time), 1 / sampling_frequency)
        # interpolator = interp1d(self.time , self.loaded_signal["y"], kind='linear')

        # # Sample the signal at the specified time points
        # sampled_amplitude = interpolator(time_sampling)
        # self.ui.graphicsView_2.plot(time_sampling, sampled_amplitude, pen=None, symbol='o', symbolPen='r', symbolBrush='r')
        
        

           
        
        
    def max_min_limits(self):
        x =  self.orignal_signal.getData()[0]
        y =  self.orignal_signal.getData()[1]
        
    
        
        
            

        
    
    # def update_signals_list(self):
    #     self.ui.listWidget.clear()
    #     for signal in self.siganls_g1:
    #         self.ui.listWidget.addItem(signal["name"])

def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
