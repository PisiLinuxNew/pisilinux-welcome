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

import subprocess
import os
from setuptools import setup, find_packages

langs = []
for f in os.listdir("languages"):
    if f.endswith(".ts"):
        lang_file = "languages/{}".format(f)
        subprocess.run(["lrelease", lang_file])
        langs.append(("languages/{}".format(f)).replace(".ts", ".qm"))

release_notes = []
for f in os.listdir("data/release-notes"):
    release_notes.append(("data/release-notes/{}".format(f)))

subprocess.run(["pyrcc5", "welcome.qrc", "-o", "welcome/resource.py"])

print(release_notes)
print(langs)

datas = [('/usr/share/applications', ['data/pisilinux-welcome.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['images/pisilinux-welcome.svg']),
         ('/etc/skel/.config/autostart', ['data/pisilinux-welcome.desktop']),
         ('/usr/share/pisilinux-welcome/data/release-notes', release_notes),
         ('/usr/share/pisilinux-welcome/languages', langs)]

setup(
    name="pisilinux-welcome",
    scripts=["pisilinux-welcome"],
    packages=find_packages(),
    version="1.0",
    license="GPLv3",
    description="Pisi Linux Welcome Application",
    author="Metehan Özbek",
    author_email="mthnzbk@gmail.com",
    url="https://github.com/PisiLinuxNew/pisilinux-welcome",
    keywords=["PyQt5"],
    data_files=datas
)
