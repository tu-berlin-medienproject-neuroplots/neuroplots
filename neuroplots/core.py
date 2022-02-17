from pickle import TRUE
from PyQt5 import QtCore, QtGui, QtWidgets

import database.database as database_module
import ui.ui as ui_module
import plot.plot as plot_module
import plot.datastream as datastream_module
import plot.select as select_module
import plot.events as event_module
import plot.marker as marker_module

import sys
import os

def newproject(ui: ui_module.Ui_MainWindow, MainWindow: QtWidgets.QMainWindow, database: database_module.Database, select: select_module.Select, events: event_module.Events, marker: marker_module.Marker):
    

    if(database.saved):

        #todo: clear memory database

        database.clearDatabase()

        #plots
        plot_module.clearPlot(ui)

        #datastreams
        datastream_module.updateDatastreamUi(ui, database)

        #selections
        select.updateSelectionUi(ui, database)

        events.loadPeaksFromDatabase(events.rpeaks_array, "R_Peak", ui, database, "b")
        events.loadPeaksFromDatabase(events.speaks_array, "S_Peak", ui, database, "y")
        events.loadPeaksFromDatabase(events.tpeaks_array, "T_Peak", ui, database, "g")
        events.loadPeaksFromDatabase(events.onsets_array, "Peak_Onsets", ui, database, "b")
        events.loadPeaksFromDatabase(events.peak_array, "Peak_Amplitude", ui, database, "y")
        events.loadPeaksFromDatabase(events.recovery_array, "Half_Recovery_Time", ui, database, "g")
        
        events.updateEventsUi(ui)

        marker.loadMarkerFromDatabase(ui, database)
        marker.updateMarkerUi(ui, database)

    else:

        #todo: ask if current project should be saved/disgarded/action canceled
        print("todo")

def openproject(ui: ui_module.Ui_MainWindow, MainWindow: QtWidgets.QMainWindow, database: database_module.Database, select: select_module.Select, events: event_module.Events, marker: marker_module.Marker):

    if(database.saved):

        #get url of project
        filename = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Open project", filter="db(*.db)")[0]

        if(filename != ""):

            #open project database
            print("Opening project " + filename)
            database.openDatabase(filename)

            #write curent filename in Database object of opened program
            database.filename = filename

            plot_module.plotData(ui, database)
            datastream_module.updateDatastreamUi(ui, database)

            #selections
            select.updateSelectionUi(ui, database)

            #peaks
            events.loadPeaksFromDatabase(events.rpeaks_array, "R_Peak", ui, database, "b")
            events.loadPeaksFromDatabase(events.speaks_array, "S_Peak", ui, database, "y")
            events.loadPeaksFromDatabase(events.tpeaks_array, "T_Peak", ui, database, "g")
            events.loadPeaksFromDatabase(events.onsets_array, "Peak_Onsets", ui, database, "b")
            events.loadPeaksFromDatabase(events.peak_array, "Peak_Amplitude", ui, database, "y")
            events.loadPeaksFromDatabase(events.recovery_array, "Half_Recovery_Time", ui, database, "g")
            events.updateEventsUi(ui)

            #marker
            marker.loadMarkerFromDatabase(ui, database)
            marker.updateMarkerUi(ui, database)

    else:

        #todo: ask if current project should be saved/disgarded/action canceled
        print("todo")

def saveproject(MainWindow: QtWidgets.QMainWindow, database: database_module.Database):

    if(database.saved):

        print("Database already saved!")

    else:

        if(database.filename == ""):

            saveprojectas(MainWindow, database)

        else:

            print("Saving project in " + database.filename)
            database.saveDatabase(database.filename)

def saveprojectas(MainWindow: QtWidgets.QMainWindow, ui: ui_module.Ui_MainWindow, database: database_module.Database, marker: marker_module.Marker, events: event_module.Events):

    print("function: saveprojectas")

    #get url and name for new project save
    filename = QtWidgets.QFileDialog.getSaveFileName(filter="db(*.db)")[0]

    if(filename != ""):

        #updateMarkerinDatabase
        marker.updateMarkerinDatabase(ui, database)

        #updatePeaksinDatabase
        events.updatePeaktsinDatabase(events.rpeaks_array, database)
        events.updatePeaktsinDatabase(events.speaks_array, database)
        events.updatePeaktsinDatabase(events.tpeaks_array, database)
        events.updatePeaktsinDatabase(events.onsets_array, database)
        events.updatePeaktsinDatabase(events.peak_array, database)
        events.updatePeaktsinDatabase(events.recovery_array, database)


        #save project database
        database.saveDatabase(filename)

        #set filename in Database object of opened program to new project save
        database.filename = filename

def importdata(ui: ui_module.Ui_MainWindow, MainWindow: QtWidgets.QMainWindow,  database: database_module.Database):

    print("function: importdata")

    #get url of data
    filename = QtWidgets.QFileDialog.getOpenFileUrl(MainWindow, "Import Data", filter="csv(*.csv)")[0]

    if (filename != ""):

        datastream_module.importdata(filename, database)
        datastream_module.updateDatastreamUi(ui, database)    

        plot_module.plotData(ui, database)
