import os
import markdown
from pathlib import Path
from ebooklib import epub

base_dir = Path(r"d:\Philosophy\Book")
output_file = r"d:\Philosophy\Manifestationism_Book.epub"

# Define the order explicitly to ensure correct sequence
files = [
    "00_Preface.md",
    "00_Meta_Discourse.md",
    "01_The_Primal_Fact.md",
    "02_Weak_Assertion.md",
    "03_Existence.md",
    "04_Manifestation_Structure.md",
    "05_Subject_Emergence.md",
    "05_1_Dimensions_Time_Space_Body.md",
    "Part1_Summary_The_View_From_The_Foundation.md",
    "06_Manifestation_Dynamics.md",
    "07_Stability_Genesis.md",
    "08_Sustainability_And_Normative_Dynamics.md",
    "09_The_Manifestation_Status_Of_Logic.md",
    "09_1_Typology_Modes_of_Presence.md",
    "Part2_Summary_Navigation_In_The_Storm.md",
    "10_The_Construction_Of_World.md",
    "11_Others_And_Intersubjectivity.md",
    "12_Meaning_And_Language.md",
    "13_Science_And_Objectivity.md",
    "13_1_Praxis_Ethics_Politics_Aesthetics.md",
    "Part3_Summary_Surviving_In_Normativity.md",
    "14_Common_Misconceptions.md",
    "14_1_Critical_Dialogues.md",
    "15_Limit_Experiences.md",
    "16_Conclusion_Living_Within_Manifestation.md"
]

def create_epub():
    print(f"Creating EPUB: {output_file}")

    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('subjective-manifestation-123456')
    book.set_title('显现的架构：显现论')
    book.set_language('zh')
    book.add_author('Unknown')

    # Create chapters
    chapters = []
    toc_links = []

    for filename in files:
        filepath = base_dir / filename
        if not filepath.exists():
            print(f"Warning: File not found: {filename}")
            continue

        print(f"Processing {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Extract title from the first line (assuming # Title format)
        lines = md_content.split('\n')
        title = filename # Default to filename if no title found
        for line in lines:
            if line.strip().startswith('# '):
                title = line.strip().replace('# ', '').strip()
                break
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        # Create chapter
        chapter_file_name = filename.replace('.md', '.xhtml')
        c = epub.EpubHtml(title=title, file_name=chapter_file_name, lang='zh')
        c.content = html_content
        
        book.add_item(c)
        chapters.append(c)
        toc_links.append(c)

    # Define Table of Contents
    book.toc = toc_links

    # Add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define CSS style
    style = 'body { font-family: "SimSun", serif; } h1 { text-align: center; }'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # Define Spine
    book.spine = ['nav'] + chapters

    # Write EPUB file
    epub.write_epub(output_file, book)
    print("EPUB creation complete.")

if __name__ == "__main__":
    create_epub()
