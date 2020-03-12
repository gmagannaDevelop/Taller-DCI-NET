
from alt import *
from login import login

if __name__ == "__main__":
  # Email variables. Modify this!
  EMAIL_FROM = 'gml.automat@gmail.com'
  EMAIL_TO = EMAIL_FROM
  EMAIL_SUBJECT = 'Hola robot!'
  EMAIL_CONTENT = 'Esto es una prueba'

  #service = service_account_login()
  service = login()
  # Call the Gmail API
  message = CreateMessage(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_CONTENT)
  sent = SendMessage(service,'me', message)

