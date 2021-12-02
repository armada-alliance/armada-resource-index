# import packages
import markdownify

# read html file to convert
html_file = open("bookmarks.html", "r")
html_string = html_file.read()
html_file.close()

# convert html to markdown
converted_html_md = markdownify.markdownify(html_string, heading_style='atx')

# write markdown to file
markdown_file = open('essential-armada.md', 'w')
markdown_file.write(converted_html_md+' ')
markdown_file.close()