import bpy
from bpy.types import Menu,Operator
from bpy.props import *

# Original code from Ozzkar Sep 2013
# Edit by Nevil July 2019

class BsMax_OT_ViewportBackground(Operator):
	bl_idname = "bsmax.viewport_background"
	bl_label = "3D View Color"
	bl_description = "Cycle 3D view background colors"

	index: IntProperty(default = 1)

	def execute(self, ctx):
		grad = ctx.preferences.themes[0].view_3d.space.gradients
		grad.show_grad = False

		if self.index == 1:
			#black
			grad.high_gradient[0] = 0.0
			grad.high_gradient[1] = 0.0
			grad.high_gradient[2] = 0.0
		elif self.index == 2:
			#7f7f7f - XSI
			grad.high_gradient[0] = 0.498
			grad.high_gradient[1] = 0.498
			grad.high_gradient[2] = 0.498
		elif self.index == 3:
			#a2a2a2 - maya light
			grad.high_gradient[0] = 0.635
			grad.high_gradient[1] = 0.635
			grad.high_gradient[2] = 0.635
		elif self.index == 4:
			#697b8f - maya gradient
			grad.show_grad = True
			grad.gradient[0] = 0.0
			grad.gradient[1] = 0.0
			grad.gradient[2] = 0.0
			grad.high_gradient[0] = 0.412
			grad.high_gradient[1] = 0.482
			grad.high_gradient[2] = 0.561
		elif self.index == 5:
			#dark blue gradient
			grad.show_grad = True
			grad.gradient[0] = 0.251
			grad.gradient[1] = 0.251
			grad.gradient[2] = 0.251
			grad.high_gradient[0] = 0.267
			grad.high_gradient[1] = 0.302
			grad.high_gradient[2] = 0.341
		else:
			#4b4b4b
			grad.high_gradient[0] = 0.294
			grad.high_gradient[1] = 0.294
			grad.high_gradient[2] = 0.294

		if self.index == 5:
			self.index = 0
		else:
			self.index += 1
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# selection menu
class BMAX_PickViewportBackground_MT(Menu):
	bl_label = "Viewport Background"
	bl_description = "3D viewport background color"
	def draw(self, ctx):
		ui = self.layout
		vbg = "bsmax.viewport_background"
		ui.operator(vbg, text="Elsyiun").index = 0
		ui.operator(vbg, text="Black").index = 1
		ui.operator(vbg, text="XSI").index = 2
		ui.operator(vbg, text="Maya Light").index = 3
		ui.operator(vbg, text="Maya Gradient").index = 4
		ui.operator(vbg, text="Grey Blue Gradient").index = 5

def viewportbg_cls(register):
	classes = [BsMax_OT_ViewportBackground]
	for c in classes:
		if register: bpy.utils.register_class(c)
		else: bpy.utils.unregister_class(c)
	return classes

if __name__ == '__main__':
	viewportbg_cls(True)

__all__ = ["viewportbg_cls"]