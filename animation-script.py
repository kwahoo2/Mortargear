#Open mortargear.FCStd and paste the script in the FreeCAD console
import FreeCAD as App, FreeCADGui as Gui, Part, time
from PySide2 import QtGui,QtCore

class Animation(object):
    def __init__(self):
        App.Console.PrintMessage('init')

        App.ActiveDocument.recompute()

        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.my_update)
        self.timer.start(500) #500ms for step, adjust to performance of the PC

        self.an = 1

    def my_update(self):
        self.an = self.an + 1 
        App.getDocument("fixedgear").Spreadsheet.set("A2", str(self.an))
        App.ActiveDocument.recompute()
        Gui.runCommand('asm3CmdSolve',0)
        #Uncomment line below to save pics
        #Gui.ActiveDocument.ActiveView.saveImage('/home/adi/freecad-projekty/mortargear/' +str(self.an)+'.png',1280,720,'Current')
        print(str(self.an))

    def stop(self):
        self.timer.stop()
       

animation = Animation()

#To stop the animation, type:
#animation.stop()

#To encode a video
#ffmpeg -framerate 25 -i %00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
