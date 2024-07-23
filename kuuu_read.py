import pandas as pd

# CSV 파일 경로
file_path = "C:/Users/USER/Downloads/tickets_data_all.csv" # 본인 파일 위치 작성

# CSV 파일을 DataFrame으로 읽어오기
df = pd.read_csv(file_path, dtype={'media_path': object, 'to_ocr_text_existance': object})

#print(df.head())

target_id = '83ff3e28#33d6b134#08a5518e' # 요기에 ID 입력하기!

# 값 유무 확인 T/F
print(target_id in df['review_policy_id'].values)

# 특정 ID 값을 가진 데이터의 general_text 컬럼 조회
result = df.loc[df['review_policy_id'] == target_id]
#result = df.dropna(axis=1)
# DataFrame 출력
#print(result) # df all column
print(result[['language', 'review_policy_id', 'general_text']])

# CSV 파일을 DataFrame으로 읽어오기
#df = pd.read_csv(file_path, dtype={'media_path': object, 'to_ocr_text_existance': object})

# 첫 몇 줄 출력하여 데이터 구조 확인
#print(df.head())


'''
# 'ticket_id' 열 확인
print(df['ticket_id'].head())

target_id = '9b4bf59bedec448a85d77f6e5dbcd41c'

# 'ticket_id' 열에 target_id 값이 있는지 확인
print(target_id in df['ticket_id'].values)

# 특정 ID 값을 가진 데이터 조회
result = df.loc[df['ticket_id'] == target_id]

# DataFrame 출력
print(result)
'''

# 결과를 CSV 파일로 저장
result_file_path = "C:/Users/USER/Downloads/filtered_data_Revealing of PII.csv"
result.to_csv(result_file_path, index=True, encoding='utf-8')
