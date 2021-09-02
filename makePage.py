import json

def makeHTML(info):
    name, cover, time, type, download, author = info['name'], info['cover'], info['time'], info['type'], info['download'], info['author']
    string = '''
    <div class="music">
        <div class="music-logo">
            <img class="img" src="{}" alt="">
        </div>
        <div class="music-info">
            <div class="music-name">
                <i class="fas fa-music"></i>&nbsp;&nbsp;{}
            </div>
            <div class="music-desc">
                <i class="fas fa-calendar-day"></i>&nbsp;&nbsp;作曲时间：{}<br/>
                <i class="fas fa-quote-left"></i>&nbsp;&nbsp;分类：{}<br/>
                <i class="fas fa-feather-alt"></i>&nbsp;&nbsp;{}
            </div>
        </div>
        <div class="music-href">
            <a href="{}">
                <button type="button" class="button">下载</button>
            </a>
        </div>
    </div>
    '''.format(cover, name, time, type, author, download)

    return string

with open('base', 'r', encoding='utf-8') as baseFile:
    baseHTML = baseFile.read()
    post = baseHTML.find('insert')

    content = baseHTML[: post]

    jsonFile = open('json/music.json', 'r', encoding='utf-8')
    infos = json.loads(jsonFile.read())
    jsonFile.close()

    for info in infos:
        content += makeHTML(info)

    content += baseHTML[post + len('insert'): ]

    with open('index.html', 'w', encoding='utf-8') as finalFile:
        finalFile.write(content)
