import asyncio

'''
async def io_foo(arg):
    print('开始')
    await asyncio.sleep(1)
    print(arg)
    return f'{arg}_end'


def call_back(arg:asyncio.Future):
    print('回调', arg.result())

# 创建事件循环
loop = asyncio.get_event_loop()
# 创建任务列表，如果不需要返回结果则不用使用loop.create_task
tasks = [loop.create_task(io_foo(f'来了来了_{i}')) for i in range(5)]
# tasks = [io_foo(f'来了来了_{i}') for i in range(5)]
for task in tasks:
    # 添加完成后的回调函数，任务将作为参数传入，任务返回的结果可通过task.result()获取到
    task.add_done_callback(call_back)

# 将任务列表转化称协程对象，控制多任务运行，不按顺序来
wait_tasks = asyncio.wait(tasks)
# 开始执行任务直到完成
loop.run_until_complete(wait_tasks)

loop.close()
'''
# ---------------------------------------
# 生产消费模型demo
import asyncio
from threading import Thread
from collections import deque
import random
import time

def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def consumer():
    while True:
        if dq:
            msg = dq.pop()
            if msg:
                asyncio.run_coroutine_threadsafe(thread_example('Zarten'+ msg), new_loop)


async def thread_example(name):
    print('正在执行name:', name)
    await asyncio.sleep(10)
    print('完了：', name)
    return '返回结果：' + name

dq = deque()
new_loop = asyncio.new_event_loop()
loop_thread = Thread(target=start_thread_loop, args=(new_loop,))
loop_thread.setDaemon(True)
loop_thread.start()

consumer_thread = Thread(target=consumer)
consumer_thread.setDaemon(True)
consumer_thread.start()


print('初始化队列')
for j in range(50):
    dq.appendleft(str(j))
print('初始化完成，队列长度', len(dq))
while True:
    i = random.randint(1, 10)
    dq.appendleft(str(i))
    time.sleep(2)