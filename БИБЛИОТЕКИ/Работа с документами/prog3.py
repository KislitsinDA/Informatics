from doсxtpl import DocxTemplate

def create_traiding_sheet(class_name, subject_name, tpl_name="tpl.docx", *info):
    info = sorted(info, key=lambda x: x[0])
    doc = DocxTemplate(tpl_name)
    marks = [{"num": i + 1, "fio": info[i][0], "mark": info[i][1]} for i in range(len(info))]
    context = {
        "class_name": class_name,
        "subject_name": subject_name,
        "marks": marks,
    }
    doc.render(context)
    doc.save("res.docx")


create_traiding_sheet("ЗИ", "Математика", "tpl.docx",
                      ("Петров Петр", "5"),
                      ("Иванов Иван", "5"),
                      ("Сергеев Сергей", "3"),
                      ("Никитин Никита", "4"))
