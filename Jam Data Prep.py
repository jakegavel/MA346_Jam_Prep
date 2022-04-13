import pandas as pd
data = pd.read_csv('jams.tsv', sep = '\t', on_bad_lines='skip', header = 0)
df = pd.DataFrame(data)
df1 = df.drop_duplicates(subset = ['user_id'])
randuser = df1['user_id'].sample(n = 2000, random_state=1)
df2 = df[df['user_id'].isin(randuser)]
df2 = df2[['user_id', 'artist', 'title']]
df2['song'] = df2["title"] + ', by ' + df2['artist']
df2 = df2[['user_id', 'song']]
df2.to_csv('jam-sample.csv', index = False)

