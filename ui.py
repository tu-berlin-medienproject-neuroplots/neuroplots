# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner_old.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Heavily edited after generated. Generating this file again will cause extensive errors.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton
from pyqtgraph.widgets.PlotWidget import PlotWidget
import sys


class Ui_MainWindow(object):
    samplingrate = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1384, 847)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.fullPage = QtWidgets.QFrame(self.centralWidget)
        self.fullPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fullPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fullPage.setObjectName("fullPage")
        self.fullLayout = QtWidgets.QVBoxLayout(self.fullPage)
        self.fullLayout.setObjectName("fullLayout")
        # upperHalf: Box for function overview and graph area
        self.upperHalf = QtWidgets.QHBoxLayout()
        self.upperHalf.setObjectName("upperHalf")

        self.graph = PlotWidget(self.fullPage)
        self.graph.setObjectName("graph")

        self.upperHalf.addWidget(self.graph)
        # functionOverview: Box with all the functionalities
        self.functionOverview = QtWidgets.QVBoxLayout()
        self.functionOverview.setObjectName("functionOverview")

        # labelDataEditing: Text "Data Editing:"
        self.labelDataEditing = QtWidgets.QLabel(self.fullPage)
        self.labelDataEditing.setObjectName("labelDataEditing")
        self.functionOverview.addWidget(self.labelDataEditing)
        # peakBox: Combo Box for choosing peaks
        self.peakBox = QtWidgets.QComboBox(self.fullPage)
        self.peakBox.setObjectName("peakBox")
        self.peakBox.addItem("")
        self.peakBox.addItem("")
        self.peakBox.addItem("")
        self.peakBox.addItem("")
        self.peakBox.addItem("")
        self.peakBox.addItem("")
        self.functionOverview.addWidget(self.peakBox)
        # peakLayout: Box around peak area
        self.peakLayout = QtWidgets.QHBoxLayout()
        self.peakLayout.setContentsMargins(-1, -1, -1, 6)
        self.peakLayout.setObjectName("peakLayout")
        # applyPeaksButton: Push Button "Apply" in peak area
        self.applyPeakButton = QtWidgets.QPushButton(self.fullPage)
        self.applyPeakButton.setObjectName("applyPeakButton")
        self.decomposeEdaButton = QtWidgets.QPushButton(self.fullPage)
        self.decomposeEdaButton.setObjectName("decomposeEdaButton")
        self.peakLayout.addWidget(self.applyPeakButton)
        self.peakLayout.addWidget(self.decomposeEdaButton)
        self.functionOverview.addLayout(self.peakLayout)

        # markerLayout: Box around marker area
        self.addPeakLayout = QtWidgets.QHBoxLayout()
        self.addPeakLayout.setContentsMargins(-1, -1, -1, 6)
        self.addPeakLayout.setObjectName("addPeakLayout")
        self.addPeakInput = QtWidgets.QLineEdit(self.fullPage)
        self.addPeakInput.setObjectName("addPeakInput")
        self.addPeakButton = QtWidgets.QPushButton(self.fullPage)
        self.addPeakButton.setObjectName("addPeakButton")
        self.addPeakLayout.addWidget(self.addPeakInput, 0, QtCore.Qt.AlignHCenter)
        self.addPeakLayout.addWidget(self.addPeakButton, 0, QtCore.Qt.AlignHCenter)        
        self.functionOverview.addLayout(self.addPeakLayout)


        # EDApeakBox: Combobox for EDA peaks
        #self.peakBoxEda = QtWidgets.QComboBox(self.fullPage)
        #self.peakBoxEda.setObjectName("peakBoxEda")
        #self.peakBoxEda.addItem("")
        #self.peakBoxEda.addItem("")
        #self.peakBoxEda.addItem("")
        #self.functionOverview.addWidget(self.peakBoxEda)
        # applyEDAPeaks Button
        #self.applyEdaPeakButton = QtWidgets.QPushButton(self.fullPage)
        #self.applyEdaPeakButton.setObjectName("applyEdaPeakButton")
        #self.functionOverview.addWidget(self.applyEdaPeakButton)


        
        self.line_3 = QtWidgets.QFrame(self.fullPage)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.functionOverview.addWidget(self.line_3)

        # labelSelectData: Text "Select Data:"
        self.labelSelectData = QtWidgets.QLabel(self.fullPage)
        self.labelSelectData.setObjectName("labelSelectData")
        self.functionOverview.addWidget(self.labelSelectData)
        # selectDataLayout: Box around select data area
        self.selectDataLayout = QtWidgets.QHBoxLayout()
        self.selectDataLayout.setObjectName("selectDataLayout")
        # checkBoxSelectData: checkBoxEKG with text: "Select Data"
        self.checkBoxSelectData = QtWidgets.QCheckBox(self.fullPage)
        self.checkBoxSelectData.setObjectName("checkBoxSelectData")
        self.selectDataLayout.addWidget(self.checkBoxSelectData)

        # Combobox to select graph to hide data from
        self.hideDataDropdown = QtWidgets.QComboBox(self.fullPage)
        self.hideDataDropdown.setObjectName("hideDataDropdown")
        self.selectDataLayout.addWidget(self.hideDataDropdown)
        self.functionOverview.addLayout(self.selectDataLayout)

        # fromToLayout: Box around "from" and "to" text
        self.fromToLayout = QtWidgets.QHBoxLayout()
        self.fromToLayout.setObjectName("fromToLayout")

        # fromEditBox: Box to edit "from" value
        self.fromEditBox = QtWidgets.QLineEdit(self.fullPage)
        self.fromEditBox.setObjectName("fromEditBox")
        # toEditBox: Box to edit "to" value
        self.toEditBox = QtWidgets.QLineEdit(self.fullPage)
        self.toEditBox.setObjectName("fromEditBox")

        self.fromToLayout.addWidget(self.fromEditBox, 0, QtCore.Qt.AlignHCenter)
        self.fromToLayout.addWidget(self.toEditBox, 0, QtCore.Qt.AlignHCenter)

        self.functionOverview.addLayout(self.fromToLayout)

        # save/hide Layout
        self.saveHideLayout = QtWidgets.QHBoxLayout()
        self.saveHideLayout.setObjectName("saveHideLayout")
        # selectDataSaveButton: Push Button "Save" in select data area
        self.selectDataSaveButton = QtWidgets.QPushButton(self.fullPage)
        self.selectDataSaveButton.setObjectName("selectDataSaveButton")
        self.saveHideLayout.addWidget(self.selectDataSaveButton)
        # selectDataHideButton: Push Button "Hide" in select data area
        self.selectDataHideButton = QtWidgets.QPushButton(self.fullPage)
        self.selectDataHideButton.setObjectName("selectDataHideButton")
        self.saveHideLayout.addWidget(self.selectDataHideButton)
        self.functionOverview.addLayout(self.saveHideLayout)

        self.line_4 = QtWidgets.QFrame(self.fullPage)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.functionOverview.addWidget(self.line_4)

        # labelMarker: Text "Marker:"
        self.labelMarker = QtWidgets.QLabel(self.fullPage)
        self.labelMarker.setObjectName("labelMarker")
        self.functionOverview.addWidget(self.labelMarker)
        # markerLayout: Box around marker area
        self.markerLayout = QtWidgets.QHBoxLayout()
        self.markerLayout.setObjectName("markerLayout")
        self.functionOverview.addLayout(self.markerLayout)

        # markerNameBox: Box to edit "name" value
        self.markerNameBox = QtWidgets.QLineEdit(self.fullPage)
        self.markerNameBox.setObjectName("markerTimeBox")
        self.markerLayout.addWidget(self.markerNameBox, 0, QtCore.Qt.AlignHCenter)

        # markerTimeBox: Box to edit "time" value
        self.markerTimeBox = QtWidgets.QLineEdit(self.fullPage)
        self.markerTimeBox.setObjectName("markerTimeBox")
        self.markerLayout.addWidget(self.markerTimeBox, 0, QtCore.Qt.AlignHCenter)

        # setMarkerButton: Push Button "Set Marker" in Marker area
        self.setMarkerButton = QtWidgets.QPushButton(self.fullPage)
        self.setMarkerButton.setObjectName("setMarkerButton")
        self.functionOverview.addWidget(self.setMarkerButton)

        self.upperHalf.addLayout(self.functionOverview)
        self.fullLayout.addLayout(self.upperHalf)
        # lowerHalf: Box for lists and calculations
        self.lowerHalf = QtWidgets.QHBoxLayout()
        self.lowerHalf.setObjectName("lowerHalf")
        # tabBar: Tab bar with "Datasets", "Selection", "Filter", "Events", "Marker"
        self.tabBar = QtWidgets.QTabWidget(self.fullPage)
        self.tabBar.setObjectName("tabBar")
        # tabDatasets: Tab "Datasets"
        self.tabDatasets = QtWidgets.QWidget()
        self.tabDatasets.setObjectName("tabDatasets")
        # layoutTabDatasets: Layout of Tab "Datasets"
        self.layoutTabDatasets = QtWidgets.QGridLayout(self.tabDatasets)
        self.layoutTabDatasets.setObjectName("layoutTabDatasets")
        # tableDatasets: Table layout for list of datasets

        self.tableDatasets = QtWidgets.QTableWidget(self.tabDatasets)
        self.tableDatasets.setObjectName("ltableDatasets")
        self.tableDatasets.setColumnCount(5)
        self.tableDatasets.setHorizontalHeaderLabels(['Name', 'Offset', 'File', 'Visible', 'Remove'])
        self.tableDatasets.setRowCount(0)
        self.tableDatasets.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableDatasets.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableDatasets.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableDatasets.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableDatasets.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.layoutTabDatasets.addWidget(self.tableDatasets, 0, 0, 1, 1)

        """ 
        self.ltableDatasetsView = QtWidgets.QTableView(self.tabDatasets)
        self.ltableDatasetsView.setObjectName("ltableDatasets")
        self.ltableDatasetsmodel = QtGui.QStandardItemModel()
        self.ltableDatasetsmodel.setColumnCount(2)
        self.ltableDatasetsView.setModel(self.ltableDatasetsmodel)
        self.ltableDatasetsView.verticalHeader().hide()
        self.ltableDatasetsView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ltableDatasetsView.horizontalHeader().hide()
        self.ltableDatasetsView.setShowGrid(False) 
        """

        self.layoutTabDatasets.addWidget(self.tableDatasets, 0, 0, 1, 1)
        self.tabBar.addTab(self.tabDatasets, "")

        # tabSelection: Tab "Selection"
        self.tabSelection = QtWidgets.QWidget()
        self.tabSelection.setObjectName("tabSelection")
        # layoutTabSelection: Layout of Tab "Selection"
        self.layoutTabSelection = QtWidgets.QGridLayout(self.tabSelection)
        self.layoutTabSelection.setObjectName("layoutTabSelection")
        # tableSelection: Table layout for list of selections
        self.tableSelection = QtWidgets.QTableWidget(self.tabSelection)
        self.tableSelection.setObjectName("tableSelection")
        self.tableSelection.setColumnCount(6)
        self.tableSelection.setHorizontalHeaderLabels(['Load', 'From', 'To', 'Hide', 'Remove', 'Applied on'])
        self.tableSelection.setRowCount(0)
        self.tableSelection.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableSelection.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableSelection.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableSelection.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableSelection.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableSelection.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.layoutTabSelection.addWidget(self.tableSelection, 0, 0, 1, 1)
        self.tabBar.addTab(self.tabSelection, "")
        # tabFilter: Tab "Filter"
        self.tabFilter = QtWidgets.QWidget()
        self.tabFilter.setObjectName("tabFilter")
        # layoutTabFilter: Layout of Tab "Filter"
        self.layoutTabFilter = QtWidgets.QGridLayout(self.tabFilter)
        self.layoutTabFilter.setObjectName("layoutTabFilter")
        # tableFilter: Table layout for list of filters
        self.tableFilter = QtWidgets.QTableWidget(self.tabFilter)
        self.tableFilter.setObjectName("tableFilter")
        self.tableFilter.setColumnCount(2)
        self.tableFilter.setHorizontalHeaderLabels(['Phase', 'Remove'])
        self.tableFilter.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableFilter.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableFilter.setRowCount(0)
        self.layoutTabFilter.addWidget(self.tableFilter, 0, 0, 1, 1)
        self.tabBar.addTab(self.tabFilter, "")
        # tabEvents: Tab "Events"
        self.tabEvents = QtWidgets.QWidget()
        self.tabEvents.setObjectName("tabEvents")
        # layoutTabEvents: Layout of Tab "Events"
        self.layoutTabEvents = QtWidgets.QGridLayout(self.tabEvents)
        self.layoutTabEvents.setObjectName("layoutTabEvents")
        # tableEvents: Table layout for list of events
        self.tableEvents = QtWidgets.QTableWidget(self.tabEvents)
        self.tableEvents.setObjectName("tableEvents")
        self.tableEvents.setColumnCount(3)
        self.tableEvents.setHorizontalHeaderLabels(['Type', 'Movable', 'Remove'])
        self.tableEvents.setRowCount(0)
        self.tableEvents.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableEvents.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableEvents.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.layoutTabEvents.addWidget(self.tableEvents, 0, 0, 1, 1)
        self.tabBar.addTab(self.tabEvents, "")
        # tabMarker: Tab "Marker"
        self.tabMarker = QtWidgets.QWidget()
        self.tabMarker.setObjectName("tabMarker")
        # layoutTabMarker: Layout of Tab "Marker"
        self.LayoutTabMarker = QtWidgets.QGridLayout(self.tabMarker)
        self.LayoutTabMarker.setObjectName("LayoutTabMarker")
        # tableMarker: Table layout for list of marker
        self.tableMarker = QtWidgets.QTableWidget(self.tabMarker)
        self.tableMarker.setObjectName("tableMarker")
        self.tableMarker.setColumnCount(3)
        self.tableMarker.setHorizontalHeaderLabels(['Name', 'Time', 'Remove'])
        self.tableMarker.setRowCount(0)

        # headerTableMarker: Header of table in Tab "Marker"
        headerTableMarker = self.tableMarker.horizontalHeader()
        headerTableMarker.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        headerTableMarker.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        headerTableMarker.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.LayoutTabMarker.addWidget(self.tableMarker, 0, 0, 1, 1)
        self.tabBar.addTab(self.tabMarker, "")
        self.lowerHalf.addWidget(self.tabBar)

        # layoutLabelCalculations: Layout for Label and Button
        self.layoutLabelCalculations = QtWidgets.QHBoxLayout()
        self.layoutLabelCalculations.setObjectName("layoutLabelCalculations")

        # labelCalculations: Text "Calculations:"
        self.labelCalculations = QtWidgets.QLabel(self.fullPage)
        self.labelCalculations.setObjectName("labelCalculations")
        self.layoutLabelCalculations.addWidget(self.labelCalculations)

        # fromCalculateBox: Box to edit "from" value
        self.fromCalculateBox = QtWidgets.QLineEdit(self.fullPage)
        self.fromCalculateBox.setObjectName("fromCalculateBox")
        self.fromCalculateBox.setPlaceholderText("from")
        self.layoutLabelCalculations.addWidget(self.fromCalculateBox)
        self.labelMs01 = QtWidgets.QLabel(self.fullPage)
        self.labelMs01.setObjectName("labelMs01")
        self.layoutLabelCalculations.addWidget(self.labelMs01)
        # toCalculateBox: Box to edit "to" value
        self.toCalculateBox = QtWidgets.QLineEdit(self.fullPage)
        self.toCalculateBox.setObjectName("toCalculateBox")
        self.toCalculateBox.setPlaceholderText("to")
        self.layoutLabelCalculations.addWidget(self.toCalculateBox)
        self.labelMs02 = QtWidgets.QLabel(self.fullPage)
        self.labelMs02.setObjectName("labelMs02")
        self.layoutLabelCalculations.addWidget(self.labelMs02)

        # calculateButton: Button "Calculate"
        self.calculateButton = QtWidgets.QPushButton(self.fullPage)
        self.calculateButton.setObjectName("calculateButton")
        self.layoutLabelCalculations.addWidget(self.calculateButton, 1)

        # layoutCalculations: Layout for "calculations"
        self.layoutCalculations = QtWidgets.QVBoxLayout()
        self.layoutCalculations.setObjectName("layoutCalculations")
        self.layoutCalculations.addLayout(self.layoutLabelCalculations)

        self.tableCalculations = QtWidgets.QTableWidget(self.fullPage)
        self.tableCalculations.setObjectName("tableCalculations")
        self.tableCalculations.setHorizontalHeaderLabels(['Name', 'Value'])
        self.layoutCalculations.addWidget(self.tableCalculations)


        self.lowerHalf.addLayout(self.layoutCalculations)
        self.fullLayout.addLayout(self.lowerHalf)
        self.gridLayout.addWidget(self.fullPage, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        # menubar: Menubar at the top
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1384, 24))
        self.menubar.setObjectName("menubar")
        # menuFile: "File" tab of menubar
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        # menuExtra: "Extra" tab of menubar
        self.menuExtra = QtWidgets.QMenu(self.menubar)
        self.menuExtra.setObjectName("menuExtra")
        MainWindow.setMenuBar(self.menubar)
        # statusBar: Bar at the bottom of MainWindow
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        # actionNewProject: Action "New Project" in Tab "File"
        self.actionNewProject = QtWidgets.QAction(MainWindow)
        self.actionNewProject.setObjectName("actionNewProject")
        # actionOpenProject: Action "Open Project" in Tab "File"
        self.actionOpenProject = QtWidgets.QAction(MainWindow)
        self.actionOpenProject.setObjectName("actionOpenProject")
        # actionSaveProject: Action "Save Project" in Tab "File"
        self.actionSaveProject = QtWidgets.QAction(MainWindow)
        self.actionSaveProject.setObjectName("actionSaveProject")
        # actionSaveProjectAs: Action "Save Project as" in Tab "File"
        self.actionSaveProjectAs = QtWidgets.QAction(MainWindow)
        self.actionSaveProjectAs.setObjectName("actionSaveProjectAs")
        # actionImportData: Action "Import" in Tab "File"
        self.actionImportData = QtWidgets.QAction(MainWindow)
        self.actionImportData.setObjectName("actionImportData")
        # actionExportData: Action "Export" in Tab "File"
        self.actionExportData = QtWidgets.QAction(MainWindow)
        self.actionExportData.setObjectName("actionExportData")
        # actionSetSamplingrate: Action "Set Samplingrate" in Tab "Extra"
        self.actionExtraSetSamplingrate = QtWidgets.QAction(MainWindow)
        self.actionExtraSetSamplingrate.setObjectName("actionExtraSetSamplingrate")

        self.menuFile.addAction(self.actionNewProject)
        self.menuFile.addAction(self.actionOpenProject)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveProject)
        self.menuFile.addAction(self.actionSaveProjectAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportData)
        self.menuFile.addAction(self.actionExportData)
        self.menuExtra.addAction(self.actionExtraSetSamplingrate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExtra.menuAction())
        self.menubar.setNativeMenuBar(False)

        self.filename = ""

        self.retranslateUi(MainWindow)
        self.tabBar.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.graph.setBackground('w')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.removePeakButton.setText(_translate("MainWindow", "Remove"))
        self.labelDataEditing.setText(_translate("MainWindow", "Data Editing "))
        self.peakBox.setItemText(0, _translate("MainWindow", "R Peaks"))
        self.peakBox.setItemText(1, _translate("MainWindow", "S Peaks"))
        self.peakBox.setItemText(2, _translate("MainWindow", "T Peaks"))
        self.peakBox.setItemText(3, _translate("MainWindow", "Peak Onsets"))
        self.peakBox.setItemText(4, _translate("MainWindow", "Peak Amplitude"))
        self.peakBox.setItemText(5, _translate("MainWindow", "Half-Recovery Time"))

        self.applyPeakButton.setText(_translate("MainWindow", "Apply Peaks"))
        self.decomposeEdaButton.setText(_translate("MainWindow", "Decompose EDA"))
        self.addPeakButton.setText(_translate("MainWindow", "Add Peak"))
        self.addPeakInput.setPlaceholderText("time")

        #self.peakBoxEda.setItemText(0, _translate("MainWindow", "Peak Onsets"))
        #self.peakBoxEda.setItemText(1, _translate("MainWindow", "Peak Amplitude"))
        #self.peakBoxEda.setItemText(2, _translate("MainWindow", "Half-Recovery Time"))
        #self.applyEdaPeakButton.setText(_translate("MainWindow", "Apply EDA Peaks"))
        self.labelSelectData.setText(_translate("MainWindow", "Select Data"))
        self.labelMarker.setText(_translate("MainWindow", "Marker"))

        self.selectDataSaveButton.setText(_translate("MainWindow", "Save"))
        # add hide data button
        self.selectDataHideButton.setText(_translate("MainWindow", "Hide"))
        self.setMarkerButton.setText(_translate("MainWindow", "Set Marker"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))

        # setplaceholder for fromEditBox and toEditBox
        self.fromEditBox.setPlaceholderText("from")
        self.toEditBox.setPlaceholderText("to")
        self.markerTimeBox.setPlaceholderText("marker time")
        self.markerNameBox.setPlaceholderText("marker name")

        # checkBoxSelectData for selecting data
        self.checkBoxSelectData.setText(_translate("MainWindow", "Select Data"))

        self.tabBar.setTabText(self.tabBar.indexOf(self.tabDatasets), _translate("MainWindow", "Datasets"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.tabSelection), _translate("MainWindow", "Selection"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.tabFilter), _translate("MainWindow", "EDA"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.tabEvents), _translate("MainWindow", "Events"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.tabMarker), _translate("MainWindow", "Marker"))
        self.labelCalculations.setText(_translate("MainWindow", "Calculations"))
        self.labelMs01.setText(_translate("MainWindow", "ms"))
        self.labelMs02.setText(_translate("MainWindow", "ms"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExtra.setTitle(_translate("MainWindow", "Extra"))

        self.actionNewProject.setText(_translate("MainWindow", "New Project"))
        self.actionOpenProject.setText(_translate("MainWindow", "Open Project"))
        self.actionSaveProject.setText(_translate("MainWindow", "Save Project"))
        self.actionSaveProjectAs.setText(_translate("MainWindow", "Save Project as"))
        self.actionImportData.setText(_translate("MainWindow", "Import Data"))
        self.actionExportData.setText(_translate("MainWindow", "Export Data"))
        self.actionExtraSetSamplingrate.setText(_translate("MainWindow", "Set Samplingrate"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
