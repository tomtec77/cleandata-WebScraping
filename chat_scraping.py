import re
import io

row = []

# Open the file with the chat logs
infile = io.open('DjangoIRClogs_20150731.html', 'r', encoding='utf8')
outfile = io.open('DjangoIRClogs_20150731.csv', 'a+', encoding='utf8')

"""
We want to extract from the file: user name, chat ID, chat text. Each chat
line is enclosed within the <li> tags, which themselves are inside the
<ul id="ll"> tag.

Line number and user name appear in several places. We'll pull the user
name from the value of the rel attribute of the li class="le" and the line
number in the name attribute of the <a href=. The chat message is enclosed
by </span> and </li>.
"""

for line in infile:
    pattern = re.compile(ur'<li class=\"le\" rel=\"(.+?)\"><a href=\"(.+?) name=\"(.+?)\">(.+?)<\/span>\s(.+?)\s<\/li>', re.UNICODE)
    if pattern.search(line):
        username = pattern.search(line).group(1)
        linenum = pattern.search(line).group(3)
        message = pattern.search(line).group(5)
        row.append(linenum)
        row.append(username)
        row.append('"'+message+'"')
        outfile.write(','.join(row))
        outfile.write(u'\n')
        row = []
infile.close()
