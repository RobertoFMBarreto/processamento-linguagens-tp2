# logic_eval
from tables import Tables


class LogicEval:
    tables = Tables()
    procedures = {}

    commands = {
        "LOAD": lambda args: LogicEval.tables.load(args[0], args[1]),
        "DISCARD": lambda args: LogicEval.tables.discard(args[0]),
        "SAVE": lambda args: LogicEval.tables.save(args[0], args[1]),
        "SHOW": lambda args: LogicEval.tables.show(tablename= args[0]),
        "SELECT": lambda args: LogicEval._select(args),
        "CREATE": lambda args: LogicEval._create(args),
        "PROCEDURE": lambda args: LogicEval._procedure(args),
        "CALL": lambda args: LogicEval._call(args),
        "INSERT": lambda args: LogicEval._insert(args)
    }

    @staticmethod
    def _insert(args):
        values, tablename = args
        if tablename not in LogicEval.tables.tables:
            raise Exception(f'Table [{tablename}] does not exist')
        if len(values) > len(LogicEval.tables.tables[tablename]['header']):
            raise Exception(f"Too many values[{len(values)}] for table {tablename}, expected {len(LogicEval.tables.tables[tablename]['header'])}")
        if len(values) < len(LogicEval.tables.tables[tablename]['header']):
            raise Exception(f"Few values[{len(values)}] for table {tablename}, expected {len(LogicEval.tables.tables[tablename]['header'])}")
        return LogicEval.tables.insert(tablename, values)

    @staticmethod
    def _procedure(args):
        name, code= args
        LogicEval.procedures[name] = code

    @staticmethod
    def _call(args):
        name = args[0]
        if name not in LogicEval.procedures:
            raise Exception(f'Procedure not defined: {name}')

        result = LogicEval.evaluate(LogicEval.procedures[name])
        return result

    @staticmethod
    def _join(args):
        # args = ['tabela2', ID, 'tabela1']
        table2, attribute, table1 = args
        if table1 not in LogicEval.tables.tables:
            raise Exception(f'Table: [{table1}] does not exist')
        if table2 not in LogicEval.tables.tables :
            raise Exception(f'Table: [{table2}] does not exist')
        if attribute not in LogicEval.tables.tables[table1]['header'] or attribute not in LogicEval.tables.tables[table2]['header']:
            raise Exception(f'Attribute: [{attribute}] is not common or doesnt exist in tables {table1}, {table2}')

        return LogicEval.tables.join_tables(table1, table2, attribute)

    @staticmethod
    def _create(args):
        # args=[nome tabela, {header:[col1,col2, col3], rows: [[val1,val2,cal3],[val1,val2,cal3],[val1,val2,cal3]]}]
        # args=[nome tabela, [col1,col2,col3,col4]]
        if type(args[-1]) is list:
            tablename, cols = args
            if tablename in LogicEval.tables.tables:
                raise Exception(f'Table {tablename} already exists!')
            else:
                return LogicEval.tables.create_empty_table(tablename, cols)
        else:
            tablename, table = args
            if tablename in LogicEval.tables.tables:
                raise Exception(f'Table {tablename} already exists!')
            else:
                if type(table) is str:
                    return LogicEval.tables.create_from_table(tablename, table)
                else:
                    return LogicEval.tables.create_from_select(tablename, table)

    @staticmethod
    def _select(args):
        if type(args[2]) != list:
            cols, table, lim = args

            if '*' in cols and len(cols) > 1:
                raise Exception('* cant have cols to select')

            if '*' not in cols and len(cols) > len(LogicEval.tables.tables[table]['header']):
                raise Exception(
                    f'Amount of columns({len(cols)}) doesnt match table {table}, expected ({len(LogicEval.tables.tables[table]["header"])})')

            if '*' not in cols:
                for col in cols:
                    if col not in LogicEval.tables.tables[table]['header']:
                        raise Exception(f'col: {col} not in table {table}')

            return LogicEval.tables.select_table(cols, table, lim)
        else:
            cols, table, cond, lim = args

            if len(cond) == 0:
                raise Exception('WHERE statement must have a condition')

            if '*' in cols and len(cols)>1:
                raise Exception('* cant have cols to select')

            if '*' not in cols and len(cols) > len(LogicEval.tables.tables[table]['header']):
                raise Exception(f'Amount of columns({len(cols)}) doesnt match table {table}, expected ({len(LogicEval.tables.tables[table]["header"])}')

            if '*' not in cols:
                for col in cols:
                    if col not in LogicEval.tables.tables[table]['header']:
                        raise Exception(f'col: {col} not in table {table}')

            for condition in cond:
                if len(condition) < 3:
                    raise Exception('Condition must have column, comparator and value: ex(col1 > 20)')
                if condition[0] not in LogicEval.tables.tables[table]['header']:
                    raise Exception(f'{condition[0]} not in table {table}')

            return LogicEval.tables.select_table(cols, table, lim, condition=cond)

    @staticmethod
    def evaluate(ast):
        if type(ast) is dict:
            return LogicEval._eval_operator(ast)
        if type(ast) is str:
            return ast
        if type(ast) is float:
            return ast
        if type(ast) is list:
            ans = None
            for a in ast:
                ans = LogicEval.evaluate(a)
            return ans

        raise Exception("Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if 'command' in ast:
            command = ast["command"]
            args = [LogicEval.evaluate(a) for a in ast['args']]

            if 'lim' in ast:
                args.append(ast['lim'])
            if 'code' in ast:
                args.append(ast['code'])
            if command in LogicEval.commands:
                func = LogicEval.commands[command]
                return func(args)
            else:
                raise Exception(f"Unknown operator {command}")

        if 'join' in ast:
            args = [LogicEval.evaluate(a) for a in ast['join']]
            return LogicEval._join(args)

        if 'list' in ast:
            return ast['list']

        if 'str' in ast:
            return ast['str']

