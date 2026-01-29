from dotenv import load_dotenv
import os
import mysql.connector
import json

# --- 1. Load biến môi trường ---
load_dotenv(dotenv_path=r"C:\Code\Ky5\SEG\Crawl\database\.env")

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DB")

# --- 2. Kết nối MySQL ---
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
cursor = conn.cursor()

# --- 3. Tạo database nếu chưa có ---
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
conn.database = database

# --- 4. Tạo bảng mới theo cấu trúc JSON processed ---
create_table_query = """
CREATE TABLE IF NOT EXISTS law_chunks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    law_id VARCHAR(50),
    chunk_num INT,
    document_type VARCHAR(100),
    issuing_agency TEXT,
    issue_date DATE NULL,
    title TEXT,
    source_url TEXT,
    raw_title TEXT,
    category VARCHAR(255),
    chunk LONGTEXT,
    INDEX (law_id),
    INDEX (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
cursor.execute(create_table_query)

# --- 5. Đọc file JSON processed ---
with open(r"C:\Code\Ky5\SEG\Crawl\Dataprocessing\Process\tvpl_congvan3days_processedv6.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- 6. Chèn dữ liệu vào bảng ---
insert_query = """
INSERT INTO law_chunks 
(law_id, chunk_num, document_type, issuing_agency, issue_date, title, source_url, raw_title, category, chunk)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

count = 0
for item in data:
    law_id = item.get("law_id")
    chunk_num = item.get("chunk_num")
    document_type = item.get("document_type")
    issuing_agency = item.get("issuing_agency")
    issue_date = item.get("issue_date")
    title = item.get("title")
    source_url = item.get("source_url")
    raw_title = item.get("raw_title")
    category = item.get("category")
    chunk = item.get("chunk")

    cursor.execute(insert_query, (
        law_id,
        chunk_num,
        document_type,
        issuing_agency,
        issue_date,
        title,
        source_url,
        raw_title,
        category,
        chunk
    ))
    count += 1

conn.commit()
cursor.close()
conn.close()

print(f"✅ Đã tạo database, bảng và chèn {count} dòng dữ liệu thành công.")
