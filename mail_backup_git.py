import imaplib
import email
import mailbox
import json
import time
import logging
from tqdm import tqdm

# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Chargement des identifiants
def load_config(file="config.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Le fichier de configuration config.json est introuvable.")
        exit(1)
    except json.JSONDecodeError:
        logging.error("Erreur lors du chargement de config.json (format JSON invalide).")
        exit(1)

config = load_config()
EMAIL = config.get("email")
PASSWORD = config.get("password")
IMAP_SERVER = "imap.gmail.com"

# Connexion IMAP
def connect_imap(email, password, server="imap.gmail.com", folder="inbox"):
    try:
        logging.info(f"📩 Connexion à {email}...")
        mail = imaplib.IMAP4_SSL(server)
        mail.login(email, password)
        mail.select(folder)
        return mail
    except imaplib.IMAP4.error:
        logging.error("Échec de connexion à la boîte mail. Vérifiez vos identifiants.")
        exit(1)

# Sauvegarde des emails en fichier mbox
def backup_emails(mail, output_file="backup_gmail.mbox"):
    status, messages = mail.search(None, "ALL")
    mail_ids = messages[0].split()
    total_emails = len(mail_ids)

    logging.info(f"📩 {total_emails} emails trouvés. Démarrage de la sauvegarde...")

    mbox = mailbox.mbox(output_file)  # Correction : suppression du "with"

    start_time = time.time()

    for num in tqdm(mail_ids, desc="Téléchargement des emails", unit="email"):
        try:
            status, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    mbox.add(msg)
        except Exception as e:
            logging.warning(f"Erreur lors du téléchargement de l'email {num}: {e}")

    # Sauvegarde et fermeture du fichier .mbox
    mbox.flush()
    mbox.close()  # Ajout pour éviter une fuite de mémoire

    elapsed_time = time.time() - start_time
    logging.info(f"✅ Sauvegarde terminée ! {total_emails} emails enregistrés en {elapsed_time:.2f} sec.")

# Exécution du script
if __name__ == "__main__":
    mail = connect_imap(EMAIL, PASSWORD)
    backup_emails(mail)
    mail.logout()
