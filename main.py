import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
from tkinter import messagebox
import sys
import os




# Dicionário de produtos com o nome da linha como chave
produtos_por_linha = {
    "Advantage": ["02.1209","02.1210","02.1217", "02.1214", "03.2093", "03.2094"],
    "Confort": ["06.5183", "06.5184", "06.5185", "06.5186", "06.5187", "06.5188", "06.5189","06.5190", "06.5191", "06.5198", "06.5199"],
    "Elegance": ["03.2085", "02.2088", "02.2089", "03.2087"],
    "Evolution Plus": ["06.5101", "06.5102", "06.5103", "06.5104", "06.5106", "06.5107", "06.5135", "06.5136", "06.5140", "06.5141", "06.5200", "06.5201"],
    "Gênova Plus": ["02.1188", "02.1189", "02.1190", "02.1191", "02.1192"],
    "Italy": ["08.7037", "08.7038", "08.7039", "08.7040", "08.7041"],
    "New": ["06.5171", "06.5172", "06.5173", "06.5174", "06.5175", "06.5176", "06.5177", "06.5178", "06.5179", "06.5180", "06.5181", "06.5182", "06.5121", "06.5122"],
    "New Baby": ["03.2095", "03.2096", "02.1219", "02.1220", "10.9207", "04.3021", "04.3022"],
    "Primacy": ["02.1198", "02.1197", "02.1196", "02.1195", "03.2086"],
    "Paris": ["06.5203", "06.5204", "06.5205", "06.5206", "06.5207", "06.5208", "06.5209", "06.5210", "06.5211", "06.5212", "06.5213", "06.5215", "06.5216"],
    "Supreme": ["02.1207", "02.1208", "02.1194", "02.1221",],
    "Top Class": ["06.5159", "06.5160", "06.5161", "06.5162", "06.5163", "06.5164", "06.5165", "06.5166", "06.5167", "06.5168", "06.5169", "06.5170", "06.5121", "06.5122", "", ""],
    "Verona": ["01.0019", "01.0020", "01.0021"],
    "Encanto": ["02.1223", "03.2097", "03.2098", "04.3023", "04.3024"],
    "Vittoria": ["06.5217", "06.5218"],
    "Encanto": ["02.1223", "03.2097","03.2098","06.3023","06.3024"]
}

# Dicionário de produtos com o nome da linha como chave
produtos_por_codigo = {
    "02.1209": {
        "Nome": "GRPA 4P 3G ADVANTAGE",
        "Medida": "1195X2038X465mm",
        "Peso": "75,1kg",
        "Padrões": [16, 22, 44],
        "Imagem": ["./img/02.1209.16.jpg","./img/02.1209.22.jpg", "./img/02.1209.44.jpg"]
    },
    "02.1210": {
        "Nome": "GRPA 6P 4G ADVANTAGE",
        "Medida": "1788x2038x465mm",
        "Peso": "111,6kg",
        "Padrões": [16, 22, 30, 44],
        "Imagem": ["./img/02.1210.16.jpg","./img/02.1210.22.jpg","./img/02.1210.44.jpg"]
    },
    "02.1217": {
        "Nome": "GRPA 7P 4G C/ESPELHO ADVANTAGE",
        "Medida": "1788X2038X463mm",
        "Peso": "117,3kg",
        "Padrões": [16, 22, 38, 44],
        "Imagem": ["./img/02.1217.16.jpg","./img/02.1217.22.jpg","./img/02.1217.38.jpg","./img/02.1217.44.jpg"]
    },
    "02.1214": {
        "Nome": "GRPA 4P 3G C/CAMA BAU ADVANTAGE",    
        "Medida": "1567X2038X465mm",
        "Peso": "102,7kg",
        "Padrões": [16, 38, 59],
        "Imagem": ["./img/02.1214.16.jpg", './img/02.1214.38.jpg', './img/02.1214.44.jpg','./img/02.1214.59 azul.jpg', './img/02.1214.59 rosa.jpg']
    },
    "03.2093": {
        "Nome": "CMDA MULTI USO 1P ADVANTAGE",
        "Medida": "480x1423x386mm",
        "Peso": "25kg",
        "Padrões": [16, 22, 44],
        "Imagem": ["./img/03.2093.16.jpg", "./img/03.2093.22.jpg", "./img/03.2093.44.jpg"]
    },
    "03.2094": {
        "Nome": "CMDA 1P 5G SPTA ADVANTAGE",
        "Medida": "907x911x465mm",
        "Peso": "36,8kg",
        "Padrões": [22, 30, 38, 44],
        "Imagem": ["./img/03.2094.22.jpg", "./img/03.2094.38.jpg", "./img/03.2094.44.jpg"]
    },
    "06.5183": {
        "Nome": "COZINHA PNLR 2P CONFORT",
        "Medida": "465x2160x448mm",
        "Peso": "40,5kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5183.60.jpg", "./img/06.5183.64.jpg", "./img/06.5183.66.jpg"]
    },
    "06.5184": {
        "Nome": "CZNH ARM AEREO 1P BASC CONFORT",
        "Medida": "1200x720x296mm",
        "Peso": "28,4kg",
        "Padrões": [60],
        "Imagem": ["./img/06.5184.60.jpg"]
    },
    "06.5185": {
        "Nome": "CZNH ARM AER 1P CONFORT",
        "Medida": "600x720x296mm",
        "Peso": "13,6kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5185.60.jpg", "./img/06.5185.64.jpg", "./img/06.5185.66.jpg"]
    },
    "06.5186": {
        "Nome": "CZNH ARM GELAD CONFORT",
        "Medida": "800x323x296mm",
        "Peso": "9,7kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5186.60.jpg", "./img/06.5186.64.jpg", "./img/06.5186.66.jpg"]
    },
    "06.5187": {
        "Nome": "CZNH GBNT 4G CONFORT",
        "Medida": "600x965x468mm",
        "Peso": "32,1kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5187.60.jpg", "./img/06.5187.64.jpg", "./img/06.5187.66.jpg"]
    },
    "06.5188": {
        "Nome": "CZNH GBNT 2P CONFORT",
        "Medida": "1200x965x468mm",
        "Peso": "45,2kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5188.60.jpg", "./img/06.5188.64.jpg", "./img/06.5188.66.jpg"]
    },
    "06.5189": {
        "Nome": "CZNH 1P 4G MICR CONFORT",
        "Medida": "600x2160x448mm",
        "Peso": "53,3Kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5189.60.jpg", "./img/06.5189.64.jpg", "./img/06.5189.66.jpg"]
    },
    "06.5190": {
        "Nome": "CZNH GBNT 2P 4G P/PIA CONFORT",
        "Medida": "1200x965x518mm",
        "Peso": "54,9kg",
        "Padrões": [60, 64],
        "Imagem": ["./img/06.5190.60.jpg", "./img/06.5190.64.jpg",]
    },
    "06.5191": {
        "Nome": "CZNH GBNT 1P CONFORT",
        "Medida": "600x965x468mm",
        "Peso": "24,3kg",
        "Padrões": [60, 64, 66],
        "Imagem": ["./img/06.5191.60.jpg", "./img/06.5191.64.jpg", "./img/06.5191.66.jpg"]
    },
    "06.5198": {
        "Nome": "CZNH ARM AER 1P 90° CONFORT",
        "Medida": "865x720x595mm",
        "Peso": "24,4kg",
        "Padrões": [60, 64],
        "Imagem": ["./img/06.5198.60.jpg", "./img/06.5198.64.jpg"]
    },
    "06.5199": {
        "Nome": "CZNH GBNT 1P 90° CONFORT",
        "Medida": "865x965x595mm",
        "Peso": "39,7kg",
        "Padrões": [60, 64],
        "Imagem": ["./img/06.5199.60.jpg", "./img/06.5199.64.jpg"]
    },
    "03.2085": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.2088": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.2089": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2087": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5101": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5102": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5103": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5104": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5106": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5107": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5135": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5136": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5140": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5141": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5200": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5201": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1188": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1189": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1190": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1191": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1192": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "08.7037": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "08.7038": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "08.7039": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "08.7040": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "08.7041": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5171": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5172": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5173": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5174": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5175": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5176": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5177": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5178": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5179": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5180": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5181": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5182": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5121": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5122": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2095": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2096": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1219": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1220": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9207": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "04.3021": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "04.30222": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1198": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1197": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1196": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1195": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2086": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5203": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5204": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5205": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5206": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5207": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5208": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5209": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5210": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5211": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5212": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5213": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5215": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5216": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1207": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1208": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1194": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1221": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5159": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5160": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5161": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5162": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5163": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5164": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5165": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5166": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5167": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5168": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5169": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5170": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9200": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9201": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9202": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9203": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9204": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9205": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9206": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2097": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2098": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2099": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "10.9170": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
}
}

# Função para fechar o sistema inteiro
def close_system():     
    sys.exit()

# Função para validar as credenciais
def validate_credentials(username, password):
    return username == "admin" and password == "admin"

# Função para lidar com o evento de login
def on_login():
    username = entry_username.get()
    password = entry_password.get()
    if validate_credentials(username, password):
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        login_window.destroy()
    else:
        messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")

# Função para encerrar o programa       
def close_program():
    close_system()

# Função para centralizar uma janela
def centralizar_janela(janela):
    largura_janela = janela.winfo_reqwidth()
    altura_janela = janela.winfo_reqheight()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posicao_x = int((largura_tela / 2) - (largura_janela / 2))
    posicao_y = int((altura_tela / 2) - (altura_janela / 2))
    janela.geometry(f"+{posicao_x}+{posicao_y}")
                    
# Função para fechar a janela ao pressionar Esc
def fechar_com_esc(event):
    close_system()

# Criar a janela de login
login_window = tk.Tk()
login_window.title("Login")

# Centralizar a janela de login na tela
centralizar_janela(login_window)

# Adicionar vinculação para fechar com Esc
login_window.bind("<Escape>", fechar_com_esc)

tk.Label(login_window, text="Nome de usuário").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(login_window)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_username.focus_set()  # Definir o foco no campo de nome de usuário

tk.Label(login_window, text="Senha").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(login_window, show='*')
entry_password.grid(row=1, column=1, padx=10, pady=10)

btn_login = tk.Button(login_window, text="Login", command=on_login)
btn_login.grid(row=2, column=0, columnspan=2, pady=10)

btn_close = tk.Button(login_window, text="Fechar", command=close_program)
btn_close.grid(row=3, column=0, columnspan=2, pady=10)

# Bind da tecla Enter para navegação
entry_username.bind("<Return>", lambda event: entry_password.focus_set())
entry_password.bind("<Return>", lambda event: btn_login.invoke())

# Iniciar o loop principal da janela de login
login_window.mainloop()

def pesquisar_produto(event=None):
    texto_pesquisa = entrada_pesquisa.get().lower()
    lista_produtos.delete(0, tk.END)
    lista_codigos.grid_remove()  # Esconde a lista de códigos

    if texto_pesquisa:
        # Filtra linhas que contêm o texto pesquisado
        produtos_coincidentes = [produto for produto in produtos_por_linha if texto_pesquisa in produto.lower()]
        # Preenche a lista de produtos com os resultados filtrados
        for produto in produtos_coincidentes:
            lista_produtos.insert(tk.END, produto)
        lista_produtos.configure(height=len(produtos_coincidentes))
    else:
        # Quando o texto de pesquisa está vazio, a lista de produtos deve estar vazia
        lista_produtos.delete(0, tk.END)

def mostrar_codigos(event=None):
    if lista_produtos.curselection():
        lista_codigos.delete(0, tk.END)
        indice_selecionado = lista_produtos.curselection()[0]
        linha_selecionada = lista_produtos.get(indice_selecionado)
        codigos = produtos_por_linha.get(linha_selecionada, [])

        for codigo in codigos:
            lista_codigos.insert(tk.END, codigo)

        # Mostra a lista de códigos
        lista_codigos.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

def exibir_informacoes_produto(event=None):
    if lista_codigos.curselection():
        indice_selecionado = lista_codigos.curselection()[0]
        codigo_selecionado = lista_codigos.get(indice_selecionado)
        informacoes_produto = produtos_por_codigo.get(codigo_selecionado, {})

        # Cria uma nova janela para exibir as informações do produto
        janela_informacoes = tk.Toplevel(janela)
        janela_informacoes.title("Informações do Produto")

        # Widget de texto para exibir as informações
        texto_informacoes = ""
        for chave, valor in informacoes_produto.items():
            if chave != "Imagem":
                texto_informacoes += f"{chave}: {valor}\n"

        texto_informacoes_widget = tk.Text(janela_informacoes, wrap="word")
        texto_informacoes_widget.insert("1.0", texto_informacoes)
        texto_informacoes_widget.configure(state="disabled")  # Define o estado como desabilitado para tornar o texto não editável
        texto_informacoes_widget.pack(padx=10, pady=10)
        
        # Adiciona um manipulador de evento para permitir a seleção de texto
        texto_informacoes_widget.tag_configure("readonly", foreground="black")
        texto_informacoes_widget.tag_bind("readonly", "<1>", lambda e: "break")

        if "Imagem" in informacoes_produto:
            imagens = informacoes_produto["Imagem"]
            carrossel = CarrosselImagens(janela_informacoes, imagens)
            carrossel.pack()

class CarrosselImagens(tk.Frame):
    def __init__(self, parent, imagens, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.imagens = imagens
        self.indice_atual = 0
        self.imagens_tk = [None] * len(self.imagens)

        self.label_frame = tk.LabelFrame(self, text="Padrões")
        self.label_frame.pack(side="right", padx=10, pady=10, fill="y")

        self.label_imagem = tk.Label(self)
        self.label_imagem.pack(side="left", padx=10)

        self.botao_anterior = tk.Button(self, text="<", command=self.mostrar_anterior)
        self.botao_anterior.pack(side="left")

        self.botao_proximo = tk.Button(self, text=">", command=self.mostrar_proximo)
        self.botao_proximo.pack(side="left")

        self.label_padrao = tk.Label(self.label_frame, text="", justify="center")
        self.label_padrao.pack(pady=(10, 0))  # Adiciona um espaço acima do nome do arquivo

        self.label_nome_arquivo = tk.Label(self.label_frame, text="", justify="center")
        self.label_nome_arquivo.pack()

        self.mostrar_imagem_atual()

    def mostrar_imagem_atual(self):
        imagem_path = self.imagens[self.indice_atual]
        if self.imagens_tk[self.indice_atual] is None:
            imagem = Image.open(imagem_path)
            imagem = imagem.resize((400, 400), Image.LANCZOS)
            self.imagens_tk[self.indice_atual] = ImageTk.PhotoImage(imagem)
        
        self.label_imagem.configure(image=self.imagens_tk[self.indice_atual])

        # Atualiza o texto do nome do arquivo na caixa ao lado da imagem
        nome_arquivo_com_extensao = os.path.basename(imagem_path)
        nome_arquivo, _ = os.path.splitext(nome_arquivo_com_extensao)  # Remove a extensão
        self.label_padrao.configure(text="Padrão do produto")
        self.label_nome_arquivo.configure(text=f"{nome_arquivo}")

    def mostrar_anterior(self):
        self.indice_atual = (self.indice_atual - 1) % len(self.imagens)
        self.mostrar_imagem_atual()

    def mostrar_proximo(self):
        self.indice_atual = (self.indice_atual + 1) % len(self.imagens)
        self.mostrar_imagem_atual()

# Função para abrir a janela de autenticação de criação de linha
def abrir_autenticacao_criacao_linha():
    janela_autenticacao = tk.Toplevel(janela)
    janela_autenticacao.title("Autenticação para Criação de Linha")

    tk.Label(janela_autenticacao, text="Nome de usuário").grid(row=0, column=0, padx=10, pady=10)
    entry_autenticacao_username = tk.Entry(janela_autenticacao)
    entry_autenticacao_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela_autenticacao, text="Senha").grid(row=1, column=0, padx=10, pady=10)
    entry_autenticacao_password = tk.Entry(janela_autenticacao, show='*')
    entry_autenticacao_password.grid(row=1, column=1, padx=10, pady=10)

    def autenticar():
        username = entry_autenticacao_username.get()
        password = entry_autenticacao_password.get()
        if username == "admin" and password == "0000":
            messagebox.showinfo("Sucesso", "Autenticação bem-sucedida!")
            janela_autenticacao.destroy()
            abrir_janela_criacao_linha()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")

    btn_autenticar = tk.Button(janela_autenticacao, text="Autenticar", command=autenticar)
    btn_autenticar.grid(row=2, column=0, columnspan=2, pady=10)


def abrir_janela_criacao_linha():
    janela_criacao_linha = tk.Toplevel(janela)
    janela_criacao_linha.title("Criar Nova Linha")

    tk.Label(janela_criacao_linha, text="Nome da Nova Linha:").grid(row=0, column=0, padx=10, pady=10)
    entry_nome_linha = tk.Entry(janela_criacao_linha)
    entry_nome_linha.grid(row=0, column=1, padx=10, pady=10)

    def criar_linha():
        nome_linha = entry_nome_linha.get().strip()
        if nome_linha in produtos_por_linha:
            messagebox.showerror("Erro", "Linha já existe. Escolha outro nome.")
        else:
            produtos_por_linha[nome_linha] = []
            messagebox.showinfo("Sucesso", "Linha criada com sucesso!")
            janela_criacao_linha.destroy()
            preencher_codigos(nome_linha)

    btn_criar = tk.Button(janela_criacao_linha, text="Criar", command=criar_linha)
    btn_criar.grid(row=1, column=0, columnspan=2, pady=10)

def preencher_codigos(nome_linha):
    janela_preenchimento = tk.Toplevel(janela)
    janela_preenchimento.title(f"Preencher Códigos - {nome_linha}")

    tk.Label(janela_preenchimento, text="Insira os códigos dos produtos, separados por vírgula:").grid(row=0, column=0, padx=10, pady=10)
    entry_codigos = tk.Entry(janela_preenchimento, width=50)
    entry_codigos.grid(row=1, column=0, padx=10, pady=10)

    def salvar_codigos():
        codigos = entry_codigos.get().split(',')
        produtos_por_linha[nome_linha] = [codigo.strip() for codigo in codigos]
        messagebox.showinfo("Sucesso", "Códigos salvos com sucesso!")
        janela_preenchimento.destroy()

    btn_salvar = tk.Button(janela_preenchimento, text="Salvar", command=salvar_codigos)
    btn_salvar.grid(row=2, column=0, pady=10)

# Cria a janela principal
janela = tk.Tk()
janela.title("Pesquisa de Produtos")

# Centralizar a janela principal na tela
centralizar_janela(janela)

# Adicionar vinculação para fechar com Esc
janela.bind("<Escape>", fechar_com_esc)
# Define o número máximo de linhas que a lista de linhas deve exibir
num_maximo_linhas = len(produtos_por_linha)

# Cria um frame principal para melhor organização
frame_principal = ttk.Frame(janela, padding=10)
frame_principal.grid(row=0, column=0, sticky='nsew')

# Cria o rótulo para a entrada de pesquisa
rotulo_linha = ttk.Label(frame_principal, text="Linha:")
rotulo_linha.grid(row=0, column=0, padx=10, pady=5, sticky='w')

# Cria a entrada de texto para pesquisa
entrada_pesquisa = ttk.Entry(frame_principal, width=30)
entrada_pesquisa.grid(row=0, column=1, padx=10, pady=5, sticky='w')
entrada_pesquisa.bind("<KeyRelease>", pesquisar_produto)

# Cria a lista de linhas (produtos) com tamanho constante
lista_produtos = tk.Listbox(frame_principal, height=num_maximo_linhas)
lista_produtos.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# Associa o evento de clique na lista de produtos
lista_produtos.bind("<Double-Button-1>", mostrar_codigos)

# Associa os eventos de teclado na lista de produtos para seleção
lista_produtos.bind("<Return>", mostrar_codigos)
lista_produtos.bind("<Up>", lambda event: lista_produtos.yview_scroll(-1, "units"))
lista_produtos.bind("<Down>", lambda event: lista_produtos.yview_scroll(1, "units"))

# Cria a lista de códigos
lista_codigos = tk.Listbox(frame_principal)

# Inicialmente, ocultamos a lista de códigos
lista_codigos.grid_remove() 

# Associa o evento de clique na lista de códigos
lista_codigos.bind("<Double-Button-1>", exibir_informacoes_produto)

# Associa os eventos de teclado na lista de códigos para seleção
lista_codigos.bind("<Return>", exibir_informacoes_produto)
lista_codigos.bind("<Up>", lambda event: lista_codigos.yview_scroll(-1, "units"))
lista_codigos.bind("<Down>", lambda event: lista_codigos.yview_scroll(1, "units"))

# Botão para abrir a janela de autenticação para criação de linha
btn_criar_linha = tk.Button(janela, text="Criar Nova Linha", command=abrir_autenticacao_criacao_linha)
btn_criar_linha.grid(row=1, column=0, pady=10)

# Executa o loop principal da aplicação
janela.mainloop()
