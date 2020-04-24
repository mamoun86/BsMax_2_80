############################################################################
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################################

import bpy
from bpy.types import Menu

def ffd_menu(self, ctx):
	layout = self.layout
	layout.separator()
	layout.operator("modifier.ffd2x2x2set",text='FFD 2x2x2 (Set)',icon="OUTLINER_OB_LATTICE")
	layout.operator("modifier.ffd3x3x3set",text='FFD 3x3x3 (Set)',icon="OUTLINER_OB_LATTICE")
	layout.operator("modifier.ffd4x4x4set",text='FFD 4x4x4 (Set)',icon="OUTLINER_OB_LATTICE")

def register_menu():
	bpy.types.BSMAX_MT_latticecreatemenu.append(ffd_menu)

def unregister_menu():
	bpy.types.BSMAX_MT_latticecreatemenu.remove(ffd_menu)