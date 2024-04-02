# This code is courtesy of ChatGPT
import csv
import qrcode

# Loop through each line in the .csv file and convert the URL into a QR Code
def generate_qr_codes(csv_file, output_directory):
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            url = row[0]
            category = row[1]
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            if category == 'good':
                img.save(f"{output_directory}/good/{url.replace('/','_')}.png")
            elif category == 'bad':
                img.save(f"{output_directory}/bad/{url.replace('/','_')}.png")

csv_file = "./phishing_site_urls.csv"
output_directory = "./phishing_qr_codes"
generate_qr_codes(csv_file, output_directory)