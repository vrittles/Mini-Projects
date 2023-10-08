import pyshorteners
url=input("Enter the url:")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)