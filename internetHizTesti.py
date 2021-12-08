import speedtest

speed = speedtest.Speedtest()


def Test():
    while True:
        print("**************************************")
        secim = int(input("""
        1) İndirme hızı
        2) Yükleme Hızı
        3) Çıkış
        seçim yapınız :
        """))
        print("****************************************")
        if secim == 1:
            print(f"İndirme Hızı: {'{:.2f}'.format(speed.download() / 1024 / 1024)}MB/S")
        elif secim == 2:
            print(f"Yükleme Hızı: {'{:.2f}'.format(speed.upload() / 1024 / 1024)}MB/S")
        elif secim == 3:
            print('çıkış yapıldı....')
            break
        else:
            print("hatalı sayı tekrar dene...")


Test()
