#!/usr/bin/env python3
"""
SPPU Result Automation Script (Final Stable Version - Fully Functional)
Author: Paras + ChatGPT
"""
import os
import time
import pytesseract
import cv2
import logging
import numpy as np
import PyPDF2
from PIL import Image
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager

CONFIG = {
    'PDF_PATH': 'rollcalllist.pdf',
    'BASE_URL': 'https://onlineresults.unipune.ac.in/Result/Dashboard/Default',
    'OUTPUT_DIR': 'results',
    'RESULTS_FILE': 'class_results.txt',
    'MAX_RETRIES': 3,
    'WAIT_BETWEEN_REQUESTS': 2,
    'ELEMENT_WAIT_TIMEOUT': 20
}

class SPPUResultAutomation:
    def __init__(self):
        os.makedirs(CONFIG['OUTPUT_DIR'], exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(CONFIG['OUTPUT_DIR'], 'automation.log')),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.driver = None
        self.results = []
        self.failed_students = []

    def extract_students_from_pdf(self):
        students = []
        if not os.path.exists(CONFIG['PDF_PATH']):
            self.logger.error("PDF file not found")
            return students

        with open(CONFIG['PDF_PATH'], 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            lines = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    lines.extend(text.splitlines())
            lines = [line.strip() for line in lines if line.strip()]

            for i in range(0, len(lines) - 3, 4):
                roll = lines[i]
                mother = lines[i + 2]
                if roll.startswith('F') and len(mother) > 1:
                    students.append({
                        'roll_number': roll,
                        'mother_name': mother.title()
                    })
        return students

    def init_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--start-maximized')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.set_page_load_timeout(CONFIG['ELEMENT_WAIT_TIMEOUT'])
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def solve_captcha(self):
        try:
            captcha_element = self.driver.find_element(By.ID, 'imgCaptcha')
            location = captcha_element.location_once_scrolled_into_view
            size = captcha_element.size
            screenshot_path = os.path.join(CONFIG['OUTPUT_DIR'], 'fullpage.png')
            captcha_path = os.path.join(CONFIG['OUTPUT_DIR'], 'captcha_crop.png')
            self.driver.save_screenshot(screenshot_path)

            img = Image.open(screenshot_path)
            left = int(location['x'])
            top = int(location['y'])
            right = left + int(size['width'])
            bottom = top + int(size['height'])
            captcha_img = img.crop((left, top, right, bottom))
            captcha_img.save(captcha_path)

            text = self.extract_text_from_image(captcha_path)
            if not text.isdigit() or len(text) < 4:
                self.logger.warning("CAPTCHA OCR failed. Asking user manually...")
                try:
                    os.system(f'open "{captcha_path}"')
                except Exception:
                    pass
                text = input("Enter CAPTCHA manually: ")
            return text.strip()
        except Exception as e:
            self.logger.error(f"CAPTCHA error: {e}")
            return input("Enter CAPTCHA manually: ")

    def extract_text_from_image(self, image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, thresh = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
        resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        return pytesseract.image_to_string(resized, config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789').strip()

    def fetch_result(self, student):
        roll = student['roll_number']
        mother = student['mother_name']

        try:
            self.driver.get(CONFIG['BASE_URL'])
            WebDriverWait(self.driver, CONFIG['ELEMENT_WAIT_TIMEOUT']).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@value='Go for Result' and contains(@class, 'dashboardbtnwidth')]"))
            ).click()

            WebDriverWait(self.driver, CONFIG['ELEMENT_WAIT_TIMEOUT']).until(
                EC.presence_of_element_located((By.ID, 'txtRollNo'))
            )

            self.driver.find_element(By.ID, 'txtRollNo').clear()
            self.driver.find_element(By.ID, 'txtRollNo').send_keys(roll)
            self.driver.find_element(By.ID, 'txtMotherName').clear()
            self.driver.find_element(By.ID, 'txtMotherName').send_keys(mother)
            captcha = self.solve_captcha()
            self.driver.find_element(By.ID, 'txtCaptcha').clear()
            self.driver.find_element(By.ID, 'txtCaptcha').send_keys(captcha)
            self.driver.find_element(By.ID, 'btnSubmit').click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'lblPercentage'))
            )
            percentage = self.driver.find_element(By.ID, 'lblPercentage').text.replace('%', '').strip()
            return float(percentage)
        except (TimeoutException, NoSuchElementException, WebDriverException) as e:
            self.logger.warning(f"Failed for {roll}: {e}")
            return None

    def run(self):
        students = self.extract_students_from_pdf()
        self.logger.info(f"Total students found: {len(students)}")
        if not students:
            print("No students found.")
            return

        self.init_browser()
        success = []

        for i, student in enumerate(students):
            print(f"\n[{i+1}/{len(students)}] Roll: {student['roll_number']} | Mother: {student['mother_name']}")
            result = self.fetch_result(student)
            if result is not None:
                print(f"✅ {student['roll_number']} → {result}%")
                self.results.append({**student, 'percentage': result})
                success.append(result)
            else:
                self.failed_students.append(student)
                print(f"❌ Failed to get result.")
            time.sleep(CONFIG['WAIT_BETWEEN_REQUESTS'])

        self.driver.quit()

        avg = sum(success)/len(success) if success else 0
        with open(os.path.join(CONFIG['OUTPUT_DIR'], CONFIG['RESULTS_FILE']), 'w') as f:
            f.write(f"SPPU CLASS RESULTS SUMMARY\n")
            f.write("="*50 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Website: {CONFIG['BASE_URL']}\n\n")
            f.write("📊 STATISTICS\n")
            f.write("-"*20 + "\n")
            f.write(f"Total Students: {len(students)}\n")
            f.write(f"Successfully Processed: {len(success)}\n")
            f.write(f"Failed to Process: {len(self.failed_students)}\n")
            f.write(f"Success Rate: {(len(success)/len(students))*100:.1f}%\n\n")
            f.write(f"Average Percentage: {avg:.2f}%\n\n")
            if self.failed_students:
                f.write("❌ FAILED STUDENTS\n")
                f.write("-"*20 + "\n")
                for fs in self.failed_students:
                    f.write(f"• {fs['roll_number']}\n")

        print(f"\n🎯 Completed. Average: {avg:.2f}%")

if __name__ == '__main__':
    SPPUResultAutomation().run()