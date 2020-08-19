# encoding: utf-8
# @FileName  :id_check.py
# @Time      :2020/8/7 17:50
# @Author    :XZX
import xlrd

# str_num_list = '''
# 342625197906100018
# 340102196507164017
# 340102197511181519
# 340102193712054010
# 340102194707054016
# 340104197408170515
# 340111196912234548
# 340102197701194011
# 340102197601044032
# 340102197011013017
# 340104197707081512
# '''

str_num_list = '''
450324198709151349
340102196912054049
342623198101146521
340102194108154023
341221194812016607
340111192506110528
340102197203094018
340123198201095283
34011119751110056X
340102197809014027
340102198612284028
'''


def check(str_id_num):
    # id_num = 340102199605184015
    # str_id_num = str(id_num)
    # str_id_num = '53010219200508011X'
    if len(str_id_num) < 18:
        return False
    mu = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ch = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    n_sum = 0
    for i in range(0, 17):
        try:
            n = int(str_id_num[i])
        except:
            return False
        n_sum = n_sum + n * mu[i]
    # print(n_sum % 11)
    mod_res = n_sum % 11
    if ch[mod_res] == str_id_num[17]:
        return True
    else:
        return False
    pass


if __name__ == '__main__':
    # print(check(None))
    # book = xlrd.open_workbook(r'C:\Users\XZX\Documents\采石苑B区集资户统计汇总表.xls')
    book = xlrd.open_workbook(r'C:\Users\XZX\Documents\(新)采石苑B区集资户统计汇总表.xls')
    book = book.sheet_by_index(0)
    for i in range(3, book.nrows):
        row = book.row_values(i)
        # print(row)
        if row[1] == '':
            print(i)
            break
        line = row[0]
        name1 = row[1]
        id_num1 = row[2]
        name2 = row[4]
        id_num2 = row[5]
        if not check(id_num1):
            print(str(line) + ' ' + name1 + '   ' + id_num1)
        if not check(id_num2):
            print(str(line) + ' ' + name2 + '   ' + id_num2)

    # num_list = str_num_list.strip().split('\n')
    # for num in num_list:
    #     print(num + '   ' + str(check(num)))
    pass
