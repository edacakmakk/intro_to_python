liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

new_list = []

def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            new_list.append(i)
        
flatten(liste)

print(new_list)