import os

def update_scripts():
    scripts = ['compile_book.py', 'create_epub.py', 'create_pdf.py']
    
    for script in scripts:
        filepath = os.path.join(r'd:\Philosophy', script)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('Subjective_Manifestation_Book', 'Manifestationism_Book')
            new_content = new_content.replace('显现的架构：主体显现论', '显现的架构：显现论')
            new_content = new_content.replace('A Theory of Subjective Manifestation', 'Manifestationism')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {script}")
        except Exception as e:
            print(f"Error updating {script}: {e}")

def rename_files():
    old_md = r'd:\Philosophy\Subjective_Manifestation_Book.md'
    new_md = r'd:\Philosophy\Manifestationism_Book.md'
    
    if os.path.exists(old_md):
        try:
            os.rename(old_md, new_md)
            print(f"Renamed {old_md} to {new_md}")
        except Exception as e:
            print(f"Error renaming {old_md}: {e}")

    # Remove old binary files if they exist
    for ext in ['.epub', '.pdf']:
        old_file = old_md.replace('.md', ext)
        if os.path.exists(old_file):
            try:
                os.remove(old_file)
                print(f"Removed old file {old_file}")
            except Exception as e:
                print(f"Error removing {old_file}: {e}")

if __name__ == "__main__":
    update_scripts()
    rename_files()
