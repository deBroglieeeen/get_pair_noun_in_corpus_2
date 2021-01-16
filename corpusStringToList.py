import re
import unicodedata
text = input()
#text = open("/Users/munekiyonaoto/Downloads/data.txt").read()

def simplifiedTree(text):
  modified = re.sub(r'\(','[',text)
  print(modified)
  modified = re.sub(r'\)',']',modified)
  print(modified)
  modified = re.sub(r'([A-Z]+\.[0-9]+\.[0-9]+\s)','',modified)
  print(modified)
  #modified = re.sub(r'([^\s]+\s)','\'\1\',',modified)

  print(modified)
  modified = re.sub(r'([A-Z]+)',r"'\1',",modified)
  modified = re.sub(r'([a-z]+)',r"'\1',",modified)
  print(modified)
  #modified = re.sub(r"(^\[^'+^[A-Z]+,+^\s+^\]+)",r"'\1'",modified)
  #modified = re.sub(r'([U+1000–U+109F]+)',r"'\1'",modified)
  #modified = re.sub(r"(u'Myanmar'+)",r"'\1",modified)

  # 英文を全て削除したが本文にも英文が残っているので注意
  # ただ、アルファベットのついてる英文の頻度は少ないので今回は無視する
  modified = re.sub(r"([^0-9'[,.a-zA-Z\]()\s]+)",r"'\1'",modified)
  print(modified)
  print(eval(modified))
def removeAllTag(text):
  modified = re.sub(r'\(|\)|[a-z]|[A-Z]|[0-9]|\.+','',text)
  #print(modified)
  modified = re.sub(r'\s+',',',modified)
  #modified = re.sub(r',')
  #print(modified)
  word_list = modified.split(',')
  while("" in word_list) :
    word_list.remove("")
  return word_list
#text = open("ALTCorpus.txt").read()
#print(text)
sentence = ""
# for word in removeAllTag(text):
#   sentence.append(word)
print(sentence.join(removeAllTag(text)))
isPlace = False

#simplifiedTree(text)

