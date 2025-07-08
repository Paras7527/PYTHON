import os
import sys
import time
import fitz  # PyMuPDF

def extract_students(pdf_path):
    if not os.path.exists(pdf_path):
        print("❌ PDF file not found!")
        exit()

    log_border = "-" * 50
    timestamp = time.ctime()
    log_filename = f"ExtractLog_{timestamp.replace(' ', '_').replace(':', '_')}.log"
    csv_filename = "Student_List.csv"

    doc = fitz.open(pdf_path)
    count = 0

    with open(csv_filename, "w") as csv_file:
        csv_file.write("Seat No,Student Name,Mother Name,PRN\n")
        for page in doc:
            lines = page.get_text().split('\n')
            for line in lines:
                if line.strip().startswith("F1"):
                    parts = line.strip().split()
                    if len(parts) >= 5:
                        seat_no = parts[0]
                        prn = parts[-1]
                        mother_name = parts[-2]
                        student_name = " ".join(parts[1:-2])
                        csv_file.write(f"{seat_no},{student_name},{mother_name},{prn}\n")
                        count += 1

    with open(log_filename, "w") as log_file:
        log_file.write(log_border + "\n")
        log_file.write("SPPU Result Automation Log\n")
        log_file.write(log_border + "\n")
        log_file.write(f"Processed file: {pdf_path}\n")
        log_file.write(f"Total students extracted: {count}\n")
        log_file.write(f"Output CSV: {csv_filename}\n")
        log_file.write(f"Log created: {timestamp}\n")
        log_file.write(log_border + "\n")

    print(f"\n✅ {count} students extracted.")
    print(f"📄 CSV File: {csv_filename}")
    print(f"📝 Log File: {log_filename}")

def main():
    border = "-" * 50
    print(border)
    print("----- SPPU Student Result Extractor (CUI) -----")
    print(border)

    if len(sys.argv) == 2:
        if sys.argv[1] in ["--h", "--H"]:
            print("Help: This script extracts student details from PDF.")
            print("Usage: python StudentResultAutomationScript.py <file.pdf>")
        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage: python StudentResultAutomationScript.py result.pdf")
        else:
            extract_students(sys.argv[1])
    else:
        print("❌ Invalid arguments. Use --h for help or --u for usage.")

    print(border)
    print("------------ Thank You for Using -------------")
    print(border)

if __name__ == "__main__":
    main()
