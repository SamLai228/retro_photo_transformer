# Streamlit Cloud 部署疑難排解

## 常見錯誤和解決方案

### 錯誤：Oh no. Error running app

這個錯誤通常由以下原因造成：

#### 1. 檢查 Streamlit Cloud 日誌

在 Streamlit Cloud 應用程式頁面：
1. 點擊應用程式
2. 點擊右上角的 **"⋮"** (三個點)
3. 選擇 **"View app logs"**
4. 查看錯誤訊息

#### 2. 常見問題和解決方案

##### 問題 A: 模組導入錯誤

**錯誤訊息類似：**
```
ModuleNotFoundError: No module named 'retro_transformer'
```

**解決方案：**
確保 `retro_transformer.py` 和 `streamlit_app.py` 在同一個目錄下。

##### 問題 B: 依賴套件版本問題

**錯誤訊息類似：**
```
ImportError: cannot import name 'xxx' from 'google.genai'
```

**解決方案：**
更新 `requirements.txt`，指定版本號：
```txt
google-genai>=1.0.0
python-dotenv>=1.0.0
streamlit>=1.28.0
Pillow>=10.0.0
```

##### 問題 C: Python 版本不相容

Streamlit Cloud 預設使用 Python 3.9。

**解決方案：**
如果您的程式碼需要特定 Python 版本，可以在專案根目錄建立 `runtime.txt`：
```
python-3.9.18
```

##### 問題 D: 檔案路徑問題

**錯誤訊息類似：**
```
FileNotFoundError: [Errno 2] No such file or directory
```

**解決方案：**
確保所有檔案路徑使用相對路徑，不要使用絕對路徑。

##### 問題 E: 語法錯誤

**解決方案：**
在本地測試應用程式：
```bash
streamlit run streamlit_app.py
```

如果本地可以運行，但 Streamlit Cloud 不行，檢查：
- 是否有平台特定的程式碼
- 是否有檔案權限問題

#### 3. 檢查清單

在部署前確認：

- [ ] `requirements.txt` 包含所有必要的依賴套件
- [ ] 所有 Python 檔案沒有語法錯誤
- [ ] `streamlit_app.py` 是主檔案
- [ ] 所有導入的模組都存在
- [ ] 沒有使用絕對路徑
- [ ] 沒有硬編碼的 API Key（應該讓使用者輸入）

#### 4. 測試步驟

1. **本地測試**
   ```bash
   streamlit run streamlit_app.py
   ```
   確保本地可以正常運行

2. **檢查依賴**
   ```bash
   pip install -r requirements.txt
   python -c "import streamlit; import retro_transformer"
   ```

3. **檢查語法**
   ```bash
   python -m py_compile streamlit_app.py retro_transformer.py
   ```

#### 5. 獲取詳細錯誤訊息

在 Streamlit Cloud：
1. 進入應用程式頁面
2. 點擊 **"⋮"** → **"View app logs"**
3. 查看完整的錯誤堆疊追蹤
4. 根據錯誤訊息進行修復

#### 6. 重新部署

修復問題後：
1. 提交變更到 GitHub
2. Streamlit Cloud 會自動重新部署
3. 或手動點擊 **"Reboot app"**

## 如果問題仍然存在

1. 檢查 Streamlit Cloud 的狀態頁面
2. 查看 Streamlit 官方文件
3. 在 Streamlit 論壇尋求幫助

