"""import folium


def show_satellite_imagery(latitude, longitude):
    # Belirtilen koordinatlar için bir folium haritası oluştur
    map_osm = folium.Map(location=[latitude, longitude], zoom_start=15)

    # Uydu görüntüsü katmanını ekle
    folium.TileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                     attr='Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
                     name='OpenStreetMap').add_to(map_osm)

    # Koordinatları işaretle
    folium.Marker([latitude, longitude], popup='Selected Location').add_to(map_osm)

    # Haritayı göster
    map_osm.save('map.html')
    import webbrowser
    webbrowser.open('map.html')


# Örnek koordinatlar (Ankara)
latitude = 39.9334
longitude = 32.8597

# Koordinatların uydu görüntüsünü göster
show_satellite_imagery(latitude, longitude)"""

"""
import matplotlib.pyplot as plt
import numpy as np

def plot_route(start, end):
    # Başlangıç ve varış noktalarını ayırma
    start_lat, start_lon = start
    end_lat, end_lon = end

    # Haritayı çizme
    plt.figure(figsize=(8, 6))
    plt.plot([start_lon, end_lon], [start_lat, end_lat], 'r', label='Rotanız')

    # Başlangıç ve varış noktalarını işaretleme
    plt.plot(start_lon, start_lat, 'go', label='Başlangıç')
    plt.plot(end_lon, end_lat, 'bo', label='Varış')

    # Eksen etiketleri ve başlık
    plt.xlabel('Boylam')
    plt.ylabel('Enlem')
    plt.title('Navigasyon Uygulaması')
    plt.legend()

    # Haritayı gösterme
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Kullanıcıdan başlangıç ve varış noktalarını al
    start_lat = float(input("Başlangıç noktasının enlemini girin: "))
    start_lon = float(input("Başlangıç noktasının boylamını girin: "))
    end_lat = float(input("Varış noktasının enlemini girin: "))
    end_lon = float(input("Varış noktasının boylamını girin: "))

    # Rotayı çiz
    start = (start_lat, start_lon)
    end = (end_lat, end_lon)
    plot_route(start, end)"""

"""
import folium

def create_route_map(start, end):
    # Harita oluşturma
    m = folium.Map(location=start, zoom_start=12)

    # Başlangıç ve varış noktalarını işaretleme
    folium.Marker(start, popup='Başlangıç Noktası', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(end, popup='Varış Noktası', icon=folium.Icon(color='blue')).add_to(m)

    # Rotayı çizme
    folium.PolyLine(locations=[start, end], color='red', weight=2.5, opacity=1).add_to(m)

    return m

if __name__ == "__main__":
    # Kullanıcıdan başlangıç ve varış noktalarını al
    start_lat = float(input("Başlangıç noktasının enlemini girin: "))
    start_lon = float(input("Başlangıç noktasının boylamını girin: "))
    end_lat = float(input("Varış noktasının enlemini girin: "))
    end_lon = float(input("Varış noktasının boylamını girin: "))

    # Başlangıç ve varış noktalarını demet olarak oluşturma
    start = (start_lat, start_lon)
    end = (end_lat, end_lon)

    # Haritayı oluştur ve göster
    route_map = create_route_map(start, end)
    route_map.save('navigation_map.html')"""

#eh işte bu
"""
import folium
import webbrowser
import tkinter as tk
from tkinter import ttk

def create_route_map(start, end):
    # Harita oluşturma
    m = folium.Map(location=start, zoom_start=12)

    # Başlangıç ve varış noktalarını işaretleme
    folium.Marker(start, popup='Başlangıç Noktası', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(end, popup='Varış Noktası', icon=folium.Icon(color='blue')).add_to(m)

    # Rotayı çizme
    folium.PolyLine(locations=[start, end], color='red', weight=2.5, opacity=1).add_to(m)

    return m

def show_map_on_form(start, end):
    # Tkinter penceresini oluşturma
    root = tk.Tk()
    root.title("Harita Gösterimi")

    # Haritayı oluştur
    route_map = create_route_map(start, end)
    route_map.save('navigation_map.html')

    # Haritayı web tarayıcısında açma fonksiyonu
    def open_map():
        webbrowser.open('navigation_map.html')

    # Buton oluşturma ve haritayı gösterme
    show_map_button = ttk.Button(root, text="Haritayı Göster", command=open_map)
    show_map_button.pack(pady=10)

    # Pencereyi gösterme
    root.mainloop()

if __name__ == "__main__":
    # Kullanıcıdan başlangıç ve varış noktalarını al
    start_lat = float(input("Başlangıç noktasının enlemini girin: "))
    start_lon = float(input("Başlangıç noktasının boylamını girin: "))
    end_lat = float(input("Varış noktasının enlemini girin: "))
    end_lon = float(input("Varış noktasının boylamını girin: "))

    # Başlangıç ve varış noktalarını demet olarak oluşturma
    start = (start_lat, start_lon)
    end = (end_lat, end_lon)

    # Haritayı masaüstü formunda göster
    show_map_on_form(start, end)"""

import folium
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore
import sys
import os

def create_route_map(start, end):
    # Harita oluşturma
    m = folium.Map(location=start, zoom_start=12)

    # Başlangıç ve varış noktalarını işaretleme
    folium.Marker(start, popup='Başlangıç Noktası', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(end, popup='Varış Noktası', icon=folium.Icon(color='blue')).add_to(m)

    # Rotayı çizme
    folium.PolyLine(locations=[start, end], color='red', weight=2.5, opacity=1).add_to(m)

    # Oluşturulan haritayı HTML olarak kaydetme
    m.save('navigation_map.html')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ana pencere oluşturma
        self.setWindowTitle("Harita Gösterimi")
        self.setGeometry(100, 100, 800, 600)

        # Web motorunu oluşturma ve HTML dosyasını yükleme
        self.browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "navigation_map.html"))
        self.browser.load(QtCore.QUrl.fromLocalFile(file_path))

        # Ana düzeni oluşturma ve web motorunu ekleyerek gösterme
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    # Kullanıcıdan başlangıç ve varış noktalarını al
    start_lat = float(input("Başlangıç noktasının enlemini girin: "))
    start_lon = float(input("Başlangıç noktasının boylamını girin: "))
    end_lat = float(input("Varış noktasının enlemini girin: "))
    end_lon = float(input("Varış noktasının boylamını girin: "))

    # Başlangıç ve varış noktalarını demet olarak oluşturma
    start = (start_lat, start_lon)
    end = (end_lat, end_lon)

    # HTML dosyasını oluştur
    create_route_map(start, end)

    # PyQt5 uygulamasını başlatma
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






