# Watchlist Saham Saat ini
watchlist = ("BBCA", "BBRI", "BBNI", "BMRI")

# list untuk simpan orders
order = []

print("=== SISTEM ORDERBOOK EMITEN ===")
print(" Simulasi Cara Kerja Orderbook ")

# Main Program
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Order Baru")
    print("2. Lihat Orderbook")
    print("3. Keluar")
    
    # Input pilihan user
    pilih = int(input("Pilih menu: "))
    
    # Conditional statements untuk memproses pilihan
    if pilih == 1:
        # CREATE - Menambah order baru
        print("\n--- TAMBAH ORDER BARU ---")
        
        # Input Saham
        saham = str(input("Masukkan kode Saham (BBCA, BBRI, BBNI, BMRI): ")).upper()
        
        # Validasi Saham menggunakan statement conditional
        if saham not in watchlist:
            print("!!!OY CUMA BISA PILIH 4. YANG LAIN COMING SOON!!!")
            continue
            
        jenis_order = input("Jenis order (🟢 BID/ASK 🔴): ").upper()
        if jenis_order not in ["BID", "ASK"]:
            print("!!!Jenis order cuma ada BID dan ASK!!!")
            continue
            
        try:
            harga = float(input("Harga: "))
            Jumlah = int(input("Jumlah (lot): "))
        except:
            print("!!INPUT HARUS ANGKA!!!")
            continue
        
        # Membuat order dan masuk ke list
        order_baru = [saham, jenis_order, harga, Jumlah]
        order.append(order_baru)
        
        print("Order berhasil ditambahkan✅")
        
    elif pilih == 2:
        # READ - Menampilkan orderbook
        print("\n--- ORDERBOOK ---")
        
        if len(order) == 0:
            print("Belum ada order.")
        else:
            print("Daftar Order:")
            no = 1
            for order in order:
                if order[1] == "BID":
                    print(f"{no}. {order[0]} | 🟢 {order[1]} | {order[2]:,.0f} | {order[3]} lot")
                else:
                    print(f"{no}. {order[0]} | 🔴 {order[1]} | {order[2]:,.0f} | {order[3]} lot")
                no += 1
                
# End Program
    elif pilih == 3:
        print("Thank you udah nyoba!👋🏻")
        break
        
    else:
        print("!!!CUMA BISA PILIH 1-3!!!")