import aiohttp
import asyncio
import requests
from pyquery import PyQuery as pq
import re
from tqdm import tqdm
# 随机生成请求头
import fake_useragent
from contextvars import ContextVar

# 定义全局上下文管理器
concurrent = ContextVar("concurrent")

# 默认的网站
base_url = "https://wallhaven.cc/search?"

# 存放图片
image_lists = []
# 存放图片地址
real_image_lists = set()

# 代理

async def catch_url(base_url, thing, page, ua):
    print("search:%s page %s ua %s" %(thing,page,ua))
    params = {
        'q': thing,
        'page': str(page)
    }
    headers = {
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': ua
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url, params=params, headers=headers, timeout=10) as r:
                if r.status == 200:
                    print(await r.text())
                    first_param_image_url(await r.text())
    except Exception as e:
        print(e.args)

async def catch_image_url(raw_url, ua):
    print("raw_url:%s",raw_url)
    headers = {
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': ua
    }
    # 获取上下文关键字
    sem = concurrent.get()
    try:
        async with sem:
            async with aiohttp.ClientSession() as session:
                async with session.get(raw_url,headers=headers, timeout=10, ) as r:
                    if r.status == 200:
                        second_param_image_url(await r.text())
    except Exception as e:
        print(e.args)


def first_param_image_url(text):
    doc = pq(text)
    all_images = doc('section[class="thumb-listing-page"] ul li figure a')
    for image in all_images.items():
        try:
            image_lists.append(image.attr.href)
        except Exception as e:
            print(e.args)

def second_param_image_url(text):
    doc = pq(text)
    image = doc('#wallpaper')
    try:
        url = image.attr.src
        if url and len(url) != 0:
            real_image_lists.add(url)
    except Exception as e:
        print(e.args)




async def get_image_url():
    # windows限制最多打开文件数为509
    concurrent.set(asyncio.Semaphore(50))
    ua = fake_useragent.UserAgent()
    tasks = [asyncio.create_task(catch_url(base_url, 'asuna', 1, ua.random)) ]
    await asyncio.wait(tasks, return_when="ALL_COMPLETED")
    print(f"获取url{len(image_lists)}个")
    new_tasks = [asyncio.create_task(catch_image_url(raw_url, ua.random)) for raw_url in image_lists]
    await asyncio.wait(new_tasks, return_when='ALL_COMPLETED')
    print(f"捕获url{len(real_image_lists)}个")
    print(real_image_lists)


if __name__ == "__main__":
    asyncio.run(get_image_url())
    with open('images.txt', 'w') as f:
        for image in real_image_lists:
            f.write(image+'\n')


