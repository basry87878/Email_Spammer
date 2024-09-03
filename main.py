import smtplib, ssl
import spammer
import timeit

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email_here@gmail.com"
    password = os.getenv('EMAIL_PASSWORD')  # Use environment variable
    receiver_email = "receiver_email_here@gmail.com"
    
    context = ssl.create_default_context() #defines the server
    server = None  # Initialize server here
    
    try: 
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() #allow us to transfer our messages
        server.starttls(context=context)
        server.ehlo() #be ready to send our messsage
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode('utf-8')) # Encoding to UTF-8
        
    except Exception as e:
        print(e) #print the error
    
    finally:
        if server is not None:
            server.quit()

txt = spammer.text

# Use timeit.timeit() to measure the execution time
spam_execution_time = timeit.timeit(lambda: sendEmail(txt), number=10)
print(f'Email Sent in {spam_execution_time} seconds on average.')