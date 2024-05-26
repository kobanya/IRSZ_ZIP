import pandas as pd

# Töltsd be az Excel fájlt, figyelmen kívül hagyva az oszlopneveket
file_path = 'Iranyitoszam-Internet_uj.xlsx'
data = pd.read_excel(file_path, sheet_name=2, engine='openpyxl', header=None)  # A 3. lap betöltése (0-indexeléssel a 2. lap)

# Csak az első négy oszlopot vizsgáljuk, és az első sor kihagyása (fejlécek)
adatok_listaja = list(zip(data[0][1:], data[1][1:], data[2][1:], data[3][1:],data[4][1:]))

# Az első néhány bejegyzés megjelenítése
print(adatok_listaja)


