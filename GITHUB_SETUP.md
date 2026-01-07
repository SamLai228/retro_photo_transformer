# GitHub 上傳指南

## 準備上傳到 GitHub

### 1. 確認敏感檔案已被忽略

執行以下命令確認 `.env` 和其他敏感檔案不會被上傳：

```bash
git status
```

您應該**不會**看到以下檔案：
- `.env` (包含 API Key)
- `venv/` (虛擬環境)
- `output/` (輸出圖片)
- `*.jpg`, `*.png` (圖片檔案)
- 任何包含 `key`, `secret`, `credentials` 的檔案

### 2. 確認要上傳的檔案

應該會看到以下檔案：
- `.env.example` (範例檔案，安全)
- `.gitignore`
- `README.md`
- `LICENSE`
- `requirements.txt`
- `app.py`
- `streamlit_app.py`
- `retro_transformer.py`
- `run_app.sh`
- `.streamlit/config.toml`

### 3. 第一次提交

```bash
# 添加所有檔案
git add .

# 檢查要提交的檔案（確認沒有敏感檔案）
git status

# 提交
git commit -m "Initial commit: 1980年代復古照片轉換應用程式"

# 連接到 GitHub 遠端倉庫（替換為您的倉庫 URL）
git remote add origin https://github.com/your-username/retro_photo_transformer.git

# 推送到 GitHub
git push -u origin main
```

### 4. 重要提醒

⚠️ **在推送之前，請再次確認：**

1. `.env` 檔案**不會**被上傳
2. 沒有任何 API Key 或敏感資訊在程式碼中
3. `output/` 目錄中的圖片**不會**被上傳
4. 虛擬環境 `venv/` **不會**被上傳

### 5. 如果已經意外提交了敏感檔案

如果發現敏感檔案已經被提交，請執行：

```bash
# 從 Git 歷史中移除 .env（但保留本地檔案）
git rm --cached .env

# 提交這個變更
git commit -m "Remove .env from tracking"

# 推送到 GitHub
git push
```

**注意**：如果敏感資訊已經被推送到 GitHub，您需要：
1. 立即在 GitHub 上刪除該檔案
2. 重新生成您的 API Key
3. 更新 `.env` 檔案中的新 API Key

### 6. 驗證上傳

上傳後，在 GitHub 上檢查：
- ✅ `.env.example` 存在
- ❌ `.env` **不存在**
- ❌ `venv/` **不存在**
- ❌ `output/` **不存在**
- ✅ 所有程式碼檔案都存在

## 安全檢查清單

- [ ] `.env` 檔案不在 Git 追蹤中
- [ ] `.env.example` 已上傳（作為範例）
- [ ] 程式碼中沒有硬編碼的 API Key
- [ ] `venv/` 目錄不在 Git 追蹤中
- [ ] `output/` 目錄不在 Git 追蹤中
- [ ] 所有圖片檔案都被忽略
- [ ] `.gitignore` 檔案已正確設定

