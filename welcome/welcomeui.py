#
#
#  Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
                             QLabel, QSpacerItem, QSizePolicy, QCheckBox,
                             QDesktopWidget)
from PyQt5.QtGui import QIcon, QDesktopServices, QPixmap
from PyQt5.QtCore import Qt, QSysInfo, QSize, QUrl, QProcess
import os
import shutil


class WelcomeUi(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle(self.tr("Welcome Pisi GNU/Linux"))
        self.setFixedSize(700, 475)
        self.setWindowIcon(QIcon(":/images/pisilinux-welcome.svg"))
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("QPushButton {border: none; text-align: left; color: black;} QLabel {color:black;}")

        x = (QDesktopWidget().width() - self.width()) // 2
        y = (QDesktopWidget().height() - self.height()) // 2
        self.move(x, y)

        # The header code:

        self.headerWidget = QWidget()
        self.headerWidget.setFixedHeight(80)
        self.headerWidget.setLayout(QHBoxLayout())
        self.headerWidget.setStyleSheet("background-image: url(:/images/background.png);")
        self.layout().addWidget(self.headerWidget)

        self.logoLabel = QLabel()
        self.logoLabel.setFixedSize(64, 64)
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setPixmap(QIcon(":/images/pisi-white.svg").pixmap(self.logoLabel.size()))
        self.headerWidget.layout().addWidget(self.logoLabel)

        self.pisiLogoLabel = QLabel()
        self.pisiLogoLabel.setFixedSize(157, 48)
        self.pisiLogoLabel.setScaledContents(True)
        self.pisiLogoLabel.setPixmap(QPixmap(":/images/pisi.png"))
        self.headerWidget.layout().addWidget(self.pisiLogoLabel)

        self.headerWidget.layout().addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.versionLabel = QLabel()
        font = self.versionLabel.font()
        font.setPointSize(12)
        self.versionLabel.setFont(font)
        self.versionLabel.setText("{} - {}".format(QSysInfo.productVersion(), QSysInfo.currentCpuArchitecture()))
        self.versionLabel.setStyleSheet("color: white; font-weight: bold;")
        self.headerWidget.layout().addWidget(self.versionLabel)

        # The middle area code:

        self.contentWidget = QWidget()
        self.contentWidget.setLayout(QVBoxLayout())
        self.contentWidget.setStyleSheet("background-color: white;")
        self.layout().addWidget(self.contentWidget)

        self.descriptionLabel = QLabel()
        self.descriptionLabel.setText(self.tr("Welcome to Pisi GNU/Linux! Thank you for joining our community!\n\n"\
                                              "As Pisi GNU/Linux developers, we hope you enjoy using Pisi GNU/Linux. "\
                                              "The following links will guide you while using Pisi GNU/Linux. Please do not "\
                                              "hesitate to inform about your experiences, suggestions and errors you have encountered."))

        self.descriptionLabel.setWordWrap(True)
        font = self.descriptionLabel.font()
        font.setPointSize(10)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setAlignment(Qt.AlignHCenter)
        self.descriptionLabel.setStyleSheet("color: black;")
        self.contentWidget.layout().addWidget(self.descriptionLabel)

        self.mainLayout = QHBoxLayout()
        self.contentWidget.layout().addLayout(self.mainLayout)

        vlayoutI = QVBoxLayout()

        self.docLabel = QLabel()
        font = self.docLabel.font()
        font.setPointSize(14)
        font.setBold(True)
        self.docLabel.setFont(font)
        self.docLabel.setAlignment(Qt.AlignHCenter)
        self.docLabel.setText(self.tr("Documents"))
        vlayoutI.addWidget(self.docLabel)

        self.installDocButton = QPushButton()
        self.installDocButton.setFixedWidth(160)
        self.installDocButton.setCursor(Qt.PointingHandCursor)
        self.installDocButton.setText(self.tr("Installation Guide"))
        self.installDocButton.setIcon(QIcon(":/images/guide.svg"))
        self.installDocButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.installDocButton)

        self.releaseButton = QPushButton()
        self.releaseButton.setFixedWidth(160)
        self.releaseButton.setCursor(Qt.PointingHandCursor)
        self.releaseButton.setText(self.tr("Release Notes"))
        self.releaseButton.setIcon(QIcon(":/images/info.svg"))
        self.releaseButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.releaseButton)

        self.wikiButton = QPushButton()
        self.wikiButton.setFixedWidth(160)
        self.wikiButton.setCursor(Qt.PointingHandCursor)
        self.wikiButton.setText(self.tr("Pisi GNU/Linux Wiki"))
        self.wikiButton.setIcon(QIcon(":/images/wikipedia-logo.svg"))
        self.wikiButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.wikiButton)

        vlayoutII = QVBoxLayout()

        self.supportLabel = QLabel()
        font = self.supportLabel.font()
        font.setPointSize(14)
        font.setBold(True)
        self.supportLabel.setFont(font)
        self.supportLabel.setAlignment(Qt.AlignHCenter)
        self.supportLabel.setText(self.tr("Support"))
        vlayoutII.addWidget(self.supportLabel)

        self.forumButton = QPushButton()
        self.forumButton.setFixedWidth(160)
        self.forumButton.setCursor(Qt.PointingHandCursor)
        self.forumButton.setText(self.tr("Forum"))
        self.forumButton.setIconSize(QSize(32, 32))
        self.forumButton.setIcon(QIcon(":/images/forum.svg"))
        vlayoutII.addWidget(self.forumButton)

        self.chatButton = QPushButton()
        self.chatButton.setFixedWidth(160)
        self.chatButton.setCursor(Qt.PointingHandCursor)
        self.chatButton.setText(self.tr("Chat Rooms"))
        self.chatButton.setIcon(QIcon(":/images/chat.svg"))
        self.chatButton.setIconSize(QSize(32, 32))
        vlayoutII.addWidget(self.chatButton)

        self.bugsButton = QPushButton()
        self.bugsButton.setFixedWidth(160)
        self.bugsButton.setCursor(Qt.PointingHandCursor)
        self.bugsButton.setText(self.tr("Bug Report"))
        self.bugsButton.setIcon(QIcon(":/images/bug.svg"))
        self.bugsButton.setIconSize(QSize(32, 32))
        vlayoutII.addWidget(self.bugsButton)

        vlayoutIII = QVBoxLayout()

        self.installLabel = QLabel()
        font = self.installLabel.font()
        font.setPointSize(14)
        font.setBold(True)
        self.installLabel.setFont(font)
        self.installLabel.setAlignment(Qt.AlignHCenter)
        self.installLabel.setText(self.tr("Installation"))
        vlayoutIII.addWidget(self.installLabel)

        # TODO: Calamares -> YALI
        self.useKalamarButton = QPushButton()
        self.useKalamarButton.setFixedWidth(160)
        self.useKalamarButton.setCursor(Qt.PointingHandCursor)
        self.useKalamarButton.setText(self.tr("Start Installation"))
        self.useKalamarButton.setIcon(QIcon(":/images/calamares.svg"))
        self.useKalamarButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.useKalamarButton)

        self.getInvolvedButton = QPushButton()
        self.getInvolvedButton.setFixedWidth(160)
        self.getInvolvedButton.setCursor(Qt.PointingHandCursor)
        self.getInvolvedButton.setText(self.tr("Join Us"))
        self.getInvolvedButton.setIcon(QIcon(":/images/joinus.svg"))
        self.getInvolvedButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.getInvolvedButton)

        self.donateButton = QPushButton()
        self.donateButton.setFixedWidth(160)
        self.donateButton.setCursor(Qt.PointingHandCursor)
        self.donateButton.setText(self.tr("Donate"))
        self.donateButton.setIcon(QIcon(":/images/donate.svg"))
        self.donateButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.donateButton)

        self.mainLayout.addLayout(vlayoutI)
        self.mainLayout.addLayout(vlayoutII)
        self.mainLayout.addLayout(vlayoutIII)

        self.noteLabel = QLabel()
        font = self.noteLabel.font()
        font.setPointSize(12)
        font.setBold(True)
        self.noteLabel.setFont(font)
        self.noteLabel.setText(self.tr("Note: The password is \"live\"."))
        self.noteLabel.setAlignment(Qt.AlignHCenter)
        self.contentWidget.layout().addWidget(self.noteLabel)

        # The footer code:

        self.footerWidget = QWidget()
        self.footerWidget.setFixedHeight(50)
        self.footerWidget.setLayout(QHBoxLayout())
        self.footerWidget.setStyleSheet("background-image: url(:/images/background.png);")
        self.layout().addWidget(self.footerWidget)

        self.facebookButton = QPushButton()
        self.facebookButton.setFixedSize(36, 36)
        self.facebookButton.setIconSize(QSize(36, 36))
        self.facebookButton.setIcon(QIcon(":/images/facebook.svg"))
        self.facebookButton.setCursor(Qt.PointingHandCursor)
        self.facebookButton.setToolTip(self.tr("Facebook Page"))
        self.footerWidget.layout().addWidget(self.facebookButton)

        self.twitterButton = QPushButton()
        self.twitterButton.setFixedSize(36, 36)
        self.twitterButton.setIconSize(QSize(36, 36))
        self.twitterButton.setIcon(QIcon(":/images/twitter.svg"))
        self.twitterButton.setCursor(Qt.PointingHandCursor)
        self.twitterButton.setToolTip(self.tr("Twitter Page"))
        self.footerWidget.layout().addWidget(self.twitterButton)

        self.googleButton = QPushButton()
        self.googleButton.setFixedSize(36, 36)
        self.googleButton.setIconSize(QSize(36, 36))
        self.googleButton.setIcon(QIcon(":/images/google-plus.svg"))
        self.googleButton.setCursor(Qt.PointingHandCursor)
        self.googleButton.setToolTip(self.tr("Google+ Page"))
        self.footerWidget.layout().addWidget(self.googleButton)

        self.instagramButton = QPushButton()
        self.instagramButton.setFixedSize(36, 36)
        self.instagramButton.setIconSize(QSize(36, 36))
        self.instagramButton.setIcon(QIcon(":/images/instagram.svg"))
        self.instagramButton.setCursor(Qt.PointingHandCursor)
        self.instagramButton.setToolTip(self.tr("Instagram Page"))
        self.footerWidget.layout().addWidget(self.instagramButton)

        self.githubButton = QPushButton()
        self.githubButton.setFixedSize(36, 36)
        self.githubButton.setIconSize(QSize(36, 36))
        self.githubButton.setIcon(QIcon(":/images/github-logo.svg"))
        self.githubButton.setCursor(Qt.PointingHandCursor)
        self.githubButton.setToolTip(self.tr("GitHub Page"))
        self.footerWidget.layout().addWidget(self.githubButton)

        self.slackButton = QPushButton()
        self.slackButton.setFixedSize(36, 36)
        self.slackButton.setIconSize(QSize(36, 36))
        self.slackButton.setIcon(QIcon(":/images/Slack.png"))
        self.slackButton.setCursor(Qt.PointingHandCursor)
        self.slackButton.setToolTip(self.tr("Slack Page"))
        self.footerWidget.layout().addWidget(self.slackButton)

        self.footerWidget.layout().addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.openCheckBox = QCheckBox()
        self.openCheckBox.setChecked(os.path.exists(os.path.join(os.environ["HOME"],
                                                                 ".config", "autostart", "pisilinux-welcome.desktop")))
        font = self.openCheckBox.font()
        font.setBold(True)
        self.openCheckBox.setFont(font)
        self.openCheckBox.setText(self.tr("Show on startup"))
        self.openCheckBox.setStyleSheet("color: white;")
        self.footerWidget.layout().addWidget(self.openCheckBox)

        self.facebookButton.clicked.connect(self.facebookPage)
        self.twitterButton.clicked.connect(self.twitterPage)
        self.googleButton.clicked.connect(self.googlePage)
        self.instagramButton.clicked.connect(self.instagramPage)
        self.githubButton.clicked.connect(self.githubPage)
        self.slackButton.clicked.connect(self.slackPage)

        self.installDocButton.clicked.connect(self.installDoc)
        self.releaseButton.clicked.connect(self.releaseNote)
        self.wikiButton.clicked.connect(self.wikiPage)
        self.forumButton.clicked.connect(self.forumPage)
        self.chatButton.clicked.connect(self.chatPages)
        self.getInvolvedButton.clicked.connect(self.involvedPage)
        self.donateButton.clicked.connect(self.donatePage)
        self.openCheckBox.clicked.connect(self.openState)
        self.bugsButton.clicked.connect(self.issuePage)

    def setSystem(self, type):
        if type == "live":
            self.useKalamarButton.clicked.connect(self.calamaresExec)

        else:
            self.useKalamarButton.setText(self.tr("Start Kaptan"))
            self.useKalamarButton.setIcon(QIcon(":/images/kaptan.svg"))
            self.useKalamarButton.clicked.connect(self.kaptanExec)
            self.installLabel.setText(self.tr("Project"))
            self.noteLabel.hide()
            self.contentWidget.layout().addItem(QSpacerItem(20, 50, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def facebookPage(self):
        QDesktopServices.openUrl(QUrl("https://www.facebook.com/Pisilinux/"))

    def twitterPage(self):
        QDesktopServices.openUrl(QUrl("https://twitter.com/pisilinux"))

    def googlePage(self):
        QDesktopServices.openUrl(QUrl("https://plus.google.com/communities/113565681602860915332"))

    def instagramPage(self):
        QDesktopServices.openUrl(QUrl("https://www.instagram.com/pisilinux/"))

    def githubPage(self):
        QDesktopServices.openUrl(QUrl("https://github.com/pisilinux"))

    def slackPage(self):
        QDesktopServices.openUrl(QUrl("http://pisi.slack.com/"))

    def installDoc(self):
        QProcess.startDetached("xdg-open /usr/share/welcome/data/pisilinux-2-0-kurulum-belgesi.pdf")

    def releaseNote(self):
        pass

    def wikiPage(self):
        QDesktopServices.openUrl(QUrl("http://wiki.pisilinux.org"))

    def forumPage(self):
        QDesktopServices.openUrl(QUrl("http://forum.pisilinux.org"))

    def chatPages(self):
        QDesktopServices.openUrl(QUrl("http://pisi.slack.com"))

    def calamaresExec(self):
        QProcess.startDetached("sudo LC_ALL=en_US calamares &")

    def kaptanExec(self):
        QProcess.startDetached("kaptan &")

    def involvedPage(self):
        QDesktopServices.openUrl(QUrl("http://www.pisilinux.org/iletisim/"))

    def donatePage(self):
        QDesktopServices.openUrl(QUrl("https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=AS4PKA7HH38PE"))

    def issuePage(self):
        QDesktopServices.openUrl(QUrl("https://github.com/pisilinux/main/issues/new"))

    def openState(self):
        if self.openCheckBox.isChecked():
            try:
                shutil.copy("/usr/share/welcome/data/pisilinux-welcome.desktop",
                            os.path.join(os.environ["HOME"], ".config", "autostart"))

            except OSError as err:
                print(err)

        else:
            try:
                os.remove(os.path.join(os.environ["HOME"], ".config", "autostart", "pisilinux-welcome.desktop"))

            except OSError as err:
                print(err)
