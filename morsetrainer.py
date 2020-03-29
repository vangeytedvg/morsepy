"""
   Filename : morsetrainer.py
   Purpose  : 
   Created  : 27/03/2020
   Written and designed by Danny Van Geyte
   Modification history: 
          LM   : 29/03/2020 (Added lightbulb simulator)
"""
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
        # ------ Default to morse sounds
        self.dotSound = "sounds/dot.mp3"
        self.dashSound = "sounds/dash.mp3"

        # ------ QT Desginer does not allow to add
        # ------ controls with the same name, this hack does the job.
        self.addRadioButtons()

        # ---- Action events
        self.actionLightbulb_simmulator.triggered.connect(
            self.lightbulb_clicked)

        # ---- Button or control events
        self.btnSendMorse.pressed.connect(self.transmit_morse)
        self.wpmSlider.valueChanged.connect(self.changeWPM)
        self.actionLightbulb_simmulator.triggered.connect(
            self.lightbulb_clicked)
            
    # ------ Non event related methods

    def addRadioButtons(self):
        """
            Purpose    : Add radio buttons to the groupbox
            Parameters : None 
            Returns    : None
        """
        # ------ Real morse sounds button
        rbSoundType = QRadioButton("Real morse sounds")
        rbSoundType.setChecked(True)
        rbSoundType.tag = "morse"
        rbSoundType.toggled.connect(self.rbSoundType_onClicked)
        self.horizontalLayout.addWidget(rbSoundType)
        # ------ Dit Dah Button
        rbSoundType = QRadioButton("Dit Dah sounds")
        rbSoundType.tag = "didah"
        rbSoundType.toggled.connect(self.rbSoundType_onClicked)
        self.horizontalLayout.addWidget(rbSoundType)


    def changeWPM(self):
        """
            Purpose    : Set speed
            Parameters : None
            Returns    : None
        """
        self.WPM = self.wpmSlider.value()


    def tone(self, cypher=None, speed=10):
        """
            Purpose    : Generate the morse code sound
            Parameters : Morse code, transmit speed
            Returns    : None
        """
        for cmorse in cypher:
            if cmorse == '.':
                subprocess.call(["mpg123", "-q", self.dotSound])
            elif cmorse == '-':
                subprocess.call(["mpg123", "-q", self.dashSound])
            elif cmorse == ' ':
                if self.actionPlay_space_holder.isChecked():
                    subprocess.call(["mpg123", "-q", "sps.mp3"])
            if self.actionLetter.isChecked():
                subprocess.call(["mpg123", "-q", "single.mp3"])
            # ------ Wait
            sleep(speed / 50)


    def light_bulb(self, cypher, speed=10):
        """
            Purpose    : Simulate a light been flased according to morse code
            Parameters : cypher, the morse code,
                         speed, lightsignal duration
            Returns    : None
        """
        for dida in cypher:
            self.lblAlpha.setText(" ")
            self.lblAlpha.setStyleSheet("background-color: rgb(0, 0, 0);")
            QApplication.processEvents()
            sleep(0.05*10)
            if dida == '.':
                self.lblAlpha.setText(".")
                self.lblAlpha.setStyleSheet(
                    "background-color: rgb(255, 255, 127);")
                QApplication.processEvents()
                sleep(0.05 * (speed + 5))
                #self.lblAlpha.setStyleSheet("background-color: rgb(255, 255, 127);")
            elif dida == '-':
                self.lblAlpha.setText("-")
                self.lblAlpha.setStyleSheet(
                    "background-color: rgb(255, 255, 127);")
                QApplication.processEvents()
                sleep(0.05 * (speed + 20))
                #self.lblAlpha.setStyleSheet("background-color: rgb(255, 255, 127);")

    # ------ Action event handlers

    # ------ Button event handlers
    def rbSoundType_onClicked(self):
        rb = self.sender()
        if rb.isChecked():
            if rb.tag == "morse":
                self.dotSound = "sounds/dot.mp3"
                self.dashSound = "sounds/dash.mp3"
            elif rb.tag == "didah":
                self.dotSound = "sounds/di.mp3"
                self.dashSound = "sounds/da.mp3"
            print(self.dotSound, self.dashSound)


    def transmit_morse(self):
        """
            Purpose    : Generate morse code
            Parameters : None
            Returns    : None
        """
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


    def lightbulb_clicked(self):
        """
            Purpose    : Deactivate or Activate controls based on selection
            Parameters : None
            Returns    : None
        """
        if self.actionLightbulb_simmulator.isChecked():
            self.lblMorse.setText(" ")
            self.lblAlpha.setStyleSheet("background-color: rgb(0, 0, 0);")
            # ------ Make the flashlight bigger
            self.lblAlpha.setFixedSize(QSize(200, 200))
            self.actionLearn.setChecked(False)
            self.actionLearn.setEnabled(False)
            self.actionLetter.setChecked(False)
            self.actionLetter.setEnabled(False)
            self.actionPlay_space_holder.setChecked(False)
            self.actionPlay_space_holder.setEnabled(False)
            self.wpmSlider.setEnabled(False)
        else:
            self.lblAlpha.setStyleSheet("")
            self.lblAlpha.setFixedSize(QSize(100, 100))
            self.wpmSlider.setEnabled(True)
            self.actionPlay_space_holder.setEnabled(True)
            self.actionLetter.setEnabled(True)
            self.actionLearn.setEnabled(True)


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
    app = QApplication(sys.argv)
    # # time.sleep(1)
    main_form = MorseTrainer()
    # # time.sleep(5)
    main_form.show()
    sys.exit(app.exec_())
