#混淆：密钥字母后面接一个明文字母，之后随机插入0-3个字符再出现下一个密钥明文对
#1.密钥串的循环 2.排除密钥字母 3插入混淆字符
#tip:morsecode yourname MIGI+泉新一
#映射 morse code: 字母间以空格分隔，//[]单词间以/分隔
import random

key = "dsf"
msg = "goodgirl"#如何处理空格
print("msg:%s"%(msg))

#生成不包括key的字母字表
alpha = "abcdefghijklmnopqrstuvwxyz"
encryt_table = [x for x in alpha if x not in key ]

randmsg = ""
pos=0
msg_len = len(msg)

#encryption
#step 1: mix
while True:
    for c in key:
        #disturb_char_count = random.randint(0, 3)#插入3个随机字符
        #for i in range(disturb_char_count):
            #列表中随机选3个
        randmsg += ''.join( random.sample(encryt_table, random.randint(0, 3)))
        randmsg += msg[pos]
        randmsg += c
        pos += 1
        if pos == msg_len:
            break
    if pos == msg_len:
        break
print("randmsg:%s"%(randmsg))

#step 2: reflect morse code
alpha = "abcdefghijklmnopqrstuvwxyz"
pot = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
       "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
       "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
       "-.--", "--.."]

#generate morse dictionary 
morse_table = {}
for c in alpha:
    morse_table[c] = pot[ alpha.index(c)]

morse_code = ""
for c in randmsg:
    morse_code += morse_table[c]
    morse_code += ' '
print("morse_code:%s"%(morse_code))

#crack


#print( random.randint(0, 3) )
