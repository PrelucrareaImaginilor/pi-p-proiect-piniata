import pandas as pd
df = pd.read_csv('./shapescolors.csv')
shapes = df['shape'].values
colors = df['color'].values
file_no = df['file_name'].values
names = df['name'].values
ndc = df['ndc11'].values

def find_name(color, shape):
    name=[]
    for i in range(len(shapes)): #cauta in forme
        if shapes[i] == (" "+shape):
            correct = 0
            for x in color.split(","):
                if x in colors[i].split(", ") or (" "+x) in colors[i].split(", "):
                    correct = correct + 1
            if correct == len(colors[i ].split(", ")):
                if(names[i]=="-"):
                    name.append(ndc[i])
                else:
                    name.append(names[i])
    return name


