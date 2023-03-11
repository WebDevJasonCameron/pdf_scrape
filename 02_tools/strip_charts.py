import tabula

tables = tabula.read_pdf("sample_01.pdf", pages="all")

# print(tables)
df = tables[0]
print(df)

for t in tables:
    print(t)
    print("================================================")
