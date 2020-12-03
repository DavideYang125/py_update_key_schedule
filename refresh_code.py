#更新沙箱密钥

# coding=utf-8
import requests
import xml.dom.minidom as xmldom
import db_handle as db
import redis_handle as redis


#主方法
def main():
    code = get_sandbox_key()
    if (len(code) > 0):
        print(code)
        update_db(code)
        print('数据库修改完成', flush=True)
        redis.del_key_data()
        print('redis处理完成', flush = True)
        print('沙箱密钥更新完成!', flush=True)
    else:
        print('获取沙箱密钥失败', flush=True)


#修改数据库字段
def update_db(code):
    db.update_key(code)


#获取沙箱密钥
'''
返回数据示例
<xml>
  <return_code><![CDATA[SUCCESS]]></return_code>
  <return_msg><![CDATA[ok]]></return_msg>
  <sandbox_signkey><![CDATA[eb610b41040c69c2c3d4474bf2203591]]></sandbox_signkey>
</xml>
'''


def get_sandbox_key():
    url = 'https://api.mch.weixin.qq.com/sandboxnew/pay/getsignkey'
    body='<xml>' \
        '<mch_id></mch_id>' \
        '<nonce_str></nonce_str>' \
        '<sign></sign>' \
        '</xml>'
    r = requests.post(url, data=body.encode('utf-8'))
    if r.status_code == 200:
        domobj = xmldom.parseString(r.text)
        elementobj = domobj.documentElement
        code = elementobj.getElementsByTagName(
            "sandbox_signkey")[0].firstChild.data
        return code
    else:
        return ''


if __name__ == "__main__":
    main()