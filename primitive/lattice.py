import bpy
from bpy.types import Operator
from mathutils import Vector
from bpy.props import IntProperty, FloatProperty
from primitive.primitive import CreatePrimitive
from bsmax.actions import delete_objects
from bsmax.math import get_offset_by_orient

class Lattice:
	def __init__(self):
		self.finishon = 3
		self.owner = None
	def reset(self):
		self.__init__()
	def create(self, ctx, clickpoint):
		bpy.ops.object.add(type='LATTICE', location=clickpoint.view)
		self.owner = ctx.active_object
		self.owner.rotation_euler = clickpoint.orient
	def update(self):
		pass
	def abort(self):
		delete_objects([self.owner])

class BsMax_OT_CreateLattice(CreatePrimitive):
	bl_idname = "bsmax.createlattice"
	bl_label = "Lattice (Create)"
	subclass = Lattice()

	resolution: IntProperty(name="Resolation", min= 2, max= 64)
	width, length, height = 0, 0, 0
	location = Vector((0,0,0))

	def create(self, ctx, clickpoint):
		self.subclass.create(ctx, clickpoint)
		self.subclass.owner.scale = (0,0,0)
		self.subclass.owner.data.points_u = self.resolution
		self.subclass.owner.data.points_v = self.resolution
		self.subclass.owner.data.points_w = self.resolution

	def update(self, clickcount, dimantion):
		if clickcount == 1:
			self.width = dimantion.width
			self.length = dimantion.length
			self.location = self.subclass.owner.location = dimantion.center
		if clickcount == 2:
			self.height = dimantion.height
			offset = get_offset_by_orient(Vector((0,0,dimantion.height / 2)), dimantion.view_name)
			self.subclass.owner.location = self.location + offset
		self.subclass.owner.scale = (self.width, self.length, self.height)
	def finish(self):
		pass

class BsMax_OT_EditLattice(Operator):
	bl_idname = "bsmax.editlattice"
	bl_label = "Edit Lattice"
	bl_options = {"UNDO"}

	width: FloatProperty(name="Width", min= 0)
	length: FloatProperty(name="Length", min= 0)
	height: FloatProperty(name="Height", min= 0)
	u_res: IntProperty(name="Resolation U", min= 2, max= 1000)
	v_res: IntProperty(name="Resolation V", min= 2, max= 1000)
	w_res: IntProperty(name="Resolation W", min= 2, max= 1000)
	obj = None

	@classmethod
	def poll(self, ctx):
		if ctx.active_object != None:
			if ctx.active_object.type == 'LATTICE':
				return True
		return False

	def draw(self, ctx):
		layout = self.layout
		row = layout.row()
		Box = row.box()
		Col = Box.column(align = True)
		Col.label(text = "Parameters")
		Col.prop(self, "width")
		Col.prop(self, "length")
		Col.prop(self, "height")
		Col = Box.column(align = True)
		Col.prop(self, "u_res")
		Col.prop(self, "v_res")
		Col.prop(self, "w_res")

	def check(self, ctx):
		self.obj.dimensions = (self.width, self.length, self.height)
		self.obj.data.points_u = self.u_res
		self.obj.data.points_v = self.v_res
		self.obj.data.points_w = self.w_res
		return True

	def execute(self, ctx):
		return {'FINISHED'}

	def cancel(self, ctx):
		return None

	def invoke(self, ctx, event):
		self.obj = ctx.active_object
		if self.obj.type == "LATTICE":
			self.width = self.obj.dimensions.x
			self.length = self.obj.dimensions.y
			self.height = self.obj.dimensions.z
			self.u_res = self.obj.data.points_u
			self.v_res = self.obj.data.points_v
			self.w_res = self.obj.data.points_w
		wm = ctx.window_manager
		return wm.invoke_props_dialog(self, width = 140)

def lattice_cls(register):
	classes = [BsMax_OT_CreateLattice,BsMax_OT_EditLattice]
	for c in classes:
		if register: bpy.utils.register_class(c)
		else: bpy.utils.unregister_class(c)

if __name__ == '__main__':
	lattice_cls(True)

__all__ = ["lattice_cls"]