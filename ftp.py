from ftplib import FTP

def ftp_client():
    ftp = FTP("ftp.dlptest.com")  # public test FTP server
    ftp.login(user="dlpuser", passwd="rNrKYTX9g7z3RgJRmxWuGHbeu")

    print("Connected to FTP server.")
    
    # List files
    print("Directory Listing:")
    ftp.retrlines("LIST")

    # Upload a test file
    with open("test_upload.txt", "w") as f:
        f.write("Hello from CN Lab - FTP Upload!")

    with open("test_upload.txt", "rb") as f:
        ftp.storbinary("STOR test_upload.txt", f)
    print("✅ File uploaded.")

    # Download a file
    with open("downloaded.txt", "wb") as f:
        ftp.retrbinary("RETR test_upload.txt", f.write)
    print("✅ File downloaded.")

    ftp.quit()

ftp_client()
