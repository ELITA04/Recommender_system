# Converting existing dataset to Spacy format

import random
import json
import numpy as np
import pandas as pd
import spacy
import warnings
from spacy.util import minibatch, compounding

with open('./CloudProject/data/TRAIN_DATA.json', 'r') as f:
    TRAIN_DATA = json.load(f)
print(TRAIN_DATA)

TRAIN_DATA = [
  ('Intern post in Cloud Counselage for Security Web Development Machine Learning Data Science Networking Python Finance IoT ', {"entities" : [(0, 5, 'event-Internship'), (36, 43, 'domain-Security'), (45, 59, 'domain-WebDevelopment'), (61, 76, 'domain-MachineLearning'), (78, 89, 'domain-DataScience'), (91, 100, 'domain-Networking'), (102, 107, 'domain-Python'), (109, 115, 'domain-Finance'), (117, 119, 'domain-IoT')]}),
  ('good news! internships for Web Development Higher Education Coding Finance C++ Machine Learning Security ', {"entities" : [(11, 21, 'event-Internship'), (27, 41, 'domain-WebDevelopment'), (43, 58, 'domain-HigherEducation'), (60, 65, 'domain-Coding'), (67, 73, 'domain-Finance'), (75, 77, 'domain-C++'), (79, 94, 'domain-MachineLearning'), (96, 103, 'domain-Security')]}),
  ('Edifecs hiring intern for IoT IoT C Cloud Computing Security Cloud Computing ', {"entities" : [(8, 13, 'event-Job'), (15, 20, 'event-Internship'), (26, 28, 'domain-IoT'), (34, 34, 'domain-C'), (36, 50, 'domain-CloudComputing'), (52, 59, 'domain-Security')]}),
  ('Star hiring intern for JavaScript Software Architecture Machine Learning Mobile Applications C++ Security ', {"entities" : [(5, 10, 'event-Job'), (12, 17, 'event-Internship'), (23, 32, 'domain-JavaScript'), (34, 54, 'domain-SoftwareArchitecture'), (56, 71, 'domain-MachineLearning'), (73, 91, 'domain-MobileApplications'), (93, 95, 'domain-C++'), (97, 104, 'domain-Security')]}),
  ('want to attend a expo on Artificial Intelligence IoT Java JavaScript Cloud Computing System administration Coding Management Development Processes Data Science Python Mobile Applications', {"entities" : [(25, 34, 'domain-ArtificialIntelligence'), (36, 47, 'domain-ArtificialIntelligence'), (49, 51, 'domain-IoT'), (53, 56, 'domain-Java'), (58, 67, 'domain-JavaScript'), (69, 73, 'domain-CloudComputing'), (75, 83, 'domain-CloudComputing'), (85, 90, 'domain-Other'), (92, 105, 'domain-Other'), (107, 112, 'domain-Coding'), (114, 123, 'domain-Management'), (125, 135, 'domain-DevelopmentProcesses'), (137, 145, 'domain-DevelopmentProcesses'), (147, 150, 'domain-DataScience'), (152, 158, 'domain-DataScience'), (160, 165, 'domain-Python'), (167, 172, 'domain-MobileApplications'), (174, 185, 'domain-MobileApplications')]}),
  ('attend a expo on C Java Higher Education System administration Blockchain Development Processes Cloud Computing Java Mobile Applications Networking C IoT Security ', {"entities" : [(9, 12, 'event-Expos'), (19, 22, 'domain-Java'), (24, 39, 'domain-HigherEducation'), (41, 61, 'domain-Other'), (63, 72, 'domain-Blockchain'), (74, 94, 'domain-DevelopmentProcesses'), (96, 110, 'domain-CloudComputing'), (117, 135, 'domain-MobileApplications'), (137, 146, 'domain-Networking'), (17, 17, 'domain-C'), (150, 152, 'domain-IoT'), (154, 161, 'domain-Security')]}),
  ('expo on the following topic Web Development Machine Learning IoT Management C  ', {"entities" : [(0, 3, 'event-Expos'), (28, 42, 'domain-WebDevelopment'), (44, 58, 'domain-MachineLearning'), (65, 74, 'domain-Management'), (76, 76, 'domain-C'), (61, 63, 'domain-IoT')]}),
  ('open to all Competitions in Artificial Intelligence Security Mobile Applications Software Architecture Web Development Machine Learning Coding ', {"entities" : [(12, 23, 'event-Competitions'), (28, 37, 'domain-ArtificialIntelligence'), (39, 50, 'domain-ArtificialIntelligence'), (52, 59, 'domain-Security'), (61, 79, 'domain-MobileApplications'), (81, 101, 'domain-SoftwareArchitecture'), (103, 117, 'domain-WebDevelopment'), (119, 134, 'domain-MachineLearning'), (136, 141, 'domain-Coding')]}),
  ('attend competitions in Hardware Mobile Applications JavaScript Security  C Finance ', {"entities" : [(7, 18, 'event-Competitions'), (23, 30, 'domain-Hardware'), (32, 50, 'domain-MobileApplications'), (52, 61, 'domain-JavaScript'), (63, 70, 'domain-Security'), (73, 73, 'domain-C'), (75, 81, 'domain-Finance')]}),
  ('there are competitions for Higher Education Networking Finance Coding Java C Resume building JavaScript Blockchain Python Web Development Personality development Cloud Computing ', {"entities" : [(10, 21, 'event-Competitions'), (27, 42, 'domain-HigherEducation'), (44, 53, 'domain-Networking'), (55, 61, 'domain-Finance'), (63, 68, 'domain-Coding'), (70, 73, 'domain-Java'), (77, 91, 'domain-Other'), (93, 102, 'domain-JavaScript'), (104, 113, 'domain-Blockchain'), (115, 120, 'domain-Python'), (122, 136, 'domain-WebDevelopment'), (138, 160, 'domain-Other'), (162, 176, 'domain-CloudComputing')]}),
  
  ('want to attend a seminar on Management Python Personality development Web Development C++ Cloud Computing Mobile Applications C Higher Education Finance Development Processes ', {"entities" : [(17, 23, 'event-Seminar'), (28, 37, 'domain-Management'), (39, 44, 'domain-Python'), (46, 68, 'domain-Other'), (70, 84, 'domain-WebDevelopment'), (86, 88, 'domain-C++'), (90, 104, 'domain-CloudComputing'), (106, 124, 'domain-MobileApplications'), (126, 126, 'domain-C'), (128, 143, 'domain-HigherEducation'), (145, 151, 'domain-Finance')]}),
  ('there is a free seminar hosted by cloud counselage on Software Architecture Java Finance Security C Python Higher Education JavaScript Machine Learning Blockchain Datascience ', {"entities" : [(16, 22, 'event-Seminar'), (54, 74, 'domain-SoftwareArchitecture'), (76, 79, 'domain-Java'), (81, 87, 'domain-Finance'), (89, 96, 'domain-Security'), (98, 98, 'domain-C'), (100, 105, 'domain-Python'), (107, 122, 'domain-HigherEducation'), (124, 133, 'domain-JavaScript'), (135, 150, 'domain-MachineLearning'), (152, 161, 'domain-Blockchain'), (163, 173, 'domain-DataScience')]}),
  ('good news College is hosting a seminar on C Coding Blockchain Development Processes Finance Higher Education JavaScript Mobile Applications System administration ', {"entities" : [(31, 37, 'event-Seminar'), (10, 16, 'domain-C'), (44, 49, 'domain-Coding'), (51, 60, 'domain-Blockchain'), (62,  82, 'domain-DevelopmentProcesses'), (84, 90, 'domain-Finance'), (92, 107, 'domain-HigherEducation'), (109, 118, 'domain-JavaScript'), (120, 138, 'domain-MobileApplications'), (140, 160, 'domain-Other')]}),
  ('attend free seminars for Cloud Computing Finance Java C++ Management Mobile Applications Coding IoT Higher Education ', {"entities" : [(12, 19, 'event-Seminar'), (25,39, 'domain-CloudComputing'), (41, 47, 'domain-Finance'), (49, 52, 'domain-Java'), (54, 56, 'domain-C++'), (58, 67, 'domain-Management'), (69, 87, 'domain-MobileApplications'), (96, 98, 'domain-IoT'), (100, 115, 'domain-HigherEducation')] }), 
  ('Get a System Administration certification from PurpleHat ', {"entities" : [(6, 26, 'domain-Other'), (28, 40, 'event-Certifications')]}), 
  ('Lockdown special courses on Ydemi. 22 hours left!', {"entities" : [(17, 23, 'event-Courses')]}),
  ('CodeBoost codeathon is live now! ', {"entities" : [(10, 18, 'event-Hackathons')]}),
  ('first Virtual Internship Experience by JPMorgan Chase & Co. through InsideSherpa. Worked on project which used python and typescript for data analysis and data visualisation.', {"entities" : [(111, 116, 'domain-Python'), (122, 131, 'domain-Other'), (137, 149, 'domain-DataScience'), (155, 173, 'domain-DataScience')]}),
  ('Become a Machine Learning and Cloud Expert. Gain hands-on learning experience with Python, Deploying Machine Learning Models, PySpark on Cloud with this program by IIT Madras and upGrad. 9 Months. 380+ Hours of Learning. Online Programs for Working Professionals.', {"entities" : [(9, 15, 'domain-MachineLearning'), (17, 24, 'domain-MachineLearning'), (30, 34, 'domain-CloudComputing'), (83, 89, 'domain-Python'), (91, 99, 'domain-Other'), (126, 132, 'domain-Other'), (228, 235, 'event-Courses')]}),
  ('Finally!!! Ive completed my PG Diploma in Data Science. My sincere thanks to upGrad team and International Institute of Information Technology Bangalore for providing me such a wonderful platform and faculties to enhance my skills.', {"entities" : [(28, 37, 'event-Courses'), (42, 54, 'domain-DataScience')] }),
  
  ('Lenovo is hiring finance & accounting as Senior Financial Analyst at Hongkong having experience of 4 years or more.', {"entities" : [(10, 15, 'event-Job'), (17, 23, 'domain-Finance'), (27, 36, 'domain-Finance')]}),
  ('I always prefer C++ for programming, but that doesnt mean I lack in Python (Basic), it is just a preference. To test the Python skills, I participated in HackerRank skills certifications. ', {"entities" : [(16, 18, 'domain-C++'), (68, 73, 'domain-Python'), (172, 186, 'event-Certifications')]}),
  ('Looking for a Data Scientist with Machine Learning and Algorithm Development experience using R and Python, NumPy, SciPy, Pandas. This is a permanent opportunity in Toronto. Please let me know if you are interested.', {"entities" : [(14, 27, 'domain-DataScience'), (34, 49, 'domain-MachineLearning'), (55, 63, 'domain-Other'), (94, 94, 'domain-Other'), (108, 113, 'domain-Python'), (115, 120, 'domain-Python'), (122, 128, 'domain-Python')]}),
  ('Thanks to Indian Opensource Community For providing such a cloud based internship', {"entities" : [(59, 63, 'domain-CloudComputing'), (71, 80, 'event-Internship')]}),
  ('Just finished the course “Learning SQL Programming”!', {"entities" : [(59, 63, 'domain-CloudComputing'), (71, 80, 'event-Internship')]}),
  ('Python specialisation with honor certificate, provided the fundamentals of python programming.', {"entities" : [(0, 5, 'domain-Python'), (7, 20, 'event-Certifications'), (33, 44, 'event-Certifications'), (75, 80, 'domain-Python'), (82, 93, 'domain-Coding')]}),
  ('Hi everyone - I am looking for a new role in Data Science and Analytics and would appreciate your support.', {"entities" : [(37, 40, 'event-Job'), (45, 56, 'domain-DataScience'), (62, 70, 'domain-DataScience')]}),
  ('Finally i completed my AWS-EKS task , before that i took 2 days training on AWS-EKS under the #worldrecordholder Mr.Vimal Daga sir', {"entities" : [(23, 29, 'domain-Other'), (64, 71, 'event-Trainings')]}),
  ('Smart, Actionable Advice From Top LinkedIn Career And Job Search Professionals By Jack Kelly', {"entities" : [(18, 23, 'event-Webinars'), (54, 56, 'event-Job')]}), 
  ('Talks job Internship competition courses seminars ', {'entities': [(0, 4, 'event-Talks'), (6, 8, 'event-Job'), (10, 19, 'event-Internship'), (21, 31, 'event-Competitions'), (33, 39, 'event-Courses'), (41, 48, 'event-Seminar')]}),

  ('Very helpful sessions by the experienced entrepreneur from all around the world', {"entities" : [(13, 20, 'event-Seminar')]}),
  ('latest episode of our podcast, Machine Learning That Works, we had a great pleasure to talk to Gabriel Preda, a Lead Data Scientist at Endava and a Kaggle Grandmaster.', {"entities" : [(22, 29, 'event-Webinar'), (31, 46, 'domain-MachineLearning')]}),
  ('Glad to let you know that I have been awarded with a Wolfram Award for another worldwide Hackathon fighting COVID19 which was organised by Wolfram and echoAR ', {"entities" : [(89, 97, 'event-Hackathons')]}),
  ('DataEthics4All is hosting an #Ethics4NextGenAI Hackathon on Saturday, August 8th to help BLM with AI in Criminal Justice, Predictive Policing, COVID-19 Contact Tracing.', {"entities" : [(89, 97, 'event-Hackathons')]}),
  ('HCL HACK IITK 2020 - Worlds Top and Indias #1 cybersecurity #hackathon', {"entities" : [(46, 58, 'domain-Security'), (60, 69, 'event-Hackathons')]}),
  ('Excited to share that I am qualified for the final round of #HackWithInfy 2020 Hackathon where I am among the top 100 coders in India to compete in the grand finale.', {"entities" : [(60, 72, 'event-Hackathons'), (79, 87, 'event-Hackathons')]}),
  ('My team The Intimidators is selected for the Tata Crucible Hackathon 2020, a total of 9 teams have been shortlisted in which my team is one of the shortlisted teams from the north zone for the final event of Hackathon.', {"entities" : [(31, 39, 'event-Hackathons')]}),
  ('If you are seeking #knowledge and #training, I can’t recommend #FedVTE highly enough', {"entities" : [(34, 43, 'event-Trainings')]}),
  ('Completed two week online international internship it was on IOT TO PRODUCT DESIGN organised by University of Mauritius and Trans Asian Chambers of Commerce and Industry ,India', {"entities" : [(40, 49, 'event-Internship'), (61, 63, 'domain-IoT')]}),
  ('Our "Five Things Only Experienced Data Scientists Know" meetup will start in 2 hours.', {"entities" : [(34, 48, 'domain-DataScience'), (56, 61, 'event-Webinars')]}),

  ('Urgently looking for a skilled Freelance Web Designer & Developer. Please message me if you are available to start immediately.', {"entities" : [(41, 65, 'domain-WebDevelopment')]}),
  ('looking for a #job in PHP profile, she is fresher, she has recently completed his master, she has good knowledge #HTML #Boostrap #PHP, #LARAVEL, immediate joiner.', {"entities" : [(14, 17, 'event-Job'), (22, 24, 'domain-WebDevelopment'), (82, 88, 'domain-HigherEducation'), (113, 117, 'domain-WebDevelopment'), (119, 127, 'domain-WebDevelopment'), (129, 133, 'domain-WebDevelopment'), (135, 143, 'domain-WebDevelopment')]}),
  ('Hello connections #javascript post If you ever got confused about cloning Objects or Arrays, this post might help you.', {"entities" : [(18, 28, 'domain-JavaScript')]}),
  ('World Blockchain Summit is back! Not in #Dubai, #Singapore or #Amsterdam this time, but online connecting together from around the world.', {"entities" : [(6, 15, 'domain-Blockchain'), (88, 93, 'event-Weminar')] }),
  ('Re-post from yesterday as we are #Hiring for positions of #Technical #BusinessAnalyst urgently.', {"entities" : [(33, 39, 'event-Job'), (58, 67, 'domain-C'), (69, 84, 'domain-Other')]}),
  ('Criteria - 2+ Years experience with "#hardware #TROUBLESHOOTING" ', {"entities" : [(36, 45, 'domain-Hardware')]}),
  ('Hiring Hardware and Software engineers to build the future of Food distribution. Please reach out if you are interested.  #robotics #hiring #IoT #hardware', {"entities" : [(0, 5, 'event-Job'), (7, 14, 'domain-Hardware'), (20, 27, 'domain-SoftwareArchitecture'), (122, 130, 'domain-Hardware'), (132, 138, 'event-Job'), (140, 143, 'domain-IOT')]}),
  ('Dear Students, it gives us immense pleasure to announce that we, Training & Placement Cell, RMD Sinhgad Technical Institutes Campus Warje, Pune-58 organizing the Webinar: AI and Data Science.', {"entities" : [(65, 72, 'event-Trainings'), (76, 84, 'event-Job'), (162, 169, 'event-Webinars'), (171, 172, 'domain-ArtificialIntelligence'), (178, 189, 'domain-DataScience')]}),
  ('Join the Webinar to grab the opportunity to learn about building Career In Cyber Security on July 19, 2020 @ 5 P.M via GoToMeeting.', {"entities" : [(9, 15, 'event-Webinars'), (75, 88, 'domain-Security')]}),
  ('Hello one, hello all We at XYZ College of Engieering and inviting all of you to our E-Hackathon Topic include Machine Learning, Blockchain, IoT and Finance', {"entities" : [(84, 94, 'event-Hackathons'), (110, 126, 'domain-MachineLearning'), (128, 138, 'domain-Blockchain'), (140, 142, 'domain-IoT'), (148, 154, 'domain-Finance')]}),

  ('Internship opporunity for app development, AI, ML, datascience, DL, NLP, IOT ', {'entities': [(0, 9, 'event-Internship'), (26, 41, 'domain-MobileApplications'), (43, 45, 'domain-ArtificialIntelligence'), (47, 49, 'domain-MachineLearning'), (51, 62, 'domain-DataScience'), (64, 66, 'domain-ArtificialIntelligence'), (68, 71, 'domain-ArtificialIntelligence'), (73, 75, 'domain-IoT')]}),
  ('Want to get certified in Blockchain, Cyber security, Python, Java. DOnt worry we got you covered! ', {'entities': [(12, 20, 'event-Certifications'), (25, 35, 'domain-Blockchain'), (43, 51, 'domain-Security'), (53, 59, 'domain-Python'), (61, 65, 'domain-Java')]}),
  ('GoIreland is offering a webinar on Higher Education and masters in Ireland ', {'entities': [(24, 30, 'event-Webinars'), (35, 50, 'domain-HigherEducation'), (56, 62, 'domain-HigherEducation')]}),
  ('Attend a seminar and talk by world renowned expert on Management and coding ', {'entities': [(9, 15, 'event-Seminar'), (21, 24, 'event-Talks'), (54, 63, 'domain-Management'), (69, 74, 'domain-Coding')]}),
  ('Cloud counselage is offering workshops on Java, C and python! ', {'entities': [(29, 37, 'event-Workshops'), (42, 46, 'domain-Java'), (47, 48, 'domain-C'), (53, 58, 'domain-Python')]}),
  ('Design a website using HTML, CSS, javascript and get certified for the same ', {'entities': [(9, 15, 'domain-WebDevelopment'), (23, 27, 'domain-WebDevelopment'), (29, 32, 'domain-WebDevelopment'), (34, 43, 'domain-WebDevelopment'), (53, 61, 'event-Certifications')]}),
  ('Attend a hackathon on Blockchain , AI and IOT ', {'entities': [(9, 17, 'event-Hackathons'), (22, 31, 'domain-Blockchain'), (35, 36, 'domain-ArtificialIntelligence'), (42, 45, 'domain-IOT')]}),
  ('Compete for the utlimate python master ', {'entities': [(0, 6, 'event-Competitions'), (25, 30, 'domain-Python')]}),
  ('Strengthen you coding by participating in C++ and C competitions ', {'entities': [(15, 20, 'domain-Coding '), (42, 44, 'domain-C++'), (50, 50, 'domain-C'), (52, 63, 'event-Competitions')]}),
  ('Trainings in cloud computing, networking and finance by renowned experts for Rs3000/- ', {'entities': [(0, 8, 'event-Trainings'), (13, 28, 'domain-CloudComputing'), (30, 39, 'domain-Networking'), (44, 50, 'domain-Finance')]}),

  ('Apply for a job in datascience, finance, management ', {'entities': [(12, 14, 'event-Job'), (19, 30, 'domain-DataScience'), (32, 39, 'domain-Finance'), (41, 50, 'domain-Management')]}),
  ('Codethon is on! Compete in different domains, web, app, ML, AI, IOT and win exciting prizes ', {'entities': [(0, 7, 'event-Hackathons'), (46, 49, 'domain-WebDevelopment'), (51, 54, 'domain-MobileApplications'), (56, 58, 'domain-MachineLearning'), (60, 62, 'domain-ArtificalIntelligence'), (64, 66, 'domain-IoT')]}),
  ('Courses on Security, cloud computing, networking for 499/- ', {'entities': [(0, 6, 'event-Courses'), (11, 19, 'domain-Security'), (21, 36, 'domain-CloudComputing'), (38, 47, 'domain-Networking')]}),
  ('Trainings on resume building ', {'entities': [(0, 8, 'event-Trainings'), (13, 27, 'domain-Other')]}),
  ('Webinar on resume building ', {'entities': [(0, 6, 'event-Webinar'), (11, 25, 'domain-Other')]}),
  ('Intern for XYZ company as a web developer ', {'entities': [(0, 5, 'event-Internship'), (28, 40, 'domain-WebDevelopment')]}),
  ('seminar for higher studies ', {'entities': [(0, 6, 'event-Seminar'), (12, 25, 'domain-HigherEducation')]}),
  ('Workshops on game development ', {'entities': [(0, 8, 'event-Workshops'), (13, 28, 'domain-C++')]}),
  ('Flutter and android developer required urgently for job ', {'entities': [(0, 6, 'domain-MobileApplications'), (12, 28, 'domain-MobileApplications'), (52, 54, 'event-Job')]}),
  ('Machine Learning using Javascript. Apply today! ', {'entities': [(0, 15, 'domain-MachineLearning'), (23, 33, 'domain-JavaScript')]}),

  ('Security Higher Education Masters Management Resume building Internships Expos Competitions Compete ', {'entities': [(0, 7, 'domain-Security'), (9, 24, 'domain-HigherEducation'), (26, 32, 'domain-HigherEducation'), (34, 43, 'domain-Management'), (45, 59, 'domain-Other'), (61, 71, 'event-Internship'), (73, 77, 'event-Expos'), (79, 90, 'event-Competitions'), (92, 98, 'event-Competitions')]}),
  ('React, ML, AI, IOT, Blockchain, App development ', {'entities': [(0, 5, 'domain-WebDevelopment'), (7, 9, 'domain-MachineLearning'), (11, 13, 'domain-ArtificialIntelligence'), (15, 18, 'domain-IoT'), (20, 30, 'domain-Blockchain'), (32, 46, 'domain-MobileApplications')]}),
  ('Courses, seminar, webinar on cloud computing, networking and finance', {'entities': [(0, 7, 'event-Courses'),(9, 16, 'event-Seminar'),(18, 24, 'event-Webinars'),(29, 44, 'domain-CloudComputing'),(46, 55, 'domain-Networking'), (61, 67, 'domain-Finance')]}),
  ('Hackathon on coding python java C javascript ', {'entities': [(0, 8, 'event-Hackathons'), (13, 18, 'domain-Coding'), (20, 25, 'domain-Python'), (27, 30, 'domain-Java'), (32, 32, 'domain-C'), (34, 43, 'domain-JavaScript')]}),
  ('Develop your skills by taking courses and get certified for the same ', {'entities': [(13, 18, 'domain-Other'), (30, 36, 'event-Courses'), (46, 54, 'event-Certifications')]})
]

random.shuffle(TRAIN_DATA)

"""### Define our variables"""

model = None
n_iter = 500

"""### Loading the model
- if existing model present ? load : en_model
"""

if model is not None:
  nlp = spacy.load(model) #load exisitng model
  print(f'Loaded model {model}')
else:
  nlp = spacy.blank('en') #create blank language class
  print('Creating a blank en model')

"""### create the built-in pipeline components and add them to the pipeline"""

if 'ner' not in nlp.pipe_names:
  ner = nlp.create_pipe('ner')
  nlp.add_pipe(ner, last = True)
else:
  ner = nlp.get_pipe('ner')

"""## Training the recognizer
- Add labels
- Add pipes
"""

TRAIN_DATA

for _, annotations in TRAIN_DATA:
  for ent in annotations.get('entities'):
    ner.add_label(ent[2])

#get the names of other pipes to disable during training
pipe_exceptions = ['ner', 'trf_wordpiecer', 'trf_tok2vec']
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*other_pipes), warnings.catch_warnings():
  #show warning for misaligned entity spans once
  warnings.filterwarnings('once', category=UserWarning, module = 'spcay')

  #reset and initialize the weights randomly
  #training the model
  if model is None:
    nlp.begin_training()
  for itn in range(n_iter):
    random.shuffle(TRAIN_DATA)
    losses = {}
    #batch up using spacys minibatch
    batches = minibatch(TRAIN_DATA, size = compounding(4.0, 32.0, 1.001))
    for batch in batches:
      texts, annotations = zip(*batch)
      nlp.update(texts, annotations, drop = 0.5, losses = losses)
    print(losses)

# test the trained model
for text, _ in TRAIN_DATA:
  doc = nlp(text)
  print("Entities ", [(ent.text, ent.label_) for ent in doc.ents])

sent = "first Virtual Internship Experience by JPMorgan Chase & Co. through InsideSherpa. Worked on project which used python and typescript for data analysis and data visualisation."
doc = nlp(sent)
print("Entities ", [(ent.text, ent.label_) for ent in doc.ents])

