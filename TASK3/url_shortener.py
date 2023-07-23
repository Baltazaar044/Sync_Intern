import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
type_bitly = pyshorteners.Shortener(api_key='15b577576ba03cded91d667ba803782dc57fb19e')
short_url = type_bitly.bitly.short(long_url)
 
print("The Shortened URL is: " + short_url)