import speedtest

def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        print("Testing internet speed...")

        # Perform the download speed test
        download_speed = st.download() / 1000000  

        # Perform the upload speed test
        upload_speed = st.upload() / 1000000 

        # Print the results
        print("Download Speed: {:.2f} Mbps".format(download_speed))
        print("Upload Speed: {:.2f} Mbps".format(upload_speed))
        print(st.__dict__)

    except Exception as e:
        print("An error occurred during the speed test:", str(e))

test_internet_speed()

