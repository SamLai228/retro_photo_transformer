"""
復古照片風格轉換模組
使用 Google Gemini API 將照片轉換為復古風格
"""

import mimetypes
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 載入 .env 檔案
load_dotenv()


def save_binary_file(file_name, data):
    """儲存二進位檔案"""
    f = open(file_name, "wb")
    f.write(data)
    f.close()
    print(f"檔案已儲存至: {file_name}")


def load_image_bytes(image_path):
    """載入圖片為二進位資料"""
    with open(image_path, "rb") as image_file:
        return image_file.read()


def get_image_mime_type(image_path):
    """根據檔案副檔名取得 MIME 類型"""
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type is None:
        # 根據副檔名判斷
        ext = Path(image_path).suffix.lower()
        mime_map = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }
        mime_type = mime_map.get(ext, 'image/jpeg')
    return mime_type


def transform_to_retro(image_path, output_dir="output"):
    """
    將照片轉換為 1980 年代復古風格
    
    Args:
        image_path: 輸入圖片路徑
        output_dir: 輸出目錄
    """
    # 檢查 API Key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("請設定環境變數 GEMINI_API_KEY")
    
    # 檢查輸入檔案是否存在
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"找不到圖片檔案: {image_path}")
    
    # 建立輸出目錄
    os.makedirs(output_dir, exist_ok=True)
    
    # 初始化客戶端
    client = genai.Client(api_key=api_key)
    model = "gemini-3-pro-image-preview"
    
    # 載入圖片
    image_bytes = load_image_bytes(image_path)
    mime_type = get_image_mime_type(image_path)
    
    # 1980 年代復古風格轉換提示詞
    prompt = """Transform the uploaded photo into a photorealistic 1980s vintage photograph.

Preserve the original composition, camera angle, body pose, facial features, expressions, and proportions exactly as in the source image.

Style requirements:

- Era: authentic 1980s analog film photography

- Mood: nostalgic, warm, sentimental, playful, expressive, and character-driven

- Color: faded warm tones with a subtle yellow or sepia cast

- Texture: subtle film grain and natural aging noise

- Lighting: soft highlights, lower contrast, gently muted shadows

- Lens: mild softness and light blur, avoiding modern digital sharpness

- Paper aging: gentle vignette and slight edge darkening

Clothing transformation:

- Replace the original clothing with realistic 1980s-style vintage clothing

- Clothing should reflect common 1980s fashion aesthetics, including bold yet authentic retro colors, classic cuts, and period-appropriate fabrics

- Maintain the same clothing type and coverage (e.g., shirt remains a shirt, jacket remains a jacket)

- Ensure the clothing fits naturally on the body without altering body shape or proportions

- Clothing changes must look realistic and consistent with the lighting and scene

Retro accessories and hand-held props:

- Add one or two visually prominent, large, and iconic 1980s-era accessories or props that are clearly visible and eye-catching

- At least one prop should be held naturally in the person's hand or hands, and should be noticeably large or prominent in size

- Hand-held props may include diverse retro items such as: vintage cassette players (large boomboxes), cassette tapes, retro cameras (Polaroid cameras, film cameras), classic oversized headphones, analog walkman-style devices, old magazines or newspapers, vintage telephones, retro gaming devices (Game Boy, Atari controllers), vintage sunglasses cases, retro watches, vintage radios, old cameras with flash, vintage microphones, retro skateboards, vintage bicycles, or other recognizable everyday objects from the 1980s

- Props should be large enough to be clearly visible and prominent in the photo, making them a focal point

- Props should feel casually held, as if captured in a spontaneous moment, not posed or staged

- Ensure hand position, grip, and scale look natural and anatomically correct, but the props should be noticeably large or prominent

- Props must match the lighting, perspective, and realism of the scene

- Randomly add vintage 1980s-style sunglasses (aviator sunglasses, oversized frames, colorful frames, or classic retro designs) to the person's face when appropriate - these should be highly visible and characteristic of 1980s fashion

Constraints:

- Do NOT alter the person's identity, face shape, facial features, hairstyle, body shape, or posture

- Do NOT change the background layout or scene structure

- Do NOT distort hands, fingers, or object proportions

- No illustration, painting, anime, or stylized AI-art appearance

- No fantasy, exaggerated, or comedic elements

- No modern technology, logos, or contemporary branding

- No HDR, no ultra-sharp details, no modern color grading

The final result should look like a genuine photograph taken in the 1980s, featuring period-accurate clothing, iconic accessories, hand-held retro props, and naturally aged photo characteristics."""
    
    # 建立內容 - 使用 from_bytes 方法上傳圖片
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type
                ),
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    
    # 設定生成配置
    generate_content_config = types.GenerateContentConfig(
        response_modalities=[
            "IMAGE",
            "TEXT",
        ],
        image_config=types.ImageConfig(
            image_size="1K",
        ),
    )
    
    # 準備輸出檔名
    input_filename = Path(image_path).stem
    file_index = 0
    
    print(f"正在轉換圖片: {image_path}")
    print("風格: 1980 年代復古風格")
    print("處理中...")
    
    # 生成內容
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if (
            chunk.candidates is None
            or chunk.candidates[0].content is None
            or chunk.candidates[0].content.parts is None
        ):
            continue
        
        # 處理圖片輸出
        if chunk.candidates[0].content.parts[0].inline_data and chunk.candidates[0].content.parts[0].inline_data.data:
            file_extension = mimetypes.guess_extension(
                chunk.candidates[0].content.parts[0].inline_data.mime_type
            ) or ".png"
            
            output_filename = f"{input_filename}_retro_1980s_{file_index}{file_extension}"
            output_path = os.path.join(output_dir, output_filename)
            file_index += 1
            
            inline_data = chunk.candidates[0].content.parts[0].inline_data
            data_buffer = inline_data.data
            
            save_binary_file(output_path, data_buffer)
        
        # 處理文字輸出
        elif hasattr(chunk, 'text') and chunk.text:
            print(chunk.text)
    
    print(f"\n轉換完成！輸出目錄: {output_dir}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("使用方法: python retro_transformer.py <圖片路徑> [輸出目錄]")
        print("範例: python retro_transformer.py photo.jpg output")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    
    try:
        transform_to_retro(image_path, output_dir)
    except Exception as e:
        print(f"錯誤: {e}")
        sys.exit(1)

