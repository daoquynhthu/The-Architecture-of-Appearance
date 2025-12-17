import os
import markdown
from pathlib import Path
from xhtml2pdf import pisa
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import xhtml2pdf.default

base_dir = Path(r"d:\Philosophy\Book")
output_file = r"d:\Philosophy\Manifestationism_Book.pdf"
font_path = r"d:\Philosophy\simhei.ttf"

# Define the order explicitly to ensure correct sequence
files = [
    "00_Preface.md",
    "00_Meta_Discourse.md",
    "01_The_Primal_Fact.md",
    "02_Weak_Assertion.md",
    "03_Existence.md",
    "04_Manifestation_Structure.md",
    "05_Subject_Emergence.md",
    "Part1_Summary_The_View_From_The_Foundation.md",
    "06_Manifestation_Dynamics.md",
    "07_Stability_Genesis.md",
    "08_Sustainability_And_Normative_Dynamics.md",
    "09_The_Manifestation_Status_Of_Logic.md",
    "Part2_Summary_Navigation_In_The_Storm.md",
    "10_The_Construction_Of_World.md",
    "11_Others_And_Intersubjectivity.md",
    "12_Meaning_And_Language.md",
    "13_Science_And_Objectivity.md",
    "Part3_Summary_Surviving_In_Normativity.md",
    "14_Limit_Experiences.md",
    "15_Conclusion_Living_Within_Manifestation.md"
]

def create_pdf():
    print(f"Creating PDF: {output_file}")
    
    # Register font directly with ReportLab
    try:
        pdfmetrics.registerFont(TTFont('SimHei', font_path))
        print(f"Successfully registered font: SimHei from {font_path}")
        
        # HACK: Force xhtml2pdf to use our font as default
        # Note: DEFAULT_FONT expects keys like 'helvetica' (the default) to be overridden, 
        # or we need to ensure CSS font-family maps correctly. 
        # But 'AttributeError: NoneType object has no attribute lower' suggests a missing font mapping.
        # Let's try to update the font mapping more aggressively.
        xhtml2pdf.default.DEFAULT_FONT = {
            "helvetica": "SimHei",
            "courier": "SimHei",
            "times": "SimHei",
            "zapfdingbats": "SimHei",
            "symbol": "SimHei",
        }
    except Exception as e:
        print(f"Error registering font: {e}")
        return
    
    full_html = ""

    # CSS with Font Registration
    # Note: xhtml2pdf requires explicit font definition for non-latin characters
    css = f"""
    <style>
        body {{
            font-family: "SimHei";
            font-size: 12pt;
            line-height: 1.5;
        }}
        h1 {{
            font-size: 24pt;
            text-align: center;
            page-break-before: always;
        }}
        h2 {{
            font-size: 18pt;
            margin-top: 20px;
        }}
        h3 {{
            font-size: 14pt;
        }}
        p {{
            margin-bottom: 10px;
            text-align: justify;
        }}
        code {{
            font-family: monospace;
            background-color: #f0f0f0;
        }}
        blockquote {{
            margin-left: 20px;
            border-left: 4px solid #ccc;
            padding-left: 10px;
            color: #555;
        }}
    </style>
    """

    content_html = ""
    for filename in files:
        filepath = base_dir / filename
        if not filepath.exists():
            print(f"Warning: File not found: {filename}")
            continue

        print(f"Processing {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert Markdown to HTML
        html_segment = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        content_html += html_segment + "\n"

    # Wrap in full HTML structure
    full_html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        {css}
    </head>
    <body>
        <div style="text-align: center; padding-top: 100px; padding-bottom: 100px;">
            <h1 style="font-size: 36pt; page-break-before: auto;">显现的架构：显现论</h1>
            <h2 style="font-size: 20pt; color: #555;">The Architecture of Appearance</h2>
        </div>
        <div style="page-break-after: always;"></div>
        {content_html}
    </body>
    </html>
    """

    # Write HTML to a temp file for debugging (optional)
    # with open("temp_book.html", "w", encoding="utf-8") as f:
    #     f.write(full_html)

    # Convert to PDF
    with open(output_file, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(
            full_html,                # the HTML to convert
            dest=pdf_file,            # file handle to recieve result
            encoding='utf-8'
        )

    if pisa_status.err:
        print(f"Error creating PDF: {pisa_status.err}")
    else:
        print("PDF creation complete.")

if __name__ == "__main__":
    create_pdf()
