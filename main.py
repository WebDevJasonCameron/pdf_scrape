import re

from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("sample.pdf"):
#     for element in page_layout:
#         print(element)

write_file = open("text_file.txt", "a")

text = extract_text("sample.pdf")
write_file.writelines(text)
print("done")

write_file.close()
