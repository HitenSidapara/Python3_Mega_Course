# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get("https://www.themoviedb.org/discover/movie")
# c = r.content
#
# soup = BeautifulSoup(c,"html.parser")
#
# all = soup.find_all("div",{"class":"item poster card"})
# # print(all)
# # print(len(all))
#
# for item in all:
#     data = item.find("a",{"class":"result"})
#     print(data)
