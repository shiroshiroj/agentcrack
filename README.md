# Flask Upload API (for Render)

## 📂 結構
- app.py: 主程式
- requirements.txt: 依賴套件
- Procfile: Render 啟動設定

## ⚡ 如何使用

### 1️⃣ 推到 GitHub

把這個專案丟上你的 GitHub Repo

### 2️⃣ Render 設定

- New Web Service
- 連結你的 Repo
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Environment: Python 3.x

完成後 Render 會給你一個 HTTPS API 網址！
