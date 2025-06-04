# 🚀 PointNet 3D AI Web API

✅ ทำนายค่า:
- Max Load (N)
- Max Speed (km/h)
- Drag Coefficient

### ⚙️ การใช้งาน (Local)

```bash
pip install -r requirements.txt
python app.py
```

### 🌐 เรียกใช้งาน API

**POST** `/predict`  
**Form-data:** file = model.stl

**Response:**
```json
{
  "max_load_N": 500.0,
  "max_speed_kmh": 120.0,
  "drag_coefficient": 0.32
}
```

### 🚀 Deploy บน Render

1. สมัคร/ล็อกอิน [Render](https://render.com)
2. New Web Service → เชื่อม repo หรือ upload ZIP นี้
3. Start Command: `python app.py`
4. รอ build & deploy เสร็จ → ได้ URL สาธารณะ!

สนุกกับ AI ครับ! ✨
