import pandas as pd

# Just update this variable
excel_file_path = 'file.xlsx'
format_output_name = 'output-sms1'

df = pd.read_excel(excel_file_path)

max_rows_per_chunk = 30
num_chunks = len(df) // max_rows_per_chunk + 1

for i in range(num_chunks):
    start_idx = i * max_rows_per_chunk
    end_idx = (i + 1) * max_rows_per_chunk
    chunk = df.iloc[start_idx:end_idx]
    
    json_data = chunk.to_json(orient='records')
    
    with open(f'{format_output_name}-{i + 1}.json', 'w') as json_file:
        json_file.write(json_data)

print(f'Excel file has been successfully split into {num_chunks} JSON files.')