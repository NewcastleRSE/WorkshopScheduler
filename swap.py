import  pandas as pd
data = {'name':['jannetta','danny','mark'],
        'surname':['steyn','watson','turner']}

df = pd.DataFrame(data)
print(df)
print("-------")
# Get first row
row0 = df.iloc[0]
# Get second row
row1 = df.iloc[1]
# print rows to see content
print(row0)
print(row1)
print("-------")

# Make temporary row variable (tmp_row) equal to row0
tmp_row = row0.copy()
# Make row0 equal to row1
row0 = row1
# Make row1 equal to temporary row
row1 = tmp_row

print(row0)
print(row1)
print("--------")
df.iloc[0] = row0
df.iloc[1] = row1
print(df)