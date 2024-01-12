import json
from datetime import datetime, timedelta

sekarang = datetime.now()
waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
code = sekarang - \
    timedelta(seconds= 10)
code.strftime("%Y%m%d%H%M%S")
menu = {}
file_path = 'menu.json'

try :
    with open(file_path, 'r') as file:
        menu = json.load(file)

except Exception as e:
    print(f"terjadi Kesalahan: {e}")

# Show the food and drink
print()
print('|==========================================|')
print('|              Detail Pesanan              |')
print('|==========================================|')
print(f"|{'  Kode':7} | {'     Menu':15}| {'     Harga':8}     |")
print('|==========================================|')
for item, info in menu.items():
    print(f"|   {info[ 'kode']:4} | {   item:14} | Rp{info['harga']:8}     |")
print('|==========================================|')

# Function for take the order
def take_order(menu):
    name = input("Nama Pelanggan: ")
    orders = []
    total_harga = 0
    print("Masukan Kode dan porsi (Contoh: 3, 2)")
    print('(Pilih nomor 0 untuk keluar)')
    while True:
        try:
            order = input("Pesanan: ")
            if order.lower() == '0':
                break
            kode_pesanan, porsi = order.split(",")
            if kode_pesanan in [info['kode'] for info in menu.values()]:
                item_terpilih = next(item for item, info in menu.items() if info['kode'] == kode_pesanan)
                harga_terpilih = menu[item_terpilih]['harga']
                print(f"Anda memesan {item_terpilih} dengan harga Rp{harga_terpilih}.")
                if item in menu:
                    harga = harga_terpilih * int(porsi)
                    total_harga += harga
                    orders.append({'item': item_terpilih, 'porsi': int(porsi), 'harga': harga})
                else:
                    print(f"item {item} tidak tersedia di menu.")
            else:
                print("kode menu tidak valid.")
        except:
            print('Format input salah')
    print('Total harga:', total_harga)
    uang = int(input("Masukan uang pelanggan: "))
    return name, orders, total_harga, uang 

# Save the order in file
def save_order(nama_pelanggan, orders, total_harga, uang):
    order_details = {
        'Nama Pelanggan': nama_pelanggan,
        'orders': orders,
        'Total_harga': total_harga,
        'Uang': uang,
        'kembali': uang - total_harga
    }
    with open('pesanan.txt', 'a') as file:
        file.write(json.dumps(order_details) + "\n")
            

def read_orders():
    with open('pesanan.txt', 'r') as file:
        lines = file.readlines()
        baris_terakhir = lines[-1]
        order_details = json.loads(baris_terakhir)
        print()
        print('|==========================================|')
        print(f"|Kode Transaksi: {code.strftime("%Y%m%d%H%M%S")}            |")
        print('|==========================================|')
        print(f"|Nama Pelanggan: {order_details['Nama Pelanggan']:15}           |")
        print('|==========================================|')
        print(f"|Tanggal: {waktu}              |")
        print('|==========================================|')
        print('|              Detail Pesanan              |')
        print('|==========================================|')
        print(f"|{'         Menu':20} | {'porsi'  :2} | {'    Harga  ':6}|")
        print('|==========================================|')
        for order in order_details['orders']:
            print(f"|   {order[ 'item'  ]:17} | {order['porsi']:5} | Rp{order['harga']:6}   |")
            print('|==========================================|')
        print(f"|   Total Harga {'':15}  Rp{order_details['Total_harga']:8}|")
        print('|------------------------------------------|')
        print(f"|   Uang Bayar {'':15}   Rp{order_details['Uang']:8}|")
        print('|------------------------------------------|')
        print(f"|   Kembalian {'':15}    Rp{order_details['kembali']:8}|")
        print('|==========================================|')
        print('|               Terima Kasih               |')
        print('|==========================================|')

        

nama_pelanggan, orders, total_harga, uang = take_order(menu)
save_order(nama_pelanggan, orders, total_harga, uang,)
read_orders()
print()