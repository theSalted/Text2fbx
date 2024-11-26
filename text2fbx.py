import bpy
import os
import re

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the array of strings
strings = ["EDIT ME", "CHANGE ME", "MODIFY ME"]

# Set the export directory to be relative to the script's location
export_dir = os.path.join(script_dir, 'Exports')

if not os.path.exists(export_dir):
    os.makedirs(export_dir)

# Clear the scene of all objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Load the Spooky-Yxay.ttf font from the script's location
font_path = os.path.join(script_dir, 'Spooky-Yxay.ttf')

if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font 'Spooky-Yxay.ttf' not found in script directory. Please ensure the font file is in the same folder as this script.")

font = bpy.data.fonts.load(font_path)

for s in strings:
    # Add a text object
    bpy.ops.object.text_add(location=(0, 0, 0))
    obj = bpy.context.object
    obj.data.body = s  # Set the text to the string

    # Set the font to Spooky-Yxay.ttf
    obj.data.font = font

    # Scale the text object by 0.1
    obj.scale = (0.1, 0.1, 0.1)

    # Give it a slight thickness
    obj.data.extrude = 0.05  # Adjust the value as needed

    # Convert the text object to a mesh
    bpy.ops.object.convert(target='MESH')

    # Prepare a safe filename by replacing invalid characters
    filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', s) + '.fbx'
    filepath = os.path.join(export_dir, filename)

    # Select only the current object
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Export the object as an individual FBX file
    bpy.ops.export_scene.fbx(filepath=filepath, use_selection=True)

    # Delete the object before moving to the next string
    bpy.ops.object.delete()