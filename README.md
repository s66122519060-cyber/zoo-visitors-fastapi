# Zoo Visitors FastAPI (Fiscal Year 2569)

โปรเจกต์ RESTful API สำหรับข้อมูลรายงานสถิติจำนวนผู้เข้าชมสวนสัตว์ ปีงบประมาณ 2569

## 1. เตรียมข้อมูลจริง

1. เปิด https://data.go.th/dataset/zoo-visitors2569
2. ดาวน์โหลดทรัพยากรในรูปแบบ CSV ที่ตรงกับ Resource ID ที่โจทย์กำหนด
3. นำไฟล์ CSV มาใส่ในโฟลเดอร์ `data`
4. เปลี่ยนชื่อไฟล์เป็น `zoo_visitors.csv`

อย่าสร้างข้อมูลตัวอย่างแทนข้อมูลจริง และอย่าใช้ไฟล์ Excel ที่ยังไม่ได้แปลงเป็น CSV โดยเปลี่ยนนามสกุลเฉย ๆ

## 2. ติดตั้งและรันบน Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

ถ้า PowerShell ไม่อนุญาตให้ activate ให้ใช้ Command Prompt แล้วรัน:

```cmd
.venv\Scripts\activate.bat
```

เปิด:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/api/zoo-visitors
- http://127.0.0.1:8000/docs

## 3. ทดสอบด้วย Postman

- Method: GET
- URL: http://127.0.0.1:8000/api/zoo-visitors
- กด Send
- ควรได้ HTTP 200 และ JSON ที่มี `source`, `fiscal_year`, `record_count`, `data`

## 4. GitHub

สร้าง repository เปล่าบน GitHub แล้วใช้คำสั่ง:

```cmd
git init
git add .
git commit -m "Create Zoo Visitors FastAPI"
git branch -M main
git remote add origin https://github.com/ชื่อผู้ใช้/ชื่อrepository.git
git push -u origin main
```

## 5. Deploy บน Render

สร้าง New > Web Service แล้วเชื่อม GitHub repository นี้

- Language: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

หลัง Deploy สำเร็จ:
- `https://ชื่อบริการ.onrender.com/api/zoo-visitors`
- `https://ชื่อบริการ.onrender.com/docs`

หมายเหตุ: ต้อง commit ไฟล์ `data/zoo_visitors.csv` ไปกับ repository เพื่อให้ Render อ่านข้อมูลได้

## Firebase

โปรเจกต์นี้ไม่ใช้ Firebase และไม่ต้องกรอก Firebase URL
