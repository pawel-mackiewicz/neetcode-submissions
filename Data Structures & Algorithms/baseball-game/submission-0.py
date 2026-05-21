class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                b = record.pop()
                a = record.pop()
                c = a + b
                record.append(a) 
                record.append(b)
                record.append(c)
            elif op == 'D':
                a = record[-1]
                record.append(a*2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
        return sum(record)