from bs4 import BeautifulSoup
import io

infile = io.open('DjangoIRClogs_20150731.html', 'r', encoding='utf8')
outfile = io.open('DjangoIRClogs_20150731_method2.csv', 'a+', encoding='utf8')
soup = BeautifulSoup(infile)

row = []
allLines = soup.findAll("li","le")
for line in allLines:
    username = line['rel']
    linenum = line.contents[0]['name']
    message = line.contents[3].lstrip()
    row.append(linenum)
    row.append(username)
    row.append(message)
    outfile.write(','.join(row))
    outfile.write(u'\n')
    row = []
infile.close()
outfile.close()
