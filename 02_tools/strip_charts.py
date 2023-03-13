import tabula

tables = tabula.read_pdf(
    "/Users/jasoncameron/00_Drive/Core/DM/03_Sources/01_Basic_Rules/03_Chapter_03.pdf", pages="all")

# print(tables)
df = tables[0]
print(df)

for t in tables:
    print(t)
    print("================================================")
