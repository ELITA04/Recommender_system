import difflib
import numpy as np
import pandas as pd
import spacy
import os
import sys
from pathlib import Path
import re

# **** create a dataframe for input with heading 'InputSent ****


#Loading model from directory
output_dir = './Model'

# read the input csv
df = pd.read_csv('./input.csv')
# read the employee data
Employee = pd.read_csv('./EmployeeData/Employee.csv')
Employee.tail()


print("Loading ")
nlp_test = spacy.load(output_dir)

domain = {'Security', 'HigherEducation', 'Hardware', 'Management', 'DevelopmentProcesses', 'SoftwareArchitecture', 'Other', 'WebDevelopment', 'IoT', 'MobileApplications', 'DataScience', 'MachineLearning', 'Blockchain', 'ArtificialIntelligence', 'CloudComputing', 'Networking', 'Finance', 'Coding', 'Java', 'C++', 'Python', 'C', 'JavaScript'}
event = {'Internship', 'Expo', 'Competitions', 'Jobs', 'Talks', 'Courses', 'Certifications', 'Hackathons', 'Trainings', 'Webinars', 'Workshops'}

i = 0
for sent in df['InputSent']:
  inp = sent
  temp = inp
  # using the model to get Domain and Event names
  doc_test = nlp_test(inp)
  l = []
  for ent in doc_test.ents:
    l.append(ent.label_.split('-')[1])

  inp = inp.split(' ')
  for word in inp:
    # incase the model misses the entity prediction, using get_close_matches as a fail safe
    label = difflib.get_close_matches(word, ['Security', 'Education', 'Data Science', 'Machine Learning', 'Blockchain', 'Artifical Intelligence', 'Hardware', 'Management', 'Web', 'IoT', 'Mobile', 'Coding', 'Java', 'Python', 'C', 'JavaScript', 'Finance', 'Internship', 'Competitions', 'Expo', 'Jobs', 'Talks', 'Courses', 'Certifications', 'Hackathons', 'Trainings', 'Webinars', 'Workshops', 'AI', 'ML'])
    if label != [] and label[0] not in l:
      l.append(label[0])
  print(l)
  l = ['WebDevelopment' if x=='Web' else x for x in l]
  l = ['MobileApplications' if x=='Mobile' else x for x in l]
  l = ['ArtificialIntelligence' if x=='AI' else x for x in l]
  l = ['MachineLearning' if x=='ML' else x for x in l]
  l = set(l)
  
  #seperating domain and events
  dom = l.intersection(domain)
  dom = list(dom)
  ev = l.intersection(event)
  ev = list(ev)

  #refreame domain and events
  domains = []
  for _domain in dom:
    if _domain != 'IoT':
      word_l  = re.sub( r"([A-Z])", r" \1", _domain).split()
      if len(word_l) == 1:
        domains.append(word_l[0])
      else:
        d = ' '.join(word_l)
        domains.append(d)
    else:
      domains.append(_domain)

  events = []
  for _event in ev:
    word_l  = re.sub( r"([A-Z])", r" \1", _event).split()
    if len(word_l) == 1:
      events.append(word_l[0])
    else:
      e = ' '.join(word_l)
      events.append(e)

  final_res = []
  #for multiple domain and events
  if dom != [] and ev != []:
    for _domain in domains:
      for _event in events:
        res = Employee.loc[((Employee['Event1'] == _event) & (Employee['Domain'] == _domain)) | (Employee['Event2'] == _event) & (Employee['Domain'] == _domain), 'Name']
        res = res.tolist()
        final_res += res
  elif ev != []:
    # if only events exist 
    for _event in events:
      res = Employee.loc[((Employee['Event1'] == _event) | (Employee['Event2'] == _event)), 'Name']
      res = res.tolist()
      final_res += res
  elif dom != []:
    for _domain in domains:
      res = Employee.loc[((Employee['Domain']) == _domain), 'Name']
      res = res.tolist()
      final_res += res

  print(final_res)
  if final_res != []:
    listToStr = ' ,'.join([str(elem) for elem in final_res]) 
    print(listToStr)
    output = {'InputSent' : temp, 'Recommend' : listToStr}
    df_output = pd.DataFrame(output, index = [i])
    i = i + 1
    df_output.to_csv('./output.xls', mode = 'a', header = False)

  print('\n')
