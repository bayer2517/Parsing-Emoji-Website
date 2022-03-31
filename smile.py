from bs4 import BeautifulSoup
import lxml
import json
import requests

# url = "https://emojipedia.org/skype/"
#
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
# #
# req = requests.get(url, headers=headers)
#
# src = req.text
# #print(src) #got website code in panel


##########################################################
# with open("smile.html", "w", encoding="utf-8") as file: # download code as smile.html
#    file.write(src)
##########################################################


###########################################################
# with open("smile.html", encoding='utf-8') as file:
#     src = file.read()
# #print(src) check if it's open.
#
#
# soup = BeautifulSoup(src, "lxml")
# all_emoji_img = soup.find(class_= "emoji-grid").find_all("img")
# all_emoji_a = soup.find(class_= "emoji-grid").find_all("a")
#
# #print(all_emoji_a) # Check for right class and smiles inside
# skype_emoji_dic = {}
# count = 1
# for i in all_emoji_img:
#     emoji_image_name = i.get("alt") # In alt we can find name of smile
#     emoji_image_link = i.get("src") # in img link, but at some point in "src" we need to change to "data-src"
#     if emoji_image_link == "/static/img/lazy.svg":
#         emoji_image_link = i.get("data-src")
#     else:
#         emoji_image_link = i.get("src")
# #    print(f'{emoji_image_name} : {emoji_image_link}')  # Everything fine
# # print("Total emojis is:", count)
#         skype_emoji_dic[emoji_image_name] = emoji_image_link # add everything in list


#         # остановился на том, что надо создать сначала список добавить dict в список а цже потому дальше идти
# Можно сделать def из имени и zip его вместе с emoji description

# emoji_href_dict = {}
# for item in all_emoji_a:
#     name_href = item.get("href")
#     all_emoji_href = "https://emojipedia.org" + item.get("href")
#
#     emoji_href_dict[name_href] = all_emoji_href

# with open("all_href_emoji.json", "w") as file:
#     json.dump(emoji_href_dict, file, indent=4)
###################################################################################

# emoji_json = {}
####################################################################
# with open("all_href_emoji.json") as file:  # opened json file
#     all_emoji_description = json.load(file)
# count = 1
# for emoji_name, emoji_link in all_emoji_description.items():  # replace all symbols to "_"
#     rep = [",", "-", "'", "/"]
#     for item in rep:
#         if item in emoji_name:
#             emoji_name = emoji_name.replace(item, "_")
#     emoji_json[emoji_name] = emoji_link # i decide to change all characters to _, i don't know ehy

# with open("all_emoji_href.json", 'w') as file:
#     json.dump(emoji_json, file, indent=4)

with open("all_emoji_href.json") as file:  # opened json file
    all_emoji_description = json.load(file)

for emoji_name, emoji_link in all_emoji_description.items():
    req = requests.get(url = emoji_link, headers=headers)
    src = req.text

    with open(f"data_emoji/{emoji_name}.html", "w", encoding="utf-8") as file:
        file.write(src)





