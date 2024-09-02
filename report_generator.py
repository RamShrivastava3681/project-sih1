from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

class ReportGenerator:
    def __init__(self, report_dir, screenshot_dir):
        self.report_dir = report_dir
        self.screenshot_dir = screenshot_dir
        self.setup_directories()

    def setup_directories(self):
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def create_pdf(self, filename, sections):
        filepath = os.path.join(self.report_dir, filename)
        c = canvas.Canvas(filepath, pagesize=letter)
        width, height = letter

        y_position = height - 100  # Start position for the first section

        for section in sections:
            # Add section title
            c.setFont("Helvetica-Bold", 16)
            c.drawString(72, y_position, section.capitalize())
            y_position -= 30

            # Add screenshots for the section
            screenshot_number = 1
            while True:
                screenshot_path = os.path.join(self.screenshot_dir, f"facebook_{section}_{screenshot_number}.png")
                if not os.path.isfile(screenshot_path):
                    break
                try:
                    c.drawImage(screenshot_path, 50, y_position - 150, width=5*inch, height=3*inch)
                    y_position -= 200  # Adjust spacing for next image
                    if y_position < 100:  # Start new page if space is low
                        c.showPage()
                        y_position = height - 100
                except Exception as e:
                    print(f"Error adding image {screenshot_path}: {e}")
                    c.drawString(50, y_position - 150, "Error adding image: " + screenshot_path)
                    y_position -= 200

                screenshot_number += 1

            c.showPage()  # Start a new page for the next section

        c.save()
        print(f"Report saved as {filepath}.")

# Example usage
if __name__ == "__main__":
    report_gen = ReportGenerator("assets/reports", "assets/screenshots")
    sections = ["profile", "friends", "about", "posts"]
    report_gen.create_pdf("facebook_scraping_report.pdf", sections)