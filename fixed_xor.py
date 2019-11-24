def main():
    hex_1 = int('1c0111001f010100061a024b53535009181c',16)
    hex_2 = int('686974207468652062756c6c277320657965',16)
    print((hex(hex_1^hex_2))[2:])

if __name__ == '__main__':
    main()
