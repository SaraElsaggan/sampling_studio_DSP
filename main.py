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
        self.ui.dial.valueChanged.connect(self.add_noise)
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
    
   


    def add_noise(self):
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
            self.ui.graphicsView_2.plot(self.time , self.mixed_signal) 
            
            sampling_frequency = self.ui.horizontalSlider.value() * (max_frequency)
            # sampling_frequency = 100
            sampling_interval = 1 / sampling_frequency
            x_data, y_data = self.orignal_signal.getData()  
            num_samples = int((x_data[-1] - x_data[0]) / sampling_interval)

            sampled_signal_x = x_data[::int(len(x_data) / num_samples)]
            sampled_signal_y = y_data[::int(len(x_data) / num_samples)]
            sampled_plot = self.ui.graphicsView_2.plot(sampled_signal_x, sampled_signal_y ,  pen=None, symbol='o', symbolSize=7, symbolPen='b', symbolBrush='b')
        # if self.isloaded:
        #     self.sample_loaded_signal()
            

        
        
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
