from tabula import read_pdf


# try:
#   df2 = read_pdf("2018-2019.pdf")
# except error:
#   print ("error _>"+error)

# df = pd.DataFrame(df2)

# print(df.columns)
# print(df["Unnamed: 0"])
emailText = ""

for page in range(1,3):# [1,2]
  df_of_page = read_pdf("2018-2019.pdf",pages=page)
  ids = df_of_page["Unnamed: 0"]
  for id_number in ids:
    metu_email = "e" + (str(id_number))[0:6] + "@metu.edu.tr"
    emailText += metu_email + "\n"
    # print(metu_email)


## 
#
file = open("email.txt","a")
file.write(emailText)