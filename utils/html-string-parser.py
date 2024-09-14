from bs4 import BeautifulSoup


def format_html(html):
    # Parse the HTML string
    soup = BeautifulSoup(html, 'html.parser')

    # Find the first tag in the HTML string (assuming there's only one top-level tag)
    tag = soup.find()

    # Start building the output string with the opening tag and attributes on the first line
    attrs = []
    for attr, value in tag.attrs.items():
        if attr != 'class':
            attrs.append(f'{attr}="{value}"')

    formatted_html = f"<{tag.name} {' '.join(attrs)}\n"

    # Handle 'class' attribute by placing it on its own line, then breaking out each value on a new line
    if 'class' in tag.attrs:
        values = '\n    '.join(tag['class'])
        formatted_html += f"  class=\"\n    {values}\">\n"
    else:
        formatted_html += ">\n"

    # Add the contents between the tags, if any
    if tag.search_string:
        formatted_html += f"  {tag.search_string}\n"

    # Add the closing tag
    formatted_html += f"</{tag.name}>\n"

    # Print the result
    print(formatted_html)

while True:
    html_string = input("_> ")
    format_html(html_string)
