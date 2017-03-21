
import numpy as np
from qtpy import QtWidgets, QtCore, QtGui


import flika
flika_version = flika.__version__
from flika import global_vars as g
from flika.process.BaseProcess import BaseProcess, WindowSelector, SliderLabel, CheckBox
from flika.window import Window
from flika.roi import ROI_rectangle, makeROI
from flika.process.file_ import open_file_gui, open_file


class Cloud_counter(BaseProcess):
    """ cloud_counter(firstFrame,lastFrame,increment=False,keepSourceWindow=False)
    This creates a new stack from the frames between the firstFrame and the lastFrame

    Parameters:
        | firstFrame (int) -- The index of the first frame in the stack to be kept.
        | lastFrame (int) -- The index of the last frame in the stack to be kept.
        | increment (int) -- if increment equals i, then every ith frame is kept.
        | delete (bool) -- if False, then the specified frames will be kept.  If True, they will be deleted.
    Returns:
        newWindow
    """

    def __init__(self):
        super().__init__()

    def gui(self):
        self.gui_reset()
        nFrames = 1
        if g.currentWindow is not None:
            nFrames = g.currentWindow.image.shape[0]
        firstFrame = QtWidgets.QSpinBox()
        firstFrame.setMaximum(nFrames - 1)
        lastFrame = QtWidgets.QSpinBox()
        lastFrame.setRange(0, nFrames - 1)
        increment = QtWidgets.QSpinBox()
        increment.setMaximum(nFrames)
        increment.setMinimum(1)
        delete = CheckBox()

        self.items.append({'name': 'firstFrame', 'string': 'First Frame', 'object': firstFrame})
        self.items.append({'name': 'lastFrame', 'string': 'Last Frame', 'object': lastFrame})
        self.items.append({'name': 'increment', 'string': 'Increment', 'object': increment})
        self.items.append({'name': 'delete', 'string': 'Delete', 'object': delete})
        super().gui()

    def get_init_settings_dict(self):
        s = dict()
        s['firstFrame'] = 0
        s['lastFrame'] = g.currentWindow.image.shape[0]
        s['increment'] = 1
        s['delete'] = False
        return s

    def __call__(self, firstFrame, lastFrame, increment=1, delete=False, keepSourceWindow=False):
        self.start(keepSourceWindow)
        if not delete:
            self.newtif = self.tif[firstFrame:lastFrame + 1:increment]
        if delete:
            idxs_not = np.arange(firstFrame, lastFrame + 1, increment)
            idxs = np.ones(len(self.tif), dtype=np.bool)
            idxs[idxs_not] = False
            self.newtif = self.tif[idxs]
        self.newname = self.oldname + ' - Kept Stack'
        return self.end()

cloud_counter = Cloud_counter()


def launch_docs():
    url='https://github.com/flika-org/flika_plugin_template'
    QtWidgets.QDesktopServices.openUrl(QtCore.QUrl(url))