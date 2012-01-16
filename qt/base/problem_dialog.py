# Created By: Virgil Dupras
# Created On: 2010-04-12
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtCore import Qt
from PyQt4.QtGui import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy,
    QLabel, QTableView, QAbstractItemView, QApplication)

from hscommon.trans import trget
from .problem_table import ProblemTable

tr = trget('ui')

class ProblemDialog(QDialog):
    def __init__(self, parent, model):
        flags = Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowSystemMenuHint
        QDialog.__init__(self, parent, flags)
        self._setupUi()
        self.model = model
        self.model.view = self
        self.table = ProblemTable(self.model.problem_table, view=self.tableView)
        
        self.revealButton.clicked.connect(self.model.reveal_selected_dupe)
        self.closeButton.clicked.connect(self.accept)
    
    def _setupUi(self):
        self.setWindowTitle(tr("Problems!"))
        self.resize(413, 323)
        self.verticalLayout = QVBoxLayout(self)
        self.label = QLabel(self)
        msg = tr("There were problems processing some (or all) of the files. The cause of "
            "these problems are described in the table below. Those files were not "
            "removed from your results.")
        self.label.setText(msg)
        self.label.setWordWrap(True)
        self.verticalLayout.addWidget(self.label)
        self.tableView = QTableView(self)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setDefaultSectionSize(18)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QHBoxLayout()
        self.revealButton = QPushButton(self)
        self.revealButton.setText(tr("Reveal Selected"))
        self.horizontalLayout.addWidget(self.revealButton)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QPushButton(self)
        self.closeButton.setText(tr("Close"))
        self.closeButton.setDefault(True)
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
    

if __name__ == '__main__':
    import sys
    from ..testapp import TestApp
    app = QApplication([])
    dgapp = TestApp()
    dialog = ProblemDialog(None, dgapp)
    dialog.show()
    sys.exit(app.exec_())