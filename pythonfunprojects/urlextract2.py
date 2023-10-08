from urllib.request import urlopen
page=urlopen("https://techieempire.tech")

sourcecode=page.read()
print(sourcecode)