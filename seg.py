# -*- coding: cp936 -*-

import NLPIR
import os

class Seg:
        def __init__(self,code='GBK'):
                dataurl = os.path.join('')#��ǰĿ¼

                if code=='GBK':
                        NLPIR.NLPIR_Init(dataurl,NLPIR.ENCODING.GBK_CODE)
                elif code=='UTF-8':
                        NLPIR.NLPIR_Init(dataurl,NLPIR.ENCODING.UTF8_CODE)
                elif code=='BIG5':
                        NLPIR.NLPIR_Init(dataurl,NLPIR.ENCODING.BIG5_CODE)
                elif code=='GBK_FANTI':
                        NLPIR.NLPIR_Init(dataurl,NLPIR.ENCODING.GBK_FANTI_CODE)
                else:print "code wrong!"
        def seg(self,str):
                """
                �ִ�
                """
                return NLPIR.ParagraphProcess(str,0)

        def tag(self,str):
                """
                ���Ա�ע
                """
                return NLPIR.ParagraphProcess(str,1)

        def fileSeg(self,sourceFile,targetFile):
                """
                �ļ��ִ�
                """
                return NLPIR.FileProcess(sourceFile,targetFile,0)

        def fileTag(self,sourceFile,targetFile):
                """
                �ļ����Ա�ע
                """
                return NLPIR.FileProcess(sourceFile,targetFile,1)
        def importUserDict(self,userDictFile):
                """
                �����û��ʵ䣬���ص���ɹ��ʸ���
                """
                return NLPIR.ImportUserDict(userDictFile)
        def addUserWord(self,word):
                "return 0 or 1"
                return NLPIR.AddUserWord(word)
                
        def saveTheUserDict(self):
                "return 1 true or 2 false"
                return NLPIR.SaveTheUsrDic()
        def delUserWord(self,word):
                """Returns    :
                -1,the word not exist in the user dictionary;
                else, the handle of the word deleted
                """
                return NLPIR.DelUsrWord(word)

        def exit(self):
                return NLPIR.Exit()

        
        
