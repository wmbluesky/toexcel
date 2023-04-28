import pandas as pd
import openpyxl
 # 从文件A和B中读取数据
df_a = pd.read_excel('/Users/kylewan/Desktop/data1.xlsx')
df_b = pd.read_excel('/Users/kylewan/Desktop/test.xlsx')
 # 根据人名匹配数据信息，将匹配结果输出到文件B中
for i in range(len(df_b)):
    name = df_b.loc[i, '用户']
    row = df_a.loc[df_a['用户'] == name]
    if len(row) > 0:
        data = row.iloc[0, 1:]
        for j, value in enumerate(data):
            df_b.loc[i, '数据{}'.format(j+1)] = value
 # 将结果输出到文件B中
#with pd.ExcelWriter('/Users/kylewan/Desktop/test.xlsx', engine='openpyxl', mode='a') as writer:
#    writer.book = openpyxl.load_workbook('/Users/kylewan/Desktop/test.xlsx')
#    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    df_b.to_excel('/Users/kylewan/Desktop/output.xlsx', index=False)
#    writer.save()
