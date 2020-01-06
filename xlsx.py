import xlsxwriter

class Xlsx(object):

    def __init__(self, data, number):
        self.data = data
        self.number = number

    def write_to_xlsx(self):
        headers = ['NUMBER', 'TITLE', 'ADDRESS', 'AREA', 'PRICE [kr]', 'SIZE [m²]', 'LINK']

        workbook = xlsxwriter.Workbook('apartments_excel.xlsx')
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format()
        cell_format.set_font_size(14)
        cell_format.set_font_name('Times New Roman')

        col = 0
        row = 0
        for item in headers:
            worksheet.write_string(row, col, item)
            col += 1
        col = 0
        row =+ 1

        for line in self.data:
            for item in line:
                if col == 4 or col == 0 or col == 5:
                    try:
                        integer = int(item)
                        worksheet.write_number(row, col, integer, cell_format)
                    except:
                        worksheet.write(row, col, item, cell_format)
                else:
                    worksheet.write(row, col, item, cell_format)
                col += 1
                if col == 7:
                    col = 0
                    row += 1

        self.conditional_formatting(worksheet, workbook)
        workbook.close()

    def conditional_formatting(self, worksheet, workbook):
        format1 = workbook.add_format({'bg_color': '#00FF00', 'bold': 1})
        format2 = workbook.add_format({'bg_color': '#FFFF00'})
        format3 = workbook.add_format({'bg_color': '#FF0000'})
        format_all = workbook.add_format({'font_name': 'Arial', 'font_size': 14})




        worksheet.conditional_format('E2:E200', {'type': 'cell',
                                               'criteria': 'between',
                                               'minimum':  9500,
                                               'maximum':  12000,
                                               'format':   format1
                                               })
        worksheet.conditional_format('E2:E200', {'type': 'cell',
                                               'criteria': 'between',
                                               'minimum':  12001,
                                               'maximum':  20000,
                                               'bar_color': '#4dffa6',
                                               'format':   format3
                                               })
        worksheet.conditional_format('E2:E200', {'type': 'cell',
                                               'criteria': 'between',
                                               'minimum':  1,
                                               'maximum':  9499,
                                               'format':   format2
                                               })

        worksheet.conditional_format('F2:F200', {'type': 'cell',
                                               'criteria': 'between',
                                               'minimum':  22,
                                               'maximum':  45,
                                               'format':   format1
                                               })
        worksheet.conditional_format('F2:F200', {'type': 'cell',
                                               'criteria': 'between',
                                               'minimum':  46,
                                               'maximum':  100,
                                               'bar_color': '#4dffa6',
                                               'format':   format3
                                               })
        worksheet.conditional_format('F2:F200', {'type': 'cell',
                                               'criteria': 'between',
                                               'minimum':  10,
                                               'maximum':  21,
                                               'format':   format3
                                               })


        # worksheet.conditional_format('E1:E200', {'type': 'data_bar',
        #                                        'criteria': '<=',
        #                                        'value': '10000',
        #                                        'bar_color': '#FF1A1A',
        #                                        'data_bar_2010': True})
        print("Conditional formatting done!")
