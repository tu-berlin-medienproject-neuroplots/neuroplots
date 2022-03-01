import pandas as pd 
from pyqtgraph.graphicsItems.PlotDataItem import PlotDataItem
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import neurokit2 as nk

import ui.ui as ui_module
import database.database as database_module
import plot.select as select_module


plots = []  # list that contains all plotted graphs visible
#legend = ui_module.Ui_MainWindow().graph.getPlotItem().addLegend(pen = pg.mkPen(color=(204,204,204)),brush = pg.mkBrush(color=(255,255,255)),labelTextColor=(0,0,0) )
#legend = pg.LegendItem()

"""----------------------------functions----------------------"""
# Plot all visible items of database
def plotData(ui: ui_module.Ui_MainWindow, database: database_module.Database):

    #print("function: plotData")

    #get datastreams from database
    datastreams = database.getAllDatastreamsOf(1)
    
    #legend = ui.graph.getPlotItem().addLegend(pen = pg.mkPen(color=(204,204,204)),brush = pg.mkBrush(color=(255,255,255)),labelTextColor=(0,0,0) )
    #setSamplingrate(ui,database)

    for datastream in datastreams:

        #chek if datastream is visible
        if (datastream["visibility"] == 1):

            #plot datastream

            file = pd.read_csv(datastream["rawdata"])
            time = file["time"]

            pen = pg.mkPen(color=(255, 0, 0))
            # todo set samplingrate


            if datastream["datakey"] == "ECG":
                signal = nk.ecg_clean(file["ECG"],ui.samplingrate[datastream["id"]-1])
            if datastream["datakey"] == "EDA":
                signal = nk.eda_clean(file["EDA"],ui.samplingrate[datastream["id"]-1])

    
            item = PlotDataItem(time, signal, pen = pen, name= datastream["name"])

            ui.hideDataDropdown.addItem(datastream["name"])
            ui.graph.addItem(item)
            plots.append(item)

#select_module.Select.getDatastreamCopy(select_module.Select(),ui,database)
def setSamplingrate(ui: ui_module.Ui_MainWindow, database: database_module.Database):
    datastreams = database.getAllDatastreamsOf(1)
    for datastream in datastreams:
        ui.setSamplingRateWidget = QtWidgets.QInputDialog()
        ui.setSamplingRateWidget.setInputMode(2)
        ui.setSamplingRateWidget.setDoubleMaximum(100000.0)
        ui.setSamplingRateWidget.setDoubleMinimum(0.0)
        if len(ui.samplingrate) >= datastream["id"]:
            ui.setSamplingRateWidget.setDoubleValue(ui.samplingrate[datastream["id"]-1])
        ui.setSamplingRateWidget.setWindowTitle("Set Samplingrate")
        ui.setSamplingRateWidget.setLabelText("Set Samplingrate for " + datastream["datakey"])
        ui.setSamplingRateWidget.setWindowFlags(QtCore.Qt.WindowTitleHint)
        ui.setSamplingRateWidget.exec()
        if len(ui.samplingrate) >= datastream["id"]:
            ui.samplingrate[datastream["id"]-1] = ui.setSamplingRateWidget.doubleValue()
        if len(ui.samplingrate) <= datastream["id"]:
            ui.samplingrate.append(ui.setSamplingRateWidget.doubleValue())
    clearPlot(ui)
    plotData(ui,database)

def clearPlot(ui: ui_module.Ui_MainWindow):

    ui.graph.clear()

def removePlot(ui: ui_module.Ui_MainWindow, plotname):

    #print("function: removePlot")
    for item in plots:

        if (item.name() == plotname):

            #remove item from graph
            ui.graph.removeItem(item)
    for item in plots:
        if item.name() == plotname + 'del':
            ui.graph.removeItem(item)

def addPlot(ui: ui_module.Ui_MainWindow, plotname):

    #print("function: addPlot")

    for item in plots:

        if (item.name() == plotname):

            #add item to graph
            ui.graph.addItem(item)