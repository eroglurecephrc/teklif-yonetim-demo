import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from utils.pdf_export import teklif_pdf_olustur, siparis_pdf_olustur
from utils.tcmb_kur import get_tcmb_kurlar

class TeklifUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Teklif ve Sipariş Yönetimi")
        self.root.geometry("900x600")

        # Sekmeli yapı
        self.tab_control = ttk.Notebook(self.root)

        self.tab_musteri = ttk.Frame(self.tab_control)
        self.tab_teklif = ttk.Frame(self.tab_control)
        self.tab_siparis = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_musteri, text='Müşteri Kartları')
        self.tab_control.add(self.tab_teklif, text='Teklif Oluştur')
        self.tab_control.add(self.tab_siparis, text='Sipariş Formu')

        self.tab_control.pack(expand=1, fill='both')

        self.ekle_musteri_tab()
        self.ekle_teklif_tab()
        self.ekle_siparis_tab()

    def ekle_musteri_tab(self):
        ttk.Label(self.tab_musteri, text="Müşteri Adı:").pack(pady=5)
        self.entry_musteri = ttk.Entry(self.tab_musteri, width=40)
        self.entry_musteri.pack()
        ttk.Button(self.tab_musteri, text="Kaydet", command=self.musteri_kaydet).pack(pady=10)

    def ekle_teklif_tab(self):
        ttk.Label(self.tab_teklif, text="Teklif Kalemleri (örnek)").pack(pady=5)
        self.text_teklif = tk.Text(self.tab_teklif, height=15)
        self.text_teklif.pack()
        ttk.Button(self.tab_teklif, text="PDF Kaydet", command=self.teklif_kaydet).pack(pady=10)

    def ekle_siparis_tab(self):
        ttk.Label(self.tab_siparis, text="Tedarikçi Adı:").pack(pady=5)
        self.entry_tedarikci = ttk.Entry(self.tab_siparis, width=40)
        self.entry_tedarikci.pack()
        ttk.Label(self.tab_siparis, text="Malzeme / Ölçü / Adet").pack(pady=5)
        self.text_siparis = tk.Text(self.tab_siparis, height=10)
        self.text_siparis.pack()
        ttk.Button(self.tab_siparis, text="Siparişi PDF Kaydet", command=self.siparis_kaydet).pack(pady=10)

    def musteri_kaydet(self):
        musteri_adi = self.entry_musteri.get()
        messagebox.showinfo("Müşteri", f"{musteri_adi} başarıyla kaydedildi.")


    def teklif_kaydet(self):
        teklif = self.text_teklif.get("1.0", tk.END).strip()
        musteri_adi = self.entry_musteri.get() or "Musteri"
        dosya_adi = teklif_pdf_olustur(teklif, musteri_adi)
        messagebox.showinfo("Teklif", f"PDF olarak kaydedildi:\n{dosya_adi}")
        
  
    def siparis_kaydet(self):
        siparis = self.text_siparis.get("1.0", tk.END).strip()
        tedarikci = self.entry_tedarikci.get() or "Tedarikci"
        dosya_adi = siparis_pdf_olustur(siparis, tedarikci)
        messagebox.showinfo("Sipariş", f"PDF olarak kaydedildi:\n{dosya_adi}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TeklifUygulamasi(root)
    root.mainloop()
