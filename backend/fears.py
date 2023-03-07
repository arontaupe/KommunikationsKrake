from response_func import chip_response
from video_builder import make_video_array
import pandas as pd  # Load pandas
import random  # generates random chips for me
import numpy as np


def fears_module(intent_name):
	pass


def give_curated_fears():
	df = pd.read_csv('fears_curated.csv')
	fears_curated = np.array(df.fears_curated.values.tolist())
	return fears_curated


def give_curated_resolutions():
	df = pd.read_csv('fears_curated.csv')
	resolutions_curated = np.array(df.resolutions_curated.values.tolist())
	return resolutions_curated


def add_fear(fear):
	df = pd.DataFrame({'fears_collected'      : [fear],
	                   'resolutions_collected': [None]}
	                  )
	df.to_csv("fears_collected.csv", mode='a', index=False, header=False)


def add_fear_and_resolution(fear, resolution):
	df = pd.DataFrame({'fears_collected'      : [fear],
	                   'resolutions_collected': [resolution]}
	                  )
	df.to_csv("fears_collected.csv", mode='a', index=False, header=False)


def add_resolution(resolution):
	df = pd.DataFrame({'fears_collected'      : [None],
	                   'resolutions_collected': [resolution]}
	                  )
	df.to_csv("fears_collected.csv", mode='a', index=False, header=False)


add_fear("Mäuse")
