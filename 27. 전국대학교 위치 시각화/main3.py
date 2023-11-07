import pandas as pd
import folium

filePath = r'27. 전국대학교 위치 시각화\학교주소좌표.xlsx'
df_from_excel = pd.read_excel(filePath,engine="openpyxl",header=None)

df_from_excel.columns = ['학교명','주소','x','y']

name_list = df_from_excel['학교명'].to_list()
addr_list = df_from_excel['주소'].to_list()
pos_x_list = df_from_excel['x'].to_list()
pos_y_list = df_from_excel['y'].to_list()

map = folium.Map(location=[37,127], zoom_start=7)

for i in range(len(name_list)):
    if pos_x_list[i] != 0:
        marker=folium.Marker([pos_y_list[i],pos_x_list[i]],popup=name_list[i],icon=folium.Icon(color='blue'))
        marker.add_to(map)
map.save(r'27. 전국대학교 위치 시각화/uni_map.html')
