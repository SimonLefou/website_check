import requests
import pandas as pd

# email_add = os.environ.get('EMAIL_ADD')
# password = os.environ.get('EMAIL_PASS')


excel_file = pd.read_excel("liste_site.xlsx")


for websites in excel_file.iterrows():

    try:
        response = requests.get(websites)
        # df.at[index, "status_code"] = "Site ok {}".format(response.status_code)
    except ValueError:
        excel_file.at[websites, "status_code"] = "Site non attaignable"

print(excel_file)

"""
def send_email():
    s = smtplib.SMTP('ADRESSE DU SERVEUR SMTP', 587)
    s.starttls()
    s.login(email_add, password)
    subject = "Website Down !!"
    body = f"Attention ce {website} est down"
    message = f"Subject: {subject}\n\n {body}"
    s.sendmail(email_add, email_add, message)
    s.quit()



statuscode = requests.get(df, timeout=5)
if statuscode.status_code != 200:
    send_email()
"""
