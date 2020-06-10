from PIL import Image
im = Image.open("toread.png")
l = list(im.getdata())
d = {"(0, 0, 255)":"b","(0, 255, 255)":"c","(0, 255, 0)":"g","(255, 255, 0)":"y","(255, 0, 0)":"r","(255, 255, 255)":"l","(0, 0, 0)":"d","(255, 0, 255)":"m","(128, 128, 128)":"s"}

c = 0
megalist = []
sub = ''
for i in l:
	if c == 100:
		megalist.append(sub)
		sub = ''
		c = 0
	sub+=d[str(i)]
	c+=1
megalist.append(sub)
d = {
	"mrgybc":"A",
	"rmgybc":"B",
	"rgmybc":"C",
	"rgymbc":"D",
	"rgybmc":"E",
	"rgybcm":"F",
	"grybcm":"G",
	"gyrbcm":"H",
	"gybrcm":"I",
	"gybcrm":"J",
	"gybcmr":"K",
	"ygbcmr":"L",
	"ybgcmr":"M",
	"ybcgmr":"N",
	"ybcmgr":"O",
	"ybcmrg":"P",
	"bycmrg":"Q",
	"bcymrg":"R",
	"bcmyrg":"S",
	"bcmryg":"T",
	"bcmrgy":"U",
	"cbmrgy":"V",
	"cmbrgy":"W",
	"cmrbgy":"X",
	"cmrgby":"Y",
	"cmrgyb":"Z",
	"dllddl":".", #d->black l->white s->gray
	"lddlld":",",
	"llllll":" ",
	"dddddd":" ",
	"dsldsl":"0",
	"sdldsl":"1",
	"slddsl":"2",
	"sldsdl":"3",
	"sldsld":"4",
	"lsdsld":"5",
	"ldssld":"6",
	"ldslsd":"7",
	"ldslds":"8",
	"dlslds":"9"
}

for i in range(0,len(megalist)-2,3):
	a = megalist[i]
	b = megalist[i+1]
	c = megalist[i+2]

	for j in range(0,100,2):
		print(d[a[j:j+2] + b[j:j+2] + c[j:j+2]],end = '')
print()
