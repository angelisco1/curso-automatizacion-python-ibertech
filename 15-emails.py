import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import mimetypes


def get_connection():
  return {
    "host": os.getenv("HOST_GMAIL"),
    "port": os.getenv("PORT_GMAIL"),
    "user": os.getenv("USER_GMAIL"),
    "password": os.getenv("PASSWORD_GMAIL")
  }


if __name__ == "__main__":
  load_dotenv()
  connection_data = get_connection()


  with smtplib.SMTP(connection_data["host"], connection_data["port"]) as server:
    server.starttls()
    server.login(connection_data["user"], connection_data["password"])

    # mensaje = """
    # Subject: Asunto del mensaje

    # Ole ole los caracoles."""

    # server.sendmail(connection_data["user"], ["avillalba@pronoide.com"], mensaje)

    mensaje = EmailMessage()
    mensaje["From"] = connection_data["user"]
    mensaje["To"] = ["avillalba@pronoide.com"]
    mensaje["Subject"] = "Bienvenido a la empresa"
    mensaje.set_content("Bienvenido a la empresa Ángel.\n\n...\nUn saludo.")

    mensaje_html = """
      <html>
      <body>
        <h2>Bienvenido a la empresa <span style="color:yellowgreen;">Ángel</span></h2>
        <p>Tendrás que seguir las siguientes <strong>instrucciones</strong> para crearte las cuentas necesarias para el trabajo...</p>
        <p>Un saludo.</p>
      </body>
      </html>
    """

    mensaje.add_alternative(mensaje_html, subtype="html")

    imagen_path = "/Users/angelisco1/Pronoide/mis-cursos/curso-ibertech-automatizacion-python/curso-automatizacion-python-ibertech/files/DianaVisualok.png"
    nombre_imagen = os.path.basename(imagen_path)
    file_type, _ = mimetypes.guess_type(imagen_path) # image/png
    _, file_subtype = file_type.split('/', 1) # png

    with open(imagen_path, "rb") as imagen:
      datos_imagen = imagen.read()
      mensaje.add_attachment(datos_imagen, maintype=file_type, subtype=file_subtype, filename=nombre_imagen)

    server.send_message(mensaje)