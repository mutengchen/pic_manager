import os

import aiohttp
from tqdm import tqdm
import asyncio
from contextvars import ContextVar
import fake_useragent

# 定义全局上下文管理器
concurrent = ContextVar("concurrent")
# 一次下载大小
chunk_size = 1024
# 代理
# proxies = 'http://localhost:1080'

URL_PATH = 'images.txt'

async def download_image(url, ua):
    print("url:%s",url)
    headers = {
        'cache-control': 'max-age=0',
        'referer': 'https://alpha.wallhaven.cc/',
        'upgrade-insecure-requests': '1',
        'user-agent': ua
    }

    sem = concurrent.get()
    try:
        async with sem:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as resp:
                    # file_size = resp.headers.get('content-length')
                    # if file_size:
                    #     file_size = int(file_size)
                    # else:
                    #     file_size = "未知"
                    name = url.split('/')[-1]
                    path = os.path.join(".","download_pic",name)
                    print("name",path)
                    # pbar = tqdm(unit="B", unit_scale=True, desc=name)
                    with open(path, 'wb') as f:
                        while True:
                            chunk = await resp.content.read(chunk_size)
                            if not chunk:
                                break
                            f.write(chunk)
                        #     pbar.update(chunk_size)
                        # pbar.close()
    except Exception as e:
        print(e.args)

def get_url(url_path=URL_PATH):
    with open(url_path, 'r') as f:
        while True:
            url = f.readline()
            if url:
                yield url.strip('\n')
            else:
                break




async def main():
    # windows限制最多打开文件数为509
    concurrent.set(asyncio.Semaphore(50))
    ua = fake_useragent.UserAgent()
    urls = get_url()
    tasks = [asyncio.create_task(download_image(url, ua.random)) for url in urls]
    await asyncio.wait(tasks, return_when="ALL_COMPLETED")

if __name__ == "__main__":
    asyncio.run(main())
    print("完毕")

