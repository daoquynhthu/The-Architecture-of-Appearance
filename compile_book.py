import os

base_dir = r"d:\Philosophy\Book"
output_file = r"d:\Philosophy\Manifestationism_Book.md"

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

def compile_book():
    print(f"Compiling book to {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write Title (optional, can be taken from TOC or hardcoded)
        outfile.write("# 显现的架构：显现论\n")
        outfile.write("# The Architecture of Appearance: Manifestationism\n\n")
        
        for filename in files:
            filepath = os.path.join(base_dir, filename)
            if os.path.exists(filepath):
                print(f"Processing {filename}...")
                try:
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write("\n\n---\n\n") # Add separator
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
            else:
                print(f"Warning: File not found: {filename}")

    print("Compilation complete.")

if __name__ == "__main__":
    compile_book()
