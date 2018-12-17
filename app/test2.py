#encoding:utf-8
'''
所有的路走一遍

停止条件：所有路都走完

'''
import traceback
import re

# X = [(1,2),(3,2),(4,5),(7,2)]
X = []
# X_attached = [False,False,False,False]
X_attached = []
X_len = len(X)
X_attached_count = 0

source = ()
dest_list = []
dest_attached = []
steps_list = [] #步数列表
path_list = [] #路径列表

input = '''
XXXXXX
X*OOOX
XOO#OX
XXXXXX
'''
def generate_data(input):
    global X
    global X_attached
    global X_len
    global X_attached_count
    global steps_list
    lines = re.findall(r'.+\n',input)
    for index,line in enumerate(lines):
        y = -(index+1)
        for x,val in enumerate(line):
            x = +x
            if val=='X':
                X.append((x,y))
                X_attached.append(False)
            elif val == 'O':
                pass
            elif val == '*':
                dest_list.append((x,y))
                dest_attached.append(False)
            elif val == '#':
                source = (x,y)
            else:
                raise Exception('不识别输入{0}'.format(val))
    if not len(X) == len(set(X)):
        raise Exception('X 有重复 {0}'.format(X))
    else:
        X_len = len(X)
    if not len(dest_list) == len(set(dest_list)):
        raise Exception('dest_list 有重复 {0}'.format(dest_list))

def valid_correct():
    global X
    global X_attached
    global X_len
    global X_attached_count
    global steps_list

    X = []
    # X_attached = [False,False,False,False]
    X_attached = []
    X_len = len(X)
    X_attached_count = 0

    source = ()
    dest_list = []
    dest_attached = []
    steps_list = []  # 步数列表
    path_list = []  # 路径列表

    def is_repeated(list):
        if not len(list) == len(set(list)):
            raise Exception('重复了 {0}'.format(list))

    for val in [X,dest_list,]:
        pass

def record_path(path):
    # 将路径记录在案
    init_path_list_len = len(path_list)
    path_list.append(tuple(path))
    after_path__list_len = len(path_list)
    if not after_path__list_len - init_path_list_len == 1:
        raise Exception('增加路径数量不对  {0}'.format(after_path__list_len - init_path_list_len))


def judge_after_moved(source, step_count, path):
    global X
    global X_attached
    global X_len
    global X_attached_count
    global steps_list


    try:
        #如果曾经走过这一步，返回，不记录路径
        if source in path:
            return
        # 如果碰壁，并且该X坐标的X_attached标记为False，就将X上的该坐标标记为True，并且X_attached_count++
        index = X.index(source)
        if not X_attached[index]:
            X_attached[index]=True
            X_attached_count = + X_attached_count
            record_path(path)
            # 判断一下中共碰的壁是否小于等于X_len,如果大于就报错
            if X_attached_count>X_len:
                raise  Exception('碰到墙壁总数壁X_len大，肯定有问题')
            return #碰壁就停止
    except ValueError:
        # 如果没问题就判断是否到达目的地,到了就记录步数，并停止当前路程
        if source in dest_attached:
            steps_list.append(step_count)
            record_path(path)
            dest_attached[dest_attached.index(source)]=True
            return
        # 如果还没到目的地就递归
        else:
            source_next(source, path, step_count)
    except Exception as e:
        traceback.format_exc()


def source_next(source ,path=set, step_count=0):
    step_count = + step_count
    init_path_len = len(path)
    path.add(source)
    after_path_len = len(path)
    if not after_path_len-init_path_len == 1:
        raise Exception('增加路径步数不对  {0}'.format(after_path_len-init_path_len))
    source = list(source)
    # 尝试移动x
    source[0]= + source[0]
    judge_after_moved(tuple(source), step_count, path)
    source[0]= - source[0]
    judge_after_moved(tuple(source), step_count, path)
    # 尝试移动y并重复x一样的动作
    source[1]= + source[1]
    judge_after_moved(tuple(source), step_count, path)
    source[1]= - source[1]
    judge_after_moved(tuple(source), step_count, path)



if __name__=="__main__":
    pass