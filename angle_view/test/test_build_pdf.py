from angle_view import BuildPDF


class TestBuildPDF:

    def test_create_pdf(self):
        data = [
            {"data": "New Title for Xmass", "style": "title"},
            {"data": "Paragraph 1 is here for Xmass", "style": "BodyText"},
            {"data": "Paragraph 2 is here for Xmass", "style": "BodyText"},
            {"data": "", "style": "BodyText"},
            {"data": "Paragraph 3 is here for Xmass", "style": "BodyText"},
            {"data": "Paragraph 4 is here for Xmass", "style": "BodyText"}
        ]
        build_pdf = BuildPDF()
        build_pdf.create_from_json(data)
        build_pdf.build()
        buf = build_pdf.get_buffer().getvalue()
        with open("test_create_pdf_1.pdf", "wb") as f:
            f.write(buf)


if __name__ == "__main__":
    TestBuildPDF().test_create_pdf()
