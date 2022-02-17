import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets

import ui.ui as ui_module
import database.database as database_module

class Marker:
    def __init__(self):
        self.markerLinesArray = []

    #sets the marker in the graph
    def setMarker(self, ui: ui_module.Ui_MainWindow, database : database_module.Database):
        markerTime = float(ui.markerTimeBox.text())
        markerName = str(ui.markerNameBox.text())

        marker = pg.InfiniteLine(markerTime, name="event", movable=True, pen="g")
        ui.graph.addItem(marker)

        database.createMarker(markerName, markerTime, 1)

        self.markerLinesArray.append((marker, markerName))

        self.updateMarkerUi(ui, database)
        marker.sigPositionChanged.connect(lambda: self.updateMarkerUi(ui, database))

        self.updateMarkerinDatabase(ui, database)

    #adds the added marker to the table events
    def updateMarkerUi(self, ui: ui_module.Ui_MainWindow, database : database_module.Database):

        ui.tableMarker.setRowCount(0)
        # Tabelle sortieren einfügen
        for markerTuple in self.markerLinesArray:

            row = ui.tableMarker.rowCount()
            ui.tableMarker.setRowCount(row+1)
            ui.tableMarker.setItem(row, 1, QtWidgets.QTableWidgetItem(str(markerTuple[0].getPos()[0])))
            ui.tableMarker.setItem(row, 0, QtWidgets.QTableWidgetItem(markerTuple[1]))
            ui.removeMarkerButton = QtWidgets.QPushButton()
            ui.removeMarkerButton.setText('Remove')
            ui.removeMarkerButton.clicked.connect(lambda: self.removeMarker(ui, database, markerTuple, row))
            ui.tableMarker.setCellWidget(row, 2, ui.removeMarkerButton)

    #removes an added marker
    def removeMarker(self, ui: ui_module.Ui_MainWindow, database : database_module.Database, markerTupel, row):

        self.markerLinesArray.remove(markerTupel)
        ui.graph.removeItem(markerTupel[0])
        ui.tableMarker.removeRow(row)

        database.deleteMarker(database.getMarkerByName(markerTupel[1])["id"])
        self.updateMarkerUi(ui, database)

    def loadMarkerFromDatabase(self, ui: ui_module.Ui_MainWindow, database : database_module.Database):

        markers = database.getAllMarkerOf(1)
        print(markers)
        for marker in markers:

            markerTime = marker["time"]
            markerName = marker["name"]

            marker = pg.InfiniteLine(markerTime, name="event", movable=True, pen="g")
            ui.graph.addItem(marker)

            database.createMarker(markerName, markerTime, 1)

            self.markerLinesArray.append((marker, markerName))

            self.updateMarkerUi(ui, database)
            marker.sigPositionChanged.connect(lambda: self.updateMarkerUi(ui, database))

    def updateMarkerinDatabase(self, ui: ui_module.Ui_MainWindow, database : database_module.Database):

        database.deleteAllMarker()

        for marker in self.markerLinesArray:

            database.createMarker(marker[1], marker[0].pos()[0], 1)

