import sys

with open("08/Constitution.txt", "r") as file:
    lines = [line.rstrip('\n') for line in file]

def find_sections_with_term(search_term, lines):
    printed_sections = set()
    line_count = len(lines)
    i = 0

    while i < line_count:
        line = lines[i]
        if search_term.lower() in line.lower():
            start = i
            while start > 0 and lines[start].strip() != '':
                start -= 1

            section_start = start if lines[start].strip() == '' else start - 1
            section_start = max(section_start, 0)

            end = i
            while end < line_count and lines[end].strip() != '':
                end += 1

            section_end = end + 1 if end + 1 < line_count else end

            section_key = (section_start, section_end)
            if section_key not in printed_sections:
                print(f"\n[Match at line {i + 1}]")
                for j in range(section_start, section_end):
                    print(f"{j + 1:>4}: {lines[j]}")
                printed_sections.add(section_key)

            i = section_end
        else:
            i += 1

while True:
    search_term = input("\nEnter a search term (or leave blank to quit): ").strip()
    if not search_term:
        print("Exiting program.")
        sys.exit()

    find_sections_with_term(search_term, lines)