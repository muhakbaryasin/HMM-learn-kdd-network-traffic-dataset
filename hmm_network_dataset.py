import os

import numpy as np
from hmmlearn import hmm
import pandas
from time import time

# Class to handle all HMM related processing
class HMMTrainer(object):
	def __init__(self, model_name='GaussianHMM', n_components=4, cov_type='diag', n_iter=1000):
		self.model_name = model_name
		self.n_components = n_components
		self.cov_type = cov_type
		self.n_iter = n_iter
		self.models = []

		if self.model_name == 'GaussianHMM':
			self.model = hmm.GaussianHMM(n_components=self.n_components, 
					covariance_type=self.cov_type, n_iter=self.n_iter)
		else:
			raise TypeError('Invalid model type')

	# X is a 2D numpy array where each row is 13D
	def train(self, X):
		np.seterr(all='ignore')
		self.models.append(self.model.fit(X))

	# Run the model on input data
	def get_score(self, input_data):
		return self.model.score(input_data)

if __name__=='__main__':
	
	# Kolom yang ada dalam dataset
	col_names = ["duration","protocol_type","service","flag","src_bytes",
		"dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
		"logged_in","num_compromised","root_shell","su_attempted","num_root",
		"num_file_creations","num_shells","num_access_files","num_outbound_cmds",
		"is_host_login","is_guest_login","count","srv_count","serror_rate",
		"srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
		"diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
		"dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
		"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
		"dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]
	
	# Load dataset dari file
	dataset = pandas.read_csv("kddcup.data_10_percent_corrected", header=None, names = col_names)
	
	# Menampilkan dataset pada console
	print("Menampilkan dataset pada console: ")
	print(dataset.shape)
	print("Example 20 first rows")
	print(dataset.head(20))
	print(dataset['label'].value_counts())

	# Fitur2 yang diperlukan
	num_features = [
		"duration","src_bytes",
		"dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
		"logged_in","num_compromised","root_shell","su_attempted","num_root",
		"num_file_creations","num_shells","num_access_files","num_outbound_cmds",
		"is_host_login","is_guest_login","count","srv_count","serror_rate",
		"srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
		"diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
		"dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
		"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
		"dst_host_rerror_rate","dst_host_srv_rerror_rate"
	]
	features = dataset[num_features].astype(float)
	
	# Menampilkan fitur dataset pada console
	print("Menampilkan fitur dataset pada console:")
	print(features.shape)
	import pdb; pdb.set_trace()
	
	hmm_models = []

	# Extract label, labelnya normal/attack
	label = subfolder[subfolder.rfind('/') + 1:]

	# Initialize variables
	X = np.array([])
	y_words = []

	# Iterate through the datasets (leaving 1 file for testing in each class)
	# for filename in [x for x in os.listdir(subfolder) if x.endswith('.wav')][:-1]:
	# bagian sini diganti berdasarkan traffic normal sama traffic attack
	# sampling_freq, audio = wavfile.read(filepath)
	# Extract features
	# mfcc_features = mfcc(audio, sampling_freq)
	

	# Append to the variable X
	if len(X) == 0:
		X = mfcc_features
	else:
		X = np.append(X, mfcc_features, axis=0)
	
	# Append the label
	y_words.append(label)

	print 'X.shape =', X.shape
	
	# Train and save HMM model
	hmm_trainer = HMMTrainer()
	hmm_trainer.train(X)
	hmm_models.append((hmm_trainer, label))
	hmm_trainer = None

	# Test files
	input_files = [
			'data/pineapple/pineapple15.wav',
			'data/orange/orange15.wav',
			'data/apple/apple15.wav',
			'data/kiwi/kiwi15.wav'
			]

	# Classify input data
	for input_file in input_files:
		# Read input file
		sampling_freq, audio = wavfile.read(input_file)

		# Extract MFCC features
		mfcc_features = mfcc(audio, sampling_freq)

		# Define variables
		max_score = None
		output_label = None

		# Iterate through all HMM models and pick 
		# the one with the highest score
		for item in hmm_models:
			hmm_model, label = item
			score = hmm_model.get_score(mfcc_features)
			if score > max_score:
				max_score = score
				output_label = label

		# Print the output
		print "\nTrue:", input_file[input_file.find('/')+1:input_file.rfind('/')]
		print "Predicted:", output_label 

