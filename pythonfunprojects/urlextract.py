from urllib.request import urlopen

page=urlopen("https://techieempire.tech")
print(page.headers)