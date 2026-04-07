"""
Build script: Convert images to WebP + Generate QR codes for EmmBee.One
"""
from PIL import Image
import qrcode
import os

RAW = "raw-data/images-pdfs-docs"
OUT = "images"

# --- 1. Convert PNG/JPG images to WebP ---
convert_list = [
    ("Classroom-image.png", "Classroom-image.webp"),
    ("Mentor-photo.png", "Mentor-photo.webp"),
    ("Studio-01.jpg", "Studio-01.webp"),
    ("Studio-02.jpg", "Studio-02.webp"),
    ("Studio-03.jpg", "Studio-03.webp"),
    ("Sai-Image.png", "Sai-Image.webp"),
    ("Line-graph.png", "Line-graph.webp"),
    ("LOGO.png", "LOGO.png"),  # Keep as PNG for favicon
]

# Copy already-webp files
copy_list = [
    ("Website-Head-Banner-image.webp", "Website-Head-Banner-image.webp"),
    ("students-image.webp", "students-image.webp"),
]

print("=== Converting images to WebP ===")
for src, dst in convert_list:
    src_path = os.path.join(RAW, src)
    dst_path = os.path.join(OUT, dst)
    if not os.path.exists(src_path):
        print(f"  SKIP (not found): {src}")
        continue
    img = Image.open(src_path)
    if dst.endswith(".webp"):
        img.save(dst_path, "WEBP", quality=85)
    else:
        img.save(dst_path)
    src_size = os.path.getsize(src_path) / 1024
    dst_size = os.path.getsize(dst_path) / 1024
    print(f"  {src} ({src_size:.0f}KB) -> {dst} ({dst_size:.0f}KB)")

print("\n=== Copying WebP files ===")
for src, dst in copy_list:
    src_path = os.path.join(RAW, src)
    dst_path = os.path.join(OUT, dst)
    if not os.path.exists(src_path):
        print(f"  SKIP (not found): {src}")
        continue
    import shutil
    shutil.copy2(src_path, dst_path)
    print(f"  Copied: {src} -> {dst}")

# --- 2. Generate QR Codes ---
print("\n=== Generating QR Codes ===")

PHONE = "917505705644"
qr_data = [
    ("qr-class8.png", f"https://wa.me/{PHONE}?text=CLASS%208"),
    ("qr-class9.png", f"https://wa.me/{PHONE}?text=CLASS%209"),
    ("qr-class10.png", f"https://wa.me/{PHONE}?text=CLASS%2010"),
    ("qr-demo.png", f"https://wa.me/{PHONE}?text=I%20want%20to%20schedule%20a%20demo%20class"),
    ("qr-success-stories.png", "https://www.emmbee.one/success-stories.html"),
]

for filename, data in qr_data:
    qr = qrcode.QRCode(version=1, box_size=10, border=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0a192f", back_color="white")
    out_path = os.path.join(OUT, filename)
    img.save(out_path)
    print(f"  Generated: {filename} -> {data[:60]}...")

print("\n=== Done! ===")
