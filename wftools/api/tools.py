from wftools.core.ToolsType import MainTools

mainTools = MainTools()


# @except_dec()
def transtools(content, to_lang, from_lang):
    return mainTools.transtools(to_lang=to_lang, from_lang=from_lang, content=content)


# @except_dec()
def qrcodetools(url: str, output: str = r'./qrcode_img.png'):
    mainTools.qrcodetools(url, output)


# @except_dec()
def passwordtools(len=8):
    return mainTools.passwordtools(len)


# @except_dec()
def weather():
    mainTools.weather()


# 测试网速
def net_speed_test():
    mainTools.net_speed_test()


# 通过url，获取ip地址
# # @except_dec()
def url2ip(url):
    return mainTools.url2ip(url)


# 通过url，获取ip地址
# @except_dec()
def lottery8ticket():
    mainTools.lottery8ticket()


# @except_dec()
def create_article(theme, line_num=200):
    mainTools.create_article(theme, line_num)


# @except_dec()
def pwd4wifi(len_pwd=8, pwd_list=[]):
    mainTools.pwd4wifi(len_pwd, pwd_list)


def open_soft(soft_path, num):
    mainTools.open_soft(soft_path, num)
