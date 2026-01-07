"""
復古照片轉換應用程式主程式
提供簡單的命令列介面
"""

import argparse
import os
import sys
from retro_transformer import transform_to_retro


def main():
    parser = argparse.ArgumentParser(
        description="1980 年代復古照片轉換工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  python app.py photo.jpg
  python app.py photo.jpg --output my_output
  python app.py photo.jpg --output results --api-key your_api_key

說明:
  將照片轉換為 1980 年代復古風格，包含：
  - 真實的 1980 年代類比膠片攝影效果
  - 自動轉換為 1980 年代服裝風格
  - 添加復古配件（如卡帶播放器、復古相機等）
  - 保持人物原貌不變
        """
    )
    
    parser.add_argument(
        "image",
        help="輸入圖片路徑"
    )
    
    parser.add_argument(
        "--output",
        "-o",
        default="output",
        help="輸出目錄 (預設: output)"
    )
    
    parser.add_argument(
        "--api-key",
        help="Google Gemini API Key (或設定環境變數 GEMINI_API_KEY)"
    )
    
    args = parser.parse_args()
    
    # 設定 API Key
    if args.api_key:
        os.environ["GEMINI_API_KEY"] = args.api_key
    elif not os.environ.get("GEMINI_API_KEY"):
        print("錯誤: 請設定 GEMINI_API_KEY 環境變數或使用 --api-key 參數")
        print("設定方式: export GEMINI_API_KEY='your_api_key'")
        sys.exit(1)
    
    try:
        print("=" * 50)
        print("1980 年代復古照片轉換工具")
        print("=" * 50)
        transform_to_retro(args.image, args.output)
        print("\n✓ 轉換成功完成！")
    except FileNotFoundError as e:
        print(f"錯誤: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"錯誤: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

