import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
from tkinter import messagebox



# Dicionário de produtos com o nome da linha como chave
produtos_por_linha = {
    "Advantage": ["02.1209","02.1210","02.1217", "02.1214", "02.1197", "02.1196", "02.1195","03.2093", "03.2094"],
    "Confort": ["06.5183", "06.5184", "06.5185", "06.5186", "06.5187", "06.5188", "06.5189", "06.5191", "06.5198", "06.5199", "", "", "", ""],
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
    "Vittoria": ["06.5217", "06.5218"]
}

# Dicionário de produtos com o nome da linha como chave
produtos_por_codigo = {
    "02.1209": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": ["./img/02.1209.16.jpg", "./img/02.1209.44.jpg"]
    },
    "02.1210": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1217": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "02.1214": {
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
    "03.2093": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2094": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5183": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5184": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5185": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5186": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5187": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5188": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5189": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5191": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5198": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "06.5199": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
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
    "03.2093": {
        "Nome": "Produto A",
        "Medida": "100x50 cm",
        "Peso": "500 g",
        "Padrões": [16, 38],
        "Imagem": "./img/02.1209.16.jpg"
    },
    "03.2094": {
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

def verificar_login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
        login_window.destroy()
    else:
        messagebox.showerror("Erro de login", "Nome de usuário ou senha incorretos")


# Criar a janela de login
login_window = tk.Tk()
login_window.title("Tela de Login")

tk.Label(login_window, text="Nome de usuário:").pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

tk.Label(login_window, text="Senha:").pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack()

tk.Button(login_window, text="Login", command=verificar_login).pack()

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
        texto_informacoes_widget.insert(tk.END, texto_informacoes)
        texto_informacoes_widget.pack()

        # Carrossel de imagens
        imagens = informacoes_produto.get("Imagem", [])
        if imagens:
            carrossel_imagens = CarrosselImagens(janela_informacoes, imagens)
            carrossel_imagens.pack()

class CarrosselImagens(tk.Frame):
    def __init__(self, parent, imagens, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.imagens = imagens
        self.indice_atual = 0
        self.imagens_tk = [None] * len(self.imagens)

        self.label_frame = tk.LabelFrame(self, text="Padrão da imagem")
        self.label_frame.pack(side="right", padx=10, pady=10, fill="y")

        self.label_imagem = tk.Label(self)
        self.label_imagem.pack(side="left", padx=10)

        self.botao_anterior = tk.Button(self, text="<", command=self.mostrar_anterior)
        self.botao_anterior.pack(side="left")

        self.botao_proximo = tk.Button(self, text=">", command=self.mostrar_proximo)
        self.botao_proximo.pack(side="left")

        self.label_padrao = tk.Label(self.label_frame, text="")
        self.label_padrao.pack()

        self.mostrar_imagem_atual()

    def mostrar_imagem_atual(self):
        imagem_path = self.imagens[self.indice_atual]
        if self.imagens_tk[self.indice_atual] is None:
            imagem = Image.open(imagem_path)
            imagem = imagem.resize((400, 400), Image.LANCZOS)
            self.imagens_tk[self.indice_atual] = ImageTk.PhotoImage(imagem)
        
        self.label_imagem.configure(image=self.imagens_tk[self.indice_atual])

        # Determina o padrão da imagem pelo nome do arquivo
        nome_arquivo = self.imagens[self.indice_atual]
        padrao = nome_arquivo.split('.')[-1]

        # Atualiza o texto do padrão na caixa ao lado da imagem
        self.label_padrao.configure(text=f"Padrão: {padrao}")

    def mostrar_anterior(self):
        self.indice_atual = (self.indice_atual - 1) % len(self.imagens)
        self.mostrar_imagem_atual()

    def mostrar_proximo(self):
        self.indice_atual = (self.indice_atual + 1) % len(self.imagens)
        self.mostrar_imagem_atual()

# Cria a janela principal
janela = tk.Tk()
janela.title("Pesquisa de Produtos")

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
lista_produtos.bind("<Button-1>", mostrar_codigos)

# Associa os eventos de teclado na lista de produtos para seleção
lista_produtos.bind("<Return>", mostrar_codigos)
lista_produtos.bind("<Up>", lambda event: lista_produtos.yview_scroll(-1, "units"))
lista_produtos.bind("<Down>", lambda event: lista_produtos.yview_scroll(1, "units"))

# Cria a lista de códigos
lista_codigos = tk.Listbox(frame_principal)

# Inicialmente, ocultamos a lista de códigos
lista_codigos.grid_remove()

# Associa o evento de clique na lista de códigos
lista_codigos.bind("<Button-1>", exibir_informacoes_produto)

# Associa os eventos de teclado na lista de códigos para seleção
lista_codigos.bind("<Return>", exibir_informacoes_produto)
lista_codigos.bind("<Up>", lambda event: lista_codigos.yview_scroll(-1, "units"))
lista_codigos.bind("<Down>", lambda event: lista_codigos.yview_scroll(1, "units"))

# Executa o loop principal da aplicação
janela.mainloop()
