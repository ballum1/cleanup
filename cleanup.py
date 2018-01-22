
df = pd.read_csv("testNEW.csv")
df['idx'] = df.groupby('cluster_id').cumcount()
new_df = df.pivot(index='cluster_id',columns='idx')[['link_score','source_file','sss']]
new_df.to_csv("output1.csv")

