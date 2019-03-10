import pandas as pd

df = pd.read_csv("./data.csv")


# print df.head() ## ilk 4 satisr
# print df.tail() ## son 4 satir
# print df.columns ## sutunlar
# for i in df: # get columns
#   print i

# print df["puan"][4]

# print df.loc[[2]]

def get_field(df,index,field):
  arr = ((df.loc[[index]][field]).to_string()).split(" ")
  return str(arr[len(arr) - 1])

satirSayisi = (df).size / (df.columns).size
#numofbooks,internship,homeworks,participation,community,puan

jsonText = "["
for row in range(1,satirSayisi):
  jsonText += "{ input : { numofbooks :" + get_field(df,row,"numofbooks") + ","
  jsonText += "internship : " + get_field(df,row,"internship") + ","
  jsonText += "homeworks : " + get_field(df,row,"homeworks") + ","
  jsonText += "participation : " + get_field(df,row,"participation") + ","
  jsonText += "community :" + get_field(df,row,"community") + "},"
  aa = 999
  dd = 999
  if get_field(df,row,"puan") == "AA":
    aa = 1
    dd = 0
  else:
    aa = 0
    dd = 1
  jsonText += "output : { AA : " + str(aa) + " , DD : " + str(dd) + "}"
  jsonText += "},"

jsonText += "]"
# print jsonText

file = open("data.json","a")
file.write(jsonText)


