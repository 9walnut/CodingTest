# ANTlabs test
import difflib


def highlight_differences(str1, str2):
    diff = difflib.ndiff(str1, str2)

    result_str1 = ""
    result_str2 = ""

    for i, s in enumerate(diff):
        if s.startswith("  "):
            result_str1 += s[2]
            result_str2 += s[2]
        elif s.startswith("- "):
            result_str1 += f'<span style="background-color: pink;">{
                s[2]}</span>'
        elif s.startswith("+ "):
            result_str2 += f'<span style="background-color: lightblue;">{
                s[2]}</span>'

    return result_str1, result_str2


def generate_html(str1, str2):
    highlighted_str1, highlighted_str2 = highlight_differences(str1, str2)

    html = f"""
    <html>
    <body>
        <p>First String:</p>
        <p>{highlighted_str1}</p>
        <p>Second String:</p>
        <p>{highlighted_str2}</p>
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
