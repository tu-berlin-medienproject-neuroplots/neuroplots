import pandas as pd
import pyqtgraph as pg
import neurokit2 as nk
from PyQt5 import QtCore, QtGui, QtWidgets
import math

import ui.ui as ui_module
import database.database as database_module

class Calculations:
    def calculateECG(self, ui: ui_module.Ui_MainWindow, database: database_module.Database):
        ecg_datastream = database.getDatastreamOfType("ECG")
        file = pd.read_csv(ecg_datastream["rawdata"])
        ecg_signal = file["ECG"]
        signals, info = nk.ecg_process(ecg_signal,ui.samplingrate)
        time = file["time"]
        dataframe = nk.ecg_analyze(signals, sampling_rate = ui.samplingrate)

        # set up table
        ui.tableCalculations.setColumnCount(2)
        ui.tableCalculations.setRowCount(2)
        ui.tableCalculations.setHorizontalHeaderLabels(['Name', 'Value'])

        ui.tableCalculations.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        ui.tableCalculations.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # heart rate mean
        ui.tableCalculations.setItem(0, 0, QtWidgets.QTableWidgetItem("Heart Rate Mean in bpm"))
        ui.tableCalculations.setItem(0, 1, QtWidgets.QTableWidgetItem(str(dataframe.loc[0][0])))

        # heart rate variability
        ui.tableCalculations.setItem(1, 0, QtWidgets.QTableWidgetItem("Heart Rate Variability Mean in ms"))
        ui.tableCalculations.setItem(1, 1, QtWidgets.QTableWidgetItem(str(dataframe.loc[0][1])))

        fromValue = ui.fromCalculateBox.text()
        toValue = ui.toCalculateBox.text()

        # calculate
        if ((fromValue != "from") and  (toValue!="to")):
            # read from and to value
            fromValue = int(fromValue)
            toValue = int (toValue)
            fromIndex = pd.Index(time).get_loc(fromValue, method="nearest")
            toIndex = pd.Index(time).get_loc(toValue, method="nearest")

            epochs_end = math.ceil((toValue - fromValue) / 1000)
            epochs = nk.epochs_create(signals, events=[fromIndex], sampling_rate=ui.samplingrate, epochs_start=0, epochs_end=epochs_end)

            # Calculations for range
            ui.tableCalculations.setRowCount(3)
            ui.tableCalculations.setItem(2, 0, QtWidgets.QTableWidgetItem(">> Calculations for range <<"))

            if (epochs_end<=10):
                dataframeFromTo = nk.ecg_eventrelated(epochs)
                baseline = dataframeFromTo.loc["1"][2]
                ui.tableCalculations.setRowCount(6)
                ui.tableCalculations.setItem(3, 0, QtWidgets.QTableWidgetItem("Heart Rate Mean in bpm"))
                ui.tableCalculations.setItem(3, 1,QtWidgets.QTableWidgetItem(str(dataframeFromTo.loc["1"][5] + baseline)))
                ui.tableCalculations.setItem(4, 0, QtWidgets.QTableWidgetItem("Heart Rate Maximum in bpm"))
                ui.tableCalculations.setItem(4, 1,QtWidgets.QTableWidgetItem(str(dataframeFromTo.loc["1"][3] + baseline)))
                ui.tableCalculations.setItem(5, 0, QtWidgets.QTableWidgetItem("Heart Rate Minimum in bpm"))
                ui.tableCalculations.setItem(5, 1,QtWidgets.QTableWidgetItem(str(dataframeFromTo.loc["1"][4] + baseline)))
            else:
                dataframeFromTo = nk.ecg_intervalrelated(epochs, sampling_rate=ui.samplingrate)
                ui.tableCalculations.setRowCount(5)
                ui.tableCalculations.setItem(3, 0, QtWidgets.QTableWidgetItem("Heart Rate Mean in bpm"))
                ui.tableCalculations.setItem(3, 1, QtWidgets.QTableWidgetItem(str(dataframeFromTo.loc["1"][1])))
                ui.tableCalculations.setItem(4, 0, QtWidgets.QTableWidgetItem("Heart Rate Variability Mean in ms"))
                ui.tableCalculations.setItem(4, 1, QtWidgets.QTableWidgetItem(str(dataframeFromTo.loc["1"][2])))
