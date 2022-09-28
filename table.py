from tabulate import tabulate
import requests


table_data = [['Name', 'Age', 'Job'],
				['Tashi', '22', 'Programmer'],
				['Dawa', '27', 'Programmer']]

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))


data = requests.get("http://202.144.136.82:3000/api/graphical/drprowone").text
print(data)
print(type(data))

s_data = data.split(",")

gid1 = s_data[0]
s_gid1 = gid1.split(":")
val = s_gid1[1]
fgid1 = val[1:-1]
print(fgid1)

gid1_ph = s_data[2]
s_gid1ph = gid1_ph.split(":")
val2 = s_gid1ph[1]
fgid1_ph = val2[1:-1]
print(fgid1_ph)


gid1_ec = s_data[3]
s_gid1ec = gid1_ec.split(":")
val3 = s_gid1ec[1]
fgid1_ec = val3[1:-1]
print(fgid1_ec)

gid1_n = s_data[4]
s_gid1n = gid1_n.split(":")
val4 = s_gid1n[1]
fgid1_n = val4[1:-1]
print(fgid1_n)

gid1_p = s_data[5]
s_gid1p = gid1_p.split(":")
val5 = s_gid1p[1]
fgid1_p = val5[1:-1]
print(fgid1_p)

gid1_k = s_data[6]
s_gid1k = gid1_k.split(":")
val6 = s_gid1k[1]
fgid1_k = val6[1:-1]
print(fgid1_k)

gid1_hum = s_data[7]
s_gid1hum = gid1_hum.split(":")
val7 = s_gid1hum[1]
fgid1_hum = val7[1:-1]
print(fgid1_hum)

gid1_tem = s_data[8]
s_gid1tem = gid1_tem.split(":")
val8 = s_gid1tem[1]
fgid1_tem = val8[1:-1]
print(fgid1_tem)

gid1_lev= s_data[9]
s_gid1lev = gid1_lev.split(":")
val9 = s_gid1lev[1]
fgid1_lev = val9[1:-1]
print(fgid1_lev)

gid1_date = s_data[10]
s_gid1date = gid1_date.split(":")
val10 = s_gid1date[1]
fgid1_date = val10[1:-1]
print(fgid1_date)

gid1_time = s_data[11]
Fgid1_time = gid1_time[15:-2]
print(Fgid1_time)

#Row Two
gid2 = s_data[12]
s_gid2 = gid2.split(":")
val = s_gid2[1]
fgid2 = val[1:-1]
print(fgid2)

gid2_ph = s_data[14]
s_gid2ph = gid2_ph.split(":")
val2 = s_gid2ph[1]
fgid2_ph = val2[1:-1]
print(fgid2_ph)


gid2_ec = s_data[15]
s_gid2ec = gid2_ec.split(":")
val3 = s_gid2ec[1]
fgid2_ec = val3[1:-1]
print(fgid2_ec)

gid2_n = s_data[16]
s_gid2n = gid2_n.split(":")
val4 = s_gid2n[1]
fgid2_n = val4[1:-1]
print(fgid2_n)

gid2_p = s_data[17]
s_gid2p = gid2_p.split(":")
val5 = s_gid2p[1]
fgid2_p = val5[1:-1]
print(fgid2_p)

gid2_k = s_data[18]
s_gid2k = gid2_k.split(":")
val6 = s_gid2k[1]
fgid2_k = val6[1:-1]
print(fgid2_k)

gid2_hum = s_data[19]
s_gid2hum = gid2_hum.split(":")
val7 = s_gid2hum[1]
fgid2_hum = val7[1:-1]
print(fgid2_hum)

gid2_tem = s_data[20]
s_gid2tem = gid2_tem.split(":")
val8 = s_gid2tem[1]
fgid2_tem = val8[1:-1]
print(fgid2_tem)

gid2_lev= s_data[21]
s_gid2lev = gid2_lev.split(":")
val9 = s_gid2lev[1]
fgid2_lev = val9[1:-1]
print(fgid2_lev)

gid2_date = s_data[22]
s_gid2date = gid2_date.split(":")
val10 = s_gid1date[1]
fgid2_date = val10[1:-1]
print(fgid2_date)

gid2_time = s_data[23]
Fgid2_time = gid2_time[15:-2]
print(Fgid2_time)

#ROW THREE



df =  [['Green House', 'pH', 'EC', 'Nitrogen', 'Phosphorus', 'Potassium', 'Soil Moisture', 'Soil Temperature', 'Tank Level', 'Date', 'Time'],
		[fgid1, fgid1_ph, fgid1_ec, fgid1_n, fgid1_p, fgid1_k, fgid1_hum, fgid1_tem, fgid1_lev, fgid1_date, Fgid1_time],
		[fgid2, fgid2_ph, fgid2_ec, fgid2_n, fgid2_p, fgid2_k, fgid2_hum, fgid2_tem, fgid2_lev, fgid2_date, Fgid2_time]

				]

print(tabulate(df, headers="firstrow", tablefmt="fancy_grid"))
