# -*- coding: cp936 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

'''
Python Warpper for ICTCLAS2014
Loading functions from Dynamic Link Library  directly.
'''
from ctypes import *
from os.path import dirname
#NLPIR2014 Lib File (NLPIR64, NLPIR32, libNLPIR64.so, libNLPIR32.so),
#Change this when you are not using a Win64 environment:
libFile = dirname(__file__)+r'/nlpir/NLPIR64'

dll =  CDLL(libFile)
def loadFun(exportName, restype, argtypes):
    global dll
    f = getattr(dll,exportName)
    f.restype = restype
    f.argtypes = argtypes
    return f

class ENCODING:
    GBK_CODE        =   0               #Ĭ��֧��GBK����
    UTF8_CODE       =   GBK_CODE+1      #UTF8����
    BIG5_CODE       =   GBK_CODE+2      #BIG5����
    GBK_FANTI_CODE  =   GBK_CODE+3      #GBK���룬�������������

class POSMap:
    ICT_POS_MAP_SECOND  = 0 #������������ע��
    ICT_POS_MAP_FIRST   = 1 #������һ����ע��
    PKU_POS_MAP_SECOND  = 2 #���������ע��
    PKU_POS_MAP_FIRST   = 3	#����һ����ע��

POS = {
	"n": {  #1.	����  (1��һ�࣬7�����࣬5������)
		"n":"����",
		"nr":"����",
		"nr1":"��������",
		"nr2":"��������",
		"nrj":"��������",
		"nrf":"��������",
		"ns":"����",
		"nsf":"�������",
		"nt":"����������",
		"nz":"����ר��",
		"nl":"�����Թ�����",
		"ng":"����������"
	},
	"t": {  #2.	ʱ���(1��һ�࣬1������)
		"t":"ʱ���",
		"tg":"ʱ���������"
	},
	"s": {  #3.	������(1��һ��)
		"s":"������"
	},
	"f": {  #4.	��λ��(1��һ��)
		"f":"��λ��"
	},
	"v": {  #5.	����(1��һ�࣬9������)
		"v":"����",
		"vd":"������",
		"vn":"������",
		"vshi":"���ʡ��ǡ�",
		"vyou":"���ʡ��С�",
		"vf":"���򶯴�",
		"vx":"��ʽ����",
		"vi":"�����ﶯ�ʣ��ڶ��ʣ�",
		"vl":"�����Թ�����",
		"vg":"����������"
	},
	"a": {  #6.	���ݴ�(1��һ�࣬4������)
		"a":"���ݴ�",
		"ad":"���δ�",
		"an":"���δ�",
		"ag":"���ݴ�������",
		"al":"���ݴ��Թ�����"
	},
	"b": {  #7.	�����(1��һ�࣬2������)
		"b":"�����",
		"bl":"������Թ�����"
	},
	"z": {  #8.	״̬��(1��һ��)
		"z":"״̬��"
	},
	"r": {  #9.	����(1��һ�࣬4�����࣬6������)
		"r":"����",
		"rr":"�˳ƴ���",
		"rz":"ָʾ����",
		"rzt":"ʱ��ָʾ����",
		"rzs":"����ָʾ����",
		"rzv":"ν����ָʾ����",
		"ry":"���ʴ���",
		"ryt":"ʱ�����ʴ���",
		"rys":"�������ʴ���",
		"ryv":"ν�������ʴ���",
		"rg":"����������"
	},
	"m": {  #10.	����(1��һ�࣬1������)
		"m":"����",
		"mq":"������"
	},
	"q": {  #11.	����(1��һ�࣬2������)
		"q":"����",
		"qv":"������",
		"qt":"ʱ����"
	},
	"d": {  #12.	����(1��һ��)
		"d":"����"
	},
	"p": {  #13.	���(1��һ�࣬2������)
		"p":"���",
		"pba":"��ʡ��ѡ�",
		"pbei":"��ʡ�����"
	},
	"c": {  #14.	����(1��һ�࣬1������)
		"c":"����",
		"cc":"��������"
	},
	"u": {  #15.	����(1��һ�࣬15������)
		"u":"����",
		"uzhe":"��",
		"ule":"�� �",
		"uguo":"��",
		"ude1":"�� ��",
		"ude2":"��",
		"ude3":"��",
		"usuo":"��",
		"udeng":"�� �ȵ� ����",
		"uyy":"һ�� һ�� �Ƶ� ��",
		"udh":"�Ļ�",
		"uls":"���� ��˵ ���� ˵��",
		"uzhi":"֮",
		"ulian":"�� " #������Сѧ�����ᡱ��
	},
	"e": {  #16.	̾��(1��һ��)
		"e":"̾��"
	},
	"y": {  #17.	������(1��һ��)
		"y":"������(delete yg)"
	},
	"o": {  #18.	������(1��һ��)
		"o":"������"
	},
	"h": {  #19.	ǰ׺(1��һ��)
		"h":"ǰ׺"
	},
	"k": {  #20.	��׺(1��һ��)
		"k":"��׺"
	},
	"x": {  #21.	�ַ���(1��һ�࣬2������)
		"x":"�ַ���",
		"xx":"��������",
		"xu":"��ַURL"
	},
	"w":{   #22.	������(1��һ�࣬16������)
		"w":"������",
		"wkz":"������", 	#�� ��  ��  ��  �� ��  �� ��   ��ǣ�( [ { <
		"wky":"������", 	#�� ��  �� �� ��  �� �� �� ��ǣ� ) ] { >
		"wyz":"ȫ��������", 	#�� �� ��
		"wyy":"ȫ��������", 	#�� �� ��
		"wj":"ȫ�Ǿ��",	#��
		"ww":"�ʺ�",	#ȫ�ǣ��� ��ǣ�?
		"wt":"̾��",	#ȫ�ǣ��� ��ǣ�!
		"wd":"����",	#ȫ�ǣ��� ��ǣ�,
		"wf":"�ֺ�",	#ȫ�ǣ��� ��ǣ� ;
		"wn":"�ٺ�",	#ȫ�ǣ���
		"wm":"ð��",	#ȫ�ǣ��� ��ǣ� :
		"ws":"ʡ�Ժ�",	#ȫ�ǣ�����  ��
		"wp":"���ۺ�",	#ȫ�ǣ�����   ����   ������   ��ǣ�---  ----
		"wb":"�ٷֺ�ǧ�ֺ�",	#ȫ�ǣ��� ��   ��ǣ�%
		"wh":"��λ����"	#ȫ�ǣ��� �� ��  ��  ��  ��ǣ�$
	}
}

class SegAtom(Structure):
    _fields_ = [("start", c_int32), ("length", c_int32),
        ("sPOS", c_char * 40),      ("iPOS", c_int32),
        ("word_ID", c_int32),       ("word_type", c_int32), ("weight", c_int32)
    ]

def translatePOS(sPOS):
    global POS
    if sPOS=='url': sPOS = 'xu'
    c = sPOS[0]
    return POS[c][sPOS]

Init = loadFun('NLPIR_Init',c_int, [c_char_p, c_int, c_char_p])
Exit = loadFun('NLPIR_Exit',c_bool, None)
ParagraphProcess = loadFun('NLPIR_ParagraphProcess',c_char_p, [c_char_p, c_int])
ParagraphProcessA = loadFun('NLPIR_ParagraphProcessA',POINTER(SegAtom), [c_char_p, c_void_p, c_bool])
#ParagraphProcessAW = loadFun('NLPIR_ParagraphProcessAW',None, [c_int, POINTER(SegAtom)])
FileProcess = loadFun('NLPIR_FileProcess',c_double, [c_char_p, c_char_p, c_int])
ImportUserDict = loadFun('NLPIR_ImportUserDict',c_uint, [c_char_p])
AddUserWord = loadFun('NLPIR_AddUserWord', c_int, [c_char_p])
SaveTheUsrDic = loadFun('NLPIR_SaveTheUsrDic', c_int, None)
DelUsrWord = loadFun('NLPIR_DelUsrWord',c_int, [c_char_p])
GetUniProb = loadFun('NLPIR_GetUniProb', c_double, [c_char_p])
IsWord = loadFun('NLPIR_IsWord',c_bool, [c_char_p])
GetKeyWords = loadFun('NLPIR_GetKeyWords',c_char_p, [c_char_p, c_int, c_bool])
GetFileKeyWords = loadFun('NLPIR_GetNewWords',c_char_p, [c_char_p, c_int, c_bool])
GetNewWords = loadFun('NLPIR_GetNewWords', c_char_p, [c_char_p, c_int, c_bool])
GetFileNewWords = loadFun('NLPIR_GetFileNewWords',c_char_p, [c_char_p, c_int, c_bool])
FingerPrint = loadFun('NLPIR_FingerPrint',c_ulong, [c_char_p])
SetPOSmap = loadFun('NLPIR_SetPOSmap',c_int, [c_int])
#New Word Identification
NWI_Start = loadFun('NLPIR_NWI_Start', c_bool, None)
NWI_AddFile = loadFun('NLPIR_NWI_AddFile',c_bool, [c_char_p])
NWI_AddMem = loadFun('NLPIR_NWI_AddMem',c_bool, [c_char_p])
NWI_Complete = loadFun('NLPIR_NWI_Complete', c_bool, None)
NWI_GetResult = loadFun('NLPIR_NWI_GetResult',c_char_p, [c_int])
NWI_Result2UserDict = loadFun('NLPIR_NWI_Result2UserDict',c_uint, None)

def NLPIR_Init(dataurl, CODE):
    #if not Init('',ENCODING.UTF8_CODE,''):
    if not Init(dataurl, CODE,''):
        print("Initialization failed!")
        exit(-111111)
    else:
        pass
        #print("succeed")
#SetPOSmap(3)
'''
if not SetPOSmap(1): #POSMap.ICT_POS_MAP_SECOND
    print("Setting POS Map failed!")
    exit(-22222)
'''
'''
def seg(paragraph):
    result = ParagraphProcess(paragraph, c_int(1))
    atoms = [i.strip().split('/') for i in result.split(' ') if len(i)>=1 and i[0]!=' ']
    atoms = [(a[0],a[1]) for a in atoms if len(a[0])>0]
    return atoms

def segment(paragraph):
    count = c_int32()
    result = ParagraphProcessA(paragraph, byref(count),c_bool(True))
    count = count.value
    atoms = cast(result, POINTER(SegAtom))
    return [atoms[i] for i in range(0,count)]

def Seg(paragraph):
    atoms = segment(paragraph)
    for a in atoms:
        if len(a.sPOS) < 1: continue
        i = paragraph[a.start: a.start + a.length]#.decode('utf-8')#.encode('ascii')
        yield (i, a.sPOS)

if __name__ == "__main__":
    p = "Big News: @����ձ� [����]��������·��ԭ���ֳ��������� ��ͷʹ��Ǯ��2013��12�µף�������·��ԭ���ֳ��������ܻ߱�����������˵��ͷʹ��Ǯ���Ӻ��ͺ��ص��������������ǹ��������ⷿ���ڻ�֮��ȥ�Ŀ־��У������8800����Ԫ419��ŷԪ30�򡢸۱�27�򣬻ƽ�43.3����𽥶������������ӡ��� http://t.cn/8kgR6Yi"
    p = "1978���¼ұ��������һ�����ˡ�һ���ֵ����ȸ���������ʵ�ֹ�ͬ��ԣ�����˼��ӵ�ʱ�ı����ȿ���"
    for t in Seg(p): #.decode('UTF8').encode('GBK')
        s = '%s\t%s\t%s' % (t[0],t[1],translatePOS(t[1]))
        print(s)
'''
