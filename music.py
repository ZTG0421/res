#通过id获取网易云歌曲封面
def get_music_cover(id):
    import requests
    from lxml import etree
    url = 'https://music.163.com/song?id={}'.format(id)
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=head)
    html = etree.HTML(response.text)
    cover_url=html.xpath('//img/@data-src')[0]
    return cover_url
