# 1980 年代復古照片轉換應用程式

使用 Google Gemini API 將照片轉換為 1980 年代復古風格的應用程式。

## 功能特色

- 🎨 1980 年代復古風格轉換
- 🖼️ 支援多種圖片格式（JPG, PNG, GIF, WebP）
- 🚀 使用 Google Gemini 3 Pro Image Preview 模型
- 💻 簡單易用的命令列介面
- 🌐 復古懷舊風格的 Web 前端介面（Streamlit）
- 🔐 支援 .env 檔案管理 API Key
- 👕 自動轉換為 1980 年代服裝風格
- 🕶️ 自動添加復古配件和墨鏡

## 安裝步驟

### 1. 克隆專案

```bash
git clone <your-repo-url>
cd retro_photo_transformer
```

### 2. 建立虛擬環境

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

### 3. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 4. 設定 API Key

取得 Google Gemini API Key 後，有兩種方式設定：

**方式一：使用 .env 檔案（推薦）**

複製 `.env.example` 檔案為 `.env`：

```bash
cp .env.example .env
```

然後編輯 `.env` 檔案，將您的 API Key 填入：

```bash
GEMINI_API_KEY=your_api_key_here
```

**方式二：設定環境變數**

```bash
export GEMINI_API_KEY='your_api_key_here'
```

## 使用方法

### 🌐 Web 前端介面（推薦）

啟動 Streamlit 應用程式：

```bash
streamlit run streamlit_app.py
```

或使用快速啟動腳本：

```bash
./run_app.sh
```

瀏覽器會自動開啟，您可以在網頁介面中：
- 上傳照片
- 即時預覽轉換結果
- 下載轉換後的 1980 年代復古照片

### 💻 命令列介面

#### 基本使用

```bash
python app.py <圖片路徑>
```

#### 指定輸出目錄

```bash
python app.py photo.jpg --output my_output
```

#### 完整參數範例

```bash
python app.py photo.jpg --output results --api-key your_api_key
```

## 轉換特色

- **1980 年代復古風格**: 真實的 1980 年代類比膠片攝影效果
- **懷舊色調**: 褪色的暖色調，帶有淡黃或棕褐色調
- **膠片質感**: 細微的膠片顆粒和自然老化噪點
- **服裝轉換**: 自動將服裝轉換為 1980 年代風格
- **復古配件**: 自動添加顯眼的復古道具（如卡帶播放器、復古相機、遊戲機等）
- **復古墨鏡**: 隨機添加 1980 年代風格的墨鏡

## 專案結構

```
retro_photo_transformer/
├── venv/                 # 虛擬環境（不會上傳到 Git）
├── app.py               # 主程式（命令列介面）
├── streamlit_app.py     # Web 前端介面
├── retro_transformer.py # 核心轉換模組
├── requirements.txt     # 依賴套件清單
├── .env.example         # 環境變數範例（可上傳）
├── .env                 # 環境變數設定（不會上傳，需自行建立）
├── .gitignore          # Git 忽略檔案
├── .streamlit/         # Streamlit 配置
│   └── config.toml
├── run_app.sh          # 快速啟動腳本
├── LICENSE             # 授權文件
└── README.md           # 說明文件
```

## 輸出

轉換後的圖片會儲存在指定的輸出目錄（預設為 `output/`），檔名格式為：
`原檔名_retro_1980s_序號.副檔名`

例如：`photo_retro_1980s_0.png`

## 注意事項

1. 需要有效的 Google Gemini API Key
2. 確保有足夠的 API 配額
3. 圖片大小建議適中，過大的圖片可能需要較長處理時間
4. 輸出圖片大小為 1K（根據 API 設定）
5. 照片中的人物將保持原樣，只有服裝和配件會改變

## 疑難排解

### API Key 錯誤

如果遇到 API Key 相關錯誤，請確認：
- `.env` 檔案已正確建立並填入 API Key
- 環境變數已正確設定
- API Key 有效且未過期
- 有足夠的 API 配額

### 圖片載入失敗

請確認：
- 圖片路徑正確
- 圖片格式支援（JPG, PNG, GIF, WebP）
- 檔案權限正確

## 線上部署

本應用程式已部署到 Streamlit Cloud，您可以透過以下方式使用：

### 🌐 線上版本

訪問部署的應用程式（如果已部署）：
```
https://your-app-name.streamlit.app
```

### 📦 本地部署

詳細的部署指南請參考 [DEPLOY.md](DEPLOY.md)

## 授權

本專案採用 MIT 授權，詳見 [LICENSE](LICENSE) 檔案。

## 貢獻

歡迎提交 Issue 和 Pull Request！
