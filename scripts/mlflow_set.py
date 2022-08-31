# Get url from DVC
import warnings
import mlflow
import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
import dvc.api

# path='data/AdSmartABdata.csv'
# repo='/home/jds98/10 Academy/Week 2/a-b-hypothesis-for-ad-campaign-peformance-measurement'
# version='v1'

# data_url = dvc.api.get_url(
#	path=path,
#	repo=repo,
#	rev=version
#	)
	
mlflow.set_experiment('mlops-abtest')


if __name__ == "__main__":
	warnings.filterwarnings("ignore")
	
	# Log a parameter (key-value pair)
	log_param("param1", randint(0, 100))

	# Log a metric; metrics can be updated throughout the run
	log_metric("foo", random())
	log_metric("foo", random() + 1)
	log_metric("foo", random() + 2)

	# Log an artifact (output file)
	if not os.path.exists("outputs"):
		os.makedirs("outputs")
#	with open("outputs/test.txt", "w") as f:
#		f.write("hello world!")
	log_artifacts("outputs")
	
	# Read data
#	data = pd.read_csv(data_url, sep=",")
	
#	# Log data params
#	mlflow.log_param('data_url', data_url)
#	mlflow.log_param('data_version', version)
#	mlflow.log_param('input_rows', data.shape[0])
#	mlflow.log_param('inputs_cols', data.shape[1] 

