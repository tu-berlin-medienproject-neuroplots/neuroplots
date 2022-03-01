import core

import ui.ui as ui_module
import database.database as database_module
import plot.select as select_module
import plot.events as event_module
import plot.marker as marker_module
import plot.plot as plot_module
import plot.calculations as calculations_module

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

"""----------------------------setup ui--------------------"""
app = ui_module.QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ui_module.Ui_MainWindow()
ui.setupUi(MainWindow)

"""----------------------------setup database--------------------"""
database = database_module.Database()

"""----------------------------setup select--------------------"""
select = select_module.Select()

"""----------------------------setup events--------------------"""
events = event_module.Events()

"""----------------------------setup marker--------------------"""
marker = marker_module.Marker()

"""----------------------------setup calculations--------------------"""
calculations = calculations_module.Calculations()

"""----------------------------connections--------------------"""
ui.actionNewProject.triggered.connect(lambda: core.newproject(ui, MainWindow, database, select, events, marker))
ui.actionOpenProject.triggered.connect(lambda: core.openproject(ui, MainWindow, database, select, events, marker))
ui.actionSaveProject.triggered.connect(lambda: core.saveproject(MainWindow, database))
ui.actionSaveProjectAs.triggered.connect(lambda: core.saveprojectas(MainWindow, ui, database, marker, events))
ui.actionImportData.triggered.connect(lambda: core.importdata(ui, MainWindow, database))
ui.actionExtraSetSamplingrate.triggered.connect(lambda: plot_module.setSamplingrate(ui,database))
ui.checkBoxSelectData.clicked.connect(lambda: select.selectData(ui))
select.region.sigRegionChanged.connect(lambda: select.updateSelectionEditBox(ui))
ui.fromEditBox.returnPressed.connect(lambda: select.updateRegion(ui))
ui.toEditBox.returnPressed.connect(lambda: select.updateRegion(ui))
ui.selectDataSaveButton.clicked.connect(lambda: select.saveSelection(ui, database, False))
ui.selectDataHideButton.clicked.connect(lambda: select.readHideData(ui, database,True))
ui.selectDataHideButton.clicked.connect(lambda state, id = len(database.getAllSelectionsOf(1)) +1: select.hideData(id, ui, database))
ui.applyPeakButton.clicked.connect(lambda: events.applySelectedPeak(select, ui, database))
ui.decomposeEdaButton.clicked.connect(lambda: events.decomposeEda(select, ui, database))
ui.setMarkerButton.clicked.connect(lambda: marker.setMarker(ui, database))
ui.calculateButton.clicked.connect(lambda: calculations.calculateECG(ui, database))
ui.addPeakButton.clicked.connect(lambda: events.addSinglePeak(select, ui, database))


"""----------------------stylesheet---------------------------"""
#app.setStyleSheet ("QCheckBox#checkBoxSelectData:checked {image:url(:/images/checked.png);}")
"""-----------------------------------------------------------"""
if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())
