import re
import numpy as np

text = ""
with open("day11.txt") as file:
    text = file.read()
lvl_reduction = 3
class monkey():
    global lvl_reduction
    def __init__(self,items:list,operation,test:int,throw_dest) -> None:
        self.items = []
        self.operation = operation
        self.test = test
        self.throw_dest = throw_dest
        self.woryLvl = 0
        self.inspected = 0
        for i in items:
            self.addItem(i)
    
    def addItem(self,item):
        self.items.append(item)

    def calc_wory_lvl(self,item,reduction):
        if self.operation[1] == 'old':
            x = item
        else: x = self.operation[1]

        if self.operation[0] == '+':
            self.woryLvl = (item+x) // reduction
        if self.operation[0] == '*':
            self.woryLvl = (item*x) // reduction

        return self.woryLvl

    def do_test(self):
        if self.woryLvl % self.test == 0:
            dest = self.throw_dest[0]
        else:
            dest = self.throw_dest[1]
        return dest


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


monkey_text = list(divide_chunks(text.splitlines(),7))

def create_monkey_list(text):
    _list = []
    for monkey_props in text:
        items = [int(x) for x in re.findall(r'[\d]+',monkey_props[1])]
        operation = [int(x) if x.isdigit() else x for x in monkey_props[2].split('= ')[-1].split(' ')[1:]]
        test = int(monkey_props[3].split()[-1])
        throw_dest = [int(monkey_props[4].split()[-1]),int(monkey_props[5].split()[-1])]
        _list.append(monkey(items,operation,test,throw_dest))
    return _list

monkey_text = list(divide_chunks(text.splitlines(),7))
#part 1
monkey_list = create_monkey_list(monkey_text)

for turn in range(20):
    _monkey:monkey
    for _monkey in monkey_list:
        for item in _monkey.items:
            _monkey.calc_wory_lvl(item,3)
            dest = _monkey.do_test()
            monkey_list[dest].addItem(_monkey.woryLvl)        
            _monkey.inspected += 1
        _monkey.items = []
        
print ('\n')
for m in monkey_list:
    print (m.items, m.inspected)


most_active = [x.inspected for x in sorted(monkey_list,key=lambda x: x.inspected)[-2:]]
print ('Level of monkey buisness (1)= ',np.prod(most_active))

#part 2
monkey_list = create_monkey_list(monkey_text)
test_values = list(_monkey.test for _monkey in monkey_list)
common_devider = np.prod(test_values,dtype=np.int64)

for turn in range(10000):
    _monkey:monkey
    for _monkey in monkey_list:
        for item in _monkey.items:
            _monkey.calc_wory_lvl(item,1)
            dest = _monkey.do_test()
            monkey_list[dest].addItem(_monkey.woryLvl%common_devider)
            _monkey.inspected += 1
        _monkey.items = []

print ('\n')
for m in monkey_list:
    print (m.items, m.inspected)

most_active = [x.inspected for x in sorted(monkey_list,key=lambda x: x.inspected)[-2:]]
print ('Level of monkey buisness (2)= ',np.prod(most_active,dtype=np.int64))



