#!/usr/bin/python

import os, sys, ConfigParser


class PiStation:
    frequency = "89.9"
    file_list = []

    def __init__(self):
        os.system('clear')
        print "Welcome to PiStation!"
        print "Version 1.0"
        print "GPLv3 License"

        self.find_files()
        self.get_config()
        print "Broadcasting on frequency " , self.frequency 
    
    def get_config(self):
        config = ConfigParser.ConfigParser()
        config.read('pistation.conf')
        try:
            self.frequency = config.get('pistation', 'frequency')
        except expression as identifier:
            print "Error while reading frequency in pistation.conf"
        

    def play(self):
        for song_file in self.file_list:
            self.playSong(song_file)
    
    def find_files(self):
        
        for root, folders, files in os.walk('/media/pi/'):
            folders.sort()
            files.sort()
            for filename in files:
                if re.search(".(aac|mp3|wav|flac|m4a|ogg|pls|m3u)$", filename) != None: 
                    self.file_list.append(os.path.join(root, filename))

    def playSong(self, song_file):
        try:
            if ".mp3" in song_file.lower():
                cmd = "ffmpeg -i %s -f s16le -ar 22.05k -ac 1 - | sudo ./fm_transmitter -f %s - "%(song_file, self.frequency)
                os.system(cmd)
            elif ".wav" in song_file.lower():
                cmd = "sudo ./fm_transmitter -f %s %s "%(self.frequency, song_file)
                os.system(cmd)
            else:
                print "That file extension is not supported."
                print "File name provided: %s" % song_file
                raise IOError
        except IOError:
            print "There was an error regarding file selection. Halting."
            exit()
        except Exception:
            print "Something went wrong. Halting."
            exit()



if __name__ == '__main__':
    try:
        pi = PiStation()
        pi.play()
    except KeyboardInterrupt:
        print "Exit"
        sys.exit(0)