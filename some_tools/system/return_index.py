def unique_index(L,e):
    index = []
    for (i,j) in enumerate(L):
        if j == e:
            index.append(i)
    return index
label = [1,2,3,3,2,1]
index = unique_index(label,0)
print(index)