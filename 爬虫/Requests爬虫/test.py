import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
con = requests.get(
    "https://vd2.bdstatic.com/mda-mf44j92444hmamij/540p/h264_cae/1622862806669113909/mda-mf44j92444hmamij.mp4?v_from_s=hkapp-haokan-tucheng&auth_key=1629457935-0-0-60450300e35ed4a027358df0e759a50c&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest=",
    headers=headers).content
with open("123.mp4", 'wb') as fp:
    fp.write(con)

    fp.close()

