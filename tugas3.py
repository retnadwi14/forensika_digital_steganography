import requests
import os
import base64
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# 1. Periksa metadata pada https://journal.ittelkom-sby.ac.id/jaiit/
url = "https://journal.ittelkom-sby.ac.id/jaiit/"
response = requests.get(url)
template = "JURNAL TEMPLATE ISSN P-ISSN: ISSN 2716-1935 JAIIT dikelola dan diterbitkan oleh LPPM ITTelkom Surabaya Jl. Ketintang No. 156, Surabaya 60231 Jawa Timur, Indonesia Email: [email protected] e-ISSN : 2716-1927; p-ISSN : 2716-1935"

# 2. Kode script, pilih salah satu jurnal PDF, edit metadata, dan sesuaikan dengan paper yang dipilih
# Untuk tujuan demonstrasi, kita akan menggunakan file PDF contoh
file_pdf = "jurnal.pdf"
pdf = PdfReader(file_pdf)
pdf_baru = PdfWriter()

# Tambahkan halaman baru di awal dokumen (kosong)
pdf_baru.add_blank_page(width=letter[0], height=letter[1])

# Tambahkan halaman dari jurnal yang ada
for page in pdf.pages:
    pdf_baru.add_page(page)

# Tambahkan halaman baru di akhir dokumen (kosong)
pdf_baru.add_blank_page(width=letter[0], height=letter[1])

# Simpan PDF yang diubah
file_pdf_terubah = "jurnal_FD.pdf"
with open(file_pdf_terubah, "wb") as f:
    pdf_baru.write(f)

# 3. Dekode script
# Untuk tujuan demonstrasi, kita akan menggunakan file PDF yang diubah
pdf_terdecod = PdfReader(file_pdf_terubah)

# Output script: 2 file PDF, file PDF asli dan file PDF yang diubah dengan halaman awal dan akhir yang ditambahkan
print("File PDF Asli:", file_pdf)
print("File PDF yang Diubah:", file_pdf_terubah)