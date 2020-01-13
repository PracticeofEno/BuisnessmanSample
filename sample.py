import sys
import requests
import xml.etree.ElementTree as ElementTree


Posturl = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId="
XmlRaw = "<map id=\"ATTABZAA001R08\"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>\{x\}</txprDscmNo><dongCode>15</dongCode><psbSearch>Y</psbSearch><map id=\"userReqInfoVO\"/></map>"


def call(res_text):
    index = res.text.find("<smpcBmanTrtCntn>")
    r_index = res.text.find("</smpcBmanTrtCntn>")
    result = res.text[index:r_index]
    return result.replace("<smpcBmanTrtCntn>","")

if(len(sys.argv) < 2):
    print("Why hangul aneho?")
    exit()

value = sys.argv[1]
res = requests.post(Posturl,data=XmlRaw.replace("\{x\}",value),headers = {'Content-Type': 'text/xml'})
print(call(res.text))


