import pandas as pd 
from pyqtgraph.graphicsItems.PlotDataItem import PlotDataItem
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import neurokit2 as nk

import ui.ui as ui_module
import database.database as database_module
import plot.select as select_module


plots = []  # list that contains all plotted graphs visible


"""----------------------------functions----------------------"""
# Plot all visible items of database
def plotData(ui: ui_module.Ui_MainWindow, database: database_module.Database):

    print("function: plotData")

    #get datastreams from database
    datastreams = database.getAllDatastreamsOf(1)
    setSamplingrate(ui)
    ui.graph.getPlotItem().addLegend(pen = pg.mkPen(color=(204,204,204)),brush = pg.mkBrush(color=(255,255,255)),labelTextColor=(0,0,0) )

    for datastream in datastreams:

        #chek if datastream is visible
        if (datastream["visibility"] == 1):

            #plot datastream

            file = pd.read_csv(datastream["rawdata"])
            time = file["time"]

            pen = pg.mkPen(color=(255, 0, 0))
            # todo set samplingrate


            if datastream["datakey"] == "ECG":
                signal = nk.ecg_clean(file["ECG"],ui.samplingrate)
            if datastream["datakey"] == "EDA":
                signal = nk.eda_clean(file["EDA"],ui.samplingrate)

    
            item = PlotDataItem(time, signal, pen = pen, name= datastream["name"])

            ui.hideDataDropdown.addItem(datastream["name"])
            ui.graph.addItem(item)
            plots.append(item)

#select_module.Select.getDatastreamCopy(select_module.Select(),ui,database)
def setSamplingrate(ui: ui_module.Ui_MainWindow):
    ui.setSamplingRateWidget = QtWidgets.QInputDialog()
    ui.setSamplingRateWidget.setInputMode(2)
    ui.setSamplingRateWidget.setDoubleMaximum(100000.0)
    ui.setSamplingRateWidget.setDoubleMinimum(0.0)
    ui.setSamplingRateWidget.setDoubleValue(ui.samplingrate)
    ui.setSamplingRateWidget.setWindowTitle("Set Samplingrate")
    ui.setSamplingRateWidget.setWindowFlags(QtCore.Qt.WindowTitleHint)
    ui.setSamplingRateWidget.exec()
    ui.samplingrate = ui.setSamplingRateWidget.doubleValue()

def clearPlot(ui: ui_module.Ui_MainWindow):

    ui.graph.clear()

def removePlot(ui: ui_module.Ui_MainWindow, plotname):

    print("function: removePlot")
    print(plotname)
    for item in plots:

        if (item.name() == plotname):

            #remove item from graph
            ui.graph.removeItem(item)
    for item in plots:
        if item.name() == plotname + 'del':
            ui.graph.removeItem(item)

def addPlot(ui: ui_module.Ui_MainWindow, plotname):

    print("function: addPlot")
    print(plotname)

    for item in plots:

        if (item.name() == plotname):

            #add item to graph
            ui.graph.addItem(item)