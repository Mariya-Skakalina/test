import re

with open('./text.txt','r') as f:
    strings = f.read()
    # clear_tags = re.sub(r'(\<(/?[^>]+)>)','',strings)
    urls = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-\/]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls_fin = re.subn(urls,"https://p-z-o.com/",strings)
    # print(urls_fin)

with open('./result.txt','w+') as f:
    arr = urls_fin[0].split(',')
    for i in arr:
        f.writelines(i+'\n')