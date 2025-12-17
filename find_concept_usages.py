import os
import re

def find_usages(root_dir):
    pattern = re.compile(r'主体显现|结构显现|Subjective Manifestation|Structural Manifestation')
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                matches = pattern.finditer(content)
                for match in matches:
                    start = max(0, match.start() - 20)
                    end = min(len(content), match.end() + 20)
                    context = content[start:end].replace('\n', ' ')
                    print(f"{filepath}: {match.group()} -> ...{context}...")
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

find_usages('d:\\Philosophy')
