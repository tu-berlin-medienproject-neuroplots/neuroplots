import pyqtgraph as pg
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

import ui.ui as ui_module
import database.database as database_module
import plot.plot as Plot

class Select:

    def __init__(self):
        self.region = pg.LinearRegionItem()
        #self.calculationsArray = pd.DataFrame()
        self.calculationsArray = []

    def selectData(self, ui: ui_module.Ui_MainWindow):

        if ui.checkBoxSelectData.isChecked():
            ui.graph.removeItem(self.region)
            ui.graph.addItem(self.region)
        elif not ui.checkBoxSelectData.isChecked():
            ui.graph.removeItem(self.region)

    def updateSelectionEditBox(self, ui: ui_module.Ui_MainWindow):

        ui.fromEditBox.setText(str(int(self.region.getRegion()[0])))
        ui.toEditBox.setText(str(int(self.region.getRegion()[1])))

    def updateRegion(self, ui: ui_module.Ui_MainWindow):

        self.region.setRegion([float(ui.fromEditBox.text()),float(ui.toEditBox.text())])

    # append the selection to the selectionsArray and to the selectionTable
    def saveSelection(self, ui: ui_module.Ui_MainWindow, database: database_module.Database,hidden):
        
        df  = pd.read_csv(database.getDatastreamRawdata(database.getDatastreamId(ui.hideDataDropdown.currentText())))
        xData = df["time"].to_numpy()
        leftborder = float(Select.find_nearest(xData,float(ui.fromEditBox.text())))
        rightborder = float(Select.find_nearest(xData,float(ui.toEditBox.text())))

        name = str(leftborder) + '_' +  str(rightborder) + '_' + ui.hideDataDropdown.currentText()
        database.createSelection(name, leftborder, rightborder, hidden, ui.hideDataDropdown.currentText(), 1)        
        self.updateSelectionUi(ui, database)
    
    # update the selection ui
    def updateSelectionUi(self, ui: ui_module.Ui_MainWindow, database : database_module.Database):

        ui.tableSelection.setRowCount(0)
        selections = database.getAllSelectionsOf(1)

        for selection in selections:

            row = ui.tableSelection.rowCount()
            ui.tableSelection.setRowCount(row+1)

            #create load Selection Button
            ui.loadSelectionButton = QtWidgets.QPushButton()
            ui.loadSelectionButton.setText('Load')
            ui.tableSelection.setCellWidget(row,0,ui.loadSelectionButton)
            ui.loadSelectionButton.clicked.connect(lambda state,a = selection["id"]: self.loadSelection(a, ui, database))
            
            # set start and end of selection
            ui.tableSelection.setItem(row,1,QtWidgets.QTableWidgetItem(str(selection["starttime"])))
            ui.tableSelection.setItem(row,2,QtWidgets.QTableWidgetItem(str(selection["endtime"])))

            #create hide data checkbox
            ui.hideSelectionCheckBox = QtWidgets.QCheckBox()
            if selection["hidden"] == 2:
                ui.hideSelectionCheckBox.setCheckState(QtCore.Qt.Checked)
            if selection["hidden"] == 0:
                ui.hideSelectionCheckBox.setCheckState(QtCore.Qt.Unchecked)
            ui.hideSelectionCheckBox.stateChanged.connect(lambda state, a = selection["id"]: database.updateSelectionHidden(a,state))
            #ui.hideSelectionCheckBox.stateChanged.connect(lambda state, a = selection["id"]: self.updateSelectionUi(ui,database))
            ui.hideSelectionCheckBox.clicked.connect(lambda state, a = selection["id"]: self.loadSelection(a, ui, database))
            ui.hideSelectionCheckBox.clicked.connect(lambda state, a = selection["id"]: self.updateHidden(state,a, ui,database))
            ui.tableSelection.setCellWidget(row,3,ui.hideSelectionCheckBox)

            #create remove Button
            ui.removeSelectionButton = QtWidgets.QPushButton()
            ui.removeSelectionButton.setText('Remove')
            ui.removeSelectionButton.clicked.connect(lambda state, a = selection["id"]: self.removeSelection(a, ui, database))
            ui.tableSelection.setCellWidget(row,4,ui.removeSelectionButton)

            # set applied on
            ui.tableSelection.setItem(row,5,QtWidgets.QTableWidgetItem(str(selection["appliedOn"])))

   # #remove the selected selection from the tableSelection and selectionsArray
    def removeSelection(self, id, ui: ui_module.Ui_MainWindow, database : database_module.Database):
        self.unhideData(id,ui,database)
        database.deleteSelection(id)
        self.updateSelectionUi(ui, database)

    #load and display the selection selected in the lower left window
    def loadSelection(self, id, ui: ui_module.Ui_MainWindow, database : database_module.Database):

        ui.fromEditBox.setText(str(database.getSelection(id)["starttime"]))
        ui.toEditBox.setText(str(database.getSelection(id)["endtime"]))
        ui.hideDataDropdown.setCurrentText(str(database.getSelection(id)["appliedOn"]))
        ui.checkBoxSelectData.setChecked(True)

        self.updateRegion(ui)
        self.selectData(ui)
    
    # finds nearest value in an array (necessary for hide data)
    def find_nearest(array,value):
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return array[idx]

    #creates new PlotDataItem in grey which is put over original graph to visualize the toggled data
    def readHideData(self, ui: ui_module.Ui_MainWindow, database : database_module.Database, addSelection):
        df  = pd.read_csv(database.getDatastreamRawdata(database.getDatastreamId(ui.hideDataDropdown.currentText())))
        xData = df["time"].to_numpy()
        leftborder = Select.find_nearest(xData,float(ui.fromEditBox.text()))
        rightborder = Select.find_nearest(xData,float(ui.toEditBox.text()))
        leftindex = df.index[df["time"] == leftborder].tolist()
        rightindex = df.index[df["time"] == rightborder].tolist()
        #delete everything except chosen interval from time np array
        xData = np.delete(xData, np.arange(rightindex[0],xData.size,1))
        xData = np.delete(xData, np.arange(leftindex[0]))
        # delete everything except chosen interval from chosen datastream
        for plot in Plot.plots:
            if plot.name() == ui.hideDataDropdown.currentText():
                _ , yData = plot.getData()
        yData = np.asarray(yData)

        # for i in range(0,leftindex[0]):
        #     yDdata[i] = np.nan
        # for i in range(rightindex[0], yData.size):
        #     yData[i] = np.nan

        yData = np.delete(yData, np.arange(rightindex[0], yData.size,1))
        yData = np.delete(yData, np.arange(leftindex[0]))

        name = ui.hideDataDropdown.currentText() + 'del'
        grey = pg.PlotDataItem(xData, yData, pen = pg.mkPen(color=(220,220,220)), name=name)
        ui.graph.addItem(grey)
        Plot.plots.append(grey)
        if addSelection:
            self.saveSelection(ui, database, 2)
        if not addSelection:
            for selection in database.getAllSelectionsOf(1):
                if selection["appliedOn"] == ui.hideDataDropdown.currentText() and selection["starttime"] == leftborder and selection["endtime"] == rightborder:
                    selection["hidden"] = 2
    
    # forwards to necessary hide function
    def updateHidden(self,state, id,ui: ui_module.Ui_MainWindow, database : database_module.Database):
        #database.updateHidden(id,state)
        if state:
            self.readHideData(ui,database,False)
            self.hideData(id,ui,database)
        if not state:
            self.unhideData(id,ui,database)
    
    # unhides data
    def unhideData(self, id, ui: ui_module.Ui_MainWindow, database : database_module.Database):
        selection = database.getSelection(id)

        name = selection['appliedOn'] + 'del'
        for plot in Plot.plots:
            if plot.name() == name:
                ui.graph.removeItem(plot)
                Plot.plots.remove(plot)
                print(plot.name() + " has been removed successfully")
        for datastream in database.getAllDatastreamsOf(1):
            file = pd.read_csv(datastream["rawdata"])
            xData = file["time"].to_numpy()
            leftindex = file.index[file["time"] == Select.find_nearest(xData,float(ui.fromEditBox.text()))].tolist()
            rightindex = file.index[file["time"] == Select.find_nearest(xData,float(ui.toEditBox.text()))].tolist()
            if datastream["name"] == selection["appliedOn"]:
                for i in range(leftindex[0],rightindex[0]+1):
                    #self.calculationsArray.loc[i,datastream["datakey"]] = file[datastream["datakey"]][i]
                    self.calculationsArray[database.getDatastreamId(datastream["name"])-1][i] = file[datastream["datakey"]][i]
    
    # get copy of datastream not used ccurrently
    def getDatastreamCopy(self,ui: ui_module.Ui_MainWindow, database : database_module.Database):
        datastreams = database.getAllDatastreamsOf(1)
        for datastream in datastreams:
            file = pd.read_csv(datastream["rawdata"])
            self.calculationsArray.insert(datastream["id"]-1,datastream["datakey"],file[datastream["datakey"]])
        print(self.calculationsArray)
    #hides data for datastream
    j = 0
    def hideData(self, id, ui: ui_module.Ui_MainWindow, database : database_module.Database):
        
        #datastream  = pd.read_csv(database.getDatastreamRawdata(database.getDatastreamId(ui.hideDataDropdown.currentText())))
        datastreams = database.getAllDatastreamsOf(1)
        selection = database.getSelection(id)
        if self.j == 0:
            for datastream in datastreams:
                file = pd.read_csv(datastream["rawdata"])
                #self.calculationsArray.insert(datastream["id"]-1,datastream["datakey"],file[datastream["datakey"]])
                self.calculationsArray.append(file[datastream["datakey"]])
            self.j += 1
        
        for datastream in datastreams:
            file = pd.read_csv(datastream["rawdata"])
            xData = file["time"].to_numpy()
            leftindex = file.index[file["time"] == Select.find_nearest(xData,float(ui.fromEditBox.text()))].tolist()
            rightindex = file.index[file["time"] == Select.find_nearest(xData,float(ui.toEditBox.text()))].tolist()
            if selection["hidden"] == 2:
                if datastream["name"] == selection["appliedOn"]:
                    #if datastream["datakey"] == "ECG":
                        for i in range(leftindex[0],rightindex[0]+1):
                            #self.calculationsArray.loc[i,datastream["datakey"]] = 0
                            self.calculationsArray[database.getDatastreamId(datastream["name"])-1][i] = 0
                            #self.calculationsArray[0][i] = 0

