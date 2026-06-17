import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, scrolledtext

class Yayin:
    def __init__(self, baslik, yayin_yili):
        self.baslik = baslik
        self.yayin_yili = yayin_yili
        self.durum = "Mevcut"

class Kitap(Yayin):
    def __init__(self, baslik, yazar, yayin_yili, isbn, tur):
        super().__init__(baslik, yayin_yili)
        self.yazar = yazar
        self.isbn = isbn
        self.tur = tur

    def __str__(self):
        return f"Kitap: {self.baslik} | Yazar: {self.yazar} | Tür: {self.tur} | Durum: {self.durum}"

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        return f"✅ '{kitap.baslik}' sisteme başarıyla eklendi."

    def kitaplari_listele(self):
        if not self.kitaplar:
            return "Kütüphane şu an boş."
        else:
            tur_gruplari = {}
            for kitap in self.kitaplar:
                if kitap.tur not in tur_gruplari:
                    tur_gruplari[kitap.tur] = []
                tur_gruplari[kitap.tur].append(str(kitap))
            
            sonuc = ""
            for tur, kitaplar in tur_gruplari.items():
                sonuc += f"\n--- {tur} ---\n"
                sonuc += "\n".join(kitaplar) + "\n"
            return sonuc.strip()

    def odunc_ver(self, kitap_adi):
        for kitap in self.kitaplar:
            if kitap.baslik.lower() == kitap_adi.lower():
                if kitap.durum == "Mevcut":
                    kitap.durum = "Ödünç Verildi"
                    return f"✔️ {kitap.baslik} ödünç verildi."
                else:
                    return "❌ Bu kitap zaten ödünçte."
        return "❌ Aradığınız kitap bulunamadı."

class KutuphaneGUI:
    def __init__(self, root):
        self.kutuphane = Kutuphane()
        self.root = root
        self.root.title("📚 Kütüphane Otomasyonu")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        # Stil ayarla
        style = ttk.Style()
        style.theme_use('clam')  # Modern tema
        style.configure('TButton', font=('Arial', 12, 'bold'), padding=10)
        style.configure('TLabel', font=('Arial', 14, 'bold'), background="#f0f0f0")
        style.configure('TFrame', background="#f0f0f0")

        # Ana frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Başlık
        self.title_label = ttk.Label(main_frame, text="📚 Kütüphane Otomasyonu", foreground="#8B602E")
        self.title_label.pack(pady=(0, 20))

        # Butonlar frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        self.btn_ekle = ttk.Button(button_frame, text="➕ Kitap Ekle", command=self.kitap_ekle_pencere)
        self.btn_ekle.grid(row=0, column=0, padx=10, pady=5)

        self.btn_listele = ttk.Button(button_frame, text="📋 Kitapları Listele", command=self.kitaplari_listele)
        self.btn_listele.grid(row=0, column=1, padx=10, pady=5)

        self.btn_odunc = ttk.Button(button_frame, text="🔄 Kitap Ödünç Al", command=self.kitap_odunc_al)
        self.btn_odunc.grid(row=1, column=0, padx=10, pady=5)

        self.btn_cikis = ttk.Button(button_frame, text="❌ Çıkış", command=root.quit)
        self.btn_cikis.grid(row=1, column=1, padx=10, pady=5)

        # Liste alanı
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        ttk.Label(list_frame, text="Kitap Listesi:").pack(anchor=tk.W)
        self.list_text = scrolledtext.ScrolledText(list_frame, height=10, width=60, font=('Arial', 10))
        self.list_text.pack(fill=tk.BOTH, expand=True)

    def kitap_ekle_pencere(self):
        # Yeni pencere
        ekle_win = tk.Toplevel(self.root)
        ekle_win.title("➕ Kitap Ekle")
        ekle_win.geometry("400x350")
        ekle_win.configure(bg="#f0f0f0")

        # Stil
        style = ttk.Style(ekle_win)
        style.configure('TLabel', font=('Arial', 12), background="#f0f0f0")
        style.configure('TEntry', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 12, 'bold'), padding=5)

        frame = ttk.Frame(ekle_win, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Kitap Adı:").grid(row=0, column=0, sticky=tk.W, pady=5)
        baslik_entry = ttk.Entry(frame, width=30)
        baslik_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Yazarı:").grid(row=1, column=0, sticky=tk.W, pady=5)
        yazar_entry = ttk.Entry(frame, width=30)
        yazar_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Yayın Yılı:").grid(row=2, column=0, sticky=tk.W, pady=5)
        yil_entry = ttk.Entry(frame, width=30)
        yil_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="ISBN:").grid(row=3, column=0, sticky=tk.W, pady=5)
        isbn_entry = ttk.Entry(frame, width=30)
        isbn_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Tür:").grid(row=4, column=0, sticky=tk.W, pady=5)
        tur_entry = ttk.Entry(frame, width=30)
        tur_entry.grid(row=4, column=1, pady=5)

        def ekle():
            baslik = baslik_entry.get()
            yazar = yazar_entry.get()
            yil = yil_entry.get()
            isbn = isbn_entry.get()
            tur = tur_entry.get()
            if baslik and yazar and yil and isbn and tur:
                yeni_kitap = Kitap(baslik, yazar, yil, isbn, tur)
                mesaj = self.kutuphane.kitap_ekle(yeni_kitap)
                messagebox.showinfo("✅ Başarılı", mesaj)
                ekle_win.destroy()
                self.kitaplari_listele()  # Listeyi güncelle
            else:
                messagebox.showerror("❌ Hata", "Tüm alanları doldurun!")

        ttk.Button(frame, text="➕ Ekle", command=ekle).grid(row=5, column=0, columnspan=2, pady=20)

    def kitaplari_listele(self):
        liste = self.kutuphane.kitaplari_listele()
        self.list_text.delete(1.0, tk.END)
        self.list_text.insert(tk.END, liste)

    def kitap_odunc_al(self):
        kitap_adi = simpledialog.askstring("🔄 Kitap Ödünç Al", "Ödünç almak istediğiniz kitabın adı:")
        if kitap_adi:
            mesaj = self.kutuphane.odunc_ver(kitap_adi)
            messagebox.showinfo("📋 Sonuç", mesaj)
            self.kitaplari_listele()  # Listeyi güncelle

# --- ANA PROGRAM ---
if __name__ == "__main__":
    root = tk.Tk()
    gui = KutuphaneGUI(root)
    root.mainloop()