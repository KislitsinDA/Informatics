translated_text = ""


def translate(text):
    global translated_text
    alp = "бвгджзйклмнпрстфхцчшщъь"
    for i in text.split():
        for j in i:
            if j.lower() in alp:
                translated_text += j
        translated_text += " "


translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. "
          "Достаточно небольшой тренировки - и вы сможете это делать.")
print(" ".join(translated_text.split()))