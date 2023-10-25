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
        
        
        
        self.loaded_signal = {
            "x" : [],
            "y" : []
        }
        
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
        data = np.genfromtxt(file_path, delimiter = ',')
        x = data[:, 0].tolist()
        y = data[:, 1].tolist()

        # data = pd.read_csv(file_path)
        # x = data.values[:, 0] 
        # y = np.arange(0, 9.99, 0.01)

        self.loaded_signal["x"] = x
        self.loaded_signal["y"] = y
        file_name = os.path.basename(file_path[:-4])
        self.ui.graphicsView_2.clear()        
        # plot_loaded_siganl = self.ui.graphicsView_2.plotItem.plot(x , y)
        plot_loaded_siganl = self.ui.graphicsView_2.plotItem.plot(self.loaded_signal["x"] ,self.loaded_signal["y"]  , pen="#ffffff")
        # plot_loaded_siganl = self.ui.graphicsView_2.plotItem.plot(x , y , pen="#ffffff")
        self.ui.graphicsView_2.plotItem.vb.setLimits(xMin=0 , xMax=max(x), yMin=min(y) , yMax=max(y))
        self.ismixed = False
        self.isloaded = True
        self.orignal_signal = plot_loaded_siganl
    
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
            plotted_mixed_signal = self.ui.graphicsView_2.plot( self.time , signal) 
            
            self.ismixed = True
            self.isloaded = False
            
            self.orignal_signal = plotted_mixed_signal
            
            min_x =  min(plotted_mixed_signal.getData()[0])
            max_x =  max(plotted_mixed_signal.getData()[0])


            min_y =  min(plotted_mixed_signal.getData()[1])
            max_y =  max(plotted_mixed_signal.getData()[1])

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
    
    def add_noise(self ):
       
        snr_level = self.ui.dial.value()/10
        self.ui.graphicsView_2.clear()
        noise = np.random.normal(0, snr_level, len(self.time))
        signal_with_noise = self.mixed_signal + noise
        self.ui.graphicsView_2.plot(self.mixed_signal)
        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_2.plot(self.time , signal_with_noise )
        
    
    def add_noise_loaded_signal(self):
        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_2.plot(self.loaded_signal["x"]  , self.loaded_signal["y"]  )
        snr_level = self.ui.dial.value() / 10
        y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.loaded_signal["y"]]
        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_2.plot(self.loaded_signal["x"]  ,y_with_noise  )


    def add_noise_try(self):
        if self.isloaded:
            self.ui.graphicsView_2.clear()
            self.ui.graphicsView_2.plot(self.loaded_signal["x"]  , self.loaded_signal["y"]  )
            snr_level = self.ui.dial.value() / 10
            y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.loaded_signal["y"]]
            self.ui.graphicsView_2.clear()
            self.ui.graphicsView_2.plot(self.loaded_signal["x"]  ,y_with_noise  )
        
        if self.ismixed:
            
            snr_level = self.ui.dial.value()/10
            self.ui.graphicsView_2.clear()
            noise = np.random.normal(0, snr_level, len(self.time))
            signal_with_noise = self.mixed_signal + noise
            self.ui.graphicsView_2.plot(self.mixed_signal)
            self.ui.graphicsView_2.clear()
            self.ui.graphicsView_2.plot(self.time , signal_with_noise )
    
    
    def sampling(self):
        if self.ismixed:
            max_frequency = self.signals_components[0]["frequency"]
            for component in self.signals_components:
                if component["frequency"] > max_frequency:
                    max_frequency = component["frequency"]

            self.ui.graphicsView_2.clear()
            self.ui.graphicsView_2.plot(self.time , self.mixed_signal) # dont forget to plot the orignal not only the mixed

            
            sampling_frequency = self.ui.horizontalSlider.value() * (max_frequency)
            # sampling_frequency = 100
            sampling_interval = 1 / sampling_frequency
            x_data, y_data = self.orignal_signal.getData()  # Get the data from the PlotDataItem
            num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)

        # Sample the signal within the available data range
            sampled_signal_x = x_data[::int(len(x_data) / num_samples)]
            sampled_signal_y = y_data[::int(len(x_data) / num_samples)]
            sampled_plot = self.ui.graphicsView_2.plot(sampled_signal_x, sampled_signal_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
        if self.isloaded:
            self.sample_loaded_signal()
            

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
        
    def sample_loaded_signal(self):
        
        
        pass
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
