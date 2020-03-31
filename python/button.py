# Copyright 2017 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.


from bokeh.models import Button, Toggle

class button():
    def __init__(self, widget_lst, label):
        self.widget_lst = widget_lst
        self.button = None
        self.initialize(label)

    def initialize(self, label):
        # self.button = Button(label = label) # Using a simple button doesn't trigger callbacks for some reason
        self.button = Toggle(label = label)
        self.widget_lst.append(self.button)

    def add_callback(self, callback):
        self.button.on_click(callback)
