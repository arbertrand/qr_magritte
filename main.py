import segno

# Dein QR-Code-Inhalt
data = 'https://example.com'

# Alle 8 Masken durchprobieren
for mask in range(8):
    # QR-Code mit bestimmter Maske erzeugen
    qr = segno.make_qr(data, mask=mask)

    # Datei speichern mit Masken-Nummer im Namen
    filename = f'result/qr_mask_{mask}.png'
    qr.save(filename, scale=10)
    print(f'Gespeichert: {filename}')