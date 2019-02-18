# -*- coding: utf-8 -*-
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
import os
import shutil
import webbrowser

from PyQt5.QtCore import Qt, QSysInfo, QSize, QProcess
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
                             QLabel, QSpacerItem, QSizePolicy, QCheckBox,
                             QDesktopWidget)


class welcomeui(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle(self.tr("Welcome Pisi GNU/Linux"))
        self.setFixedSize(700, 475)
        self.setWindowIcon(QIcon(":/images/pisilinux-welcome.svg"))
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("QPushButton {border: none; text-align: left; color:black;} QLabel {color:black;}")

        x = (QDesktopWidget().width() - self.width()) // 2
        y = (QDesktopWidget().height() - self.height()) // 2
        self.move(x, y)

        # The header code:

        self.headerWidget = QWidget()
        self.headerWidget.setFixedHeight(80)
        self.headerWidget.setLayout(QHBoxLayout())
        self.headerWidget.setStyleSheet("background-image:url(:/images/background.png);")
        self.layout().addWidget(self.headerWidget)

        self.pisiWhiteLogo = QLabel()
        self.pisiWhiteLogo.setFixedSize(64, 64)
        self.pisiWhiteLogo.setScaledContents(True)
        self.pisiWhiteLogo.setPixmap(
            QIcon(":/images/pisi-white.svg").pixmap(self.pisiWhiteLogo.size()))
        self.headerWidget.layout().addWidget(self.pisiWhiteLogo)

        self.pisiTextLabel = QLabel()
        self.pisiTextLabel.setFixedSize(157, 48)
        self.pisiTextLabel.setScaledContents(True)
        self.pisiTextLabel.setPixmap(QPixmap(":/images/pisi-text.png"))
        self.headerWidget.layout().addWidget(self.pisiTextLabel)

        self.headerWidget.layout().addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.versionLabel = QLabel()
        font = self.versionLabel.font()
        font.setPointSize(12)
        self.versionLabel.setFont(font)
        self.versionLabel.setText(
            "{} - {}".format(
                QSysInfo.productVersion(), QSysInfo.currentCpuArchitecture()))
        self.versionLabel.setStyleSheet("color: white; font-weight: bold;")
        self.headerWidget.layout().addWidget(self.versionLabel)

        # The middle area code:

        self.contentWidget = QWidget()
        self.contentWidget.setLayout(QVBoxLayout())
        self.contentWidget.setStyleSheet("background-color: white;")
        self.layout().addWidget(self.contentWidget)

        self.meetingLabel = QLabel()
        self.meetingLabel.setText(
            self.tr("Welcome to Pisi GNU/Linux!"
                    " Thank you for joining our community!\n\n"
                    "As Pisi GNU/Linux developers,"
                    " we hope you enjoy using Pisi GNU/Linux."
                    " The following links will guide you while"
                    " using Pisi GNU/Linux. Please do not"
                    " hesitate to inform about your experiences,"
                    " suggestions and errors you have encountered."))

        self.meetingLabel.setWordWrap(True)
        font = self.meetingLabel.font()
        font.setPointSize(10)
        self.meetingLabel.setFont(font)
        self.meetingLabel.setAlignment(Qt.AlignHCenter)
        self.meetingLabel.setStyleSheet("color: black;")
        self.contentWidget.layout().addWidget(self.meetingLabel)

        self.mainLayout = QHBoxLayout()
        self.contentWidget.layout().addLayout(self.mainLayout)

        vlayoutI = QVBoxLayout()

        self.docsHeader = QLabel()
        font = self.docsHeader.font()
        font.setPointSize(14)
        font.setBold(True)
        self.docsHeader.setFont(font)
        self.docsHeader.setAlignment(Qt.AlignHCenter)
        self.docsHeader.setText(self.tr("Documents"))
        vlayoutI.addWidget(self.docsHeader)

        self.installationDocButton = QPushButton()
        self.installationDocButton.setFixedWidth(160)
        self.installationDocButton.setCursor(Qt.PointingHandCursor)
        self.installationDocButton.setText(self.tr("Installation Guide"))
        self.installationDocButton.setIcon(QIcon(':/images/guide.svg'))
        self.installationDocButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.installationDocButton)

        self.releaseNotesButton = QPushButton()
        self.releaseNotesButton.setFixedWidth(160)
        self.releaseNotesButton.setCursor(Qt.PointingHandCursor)
        self.releaseNotesButton.setText(self.tr("Release Notes"))
        self.releaseNotesButton.setIcon(QIcon(':/images/info.svg'))
        self.releaseNotesButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.releaseNotesButton)

        self.wikiButton = QPushButton()
        self.wikiButton.setFixedWidth(160)
        self.wikiButton.setCursor(Qt.PointingHandCursor)
        self.wikiButton.setText(self.tr("Pisi GNU/Linux Wiki"))
        self.wikiButton.setIcon(QIcon(':/images/wikipedia-logo.svg'))
        self.wikiButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.wikiButton)

        vlayoutII = QVBoxLayout()

        self.supportHeader = QLabel()
        font = self.supportHeader.font()
        font.setPointSize(14)
        font.setBold(True)
        self.supportHeader.setFont(font)
        self.supportHeader.setAlignment(Qt.AlignHCenter)
        self.supportHeader.setText(self.tr("Support"))
        vlayoutII.addWidget(self.supportHeader)

        self.forumButton = QPushButton()
        self.forumButton.setFixedWidth(160)
        self.forumButton.setCursor(Qt.PointingHandCursor)
        self.forumButton.setText(self.tr("Forum"))
        self.forumButton.setIconSize(QSize(32, 32))
        self.forumButton.setIcon(QIcon(':/images/forum.svg'))
        vlayoutII.addWidget(self.forumButton)

        self.chatButton = QPushButton()
        self.chatButton.setFixedWidth(160)
        self.chatButton.setCursor(Qt.PointingHandCursor)
        self.chatButton.setText(self.tr("Chat Rooms"))
        self.chatButton.setIcon(QIcon(':/images/chat.svg'))
        self.chatButton.setIconSize(QSize(32, 32))
        vlayoutII.addWidget(self.chatButton)

        self.bugsButton = QPushButton()
        self.bugsButton.setFixedWidth(160)
        self.bugsButton.setCursor(Qt.PointingHandCursor)
        self.bugsButton.setText(self.tr("Bug Report"))
        self.bugsButton.setIcon(QIcon(':/images/bug.svg'))
        self.bugsButton.setIconSize(QSize(32, 32))
        vlayoutII.addWidget(self.bugsButton)

        vlayoutIII = QVBoxLayout()

        self.installationHeader = QLabel()
        font = self.installationHeader.font()
        font.setPointSize(14)
        font.setBold(True)
        self.installationHeader.setFont(font)
        self.installationHeader.setAlignment(Qt.AlignHCenter)
        self.installationHeader.setText(self.tr("Installation"))
        vlayoutIII.addWidget(self.installationHeader)

        # TODO: Also for YALI
        self.calamaresButton = QPushButton()
        self.calamaresButton.setFixedWidth(160)
        self.calamaresButton.setCursor(Qt.PointingHandCursor)
        self.calamaresButton.setText(self.tr("Start Installation"))
        self.calamaresButton.setIcon(QIcon(':/images/calamares.svg'))
        self.calamaresButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.calamaresButton)

        self.joinUsButton = QPushButton()
        self.joinUsButton.setFixedWidth(160)
        self.joinUsButton.setCursor(Qt.PointingHandCursor)
        self.joinUsButton.setText(self.tr("Join Us"))
        self.joinUsButton.setIcon(QIcon(':/images/joinus.svg'))
        self.joinUsButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.joinUsButton)

        self.donateButton = QPushButton()
        self.donateButton.setFixedWidth(160)
        self.donateButton.setCursor(Qt.PointingHandCursor)
        self.donateButton.setText(self.tr("Ev"))
        self.donateButton.setIcon(QIcon(':/images/ev.svg'))
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
        self.noteLabel.setMinimumSize(250, 50)
        self.noteLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.contentWidget.layout().addWidget(self.noteLabel)

        # The footer code:

        self.footerWidget = QWidget()
        self.footerWidget.setFixedHeight(50)
        self.footerWidget.setLayout(QHBoxLayout())
        self.footerWidget.setStyleSheet(
            "background-image: url(:/images//background.png);")
        self.layout().addWidget(self.footerWidget)

        self.facebookButton = QPushButton()
        self.facebookButton.setFixedSize(36, 36)
        self.facebookButton.setIconSize(QSize(36, 36))
        self.facebookButton.setIcon(QIcon(':/images/facebook.svg'))
        self.facebookButton.setCursor(Qt.PointingHandCursor)
        self.facebookButton.setToolTip(self.tr("Facebook Page"))
        self.footerWidget.layout().addWidget(self.facebookButton)

        self.twitterButton = QPushButton()
        self.twitterButton.setFixedSize(36, 36)
        self.twitterButton.setIconSize(QSize(36, 36))
        self.twitterButton.setIcon(QIcon(':/images/twitter.svg'))
        self.twitterButton.setCursor(Qt.PointingHandCursor)
        self.twitterButton.setToolTip(self.tr("Twitter Page"))
        self.footerWidget.layout().addWidget(self.twitterButton)

        self.googleButton = QPushButton()
        self.googleButton.setFixedSize(36, 36)
        self.googleButton.setIconSize(QSize(36, 36))
        self.googleButton.setIcon(QIcon(':/images/google-plus.svg'))
        self.googleButton.setCursor(Qt.PointingHandCursor)
        self.googleButton.setToolTip(self.tr("Google+ Page"))
        self.footerWidget.layout().addWidget(self.googleButton)

        self.instagramButton = QPushButton()
        self.instagramButton.setFixedSize(36, 36)
        self.instagramButton.setIconSize(QSize(36, 36))
        self.instagramButton.setIcon(QIcon(':/images/instagram.svg'))
        self.instagramButton.setCursor(Qt.PointingHandCursor)
        self.instagramButton.setToolTip(self.tr("Instagram Page"))
        self.footerWidget.layout().addWidget(self.instagramButton)

        self.githubButton = QPushButton()
        self.githubButton.setFixedSize(36, 36)
        self.githubButton.setIconSize(QSize(36, 36))
        self.githubButton.setIcon(QIcon(':/images/github-logo.svg'))
        self.githubButton.setCursor(Qt.PointingHandCursor)
        self.githubButton.setToolTip(self.tr("GitHub Page"))
        self.footerWidget.layout().addWidget(self.githubButton)

        self.footerWidget.layout().addItem(
            QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.startupCheckBox = QCheckBox()
        self.startupCheckBox.setChecked(
            os.path.exists(os.path.join(os.environ["HOME"],
                                        ".config",
                                        "autostart",
                                        "pisilinux-welcome.desktop")))
        font = self.startupCheckBox.font()
        font.setBold(True)
        self.startupCheckBox.setFont(font)
        self.startupCheckBox.setText(self.tr("Show on startup"))
        self.startupCheckBox.setStyleSheet("color: white;")
        self.footerWidget.layout().addWidget(self.startupCheckBox)

        self.facebookButton.clicked.connect(self.facebookPage)
        self.twitterButton.clicked.connect(self.twitterPage)
        self.googleButton.clicked.connect(self.googlePage)
        self.instagramButton.clicked.connect(self.instagramPage)
        self.githubButton.clicked.connect(self.githubPage)

        self.releaseNotesButton.clicked.connect(self.releaseNotes)
        self.wikiButton.clicked.connect(self.wikiPage)
        self.forumButton.clicked.connect(self.forumPage)
        self.chatButton.clicked.connect(self.chatPages)
        self.joinUsButton.clicked.connect(self.joinUsPage)
        self.donateButton.clicked.connect(self.homePage)
        self.startupCheckBox.clicked.connect(self.startupState)
        self.bugsButton.clicked.connect(self.issuesPage)

    def setSystem(self, type):
        if type == "live":
            self.installationDocButton.clicked.connect(self.installationDocument)

            # TODO: Also for YALI
            self.calamaresButton.clicked.connect(self.calamaresExec)

        else:
            self.installationDocButton.setText(self.tr("Pisi Guide"))
            self.installationDocButton.clicked.connect(self.installationDocument)

            self.installationHeader.setText(self.tr("Project"))

            # TODO: Also for YALI
            self.calamaresButton.setText(self.tr("Start Kaptan"))
            self.calamaresButton.setIcon(QIcon(':/images/kaptan.svg'))
            self.calamaresButton.clicked.connect(self.kaptanExec)

            self.noteLabel.hide()
            self.contentWidget.layout().addItem(
                QSpacerItem(20, 50, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def open_url(self, url):
        webbrowser.get('firefox').open(url)

    def facebookPage(self):
        self.open_url("https://www.facebook.com/Pisilinux/")

    def twitterPage(self):
        self.open_url("https://twitter.com/pisilinux")

    def googlePage(self):
        self.open_url("https://plus.google.com/communities/113565681602860915332")

    def instagramPage(self):
        self.open_url("https://www.instagram.com/pisilinux/")

    def githubPage(self):
        self.open_url("https://github.com/pisilinux")

    def installationDocument(self):
        self.open_url("https://pisilinux.org/wiki/cont/53-pisi-linux-kurulum.html")

    def releaseNotes(self):
        self.open_url("/usr/share/welcome/data/media-content/index.html")

    def wikiPage(self):
        self.open_url("https://pisilinux.org/wiki")

    def forumPage(self):
        self.open_url("https://pisilinux.org/forum")

    def chatPages(self):
        self.open_url("https://gitter.im/Pisi-GNU-Linux/Lobby")

    def joinUsPage(self):
        self.open_url("http://www.pisilinux.org/iletisim/")

    def homePage(self):
        self.open_url("http://www.pisilinux.org")

    # TODO: Also for YALI
    def calamaresExec(self):
        QProcess.startDetached("sudo LC_ALL=en_US calamares &")

    def kaptanExec(self):
        QProcess.startDetached("kaptan &")

    def issuesPage(self):
        self.open_url("https://github.com/pisilinux/main/issues/new")

    def startupState(self):
        if self.startupCheckBox.isChecked():
            try:
                shutil.copy("/usr/share/applications/pisilinux-welcome.desktop",
                            os.path.join(os.environ["HOME"],
                                         ".config", "autostart"))

            except OSError as err:
                print(err)

        else:
            try:
                os.remove(
                    os.path.join(
                        os.environ["HOME"], ".config", "autostart",
                        "pisilinux-welcome.desktop"))

            except OSError as err:
                print(err)
