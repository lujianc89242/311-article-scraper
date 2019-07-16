def file_output(section):
    for element in section.contents:
        if(str(type(element)) == "<class 'bs4.element.Tag'>"):
            if(element.name == "a"):
                url_p = element.text + "(" + element['href'] + ")"
                document.add_paragraph(url_p)
                output_text = output_text + element.text.strip()
                print(url_p)

            if(element.name == "strong"):
                document.add_heading(element.text.strip(), level=3)
                output_text = output_text + element.text.strip()
                print(element.text, "(a bold text)")
            if(element.name == "br"):
                print("")
                # print("\n")
        if(str(type(element)) == "<class 'bs4.element.NavigableString'>"):
            document.add_paragraph(element)
            output_text = output_text + element
            print(element)
