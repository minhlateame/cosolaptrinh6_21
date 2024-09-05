str = input()
w=[]
clean_str = str.strip()
clean_str = clean_str.lower()
ws =clean_str.split()
for i in range(0,len(ws)):
    if i==0:
        w.append(ws[0].title())
    else:
        w.append(ws[i].lower())
clean_str=' '.join(w)
clean_str = clean_str.replace(" ,", ",")
clean_str = clean_str.replace(" .", ".")
clean_str = clean_str.replace(" :", ":")
clean_str = clean_str.replace(" ;", ";")
print(clean_str)
