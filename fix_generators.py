import re
import xml.etree.ElementTree as ET

def clean_svg_string(svg_str):
    # 1. Fix unescaped & (not followed by amp;, lt;, gt;, quot;, apos;, or #...)
    # Replace & that is not part of a valid XML entity with &amp;
    cleaned = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_str)
    
    # 2. Fix HTML tags inside SVG <text>: <strong>text</strong> -> <tspan font-weight="bold">text</tspan>
    cleaned = re.sub(r'<strong>(.*?)</strong>', r'<tspan font-weight="bold">\1</tspan>', cleaned)
    cleaned = re.sub(r'<em>(.*?)</em>', r'<tspan font-style="italic">\1</tspan>', cleaned)
    cleaned = re.sub(r'<b>(.*?)</b>', r'<tspan font-weight="bold">\1</tspan>', cleaned)
    cleaned = re.sub(r'<i>(.*?)</i>', r'<tspan font-style="italic">\1</tspan>', cleaned)
    
    # 3. Fix unescaped arrows in text e.g. "->" inside <text>
    # (Only inside text tags)
    def fix_text_tags(match):
        inner = match.group(1)
        inner = inner.replace('->', '&rarr;')
        return f'<text{match.group(0)[5:match.group(0).find(">")]}>{inner}</text>'
    
    # 4. Enhance SVG colors for dark mode:
    # Replace dark slate #1e293b when used in strokes, arrows, fork bars, nodes with theme-aware classes or vibrant colors
    # Replace #1e293b stroke or fill
    cleaned = cleaned.replace('fill="#1e293b"', 'class="uml-dark-shape" fill="#60a5fa"')
    cleaned = cleaned.replace('stroke="#1e293b"', 'class="uml-dark-stroke" stroke="#60a5fa"')
    
    # Replace activation grey #cbd5e1 with class
    cleaned = cleaned.replace('fill="#cbd5e1" stroke="#475569"', 'class="uml-activation" fill="rgba(56,189,248,0.25)" stroke="#38bdf8"')
    cleaned = cleaned.replace('fill="#cbd5e1"', 'class="uml-cube-top" fill="#24344d"')
    cleaned = cleaned.replace('fill="#94a3b8"', 'class="uml-cube-side" fill="#182335"')
    
    # Replace light pastel callouts in SVGs
    cleaned = cleaned.replace('fill="#fee2e2"', 'fill="rgba(239, 68, 68, 0.2)"')
    cleaned = cleaned.replace('fill="#fef3c7"', 'fill="rgba(245, 158, 11, 0.2)"')
    cleaned = cleaned.replace('fill="#e0e7ff"', 'fill="rgba(99, 102, 241, 0.2)"')
    cleaned = cleaned.replace('fill="#d1fae5"', 'fill="rgba(16, 185, 129, 0.2)"')
    cleaned = cleaned.replace('fill="#ede9fe"', 'fill="rgba(139, 92, 246, 0.2)"')
    cleaned = cleaned.replace('fill="#f1f5f9"', 'fill="rgba(148, 163, 184, 0.15)"')
    cleaned = cleaned.replace('fill="#f5f3ff"', 'fill="rgba(139, 92, 246, 0.15)"')

    return cleaned

for part_idx in range(1, 7):
    filename = f"generate_sections_part{part_idx}.py"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all SVGs in the python file
    def replace_svg(m):
        raw_svg = m.group(1)
        cleaned = clean_svg_string(raw_svg)
        return cleaned

    new_content = re.sub(r'(<svg[\s\S]*?</svg>)', replace_svg, content)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated {filename}")

