import pandas as pd
df = pd.read_csv('./shapescolors.csv')
shapes = df['shape'].values
colors = df['color'].values
file_no = df['file_name'].values
names = df['name'].values
ndc = df['ndc11'].values

def find_name(color, shape):
    corect_indices=[]
    indices = []
    for i in range(len(shapes)):
        if shapes[i] == (" "+shape):
           indices.append(i)
    for i in indices:
        correct = 0
        for x in color.split(","):
            if x in colors[i].split(", "):
                correct = correct + 1
        if correct == len(colors[i ].split(", ")):
            corect_indices.append(i)

    name=[]
    for i in corect_indices:
        if(names[i]=="-"):
            name.append(ndc[i])
        else:
            name.append(names[i])
    return name


