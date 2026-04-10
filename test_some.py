from rplidar import RPLidar, RPLidarException
import time

PORT_NAME = 'COM4'

def main():
    lidar = RPLidar(PORT_NAME, baudrate=115200, timeout=3)
    
    print("Sistem baslatiliyor...")
    lidar.start_motor()
    time.sleep(2) # Motorun tam hıza ulaşması için bekleme süresi
    
    try:
        lidar._serial_port.reset_input_buffer()
    except:
        pass
        
    print("Tarama baslatiliyor (Hatalı paketler filtrelenecek)...\n")
    
    while True:
        try:
            for i, scan in enumerate(lidar.iter_scans(max_buf_meas=500)):
                print(f"--- Tur Tamamlandi | Toplam Nokta: {len(scan)} ---")
                
                for point in scan:
                    kalite, aci, mesafe = point
                    if mesafe > 0:
                        print(f"Aci: {aci:05.1f}° | Mesafe: {mesafe:06.1f} mm")

        except RPLidarException as e:
            # "Descriptor length mismatch" hatalarında çökmek yerine tamponu temizleyip devam eder
            print(f"\n[ATLANDI] Anlik veri bozulmasi: {e}. Senkronizasyon yenileniyor...")
            try:
                lidar._serial_port.reset_input_buffer()
            except:
                pass
            time.sleep(0.1) 
            continue 
            
        except KeyboardInterrupt:
            print("\nIslem kullanici tarafindan durduruldu.")
            break
        except Exception as e:
            print("\nBeklenmeyen sistem hatasi:", e)
            break

    print("Motor durduruluyor ve baglanti kesiliyor...")
    try:
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
    except:
        pass

if __name__ == '__main__':
    main()