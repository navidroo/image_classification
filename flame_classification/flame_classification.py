import numpy as np
import h5py
import tensorflow
from os import path

here = path.abspath(path.dirname(__file__))

############################
class FCA():
	""" Base class for Flame Classification Algorithm (FCA) classes.
	"""

	def normalize(arr):
		"""
		Normalize the values within the array (image) to a (0, 1) range.
		The array shape must be (74, 74).
		It sets the NaN values to zero by default.
		"""
		arr[np.isnan(arr)]=0
		
		if arr.shape != (74,74):
			raise ValueError("Image's shape must be (74,74)!")
		else:
			return ((arr - arr.min()) * (1 / (arr.max() - arr.min())))

	def cl_model_load():
		print(here)
		loaded = tensorflow.keras.models.load_model(path.join(here, 'data', 'min_val_loss.h5'),compile=False)
		return loaded
	
	def get_meta():
		"""
		It is used to obtian the meta-data for each image in the original
		dataset.
		"""
		
		with h5py.File(path.join(here, 'data', 'meta_flames_classification.h5'), "r") as meta:
			# List all groups
			print("Keys: %s" % meta.keys())
			a_group_key = list(meta.keys())[0]
			# Get the data
			data_meta = np.array(list(meta[a_group_key]))
		return data_meta
		
	def get_image():
		"""
		It is used to obtian the image array for each image in the original
		dataset.
		"""
		
		with h5py.File(path.join(here, 'data', 'x_flames_classification.h5'), "r") as flame_file:
			# List all groups
			print("Keys: %s" % flame_file.keys())
			a_group_key = list(flame_file.keys())[0]
			
			# Get the data
			image_array = np.array(list(flame_file[a_group_key]))
		return image_array
		
	def get_class_number():
		"""
		It is used to obtian the flame type number for each image in the original
		dataset.
		The flame type in the original dataset is set by the operator.
		
			0: Weak flame
			1: FREI
			2: Stable flame
		"""
		
		with h5py.File(path.join(here, 'data', 'y_flames_classification.h5'), "r") as flame_type:
			# List all groups
			print("Keys: %s" % flame_type.keys())
			a_group_key = list(flame_type.keys())[0]
			
			# Get the data
			class_number = np.array(list(flame_type[a_group_key]))
		return class_number
		
	def get_flame_class():
		"""
		It is used to obtian the flame type for each image in the original
		dataset (i.e. Weak flame, FREI, and stable flame).
		The flame type in the original dataset is set by the operator
		"""
		class_names = ['Weak flame', 'FREI', 'Normal Flame']
		with h5py.File(path.join(here, 'data', 'y_flames_classification.h5'), "r") as flame_class:
			# List all groups
			print("Keys: %s" % flame_class.keys())
			a_group_key = list(flame_class.keys())[0]
			
			# Get the data
			class_number = np.array(list(flame_class[a_group_key]))
			flame_type = [class_names[class_number[i]] for i in range(len(class_number)) ]
		return flame_type