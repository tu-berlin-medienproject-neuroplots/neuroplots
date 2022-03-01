import pandas as pd
import pyqtgraph as pg
import neurokit2 as nk
from PyQt5 import QtCore, QtGui, QtWidgets

import ui.ui as ui_module
import database.database as database_module
import plot.select as select_module
import plot.plot as Plot


class Events:
    def __init__(self):
        self.rpeaks_array = []  #list with all rpeaks as single infiniteline Items current visible
        self.speaks_array = []
        self.tpeaks_array = []
        self.onsets_array = []
        self.peak_array = []
        self.recovery_array = []

        self.phases = []


    # Function thats checks which type of peak in the combobox is selected
    def applySelectedPeak(self, select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database):

        selectedPeak = ui.peakBox.currentText()
        
        if (selectedPeak == "R Peaks"):
            self.findPeaks(select, ui, database, "R_Peak","ECG_R_Peaks", self.rpeaks_array,"b")
        if (selectedPeak== "S Peaks"):
            self.findPeaks(select, ui, database, "S_Peak","ECG_S_Peaks", self.speaks_array,"y")  
        if (selectedPeak == "T Peaks"):
            self.findPeaks(select, ui, database, "T_Peak", "ECG_T_Peaks", self.tpeaks_array,"g")    
        if (selectedPeak == "Peak Onsets"):
            self.findEdaPeaks(select, ui, database, "Peak_Onsets","SCR_Onsets", self.onsets_array,"b")
        if (selectedPeak== "Peak Amplitude"):
            self.findEdaPeaks(select, ui, database, "Peak_Amplitude","SCR_Peaks", self.peak_array,"y")  
        if (selectedPeak == "Half-Recovery Time"):
            self.findEdaPeaks(select, ui, database, "Half_Recovery_Time", "SCR_Recovery", self.recovery_array,"g")  

    def addSinglePeak(self, select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database):

        selectedPeak = ui.peakBox.currentText()
        
        if (selectedPeak == "R Peaks"):
            self.findSinglePeak(select, ui, database, "R_Peak","ECG_R_Peaks", self.rpeaks_array,"b")
        if (selectedPeak== "S Peaks"):
            self.findSinglePeak(select, ui, database, "S_Peak","ECG_S_Peaks", self.speaks_array,"y")  
        if (selectedPeak == "T Peaks"):
            self.findSinglePeak(select, ui, database, "T_Peak", "ECG_T_Peaks", self.tpeaks_array,"g")    
        if (selectedPeak == "Peak Onsets"):
            self.findSinglePeak(select, ui, database, "Peak_Onsets","SCR_Onsets", self.onsets_array,"b")
        if (selectedPeak== "Peak Amplitude"):
            self.findSinglePeak(select, ui, database, "Peak_Amplitude","SCR_Peaks", self.peak_array,"y")  
        if (selectedPeak == "Half-Recovery Time"):
            self.findSinglePeak(select, ui, database, "Half_Recovery_Time", "SCR_Recovery", self.recovery_array,"g")           

    # Function thats checks which type of eda peak in the combobox is selected
    def applySelectedEdaPeak(self, select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database):

        selectedPeak = ui.peakBoxEda.currentText()
        
        if (selectedPeak == "Peak Onsets"):
            self.findEdaPeaks(select, ui, database, "Peak_Onsets","SCR_Onsets", self.onsets_array,"b")
        if (selectedPeak== "Peak Amplitude"):
            self.findEdaPeaks(select, ui, database, "Peak_Amplitude","SCR_Peaks", self.peak_array,"y")  
        if (selectedPeak == "Half-Recovery Time"):
            self.findEdaPeaks(select, ui, database, "Half_Recovery_Time", "SCR_Recovery", self.recovery_array,"g")   

    #Function that adds one Peak of the selected Peak to the Plot        

    def findSinglePeak(self, select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database, name, peak, array, color):
        
        
        def remove_on_click(self):
            ui.graph.removeItem(self)
            for i in array:
                if i.getPos() == self.getPos():
                    array.remove(i)
        time = int(ui.addPeakInput.text())         
        peak = pg.InfiniteLine(time, name = name, movable = True , pen =color) 
        peak.sigClicked.connect(remove_on_click)           
        ui.graph.addItem(peak)
        array.append(peak)
        
    def findPeaks(self, select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database, name, peak, array, color):

        ecg_datastream = database.getDatastreamOfType("ECG")
        file = pd.read_csv(ecg_datastream["rawdata"])
        if len(select.calculationsArray) == 0:
            ecg_signal = file["ECG"]
        if len(select.calculationsArray) != 0:
            ecg_signal = select.calculationsArray[database.getDatastreamId(ecg_datastream["name"])-1]
        
        time = file["time"]

        #todo noah implement belas getsamplingrate

        signals, info = nk.ecg_process(ecg_signal,ui.samplingrate[ecg_datastream["id"]-1])

        def remove_on_click(self):
            ui.graph.removeItem(self)
            for i in array:
                if i.getPos() == self.getPos():
                    array.remove(i)

        # loop through time array and rpekas at the same time
        for x,y in zip(time, signals[peak]):
            if y == 1:
                peak = pg.InfiniteLine(x, name = name, movable= True, pen = color)
                peak.sigClicked.connect(remove_on_click)

                # add plotdataitem to the PlotWidget(PlotItem)
                ui.graph.addItem(peak) 
                array.append(peak)

        self.updateEventsUi(ui)
    
    def findEdaPeaks(self, select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database, name, peak, array, color):

        eda_datastream = database.getDatastreamOfType("EDA")
        file = pd.read_csv(eda_datastream["rawdata"])
        
        if len(select.calculationsArray) == 0:
            eda_signal = file["EDA"]
        if len(select.calculationsArray) != 0:
            eda_signal = select.calculationsArray[database.getDatastreamId(eda_datastream["name"])-1]
        time = file["time"]

        #todo noah implement belas getsamplingrate

        signals, info = nk.eda_process(eda_signal,ui.samplingrate[eda_datastream["id"]-1])

        def remove_on_click(self):
            ui.graph.removeItem(self)
            for i in array:
                if i.getPos() == self.getPos():
                    array.remove(i)

        # loop through time array and rpekas at the same time
        for x,y in zip(time, signals[peak]):
            if y == 1:
                peak = pg.InfiniteLine(x, name = name, movable= True, pen = color)
                peak.sigClicked.connect(remove_on_click)

                # add plotdataitem to the PlotWidget(PlotItem)
                ui.graph.addItem(peak) 
                array.append(peak)

        self.updateEventsUi(ui)
        self.updatePeaktsinDatabase(array, database)
     
    def removePeaks(self, ui: ui_module.Ui_MainWindow, array):

        for i in array:
            ui.graph.removeItem(i)

        array.clear()

        self.updateEventsUi(ui)

    def updatePeaktsinDatabase(self, array, database: database_module.Database):

        if array:

            database.deletePeaksOfType(array[0].name())

            for peak in array:
                
                database.createPeak(peak.name(), peak.getPos()[0], peak.movable, True, True, 1)


    def updateEventsUi(self, ui: ui_module.Ui_MainWindow):

        ui.tableEvents.setRowCount(0)
        
        if self.rpeaks_array:

            row = ui.tableEvents.rowCount()
            ui.tableEvents.setRowCount(row+1)

            #set name/type of Event
            ui.tableEvents.setItem(row,0,QtWidgets.QTableWidgetItem("R-Peaks"))

            rpeaks_array = self.rpeaks_array
            def setmovable(self):
                for i in rpeaks_array:
                    i.setMovable(self)

            #create movable button
            ui.movableEventCheckBox = QtWidgets.QCheckBox()
            ui.movableEventCheckBox.setCheckState(QtCore.Qt.Checked)
            ui.movableEventCheckBox.clicked.connect(setmovable)
            ui.tableEvents.setCellWidget(row,1,ui.movableEventCheckBox)

            #create remove Button
            ui.removeEventButton = QtWidgets.QPushButton()
            ui.removeEventButton.setText('Remove')
            ui.removeEventButton.clicked.connect(lambda: self.removePeaks(ui, self.rpeaks_array))
            ui.tableEvents.setCellWidget(row,2,ui.removeEventButton)
            
        if self.speaks_array:

            row = ui.tableEvents.rowCount()
            ui.tableEvents.setRowCount(row+1)

            #set name/type of Event
            ui.tableEvents.setItem(row,0,QtWidgets.QTableWidgetItem("S-Peaks"))

            speaks_array = self.speaks_array
            def setmovable(self):
                for i in speaks_array:
                    i.setMovable(self)

            #create movable button
            ui.movableEventCheckBox = QtWidgets.QCheckBox()
            ui.movableEventCheckBox.setCheckState(QtCore.Qt.Checked)
            ui.movableEventCheckBox.clicked.connect(setmovable)
            ui.tableEvents.setCellWidget(row,1,ui.movableEventCheckBox)

            #create remove Button
            ui.removeEventButton = QtWidgets.QPushButton()
            ui.removeEventButton.setText('Remove')
            ui.removeEventButton.clicked.connect(lambda: self.removePeaks(ui, self.speaks_array))
            ui.tableEvents.setCellWidget(row,2,ui.removeEventButton)
        
        if self.tpeaks_array:

            row = ui.tableEvents.rowCount()
            ui.tableEvents.setRowCount(row+1)

            #set name/type of Event
            ui.tableEvents.setItem(row,0,QtWidgets.QTableWidgetItem("T-Peaks"))

            tpeaks_array = self.tpeaks_array
            def setmovable(self):
                for i in tpeaks_array:
                    i.setMovable(self)

            #create movable button
            ui.movableEventCheckBox = QtWidgets.QCheckBox()
            ui.movableEventCheckBox.setCheckState(QtCore.Qt.Checked)
            ui.movableEventCheckBox.clicked.connect(setmovable)
            ui.tableEvents.setCellWidget(row,1,ui.movableEventCheckBox)

            #create remove Button
            ui.removeEventButton = QtWidgets.QPushButton()
            ui.removeEventButton.setText('Remove')
            ui.removeEventButton.clicked.connect(lambda: self.removePeaks(ui, self.tpeaks_array))
            ui.tableEvents.setCellWidget(row,2,ui.removeEventButton)
        
        if self.onsets_array:

            row = ui.tableEvents.rowCount()
            ui.tableEvents.setRowCount(row+1)

            #set name/type of Event
            ui.tableEvents.setItem(row,0,QtWidgets.QTableWidgetItem("Peak-Onsets"))

            onsets_array = self.onsets_array
            def setmovable(self):
                for i in onsets_array:
                    i.setMovable(self)

            #create movable button
            ui.movableEventCheckBox = QtWidgets.QCheckBox()
            ui.movableEventCheckBox.setCheckState(QtCore.Qt.Checked)
            ui.movableEventCheckBox.clicked.connect(setmovable)
            ui.tableEvents.setCellWidget(row,1,ui.movableEventCheckBox)

            #create remove Button
            ui.removeEventButton = QtWidgets.QPushButton()
            ui.removeEventButton.setText('Remove')
            ui.removeEventButton.clicked.connect(lambda: self.removePeaks(ui, self.onsets_array))
            ui.tableEvents.setCellWidget(row,2,ui.removeEventButton)
        
        if self.peak_array:

            row = ui.tableEvents.rowCount()
            ui.tableEvents.setRowCount(row+1)

            #set name/type of Event
            ui.tableEvents.setItem(row,0,QtWidgets.QTableWidgetItem("Peak-Amplitude"))

            peak_array = self.peak_array
            def setmovable(self):
                for i in peak_array:
                    i.setMovable(self)

            #create movable button
            ui.movableEventCheckBox = QtWidgets.QCheckBox()
            ui.movableEventCheckBox.setCheckState(QtCore.Qt.Checked)
            ui.movableEventCheckBox.clicked.connect(setmovable)
            ui.tableEvents.setCellWidget(row,1,ui.movableEventCheckBox)

            #create remove Button
            ui.removeEventButton = QtWidgets.QPushButton()
            ui.removeEventButton.setText('Remove')
            ui.removeEventButton.clicked.connect(lambda: self.removePeaks(ui, self.peak_array))
            ui.tableEvents.setCellWidget(row,2,ui.removeEventButton)

        if self.recovery_array:

            row = ui.tableEvents.rowCount()
            ui.tableEvents.setRowCount(row+1)

            #set name/type of Event
            ui.tableEvents.setItem(row,0,QtWidgets.QTableWidgetItem("Half-Recovery-Time"))

            recovery_array = self.recovery_array
            def setmovable(self):
                for i in recovery_array:
                    i.setMovable(self)

            #create movable button
            ui.movableEventCheckBox = QtWidgets.QCheckBox()
            ui.movableEventCheckBox.setCheckState(QtCore.Qt.Checked)
            ui.movableEventCheckBox.clicked.connect(setmovable)
            ui.tableEvents.setCellWidget(row,1,ui.movableEventCheckBox)

            #create remove Button
            ui.removeEventButton = QtWidgets.QPushButton()
            ui.removeEventButton.setText('Remove')
            ui.removeEventButton.clicked.connect(lambda: self.removePeaks(ui, self.recovery_array))
            ui.tableEvents.setCellWidget(row,2,ui.removeEventButton)
    
    def decomposeEda(self,select: select_module.Select, ui: ui_module.Ui_MainWindow, database: database_module.Database):
        eda_datastream = database.getDatastreamOfType("EDA")
        file = pd.read_csv(eda_datastream["rawdata"])
        time = file["time"]
        eda_signal = file["EDA"]
        #eda_signal = select.calculationsArray[database.getDatastreamId(eda_datastream["name"])-1]
        data = nk.eda_phasic(nk.standardize(eda_signal), sampling_rate = ui.samplingrate[eda_datastream["id"]-1])
        itemTonic = pg.PlotDataItem(time,data["EDA_Tonic"], pen = pg.mkPen(255,165,0), name = "EDA_Tonic")
        itemPhasic = pg.PlotDataItem(time,data["EDA_Phasic"], pen = pg.mkPen(135,206,235), name = "EDA_Phasic")
        self.phases.append(itemTonic)
        self.phases.append(itemPhasic)
        ui.graph.addItem(itemTonic)
        ui.graph.addItem(itemPhasic)
        self.updateEdaUi(ui)

    def updateEdaUi(self,ui: ui_module.Ui_MainWindow):
        ui.tableFilter.setRowCount(0)
        for phase in self.phases:
            row = ui.tableFilter.rowCount()
            ui.tableFilter.setRowCount(row+1)
            # name of phase 
            ui.tableFilter.setItem(row,0,QtWidgets.QTableWidgetItem(phase.name()))
            # remove button
            ui.removeFilterButton = QtWidgets.QPushButton()
            ui.removeFilterButton.setText('Remove')
            ui.removeFilterButton.clicked.connect(lambda state, a = phase:self.removePhase(ui,a))
            ui.tableFilter.setCellWidget(row,1,ui.removeFilterButton)

    def removePhase(self, ui: ui_module.Ui_MainWindow, phase):
        
        for i in self.phases:
            if i.name() == phase.name():
                self.phases.remove(i)
                ui.graph.removeItem(i)
        self.updateEdaUi(ui)
            
    def loadPeaksFromDatabase(self, array, peaktype, ui: ui_module.Ui_MainWindow, database: database_module.Database, color):

        array.clear()
        
        def remove_on_click(self):
            ui.graph.removeItem(self)
            for i in array:
                if i.getPos() == self.getPos():
                    array.remove(i)

        #rpeaks
        peaks = database.getPeaksOfType(peaktype)
        for peak in peaks:

            thispeak = pg.InfiniteLine(peak["time"], name = peak["peaktype"], movable = peak["movable"] , pen = color) 
            thispeak.sigClicked.connect(remove_on_click)           
            ui.graph.addItem(thispeak)
            array.append(thispeak)

        




            

        

    
        
