a = [1, 2]
print(a)
a.append(a[-1]+1)
s = "a = " + f"{a}\n"
with open('4.1.py', 'r') as file_r:
    lines = file_r.readlines()[1:]
    lines.insert(0, s)
   
    with open('4.1.py', 'w') as file_w:
        for i in lines:
            file_w.write(i)
    
