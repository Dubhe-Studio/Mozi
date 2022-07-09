import requests
import json


def get_music(name: str):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=03d8db13899e9a794900679a060f5708,1634014441532; _ntes_nuid=03d8db13899e9a794900679a060f5708; NMTID=00OXlzMXBvZMONDTUPAphyu6n2Q3lkAAAF8ctmxVA; WEVNSM=1.0.0; WNMCID=axppxw.1634014447487.01.0; WM_TID=CiZeIL6vI6BEEAUEBBdq5S4Ys5f2uVHj; hb_MA-B701-2FC93ACD9328_source=mail.st.xatu.edu.cn; timing_user_id=time_HLdBgtgIVZ; JSESSIONID-WYYY=RbUSVrZ6vb0sTqNbrJSerMfkY9JtcHuVeta%5CtlowxMEGKgYTWHhBFIS%2F0ef8bXTf325z96NzMWbkeI0m7bX8hA8EGfbdkmGeO3FOaG9JlHI57%2FP9n0ujikvRoIQrY%2BPmjZA3RWFy8I8ngd8dheJ%5Cwrj22uQjFgKyVPz8FBnU9IFhzwaz%3A1637759947642; WM_NI=wPL7kiWyuTnQttj4mpalNKkG5tqXVI00c4WJHE%2FujdyK47dYMRJe8iElMlvsgCWKiF%2FLhO%2BxMfS3bVOwNfyOdIqs5LToqrCqp4ifv5BZ5HqOE%2FbBJ6%2Fwr%2B%2Fk%2Fp1KdECASFM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed6ec5fede9fdd2c67bb08a8ab3c15f928f9b84f180f2978997ae7da78baa8aca2af0fea7c3b92ab59084d8ea6395a7bbb5ed5bb8aca6d5f07ca3b482acea4df7acbfb9d543f4f0add5d6428c9be196e970bb95fcd8e7538f8e8686bb6387b4838df579a59d99acec4eed94a8b0aa748fba9dd4e15e8da98287fc45a897bf94b84898b1bf93c27bb4eca787f53f8286fba9f44587f1aea3c93eeda9beccae61edb0fface74f819f9da7d037e2a3',
        'Host': 'music.163.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
    }
    x = json.loads(
        requests.get('http://music.163.com/api/search/pc?s=' + name + '&offset=0&limit=1&type=1', headers=headers).text)
    name = x['result']['songs'][0]['name']
    src = "http://music.163.com/song/media/outer/url?id=" + str(x['result']['songs'][0]['id']) + ".mp3"
    img = x['result']['songs'][0]['album']['picUrl']
    card_message = [
        {
            "type": "card",
            "theme": "secondary",
            "size": "lg",
            "modules": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain-text",
                        "content": name + "的搜索结果如下："
                    }
                },
                {
                    "type": "audio",
                    "title": name,
                    "src": src,
                    "cover": img
                }
            ]
        }
    ]
    return card_message
