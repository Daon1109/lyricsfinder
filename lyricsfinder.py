import requests
from bs4 import BeautifulSoup

print("Lyrics Finder - powered by Google & Lyricstranslate.com\n")

titleOrigin = input("Song's Title: ")
artistOrigin = input("Artist: ")
if ' ' in titleOrigin:
    titleReplaced = titleOrigin.replace(' ','+')
else:
    titleReplaced = titleOrigin
if ' ' in artistOrigin:
    artistReplaced = artistOrigin.replace(' ','+')
else:
    artistReplaced = artistOrigin

urlString = "https://www.google.com/search?q="+titleReplaced+"+lyrics+"+artistReplaced

#for test
print("\nLink: "+urlString+"\n\n")

response = requests.get(urlString)
source = response.text
soup = BeautifulSoup(source, 'lxml')


body = soup.find('body')

body = body.text
bodySplited1 = body.split('있습니다.')
if bodySplited1[0] == body:
    bodySplited1 = body.split('결과완전일치')
bodySplited2 = bodySplited1[1].split('가사 ©')
print(bodySplited2[0])

# Update: more data
satisfaction = int(input("Satisfied with the result?(0/1): "))
if satisfaction == 0:
    if ' ' in titleOrigin:
        titleReplaced = titleOrigin.replace(' ','-')
    else:
        titleReplaced = titleOrigin
    if ' ' in artistOrigin:
        artistReplaced = artistOrigin.replace(' ','-')
    else:
        artistReplaced = artistOrigin

    re_urlString = "https://lyricstranslate.com/en/"+artistReplaced+"-"+titleReplaced+"-lyrics.html"
    print("\nLink: "+re_urlString+"\n\n")

    re_response = requests.get(re_urlString)
    re_source = re_response.text
    re_soup = BeautifulSoup(re_source, 'lxml')
    re_body = re_soup.find('body')

    re_body = re_body.text
    bodyresplited1 = re_body.split('Proofreading requested')
    if bodyresplited1[0] == re_body:
        print("\n\nLyrics Not Found :(\n\n")
    else:
        bodyresplited2 = bodyresplited1[1].split('Thanks! ❤')
        print(bodyresplited2[0])