import re


csv_data = '''id,name
1,"Johnson, Smith, and Jones Co."
2,"Sam ""Mad Dog"" Smith"
3,Barney & Company
4,Johnson's Automotive'''.split('\n')
col_regexp = re.compile(r'([A-Za-z_]+),([A-Za-z_"]+)')
cols = col_regexp.match(csv_data[0]).groups()
row_regexp = re.compile(r'([0-9]+),([A-Za-z0-9 .,&\'"]+)')
json_data = {}
for csv_row in csv_data[1:]:
    row_match = row_regexp.match(csv_row).groups()
    json_data[cols[0]] = json_data.get(cols[0], []) + [int(row_match[0])]
    json_data[cols[1]] = json_data.get(cols[1], []) + [row_match[1]]
print(json_data)
