import bpy, bmesh
from mathutils import Matrix
from primitive.primitive import PrimitiveGeometryClass, CreatePrimitive
from bsmax.actions import delete_objects

class Icosphere(PrimitiveGeometryClass):
	def __init__(self):
		self.classname = "Icosphere"
		self.finishon = 2
		self.owner = None
		self.data = None
	def reset(self):
		self.__init__()
	def create(self, ctx):
		scene = ctx.scene
		# Create an empty mesh and the object.
		newmesh = bpy.data.meshes.new(self.classname)
		self.owner = bpy.data.objects.new(self.classname, newmesh)
		# Add the object into the scene.
		ctx.collection.objects.link(self.owner)
		ctx.view_layer.objects.active = self.owner
		self.owner.select_set(state = True)
		# Construct the bmesh monkey and assign it to the blender mesh
		bm = bmesh.new()
		bmesh.ops.create_icosphere(bm, matrix=Matrix.Scale(0, 4),calc_uvs=True)
		bm.to_mesh(newmesh)
		bm.free()
		self.data = self.owner.data
		pd = self.data.primitivedata
		pd.classname = self.classname
		pd.wsegs = 1
	def update(self):
		pd = self.data.primitivedata
		orgmesh = bpy.data.meshes[self.data.name]
		bm = bmesh.new()
		bmesh.ops.create_icosphere(bm, subdivisions= pd.wsegs,
							diameter= pd.radius1,
							matrix=Matrix(), calc_uvs=True)
		bm.to_mesh(orgmesh.id_data)
		bm.free()
	def abort(self):
		delete_objects([self.owner])

class BsMax_OT_CreateIcosphere(CreatePrimitive):
	bl_idname = "bsmax.createuicosphere"
	bl_label = "Create Icosphere (Create)"
	subclass = Icosphere()

	def create(self, ctx, clickpoint):
		self.subclass.create(ctx)
		self.params = self.subclass.owner.data.primitivedata
		self.subclass.owner.location = clickpoint.view
		self.subclass.owner.rotation_euler = clickpoint.orient
	def update(self, clickcount, dimantion):
		if clickcount == 1:
			self.params.radius1 = dimantion.radius
		if clickcount > 0:
			self.subclass.update()
	def finish(self):
		pass

def icosphere_cls(register):
	c = BsMax_OT_CreateIcosphere
	if register: bpy.utils.register_class(c)
	else: bpy.utils.unregister_class(c)

if __name__ == '__main__':
	icosphere_cls(True)

__all__ = ["icosphere_cls", "Icosphere"]