import numpy as np
from qtpy import QtWidgets, QtCore, QtGui
import flika
flika_version = flika.__version__
from flika import global_vars as g


def launch_docs():
    url='https://github.com/flika-org/flika_plugin_template'
    QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))