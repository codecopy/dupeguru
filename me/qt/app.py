#!/usr/bin/env python
# Unit Name: app
# Created By: Virgil Dupras
# Created On: 2009-05-21
# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)

import hsfs.phys.music

from dupeguru import data_me, scanner

from base.app import DupeGuru as DupeGuruBase
from details_dialog import DetailsDialog
from preferences import Preferences
from preferences_dialog import PreferencesDialog

class DupeGuru(DupeGuruBase):
    LOGO_NAME = 'logo_me'
    NAME = 'dupeGuru Music Edition'
    VERSION = '5.6.2'
    DELTA_COLUMNS = frozenset([2, 3, 4, 5, 7, 8])
    
    def __init__(self):
        DupeGuruBase.__init__(self, data_me, appid=1)
    
    def _setup(self):
        self.scanner = scanner.ScannerME()
        self.directories.dirclass = hsfs.phys.music.Directory
        DupeGuruBase._setup(self)
    
    def _update_options(self):
        DupeGuruBase._update_options(self)
        self.scanner.min_match_percentage = self.prefs.filter_hardness
        self.scanner.scan_type = self.prefs.scan_type
        self.scanner.word_weighting = self.prefs.word_weighting
        self.scanner.match_similar_words = self.prefs.match_similar
        scanned_tags = set()
        if self.prefs.scan_tag_track:
            scanned_tags.add('track')
        if self.prefs.scan_tag_artist:
            scanned_tags.add('artist')
        if self.prefs.scan_tag_album:
            scanned_tags.add('album')
        if self.prefs.scan_tag_title:
            scanned_tags.add('title')
        if self.prefs.scan_tag_genre:
            scanned_tags.add('genre')
        if self.prefs.scan_tag_year:
            scanned_tags.add('year')
        self.scanner.scanned_tags = scanned_tags
    
    def _create_details_dialog(self, parent):
        return DetailsDialog(parent, self)
    
    def _create_preferences(self):
        return Preferences()
    
    def _create_preferences_dialog(self, parent):
        return PreferencesDialog(parent, self)
    
