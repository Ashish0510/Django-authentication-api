from django.core.mail import EmailMessage

class Utils:
    @staticmethod
    def send_mail(data):
        email=EmailMessage(
            subject=data["subject"],
            body=data["body"],
            from_email='*******@gmail.com',
            to=[data['to_mail']]
            )
        email.send()




