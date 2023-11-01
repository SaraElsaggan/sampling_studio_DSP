from scipy.signal import resample
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
        
        self.time = np.linspace(0, 5 , 1000)
        
        # self.orignal_signal = []
        # self.signals_components = []

        self.example_signals = []

        self.signals_components = [
        #     {
        #     "amplitude" : 1, 
        #     "phase" : 0,
        #     "frequency" : 2,
        # },
        #     {
        #     "amplitude" : 2, 
        #     "phase" : 0,
        #     "frequency" : 6,
        # }, 
            
            
            
        #     {
        #     "amplitude" : 1, 
        #     "phase" : 0,
        #     "frequency" : 3,
        # }, 
        #     {
        #     "amplitude" : 3, 
        #     "phase" : 0,
        #     "frequency" : 4,
        # }, 
            
            
            
        #     {
        #     "amplitude" : 1, 
        #     "phase" : 0,
        #     "frequency" : 5,
        # }, 
            
        #     {
        #     "amplitude" : 4, 
        #     "phase" : 0,
        #     "frequency" : 1,
        # }, 
            
            
            
        ]

        self.orignal_signal = None
        self.max_freq = 62.5
        
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
        self.ui.horizontalSlider.setMaximum(10)
        
        self.ui.dial_noise.setMinimum(0)
        self.ui.dial_noise.setMaximum(10)
        self.ui.dial_noise.valueChanged.connect(self.add_noise_try)
        self.ui.horizontalSlider.valueChanged.connect(self.input_freq_slider)
        # self.ui.btn_sample.clicked.connect(self.input_freq_spin)
        self.ui.spin__samp_freq.editingFinished.connect(self.input_freq_spin)
        self.ui.btn_import.clicked.connect(self.load_signal)
        self.ui.btn_add_comp.clicked.connect(self.create_signal_component)
        self.ui.btn_remove.clicked.connect(self.remove_component)
        
        self.ui.btn_mixed_plot.clicked.connect(self.plot_compose_signal)
        
        self.ui.comb_bx_examp.currentIndexChanged.connect(self.creat_and_plot_example)
      
    #   def example_list_update(self ,self.ui. ):
    #       for comp in self.signals_components:
    #         #   if self.ui.list_comps.currentIndex() == 0:
                  
      
        self.isslider = True
   
    def input_freq_slider(self):
        self.isslider = True
        self.isspin = False
        self.sampling()
    
    def input_freq_spin(self):
        self.isslider = False
        self.isspin = True
        self.sampling()
        
    def load_signal(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")
    
        data = pd.read_csv(file_path)
        
        self.yData = data.values[:, 1]
        self.xData = data.values[:, 0]
        
        print(self.max_freq)
        self.ui.graph_orignal.clear()
        self.orignal_signal = self.ui.graph_orignal.plotItem.plot(self.xData , self.yData , pen="#ffffff")
        self.ui.graph_orignal.plotItem.vb.setLimits(xMin= np.min(self.xData), xMax=max(self.xData), yMin=min(self.yData) , yMax=max(self.yData))
        self.ui.graph_orignal.getViewBox().autoRange()
        self.isloaded = True
        self.ismixed = False
        self.ui.graph_error.clear()
        self.ui.graph_recons.clear()
        self.sampling()
    def create_signal_component(self):
        amplitude =  self.ui.spin_amp.value()
        phase = self.ui.spin_phase.value()
        frequency = self.ui.spin_freq.value()
        
        amplitude = float(amplitude)
        phase = float(phase)
        frequency = float(frequency)
        
        signal_component = {
            "amplitude" : amplitude, 
            "phase" : phase,
            "frequency" : frequency,
        }
        
        
        
        self.signals_components.append(signal_component)
        print(self.signals_components)
        
        # self.max_freq = frequency
        # for component in self.signals_components:
        #     if component["frequency"] > self.max_freq:
        #         self.max_freq = component["frequency"]
        
        # print(self.max_freq)
        
                
    
        self.plot_compose_signal()
        self.sampling()
        
        # self.update_component_list()        
       
    def creat_and_plot_example(self):
        self.ismixed = True
        # self.isexample = True
        self.isloaded = False
        self.ui.graph_orignal.clear()
        self.ui.graph_error.clear()
        self.ui.graph_recons.clear()
        example_1 = np.sin(2 * np.pi * 6  * self.time ) + np.sin(2 * np.pi * 2  * self.time)
        example_2 = np.sin(2 * np.pi * 5  * self.time ) +2 * np.sin(2 * np.pi * 3  * self.time)
        example_3 =2 *np.sin(2 * np.pi * 4  * self.time ) +  np.sin(2 * np.pi * 1 * self.time) + np.sin(2* np.pi * 3 * self.time)

        if self.ui.comb_bx_examp.currentIndex() == 1:
            # signal = comp_0 + comp_1
            self.max_freq = 6
            self.mixed_signal = example_1
        elif self.ui.comb_bx_examp.currentIndex() == 2:
            # signal = comp_2 + comp_3
            self.max_freq = 5
            self.mixed_signal = example_2

        elif self.ui.comb_bx_examp.currentIndex() == 3:
            # signal = comp_4 + comp_5
            self.max_freq = 4
            self.mixed_signal = example_3
           
        self.plot_sine_signal(self.mixed_signal)
        
    def plot_compose_signal(self): 
        self.ui.graph_orignal.clear()
        self.ui.graph_error.clear()
        self.ui.graph_recons.clear()# add sig_componets and then call the plot function
        if self.signals_components:
            signal = self.signals_components[0]['amplitude'] * np.sin(2 * np.pi * self.signals_components[0]['frequency']  * self.time + self.signals_components[0]['phase'])
            for component in self.signals_components[1:]:
                add_comp = component['amplitude'] * np.sin(2 * np.pi * component['frequency']  * self.time + component['phase'])
                signal += add_comp
            self.plot_sine_signal(signal)
            self.ismixed = True
            self.isloaded = False
            
            self.max_freq = 0
            for component in self.signals_components:
                if component["frequency"] > self.max_freq:
                    self.max_freq = component["frequency"]
            self.sampling()
            print(self.max_freq)
        else:
            self.ui.graph_orignal.clear()
            self.ui.graph_error.clear()
            self.ui.graph_recons.clear()
        
    def plot_sine_signal(self , signal): # take the finla sine signal and plot
        self.ui.graph_orignal.clear()
        self.mixed_signal = signal
            
        self.orignal_signal = self.ui.graph_orignal.plot( self.time , signal) 
        
       
        self.orignal_signal_xy = (self.time , signal )

        #set limits of the graph
        min_x , max_x , min_y , max_y = self.min_max(self.orignal_signal)
        self.ui.graph_orignal.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y)  
        self.ui.graph_orignal.getViewBox().autoRange()
        
        self.update_component_list() 
 
    def min_max(self, graph):
        min_x =  min(graph.getData()[0])
        max_x =  max(graph.getData()[0])


        min_y =  min(graph.getData()[1])
        max_y =  max(graph.getData()[1])
        return min_x  , max_x , min_y , max_y
        
    def plot_difference_between_graphs(self):
        
        self.ui.graph_error.clear()
        x_data_1, y_data_1 = self.ui.graph_orignal.plotItem.curves[0].getData()
        x_data_2, y_data_2 = self.ui.graph_recons.plotItem.curves[0].getData()
        difference = np.array(y_data_1) - np.array(y_data_2)
        data_line = self.ui.graph_error.plot(x_data_1, difference, pen='r')  
        min_x , max_x , min_y , max_y = self.min_max(data_line)
        self.ui.graph_error.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y) 
        self.ui.graph_orignal.getViewBox().autoRange()
        self.ui.graph_recons.getViewBox().autoRange() 
        self.ui.graph_error.getViewBox().autoRange() 
    
    def update_component_list(self):
        self.ui.list_comps.clear()
        # if self.ui.chk_bx_examp.isChecked():
            
        for compnent in self.signals_components:
            amplitude = compnent["amplitude"]
            frequency = compnent["frequency"]
            phase = compnent["phase"]
            self.ui.list_comps.addItem(f"{amplitude}sin(2πx({frequency}) + {phase}))")
        # else :
        #     for compnent in self.signals_components[6:]:
        #         amplitude = compnent["amplitude"]
        #         frequency = compnent["frequency"]
        #         phase = compnent["phase"]
        #         self.ui.list_comps.addItem(f"{amplitude}sin(2πx({frequency}) + {phase}))")
            
    def remove_component(self):
        delete_component_indx = self.ui.list_comps.currentRow()
        print("curr" , delete_component_indx)
        self.signals_components.pop(delete_component_indx)
        print(self.signals_components)
        # if not self.signals_components:
        #     self.ui.graph_orignal.clear()
        #     self.ui.graph_error.clear()
        #     self.ui.graph_recons.clear()
        self.plot_compose_signal()
        # self.create_signal_component()
        self.update_component_list()
        # print(self.signals_components[delete_component_indx]["phase"])

    def add_noise_try(self):
        
        if self.isloaded:
            snr_level = self.ui.dial_noise.value() / 10
            # self.ui.graph_orignal.clear()
            # self.ui.graph_orignal.plot(self.xData , self.yData  )
            y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.yData]
            self.ui.graph_orignal.clear()
            
            self.orignal_signal = self.ui.graph_orignal.plot(self.xData  ,y_with_noise  )
            # self.yData = y_with_noise
            # self.orignal_signal_loaded = (self.x , y_with_noise)
        
        if self.ismixed:
            
            snr_level = self.ui.dial_noise.value()/10
            noise = np.random.normal(0, snr_level, len(self.time))
            self.mixed_signal_with_noise = self.mixed_signal + noise
            # self.ui.graph_orignal.plot(self.mixed_signal)
            # self.ui.graph_orignal.clear()
            self.ui.graph_orignal.clear()
            self.orignal_signal = self.ui.graph_orignal.plot(self.time , self.mixed_signal_with_noise )
            # self.orignal_signal_mixed = (self.time , self.mixed_signal_with_noise )
            
        self.sampling()
        self.plot_difference_between_graphs()
    
    # def get_max_freq(self):
    #     max_frequency = self.signals_components[6]["frequency"]
    #     for component in self.signals_components[6:]:
    #         if component["frequency"] > max_frequency:
    #             max_frequency = component["frequency"]
      
    def sampling(self):
        if self.isslider:
            
            sampling_frequency = self.ui.horizontalSlider.value() * (self.max_freq)
            print("slider" , sampling_frequency)
            self.ui.lbl_samp_freq.setText(f"{self.ui.horizontalSlider.value()} fmax")
            self.ui.lbl_samp_freq.setText(f"{self.ui.horizontalSlider.value()} fmax")
        elif self.isspin:
            sampling_frequency = self.ui.spin__samp_freq.value()
            print("spin" , sampling_frequency)
        
        self.ui.lbl_fmax.setText(f"{self.max_freq}")
        self.ui.lbl_samp_freq_abs.setText(f"{sampling_frequency}")
        
        if self.ismixed:    
            # get the sampling frequency 
                
            self.ui.graph_orignal.clear()
            self.ui.graph_orignal.plot(self.orignal_signal.getData()[0] , self.orignal_signal.getData()[1] ) # dont forget to plot the orignal not only the mixed
            sampling_interval = 1 / sampling_frequency
            x_data, y_data = self.orignal_signal.getData()  # Get the data from the PlotDataItem
            num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)
            
            # sampled_signal_y = resample(y_data, num_samples)
            # sampled_signal_x = np.linspace(x_data[0], x_data[-1], len(sampled_signal_y), endpoint=False)
            
            sampled_signal_x = x_data[::int(len(x_data) / num_samples)]
            sampled_signal_y = y_data[::int(len(x_data) / num_samples)]
            
            
            sampled_plot = self.ui.graph_orignal.plot(sampled_signal_x, sampled_signal_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
            reconstructed_data = self.sinc_interp(sampled_signal_x , sampled_signal_y , x_data)
            
            self.ui.graph_recons.clear()
            rec_data_line  = self.ui.graph_recons.plot(x_data , reconstructed_data ,pen='g')
            
            

            # self.ui.graph_orignal.plot(x_data , reconstructed_data ,pen='g')
            # self.ui.graph_recons.plotItem.vb.setLimits(0 , 10 ,max(self.ui.graph_orignal.plot(x_data , reconstructed_data ,pen='g').getData()[1])  )

        if self.isloaded:
            # sampling_rate = self.ui.horizontalSlider.value() * self.max_freq
            
            
            
            
            
            # sampling_interval = 1 / sampling_rate
            # x_data, y_data = self.orignal_signal.getData()  # Get the data from the PlotDataItem
            # num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)
            
            # sampled_y = resample(y_data, num_samples)
            # sampled_x = np.linspace(x_data[0], x_data[-1], len(sampled_y), endpoint=False)
            
            
            
            
            
            
            
            
            
            
            
            
    # Ensure that x and y are NumPy arrays
            x_data, y_data = self.orignal_signal.getData()  # Get the data from the PlotDataItem
            x = np.array(x_data)
            y = np.array(y_data)

            # Determine the time increment between samples
            time_increment = 1 / sampling_frequency

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
            
            self.ui.graph_orignal.clear()
            orginal_signal = self.ui.graph_orignal.plot(self.orignal_signal.getData()[0] , self.orignal_signal.getData()[1] ) # dont forget to plot the orignal not only the mixed
        
            
            
            self.ui.graph_orignal.plot(sampled_x, sampled_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
            reconstructed_data = self.sinc_interp(sampled_x , sampled_y , x_data)
            # x_data = x_data[:len(reconstructed_data)]
            self.ui.graph_recons.clear() 
            rec_data_line = self.ui.graph_recons.plot(x_data , reconstructed_data ,pen='g')

            # self.ui.graph_orignal.plot(x_data , reconstructed_data ,pen='g')
            # self.ui.graph_recons.plotItem.vb.setLimits(0 , 10 ,max(self.ui.graph_orignal.plot(x_data , reconstructed_data ,pen='g').getData()[1])  )

        min_x , max_x , min_y , max_y = self.min_max(rec_data_line)
        self.ui.graph_recons.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y) 
        self.plot_difference_between_graphs()
            

            # return sampled_x, sampled_y§

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
        # self.ui.graph_error.plot(t_interpolated, interpolated_signal)
    





        # T = 1 / sampling_frequency
        # n = np.arange(0, 0.5 / T)
        # nT = n * T
        # # sampling_t = np.arange(-1 , 1 , sampling_rate)

        # x2 = np.sin(2 * np.pi * sampling_frequency * nT)
        
        # self.ui.graph_orignal.plot(nT, x2, symbol='o', symbolPen='r', symbolBrush='r', name='Sample Marks')
        
        
        
        
        
        
        
    
        # snr_level = self.ui.dial_noise.value() / 10
        # x =  self.orignal_signal.getData()[0]
        # y =  self.orignal_signal.getData()[1]
        # y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.loaded_signal["y"]]
        # self.ui.graph_orignal.clear()
        # self.orignal_signal
        # self.ui.graph_orignal.plot( x , y_with_noise)

def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
