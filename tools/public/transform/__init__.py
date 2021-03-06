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

from .alignobjects import register_alignobjects,unregister_alignobjects
from .mirror import register_mirror,unregister_mirror
from .transforms import register_transforms,unregister_transforms
from .transformtypein import register_transformtypein,unregister_transformtypein
from .zoomextended import register_zoomextended,unregister_zoomextended

def register_transform():
	register_alignobjects()
	register_mirror()
	register_transforms()
	register_transformtypein()
	register_zoomextended()

def unregister_transform():
	unregister_alignobjects()
	unregister_mirror()
	unregister_transforms()
	unregister_transformtypein()
	unregister_zoomextended()