import xlrd

# table.nrows
# table.ncols
# a = table.row_values(0)
# print(a)
class ReadExc(object):
    def get_list(self,path,index):
        book = xlrd.open_workbook(path)
        table = book.sheet_by_name(index)
        header  = table.row_values(0)
        data_list = []
        for i in range(1,table.nrows):
            d = table.row_values(i)
            dd = dict(zip(header,d))
            data_list.append(dd)
            # print(data_list)
        return data_list
    def get_data(self,data_list,name):
        for data in data_list:
            if name == data['casename']:
                return data

if __name__ == '__main__':
    a = ReadExc()
    datalist = a.get_list('../data/login163.xlsx','login')
    print(datalist)
    data = a.get_data(datalist,'log_normal')
    print(data)