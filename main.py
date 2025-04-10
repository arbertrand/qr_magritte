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
shutil.copyfile(f'result/qr_mask_4.png', f'./qr_magritte.png')
