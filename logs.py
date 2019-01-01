import datetime
import xlsxwriter

def createTrafficLog(log):
    
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

  # Start from the first cell. Rows and columns are zero indexed.
  row = 1
  col = 0

  # Iterate over the data and write it out row by row.
  for res in log:
      worksheet.write(row, col, res)
      col += 1
  row +=1
  # Write a total using a formula.
  # worksheet.write(row, 0, 'Total')
  # worksheet.write(row, 1, '=SUM(B1:B4)')

  workbook.close()