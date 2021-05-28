import pandas as pd
from datetime import datetime, date

def ws2xlsx(input_file, output_file):
    # Create a Pandas dataframe from some datetime data.
    df = pd.read_csv(input_file)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # Also set the default datetime and date formats.
    writer = pd.ExcelWriter(output_file,
                            engine='xlsxwriter',
                            datetime_format='mmm d yyyy hh:mm:ss',
                            date_format='mmmm dd yyyy')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Get the xlsxwriter workbook and worksheet objects in order to set the column
    # widths, to make the dates clearer.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    
    worksheet.set_column('A:H', 20)
    worksheet.set_column('D:D', 60)
    worksheet.set_column('F:F', 50)
    worksheet.set_column('G:G', 80)    
    
    # Create a format to use in the merged range.
    merge_format = workbook.add_format({
        'text_wrap': True,
        'align': 'center',
        'valign': 'top',
        })
    
    merge_row_format = workbook.add_format({
        'text_wrap': True,
        'align': 'center',
        'valign': 'top',
        'bg_color': '#CCCCCC'
        })
    
    row_format = workbook.add_format({'bg_color': '#CCCCCC'})
    
    # work through the groups to merge
    pos = 0
    toggle = True
    while pos < len(df):
        count = (df['project::Project Title']==df['project::Project Title'][pos]).sum()
        print(pos, count, toggle)
        if count > 1:
            for col in (0,1,2,3,7):
                if toggle:
                    worksheet.merge_range(pos+1, col, pos+count, col, df[df.keys()[col]][pos], merge_row_format)
                else :
                    worksheet.merge_range(pos+1, col, pos+count, col, df[df.keys()[col]][pos], merge_format)
        if toggle:
            for i in range(count):
                worksheet.set_row(pos+1+i, cell_format=row_format)
        toggle = not toggle
        pos += count

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
