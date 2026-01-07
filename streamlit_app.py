"""
復古照片轉換應用程式 - Streamlit 前端介面
"""

import os
import streamlit as st
from pathlib import Path
import tempfile
from PIL import Image
from retro_transformer import transform_to_retro, get_image_mime_type
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 初始化 session state
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

# 設定頁面配置
st.set_page_config(
    page_title="復古照片轉換器",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 復古懷舊風格 CSS
st.markdown("""
    <style>
    /* 整體背景 - 復古米色調 */
    .stApp {
        background: linear-gradient(135deg, #f5e6d3 0%, #e8d5b7 100%);
    }
    
    /* 主標題 - 復古棕色，帶有輕微陰影 */
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #6B4423;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(107, 68, 35, 0.3);
        font-family: 'Georgia', 'Times New Roman', serif;
        letter-spacing: 2px;
    }
    
    /* 副標題 - 溫暖的棕色 */
    .sub-header {
        text-align: center;
        color: #8B6F47;
        margin-bottom: 2rem;
        font-style: italic;
        font-size: 1.1rem;
    }
    
    /* 按鈕 - 復古棕色，帶有復古邊框 */
    .stButton>button {
        width: 100%;
        background: linear-gradient(180deg, #8B6F47 0%, #6B4423 100%);
        color: #F5E6D3;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        border: 2px solid #5A3A1F;
        box-shadow: 0 4px 6px rgba(107, 68, 35, 0.3);
        transition: all 0.3s ease;
        font-size: 1.1rem;
    }
    
    .stButton>button:hover {
        background: linear-gradient(180deg, #A0826B 0%, #8B6F47 100%);
        box-shadow: 0 6px 8px rgba(107, 68, 35, 0.4);
        transform: translateY(-2px);
    }
    
    /* 側邊欄 - 復古米色背景 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F5E6D3 0%, #E8D5B7 100%);
        border-right: 3px solid #8B6F47;
    }
    
    /* 側邊欄標題 */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #6B4423;
    }
    
    /* 主內容區卡片 - 復古紙張效果 */
    .main .block-container {
        background: rgba(255, 248, 240, 0.8);
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 8px rgba(107, 68, 35, 0.2);
    }
    
    /* 標題樣式 */
    h1, h2, h3 {
        color: #6B4423;
        font-family: 'Georgia', 'Times New Roman', serif;
    }
    
    /* 輸入框 - 復古風格 */
    .stTextInput>div>div>input {
        background-color: #FFF8F0;
        border: 2px solid #8B6F47;
        border-radius: 5px;
        color: #5A3A1F;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #6B4423;
        box-shadow: 0 0 5px rgba(107, 68, 35, 0.3);
    }
    
    /* 檔案上傳區域 */
    .uploadedFile {
        border: 2px dashed #8B6F47;
        border-radius: 8px;
        background-color: #FFF8F0;
    }
    
    /* 資訊框 - 復古色調 */
    .stInfo {
        background-color: #F5E6D3;
        border-left: 4px solid #8B6F47;
        color: #5A3A1F;
    }
    
    /* 成功訊息 */
    .stSuccess {
        background-color: #E8D5B7;
        border-left: 4px solid #6B4423;
        color: #5A3A1F;
    }
    
    /* 警告訊息 */
    .stWarning {
        background-color: #F5E6D3;
        border-left: 4px solid #8B6F47;
        color: #6B4423;
    }
    
    /* 錯誤訊息 */
    .stError {
        background-color: #E8D5B7;
        border-left: 4px solid #8B0000;
        color: #5A0000;
    }
    
    /* 下載按鈕 */
    .stDownloadButton>button {
        background: linear-gradient(180deg, #A0826B 0%, #8B6F47 100%);
        color: #F5E6D3;
        border: 2px solid #6B4423;
    }
    
    /* 頁尾 */
    .footer {
        text-align: center;
        color: #8B6F47;
        padding: 1rem;
        font-style: italic;
        border-top: 2px solid #8B6F47;
        margin-top: 2rem;
    }
    
    /* 分隔線 */
    hr {
        border-color: #8B6F47;
        border-width: 2px;
    }
    
    /* 圖片容器 - 添加復古邊框 */
    .stImage img {
        border: 3px solid #8B6F47;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(107, 68, 35, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # 標題 - 復古風格
    st.markdown('<h1 class="main-header">📸 1980 年代復古照片轉換器</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">✨ 將您的照片轉換為懷舊的 1980 年代復古風格 ✨</p>', unsafe_allow_html=True)
    
    # 側邊欄設定
    with st.sidebar:
        st.header("⚙️ 設定")
        
        # API Key 設定
        st.subheader("🔑 API Key 設定")
        st.markdown("請輸入您的 Key")
        
        # 從 .env 載入預設值（僅在第一次載入時）
        default_key = os.environ.get("GEMINI_API_KEY", "")
        
        # 使用 session state 管理 API Key
        api_key_input = st.text_input(
            "Key",
            value=st.session_state.api_key if st.session_state.api_key else default_key,
            type="password",
            help="請輸入您的 API Key。刷新頁面後需要重新輸入。",
            key="api_key_input"
        )
        
        # 更新 session state
        if api_key_input:
            st.session_state.api_key = api_key_input
            os.environ["GEMINI_API_KEY"] = api_key_input
            st.success("✅ API Key 已設定")
        elif default_key and not st.session_state.api_key:
            # 如果有 .env 中的 Key 且 session state 為空，使用它
            st.session_state.api_key = default_key
            os.environ["GEMINI_API_KEY"] = default_key
            st.info("ℹ️ 使用 .env 檔案中的 API Key")
        elif not api_key_input:
            # 清除 session state
            st.session_state.api_key = ""
            if os.environ.get("GEMINI_API_KEY"):
                del os.environ["GEMINI_API_KEY"]
            st.warning("⚠️ 請輸入 API Key 才能使用轉換功能")
        
        # 清除按鈕
        if st.session_state.api_key:
            if st.button("🗑️ 清除 Key", use_container_width=True):
                st.session_state.api_key = ""
                if "GEMINI_API_KEY" in os.environ:
                    del os.environ["GEMINI_API_KEY"]
                st.rerun()
        
        st.divider()
        
        # 風格說明
        st.subheader("🎨 轉換風格")
        st.info("""
        **1980 年代復古風格**
        
        - 真實的 1980 年代類比膠片攝影效果
        - 懷舊、溫暖、感性的色調
        - 褪色的暖色調，帶有淡黃或棕褐色調
        - 細微的膠片顆粒和自然老化噪點
        - 柔和高光，低對比度，柔和陰影
        - 自動添加 1980 年代服裝和復古配件
        """)
        
        st.divider()
        
        # 輸出設定
        st.subheader("📁 輸出設定")
        output_dir = st.text_input("輸出目錄", value="output")
        
        st.divider()
        
        # 使用說明
        st.subheader("📖 使用說明")
        st.markdown("""
        1. 在「🔑 API Key 設定」中輸入您的 Key
        2. 上傳一張照片
        3. 點擊「開始轉換」按鈕
        4. 等待處理完成
        5. 下載轉換後的 1980 年代復古照片
        
        **注意事項：**
        - 需要有效的 API Key
        - 照片中的人物將保持原樣
        - 服裝會自動轉換為 1980 年代風格
        - 會自動添加復古配件（如卡帶播放器、復古相機等）
        """)
    
    # 主內容區
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📤 上傳照片")
        
        # 檔案上傳
        uploaded_file = st.file_uploader(
            "選擇圖片檔案",
            type=['jpg', 'jpeg', 'png', 'gif', 'webp'],
            help="支援 JPG, PNG, GIF, WebP 格式"
        )
        
        if uploaded_file is not None:
            # 顯示預覽
            image = Image.open(uploaded_file)
            st.image(image, caption="原始照片", use_container_width=True)
            
            # 顯示檔案資訊
            st.info(f"📄 檔案名稱: {uploaded_file.name}\n📏 尺寸: {image.size[0]} x {image.size[1]}")
    
    with col2:
        st.header("📥 轉換結果")
        
        if uploaded_file is not None:
            # 轉換按鈕
            if st.button("🚀 開始轉換", type="primary", use_container_width=True):
                # 檢查 API Key（優先使用 session state）
                api_key = st.session_state.get("api_key", "") or os.environ.get("GEMINI_API_KEY", "")
                if not api_key or api_key == "your_api_key_here" or api_key.strip() == "":
                    st.error("❌ 請先在側邊欄輸入 Key！")
                    st.info("💡 請在左側側邊欄的「🔑 API Key 設定」中輸入您的 Key")
                    st.stop()
                # 確保環境變數已設定
                os.environ["GEMINI_API_KEY"] = api_key
                
                # 儲存上傳的檔案到臨時目錄
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                try:
                    # 顯示進度
                    with st.spinner("🔄 正在轉換照片為 1980 年代復古風格，請稍候..."):
                        # 執行轉換
                        transform_to_retro(tmp_path, output_dir)
                        
                        # 尋找輸出檔案
                        output_path = Path(output_dir)
                        output_files = list(output_path.glob(f"*_retro_1980s_*"))
                        
                        if output_files:
                            # 顯示最新的輸出檔案
                            latest_file = max(output_files, key=os.path.getctime)
                            
                            # 讀取並顯示結果
                            result_image = Image.open(latest_file)
                            st.image(result_image, caption="1980 年代復古風格", use_container_width=True)
                            
                            # 下載按鈕
                            with open(latest_file, "rb") as f:
                                st.download_button(
                                    label="💾 下載轉換後的照片",
                                    data=f.read(),
                                    file_name=latest_file.name,
                                    mime=get_image_mime_type(str(latest_file)),
                                    use_container_width=True
                                )
                            
                            st.success(f"✅ 轉換完成！檔案已儲存至: {latest_file}")
                        else:
                            st.warning("⚠️ 未找到輸出檔案，請檢查轉換過程")
                
                except Exception as e:
                    st.error(f"❌ 轉換失敗: {str(e)}")
                    st.exception(e)
                
                finally:
                    # 清理臨時檔案
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path)
        else:
            st.info("👆 請先上傳一張照片")
    
    # 頁尾 - 復古風格
    st.divider()
    st.markdown(
        "<div class='footer'>"
        "📸 1980 年代復古照片轉換器 | 使用 Google Gemini API 驅動 | 重溫美好時光 ✨"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

