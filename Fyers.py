def read_csv(file):
     with open(path,'r+') as file:
    results=[]
    text=file.read()
    for line in text.split('\n'):
          a=line.split(',')
          b=tuple(a)
          results.append(b)
    return results

data=read_csv('airline_csv')

data=data[1:-1] # In order to remove header line and last empty line

names=[]
for i in data:
  names.append(i[1]+","+i[2])

data_dict={}
for i in names:
  if (i in data_dict):
    data_dict[i]+=1
  else:
    data_dict[i]=1

Output1=data_dict

def counts(a):
    max_count=0
    min_count=10**8
    for j,v in a.items():
        if(v>max_count):
            max_count=v
            name_max_count=j
        if(v<min):
            min_count=v
            name_min_count=j

    return max_count, name_max_count, min_count, name_min_count

output=counts(data_dict)
Output2=(output[0],output([1])
Output3=(output[2],output[3])

print(Output1)
print(Output2)
print(Output3)
