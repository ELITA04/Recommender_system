
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random

"""### Reading the original dataset"""

df = pd.read_csv('./data/CCMLEmployeeData.csv')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Name, df.Domain, df.Event1, df.Event2],
               fill_color='lavender',
               align='left'))
])

fig.show()

# Plot the unique domians
values = df['Domain'].value_counts().keys().tolist()
counts = df['Domain'].value_counts().tolist()
d = {'Domain' : values, 'Counts' : counts}
domain_values = pd.DataFrame(d, columns=['Domain','Counts'])
fig = px.pie(domain_values, values= 'Counts', names='Domain',
             title='Value counts of Different Domains',
             hover_data=['Counts'])
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

#Plot the unique events

values_event1 = df['Event1'].value_counts().keys().tolist()
counts_event1 = df['Event1'].value_counts().tolist()
values_event2 = df['Event2'].value_counts().keys().tolist()
counts_event2 = df['Event2'].value_counts().tolist()
d1 = {'Events' : values_event1, 'Counts1' : counts_event1}
d2 = {'Events' : values_event2, 'Counts2' : counts_event2}

print(d1, d2)
events_1 = pd.DataFrame(d1, columns=['Events','Counts1'])
events_2 = pd.DataFrame(d2, columns=['Events','Counts2'])
events = pd.merge(events_1, events_2)
events['Counts'] = events['Counts1'] + events['Counts2']


fig = go.Figure(data=[go.Table(
    header=dict(values=list(['Events', 'Counts']),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[events.Events,  events.Counts],
               fill_color='lavender',
               align='left'))
])

fig.show()

# Plot the unique events

fig = px.pie(events, values= 'Counts', names='Events',
             title='Value counts of Different Events',
             hover_data=['Events', 'Counts'])
# fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

"""Trying mutli-label classification
Step 1 : Making a dataframe consisting of Domains and Events and using this for mutli-label classification.
"""

domain_event1_df = df[['Domain', 'Event1']]
domain_event1_df.columns = ['Domain', 'Event']
fig = go.Figure(data=[go.Table(
    header=dict(values=list(domain_event1_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[domain_event1_df.Domain, domain_event1_df.Event],
               fill_color='lavender',
               align='left'))
])

fig.show()

domain_event2_df = df[['Domain', 'Event2']]
domain_event2_df.columns = ['Domain', 'Event']
fig = go.Figure(data=[go.Table(
    header=dict(values=list(domain_event2_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[domain_event2_df.Domain, domain_event2_df.Event],
               fill_color='lavender',
               align='left'))
])

fig.show()

domain_event = pd.concat([domain_event1_df, domain_event2_df])

fig = go.Figure(data=[go.Table(
    header=dict(values=list(domain_event.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[domain_event.Domain, domain_event.Event],
               fill_color='lavender',
               align='left'))
])

fig.show()

grouped = domain_event.groupby('Event')['Domain'].apply(list)
print(grouped)

