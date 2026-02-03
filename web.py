# -*- coding: utf-8 -*-

import json
import time
import logging
from datetime import datetime
from flask import Flask, request, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# -------------------------- 全局配置 & 常量 --------------------------
SERVER_VERSION = "1.0.0 Alpha"
RECOMMANDED_APP_VERSION = "1.3.0.2"
SHARED_TOKEN = "T_CrackedByBobH233"
SHARED_KEY = "UsrTjEVxwRaQsvV5hD8I3Db8zrkjuavD/O8hJcVLUOkDimJc6ShgOQEzV5srpEPcOL63J2chFQA="
SHARED_USER_ID = "BobH233LoveLerist"
USE_VERIFICATION = False  # 关闭密码验证


# -------------------------- 日志配置 (复刻原 Logger.js 功能) --------------------------
def setup_logger():
    # 创建 logs 目录（如果不存在）
    import os
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    # 日志文件名：按日期命名
    log_filename = datetime.now().strftime("%Y-%m-%d") + ".txt"
    log_path = os.path.join("Logs", log_filename)

    # 配置日志格式
    log_format = "[%(asctime)s][%(levelname)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # 配置日志处理器（控制台 + 文件）
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


# 初始化日志
logger = setup_logger()


# -------------------------- 核心业务逻辑 --------------------------
def get_current_timestamp():
    """获取当前时间戳（毫秒）"""
    return int(time.time() * 1000)


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def handle_all_get(path):
    """处理所有 GET 请求，返回服务器版本"""
    return f"FakeLocationServer @ {SERVER_VERSION}"


@app.route('/FakeLocation/user/login', methods=['POST'])
def handle_login():
    """处理登录请求"""
    req_body = request.get_json() or {}
    app_version = req_body.get('versionName', 'unknown')

    # 版本校验警告
    if app_version != RECOMMANDED_APP_VERSION:
        logger.warning(
            f"Login request shows the version of the app is {app_version}. "
            f"However, version {RECOMMANDED_APP_VERSION} is recommanded."
        )

    # 打印登录信息
    username = req_body.get('loginName', 'unknown')
    password = req_body.get('loginPwd', 'unknown')
    device_model = req_body.get('deviceModel', 'unknown')
    logger.info(f"[ device: {device_model} ] Username = {username}, password = {password} login!")

    # 构造响应（忽略密码验证）
    if not USE_VERIFICATION:
        response_data = {
            "body": {
                "regtime": get_current_timestamp() - 1000 * 60 * 60,
                "proindate": get_current_timestamp() + 1000 * 60 * 60 * 24 * 365,
                "createTime": get_current_timestamp() - 1000 * 60 * 60 - 1,
                "loginType": "email",
                "loginName": "BobH" + "Crack",
                "updateTime": 0,
                "type": 1,
                "userId": SHARED_USER_ID,
                "key": SHARED_KEY,
                "token": SHARED_TOKEN
            },
            "code": 200,
            "returnTime": get_current_timestamp(),
            "success": True
        }
        return json.dumps(response_data, ensure_ascii=False)
    return jsonify({"code": 401, "success": False})


@app.route('/FakeLocation/user/checkPwdExist', methods=['POST'])
@app.route('/FakeLocation/user/checkUserExist', methods=['POST'])
def handle_check_exist():
    """处理用户/密码存在性检查"""
    logger.info("checkExist request.")
    response_data = {
        "body": True,
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return json.dumps(response_data, ensure_ascii=False)


@app.route('/Notice/getNotices', methods=['POST'])
def handle_get_notices():
    """处理获取公告请求"""
    logger.info("getNotices request.")
    response_data = [
        {
            "content": "<p><strong>这是由BobH破解的FakeLocationApp的服务端发送的消息</strong></p>\r\n\r\n<p><strong>请勿将此软件用于非法用途，请勿用于出售或非法盈利</strong></p>\r\n\r\n",
            "createTime": 0,
            "flavor": "*",
            "id": "00008",
            "isAvailable": True,
            "isNeedAgree": True,
            "language": "*",
            "needAgree": True,
            "title": "破解说明",
            "type": "text",
            "weight": 100001
        }
    ]
    return json.dumps(response_data, ensure_ascii=False)


@app.route('/Ads/getAds', methods=['POST'])
def handle_get_ads():
    """处理获取广告请求"""
    logger.info("getAds request.")
    response_data = [
        {
            "available": True,
            "createTime": 0,
            "intervalTime": 30000,
            "isAvailable": True,
            "isRandom": False,
            "language": "*",
            "provider": "BobH",
            "random": False,
            "texts": "此软件已经连接破解版服务器，无需再进行购买即可免费不限制使用",
            "urls": "#",
            "weight": 3
        },
        {
            "available": True,
            "createTime": 0,
            "intervalTime": 16000,
            "isAvailable": True,
            "isRandom": False,
            "language": "*",
            "provider": "BobH",
            "random": False,
            "texts": "已经解锁了软件的全部应用模拟功能，不再有特定应用无法使用的问题",
            "urls": "#",
            "weight": 2
        }
    ]
    return json.dumps(response_data, ensure_ascii=False)


@app.route('/FakeLocation/goods/getRenewalGoodsList', methods=['POST'])
def handle_get_renewal_goods_list():
    """处理获取续费商品列表"""
    logger.info("getRenewalGoodsList request.")
    response_data = {
        "body": [
            {
                "createTime": 0,
                "description": "",
                "id": "0011",
                "isAvailable": 1,
                "locale": "*",
                "name": "永久使用无限制",
                "price": 0,
                "priceUnit": "¥",
                "recommend": "BobH",
                "updateTime": 0,
                "value": 30,
                "weight": 4
            }
        ],
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return json.dumps(response_data, ensure_ascii=False)


@app.route('/FakeLocation/app/getAppConfigs', methods=['POST'])
def handle_get_app_configs():
    """处理获取APP配置（解锁所有功能）"""
    logger.info("getAppConfigs request.")
    response_data = {
        "body": {
            "createTime": get_current_timestamp(),
            "disabledApps": [],
            "disabledFuncs": [],
            "disabledInfos": [],
            "isAllowRun": 1,
            "isAvailable": 1,
            "notice": "",
            "updateTime": 0
        },
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return json.dumps(response_data, ensure_ascii=False)


@app.route('/FakeLocation/version/checkApkUpdate', methods=['POST'])
def handle_check_apk_update():
    """处理版本更新检查"""
    logger.info("checkApkUpdate request.")
    req_body = request.get_json() or {}
    version_code = req_body.get('versionCode', 0)
    response_data = {
        "code": int(version_code),
        "message": "??????",
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return json.dumps(response_data, ensure_ascii=False)


@app.route('/FakeLocation/user/get', methods=['POST'])
def handle_user_get():
    """处理用户信息获取"""
    logger.info("userget request.")
    response_data = {
        "body": {
            "regtime": get_current_timestamp() - 1000 * 60 * 60,
            "proindate": get_current_timestamp() + 1000 * 60 * 60 * 24 * 365,
            "createTime": get_current_timestamp() - 1000 * 60 * 60 - 1,
            "loginType": "email",
            "loginName": "BobH" + "Crack",
            "updateTime": 0,
            "type": 1,
            "key": SHARED_KEY,
            "token": SHARED_TOKEN
        },
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return json.dumps(response_data, ensure_ascii=False)


# -------------------------- 启动服务器 --------------------------
if __name__ == '__main__':
    logger.info(f"Server running at http://0.0.0.0:8000!")
    # 启动 Flask 服务器（监听所有网卡的 8000 端口，调试模式关闭）
    app.run(host='0.0.0.0', port=8000, debug=False)