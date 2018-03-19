import unittest

inp = '516299281491169512719425276194596424291268712697155863651846937925928456958813624428156218468331423858422613471962165756423837756856519754524985759763747559711257977361228357678293572698839754444752898835313399815748562519958329927911861654784216355489319995566297499836295985943899373615223375271231128914745273184498915241488393761676799914385265459983923743146555465177886491979962465918888396664233693243983969412682561799628789569294374554575677368219724142536789649121758582991345537639888858113763738518511184439854223386868764189133964543721941169786274781775658991329331759679943342217578532643519615296424396487669451453728113114748217177826874953466435436129165295379157226345786756899935747336785161745487933721527239394118721517195849186676814232887413175587327214144876898248571248517121796766248817366614333915154796983612174281237846165129114988453188844745119798643314857871527757831265298846833327863781341559381238458322786192379487455671563757123534253463563421716138641611915686247343417126655317378639314168461345613427262786624689498485599942336813995725145169355942616672812792174556866436158375938988738721253664772584577384558696477546232189312287262439452141564522329987139692281984783513691857538335537553448919819545332125483128878925492334361562192621672993868479566688564752226111784486619789588318171745995253645886833872665447241245329935643883892447524286642296955354249478815116517315832179925494818748478164317669471654464867111924676961162162841232473474394739793968624974397916495667233337397241933765513777241916359166994384923869741468174653353541147616645393917694581811193977311981752554551499629219873391493426883886536219455848354426461562995284162323961773644581815633779762634745339565196798724847722781666948626231631632144371873154872575615636322965353254642186897127423352618879431499138418872356116624818733232445649188793318829748789349813295218673497291134164395739665667255443366383299669973689528188264386373591424149784473698487315316676637165317972648916116755224598519934598889627918883283534261513179931798591959489372165295'

def captcha_original(number):
    sum = 0
    shifted_number = number[-1] + number[:-1]
    for (c,n) in zip(number, shifted_number):
        if c == n:
             sum += int(c)
    return sum

def captcha_original(number):
    sum = 0
    shift = len(number)//2
    shifted_number = number[-shift:] + number[:-shift]
    for (c,n) in zip(number, shifted_number):
        if c == n:
             sum += int(c)
    return sum

def captcha(digits):
    return sum([int(d) for i, d in enumerate(digits) if digits[i] == digits[(i+1) % len(digits)]])

def captcha2(digits):
    size = len(digits)
    return sum([int(d) for i, d in enumerate(digits) if digits[i] == digits[(i+size//2) % size]])

class Test(unittest.TestCase):
    def test_1122(self):
        self.assertEqual(captcha('1122'), 3)

    def test_1111(self):
        self.assertEqual(captcha('1111'), 4)

    def test_1234(self):
        self.assertEqual(captcha('1234'), 0)

    def test_91212129(self):
        self.assertEqual(captcha('91212129'), 9)

    def test2_1212(self):
        self.assertEqual(captcha2('1212'), 6)

    def test2_1221(self):
        self.assertEqual(captcha2('1221'), 0)

    def test2_123425(self):
        self.assertEqual(captcha2('123425'), 4)

    def test2_123123(self):
        self.assertEqual(captcha2('123123'), 12)

    def test2_12131415(self):
        self.assertEqual(captcha2('12131415'), 4)
    
    def test_input(self):
        self.assertEqual(captcha(inp),1251)

    def test2_input(self):
        self.assertEqual(captcha2(inp),1244)


print("Result:", captcha(inp))
print("Result Part 2:", captcha2(inp))
unittest.main()
