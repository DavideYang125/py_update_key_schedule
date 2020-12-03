import redis

def del_key_data():
    r = redis.Redis(host='', port=6379, decode_responses=True,password='',db=2,)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    r.delete('test1')
    r.delete('test2')

if __name__ == "__main__":
    del_key_data()