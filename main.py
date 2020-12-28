import csv
from datetime import time
from faker import Faker


class Search:

    def __init__(self, a):
        fake = Faker("En")
        Faker.seed(time.time())
        self.name = fake.word()
        self.grade = fake.int()
        self.scale = fake.int()
        self.online_consultation = fake.isinstance()
        self.main_departments = fake.word()
        self.number_of_patients = fake.int()
        self.service = fake.word(ext_word_list=['Best', 'Good', 'General', 'Ok'])
        self.quality = fake.word(ext_word_list=['Best', 'Good', 'General', 'Ok'])
        self.effectiveness = fake.word(ext_word_list=['Best', 'Good', 'General', 'Ok'])

    def GenerateData(self):
        with open('hospital.csv', 'w', newline='', encoding="utf-8") as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0, 100):
                hospital = hospital()
                spamwriter.writerow([hospital.name, hospital.grade, hospital.scale,
                                     hospital.online_consultation, hospital.main_departments,
                                     hospital.number_of_patient, hospital.service,
                                     hospital.quality, hospital.effectiveness])


    def readData(self):
        sFilename = 'e:hospital.csv'
        # 打开文件
        eFile = open(sFilename)
        # 读取csv文件
        eReader=csv.reader(eFile)
        # 遍历csv对象获取数据，每一条数据都是一个list，每一列是list中的一个元素
        # line_num是行号，这里只读取前100行
        for row in eReader:
            if eReader.line_num <= 100:
                print('行 '+str(eReader.line_num) + ': '+str(row))
            else:
                break
        # 关闭文件
        eFile.close()


    def search(self):
        # 获取搜索值
        scale_floor = int(self.csv.lineEdit.text())  # 规模下限
        scale_cell = int(self.csv.lineEdit_2.text())  # 规模上限
        discount_floor = int(self.csv.lineEdit_3.text())
        discount_cell = int(self.csv.lineEdit_4.text())
        print(scale_floor, scale_cell)

        # 记录有几个match
        newDis = {}
        for k, v in dict.items():
            # match = 0
            newDis[k] = 0
            if (v[0] > scale_floor) & (v[0] < scale_cell):
                # match += 1
                newDis[k] += 1
            if (v[1] > discount_floor) & (v[1] < discount_cell):
                # match += 1
                newDis[k] += 1
        print(newDis)

