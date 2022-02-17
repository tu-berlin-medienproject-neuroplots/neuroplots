from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd 

import database.database as database_module
import ui.ui as ui_module
import plot.plot as plot_module


def importdata(filename, database: database_module.Database):

    file = pd.read_csv(filename.url())

    for col in file:
        if col != "time":
            database.createDatastream(filename.fileName() + "_" + col, 0, filename.url(), col, col, 1, True)

def updateDatastreamUi(ui: ui_module.Ui_MainWindow, database : database_module.Database):

    ui.tableDatasets.setRowCount(0)
    datastreams = database.getAllDatastreamsOf(1)

    for datastream in datastreams:        

        row = ui.tableDatasets.rowCount()
        ui.tableDatasets.setRowCount(row+1)

        #set name
        ui.tableDatasets.setItem(row,0,QtWidgets.QTableWidgetItem(str(datastream["name"])))
        #set offset
        ui.tableDatasets.setItem(row,1,QtWidgets.QTableWidgetItem(str(datastream["offset"])))
        #set file
        ui.tableDatasets.setItem(row,2,QtWidgets.QTableWidgetItem(str(datastream["rawdata"])))

        #create visible checkbox
        ui.visibilityDatastreamCheckBox = QtWidgets.QCheckBox()
        ui.visibilityDatastreamCheckBox.setCheckState(QtCore.Qt.Checked)
        ui.visibilityDatastreamCheckBox.clicked.connect(lambda state, a = datastream["id"]: updateVisibilityDatastream(state, a, ui, database))
        ui.tableDatasets.setCellWidget(row,3,ui.visibilityDatastreamCheckBox)
        
        #create remove Button
        ui.removeDatastreamButton = QtWidgets.QPushButton()
        ui.removeDatastreamButton.setText('Remove')
        ui.removeDatastreamButton.clicked.connect(lambda state, a = datastream["id"]: removeDatastream(a, ui, database))
        ui.tableDatasets.setCellWidget(row,4,ui.removeDatastreamButton)

def updateVisibilityDatastream(state, id, ui: ui_module.Ui_MainWindow, database : database_module.Database):

    database.updateDatastreamVisibility(id, state)

    if state:
        plot_module.addPlot(ui, database.getDatastreamName(id))
    if not state:
        plot_module.removePlot(ui, database.getDatastreamName(id))

def removeDatastream(id, ui: ui_module.Ui_MainWindow, database : database_module.Database):

    plot_module.removePlot(ui, database.getDatastreamName(id))
    database.deleteDatastream(id)
    updateDatastreamUi(ui, database)