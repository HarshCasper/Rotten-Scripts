import html2markdown
html_text = input("Paste HTML text here (eg. <p>this is stuff <strong>stuff</strong></p>): ")
print (html2markdown.convert(html_text))
