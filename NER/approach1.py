"""
Approach 1
Dataset built using domain and event name in employee.csv
This is then fed to BERT model
"""

# Commented out IPython magic to ensure Python compatibility.
# %reload_ext autoreload
# %autoreload 2
# %matplotlib inline
import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

import ktrain
from ktrain import text
import json

with open('./x_train.json', 'r') as f:
    x_train = json.load(f)

print(f'Length of x_train : {len(x_train)}')

with open('./y_train.json', 'r') as f:
    y_train = json.load(f)

print(f'Length of y_train : {len(y_train)}')

(trn, val, preproc) = text.entities_from_array(x_train, y_train)

text.print_sequence_taggers()

WV_URL='https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.nl.300.vec.gz'
model = text.sequence_tagger('bilstm-bert', preproc, bert_model='bert-large-cased', wv_path_or_url=WV_URL)

learner = ktrain.get_learner(model, train_data = trn, val_data = val, batch_size = 64)

learner.lr_find()

learner.lr_plot()

learner.fit(1e-2, 1, cycle_len=1)

learner.validate()

predictor = ktrain.get_predictor(learner.model, preproc)

predictor.predict('Cloud counselage seminar in Data Science')

