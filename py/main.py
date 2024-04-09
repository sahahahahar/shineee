
from fastapi import FastAPI
import smtplib
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

SERVER_EMAIL = "cleanyourhome48@gmail.com"
SERVER_PWD = "mzgttririnqwjghi" # This is an App Password

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api/contact')
def sendMail(email: str, username: str):
    # If you really care, add the exception and edge-case handling somewhere here
    # Wrong email, scuffed username etc.
    mail = smtplib.SMTP("smtp.gmail.com")
    mail.starttls()
    mail.login(user=SERVER_EMAIL, password=SERVER_PWD)
    mail.sendmail(from_addr=SERVER_EMAIL, to_addrs=email, msg=f"Hello, {username}. Here is your sell: kamajoba!")
    mail.close()

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)