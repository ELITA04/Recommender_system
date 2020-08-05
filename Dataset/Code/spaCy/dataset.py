# spaCy has a particular format in which input is given to the dataset
# The format is : (x, {'entities': [(23, 29, 'PRODUCT'), (62, 68, 'PRODUCT'), (309, 315, 'PRODUCT')]

# to create this dataset I have manually considered senteneces from LinkedIn

TRAIN_DATA = []

sent = 'Hello one, hello all We at XYZ College of Engieering and inviting all of you to our E-Hackathon Topic include Machine Learning, Blockchain, IoT and Finance'
sent_list = sent.split(' ')

entity_arr = []

# writing a function to manually annotate each term
for word in sent_list:
  print(word)
  inp = input('Do you want to tag? ')
  if inp == 'y':
    start_idx = sent.find(word) 
    end_idx = start_idx + sent[start_idx:].index(' ') - 1
    tag = input('Enter tag: ')
    tup = (start_idx, end_idx, tag)
    print(tup)
    entity_arr.append(tup)
    #final tuple
    x = (sent, {"entities" : entity_arr})
    TRAIN_DATA.append(x)