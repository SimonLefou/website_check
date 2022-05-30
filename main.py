import requests
import pandas as pd


excel_file = pd.read_excel("liste_site.xlsx", header=None)
col1 = [website for website in excel_file[0] if type(website) == str]   # Recupération des Websites en colonne
nbre_url = len(col1)
LISTE_EXTENSION = ["com", "fr"]


def convert(url):
    if url.startswith('http://www.'):
        return 'https://www.' + url[len('http://www.'):]
    elif url.startswith('www.'):
        return 'https://' + url[len('www.'):]
    elif url.startswith('http://'):
        return 'https://' + url[len('http://'):]
    if not url.startswith('https://'):
        return 'https://' + url
    return url


def clean_url(url):
    url_copy = url
    url = url.split("/")
    url = url[-1].split(".")
    if url[-1] not in LISTE_EXTENSION:
        url = url_copy.split("/")
        url.pop(-1)
        url = ("/".join(url))
    else:
        url = url_copy.split("/")
        url = ("/".join(url))
    return url


def is_down(url):
    try:
        reponse = requests.get(url)
        print(f"Status Code : {reponse.status_code}")
    except:
        print(f"{url} = non disponible")
        return True
    return False


file = open("Liste_Sites_Down.txt", "w+")


for i in range(len(col1)):
    check_url = col1[i]
    check_url = convert(check_url)
    check_url = clean_url(check_url)
    print(check_url)

    if is_down(check_url):
        file.write(check_url)
        file.write("\n")
    print("Programme en cours")
    print(f"{int(i / nbre_url * 100)}%")

print("Fin d'execution")
file.close()


"""
    POSIBILITE ULTERIEUR : ENVOI DE MAIL

# email_add = os.environ.get('EMAIL_ADD')
# password = os.environ.get('EMAIL_PASS')
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