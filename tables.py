from comparison import Comparison


class Tables:

    def __init__(self):
        self.tables = {}
        self.compare = Comparison()

    def load(self, tablename, filename):
        try:
            with open(f'files/{filename}', 'r', encoding='utf-8') as fh:
                contents = fh.read()

            self.tables[tablename] = {
                'header': contents.split('\n')[0].split(','),
                'rows': [contents.split('\n')[i].split(',') for i in range(1, len(contents.split('\n')))],
            }
            return f'\033[92m Table {tablename} loaded \033[0m'
        except Exception as e:
            raise e

    def discard(self, tablename):
        try:
            self.tables.pop(tablename)
            return f'\033[92m Table {tablename} discarded \033[0m'
        except Exception as e:
            raise e

    def save(self, tablename, filename):
        try:
            f = open(f"files/{filename}", "w")
            text = ''
            header = self.tables[tablename]['header']

            for i in range(0, len(header)):
                text = text + header[i]
                if i < (len(header) - 1):
                    text = text + ','
                else:
                    text = text + '\n'

            rows = self.tables[tablename]['rows']
            for i in range(0, len(rows)):
                for j in range(0, len(rows[i])):
                    text = text + rows[i][j]
                    if j < (len(rows[i]) - 1):
                        text = text + ','
                    elif i != (len(rows) - 1):
                        text = text + '\n'
            f.write(text)
            f.close()
            return f'\033[92m Table {tablename} saved \033[0m'
        except Exception as e:
            raise e

    def insert(self, tablename, values):
        self.tables[tablename]['rows'].append(values)
        return f'\033[92m Values {values} inserted in table {tablename} \033[0m'

    def create_empty_table(self, tablename, header):
        self.tables[tablename] = {'header': header, 'rows': []}
        return f'\033[92m Table {tablename} created \033[0m'

    def create_from_select(self, tablename, select):
        self.tables[tablename] = select
        self.show(tablename=tablename)
        return f'\033[92m Table {tablename} created \033[0m'

    def create_from_table(self, tablename, table):
        self.tables[tablename] = self.tables[table]
        self.show(tablename=tablename)
        return f'\033[92m Table {tablename} created \033[0m'

    def find_highest(self, header, rows, col):
        highest = len(header[col])
        for i in range(0, len(rows)):
            if len(rows[i][col]) > highest:
                highest = len(rows[i][col])

        return highest

    @staticmethod
    def get_cols(cols, header):
        cols_num = []
        for i in range(0, len(header)):
            if header[i] in cols:
                cols_num.append(i)

        return cols_num

    @staticmethod
    def print_text(highest, word, isHeader=False):
        rest = highest - len(word)
        text = word
        if rest > 0:
            text = text + (' ' * rest)
        if not isHeader:
            print(text + ' | ', end='')
        else:
            print(f'\033[47m{text} | \033[0m', end='')

    @staticmethod
    def print_header(highest, header):
        for i in range(0, len(header)):
            Tables.print_text(highest[i], header[i], isHeader=True)
            if i == len(header) - 1:
                print()

    @staticmethod
    def get_header(header, cols_num):
        show_header = []
        for i in range(0, len(header)):
            if len(cols_num) == 0:
                show_header.append(header[i])
            else:
                if i in cols_num:
                    show_header.append(header[i])
        return show_header

    def print_rows(self, highest, rows, lim):
        for i in range(0, len(rows)):
            if lim < 0:
                for j in range(0, len(rows[i])):
                    self.print_text(highest[j], rows[i][j])
                    if j == (len(rows[i]) - 1):
                        print()
            else:
                if (i + 1) <= lim:
                    for j in range(0, len(rows[i])):
                        self.print_text(highest[j], rows[i][j])
                        if j == (len(rows[i]) - 1):
                            print()

    def get_rows(self, rows, cond_cols, cols_num):
        table_rows = []
        for i in range(0, len(rows)):
            row = []
            can_append = True
            if len(cond_cols) != 0:
                for cond in cond_cols:
                    if can_append:
                        if not self.compare.switch(cond[1], rows[i][cond[0]], cond[-1]):
                            can_append = False

            if can_append:
                for j in range(0, len(rows[i])):
                    if len(cols_num) != 0:
                        if j in cols_num:
                            row.append(rows[i][j])
                            if j == max(cols_num):
                                table_rows.append(row)
                    else:
                        row.append(rows[i][j])
                        if j == (len(rows[i]) - 1):
                            table_rows.append(row)
        return table_rows

    def build_table(self, tablename, cols=[], condition=[]):
        table = {}
        full_header = self.tables[tablename]['header']
        highest = [self.find_highest(full_header, self.tables[tablename]['rows'], i) for i in
                   range(0, len(full_header))]

        if len(cols) != 0:
            cols_num = self.get_cols(cols, full_header)

        header = self.get_header(full_header,
                                 cols_num if len(cols) != 0 else [])
        table['header'] = header

        if len(condition) != 0:
            cond_cols = self.get_cond_cols(full_header, condition)

        rows = self.get_rows(self.tables[tablename]['rows'], cond_cols if len(condition) != 0 else [],
                             cols_num if len(cols) != 0 else [])
        table['rows'] = rows
        return table

    def show(self, table='', lim='', tablename=''):
        if tablename != '' and table == '':
            _table = self.tables[tablename]
        elif table != '':
            _table = table

        print(f'Table: {tablename}')
        full_header = _table['header']

        highest = [self.find_highest(full_header, _table['rows'], i)
                   for i in range(0, len(full_header))]

        self.print_header(highest, full_header)

        rows = _table['rows']
        self.print_rows(highest, rows, -1 if lim == '' else lim)
        print('-' * (sum(highest) + len(full_header * 3)))

    def get_cond_cols(self, header, condition):
        cond_cols = []
        for i in range(0, len(header)):
            for cond in condition:
                if cond[0] == header[i]:
                    cond_cols.append([i, cond[1], cond[-1]])
        return cond_cols

    def select_table(self, cols, tablename, lim, condition=[]):

        if cols[0] == '*':
            table = self.build_table(tablename, condition=condition)
            self.show(table=table, tablename=tablename, lim=lim)
        else:
            table = self.build_table(tablename, condition=condition, cols=cols)
            self.show(table=table, tablename=tablename, lim=lim)
        return table

    @staticmethod
    def find_attrib_col(attrib, header):
        for i in range(0, len(header)):
            if header[i] == attrib:
                return i

    @staticmethod
    def find_all_attrib(rows, col):
        all_attrib = {}
        for i in range(0, len(rows)):
            if f'{rows[i][col]}' not in all_attrib:
                all_attrib[f'{rows[i][col]}'] = [i]
            else:
                all_attrib[f'{rows[i][col]}'].append(i)

        return all_attrib

    def join_tables(self, table1, table2, attribute):
        table = {}
        t1_header = self.tables[table1]['header']
        t2_header = self.tables[table2]['header']
        table['header'] = t1_header + t2_header

        t1_attribute_pos = self.find_attrib_col(attribute, t1_header)
        t2_attribute_pos = self.find_attrib_col(attribute, t2_header)
        t1_rows = self.tables[table1]['rows']
        t2_rows = self.tables[table2]['rows']

        all_t2_attrib = self.find_all_attrib(t2_rows, t2_attribute_pos)

        rows = []
        for i in range(0, len(t1_rows)):
            if t1_rows[i][t1_attribute_pos] in all_t2_attrib:
                pos = all_t2_attrib[t1_rows[i][t1_attribute_pos]]
                for p in pos:
                    rows.append(t1_rows[i] + t2_rows[p])

        table['rows'] = rows
        return table
