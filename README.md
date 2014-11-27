Python Installation  on Windows:

Download and run : https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi
It will install python in the default drive where Windows is installed suppose it is C drive. Then the path for installation will be
 "C:\python27"

1) Hold Win and press Pause.
2) Click Advanced System Settings.
3) Click Environment Variables.
4) Under User Variables Click New 
5) ;C:\python27 to the Variable Value and Path to Variable Name .
Restart Command Prompt.

-----------------------------------------------------------------------

Python installation on Ubuntu: 
1) Go to http://packages.ubuntu.com/precise/python
2) Click on amd64 or i386 depending on 64 or 32 bit architechture or Ubuntu installation(32 or 64 bit)
3) Download python2.7.deb package from any of the mirrors
4) Using terminal go to the downloaded folder
5) type "dpkg -i python2.7.deb" (if the name of package downloaded from the mirror is python2.7.deb else type the respective name).

Alternatively you can install python using sudo apt-get install python2.7
or using the synaptic manager and selecting python from there. 


-----------------------------------------------------------------------
Route Generator on Windows
Note: A new file is created for Windows(forWindows.py). It works on both Windows and Ubuntu.

Use the following link https://pypi.python.org/pypi/PyOpenGL/3.0.1 and click on exe file and execute
Else directly download and execute the following executable file 
https://pypi.python.org/packages/any/P/PyOpenGL/PyOpenGL-3.0.1.win32.exe#md5=513cc194af65af4c5a640cf9a1bd8462

Proceed to the Route Generator folder in command prompt and type "python forWindows.py" 
------------------------------------------------------------------------

Route Generator on Ubuntu
Note: If python-tk (package for tkinter) gets installed use make on Ubuntu else type "python forWindows.py".

You will need to install python tkinter module using following link
http://packages.ubuntu.com/precise/amd64/python-tk
or by typing "sudo apt-get install python-tk"

Also OpenGL package for python needs to be installed
The following link has the package https://pypi.python.org/pypi/PyOpenGL/3.0.1
The following link guides through the installation
http://pyopengl.sourceforge.net/documentation/installation.html
or the following link can be used https://pypi.python.org/pypi/PyOpenGL/3.0.1
or you can also install it by typing "sudo apt-get install python-opengl"

In terminal type "make" 

