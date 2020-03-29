'''
    Filename       : morsetrainer.py
    Last Modified  : 27/03/2020
    Purpose        : More code trainer application
    Written and designed by Danny Van Geyte
    Start of development : 27/03/2020
'''
import os
import subprocess
import sys
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import morse
from Settings import SettingsManager
from ui.main_form import Ui_MainWindow


class MorseTrainer(QMainWindow, Ui_MainWindow):
    """
        Purpose    : Represents the main window
        Parameters : QMainwindow, Entry point
        Returns    : None
    """

    def __init__(self):
        super(MorseTrainer, self).__init__()

        self.WPM = 0
        self.setupUi(self)
        self.loadsettings()

        # ---- Action events

        # ---- Button events
        self.btnSendMorse.pressed.connect(self.transmit_morse)
        self.wpmSlider.valueChanged.connect(self.changeWPM)

    # ------ Non event related methods
    def changeWPM(self):
        self.WPM = self.wpmSlider.value()

    def tone(self, cypher=None, speed=10):
        for cmorse in cypher:
            if cmorse == '.':
                subprocess.call(["mpg123", "-q", "di.mp3"])
            elif cmorse == '-':
                subprocess.call(["mpg123", "-q", "da.mp3"])
                pass
            elif cmorse == ' ':
                if self.actionPlay_space_holder.isChecked():
                    subprocess.call(["mpg123", "-q", "sps.mp3"])
            if self.actionLetter.isChecked():
                subprocess.call(["mpg123", "-q", "single.mp3"])

            sleep(speed / 50)

    def light_bulb(self, cypher, speed=10):
        # ------ Simmulate a light bulb morse code
        for dida in cypher:
            self.lblAlpha.setText(" ")
            self.lblAlpha.setStyleSheet("background-color: rgb(0, 0, 0);")
            QApplication.processEvents()
            sleep(0.05*10)
            if dida == '.':                
                self.lblAlpha.setText(".")
                self.lblAlpha.setStyleSheet("background-color: rgb(255, 255, 127);")
                QApplication.processEvents()
                sleep(0.05 * 5)
                #self.lblAlpha.setStyleSheet("background-color: rgb(255, 255, 127);")
            elif dida == '-':
                self.lblAlpha.setText("-")
                self.lblAlpha.setStyleSheet("background-color: rgb(255, 255, 127);")
                QApplication.processEvents()
                sleep(0.05 * 20)
                #self.lblAlpha.setStyleSheet("background-color: rgb(255, 255, 127);")
            

    # ------ Action event handlers

    # ------ Button event handlers
    def transmit_morse(self):
        if self.txtSource.toPlainText():
            message = self.txtSource.toPlainText()
            morse_code = ""
            for letter in message:
                # self.lblAlpha.setText(letter)
                cypher = morse.encrypt(letter.upper())
                morse_code += cypher
                self.txtCypher.setText(morse_code)
                # self.lblMorse.setText(cypher)
                QApplication.processEvents()
                sleep(self.WPM / 50)
                if self.actionLightbulb_simmulator.isChecked():
                    self.light_bulb(cypher, self.WPM)
                else:
                    self.lblAlpha.setText(letter)
                    self.lblMorse.setText(cypher)
                    if self.actionLearn.isChecked():
                        self.tone(cypher=cypher.strip(), speed=self.WPM)
                        subprocess.call(["mpg123", "-q", "nos.mp3"])
                    if letter == ' ':
                        # ------ Do we need to play a space sound
                        if self.actionPlay_space_holder.isChecked():
                            subprocess.call(["mpg123", "-q", "sps.mp3"])

    # ----- Standard system events
    def closeEvent(self, event):
        """
            Purpose    : Overides the close event
            Parameters : self, event
            Returns    : None
        """
        self.saveSettings()

    def saveSettings(self):
        """
            Purpose    : Save the apps settings
            Parameters : self
            Returns    : None
        """
        this_settings = {
            "position": self.pos(),
            "size": self.size(),
        }
        mysettings = SettingsManager()
        mysettings.saveSettings(this_settings, 'denkatech', 'morse')

    def loadsettings(self):
        """
            Purpose    : Load the settings for the app
            Parameters : self
            Returns    : None
        """
        this_settings = {
            "position": 0,
            "size": 0,
        }
        setting = SettingsManager()
        this_settings_getter = setting.load_settings(
            this_settings, 'denkatech', 'morse')
        # Restore the size of our form
        try:
            self.move(this_settings_getter["position"])
            self.resize(this_settings_getter["size"])
        except Exception as e:
            print(e)


# ----- Entry point
if __name__ == "__main__":
    """
        Purpose    : Initialize the application
        Parameters : None
        Returns    : None
    """
    import sys
    import os

    app = QApplication(sys.argv)
    # # time.sleep(1)
    main_form = MorseTrainer()
    # # time.sleep(5)
    main_form.show()
    sys.exit(app.exec_())
