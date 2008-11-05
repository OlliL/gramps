#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2008  Brian G. Matherly
# Copyright (C) 2008  Jerome Rapinat
# Copyright (C) 2008  Benny Malengier
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
from gettext import gettext as _

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from Filters.Rules import Rule

#-------------------------------------------------------------------------
# "People who have images"
#-------------------------------------------------------------------------
class HasGalleryBase(Rule):
    """Objects who have Media Object"""

    labels      = [  _('Number of instances:'), _('Number must be')]
    name        = _('Object with <count> Media reference')
    description = _("Matches objects with certain number of items in the gallery")
    category    = _('General filters')

    def prepare(self, db):
        # things we want to do just once, not for every handle
        if  self.list[1] == _('lesser than'):
           self.count_type = 0
        elif self.list[1] == _('greater than'):
            self.count_type = 2
        else:
            self.count_type = 1 # "equal to"

        self.userSelectedCount = int(self.list[0])
        
    def apply(self, db, obj):
        count = len( obj.get_media_list())
        if self.count_type == 0:     # "lesser than"
            return count < self.userSelectedCount
        elif self.count_type == 2:   # "greater than"
            return count > self.userSelectedCount
        # "equal to"
        return count == self.userSelectedCount
