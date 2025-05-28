from generate_email import generate_email
from send_email import send_email
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, COMMON_DATA

def get_speaker_info():
    name = input("Enter speaker's name (e.g., Ms. Uddin): ").strip()
    email = input("Enter speaker's email: ").strip()
    print("Enter custom paragraphs for the speaker's invitation (type 'DONE' on a new line to finish):")
    paragraphs = []
    while True:
        para = input()
        if para.strip().upper() == 'DONE':
            break
        if para.strip():
            paragraphs.append(para.strip())
    return {
        "name": name,
        "email": email,
        "custom_paragraphs": paragraphs
    }

def main():
    print("Welcome to the KIIT E-Summit Email Generator & Sender!")
    while True:
        speaker = get_speaker_info()
        data = {**COMMON_DATA, **speaker}
        
        plain_text, html_text = generate_email(data)

        print("\n--- Generated Plain Text Email ---\n")
        print(plain_text)
        
        send = input("\nDo you want to send this email now? (yes/no): ").strip().lower()
        if send in ['yes', 'y']:
            try:
                send_email(
                    smtp_server=SMTP_SERVER,
                    port=SMTP_PORT,
                    sender_email=SENDER_EMAIL,
                    sender_password=SENDER_PASSWORD,
                    receiver_email=speaker["email"],
                    subject=f"Invitation to speak at {COMMON_DATA['event_name']}",
                    plain_text=plain_text,
                    html_text=html_text
                )
            except Exception as e:
                print(f"Error sending email: {e}")
        else:
            print("Email not sent.")
        
        cont = input("\nDo you want to send another email? (yes/no): ").strip().lower
        
if __name__ == "__main__":
    main()