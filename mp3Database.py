#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GRCI
#
# Created:     10/12/2015
# Copyright:   (c) GRCI 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
from tinytag import *
from random import *

def timeConv(time):
    """Converts seconds into minutes. Example: 198 seconds converts into 3:18"""
    if len(time) >= 6:
        time = time / 1000
    remainder = time%60
    minutes = str(int((time-remainder) / 60))
    if len(str(remainder)) == 1:
        seconds = "0"+str(int(remainder))
    else:
        seconds = str(int(remainder))
    return minutes+":"+seconds

def getID3Genre(genre):
        """Returns genre retrieved from tinytag eliminating any errors that can occur"""
        #Necessary because of an error in tinytag that would result in having the location of the
        #genre in this list instead of the genre itself
        ID3V1_GENRES = [
            #list of genres from tinytag
            'Blues', 'Classic Rock', 'Country', 'Dance', 'Disco',
            'Funk', 'Grunge', 'Hip-Hop', 'Jazz', 'Metal', 'New Age', 'Oldies',
            'Other', 'Pop', 'R&B', 'Rap', 'Reggae', 'Rock', 'Techno', 'Industrial',
            'Alternative', 'Ska', 'Death Metal', 'Pranks', 'Soundtrack',
            'Euro-Techno', 'Ambient', 'Trip-Hop', 'Vocal', 'Jazz+Funk', 'Fusion',
            'Trance', 'Classical', 'Instrumental', 'Acid', 'House', 'Game',
            'Sound Clip', 'Gospel', 'Noise', 'AlternRock', 'Bass', 'Soul', 'Punk',
            'Space', 'Meditative', 'Instrumental Pop', 'Instrumental Rock',
            'Ethnic', 'Gothic','Darkwave', 'Techno-Industrial', 'Electronic',
            'Pop-Folk', 'Eurodance', 'Dream', 'Southern Rock', 'Comedy', 'Cult',
            'Gangsta', 'Top 40', 'Christian Rap', 'Pop/Funk', 'Jungle',
            'Native American', 'Cabaret', 'New Wave', 'Psychadelic', 'Rave',
            'Showtunes', 'Trailer', 'Lo-Fi', 'Tribal', 'Acid Punk', 'Acid Jazz',
            'Polka', 'Retro', 'Musical', 'Rock & Roll', 'Hard Rock',
            # Wimamp Extended Genres
             'Folk', 'Folk-Rock', 'National Folk', 'Swing', 'Fast Fusion', 'Bebob',
            'Latin', 'Revival', 'Celtic', 'Bluegrass', 'Avantgarde', 'Gothic Rock',
            'Progressive Rock', 'Psychedelic Rock', 'Symphonic Rock', 'Slow Rock',
            'Big Band', 'Chorus', 'Easy Listening', 'Acoustic', 'Humour', 'Speech',
            'Chanson', 'Opera', 'Chamber Music', 'Sonata', 'Symphony', 'Booty Bass',
            'Primus', 'Porn Groove', 'Satire', 'Slow Jam', 'Club', 'Tango', 'Samba',
            'Folklore', 'Ballad', 'Power Ballad', 'Rhythmic Soul', 'Freestyle',
            'Duet', 'Punk Rock', 'Drum Solo', 'A capella', 'Euro-House', 'Dance Hall',
            'Goa', 'Drum & Bass',
            # according to https://de.wikipedia.org/wiki/Liste_der_ID3v1-Genres:
            'Club-House', 'Hardcore Techno', 'Terror', 'Indie', 'BritPop',
            '', 'Polsk Punk', 'Beat', 'Christian Gangsta Rap',
            'Heavy Metal', 'Black Metal', 'Contemporary Christian', 'Christian Rock',
            # WinAmp 1.91
            'Merengue', 'Salsa', 'Thrash Metal', 'Anime', 'Jpop', 'Synthpop',
            # WinAmp 5.6
            'Abstract', 'Art Rock', 'Baroque', 'Bhangra', 'Big Beat', 'Breakbeat',
            'Chillout', 'Downtempo', 'Dub', 'EBM', 'Eclectic', 'Electro',
            'Electroclash', 'Emo', 'Experimental', 'Garage', 'Illbient',
            'Industro-Goth', 'Jam Band', 'Krautrock', 'Leftfield', 'Lounge',
            'Math Rock', 'New Romantic', 'Nu-Breakz', 'Post-Punk', 'Post-Rock',
            'Psytrance', 'Shoegaze', 'Space Rock', 'Trop Rock', 'World Music',
            'Neoclassical', 'Audiobook', 'Audio Theatre', 'Neue Deutsche Welle',
            'Podcast', 'Indie Rock', 'G-Funk', 'Dubstep', 'Garage Rock', 'Psybient',
        ]
        try:
            GENRE = ID3V1_GENRES[int(genre[1:-1])]
    #attempts to convert the contents of tag.genre excluding the first and last character into an int and
    #then return that str at that index in the list
        except ValueError:
            GENRE = genre
    #if that fails, returns tag.genre
        except TypeError:
            GENRE = "None"
    #if both fail, genre will be unknown
        return GENRE

class track:
#contains almost all metadata NUM,ARTIST,ALBUM,YEAR,TITLE,TRACKNUM,DURATION,GENRE,FAVSTATUS,DIRECTORY
    def __init__(self,dic):
        self.num = dic["NUM"]
        self.artistName = dic["ARTIST"]
        self.albumName = dic["ALBUM"]
        self.year = dic["YEAR"]
        self.trackTitle = dic["TITLE"]
        self.trackNum = dic["TRACK"]
        self.trackLen = dic["DURATION"]
        self.genre = dic["GENRE"]
        self.fileName = dic["DIRECTORY"]
        self.favStatus = dic["FAVSTATUS"]
        self.collection = dic

    def __str__(self):
        return "Class instance of track named "+self.trackTitle

    def getArtist(self):
        return self.artistName

    def getAlbum(self):
        return self.albumName

    def getYear(self):
        return self.year

    def getTitle(self):
        return self.trackTitle

    def getNum(self):
        return self.trackNum

    def getLen(self):
        return self.trackLen

    def getGenre(self):
        return self.genre

    def getDirectory(self):
        return self.fileName

    def getDic(self):
        return self.collection

    def getLoc(self):
        return self.num

    def favourite(self):
        self.favStatus = True

    def unfavourite(self):
        self.favStatus = False

    def getfavStatus(self):
        return self.favStatus

class mp3Database:
    def __init__(self,fileName,mp3Folder):
        self.objects = []
        self.fileName = fileName
        self.mp3Folder = mp3Folder

    def __str__(self):
        return "mp3Database of "+self.mp3Folder

    def getObjects(self):
        return self.objects

    def getfileName(self):
        return self.fileName

    def setfileName(self, newfileName):
        self.fileName = newfileName

    def clearObjects(self):
        self.objects = []

    def clearDatabase(self):
        """Erases contents of fileName"""
        with open(self.fileName,"w") as file:
            pass
        file.closed

    def createDatabase(self):
        """Rewrites entire song database, eliminating any prior metadata changes
        Tags organized by NUM,ARTIST,ALBUM,YEAR,TITLE,TRACKNUM,DURATION,GENRE,FAVSTATUS,DIRECTORY"""
        num = 0
        try:
            for folder in os.listdir(os.path.abspath(self.mp3Folder)):
            #os.path.abspath will list the absolute path of Montunes Music no matter what computer the program is excecuted on
            #os.listdir will list all files within Montunes Music
                if folder.endswith(".mp3"):
                    fileName = os.path.abspath(self.mp3Folder)+"\\"+folder
                    tag = TinyTag.get(fileName)
                    DURATION = int(tag.duration) * 1000
        #converts track duration into milliseconds for later use in VLC
                    GENRE = getID3Genre(tag.genre)
                    with open(self.fileName,"a") as outFile:
                        line = ("{0}{10}{1}{10}{2}{10}{3}{10}{4}{10}{5}{10}{6:0.0f}{10}{7}{10}{8}{10}{9}\n".format(str(num),tag.artist,
                        tag.album,tag.year,tag.title,tag.track,DURATION,GENRE,False,fileName,chr(165)
                        ))
                        outFile.write(line)
                    outFile.closed
                else:
                    for file in os.listdir(os.path.abspath(self.mp3Folder)+"\\"+folder):
                        if file.endswith(".mp3"):
                            fileName = os.path.abspath(self.mp3Folder)+"\\"+folder+"\\"+file
                            tag = TinyTag.get(fileName)
                            DURATION = int(tag.duration * 1000)
                #converts track duration into milliseconds for later use in VLC
                            GENRE = getID3Genre(tag.genre)
                            with open(self.fileName,"a") as outFile:
                                line = ("{0}{10}{1}{10}{2}{10}{3}{10}{4}{10}{5}{10}{6:0.0f}{10}{7}{10}{8}{10}{9}\n".format(str(num),tag.artist,
                                tag.album,tag.year,tag.title,tag.track,DURATION,GENRE,False,fileName,chr(165)
                                ))
                                outFile.write(line)
                            outFile.closed
                        num+=1
        except Exception:
            pass

    def byDatabase(self):
        """Creates objects from text file database"""
        with open(self.fileName,"r") as file:
            for line in file:
                NUM,ARTIST,ALBUM,YEAR,TITLE,TRACK,DURATION,GENRE,FAVSTATUS,DIRECTORY = line.split(chr(165))
                dic = {"NUM":NUM,"ARTIST":ARTIST,"ALBUM":ALBUM,"YEAR":YEAR,"TITLE":TITLE,"TRACK":TRACK,"DURATION":DURATION,"GENRE":GENRE,
                "FAVSTATUS":FAVSTATUS,"DIRECTORY":DIRECTORY[0:-1]}
                self.objects.append(track(dic))
        file.closed

    def byFolder(self):
        """Will create objects out of all music folders in Montunes Music"""
        try:
            count=0
            for folder in os.listdir(os.path.abspath(self.mp3Folder)):
            #os.path.abspath will list the absolute path of Montunes Music no matter what computer the program is excecuted on
            #os.listdir will list all files within Montunes Music
                if folder.endswith(".mp3"):
                    fileName = os.path.abspath(self.mp3Folder)+"\\"+folder
                    tag = TinyTag.get(fileName)
                    DURATION = int(tag.duration * 1000)
                    GENRE = getID3Genre(tag.genre)
                    dic = {"NUM":count,"ARTIST":tag.artist,"ALBUM":tag.album,"YEAR":tag.year,"TITLE":tag.title,"TRACK":tag.track
                    ,"DURATION":DURATION,"GENRE":GENRE,"FAVSTATUS":False,"DIRECTORY":fileName}
                    count+=1
                    self.objects.append(track(dic))
                else:
                    for file in os.listdir(os.path.abspath(self.mp3Folder)+"\\"+folder):
                        if file.endswith(".mp3"):
                            fileName = os.path.abspath(self.mp3Folder)+"\\"+folder+"\\"+file
                            tag = TinyTag.get(fileName)
                            DURATION = int(tag.duration * 1000)
                #converts track duration into milliseconds for later use in VLC
                            GENRE = getID3Genre(tag.genre)
                            dic = {"NUM":count,"ARTIST":tag.artist,"ALBUM":tag.album,"YEAR":tag.year,"TITLE":tag.title,"TRACK":tag.track,
                            "DURATION":str(DURATION),"GENRE":GENRE,"FAVSTATUS":False,"DIRECTORY":fileName}
                            count+=1
                            self.objects.append(track(dic))
        except Exception:
            pass

    def searchDBase(self,userInput):
        """Searches textfile database for a user inputted keyword. The location of any line that containts
        the keyword will be added to a list"""
        lineNum = []
        count = 0
        with open(self.fileName,"r") as file:
            for line in file:
                NUM,ARTIST,ALBUM,YEAR,TITLE,TRACK,DURATION,GENRE,FAVSTATUS,DIRECTORY = line.split(chr(165))
                dataCollection = [NUM,ARTIST,ALBUM,YEAR,TITLE,TRACK,DURATION,GENRE,FAVSTATUS,DIRECTORY]
                for item in dataCollection:
                    for ch in item:
                #loops through every item in the list and then loops through every character in the item
                        if count == len(userInput):
                        #count is the amount of like characters that the input and the item has
                            lineNum.append(NUM)
                            count = 0
                            break
                        #if the amount of like characters is the same as the length of the user input, appends
                        #the line number that contained the like data to a list. Then breaks one loop and moves on to the next
                        else:
                            if userInput[count].lower() == ch.lower():
                                count+=1
                                continue
                            #checks to see if the character in the user input is the same as the character the loop is currently on
                            else:
                                break
                        break
        file.closed
        return lineNum

    def searchObjects(self,userInput):
        """Searches objects in database for a user inputted keyword. Any object that contains the keyword is
        added to a list"""
        objects = []
        count = 0
        for item in self.objects:
            for heading in item.getDic():
                for ch in item.getDic()[heading]:
                #loops through all objects, all keys in the object, and all characters in the value of the key
                    if count == len(userInput):
                    #count is the amount of like characters that the input and the item has
                        objects.append(item)
                        count = 0
                        break
                    #if the amount of like characters is the same as the length of the user input, appends
                    #the line number that contained the like data to a list. Then breaks one loop and moves on to the next
                    else:
                        if userInput[count].lower() == ch.lower():
                            count+=1
                            continue
                        #checks to see if the character in the user input is the same as the character the loop is currently on
                        else:
                            break
                    break
        return objects

    def retrieveLines(self,lineNum):
        """Accesses the line numbers specified by a list of line numbers and appends the lines to a list
        and returns it"""
        lines = []
        with open(self.fileName,"r") as file:
            for line in file:
                NUM,ARTIST,ALBUM,YEAR,TITLE,TRACK,DURATION,GENRE,FAVSTATUS,DIRECTORY = line.split(chr(165))
                if NUM in lineNum:
                    lines.append(line)
                #goes through and checks if the line number is equal to whatever numbers are in the list of line numbers

        file.closed
        return lines

class playlist:
    def __init__(self,fileName):
        self.fileName = os.path.abspath("Montunes Playlists")+"\\"+fileName+".txt"
        open(os.path.abspath("Montunes Playlists")+"\\"+fileName+".txt","w")
        self.songs = []
        self.sortAttributes = []

    def addSong(self,song):
    #adds a song to the playlist object and the playlist txt file
        self.songs.append(song)
        with open(self.fileName,"a") as outFile:
            line = ("{0}{10}{1}{10}{2}{10}{3}{10}{4}{10}{5}{10}{6}{10}{7}{10}{8}{10}{9}\n".format(song.getLoc(),song.getArtist(),
            song.getAlbum(),song.getYear(),song.getTitle(),song.getNum(),song.getLen(),song.getGenre(),False,
            song.getDirectory(),chr(165)
            ))
            outFile.write(line)
        outFile.closed

    def delSong(self,pos):
    #removes a song from the playlist object and the playlist txt file
        self.songs.pop(pos)
        self.sortAttributes.pop(pos)
        for item in self.songs:
            with open(self.fileName,"a") as file:
                line = ("{0}{10}{1}{10}{2}{10}{3}{10}{4}{10}{5}{10}{6}{10}{7}{10}{8}{10}{9}\n".format(item.getLoc(),item.getArtist(),
                item.getAlbum(),item.getYear(),item.getTitle(),item.getNum(),item.getLen(),item.getGenre(),False,
                item.getDirectory(),chr(165)
                ))
                file.write(line)
            file.closed


    def clearPlaylist(self):
        self.songs = []
        with open(self.fileName,"w") as file:
            pass
        file.closed

    def getSongs(self):
        return self.songs

    def sortSongs(self):
        for num in range(len(self.sortAttributes)-1,0,-1):
    #loops over one under the length of the list of attributes to be sorted from zero to one before the end of the list
            for i in range(num):
    #will loop as many times as the current position in the list of attributes
                if self.sortAttributes[i].lower()>self.sortAttributes[i+1].lower():
    #checks to see if the current item is greater than the next one
    #greater can mean larger value or later in the alphabet
                    temp1 = self.sortAttributes[i]
    #sets a temporary value of the larger item
                    self.sortAttributes[i] = self.sortAttributes[i+1]
    #moves the smaller attribute to the index of the larger attribute
                    self.sortAttributes[i+1] = temp1
    #sets the index of the old smaller value to the larger value temp
                    temp2 = self.songs[i]
                    self.songs[i] = self.songs[i+1]
                    self.songs[i+1] = temp2

    def reverseSort(attributes,objects):
    #same as regular sort function, just backwards
        for num in range(len(attributes)-1,0,-1):
            for i in range(num):
                if attributes[i+1].lower()>attributes[i].lower():
                    temp1 = attributes[i+1]
                    attributes[i+1] = attributes[i]
                    attributes[i] = temp1
                    temp2 = objects[i+1]
                    objects[i+1] = objects[i]
                    objects[i] = temp2

    def genreAttributes(self):
    #puts all genres into a list for sorting
        self.sortAttributes[:] = []
        for item in self.songs:
            self.sortAttributes.append(item.getGenre())

    def artistAttributes(self):
    #puts all artists into a list for sorting
        self.sortAttributes[:] = []
        for item in self.songs:
            self.sortAttributes.append(item.getArtist())

    def albumAttributes(self):
    #puts all albums into a list for sorting
        self.sortAttributes[:] = []
        for item in self.songs:
            self.sortAttributes.append(item.getAlbum())

    def titleAttributes(self):
    #puts all titles into a list for sorting
        self.sortAttributes[:] = []
        for item in self.songs:
            self.sortAttributes.append(item.getTitle())

    def shuffle(self):
    #shuffles list of songs
        for item in self.songs:
            random = randint(0,len(self.songs)-1)
            index = self.songs.index(item)
            self.songs.insert(random,self.songs.pop(index))
            self.sortAttributes.insert(random,self.sortAttributes(index))

    def delPlaylist(self):
    #deletes a playlist
        os.remove(self.fileName)
        self.songs = []
        self.sortAttributes = []