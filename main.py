from PyQt5 import QtCore, QtGui
import os
import sys
from PyQt5.QtWidgets import QInputDialog  ,  QApplication, QMainWindow, QShortcut, QFileDialog
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
        
        self.time = np.linspace(0, 10, 1000)
        
        self.siganls_g1 = []
        self.signals_components = []
        
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.valueChanged.connect(self.add_noise)
        
        self.ui.pushButton.clicked.connect(self.load_signal)
        self.ui.pushButton_2.clicked.connect(self.create_signal_component)
        self.ui.pushButton_3.clicked.connect(self.remove_component)
        self.ui.pushButton_4.clicked.connect(self.add_noise)
        
        
        
    def load_signal(self):
        file_path  , _ = QFileDialog.getOpenFileName( self , "open file", "" ,"(*.csv) ")
        data = np.genfromtxt(file_path, delimiter = ',')
        x = data[:, 0].tolist()
        y = data[:, 1].tolist()
        file_name = os.path.basename(file_path[:-4])
        self.ui.graphicsView_2.clear()        
        self.ui.graphicsView_2.plotItem.plot(x , y , pen="#ffffff")
        self.ui.graphicsView_2.plotItem.vb.setLimits(xMin=0 , xMax=max(x), yMin=min(y) , yMax=max(y))
    
    def create_signal_component(self):
        amplitude, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your amplitude:') # this is just for now 
        phase, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your phase:')
        frequency, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your frequency:')
        
        amplitude = float(amplitude)
        phase = float(phase)
        frequency = float(frequency)
        
        signal_component = {
            "amplitude" : amplitude, 
            "phase" : phase,
            "frequency" : frequency,
        }
        
        # signal_component = amplitude * np.sin(2 * np.pi * frequency  * self.time + phase)
        self.signals_components.append(signal_component)
        # self.signals_components.append(signal_component)
        
        self.update_component_list()        
        self.plot_composed_signal()
        # self.ui.graphicsView_2.plot(self.time, signal, pen='b')
        
    def plot_composed_signal(self):
        self.ui.graphicsView_2.clear()
        signal = self.signals_components[0]['amplitude'] * np.sin(2 * np.pi * self.signals_components[0]['frequency']  * self.time + self.signals_components[0]['phase'])
        # signal = np.zeros(len(self.time))

        # signal =  np.sin(0)
        for component in self.signals_components[1:]:
            add_comp = component['amplitude'] * np.sin(2 * np.pi * component['frequency']  * self.time + component['phase'])
            signal += add_comp
        self.mixed_signal = signal
        plotted_signal = self.ui.graphicsView_2.plot(signal)
        
        min_x =  min(plotted_signal.getData()[0])
        max_x =  max(plotted_signal.getData()[0])


        min_y =  min(plotted_signal.getData()[1])
        max_y =  max(plotted_signal.getData()[1])

        self.ui.graphicsView_2.plotItem.vb.setLimits(xMin=min_x , xMax=max_x, yMin=min_y , yMax=max_y)
        
    
    # def plot_composed(self):
    def update_component_list(self):
        self.ui.listWidget.clear()
        for compnent in self.signals_components:
            amplitude = compnent["amplitude"]
            frequency = compnent["frequency"]
            phase = compnent["phase"]
            self.ui.listWidget.addItem(f"signal component : {len(self.signals_components)}  amplitude : {amplitude} , frequency : {frequency} , phase : {phase}")
            # print(self.ui.listWidget.item(0).text())
            
            
    
    def remove_component(self):
        delete_component_indx = self.ui.listWidget.currentRow()   
        self.signals_components.pop(delete_component_indx)
        self.plot_composed_signal()
        self.update_component_list()
        # print(self.signals_components[delete_component_indx]["phase"])
    
    def add_noise(self ):
        snr_level , ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your amplitude:') 
        snr_level = float(snr_level)   
        # self.ui.graphicsView_2.clear()
        signal_with_noise = self.mixed_signal
        # snr_level = self.ui.horizontalSlider.value()    
        noise = np.random.normal(0, snr_level, len(self.time))
        signal_with_noise += noise
        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_2.plot(signal_with_noise )
        
        
    # def rempove_compnent (self):
    #     component = self.ui.listWidget.currentItem()
    #     for component in self.signals_components:
    #         if 
        
        
        
        
        
            

        
    
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
