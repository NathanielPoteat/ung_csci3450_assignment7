import os
import qrcode
import pandas

# Loop through each line in the .csv file and convert the URL into a QR Code
def generate_qr_codes(csv_file, output_directory_bad, output_directory_good):
    count = 0
    data = pandas.read_csv(csv_file, names = ['url','label'])

    for i, row in data.iterrows():
        url = data['url']
        label = data['label']
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(url[i])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        count += 1
        if label[i] == 'good':
            if not os.path.exists(f"{output_directory_good}"):
                os.makedirs(f"{output_directory_good}")
            filename = (f"qrgood{count}.png")
            image_path = os.path.join((f"{output_directory_good}"), filename)
            img.save(image_path)
            print(f"QR, {filename} saved to: {image_path}")  

        elif label[i] == 'bad':
            if not os.path.exists(f"{output_directory_bad}"):
               os.makedirs(f"{output_directory_bad}")
            filename = (f"qrbad{count}.png")
            image_path = os.path.join((f"{output_directory_bad}"), filename)
            img.save(image_path)
            print(f"QR, {filename} saved to: {image_path}")
            
csv_file = r"C:\Users\Matthew\Desktop\PersonalProjects\ung_csci3450_assignment7\phishing_site_urls.csv"
output_directory_bad = r"C:\Users\Matthew\Desktop\PersonalProjects\ung_csci3450_assignment7\phishing_qr_codes\bad"
output_directory_good = r"C:\Users\Matthew\Desktop\PersonalProjects\ung_csci3450_assignment7\phishing_qr_codes\good"
generate_qr_codes(csv_file, output_directory_bad, output_directory_good)