import segno

# Dein QR-Code-Inhalt
data = 'https://raw.githubusercontent.com/arbertrand/qr_magritte/refs/heads/main/qr_magritte.png'
# => tiny URL
data = "https://tinyurl.com/4ycext9w"

# Alle 8 Masken durchprobieren
for mask in range(8):
    # QR-Code mit bestimmter Maske erzeugen
    qr = segno.make_qr(data, mask=mask)
    # qr = segno.make_micro(data, mask=mask)

    # Datei speichern mit Masken-Nummer im Namen
    filename = f'result/qr_mask_{mask}.png'
    qr.save(filename, scale=30)
    print(f'Gespeichert: {filename}')


import shutil
shutil.copyfile(f'result/qr_mask_4.png', f'./qr_magritte_raw.png')



from PIL import Image, ImageDraw, ImageFont
import math

# Bild laden
bild = Image.open("./qr_magritte_raw.png").convert("RGBA")

# Text, der hinzugefügt werden soll
text = "Ceci est une ■▪ □ ▢ ▫"

# Font laden – du brauchst eine Schreibschrift-Datei, z.B. 'GreatVibes-Regular.ttf'
# Kostenlos z.B. hier: https://fonts.google.com/specimen/Great+Vibes
font = ImageFont.truetype("tmp/Dancing_Script/DancingScript-VariableFont_wght.ttf", size=130)

# Neues transparentes Layer erstellen
text_layer = Image.new("RGBA", bild.size, (100, 100, 100, 0))
draw = ImageDraw.Draw(text_layer)

# Textgröße ermitteln
text_width, text_height = draw.textsize(text, font=font)

# Position berechnen: unten links
x = 30
y = bild.width - text_width + 350

# Text schreiben
draw.text((x, y), text, font=font, fill=(255, 69, 0, 255))  # rot

# Layer rotieren (ca. 45° für von unten links nach oben rechts)
text_layer = text_layer.rotate(45, resample=Image.BICUBIC, expand=1)

# Originalbild vergrößern, um Platz für Rotation zu haben
final_image = Image.new("RGBA", text_layer.size, (100, 100, 100, 100))
final_image.paste(bild, ((text_layer.width - bild.width) // 2, (text_layer.height - bild.height) // 2))

# Textlayer drauflegen
final_image = Image.alpha_composite(final_image, text_layer)

# Ergebnis speichern
final_image.convert("RGB").save("qr_magritte.png", "PNG")

