from select import select
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd 


class Database:

    def __init__(self):

        con = sqlite3.connect(":memory:")
        cur = con.cursor()

        #create timeline table
        cur.execute('''CREATE TABLE if not exists timeline ( 
            name
        )''')

        #create datastream table
        cur.execute('''CREATE TABLE if not exists datastream ( 
            name, 
            offset, 
            rawdata,
            datakey,
            type, 
            timelineId,
            visibility
        )''')

        #create marker table
        cur.execute('''CREATE TABLE if not exists marker ( 
            name,  
            time, 
            timelineId
        )''')

        # create selection table
        cur.execute('''CREATE TABLE if not exists selection ( 
            name, 
            starttime, 
            endtime,
            hidden,
            appliedOn, 
            timelineId
        )''')

        #create peak table
        cur.execute('''CREATE TABLE if not exists peak (  
            peaktype, 
            time, 
            movable,
            deletable,
            visible,
            datastreamId
        )''')

        #create filter table
        cur.execute('''CREATE TABLE if not exists filter ( 
            type, 
            parameter, 
            datastreamId, 
            starttime, 
            endtime, 
            hierarchy
        )''')

        #write connection and cursor for further use of database in self of object
        self.databasecon = con
        self.database = cur

        self.filename = ""
        self.activetimeleline = ""
        self.saved = True


    def saveDatabase(self, name):

        #create databasefile
        newdatabasecon = sqlite3.connect(name)

        #writes database into new file
        query = "".join(line for line in self.databasecon.iterdump()) 
        newdatabasecon.executescript(query)
    
    def openDatabase(self, name):

        #opens database file
        filedatabasecon = sqlite3.connect(name)

        #create database in memory
        newdatabasecon = sqlite3.connect(":memory:")

        #write data into memory database
        query = "".join(line for line in filedatabasecon.iterdump())
        # Dump old database in the new one. 
        newdatabasecon.executescript(query)        

        filedatabasecon.close()

        #write connection and cursor for further use of database in self of object
        self.databasecon = newdatabasecon
        self.database = newdatabasecon.cursor()

    def clearDatabase(self):

        #clear all timelines
        self.database.execute("DELETE FROM timeline")

        #clear all datastreams
        self.database.execute("DELETE FROM datastream")

        #clear all selection
        self.database.execute("DELETE FROM selection")
        
        #clear all peak
        self.database.execute("DELETE FROM peak")

        self.filename = ""
        self.activetimeleline = ""
        self.saved = True

        


    def createTimeline(self, name):

        self.database.execute("INSERT INTO timeline VALUES (:name)", {"name": name})

        return self.getTimeline(self.database.lastrowid)

    def getTimeline(self, timelineId):

        for timeline in self.database.execute("SELECT rowid, * FROM timeline WHERE rowid = :timelineId", {"timelineId": timelineId}):
            return {
                "id": timeline[0],
                "name": timeline[1]
                }    

    def getTimelineName(self, timelineId):

        return self.getTimeline(timelineId)["name"]

    def updateTimelineName(self, timelineId, newname):

        self.database.execute("UPDATE timeline SET name = :newname WHERE rowid = :timelineId", {"newname": newname, "timelineId": timelineId})

        return self.getTimeline(timelineId)
  
    def deleteTimeline(self, timelineId):

        self.database.execute("DELETE FROM timeline WHERE rowid = :timelineId", {"timelineId": timelineId})


    def createDatastream(self, name, offset, rawdata, datakey, type, timelineId, visibility):

        self.database.execute("INSERT INTO datastream VALUES (:name, :offset, :rawdata, :datakey, :type, :timelineId, :visibility)", {"name": name, "offset": offset, "rawdata": rawdata, "datakey": datakey, "type": type, "timelineId": timelineId, "visibility": visibility})

        return self.getDatastream(self.database.lastrowid)
        
    def getDatastream(self, datastreamId):

        for datastream in self.database.execute("SELECT rowid, * FROM datastream WHERE rowid = :datastreamId", {"datastreamId": datastreamId}):
            return {
                "id": datastream[0],
                "name": datastream[1],
                "offset": datastream[2],
                "rawdata": datastream[3],
                "datakey": datastream[4],
                "type": datastream[5],
                "timelineId": datastream[6],
                "visibility": datastream[7],
            }

    def getDatastreamOfType(self, datastreamType):

        for datastream in self.database.execute("SELECT rowid, * FROM datastream WHERE type = :datastreamType", {"datastreamType": datastreamType}):
            return {
                "id": datastream[0],
                "name": datastream[1],
                "offset": datastream[2],
                "rawdata": datastream[3],
                "datakey": datastream[4],
                "type": datastream[5],
                "timelineId": datastream[6],
                "visibility": datastream[7],
            }

    def getDatastreamName(self, datastreamId):

        return self.getDatastream(datastreamId)["name"]
    
    # Gibt die Id eines Datastreams aus.
    def getDatastreamId(self, datastreamName):

        for datastreamId in self.database.execute("SELECT rowid FROM datastream WHERE name = :datastreamName", {"datastreamName": datastreamName}):
            return(datastreamId[0])

    def getDatastreamRawdata(self, datastreamId):

        return self.getDatastream(datastreamId)["rawdata"]

    def getDatastreamType(self, datastreamId):

        return self.getDatastream(datastreamId)["type"]

    def getDatastreamTimelineId(self, datastreamId):

        return self.getDatastream(datastreamId)["timelineId"]
    
    def getDatastreamVisibility(self, datastreamId):

        return self.getDatastream(datastreamId)["visibility"]

    def updateDatastreamName(self, datastreamId, newname):

        self.database.execute("UPDATE datastream SET name = :newname WHERE rowid = :datastreamId", {"newname": newname, "datastreamId": datastreamId})

        return self.getDatastream(datastreamId)

    def updateDatastreamOffset(self, datastreamId, newoffset):

        self.database.execute("UPDATE datastream SET offset = :newoffset WHERE rowid = :datastreamId", {"newoffset": newoffset, "datastreamId": datastreamId})

        return self.getDatastream(datastreamId)

    def updateDatastreamTimelineId(self, datastreamId, newtimelineid):
        
        self.database.execute("UPDATE datastream SET timelineId = :newtimelineid WHERE rowid = :datastreamId", {"newtimelineid": newtimelineid, "datastreamId": datastreamId})

        return self.getDatastream(datastreamId)
    
    def updateDatastreamVisibility(self, datastreamId, newVisibility):
        
        self.database.execute("UPDATE datastream SET visibility = :newVisibility WHERE rowid = :datastreamId", {"newVisibility": newVisibility, "datastreamId": datastreamId})

        return self.getDatastream(datastreamId)

    def deleteDatastream(self, datastreamId):

        self.database.execute("DELETE FROM datastream WHERE rowid = :datastreamId", {"datastreamId": datastreamId})

    def getAllDatastreamsOf(self, timelineId):

        temp = []

        for datastream in self.database.execute("SELECT rowid, * FROM datastream WHERE timelineId = :timelineId", {"timelineId": timelineId}):
            temp.append({
                "id": datastream[0],
                "name": datastream[1],
                "offset": datastream[2],
                "rawdata": datastream[3],
                "datakey": datastream[4],
                "type": datastream[5],
                "timelineId": datastream[6],
                "visibility": datastream[7]
            })

        return(temp)


    def createSelection(self, name, starttime, endtime, hidden, appliedOn, timelineId):

        self.database.execute("INSERT INTO selection VALUES (:name, :starttime, :endtime, :hidden, :appliedOn, :timelineId)", {"name": name, "starttime": starttime, "endtime": endtime, "hidden": hidden, "appliedOn": appliedOn, "timelineId": timelineId})

        return self.getSelection(self.database.lastrowid)

    def getSelection(self, selectionId):

        for selection in self.database.execute("SELECT rowid, * FROM selection WHERE rowid = :selectionId", {"selectionId": selectionId}):
            return {
                "id": selection[0],
                "name": selection[1],
                "starttime": selection[2],
                "endtime": selection[3],
                "hidden": selection[4],
                "appliedOn": selection[5],
                "timelineId": selection[6],
            }

    def deleteSelection(self, selectionId):

        self.database.execute("DELETE FROM selection WHERE rowid = :selectionId", {"selectionId": selectionId})

    def getAllSelectionsOf(self, timelineId):

        temp = []

        for selection in self.database.execute("SELECT rowid, * FROM selection WHERE timelineId = :timelineId", {"timelineId": timelineId}):
            temp.append({
                "id": selection[0],
                "name": selection[1],
                "starttime": selection[2],
                "endtime": selection[3],
                "hidden": selection[4],
                "appliedOn": selection[5],
                "timelineId": selection[6],
            })

        return(temp)

    def updateSelectionHidden(self, selectionId, newhidden):

        self.database.execute("UPDATE selection SET hidden = :newhidden WHERE rowid = :selectionId", {"newhidden": newhidden, "selectionId": selectionId})

        return self.getSelection(selectionId)


    def createPeak(self, peaktype, time, movable, deletable, visible, datastreamId):

        self.database.execute("INSERT INTO peak VALUES (:peaktype, :time, :movable, :deletable, :visible, :datastreamId)", {"peaktype": peaktype, "time": time, "movable": movable, "deletable": deletable, "visible": visible, "datastreamId": datastreamId})

        return self.getPeak(self.database.lastrowid)

    def getPeak(self, peakId):

        for peak in self.database.execute("SELECT rowid, * FROM peak WHERE rowid = :peakId", {"peakId": peakId}):
            return {
                "id": peak[0],
                "peaktype": peak[1],
                "time": peak[2],
                "movable": peak[3],
                "deletable": peak[4],
                "visible": peak[5],
                "datastreamId": peak[6],
            }

    def getPeaksOfType(self, peaktype):

        temp = []

        for peak in self.database.execute("SELECT rowid, * FROM peak WHERE peaktype = :peaktype", {"peaktype": peaktype}):
            temp.append({
                "id": peak[0],
                "peaktype": peak[1],
                "time": peak[2],
                "movable": peak[3],
                "deletable": peak[4],
                "visible": peak[5],
                "datastreamId": peak[6],
            })
        
        return(temp)         

    def updatePeakTime(self, peakId, newtime):

        self.database.execute("UPDATE peak SET time = :newtime WHERE rowid = :peakId", {"newtime": newtime, "peakId": peakId})

        return self.getPeak(peakId)

    def updatePeaksMovableOfType(self, peaktype, newmovable):

        self.database.execute("UPDATE peak SET movable = :newmovable WHERE peaktype = :peaktype", {"newmovable": newmovable, "peaktye": peaktype})

        return self.getPeaksOfType(peaktype)

    def updatePeaksDeletableOfType(self, peaktype, newdeletable):

        self.database.execute("UPDATE peak SET deletable = :newdeletable WHERE peaktype = :peaktype", {"newdeletable": newdeletable, "peaktype": peaktype})

        return self.getPeaksOfType(peaktype)

    def updatePeaksVisibleOfType(self, peaktype, newvisible):

        self.database.execute("UPDATE peak SET visible = :newvisible WHERE peaktype = :peaktype", {"newvisible": newvisible, "peaktype": peaktype})

        return self.getPeaksOfType(peaktype)

    def deletePeak(self, peakId):

        self.database.execute("DELETE FROM peak WHERE rowid = :peakId", {"peakId": peakId})
    
    def deletePeaksOfType(self, peaktype):

        self.database.execute("DELETE FROM peak WHERE peaktype = :peaktype", {"peaktype": peaktype})

    def createMarker(self, name, time, timelineId):

        self.database.execute("INSERT INTO marker VALUES (:name, :time, :timelineId)", {"name": name, "time": time, "timelineId": timelineId})

        return self.getMarker(self.database.lastrowid)

    def getMarker(self, markerId):

        for marker in self.database.execute("SELECT rowid, * FROM marker WHERE rowid = :markerId", {"markerId": markerId}):
            return {
                "id": marker[0],
                "name": marker[1],
                "time": marker[2],
                "timelineId": marker[3],
            }

    def getMarkerByName(self, markerName):

        for marker in self.database.execute("SELECT rowid, * FROM marker WHERE name = :markerName", {"markerName": markerName}):
            return {
                "id": marker[0],
                "name": marker[1],
                "time": marker[2],
                "timelineId": marker[3],
            }

    def updateMarkerName(self, markerId, newname):

        self.database.execute("UPDATE marker SET name = :newname WHERE rowid = :markerId", {"newname": newname, "markerId": markerId})

        return self.getPeak(markerId)

    def updateMarkerTime(self, markerId, newtime):

        self.database.execute("UPDATE marker SET time = :newtime WHERE rowid = :markerId", {"newtime": newtime, "markerId": markerId})

        return self.getPeak(markerId)

    def getAllMarkerOf(self, timelineId):

        temp = []

        for marker in self.database.execute("SELECT rowid, * FROM marker WHERE timelineId = :timelineId", {"timelineId": timelineId}):
            temp.append({
                "id": marker[0],
                "name": marker[1],
                "time": marker[2],
                "timelineId": marker[3],
            })

        return(temp)


    def deleteMarker(self, markerId):

        self.database.execute("DELETE FROM marker WHERE rowid = :markerId", {"markerId": markerId})
    
    def deleteAllMarker(self):

        self.database.execute("DELETE FROM marker")
