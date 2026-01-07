# Streamlit Cloud 部署指南

本指南將幫助您將復古照片轉換應用程式部署到 Streamlit Cloud。

## 部署前準備

### 1. 確保所有檔案都已推送到 GitHub

```bash
# 檢查狀態
git status

# 如果有未提交的變更，提交並推送
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

### 2. 確認必要的檔案存在

確保以下檔案都在 GitHub 倉庫中：
- ✅ `streamlit_app.py` - 主應用程式檔案
- ✅ `retro_transformer.py` - 核心轉換模組
- ✅ `requirements.txt` - 依賴套件清單
- ✅ `README.md` - 說明文件（可選但建議）

## Streamlit Cloud 部署步驟

### 步驟 1: 登入 Streamlit Cloud

1. 前往 [Streamlit Cloud](https://share.streamlit.io/)
2. 使用您的 GitHub 帳號登入
3. 授權 Streamlit Cloud 存取您的 GitHub 倉庫

### 步驟 2: 建立新應用程式

1. 點擊 **"New app"** 按鈕
2. 選擇您的 GitHub 倉庫：`SamLai228/retro_photo_transformer`
3. 選擇分支：`main`（或 `master`）
4. 設定主檔案路徑：`streamlit_app.py`
5. 點擊 **"Deploy!"**

### 步驟 3: 等待部署完成

- Streamlit Cloud 會自動安裝依賴套件
- 部署過程可能需要 2-5 分鐘
- 您可以在部署頁面看到即時日誌

### 步驟 4: 測試應用程式

部署完成後，您會獲得一個公開的 URL，例如：
```
https://your-app-name.streamlit.app
```

## 重要注意事項

### API Key 管理

由於應用程式允許使用者在前端輸入 API Key，**不需要**在 Streamlit Cloud 設定 secrets。

使用者可以：
1. 開啟應用程式
2. 在側邊欄輸入自己的 API Key
3. 開始使用轉換功能

### 如果需要在 Streamlit Cloud 設定預設 API Key（可選）

如果您想為所有使用者提供預設的 API Key（不建議，因為會消耗您的配額），可以：

1. 在 Streamlit Cloud 應用程式頁面，點擊 **"⋮"** → **"Settings"**
2. 在 **"Secrets"** 區塊中，添加：

```toml
GEMINI_API_KEY = "your_api_key_here"
```

然後在 `streamlit_app.py` 中，API Key 會自動從 secrets 載入。

## 部署後檢查清單

- [ ] 應用程式可以正常開啟
- [ ] 使用者可以輸入 API Key
- [ ] 照片上傳功能正常
- [ ] 轉換功能可以正常執行
- [ ] 下載功能正常

## 更新應用程式

當您更新程式碼後：

1. 提交並推送到 GitHub：
   ```bash
   git add .
   git commit -m "Update app"
   git push origin main
   ```

2. Streamlit Cloud 會自動偵測變更並重新部署
3. 通常會在 1-2 分鐘內完成更新

## 疑難排解

### 部署失敗

1. **檢查 requirements.txt**
   - 確保所有依賴套件都正確列出
   - 檢查版本號是否相容

2. **檢查日誌**
   - 在 Streamlit Cloud 應用程式頁面查看日誌
   - 尋找錯誤訊息

3. **常見錯誤**
   - 缺少依賴套件：更新 `requirements.txt`
   - 檔案路徑錯誤：確認主檔案路徑正確
   - Python 版本問題：Streamlit Cloud 使用 Python 3.9

### 應用程式無法載入

- 檢查 `streamlit_app.py` 是否有語法錯誤
- 確認所有 import 的模組都在 `requirements.txt` 中

## 資源限制

Streamlit Cloud 免費版限制：
- 每個應用程式最多 1 GB RAM
- 每個應用程式最多 1 CPU
- 應用程式在 3 小時不活動後會進入休眠狀態

## 安全建議

1. **不要**在程式碼中硬編碼 API Key
2. **不要**在 GitHub 上提交 `.env` 檔案
3. 讓使用者自行輸入 API Key（目前的做法）
4. 定期更新依賴套件以修復安全漏洞

## 完成！

部署完成後，您的應用程式就可以讓全世界的使用者使用了！🎉

