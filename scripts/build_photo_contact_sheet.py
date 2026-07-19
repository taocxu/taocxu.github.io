#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

files = [Path(f"1 ({i}).jpg") for i in range(1, 9)]
missing = [str(p) for p in files if not p.exists()]
if missing:
    raise FileNotFoundError(f"Missing uploaded photographs: {missing}")

font = ImageFont.load_default()
cell_w, cell_h = 520, 420
image_h = 340
margin = 24
sheet = Image.new("RGB", (cell_w * 2, cell_h * 4), "white")
draw = ImageDraw.Draw(sheet)
metadata = []

for index, path in enumerate(files):
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        metadata.append(f"{path.name}\t{image.width}x{image.height}\t{image.width / image.height:.4f}")
        fitted = ImageOps.contain(image, (cell_w - 2 * margin, image_h - 2 * margin))
        x0 = (index % 2) * cell_w
        y0 = (index // 2) * cell_h
        x = x0 + (cell_w - fitted.width) // 2
        y = y0 + margin + (image_h - 2 * margin - fitted.height) // 2
        sheet.paste(fitted, (x, y))
        draw.rectangle((x0, y0, x0 + cell_w - 1, y0 + cell_h - 1), outline="#c9cdd2", width=2)
        label = f"{path.name}  |  {image.width} × {image.height}"
        draw.text((x0 + margin, y0 + image_h + 18), label, fill="black", font=font)

sheet.save("photo-contact-sheet.jpg", quality=92, optimize=True)
Path("photo-metadata.txt").write_text("\n".join(metadata) + "\n", encoding="utf-8")
