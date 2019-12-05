#  Copyright 2016 Metehan Özbek <mthnzbk@gmail.com>
#            2019 Erdem Ersoy <erdemersoy@erdemersoy.net>
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

from setuptools import setup, find_packages
from os import listdir, system


langs = []
for file in listdir('languages'):
    if file.endswith('ts'):
        system('lrelease languages/{}'.format(file))
        langs.append(('languages/{}'.format(file)).replace('.ts', '.qm'))


system('pyrcc5 welcome.qrc -o welcome/resource.py')

datas = [('/usr/share/applications', ['data/pisilinux-welcome.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['images/pisilinux-welcome.svg']),
         ('/etc/skel/.config/autostart', ['data/pisilinux-welcome.desktop']),
         ('/usr/share/pisilinux-welcome/data/media-content', ["data/media-content/logo.png"]),
         ('/usr/share/pisilinux-welcome/data/media-content', ["data/media-content/index.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-de.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-en.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-es.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-fr.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-hr.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-hu.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-it.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-nl.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-ru.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-sv.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-tr.html"]),
         ('/usr/share/pisilinux-welcome/data/media-content/release-notes', ["data/media-content/release-notes/releasenotes-ua.html"]),
         ('/usr/share/pisilinux-welcome/languages', langs)]

setup(
    name="pisilinux-welcome",
    scripts=["pisilinux-welcome"],
    packages=find_packages(),
    version="1.1",
    license="GPLv3",
    description="Pisi Linux Welcome Application",
    author="Metehan Özbek",
    author_email="mthnzbk@gmail.com",
    url="https://github.com/PisiLinuxNew/pisilinux-welcome",
    keywords=["PyQt5"],
    data_files=datas
)
