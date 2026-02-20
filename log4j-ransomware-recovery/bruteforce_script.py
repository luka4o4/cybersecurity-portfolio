from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        print(f"[+] Password found: {password.decode().strip()}")
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")

    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    break
            else:
                print("[!] Password not found in list")

if __name__ == "__main__":
    main()
