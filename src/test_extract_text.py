from extract_text import extract_text

######################################################################
# Test with a Word file
docx_file = "data/Dataset summaries and citations.docx"
print(f"Content of {docx_file}:\n")
print(extract_text(docx_file))

docx_file = "data/M.Sc. Applied Psychology.docx"
print(f"Content of {docx_file}:\n")
print(extract_text(docx_file))

docx_file = "data/Stats.docx"
print(f"Content of {docx_file}:\n")
print(extract_text(docx_file))


######################################################################
# Test with an Excel file
excel_file = "data/Loan amortisation schedule1.xlsx"
print(f"\nContent of {excel_file}:\n")
print(extract_text(excel_file))

excel_file = "data/Loan analysis.xlsx"
print(f"\nContent of {excel_file}:\n")
print(extract_text(excel_file))

excel_file = "data/party budget1.xlsx"
print(f"\nContent of {excel_file}:\n")
print(extract_text(excel_file))


######################################################################
# Test with a PDF file
pdf_file = "data/new-approaches-and-procedures-for-cancer-treatment.pdf"
print(f"\nContent of {pdf_file}:\n")
print(extract_text(pdf_file))

pdf_file = "data/Ocean_ecogeochemistry_A_review.pdf"
print(f"\nContent of {pdf_file}:\n")
print(extract_text(pdf_file))

pdf_file = "data/The_Plan_of_the_Giza_Pyramids.pdf"
print(f"\nContent of {pdf_file}:\n")
print(extract_text(pdf_file))

pdf_file = "data/The-Alchemist.pdf"
print(f"\nContent of {pdf_file}:\n")
print(extract_text(pdf_file))


######################################################################
"""# Test with a CSV file"""