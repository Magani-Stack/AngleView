from reportlab.lib import colors

from angle_view import BuildPDF

jd_table = {
    "data": [
        ['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']
    ],
    "style": [
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.green),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
    ],
    "type": "table"
}

data = [
    {"data": "New Title for Xmass", "style": "title", "type": "title"},
    {"data": "Paragraph 1 is here for Xmass", "style": "BodyText", "type": "BodyText"},
    {"data": "Paragraph 2 is here for Xmass", "style": "BodyText", "type": "BodyText"},
    {"data": "", "style": "BodyText", "type": "BodyText"},
    {"data": "Paragraph 3 is here for Xmass", "style": "BodyText", "type": "BodyText"},
    {"data": "Paragraph 4 is here for Xmass", "style": "BodyText", "type": "BodyText"},
    jd_table
]


class TestBuildPDF:

    def test_create_pdf(self):
        build_pdf = BuildPDF()
        build_pdf.create_from_json(data)
        build_pdf.build()
        buf = build_pdf.get_buffer().getvalue()
        with open("test_create_pdf_1.pdf", "wb") as f:
            f.write(buf)

    def test_create_table_from_json(self):
        build_pdf = BuildPDF()
        build_pdf.create_table_from_json(jd_table)
        build_pdf.build()
        buf = build_pdf.get_buffer().getvalue()
        with open("test_create_table_from_json_2.pdf", "wb") as f:
            f.write(buf)


if __name__ == "__main__":
    TestBuildPDF().test_create_pdf()
    TestBuildPDF().test_create_table_from_json()
