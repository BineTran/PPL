import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test101(self):
        self.assertTrue(TestLexer.test(""" fact: integer (n: auto) {
                        while(a)
                            if(a < 10) a = a + 1
                    } """, "fact,:,integer,(,n,:,auto,),{,while,(,a,),if,(,a,<,10,),a,=,a,+,1,},<EOF>", 101))
    def test102(self):
        self.assertTrue(TestLexer.test(".e32", "Ra2Ejj46lx5C9fD6rHc,<EOF>", 102))
    def test103(self):
        self.assertTrue(TestLexer.test("KjHqatNhm1", "KjHqatNhm1,<EOF>", 103))
    def test104(self):
        self.assertTrue(TestLexer.test("cOqiz53hD3_RWPRA_2j", "cOqiz53hD3_RWPRA_2j,<EOF>", 104))
    def test105(self):
        self.assertTrue(TestLexer.test("ADD", "ADD,<EOF>", 105))
    def test106(self):
        self.assertTrue(TestLexer.test("1.2e","1.2,e,<EOF>", 106))
    def test107(self):
        self.assertTrue(TestLexer.test("377489_8621_9218063205_3513524309_8593485024201660792007_87625760_426656324_5700333e+98650947474453708979848414837524247418248225766399582704288782639198912300516232928954430593363","3774898621921806320535135243098593485024201660792007876257604266563245700333e+98650947474453708979848414837524247418248225766399582704288782639198912300516232928954430593363,<EOF>", 107))
    def test108(self):
        self.assertTrue(TestLexer.test("670026958631717523e-93751946295747893305903159275499","670026958631717523e-93751946295747893305903159275499,<EOF>", 108))
    def test109(self):
        self.assertTrue(TestLexer.test(".e2",".,e2,<EOF>", 109))
    def test110(self):
        self.assertTrue(TestLexer.test(""" "ab\c" ""","""Illegal Escape In String: ab\c""", 110))
    def test111(self):
        self.assertTrue(TestLexer.test(""" "abc\c" """, """Illegal Escape In String: abc\c""", 111))
    def test112(self):
        self.assertTrue(TestLexer.test("//My name is Bine", "<EOF>", 112))
    def test113(self):
        self.assertTrue(TestLexer.test( """ "ABC\\C" """ , """Illegal Escape In String: ABC\C""", 113))
    def test114(self):
        self.assertTrue(TestLexer.test( """ "My name's Bine." """ , """My name's Bine.,<EOF>""", 114))
    def test115(self):
        self.assertTrue(TestLexer.test( "/* Alo 1234 You can count on me*/ */" , "*,/,<EOF>", 115))
    def test116(self):
        self.assertTrue(TestLexer.test( "/*Who is your father*/" , "<EOF>", 116))
    def test117(self):
        self.assertTrue(TestLexer.test( "12345e6;" , "12345e6,;,<EOF>", 117))
    def test118(self):
        self.assertTrue(TestLexer.test( "@abchadmskmkamdalsmkdlkdm!" , "Error Token @", 118))
    def test119(self):
        self.assertTrue(TestLexer.test( "7E-10" , "7E-10,<EOF>", 119))
    def test120(self):
        self.assertTrue(TestLexer.test( "{1,2,3, "" aa""}" , "{,1,,,2,,,3,,,aa,},<EOF>", 120))
    def test121(self):
        self.assertTrue(TestLexer.test( "+=*/234" , "+,=,*,/,234,<EOF>", 121))
    def test122(self):
        self.assertTrue(TestLexer.test( "!&&||%==!=" , "!,&&,||,%,==,!=,<EOF>", 122))
    def test123(self):
        self.assertTrue(TestLexer.test( "::>=<=" , "::,>=,<=,<EOF>", 123))
    def test124(self):
        self.assertTrue(TestLexer.test( "a[1,2]>=a[2,3]" , "a,[,1,,,2,],>=,a,[,2,,,3,],<EOF>", 124))
    def test125(self):
        self.assertTrue(TestLexer.test( "auto break boolean do else false float for function if integer return string true while void out continue of inherit array" , "auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>", 125))
    def test126(self):
        self.assertTrue(TestLexer.test( "abc : integer" , """abc,:,integer,<EOF>""", 126))
    def test127(self):
        self.assertTrue(TestLexer.test( """@bcd_d : float""" , """Error Token @""", 127))
    def test128(self):
        self.assertTrue(TestLexer.test( """abc_2 : float = 2;""" , """abc_2,:,float,=,2,;,<EOF>""", 128))
    def test129(self):
        self.assertTrue(TestLexer.test( """abc_2 : float = 2,3,4,5,6,7;""" , """abc_2,:,float,=,2,,,3,,,4,,,5,,,6,,,7,;,<EOF>""", 129))
    def test130(self):
        self.assertTrue(TestLexer.test( """a : boolean = 2+3%2-1""" , """a,:,boolean,=,2,+,3,%,2,-,1,<EOF>""", 130))
    def test131(self):
        self.assertTrue(TestLexer.test( """identifia : float""" , """identifia,:,float,<EOF>""", 131))
    def test132(self):
        self.assertTrue(TestLexer.test( """x: integer = 65; fact: function integer (n: innteger){}""" , """x,:,integer,=,65,;,fact,:,function,integer,(,n,:,innteger,),{,},<EOF>""", 132))
    def test133(self):
        self.assertTrue(TestLexer.test( """if (ulikeme == true) return 1; else return 0;""" , """if,(,ulikeme,==,true,),return,1,;,else,return,0,;,<EOF>""", 133))
    def test134(self):
        self.assertTrue(TestLexer.test( """ "abcsjsj  \r aa" """ , """Unclosed String: abcsjsj  \n""", 134))
    def test135(self):
        self.assertTrue(TestLexer.test( """ "abcsjsj  \n aa" """ , """Unclosed String: abcsjsj  \n""", 135))
    def test136(self):
        self.assertTrue(TestLexer.test( """123e45bcdv""" , """123e45,bcdv,<EOF>""", 136))
    def test137(self):
        self.assertTrue(TestLexer.test( """if23ULikeMePlsTalkToMe1235""" , """if23ULikeMePlsTalkToMe1235,<EOF>""", 137))
    def test138(self):
        self.assertTrue(TestLexer.test( """for(i = 2,i<=3,i=i*2)""" , """for,(,i,=,2,,,i,<=,3,,,i,=,i,*,2,),<EOF>""", 138))
    def test139(self):
        self.assertTrue(TestLexer.test( """for (i = 1, i < 10, i + 1) {writeInt(i);}""" , """for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>""", 139))
    def test140(self):
        self.assertTrue(TestLexer.test( """while(1){a : integer = 2}""" , """while,(,1,),{,a,:,integer,=,2,},<EOF>""", 140))
    def test141(self):
        self.assertTrue(TestLexer.test( """do {a=a+2} while (a <= 23);""" , """do,{,a,=,a,+,2,},while,(,a,<=,23,),;,<EOF>""", 141))
    def test142(self):
        self.assertTrue(TestLexer.test( """{r, s: int;r = 2.0;a, b: array [5] of int;s = r * r * myPI;a[0] = s;}""" , """{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>""", 142))
    def test143(self):
        self.assertTrue(TestLexer.test( """readInteger()printInteger(anArg: integer)readFloat()writeFloat(anArg: float)readBoolean()printBoolean(anArg: boolean)readString()printString(anArg: string)""" , """readInteger,(,),printInteger,(,anArg,:,integer,),readFloat,(,),writeFloat,(,anArg,:,float,),readBoolean,(,),printBoolean,(,anArg,:,boolean,),readString,(,),printString,(,anArg,:,string,),<EOF>""", 143))
    def test144(self):
        self.assertTrue(TestLexer.test( """preventDefault()""" , """preventDefault,(,),<EOF>""", 144))
    def test145(self):
        self.assertTrue(TestLexer.test( """ "abc\b" """ , """abc,<EOF>""", 145))
    def test146(self):
        self.assertTrue(TestLexer.test( """ "hello hesli'sli's" """ , """hello hesli'sli's,<EOF>""", 146))
    def test147(self):
        self.assertTrue(TestLexer.test( """bine : function void (str : string)""" , """bine,:,function,void,(,str,:,string,),<EOF>""", 147))
    def test148(self):
        self.assertTrue(TestLexer.test( """bine : function void (str : string){printString("My name is Bine")}""" , """bine,:,function,void,(,str,:,string,),{,printString,(,My name is Bine,),},<EOF>""", 148))
    def test149(self):
        self.assertTrue(TestLexer.test( """return;""" , """return,;,<EOF>""", 149))
    def test150(self):
        self.assertTrue(TestLexer.test( """3.14sp0.0sp1.0-1.0sp2.71828sp-2.71828sp100.0sp0.5sp-0.5sp10.5sp123.456sp-123.456sp1e3sp1e-3sp3.0e5sp-3.0e5""" , """3.14,sp0,.,0,sp1,.,0,-,1.0,sp2,.,71828,sp,-,2.71828,sp100,.,0,sp0,.,5,sp,-,0.5,sp10,.,5,sp123,.,456,sp,-,123.456,sp1e3sp1e,-,3,sp3,.0e5,sp,-,3.0e5,<EOF>""", 150))
    def test151(self):
        self.assertTrue(TestLexer.test( """1.2345e-8""" , """1.2345e-8,<EOF>""", 151))
    def test152(self):
        self.assertTrue(TestLexer.test( """1.2345e-8-1.41421""" , """1.2345e-8,-,1.41421,<EOF>""", 152))
    def test153(self):
        self.assertTrue(TestLexer.test( """ "ab\"c" """ , """ab,c,Unclosed String:  """, 153))
    def test154(self):
        self.assertTrue(TestLexer.test( """ "abca" """ , """abca,<EOF>""", 154))
    def test155(self):
        self.assertTrue(TestLexer.test( """ "abc\\a" """ , """Illegal Escape In String: abc\\a""", 155))
    def test156(self):
        self.assertTrue(TestLexer.test( """ "Hello\tworld!\n\"I'm using C++\"" """ , """Unclosed String: Hello	world!\n""", 156))
    def test157(self):
        self.assertTrue(TestLexer.test( """ "abc" """ , """abc,<EOF>""", 157))
    def test158(self):
        self.assertTrue(TestLexer.test( """ "Code is \n art." "Coding is my happy place." "Code is the future." """ , """Unclosed String: Code is \n""", 158))
    def test159(self):
        self.assertTrue(TestLexer.test( """ bine : array [2,3] of integer = {2,3,4} """ , """bine,:,array,[,2,,,3,],of,integer,=,{,2,,,3,,,4,},<EOF>""", 159))
    def test160(self):
        self.assertTrue(TestLexer.test( """numprime, abc : integer = 2 + 3 + 4 + 5;""" , """numprime,,,abc,:,integer,=,2,+,3,+,4,+,5,;,<EOF>""", 160))
    def test161(self):
        self.assertTrue(TestLexer.test( """a[2] = "abc" """ , """a,[,2,],=,abc,<EOF>""", 161))
    def test162(self):
        self.assertTrue(TestLexer.test( """for(integer i = 0; i < 2; i = i - 1)""" , """for,(,integer,i,=,0,;,i,<,2,;,i,=,i,-,1,),<EOF>""", 162))
    def test163(self):
        self.assertTrue(TestLexer.test( """ "My name is bien" """ , """My name is bien,<EOF>""", 163))
    def test164(self):
        self.assertTrue(TestLexer.test( """for(integer i = 0; i < 100; i = i + 1){printString("u can help me")}""" , """for,(,integer,i,=,0,;,i,<,100,;,i,=,i,+,1,),{,printString,(,u can help me,),},<EOF>""", 164))
    def test165(self):
        self.assertTrue(TestLexer.test( """ "I don't understand u huhu  \\" """ , """Unclosed String: I don't understand u huhu  \\" """, 165))
    def test166(self):
        self.assertTrue(TestLexer.test( """ {} """ , """{,},<EOF>""", 166))
    def test167(self):
        self.assertTrue(TestLexer.test( """0abc_def23""" , """0,abc_def23,<EOF>""", 167))
    def test168(self):
        self.assertTrue(TestLexer.test( """abc^2""" , """abc,Error Token ^""", 168))
    def test169(self):
        self.assertTrue(TestLexer.test( """ "are u oo" """ , """are u oo,<EOF>""", 169))
    def test170(self):
        self.assertTrue(TestLexer.test( """do {a = a + 1; a = b; c = v} while (a == 1);""" , """do,{,a,=,a,+,1,;,a,=,b,;,c,=,v,},while,(,a,==,1,),;,<EOF>""", 170))
    def test171(self):
        self.assertTrue(TestLexer.test( """isPrimerightLoveme(2);""" , """isPrimerightLoveme,(,2,),;,<EOF>""", 171))
    def test172(self):
        self.assertTrue(TestLexer.test( """( ) [ ] . , ; : { } =""" , """(,),[,],.,,,;,:,{,},=,<EOF>""", 172))
    def test173(self):
        self.assertTrue(TestLexer.test( """{ {1,2,4}, {2,3,4}, {3,4,5}}""" , """{,{,1,,,2,,,4,},,,{,2,,,3,,,4,},,,{,3,,,4,,,5,},},<EOF>""", 173))
    def test174(self):
        self.assertTrue(TestLexer.test( """if (n == 0) return 1; else return 0""" , """if,(,n,==,0,),return,1,;,else,return,0,<EOF>""", 174))
    def test175(self):
        self.assertTrue(TestLexer.test( """a, b, c : array [10] of integer;""" , """a,,,b,,,c,:,array,[,10,],of,integer,;,<EOF>""", 175))
    def test176(self):
        self.assertTrue(TestLexer.test( """for(int i = 2; i < 5; i = i /2){continue;}""" , """for,(,int,i,=,2,;,i,<,5,;,i,=,i,/,2,),{,continue,;,},<EOF>""", 176))
    def test177(self):
        self.assertTrue(TestLexer.test( """while(1){continue; break;}""" , """while,(,1,),{,continue,;,break,;,},<EOF>""", 177))
    def test178(self):
        self.assertTrue(TestLexer.test( """ "abc\\e\f" """ , """Illegal Escape In String: abc\e""", 178))
    def test179(self):
        self.assertTrue(TestLexer.test( """ "usearesobad"" """ , """usearesobad,Unclosed String:  """, 179))
    def test180(self):
        self.assertTrue(TestLexer.test( """ usearesobad\" """ , """usearesobad,Unclosed String:  """, 180))
    def test181(self):
        self.assertTrue(TestLexer.test( """ usearesobad\\" """ , """usearesobad,Error Token \\""", 181))
    def test182(self):
        self.assertTrue(TestLexer.test( """ abc = 23 + 34 + a[1] """ , """abc,=,23,+,34,+,a,[,1,],<EOF>""", 182))
    def test183(self):
        self.assertTrue(TestLexer.test( """ abc = abc "adad \h x" """ , """abc,=,abc,Illegal Escape In String: adad \h""", 183))
    def test184(self):
        self.assertTrue(TestLexer.test( """while (i <= 10) {cout << i << " ";i++;}""" , """while,(,i,<=,10,),{,cout,<,<,i,<,<, ,;,i,+,+,;,},<EOF>""", 184))
    def test185(self):
        self.assertTrue(TestLexer.test( """return 0;""" , """return,0,;,<EOF>""", 185))
    def test186(self):
        self.assertTrue(TestLexer.test( """+ - * / % == != > >= < <=""" , """+,-,*,/,%,==,!=,>,>=,<,<=,<EOF>""", 186))
    def test187(self):
        self.assertTrue(TestLexer.test( """ "tran" :: "long" :: "long" """ , """tran,::,long,::,long,<EOF>""", 187))
    def test188(self):
        self.assertTrue(TestLexer.test( """ // This is an official specification of MT22, a C-like language for use in an undergraduate class.""" , """<EOF>""", 188))
    def test189(self):
        self.assertTrue(TestLexer.test( """ifwhilefordo""" , """ifwhilefordo,<EOF>""", 189))
    def test190(self):
        self.assertTrue(TestLexer.test( """ abc = 23 /*u can show*/ c = 3""" , """abc,=,23,c,=,3,<EOF>""", 190))
    def test191(self):
        self.assertTrue(TestLexer.test( """// ppl is so hard \n huhu""" , """huhu,<EOF>""", 191))
    def test192(self):
        self.assertTrue(TestLexer.test( """// alo alo \n alo alo ///////////// alo""" , """alo,alo,<EOF>""", 192))
    def test193(self):
        self.assertTrue(TestLexer.test( """abcbcd@_2""" , """abcbcd,Error Token @""", 193))
    def test194(self):
        self.assertTrue(TestLexer.test( """amksmdksdkasmdkamdksm@@""" , """amksmdksdkasmdkamdksm,Error Token @""", 194))
    def test195(self):
        self.assertTrue(TestLexer.test( """nono's na""" , """nono,Error Token '""", 195))
    def test196(self):
        self.assertTrue(TestLexer.test( """true === false""" , """true,==,=,false,<EOF>""", 196))
    def test197(self):
        self.assertTrue(TestLexer.test( """true!=false==1""" , """true,!=,false,==,1,<EOF>""", 197))
    def test198(self):
        self.assertTrue(TestLexer.test( """ "Messi iz da best. Ronaldo < Messi" """ , """Messi iz da best. Ronaldo < Messi,<EOF>""", 198))
    def test199(self):
        self.assertTrue(TestLexer.test( """1_____67________2923.E12-3""" , """1,_____67________2923,.,E12,-,3,<EOF>""", 199))
    def test200(self):
        self.assertTrue(TestLexer.test( """ "abc \" lala" """ , """abc ,lala,Unclosed String:  """, 200))