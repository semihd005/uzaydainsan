import request 
import json

gelen_cevap = request.get("https://api.open-notify.org/astros.json")

uzaydaki_insan_sayisi = gelen_cevap.json()["number"]

print(f"Su anda uzayda {uzaydaki_insan_sayisi} insan var")