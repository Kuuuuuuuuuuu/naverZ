import pandas as pd
import json

# 엑셀 파일 경로를 지정합니다.
file_path = 'C:/Users/USER/kuu/real_data.xlsx'


# 엑셀 파일을 읽어옵니다.
df = pd.read_excel(file_path)

# JSON 컬럼에서 데이터를 추출하여 새로운 DataFrame으로 변환합니다.
# 여기서는 'json_column'이라는 이름의 컬럼에 JSON 데이터가 있다고 가정합니다.
json_column = 'zpt_content'  # JSON 데이터가 포함된 엑셀 파일의 컬럼 이름

all_data = []

for index, row in df.iterrows():
    json_data = json.loads(row[json_column])
    chat_data = json_data['chat']
    all_data.extend(chat_data)

chat_df = pd.json_normalize(all_data)


print(chat_df)

# 변환된 DataFrame을 새로운 엑셀 파일로 저장합니다.
output_file_path = 'output02.xlsx'
chat_df.to_excel(output_file_path, index=False)

print(f"JSON 데이터를 변환하여 {output_file_path} 파일로 저장 완료.")