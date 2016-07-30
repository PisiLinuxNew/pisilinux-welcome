from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QCheckBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QDesktopServices, QPixmap
from PyQt5.QtCore import Qt, QSysInfo, QSize, QUrl, QProcess
import os, shutil


class WelcomeUi(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle(self.tr("Welcome Pisi Linux"))
        self.setFixedSize(700, 475)
        self.setWindowIcon(QIcon(":/images/pisilinux-welcome.svg"))
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("QPushButton {border: none; text-align:left; color: black;} QLabel {color:black;}")

        x = (QDesktopWidget().width() - self.width()) // 2
        y = (QDesktopWidget().height() - self.height()) // 2
        self.move(x, y)

        #######################
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

        #######################
        self.contentWidget = QWidget()
        self.contentWidget.setLayout(QVBoxLayout())
        self.contentWidget.setStyleSheet("background-color: white; ")
        self.layout().addWidget(self.contentWidget)

        self.descriptionLabel = QLabel()
        self.descriptionLabel.setText(self.tr("Welcome to Pisi Linux! Thank you for joining our community!\n\n"\
                                              "As Pisi Linux developers, we hope you enjoy using Pisi Linux. "\
                                              "The following links will guide you while using Pisi Linux. Please do not "\
                                              "hesitate to inform about your experiences, suggestions and errors you have encountered."))
        self.descriptionLabel.setWordWrap(True)
        font = self.descriptionLabel.font()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.descriptionLabel.setFont(font)
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
        self.installDocButton.setFixedWidth(135)
        self.installDocButton.setCursor(Qt.PointingHandCursor)
        self.installDocButton.setText(self.tr("Installation Guide"))
        self.installDocButton.setIcon(QIcon(":/images/guide.svg"))
        self.installDocButton.setIconSize(QSize(32,32))
        vlayoutI.addWidget(self.installDocButton)

        self.releaseButton = QPushButton()
        self.releaseButton.setFixedWidth(135)
        self.releaseButton.setCursor(Qt.PointingHandCursor)
        self.releaseButton.setText(self.tr("Release Notes"))
        self.releaseButton.setIcon(QIcon(":/images/info.svg"))
        self.releaseButton.setIconSize(QSize(32, 32))
        vlayoutI.addWidget(self.releaseButton)

        self.wikiButton = QPushButton()
        self.wikiButton.setFixedWidth(135)
        self.wikiButton.setCursor(Qt.PointingHandCursor)
        self.wikiButton.setText(self.tr("Pisi Linux Wiki"))
        self.wikiButton.setIcon(QIcon(":/images/wiki.svg"))
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
        self.forumButton.setFixedWidth(135)
        self.forumButton.setCursor(Qt.PointingHandCursor)
        self.forumButton.setText(self.tr("Forum"))
        self.forumButton.setIconSize(QSize(32, 32))
        self.forumButton.setIcon(QIcon(":/images/forum.svg"))
        vlayoutII.addWidget(self.forumButton)

        self.chatButton = QPushButton()
        self.chatButton.setFixedWidth(135)
        self.chatButton.setCursor(Qt.PointingHandCursor)
        self.chatButton.setText(self.tr("Chat Rooms"))
        self.chatButton.setIcon(QIcon(":/images/chat.svg"))
        self.chatButton.setIconSize(QSize(32, 32))
        vlayoutII.addWidget(self.chatButton)

        vlayoutII.addItem(QSpacerItem(20, 40, QSizePolicy.Maximum, QSizePolicy.Maximum))


        vlayoutIII = QVBoxLayout()

        self.installLabel = QLabel()
        font = self.installLabel.font()
        font.setPointSize(14)
        font.setBold(True)
        self.installLabel.setFont(font)
        self.installLabel.setAlignment(Qt.AlignHCenter)
        self.installLabel.setText(self.tr("Installation"))
        vlayoutIII.addWidget(self.installLabel)

        self.useKalamarButton = QPushButton()
        self.useKalamarButton.setFixedWidth(135)
        self.useKalamarButton.setCursor(Qt.PointingHandCursor)
        self.useKalamarButton.setText(self.tr("Start Installation"))
        self.useKalamarButton.setIcon(QIcon(":/images/calamares.svg"))
        self.useKalamarButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.useKalamarButton)

        self.getInvolvedButton = QPushButton()
        self.getInvolvedButton.setFixedWidth(135)
        self.getInvolvedButton.setCursor(Qt.PointingHandCursor)
        self.getInvolvedButton.setText(self.tr("Join Us"))
        self.getInvolvedButton.setIcon(QIcon(":/images/joinus.svg"))
        self.getInvolvedButton.setIconSize(QSize(32, 32))
        vlayoutIII.addWidget(self.getInvolvedButton)

        self.donateButton = QPushButton()
        self.donateButton.setFixedWidth(150)
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
        self.noteLabel.setText(self.tr("Note: The username and password is \"live\"."))
        self.noteLabel.setAlignment(Qt.AlignHCenter)
        self.contentWidget.layout().addWidget(self.noteLabel)


        #######################
        self.footerWidget = QWidget()
        self.footerWidget.setFixedHeight(50)
        self.footerWidget.setLayout(QHBoxLayout())
        self.footerWidget.setStyleSheet("background-image: url(:/images/background.png);")
        self.layout().addWidget(self.footerWidget)

        self.facebookButton = QPushButton()
        self.facebookButton.setFixedSize(36, 36)
        self.facebookButton.setIconSize(QSize(36, 36))
        self.facebookButton.setIcon(QIcon(":/images/facebook.png"))
        self.facebookButton.setCursor(Qt.PointingHandCursor)
        self.facebookButton.setToolTip(self.tr("Facebook Page"))
        self.footerWidget.layout().addWidget(self.facebookButton)

        self.googleButton = QPushButton()
        self.googleButton.setFixedSize(36, 36)
        self.googleButton.setIconSize(QSize(36, 36))
        self.googleButton.setIcon(QIcon(":/images/google.png"))
        self.googleButton.setCursor(Qt.PointingHandCursor)
        self.googleButton.setToolTip(self.tr("Google+ Page"))
        self.footerWidget.layout().addWidget(self.googleButton)

        self.twitterButton = QPushButton()
        self.twitterButton.setFixedSize(36, 36)
        self.twitterButton.setIconSize(QSize(36, 36))
        self.twitterButton.setIcon(QIcon(":/images/twitter.png"))
        self.twitterButton.setCursor(Qt.PointingHandCursor)
        self.twitterButton.setToolTip(self.tr("Twitter Page"))
        self.footerWidget.layout().addWidget(self.twitterButton)

        self.githubButton = QPushButton()
        self.githubButton.setFixedSize(36, 36)
        self.githubButton.setIconSize(QSize(36, 36))
        self.githubButton.setIcon(QIcon(":/images/git.svg"))
        self.githubButton.setCursor(Qt.PointingHandCursor)
        self.githubButton.setToolTip(self.tr("GitHub Page"))
        self.footerWidget.layout().addWidget(self.githubButton)

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
        self.googleButton.clicked.connect(self.googlePage)
        self.twitterButton.clicked.connect(self.twitterPage)
        self.githubButton.clicked.connect(self.githubPage)


        self.installDocButton.clicked.connect(self.installedDoc)
        self.releaseButton.clicked.connect(self.releaseNote)
        self.wikiButton.clicked.connect(self.wikiPage)
        self.forumButton.clicked.connect(self.forumPage)
        self.chatButton.clicked.connect(self.chatPages)
        self.getInvolvedButton.clicked.connect(self.involvedPage)
        self.donateButton.clicked.connect(self.donatePage)
        self.openCheckBox.clicked.connect(self.openState)

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

    def googlePage(self):
        QDesktopServices.openUrl(QUrl("https://plus.google.com/communities/113565681602860915332"))

    def twitterPage(self):
        QDesktopServices.openUrl(QUrl("https://twitter.com/pisilinux"))

    def githubPage(self):
        QDesktopServices.openUrl(QUrl("https://github.com/pisilinux"))

    def installedDoc(self):
        QProcess.startDetached("xdg-open /usr/share/welcome/data/pisilinux-2-0-kurulum-belgesi.pdf")

    def releaseNote(self):
        pass

    def wikiPage(self):
        QDesktopServices.openUrl(QUrl("http://wiki.pisilinux.org"))

    def forumPage(self):
        QDesktopServices.openUrl(QUrl("http://forum.pisilinux.org"))

    def chatPages(self):
        QDesktopServices.openUrl(QUrl("http://pisi.slack.com"))
        QDesktopServices.openUrl(QUrl("http://www.pisilinux.org/irc-2/"))

    def calamaresExec(self):
        QProcess.startDetached("sudo LC_ALL=en_US calamares &")

    def kaptanExec(self):
        QProcess.startDetached("kaptan &")

    def involvedPage(self):
        QDesktopServices.openUrl(QUrl("http://www.pisilinux.org/iletisim/"))

    def donatePage(self):
        QDesktopServices.openUrl(QUrl("https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=AS4PKA7HH38PE"))

    def openState(self):
        if self.openCheckBox.isChecked():
            try:
                shutil.copy("/usr/share/welcome/data/pisilinux-welcome.desktop",
                            os.path.join(os.environ["HOME"], ".config", "autostart"))

            except FileNotFoundError as err:
                print(err)

        else:
            try:
                os.remove(os.path.join(os.environ["HOME"], ".config", "autostart", "pisilinux-welcome.desktop"))

            except OSError as err:
                print(err)
