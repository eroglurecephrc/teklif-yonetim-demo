import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_tcmb_kurlar():
    tarih = datetime.now().strftime("%d%m%Y")
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"

    try:
        response = requests.get(url)
        tree = ET.fromstring(response.content)

        kurlar = {
            "USD": tree.find(".//Currency[@Kod='USD']/ForexSelling").text,
            "EUR": tree.find(".//Currency[@Kod='EUR']/ForexSelling").text,
            "GBP": tree.find(".//Currency[@Kod='GBP']/ForexSelling").text,
            "CHF": tree.find(".//Currency[@Kod='CHF']/ForexSelling").text
        }
        return kurlar
    except Exception as e:
        print(f"Döviz kuru alınamadı: {e}")
        return {}
