import os
import pandas as pd

#出力先ディレクトリの設定
output_dir = './processed'

# 観測値データの読み込み
df=pd.read_csv('./raw/ame_master_20240401_utf-8.csv', encoding='utf-8')

#全観測地テーブルの読み込みと結合 →　地上気象観測装置（略字「官」）
df_filt = df[(df['種類'] == '官')| (df['種類'] == '四')]

# 「札幌市中央区北2条西　札幌管区気象台」と「札幌市中央区北2条西」のように，同じidで２個所の所在地データがあるものを1箇所に重複除外する（上にある行のデータを採用）
df_filt_drop_dup = df_filt.drop_duplicates(subset='観測所番号', keep='first')

# 緯度・経度を60進数から10進数に変換したカラムを作成
df_add_lat_long = df_filt_drop_dup.copy()
df_add_lat_long['latitude'] = df_add_lat_long['緯度(度)'] + (df_add_lat_long['緯度(分)']/60)
df_add_lat_long['longitude'] = df_add_lat_long['経度(度)'] + (df_add_lat_long['経度(分)']/60)


# 出力
df_add_lat_long.to_csv(os.path.join(output_dir, 'observatories_kansyo_drop_duplicates.csv'), index=False)

