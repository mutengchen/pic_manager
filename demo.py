# 读取配置呀
import json

import cv2
import redis
import numpy as np

file = open('params_config')
content = file.read()
redis_config = json.loads(content)

#连接redis
# # 2. 读取数据格式
pool = redis.ConnectionPool(host=redis_config['redis_host'], port=redis_config['redis_port'],
                            db=redis_config['redis_db'], password=redis_config['redis_password'],
                            socket_connect_timeout=30)
r = redis.Redis(connection_pool=pool)

#3.byte[],string转换成json
json_str = str(json_bytes, "utf-8")
res = json.loads(json_str)

#4.利用cv2 将byte[]数组转换成文件流 cv2图片流对象
image = cv2.imdecode(np.asarray(bytearray(buf),dtype='uint8'),cv2.IMREAD_COLOR)

#将cv2对象转换成图片
imgname = f"pedestron_{index}{time.time()}.jpg"
path = os.path.join(ST.SERVERSTATICROOT, self.BASEDIR, imgname)
cv2.imwrite(path, imagefile, [cv2.IMWRITE_JPEG_QUALITY, 60])

#app flask 路由跳转页面
# @frontend.route("/", methods=["GET"])
# def index():
#   return render_template("index.html", capture_list=redis_cam_frame,
#                        config_info=params_config, config_api_res=config, cam_status=cam_status


#5.网络请求get,post
resp = requests.request("POST", url, data=data, files=img, verify=False, timeout=5)
if (resp.status_code == 200):
    print("success push message")
else:
    print(str(resp.status_code) + ":" + resp.text)
#6.多线程
threads = []
t = threading.Thread(target=runRecOnThread, args=(r, redis_pool, m, str(i), config["cam_status_url"], cam_config))
threads.append(t)
for i in range(x):
    threads[i].start()
for i in range(x):
    threads[i].join()
