from urllib.request import urlopen


def get_page_source(url):
    '# Get page source of give website'
    page = urlopen(url).read().decode('utf-8')
    return page


def read_old_source(file):
    '# read give html filename source'
    o_file = open(file, "r", encoding='utf-8')

    return o_file.read()


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



#print(get_page_source("https://clubvillad.ee/"))
#print(read_old_source("clubvilla_source.html"))
#save_source(get_page_source("https://clubvillad.ee/"))
#print(compare_sources(read_old_source("clubvilla_source.html"), get_page_source("https://clubvillad.ee/")))
