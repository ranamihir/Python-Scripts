file_url = 'csv.file.url'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'file_name.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()
    
download_stock_data(file_url)