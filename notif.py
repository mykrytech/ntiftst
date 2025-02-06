from plyer import notification
import time
import sys
import threading

# Fungsi untuk mengirim notifikasi
def send_notification(title, message, timeout=1):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout  # Notifikasi akan hilang setelah timeout detik
    )

# Fungsi untuk menjalankan notifikasi berulang
def start_notifications(interval, title, message, stop_event):
    while not stop_event.is_set():
        send_notification(title, message)
        time.sleep(interval)

# Fungsi utama
def main():
    print("Pilih platform:")
    print("1. Mobile (Android/Termux)")
    print("2. Desktop (Windows/Linux/Mac)")
    platform_choice = input("Masukkan pilihan (1/2): ")

    if platform_choice not in ["1", "2"]:
        print("Pilihan tidak valid. Keluar.")
        sys.exit()

    print("\nPilih mode:")
    print("1. Mulai notifikasi")
    print("2. Berhenti notifikasi")
    mode_choice = input("Masukkan pilihan (1/2): ")

    if mode_choice == "1":
        title = input("Masukkan judul notifikasi: ")
        message = input("Masukkan pesan notifikasi: ")
        interval = int(input("Masukkan interval notifikasi (detik): "))

        # Event untuk menghentikan notifikasi
        stop_event = threading.Event()

        # Jalankan notifikasi dalam thread terpisah
        notification_thread = threading.Thread(
            target=start_notifications,
            args=(interval, title, message, stop_event)
        )
        notification_thread.start()

        print("Notifikasi telah dimulai. Tekan Enter untuk berhenti.")
        input()  # Tunggu sampai pengguna menekan Enter
        stop_event.set()  # Set event untuk menghentikan notifikasi
        notification_thread.join()  # Tunggu thread notifikasi selesai
        print("Notifikasi dihentikan.")

    elif mode_choice == "2":
        print("Tidak ada notifikasi yang berjalan.")
    else:
        print("Pilihan tidak valid. Keluar.")

if __name__ == "__main__":
    main()