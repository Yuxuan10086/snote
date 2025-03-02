from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sealos Cloud MySQL 连接配置
db_config = {
    "host": "dbconn.sealosbja.site",  # Sealos Cloud 提供的 MySQL 地址
    "user": "root",
    "password": "rtg6vg9b",
    "database": "snote",
    "port": 46042
}

# 获取数据库连接
def get_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    return conn, cursor

# 获取导航栏数据
@app.get("/navigation")
def get_navigation(user_id: int):
    conn, cursor = get_db()

    # 获取用户的甘特图
    cursor.execute("SELECT id, name FROM gantt_charts WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
    gantt_charts = cursor.fetchall()

    # 获取用户的每日计划（按日期升序）
    cursor.execute("SELECT id, plan_date FROM daily_plans WHERE user_id = %s ORDER BY plan_date ASC", (user_id,))
    daily_plans = cursor.fetchall()

    conn.close()

    return {
        "navigation": [
            {
                "name": "甘特图",
                "children": [{"id": g["id"], "name": g["name"]} for g in gantt_charts]
            },
            {
                "name": "每日计划",
                "children": [{"id": p["id"], "date": p["plan_date"].strftime("%Y-%m-%d")} for p in daily_plans]
            }
        ]
    }
