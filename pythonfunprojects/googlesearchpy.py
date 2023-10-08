from googlesearch import search
query="Techie Empire"
for i in search(query,start=0,pause=2):
    print(i)