from speedtest import Speedtest
from datetime import datetime
import csv
import time


def returnInfoBefore():
    beforeInfo = []
    with open('analise.csv', newline='') as csvfile:
        readCsv = csv.reader(csvfile, delimiter='', quotechar='|')
        for line in readCsv:
            elementLine = line[0].split(",")
            if 'Data' not in elementLine[0]:
                beforeInfo.append(elementLine)
    return beforeInfo


def returnInfoNow():
    nowInfo = datetime.now()
    actualDate = nowInfo.strftime('%d/%m/%y')
    actualHour = nowInfo.strftime('%H:%M')
    velocity = Speedtest().download(threads=None)*(10**-6)
    return actualDate, actualHour, velocity


def writeInfo(actualDate, actualHour, velocity):
    while True:
        try:
            beforeInfo = returnInfoBefore()
            with open('analise.csv', 'wt', newline='') as csvfile:
                fieldnames = ['Data', 'Hora', 'Velocidade']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for line in beforeInfo:
                    writer.writerow({'Data': line[0], 'Hora': line[1],
                                     'Velocidade': f'{line[2]} MB'})

                writer.writerow({'Data': actualDate, 'Hora': actualHour,
                                'Velocidade': f'{round(velocity, 2)} MB'})
                print(f'[DATA] {actualDate}[HORA] {actualHour}[VELOCIDADE] {round(velocity, 2)} MB')
                break
        except PermissionError:
            print('Não tenho permissão pra fazer isso...')
            time.sleep(5)


def main():
    while True:
        actualDate, actualHour, velocity = returnInfoNow()
        writeInfo(actualDate, actualHour, velocity)
        time.sleep(1800)  # Dormir 30 Minutos


main()
