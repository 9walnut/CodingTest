import difflib


def highlight_differences2(str1, str2):
    result_str1 = ""
    result_str2 = ""

    # Determine the minimum length to avoid index out of range issues
    min_len = min(len(str1), len(str2))

    # Iterate over both strings and compare characters
    for i in range(min_len):
        if str1[i] == str2[i]:
            result_str1 += str1[i]
            result_str2 += str2[i]
        else:
            result_str1 += f'<span style="background-color: pink;">{
                str1[i]}</span>'
            result_str2 += f'<span style="background-color: lightblue;">{
                str2[i]}</span>'

    # Handle the remaining part of the longer string
    if len(str1) > min_len:
        for i in range(min_len, len(str1)):
            result_str1 += f'<span style="background-color: pink;">{
                str1[i]}</span>'
    if len(str2) > min_len:
        for i in range(min_len, len(str2)):
            result_str2 += f'<span style="background-color: lightblue;">{
                str2[i]}</span>'

    return result_str1, result_str2


def highlight_differences_with_index(str1, str2):
    sm = difflib.SequenceMatcher(None, str1, str2)

    result_str1 = ""
    result_str2 = ""

    for opcode, i1, i2, j1, j2 in sm.get_opcodes():
        if opcode == 'equal':
            result_str1 += str1[i1:i2]
            result_str2 += str2[j1:j2]
        elif opcode == 'replace':
            for k in range(i1, i2):
                result_str1 += f'<span style="background-color: pink;">{
                    str1[k]}</span>'
            for k in range(j1, j2):
                result_str2 += f'<span style="background-color: lightblue;">{
                    str2[k]}</span>'
        elif opcode == 'delete':
            for k in range(i1, i2):
                result_str1 += f'<span style="background-color: pink;">{
                    str1[k]}</span>'
        elif opcode == 'insert':
            for k in range(j1, j2):
                result_str2 += f'<span style="background-color: lightblue;">{
                    str2[k]}</span>'

    return result_str1, result_str2


def generate_html(str1, str2):
    highlighted_str1, highlighted_str2 = highlight_differences2(str1, str2)
    highlighted_index_str1, highlighted_index_str2 = highlight_differences_with_index(
        str1, str2)

    html = f"""
    <html>
    <body>
        <p>First String (differences highlighted):</p>
        <p>{highlighted_str1}</p>
        <p>Second String (differences highlighted):</p>
        <p>{highlighted_str2}</p>
        <p>First String (differences with index highlighted):</p>
        <p>{highlighted_index_str1}</p>
        <p>Second String (differences with index highlighted):</p>
        <p>{highlighted_index_str2}</p>
    </body>
    </html>
    """
    return html


# Example usage
str1 = "committer_list_per_month[date + '-' + log[i].author] = 1;"
str2 = "var date_author = date + '-' + log[i].author;"
html_output = generate_html(str1, str2)

# Save to a file
with open("differences.html", "w") as file:
    file.write(html_output)

print("HTML file has been created with the differences highlighted.")
