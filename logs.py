import datetime
import os
import xlsxwriter

def createTrafficLog(logs):
  dateTime = str(datetime.datetime.now()).replace(' ', '-').replace('-', '').replace(':','')[:14]

  workbook = xlsxwriter.Workbook('logs.xlsx')
  worksheet = workbook.add_worksheet(dateTime)
  bold = workbook.add_format({'bold': 1})

  #creating a structure for organizing intercepted packages
  worksheet.write('A1', 'ID', bold)
  worksheet.write('B1', 'Source', bold)
  worksheet.write('C1', 'Destination', bold)
  worksheet.write('D1', 'Protocol', bold)
  worksheet.write('E1', 'Type of Service', bold)
  worksheet.write('F1', 'Flags', bold)
  worksheet.write('G1', 'Fragment offset', bold)
  worksheet.write('H1', 'TTL', bold)
  worksheet.write('I1', 'Version', bold)
  worksheet.write('J1', 'Checksum', bold)
  worksheet.write('K1', 'Header Length (bytes)', bold)
  worksheet.write('L1', 'Length', bold)
  worksheet.write('M1', 'Raw Data', bold)
  worksheet.write('N1', 'Payload', bold)
  worksheet.write('O1', 'Date/Time Intercepted', bold)

  # start from the first cell of the second row
  row = 1
  col = 0

  # iterate over the data and write it out column by column and starting a new line for each log

  for log in logs:
      for res in log:
        if col == 15:
          row += 1
          col = 0
          worksheet.write(row, col, res)
          col += 1
        else:  
            worksheet.write(row, col, res)
            col += 1

  workbook.close()
