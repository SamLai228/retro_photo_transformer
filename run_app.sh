#!/bin/bash

# 復古照片轉換應用程式啟動腳本

# 檢查虛擬環境是否激活
if [ -z "$VIRTUAL_ENV" ]; then
    echo "正在激活虛擬環境..."
    source venv/bin/activate
fi

# 檢查依賴是否已安裝
if ! python -c "import streamlit" 2>/dev/null; then
    echo "正在安裝依賴套件..."
    pip install -r requirements.txt
fi

# 切換到腳本所在目錄
cd "$(dirname "$0")"

# 檢查是否有其他 Streamlit 應用程式正在運行
echo "檢查是否有其他 Streamlit 應用程式正在運行..."
if lsof -ti:8501 > /dev/null 2>&1; then
    echo "警告: 端口 8501 已被佔用，正在嘗試關閉..."
    lsof -ti:8501 | xargs kill -9 2>/dev/null
    sleep 2
    echo "已關閉佔用端口的應用程式"
fi

# 使用不同的端口避免衝突（8502）
PORT=8502

# 啟動 Streamlit 應用程式，明確指定檔案和端口
echo "正在啟動復古照片轉換器..."
echo "應用程式檔案: $(pwd)/streamlit_app.py"
echo "端口: $PORT"
echo "瀏覽器將自動開啟: http://localhost:$PORT"
echo ""

# 使用絕對路徑明確指定要運行的應用程式
streamlit run "$(pwd)/streamlit_app.py" \
    --server.port $PORT \
    --server.headless false \
    --server.address localhost

