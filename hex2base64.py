from binascii import a2b_hex, b2a_base64

def main():
    print(b2a_base64(a2b_hex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')).decode("utf-8"))

if __name__ == '__main__':
    main()