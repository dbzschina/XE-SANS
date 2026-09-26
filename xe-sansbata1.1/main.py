from packaging.utils import is_normalized_name

import gonen
import time
import importlib.util
import os
import base64

# ===== 新增：无密钥 字符加密/解密函数 =====
def text_encrypt(text):
    b_data = text.encode("utf-8")
    encode_bytes = bytes([x ^ 0x33 for x in b_data])
    return base64.b64encode(encode_bytes).decode("utf-8")

def text_decrypt(enc_str):
    try:
        decode_bytes = base64.b64decode(enc_str)
        raw_bytes = bytes([x ^ 0x33 for x in decode_bytes])
        return raw_bytes.decode("utf-8")
    except:
        return "解密失败"
# ========================================

log_module_path = os.path.join(os.path.dirname(__file__), 'Rz.py')
spec = importlib.util.spec_from_file_location("Rz", log_module_path)
log_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(log_module)

op = False
log_monitor = log_module.monitor

sr=input('按任意键继续...')
if sr == 'su':
    op = True
else:
    time.sleep(1)
if not op:
    print('xe-sans bata A1.1update1')
    print('如有疑问，请输入\'help\'')
else:
    print('xe-sans bata 1.1update1 管理员')
    print('如有疑问，请输入\'help\'')

while True:
    if not op:
        sr=input('>>')
    else:
        sr=input('$>>')
    if sr == 'help':
        if not op:
            gonen.helph()
            log_monitor.info('用户以User权限打开了帮助文档')
        else:
            gonen.help()
            log_monitor.info('用户以管理员权限打开了帮助文档')
    elif sr == 'calc':
        log_monitor.info('用户打开了计算器')
        sza = float(input('数字一:'))
        log_monitor.info(f'用户输入了数字一: {sza}')
        szb = float(input('数字二:'))
        log_monitor.info(f'用户输入了数字二: {szb}')
        zf = input('符号:')
        log_monitor.info(f'用户输入了符号: {zf}')
        sc = gonen.calac(sza, szb, zf)
        print(f'结果:{sc}')
        if log_monitor.is_active():
            log_monitor.info(f'计算器: {sza} {zf} {szb} = {sc}')
    elif sr == 'us':
        if not op:
            time.sleep(0.5)
            log_monitor.info('用户已经是User，无法降权')
        else:
            var = op = False
            log_monitor.info('用户关闭了管理员权限')
    elif sr == 'log':
        if log_monitor.is_active():
            print('日志监测已在运行')
        else:
            if log_monitor.start():
                print('日志监测已启动')
                log_monitor.info('日志系统已就绪')
            else:
                print('日志监测启动失败')
    elif sr == 'quit':
        if log_monitor.is_active():
            log_monitor.info('程序退出')
            time.sleep(5)
            log_monitor.stop()
        break
    # 新增：字符加密命令
    elif sr == 'enc':
        log_monitor.info("执行字符加密")
        content = input("请输入待加密内容：")
        res = text_encrypt(content)
        print("加密结果：", res)
        log_monitor.info(f"加密 | 原文:{content} 密文:{res}")
    # 新增：字符解密命令
    elif sr == 'dec':
        log_monitor.info("执行字符解密")
        content = input("请输入密文：")
        res = text_decrypt(content)
        print("解密结果：", res)
        log_monitor.info(f"解密 | 原文:{content} 解密文:{res}")
    elif sr == "exit":
        if log_monitor.is_active():
            log_monitor.info('程序退出')
            time.sleep(5)
            log_monitor.stop()
        break
    elif sr == "kill":
        while True:
            kill = input("kill-|->")
            log_monitor.info('kill')
            if kill == 'log':
                print("kill |kill -log")
                log_monitor.error("EXIT>kill in cmd-1")
                time.sleep(1)
                log_monitor.error("EXIT>EXIT")
                time.sleep(2)
                log_monitor.stop()
            elif kill == 'cmd-1':
                time.sleep(2)
                log_monitor.info("无权限")
            elif kill == '-help':
                print("""
    log   EXIT log
    cmd-1 
    help
    kill  EXIT""")
            elif kill == 'kill':
                break
    elif sr == "":
        print("", end="")
    else:
        print(f"未知{sr}")
        log_monitor.warning(f"未知{sr}")