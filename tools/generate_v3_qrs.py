import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
PHONE = "917505705644"
OUT_DIR = "../images"
BRAND_URL = "emmbee.one"

# QR data mapping
QR_DATA = [
    ("qr-class8-v3.png", f"https://wa.me/{PHONE}?text=CLASS%208", "CLASS 8"),
    ("qr-class9-v3.png", f"https://wa.me/{PHONE}?text=CLASS%209", "CLASS 9"),
    ("qr-class10-v3.png", f"https://wa.me/{PHONE}?text=CLASS%2010", "CLASS 10"),
    ("qr-demo-v3.png", f"https://wa.me/{PHONE}?text=I%20want%20to%20schedule%20a%20demo%20session", "DEMO SESSION"),
    ("qr-success-stories-v3.png", "https://www.emmbee.one/success-stories/", "SUCCESS STORIES"),
    ("qr-share-v3.png", "https://api.whatsapp.com/send?text=Hello%20there!%20I%20found%20this%20academic%20mentoring%20program%20for%20CBSE%20classes%208,%209%20%26%2010.%20Their%20approach%20to%20building%20students%20seems%20unique%E2%80%94perhaps%20you%27d%20like%20to%20check%20it%20out:%20https://www.emmbee.one", "SHARE WITH A FRIEND"),
]

def generate_branded_qr(filename, data, label):
    print(f"Generating branded QR (FINAL EXTREME) for: {label}...")
    
    # 1. Generate standard QR code at ULTRA resolution
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=40, # Ultra high resolution (~1200-1500px wide)
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Make image
    qr_img = qr.make_image(fill_color="#000000", back_color="white").convert('RGB')
    qr_w, qr_h = qr_img.size
    
    # 2. Add tighter margins for HUGE text
    margin_top = 180
    margin_bottom = 220
    new_w = qr_w
    new_h = qr_h + margin_top + margin_bottom
    
    canvas = Image.new('RGB', (new_w, new_h), color='white')
    canvas.paste(qr_img, (0, margin_top))
    
    draw = ImageDraw.Draw(canvas)
    
    # Try different bold fonts
    font_paths = [
        "C:\\Windows\\Fonts\\impact.ttf", # Extremely bold
        "C:\\Windows\\Fonts\\ariblk.ttf", # Arial Black
        "C:\\Windows\\Fonts\\arial.ttf"
    ]
    
    font_brand = None
    font_label = None
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                font_brand = ImageFont.truetype(path, 120)
                font_label = ImageFont.truetype(path, 180)
                break
            except:
                continue
    
    if not font_brand:
        font_brand = ImageFont.load_default()
        font_label = ImageFont.load_default()
    
    # Draw "emmbee.one" at TOP margin (BLACK for visibility)
    brand_text = BRAND_URL
    brand_bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    brand_w = brand_bbox[2] - brand_bbox[0]
    draw.text(((new_w - brand_w) / 2, (margin_top - (brand_bbox[3] - brand_bbox[1])) / 2), 
              brand_text, fill="#000000", font=font_brand)
    
    # Draw Category Label at BOTTOM margin (BOLD BLACK)
    label_bbox = draw.textbbox((0, 0), label, font=font_label)
    label_w = label_bbox[2] - label_bbox[0]
    label_h = label_bbox[3] - label_bbox[1]
    draw.text(((new_w - label_w) / 2, qr_h + margin_top + (margin_bottom - label_h) / 2 - 10), 
              label, fill="#000000", font=font_label)
    
    # Save output
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
    
    out_path = os.path.join(OUT_DIR, filename)
    canvas.save(out_path)
    print(f"  Saved to: {out_path} ({new_w}x{new_h})\n")

if __name__ == "__main__":
    # Get current script dir to resolve relative output path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    for filename, data, label in QR_DATA:
        generate_branded_qr(filename, data, label)
    
    print("All branded QR codes generated successfully.")
