# import interpolate
from scipy.interpolate import interp1d
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
from sampling_studio import Ui_MainWindow  

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("sampling studio")
        
        self.time = np.linspace(0, 2 , 1000)
        self.signals_components = []

        self.plotted_orignal_signal = None
        self.orignal_signal = None
        self.max_freq = None
        
        self.xData = None
        self.yData = None
        self.y_with_noise = None

        self.mixed_signal = None        
        self.mixed_signal_with_noise = None

        self.ismixed = False
        self.isloaded= False
        
        self.ui.horizontalSlider.setMinimum(1)
        self.ui.horizontalSlider.setMaximum(4)
        
        self.ui.dial_noise.setMinimum(0)
        self.ui.dial_noise.setMaximum(10)
        self.ui.dial_noise.valueChanged.connect(self.add_noise_try)
        self.ui.horizontalSlider.valueChanged.connect(self.input_freq_slider)
        self.ui.lineEdit.editingFinished.connect(self.input_freq_spin)
        self.ui.btn_import.clicked.connect(self.load_signal)
        self.ui.btn_add_comp.clicked.connect(self.create_signal_component)
        self.ui.btn_remove.clicked.connect(self.remove_component)
        
    
        
        self.ui.btn_mixed_plot.clicked.connect(self.mix_components)
        
        self.ui.comb_bx_examp.currentIndexChanged.connect(self.plot_example)
        
        self.ui.btn_clear.clicked.connect(self.clear_graphs)
      
        self.isslider = True
        
        
        self.example_1 = np.sin(2 * np.pi * 6  * self.time ) + np.sin(2 * np.pi * 2  * self.time)
        self.example_2 = np.sin(2 * np.pi * 5  * self.time ) +2 * np.sin(2 * np.pi * 3  * self.time)
        self.example_3 =2 *np.sin(2 * np.pi * 4  * self.time ) +  np.sin(2 * np.pi * 1 * self.time) + np.sin(2* np.pi * 3 * self.time)


   
   
   
    def clear_graphs(self):
        self.ui.graph_error.clear()
        self.ui.graph_recons.clear()
        self.ui.graph_orignal.clear()
   
    def input_freq_slider(self):
        self.isslider = True
        self.isspin = False
        self.sampling()
    
    def input_freq_spin(self):
        self.isslider = False
        self.isspin = True
        self.sampling()
        
    def load_signal(self):
        #get the data file and read it
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")
        data = pd.read_csv(file_path)
        self.yData = data.values[:, 1]
        self.xData = data.values[:, 0]
        # clear the orignal graph
        # self.ui.graph_orignal.clear()
        #plot the orignal signal
        self.plotted_orignal_signal = self.ui.graph_orignal.plotItem.plot(self.xData , self.yData , pen="#ffffff")
        
        self.ui.graph_orignal.plotItem.vb.setLimits(xMin= np.min(self.xData), xMax=max(self.xData), yMin=min(self.yData) , yMax=max(self.yData))
        # self.ui.graph_orignal.getViewBox().autoRange()
        
        self.isloaded = True
        self.ismixed = False
        #sample the uploaded signal
        # self.max_freq = 62.5
        self.sampling()

    def create_signal_component(self):
        '''
        this function takes the sine signal input from the user and add to our components list 
        then call the mix finc
        and update the component list 
        '''
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
        self.mix_components()
        self.update_component_list()
       
    def plot_example(self):
        '''
        this creates and plot the examples 
        when called it polots and sample the selected example
        '''
        self.ismixed = True
        self.isloaded = False


        if self.ui.comb_bx_examp.currentIndex() == 1:
            self.max_freq = 6
            self.mixed_signal = self.example_1
        elif self.ui.comb_bx_examp.currentIndex() == 2:
            self.max_freq = 5
            self.mixed_signal = self.example_2

        elif self.ui.comb_bx_examp.currentIndex() == 3:
            self.max_freq = 4
            self.mixed_signal = self.example_3
        
        self.yData = self.mixed_signal

        self.plot_sine_signal(self.mixed_signal)
        
    def mix_components(self):
        '''
        this function takes the signal components and mix then it calss the plotting function
        '''
        if self.signals_components:
            self.max_freq = self.signals_components[0]["frequency"]
            
            signal = self.signals_components[0]['amplitude'] * np.sin(2 * np.pi * self.signals_components[0]['frequency']  * self.time + self.signals_components[0]['phase'])
            for component in self.signals_components[1:]:
                add_comp = component['amplitude'] * np.sin(2 * np.pi * component['frequency']  * self.time + component['phase'])
                signal += add_comp
                if component["frequency"] > self.max_freq:
                    self.max_freq = component["frequency"]
            self.yData = signal
            self.ismixed = True
            self.isloaded = False
            self.plot_sine_signal(signal)
        
    def plot_sine_signal(self , signal): 
        '''
        plots the final sine signal
        '''
        self.mixed_signal = signal
            
        self.ui.graph_orignal.clear()
        self.plotted_orignal_signal = self.ui.graph_orignal.plot( self.time , signal) 
        
       
        #set limits of the graph
        min_x , max_x , min_y , max_y = self.min_max(self.plotted_orignal_signal)
        self.ui.graph_orignal.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y)  
        self.ui.graph_orignal.getViewBox().autoRange()
        
        self.sampling()

    def min_max(self, graph):
        '''
        this funcrion is to cala the min and max of graph to set it limits
        '''
        min_x =  min(graph.getData()[0])
        max_x =  max(graph.getData()[0])


        min_y =  min(graph.getData()[1])
        max_y =  max(graph.getData()[1])
        return min_x  , max_x , min_y , max_y
        
        
    
    
    
    def edit_graphs(self):
        min_x , max_x , min_y , max_y = self.min_max(self.plotted_orignal_signal)
        self.ui.graph_orignal.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y) 
        self.ui.graph_recons.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y)
        self.ui.graph_error.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=min_y - 2 , yMax=max_y + 2) 
        if self.isloaded:
            self.ui.graph_error.plotItem.vb.setLimits( xMin=min_x , xMax=max_x, yMin=-1 , yMax=1) 
        
        self.ui.graph_orignal.getViewBox().autoRange()
        self.ui.graph_error.getViewBox().autoRange()
        self.ui.graph_recons.getViewBox().autoRange()
        # self.ui.graph_recons.setYRange( min_y-2 , max_y+2)
        self.ui.graph_error.setYRange( min_y-1 , max_y+2)

    
    def plot_difference_between_graphs(self):
        
        self.ui.graph_error.clear()
        x_data_1, y_data_1 = self.ui.graph_orignal.plotItem.curves[0].getData()
        x_data_2, y_data_2 = self.ui.graph_recons.plotItem.curves[0].getData()
        # difference = np.array(self.mixed_signal) - np.array(y_data_2)
        difference = np.array(self.yData) - np.array(y_data_2)
        # difference = np.array(y_data_1) - np.array(y_data_2)
        data_line = self.ui.graph_error.plot(x_data_1, difference, pen='r')  
       
        self.edit_graphs()
       
    def update_component_list(self):
        '''
        this funcrion is to update the list widget in the ui
        '''
        self.ui.list_comps.clear()
        for compnent in self.signals_components:
            amplitude = compnent["amplitude"]
            frequency = compnent["frequency"]
            phase = compnent["phase"]
            self.ui.list_comps.addItem(f"{amplitude}sin(2πx({frequency}) + {phase}))")
            
    def remove_component(self):
        '''
        removes a signal component and update the graphs and the list 
        '''
        delete_component_indx = self.ui.list_comps.currentRow()
        self.signals_components.pop(delete_component_indx)
        self.mix_components()
        self.update_component_list()

    def add_noise_try(self):
        '''
        add noise to the signal
        '''
        snr_level = self.ui.dial_noise.value() / 10
        self.ui.graph_orignal.clear()
        
        if self.isloaded:
            self.y_with_noise = [value + np.random.uniform(-snr_level, snr_level) for value in self.yData]
            
            self.plotted_orignal_signal = self.ui.graph_orignal.plot(self.xData  ,self.y_with_noise  )
        
        if self.ismixed:
            
            noise = np.random.normal(0, snr_level, len(self.time))
            self.mixed_signal_with_noise = self.mixed_signal + noise
            self.plotted_orignal_signal = self.ui.graph_orignal.plot(self.time , self.mixed_signal_with_noise )
            
        self.sampling()

    def get_sampling_freq(self):
        '''
        is to get the sampling freq from the slider of the spinbox
        '''
        if self.isslider:
            sampling_frequency = self.ui.horizontalSlider.value() * (self.max_freq)
            # self.ui.lbl_samp_freq.setText(f"{self.ui.horizontalSlider.value()} fmax")
            # self.ui.lbl_samp_freq.setText(f"{self.ui.horizontalSlider.value()} fmax")
        elif self.isspin:
            sampling_frequency = float(self.ui.lineEdit.text())

        # self.ui.lbl_fmax.setText(f"{self.max_freq}")
        # self.ui.lbl_samp_freq_abs.setText(f"{sampling_frequency}")
        
        return(sampling_frequency)
    
    def sampling(self):
        
        self.ui.graph_orignal.clear()
        self.ui.graph_error.clear()
        self.ui.graph_recons.clear()
        
        if self.ismixed:    
            sampling_frequency = self.get_sampling_freq()

            self.ui.graph_orignal.plot(self.plotted_orignal_signal.getData()[0] , self.plotted_orignal_signal.getData()[1] ) 
            x_data, y_data = self.plotted_orignal_signal.getData()  # Get the data from the PlotDataItem

            sampling_interval = 1 / sampling_frequency
            num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)
            
            
            
            sampled_signal_x = np.linspace(min(x_data), max(x_data), num_samples ,endpoint=False)
            
            # sampled_signal_y , _ = resample(y_data, num_samples ,x_data )
            sampled_signal_y = np.interp(sampled_signal_x, x_data, y_data)
            # print("sss" , int(sampling_frequency))
            # sampled_signal_y , _ = resample(y_data, int(sampling_frequency) ,x_data )
            # print(len(sampled_signal_y))
            # sampled_signal_x = np.arange(x_data[0], x_data[-1], sampling_interval)
            # print(len(_))
            
            # sampled_signal_x = np.linspace(x_data[0], x_data[-1], num_samples, endpoint=False)
            

            # f = interp1d(x_data, y_data, kind='linear')
            # sampled_signal_y = f(sampled_signal_x)
            
            self.ui.graph_orignal.plot(sampled_signal_x, sampled_signal_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
            reconstructed_data = self.sinc_interp(sampled_signal_x , sampled_signal_y , x_data)
            
            rec_data_line  = self.ui.graph_recons.plot(x_data , reconstructed_data ,pen='g')


            
        if self.isloaded:
            # Ensure that x and y are NumPy arrays
            x_data, y_data = self.plotted_orignal_signal.getData()  # Get the data from the PlotDataItem
            x = np.array(x_data)
            y = np.array(y_data)
            self.max_freq = 1/(x_data[1] - x_data[0])/2
            sampling_frequency = self.get_sampling_freq()

            print(sampling_frequency)
            
            sampling_interval = 1 / sampling_frequency
            num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)
            
            
            # sampled_y , _ = resample(y_data, num_samples , x_data)
            sampled_x = np.linspace(x_data[0], x_data[-1], num_samples,  endpoint=False)
            f = interp1d(x_data, y_data, kind='linear')
            sampled_y = f(sampled_x)

            orginal_signal = self.ui.graph_orignal.plot(self.plotted_orignal_signal.getData()[0] , self.plotted_orignal_signal.getData()[1] ) # dont forget to plot the orignal not only the mixed
        
            
            
            self.ui.graph_orignal.plot(sampled_x, sampled_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
            reconstructed_data = self.sinc_interp(sampled_x , sampled_y , x_data)
            rec_data_line = self.ui.graph_recons.plot(x_data , reconstructed_data ,pen='g')

           
        self.plot_difference_between_graphs()

    def sinc_interp(self, sampled_x, sampled_y, xData):
        
        if len(sampled_y) != len(sampled_x):
            raise ValueError('x and s must be the same length')

    # Find the period
        T_s = sampled_x[1] - sampled_x[0]

        sincM = np.tile(xData, (len(sampled_x), 1)) - \
            np.tile(sampled_x[:, np.newaxis], (1, len(xData)))
        reconstructed = np.dot(sampled_y, np.sinc(sincM/T_s))
        return reconstructed


def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
