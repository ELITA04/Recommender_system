import pandas as pd
import random
import json

df = pd.read_csv('./Dataset/Employee.csv')
values_event1 = df['Event1'].value_counts().keys().tolist()
counts_event1 = df['Event1'].value_counts().tolist()
values_event2 = df['Event2'].value_counts().keys().tolist()
counts_event2 = df['Event2'].value_counts().tolist()

d1 = {'Events' : values_event1, 'Counts1' : counts_event1}
d2 = {'Events' : values_event2, 'Counts2' : counts_event2}

events_1 = pd.DataFrame(d1, columns=['Events','Counts1'])
events_2 = pd.DataFrame(d2, columns=['Events','Counts2'])

domain_event1_df = df[['Domain', 'Event1']]
domain_event1_df.columns = ['Domain', 'Event']

domain_event2_df = df[['Domain', 'Event2']]
domain_event2_df.columns = ['Domain', 'Event']

domain_event = pd.concat([domain_event1_df, domain_event2_df])
print(f'Len of domain and events : {len(domain_event)}')

grouped = domain_event.groupby('Event')['Domain'].apply(list)

domains = ['Cloud Computing', 'Security', 'Other', 'Coding', 'Python', 'Management', 'IoT', 'Networking', 'Blockchain', 'Java', 'Mobile Applications', 'Finance', 'C++', 'C', 'Development Processes', 'Web Development', 'Higher Education', 'Machine Learning', 'JavaScript', 'Software Architecture', 'Hardware', 'Data Science', 'Artificial Intelligence']
events = ['Internships', 'Expos', 'Competitions', 'Seminars', 'Fests', 'Jobs', 'Talks', 'Courses', 'Certifications', 'Hackathons', 'Trainings', 'Webinars', 'Workshops']

print(f'The number of domains are {len(domains)} and number of events are {len(events)}')

# to create a dataset of exception cases
x_train_exceptions = [
           ['get', 'a', 'system', 'administration', 'certification', 'from', 'purplehat', 'today'],
           ['lockdown', 'special', 'courses', 'on', 'Yedmi', '22', 'hours', 'left', '!'],
           ['codeboost', 'codeathon', 'is', 'live', 'now!']
           ]
        
y_train_exceptions = [
           ['0', '0', 'domain-Other', 'domain-Other', 'event-Certifications', '0', '0', '0'],
           ['0', '0', 'event-Courses', '0', '0', '0', '0', '0', '0'],
           ['domain-coding', 'event-Hackathons', '0', '0', '0']
]

# to represent other-domain we provide a list of words
other = [
         ['System', 'administration'],
         ['Resume', 'building'],
         ['Personality', 'development']
]

#event - Internships
internships_x = [
    ['apply', 'for', 'an', 'internship', 'in'],
    ['good', 'news!', 'internships', 'for'],
    ['Star', 'hiring', 'intern', 'for'],
    ['Intern', 'post', 'in', 'Cloud', 'Counselage', 'for'],
    ['Edifecs', 'hiring', 'intern', 'for'],

]

internships_y = [
    ['0', '0', '0', 'event-Internship', '0'],
    ['0', '0', 'event-Internship', '0'],
    ['0', '0', 'event-Internship', '0'],
    ['event-Internship', '0', '0', '0', '0', '0'],
    ['0', '0', 'event-Internship', '0']
]

#event - expos
expos_x = [
    ['attend', 'a', 'expo', 'on'],
    ['want', 'to', 'attend', 'a', 'expo', 'on'],
    ['expo', 'on', 'the', 'following', 'topic'],
]

expos_y = [
    ['0', '0', 'event-Expo', '0'],
    ['0', '0', '0', '0', 'event-Expo', '0'],
    ['event-Expo', '0', '0', '0', '0'],

]

# event - Competitions
competitions_x = [
    ['there', 'are', 'competitions', 'for'],
    ['attend', 'competitions', 'in'],
    ['open', 'to', 'all', 'Competitions', 'in']
]

competitions_y = [
    ['0', '0', 'event-Competitions', '0'],
    ['0', 'event-Competitions', '0'],
    ['0', '0', '0', 'event-Competitions', '0']
]

# event - Seminars
seminars_x = [
    ['attend', 'free', 'seminars', 'for'],
    ['good', 'news', 'College', 'is', 'hosting', 'a', 'seminar', 'on'],
    ['there', 'is', 'a', 'free', 'seminar', 'hosted', 'by', 'cloud', 'counselage', 'on'],
    ['want', 'to', 'attend', 'a', 'seminar', 'on']
]

seminars_y = [
    ['0', '0', 'event-Seminars', '0'],
    ['0', '0', '0', '0', '0', '0', 'event-Seminar', '0'],
    ['0', '0', '0', '0', 'event-Seminar', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', 'event-Seminar', '0']
]

# event - Jobs
jobs_x = [
    ['apply', 'for', 'a', 'job', 'in'],
    ['good', 'news!', 'full', 'time', 'jobs', 'for'],
    ['Star', 'hiring', 'jobs', 'for'],
    ['Job', 'positions', 'in', 'Cloud', 'Counselage', 'for'],
    ['Edifecs', 'hiring', 'for'],
]

jobs_y = [
    ['0', '0', '0', 'event-Jobs', '0'],
    ['0', '0', '0', '0', 'event-Jobs', '0'],
    ['0', '0', 'event-Jobs', '0'],
    ['event-Jobs', '0', '0', '0', '0', '0'],
    ['0', 'event-Jobs', '0']
]

# events - Talks
talks_x = [
    ['attend', 'a', 'talk', 'on'],
    ['Speaker', 'XYZ', 'to', 'give', 'a', 'talk', 'on'],
    ['Cloud', 'Counselage', 'has', 'arranged', 'a', 'talk', 'by', 'Speaker', 'XYZ', 'on', 'Topics'],
]

talks_y = [
    ['0', '0', 'event-Talk', '0'],
    ['0', '0', '0', '0', '0', 'event-Talk', '0'],
    ['0', '0', '0', '0', '0', 'event-Talk', '0', '0', '0', '0', '0']
]

# event - Courses
courses_x = [
    ['get', 'courses', 'in'],
    ['good', 'news!', 'courses', 'in'],
    ['want', 'to', 'get', 'courses', 'in'],
    ['get', 'the', 'latest', 'courses', 'today', 'in']
]
courses_y = [
    ['0', 'event-Courses', '0'],
    ['0', '0', 'event-Courses', '0'],
    ['0', '0', '0', 'event-Courses', '0'],
    ['0','0', '0', 'event-Courses', '0', '0']
]

# event - Certifications
certifications_x = [
    ['get', 'certified', 'in'],
    ['good', 'news!', 'certifications', 'in'],
    ['want', 'to', 'get', 'certified', 'in'],
    ['get', 'the', 'latest', 'certifications', 'today', 'in']
]

certifications_y = [
    ['0', 'event-Certifications', '0'],
    ['0', '0', 'event-Certifications', '0'],
    ['0', '0', '0', 'event-Certifications', '0'],
    ['0','0', '0', 'event-Certifications', '0', '0']
]

# events - Hackathons
hackathons_x = [
    ['Participate', 'in', 'hackathons', 'in'],
    ['TCS', 'organising', 'hackathons', 'in', 'the', 'feilds', 'of'],
    ['Attend', 'the', 'first', 'ever', 'Hackathon', 'in']
]

hackathons_y = [
    ['0', '0', 'event-Hackathons', '0'],
    ['0', '0', 'event-Hackathons', '0', '0', '0', '0'],
    ['0', '0', '0', '0', 'event-Hackathons', '0']
]

# event - Training
training_x = [
    ['get', 'live', 'training', 'in'],
    ['we', 'are', 'carrying', 'a', '3', 'day', 'training', 'in'],
    ['a', 'unique', 'opporunity', 'to', 'get', 'trained', 'in'],
    ['coaching', 'in']
]

training_y = [
    ['0', '0', 'event-Trainings', '0'],
    ['0', '0', '0', '0', '0', '0', 'event-Trainings', '0'],
    ['0', '0', '0', '0', '0','event-Trainings', '0'],
    ['event-Trainings', '0']
]

#event - Webinar
webinar_x = [
    ['live', 'session', 'on', 'topics', 'like'],
    ['join', 'us', 'for', 'a', 'free', 'webinar', 'on'],
    ['a', 'webinar', 'to', 'kickstart', 'your', 'career', 'in'],
    ['attend', 'live', 'session', 'on']
]

webinar_y = [
    ['event-Webinar', 'event-Webinar', '0', '0', '0'],
    ['0', '0', '0', '0','0', 'event-Webinar', '0'],
    ['0', 'event-Webinar', '0', '0', '0', '0', '0'],
    ['0', 'event-Webinar', 'event-Webinar', '0']
]

#event - Workshops
workshop_x = [
    ['Cloud', 'Counselage', 'offering', 'introductory', 'workshops', 'on'],
    ['Attend', 'workshops', 'on', 'current', 'trending', 'topics', 'like'],
    ['Join', 'TCS', 'for', 'a', 'live', 'workshop', 'on']
]

workshop_y = [
    ['0', '0', '0', '0', 'event-Workshops', '0'],
    ['0', 'event-Workshops', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', 'event-Workshops', '0']
]


x_train = []
y_train = []


def create_training_data(event, X, y):
    for domain in grouped[event]:
        idx = random.randrange(0, len(X))
        x_sent = X[idx]
        y_sent = y[idx]
        # for cases where domain is not specified
        if domain == 'Other':
            x_sent +=  other[random.randrange(len(other))]
            y_sent += ['domain-Other', 'domain-Other']
        else:
            domain_arr = []
            domain_arr = domain.split(' ')
            domain_name = 'domain-' + "".join(domain_arr)
            for word in domain_arr:
                x_sent += [word]
                y_sent += [domain_name]
        x_train.append(x_sent)
        y_train.append(y_sent)



def print_list(x_train, y_train):
    for i in range(len(x_train)):
        if len(x_train[i]) != len(y_train[i]):
            print('Index ', i)
            print(x_train[i])
            print(y_train[i])
            print(f'Len of x {len(x_train[i])} Len of y {len(y_train[i])}')
    
    with open('./Dataset/y_train.json', "w") as f:
        json.dump(y_train, f)
            

def main():
# ['Internships', 'Expos', 'Competitions', 'Seminars', 'Fests', 'Jobs', 'Talks', 'Courses', 'Certifications', 'Hackathons', 'Trainings', 'Webinars', 'Workshops']
    for event in events:
        if event == 'Internships':
            X = internships_x
            y = internships_y
        if event == 'Expos':
            X = expos_x
            y = expos_y
        if event == 'Competitions':
            X = competitions_x
            y = competitions_y
        if event == 'Seminars':
            X = seminars_x
            y = seminars_y
        if event == 'Jobs':
            X = jobs_x
            y = jobs_y
        if event == 'Talks':
            X = talks_x
            y = talks_y
        if event == 'Courses':
            X = courses_x
            y = courses_y
        if event == 'Certifications':
            X = certifications_x
            y = certifications_y
        if event == 'Hackathons':
            X = hackathons_x
            y = hackathons_y
        if event == 'Trainings':
            X = training_x
            y = training_y
        if event == 'Webinar':
            X = webinar_x
            y = webinar_y
        if event == 'Workshops':
            X = workshop_x
            y = workshop_y
        create_training_data(event, X, y)
    print_list(x_train, y_train)
    print('Len of X train : ', len(x_train))
    print('Len of y train : ', len(y_train))
    

if __name__ == "__main__":
    main()





