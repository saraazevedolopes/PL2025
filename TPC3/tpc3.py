import re

def markdown_to_html(markdown_text):
    html_lines = []
    in_ol = False 

    for line in markdown_text.split("\n"):
        match = re.match(r'^(#{1,3})\s*(.+)', line)
        if match:
            level = len(match.group(1)) 
            text = match.group(2).strip()
            html_lines.append(f"<h{level}>{text}</h{level}>")
        elif (match := re.match(r'\d+\.\s+(.+)', line)):  
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            html_lines.append(f"<li>{match.group(1)}</li>")
        else:
            if in_ol:
                html_lines.append("</ol>")
                in_ol = False
            line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" style="width: 150px; height: auto; display: block; margin-top: 5px;">', line)
            line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
            html_lines.append(line)  
    
    if in_ol:
        html_lines.append("</ol>")  
    
    return "\n".join(html_lines)

def convert_markdown_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        markdown_text = infile.read()
    html_output = markdown_to_html(markdown_text)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(html_output)

input_file = "input.md"
output_file = "output.html"
convert_markdown_file(input_file, output_file)
