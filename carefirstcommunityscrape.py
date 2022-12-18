from bs4 import BeautifulSoup
import requests
import time

i = 1
while i < 20:
    try:
        link = "https://providersearch.carefirstchpmd.com/?Page={page}&LocationCity=Waldorf&PCPIndicator=False&EPSDTIndicator=False&PanelStatus=False"
        URL = link.format(page = i)

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        table = soup.find(id="content")

        doctors = table.find_all(id="record")

        for doctor in doctors:
            doctor_name = doctor.find("span", class_="provider-name")
            doctor_specialty = doctor.find("span", class_="provider-speciality")
            doctor_group = doctor.find("span", class_="provider-group")
            doctor_address = doctor_group.parent
            doctor_phone = doctor_address.text.strip().split("\n")[3]

            print(doctor_name.text.strip())
            print(doctor_specialty.text.strip())
            print(doctor_group.text.strip())
            address_pt1 = (doctor_address.text.strip().split("\n")[1])
            address_pt2 = (doctor_address.text.strip().split("\n")[2])
            print(address_pt1.strip())
            print(address_pt2.strip())
            print(doctor_phone.strip())    
            print()
        time.sleep(1)  
    except: ("An exception occurred")  
    i += 1