import smtplib

def prompt(title):
    return input(title).strip()
from_addr = prompt("From: ")
to_addr = prompt("To: ")
print("Enter message")

lines = [f"From : {from_addr}", f"To: {' , '.join(to_addr)}", ""]

while True:
    try:
        line = input()
    except EOFError:
        break 
    else:
        lines.append(line)
msg = "\r\n".join(lines)
print("Message length is , len(msg)")

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(from_addr,to_addr,msg)
server.quit()