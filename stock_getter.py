from urllib import request

intel_url = 'https://query1.finance.yahoo.com/v7/finance/download/INTC?period1=1574202738&period2=1605825138&interval=1d&events=history&includeAdjustedClose=true'

#funtion downloadstockdata takes the variable csv url

def download_stock_data(csv_url):

#call function urlopen which takes the url of a csv, which will store the connection to the webpage in response
    response = request.urlopen(csv_url)

# response.read will read the data from the url we have
# text from this stored in variable called csv and store as a string
    csv = response.read()
    csv_str = str(csv)

# call a function split on the variable csv_str which takes the long string and breaks it up whenever it comes across "\\n"
    lines = csv_str.split("\\n")

# using r is good practice when working with filepass, Here we've just saved the intel csv document as out dest_url
    dest_url = r'intel.csv'

#use file object to read and write from this
#the for loop will iterate through each line, stored in the variable lines, and will write each one to our file object
# which is the opened dest_url file. Then we use to close function to save memory

    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

#call the function
download_stock_data(intel_url)
