import speedtest


def check_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()

    print(f"Download Speed: {round(download_speed/1000000, 2)} Mbps")
    print(f"Upload Speed: {round(upload_speed/1000000, 2)} Mbps")


print("Checking Speed...")
check_speed()
