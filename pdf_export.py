from fpdf import FPDF
from datetime import datetime
import os

def teklif_pdf_olustur(teklif_metni, musteri_adi):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"TEKLİF FORMU - {musteri_adi}", ln=True, align='C')
    pdf.ln(10)

    for line in teklif_metni.splitlines():
        pdf.cell(200, 10, txt=line, ln=True)

    tarih = datetime.now().strftime("%Y%m%d_%H%M%S")
    dosya_adi = f"Teklif_{musteri_adi}_{tarih}.pdf"
    pdf.output(dosya_adi)
    return dosya_adi

def siparis_pdf_olustur(siparis_metni, tedarikci_adi):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"SİPARİŞ FORMU - {tedarikci_adi}", ln=True, align='C')
    pdf.ln(10)

    for line in siparis_metni.splitlines():
        pdf.cell(200, 10, txt=line, ln=True)

    tarih = datetime.now().strftime("%Y%m%d_%H%M%S")
    dosya_adi = f"Siparis_{tedarikci_adi}_{tarih}.pdf"
    pdf.output(dosya_adi)
    return dosya_adi
