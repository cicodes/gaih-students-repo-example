cv1 = {
    "name": "Oğuzhan",
    "age": "26",
    "city": "İstanbul",
    "profession": "Software Engineer",
    "language": ["turkish", "english"]
}

cv2 = {
    "name": "Serhat",
    "age": "23",
    "city": "Bursa",
    "profession": "Psychology",
    "language": ["turkish"]
}

cv3 = {
    "name": "Kutluhan",
    "age": "26",
    "city": "Balıkesir",
    "profession": "Network Operations",
    "language": ["turkish", "english", "spanish"]
}

cv4 = {
    "name": "Melih",
    "age": "26",
    "city": "Eskişehir",
    "profession": "Financial Analysis",
    "language": ["turkish", "arabic"]
}

cv5 = {
    "name": "Mete",
    "age": "25",
    "city": "Ankara",
    "profession": "Interior Design",
    "language": ["turkish", "russian"]
}

cvs={}
cvs[1] = cv1
cvs[2] = cv2
cvs[3] = cv3
cvs[4] = cv4
cvs[5] = cv5


for id, info in cvs.items():
    print("\nCV Number:", id)
    for key in info:
        print(key.capitalize() + ':', info[key])

