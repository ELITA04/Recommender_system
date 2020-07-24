import difflib
import numpy as np
import pandas as pd
import spacy
import os
import sys
import re
from pathlib import Path

#Loading model from directory
print("Loading ")
nlp_test = spacy.load(output_dir)

domain = {'Security', 'HigherEducation', 'Hardware', 'Management', 'DevelopmentProcesses', 'SoftwareArchitecture', 'Other', 'WebDevelopment', 'IoT', 'MobileApplications', 'DataScience', 'MachineLearning', 'Blockchain', 'ArtificialIntelligence', 'CloudComputing', 'Networking', 'Finance', 'Coding', 'Java', 'C++', 'Python', 'C', 'JavaScript'}
event = {'Internship', 'Expo', 'Competition', 'Job', 'Talks', 'Courses', 'Certifications', 'Hackathons', 'Trainings', 'Webinars', 'Workshops'}

inp = input("Enter input: ")
temp = inp

# using the model to get Domain and Event names
doc_test = nlp_test(inp)
l = []
for ent in doc_test.ents:
  l.append(ent.label_.split('-')[1])

inp = inp.split(' ')
for word in inp:
  label = difflib.get_close_matches(word, ['Security', 'HigherEducation', 'DataScience', 'MachineLearning', 'Blockchain', 'ArtificalIntelligence', 'Hardware', 'Management', 'Web', 'IOT', 'MobileApplication', 'Coding', 'Java', 'Python', 'C', 'JavaScript', 'Finance', 'Internship', 'Competitions', 'Expos', 'Job', 'Talks', 'Courses', 'Certifications', 'Hackathons', 'Trainings', 'Webinar', 'Workshops'])
  if label != [] and label[0] not in l:
    l.append(label[0])
print(l)
l = set(l)
#seperating domain and events
dom = l.intersection(domain)
dom = list(dom)
ev = l.intersection(event)
ev = list(ev)

#spliting the domain and event names eg. MachineLearning to Machine Learning
domains = []
for _domain in dom:
  word_l  = re.sub( r"([A-Z])", r" \1", _domain).split()
  if len(word_l) == 1:
    domains.append(word_l[0])
  else:
    d = ' '.join(word_l)
    domains.append(d)
print(domains)


events = []
for _event in ev:
  word_l  = re.sub( r"([A-Z])", r" \1", _event).split()
  if len(word_l) == 1:
    events.append(word_l[0])
  else:
    e = ' '.join(word_l)
    events.append(e)
print(events)


# reading domain and events
Employee = pd.read_csv('./EmployeeData/Employee.csv')

#for multiple domain and events
if dom != [] and ev != []:
  for _domain in domains:
    for _event in events:
      res = (Employee.loc[((Employee['Event1'] == _event) & (Employee['Domain'] == _domain)) | (Employee['Event2'] == _event) & (Employee['Domain'] == _domain), 'Name'])
      data = {'Input' : [temp] * len(res), 'Name' : res}
      df = pd.DataFrame(data)
      df.to_csv('./output.csv', mode = 'a', header = False)
elif ev != []:
  # if only events exist 
  for _event in events:
    res = (Employee.loc[((Employee['Event1'] == _event) | (Employee['Event2'] == _event)), 'Name'])
    data = {'Input' : [temp] * len(res), 'Name' : res}
    df = pd.DataFrame(data)
    df.to_csv('./output.csv', mode = 'a', header = False)
elif dom != []:
  for _domain in domains:
    res = Employee.loc[((Employee['Domain']) == _domain), 'Name']
    data = {'Input' : [temp] * len(res), 'Name' : res}
    df = pd.DataFrame(data)
    df.to_csv('./output.csv', mode = 'a', header = False)