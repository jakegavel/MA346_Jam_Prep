import pandas as pd
data = pd.read_csv('jams.tsv', sep = '\t', on_bad_lines='skip', header = 0)
df = pd.DataFrame(data)
df = df.drop_duplicates(subset = ['user_id'])
randuser = df['user_id'].sample(n = 2000, random_state=1)
df1 = df[df['user_id'].isin(randuser)]
df1 = df1[['user_id', 'artist', 'title']]
df1['song'] = df1["title"] + ', by ' + df1['artist']
df1 = df1[['user_id', 'song']]
df1.to_csv('jam-sample.csv', index = False)

