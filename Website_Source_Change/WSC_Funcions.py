from urllib.request import urlopen

page_url = "https://clubvillad.ee/"


def get_page_source(url):
    '# Get page source of give website'
    page = urlopen(url).read().decode('utf-8')
    return page


def read_old_source(file, url):
    '# read give html filename source'
    try:
        o_file = open(file, "r", encoding='utf-8')
        return o_file.read()

    except OSError:
        '# when first file does not exist at all, request html and save it then to disk'
        html = get_page_source(url)
        save_source(html)
        return html


def save_source(page):
    '# save html source from funcion of get_page_source()'
    file = open("clubvilla_source.html", "w+", encoding='utf-8')
    file.write(page)


def compare_sources(old_html, new_html):
    '# compare old and new html'
    if old_html == new_html:
        return True
    else:
        return False

'''
print(get_page_source("https://clubvillad.ee/"))
print(read_old_source("clubvilla_source.html", "https://clubvillad.ee"))
save_source(get_page_source("https://clubvillad.ee/"))
'''

'''print(compare_sources(read_old_source("clubvilla_source.html", page_url),
                      get_page_source(page_url)
                      )
      )'''
