# bcl2scada
software scada BCL

cara memasang software scada untuk weigher

1. install python 2.7 versi 32 bit https://www.python.org/ftp/python/2.7/python-2.7.msi
2. download semua file di repository ini ke c://Python27/python-ku
3. restart komputer, buka cmd dan jalankan perintah "pip install python-snap7"
4. copy file snap7.dll dari repo ke c://Python27/
5. copy svc.vbs ke startup folder
6. masuk startup folder dengan cara win+r shell:startup enter
7. buat shortcut hmi.py dan release/bcl2.exe ke desktop
8. restart komputer

jika board arduino rusak
maka beli board arduino mega yang baru

1. pastikan software arduino IDE sudah terinstall di komputer
2. tambahkan library https://github.com/mitchyboy9/Adafruit_MCP4725 , umtuk bisa mengkases banyak DAC dalam satu waktu seperti http://mitchtronic.blogspot.com/2017/03/addressing-multiple-mcp4724s-in-same.html
3. source code program arduino berada di folder BCL2_DAC_ALL
4. masukkan program tersebut ke arduino

coba jalankan kembali program scada, pastikan arduino masuk ke port COM5
jika tidak rubah setting port ke COM5 caranya : https://anagramus.wordpress.com/2010/05/06/cara-merubah-com/
