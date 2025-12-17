import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        # Chinese replacements
        new_content = new_content.replace('主体显现论', '显现论')
        new_content = new_content.replace('结构显现论', '显现论')
        
        # English replacements
        new_content = new_content.replace('Subjective Manifestationism', 'Manifestationism')
        new_content = new_content.replace('Structural Manifestationism', 'Manifestationism')
        new_content = new_content.replace('Subjective Manifestation Theory', 'Manifestationism')
        new_content = new_content.replace('Theory of Subjective Manifestation', 'Manifestationism')
        new_content = new_content.replace('A Theory of Subjective Manifestation', 'Manifestationism')
        
        # Specific fix for title if needed (e.g. if it results in "Manifestationism: Manifestationism")
        # But for now, direct replacement.
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def process_dir(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                replace_in_file(os.path.join(dirpath, filename))

process_dir('d:\\Philosophy')
