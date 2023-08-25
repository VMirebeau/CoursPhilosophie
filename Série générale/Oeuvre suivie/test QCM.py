import PyPDF2

# Créer un nouveau fichier PDF
pdf = PyPDF2.PdfFileWriter()

# Créer une nouvelle page pour le QCM
page = PyPDF2.pdf.PageObject.createBlankPage(None, 500, 500)

# Ajouter le texte du QCM à la page
qcm_text = "Voulez-vous manger des pâtes ?"
qcm_options = ["oui", "non", "peut-être", "demain"]
page.drawText(qcm_text, 100, 400)
for i, option in enumerate(qcm_options):
    y = 350 - i * 50
    page.drawText(f"{i+1}. {option}", 120, y)

# Ajouter la page au fichier PDF
pdf.addPage(page)

# Enregistrer le fichier PDF
with open("qcm_pates.pdf", "wb") as f:
    pdf.write(f)
