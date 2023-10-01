import random
import socket
import string
from pathlib import Path

import qrcode
import speedtest  # 测速
from pofile import mkdir
from translate import Translator

# from utils.tools.weather_city_code import WEATHER_CITY_CODE_DIC
from wftools.lib.tools.lottery8ticket import ticket_kinds
# from wftools.lib.tools.pwd4wifi_service import pwd4wifi_service
from wftools.lib.tools.qoute_dict_create_article import create_article_main
from wftools.lib.tools.weather_city_code import WEATHER_CITY_CODE_DIC
from wftools.lib.tools.weather_service import weather_spider


class MainTools():

    def transtools(self, content, to_lang, from_lang='zh'):
        # specifying the language
        translator = Translator(to_lang,from_lang)
        # typing the message
        translation = translator.translate(content)
        # print the translated message
        return  translation

    def qrcodetools(self, url: str, output: str = r'./qrcode_img.png'):
        # Creating object
        # version: defines size of image from integer(1 to 40), box_size = size of each box in pixels, border = thickness of the border.
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # add_date :  pass the input text
        qr.add_data(url)
        # converting into image
        qr.make(fit=True)
        # specify the foreground and background color for the img
        img = qr.make_image(fill='black', back_color='white')
        output_abs_path = Path(output).absolute()
        mkdir(output_abs_path.parent)
        # store the image
        img.save(output_abs_path)

    def passwordtools(self, len):
        """
        @Author & Date  : CoderWanFeng 2022/5/9 11:54
        @Desc  : 随机密码生成器，默认是8位
        @Return  ：
        """
        chars = string.digits + string.ascii_letters + string.punctuation
        pwd = ''.join(random.sample(chars * len, len))
        return pwd

    def weather(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'
        }
        while (True):
            try:
                cityName = input('请输入城市名称(按q/Q键退出)：')
                if cityName == 'q' or cityName == 'Q':
                    break
                cityCode = WEATHER_CITY_CODE_DIC[cityName]  # 得到城市代码
                url = 'http://www.weather.com.cn/weather1d/%d.shtml' % cityCode  # 得到城市天气网址
                weather_spider(url, headers)
            except:
                print('未查到%s城市，请重新输入：' % cityName)

    # 通过url，获取ip地址
    def url2ip(self, url) -> str:
        socket_list = socket.getaddrinfo(url, None, 0, socket.SOCK_STREAM)
        ip_info = socket_list[0][4][0]
        return str(ip_info)

    def lottery8ticket(self):
        '''
        自动生成彩票
        种类代码：

        '''
        while True:
            for num, name_def in ticket_kinds.items():
                print(num, name_def[0])
            kind = input("选择一个种类：")
            if kind == str(0):
                break
            print('*' * 20)
            if not ticket_kinds.get(kind)[1]():
                print('这个规则太复杂了，我们正在开发。如果可以提供建议，请私信：http://python4office.cn/wechat-qrcode')
            else:
                print(f'{ticket_kinds.get(kind)[0]}的号码是 -->> {ticket_kinds.get(kind)[1]()}')
            print('*' * 20)

    def create_article(self, theme, line_num):
        create_article_main(theme, line_num)

    # 破解wifi密码
    def pwd4wifi(self, len_pwd, pwd_list):
        '该方法已废弃，如有疑问，请联系：http://www.python4office.cn/wechat-group/'
        # pwd4wifi_service(len_pwd, pwd_list)

    def net_speed_test(self):
        print("准备测试ing...")
        # 创建实例对象
        test = speedtest.Speedtest()
        # 获取可用于测试的服务器列表
        test.get_servers()
        # 筛选出最佳服务器
        best = test.get_best_server()
        print("正在测试ing...")
        # 下载速度
        download_speed = int(test.download() / 1024 / 1024)
        # 上传速度
        upload_speed = int(test.upload() / 1024 / 1024)
        # 输出结果
        print("下载速度：" + str(download_speed) + " Mbits/s")
        print("上传速度：" + str(upload_speed) + " Mbits/s")
