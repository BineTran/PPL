# import unittest
# from TestUtils import TestParser


# class ParserSuite(unittest.TestCase):
#     def test201(self):
#         input = """
#         main: function void () {
#             mynamisbien : string;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
#     def test202(self):
#         """Simple program: int main() {} """
#         input = """
#         main: function void () {
#             mynameisbien : string = "longbien";
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))
#     def test203(self):
#         """Simple program: int main() {} """
#         input = """
#         main: function void () {
#             numberfloat : float;
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 203))
#     def test204(self):
#         input = """ x : integer = 65; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 204))
#     def test205(self):
#         input = """ _int : integer = 25, 35; """
#         expect = """Error on line 1 col 20: ,"""
#         self.assertTrue(TestParser.test(input, expect, 205))
    
#     def test206(self):
#         input = """ _abc, are : integer = 24, 25; """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 206))
    
#     def test207(self):
#         input = """printMyName("nameisBien");"""
#         expect = """Error on line 1 col 11: ("""
#         self.assertTrue(TestParser.test(input, expect, 207))
    
#     def test208(self):
#         input = """ checkMyNumberisPrime(x); """
#         expect = """Error on line 1 col 21: ("""
#         self.assertTrue(TestParser.test(input, expect, 208))
    
#     def test209(self):
#         input = """ isPrime : boolean = checkMyNumberisPrime(x); """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 209))
    
#     def test210(self):
#         input = """myName = "Bien"; """
#         expect = """Error on line 1 col 7: ="""
#         self.assertTrue(TestParser.test(input, expect, 210))
    
#     def test211(self):
#         input = """a[2] = "Bien";"""
#         expect = """Error on line 1 col 1: ["""
#         self.assertTrue(TestParser.test(input, expect, 211))
    
#     def test212(self):
#         input = """ listStudent : array [10] of string; """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 212))
    
#     def test213(self):
#         input = """ 
#         if (i == 2) {
#             printIsPrime(true);
#         } 
#         else {
#             printIsPrime(false);
#         }
#         """
#         expect = """Error on line 2 col 8: if"""
#         self.assertTrue(TestParser.test(input, expect, 213))
    
#     def test_214(self):
#         input = """
#         myVar : integer = 25;
#         index : integer;
#         if (myVar > 20) {
#             for (index = 1, index < 10, i + 1) {
#                 myVar = myVar + 1;
#                 if (myVar == 20){
#                     break;
#                 }
#             }
#         }
#         printIsTwenty(true);
#         """
#         expect = """Error on line 4 col 8: if"""
#         self.assertTrue(TestParser.test(input, expect, 214))
    
#     def test215(self):
#         input = """
#         while (true) {
#             printValue("I miss u");
#         }
#         """
#         expect = """Error on line 2 col 8: while"""
#         self.assertTrue(TestParser.test(input, expect, 215))
    
#     def test216(self):
#         input = """
#         do {
#             if (n % 2) return true;
#         }
#         while(isPrime(number));
#         """
#         expect = """Error on line 2 col 8: do"""
#         self.assertTrue(TestParser.test(input, expect, 216))
    
#     def test217(self):
#         input = """listPrime : array [10] of integer = {2,3,5,7,11,13,17,23};"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 217))

#     def test218(self):
#         input = """ listNumber : array [2,3] of integer = {{1,2,3}, {4,5,6}, {7,8,9}};"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 218))

#     def test219(self):
#         input = """a : integer = a < b < c;"""
#         expect = """Error on line 1 col 20: <"""
#         self.assertTrue(TestParser.test(input, expect, 219))

#     def test220(self):
#         input = """ a : float = 1_2345_569_"""
#         expect = """Error on line 1 col 23: _"""
#         self.assertTrue(TestParser.test(input, expect, 220))
    
#     def test221(self):
#         input = """a : integer = (a < b) < c;"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 221))
    
#     def test222(self):
#         input = """ for (i = 2, i < 5 , i - 1){
#                 a = 1234_34.2E-10 + {1,2,3,4};
#             } """
#         expect = """Error on line 1 col 1: for"""
#         self.assertTrue(TestParser.test(input, expect, 222))
    
#     def test223(self):
#         input = """ do {
#                 abc =  ! 12344 * 2345 / 2345 % 4567 - abc;
#                 for (abc = 0, abc < 100000, abc*12){
#                     do {
#                         abc = abc1234;
#                     } while(abc < 100000);
#                 }
#             } while(1); """
#         expect = """Error on line 1 col 1: do"""
#         self.assertTrue(TestParser.test(input, expect, 223))

#     def test224(self):
#         input = """
#         main : function void () {
#         do {
#                 abc =  12344 * 2345 / 2345 % 4567 ! abc;
#                 for (abc = 0, abc < 100000, abc*12){
#                     do {
#                         abc = abc1234;
#                     } while(abc < 100000);
#                 }
#             } while(1); 
#         }
#         """
        
#         expect = """Error on line 4 col 50: !"""
#         self.assertTrue(TestParser.test(input, expect, 224))
    
#     def test225(self):
#         input = """ 
#         main : function void () {
#             myStr = 123455E-102 + { {1,2}, {2,3,4}, {5,6,7}};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 225))
#     def test226(self):
#         input = """
#         main : function void () {
#             if (! a % 3) abc = 2;
#             else abc = 3;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 226))
#     def test227(self):
#         input = """
#         main : function void () {
#             areuready = "abcb2" + 12345 + {1,2,3} + foo(2,3,4) + _;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 227))
    
#     def test228(self):
#         input = """
#         recurPlus : function void (n : integer, a: float ) {
#             if ((n == 1) || (a == 5.)) return;
#             else return recurPlus(n + 1, a + 2);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 228))
    
#     def test229(self):
#         input = """
        
#         recurPlus : function void (n : integer, a: float ) {
#             if (n == 1 || a == 5.) return;
#             else return recurPlus(n + 1, a + 2);
#         }
        
        
#         main : function void () {
#             recurPlus(2,4.);
#         }
        
#         """
#         expect = """Error on line 4 col 28: =="""
#         self.assertTrue(TestParser.test(input, expect, 229))

#     def test230(self):
#         input = """
#         x : integer = 65;
#         fact : function integer (n : integer){
#             if (n == 0) return 1;
#             else return n * fact (n - 1);
#         }
#         inc : function void (out n : integer, delta : integer){
#             n = n + delta;
#         }
#         main : function void (){
#             delta: integer = fact(3);
#             inc(x, delta);
#             printInteger(x);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 230))

#     def test231(self):
#         input = """
#         funcAboutArray : function array [2] of integer (a: integer, del: float){
#             for (i = 2, i < 10, i + 2) while(1){
#                 b = {1,2,4,"abc"};
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 231))

#     def test232(self):
#         input =""" string : string;"""
#         expect = """Error on line 1 col 1: string"""
#         self.assertTrue(TestParser.test(input, expect, 232))
    
#     def test233(self):
#         input = """
#         func : function void (n : void);
#         """
#         expect = """Error on line 2 col 34: void"""
#         self.assertTrue(TestParser.test(input, expect, 233))
    
#     def test234(self):
#         input = """
#         main : function void (){
#             str = "alalalalalalalalal@2";
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 234))
    
#     def test235(self):
#         input = """
#         main : function void (){
#             str = {1234.E12, 124.E23};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 235))
    
#     def test236(self):
#         input = """
#         myf : function void (abc: void){
#             return;
#         }
#         """
#         expect = """Error on line 2 col 34: void"""
#         self.assertTrue(TestParser.test(input, expect, 236))
    
#     def test237(self):
#         input = """
#         main : function void (){

#             readInteger();
#             printInteger(anArg);
#             readFloat();
#             writeFloat(anAr);
#             readBoolean();
#             printBoolean(anArg);
#             readString() ;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 237))
    
#     def test238(self):
#         input = """
#         main : function void (){
#             printBoolean(anArg: boolean);
#         }
#         """
#         expect = """Error on line 3 col 30: :"""
#         self.assertTrue(TestParser.test(input, expect, 238))
    
#     def test239(self):
#         input = """ 
#         main : function void (){
#             a : array [2] of boolean = {true, false};
#             print(a[2]);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 239))
    
#     def test240(self):
#         input = """
#         a, b , c: integer = 2;
#         """
#         expect = """Error on line 2 col 29: ;"""
#         self.assertTrue(TestParser.test(input, expect, 240))
    
#     def test241(self):
#         input = """
#         a,c : integer = 1,2,4;
#         """
#         expect = """Error on line 2 col 27: ,"""
#         self.assertTrue(TestParser.test(input, expect, 241))
    
#     def test242(self):
#         input = """
#         mynameis : string boolean = 2;
#         """
#         expect = """Error on line 2 col 26: boolean"""
#         self.assertTrue(TestParser.test(input, expect, 242))
    
#     def test243(self):
#         input = """
#         myfunc : function void (n : boolean){
#             myfunc(2);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 243))
    
#     def test244(self):
#         input = """
#         myfunc : function void (n : boolean){
#             mystr = "i can't see u ";
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 244))
    
#     def test245(self):
#         input = """
#         arr : array [2] of integer = {"hihi", "hahaa", 23 - 123, !4};
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 245))
        
#     def test246(self):
#         input = """ 
#         myfunc : function void (n : boolean){
#         mysrt = "i want to sleep"; 
#         while (1){
#             printS(mystr);
#         }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 246))
#     def test247(self):
#         input = """
#         myfunc : function void (n : boolean){
#             ysrt = "i want to sleep"; 
#             while (1){
#                 printS(!mystr);
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 247))
#     def test248(self):
#         input = """
#         myfunc : function void (n : boolean){
#             int : integer = 2.3;
#             fl : float = 2;
#             print(fl == int);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 248))
#     def test249(self):
#         input = """
#         myfc : function void (n: float, m: string){
#             myfc(n,m);
#             for (int = 1, int < 32, int == 3) {
#                 while(1){
#                     do {
#                         abc = "mcd";
#                     } while(1);
#                 }
#             }
#         }
#         myfunc : function void (n : boolean){
#              myfc(2,3);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 249))
#     def test250(self):
#         input = """
#         gcd : function integer (a, b : integer){
#             return;
#         }
#         """
#         expect = """Error on line 2 col 33: ,"""
#         self.assertTrue(TestParser.test(input, expect, 250))
#     def test251(self):
#         input = """
#         gcd : function integer (a : integer, b : integer){
#             if (a > b) gcd(a-b,b);
#             if (b > a) gcd (a, b - a);
#             return a;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 251))
#     def test252(self):
#         input = """
#         do : function integer (a : string){
#             return;
#         }
#         """
#         expect = """Error on line 2 col 8: do"""
#         self.assertTrue(TestParser.test(input, expect, 252))
#     def test253(self):
#         input = """
#         main: function void (){
#             while (1) {
#                 do {
#                     while (1) do {
#                         return;
#                     } while (1);
#                 } while (1);
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 253))
#     def test254(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             abc = 2;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 254))
#     def test255(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             /*
#             abc = 2;
#             abc = 2;
#             */
#             for (abc = 2, abc  != 4, abc + 3){
#                 // abc = 4;
#                 print("abc");
#             // }
#         }
#         """
#         expect = """Error on line 12 col 8: <EOF>"""
#         self.assertTrue(TestParser.test(input, expect, 255))
#     def test256(self):
#         input = """myfunc : integer = "abc" :: "cad"; """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 256))
#     def test257(self):
#         input = """
#         void : function void (a : string){
#             return;
#         }
#         """
#         expect = """Error on line 2 col 8: void"""
#         self.assertTrue(TestParser.test(input, expect, 257))
#     def test258(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         for ( int = 1; int < 3; int ||2){
#             return;
#         }
#         }
#         """
#         expect = """Error on line 3 col 21: ;"""
#         self.assertTrue(TestParser.test(input, expect, 258))
#     def test259(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         for ( int = 1, int < 3, int ||2){
#             return;
#         }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 259))
#     def test260(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         babe = "icanuse";
#         for(int = 2, int < 2, int % 2){
#             if(babe) for (int = 3, int < 3, !int){
#                 return;
#             }
#         }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 260))
#     def test261(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         myfen = ababa;
#         a[10] = baba;
#         a[2] = {1,2,4};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 261))
#     def test262(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         myf = {fooo(1,2), alal(2,3), bebe(ana)};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 262))
#     def test263(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         for (i = 2, i < 10, i + 1){
#             if (a < b) return {a, b};
#             if (b < a) return {b, a};
#             while(1){
#             }
#         }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 263))
#     def test264(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         a = inputStr();
#         if (a == 2) return main();
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 264))
#     def test265(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         abc = 2/4;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 265))
#     def test266(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         sbc = "2/3";
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 266))
#     def test267(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             sum = 0;
#             for (i = 0, i < length(arr), i + 2){
#                 sum = sum + arr[i];
#             }
#             print(sum);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 267))
#     def test268(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         sum = 0;
#         for (i = 0, i < length(arr), i + 2){
#             sum + arr[i];
#         }
#         print(sum);
#         }
#         """
#         expect = """Error on line 5 col 16: +"""
#         self.assertTrue(TestParser.test(input, expect, 268))
#     def test269(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         abc = 2.3 * 3E2 / 3.E6;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 269))
#     def test270(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             for(int = 2, int < int, int + int){
#                 return int + int;
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 270))
#     def test271(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             abc = 2.3;
#             abc = 2.3 + abc;
#             return abc :: abc;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 271))
#     def test272(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         if (str == "abc") {
#             printIsabc(true);
#         }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 272))
#     def test273(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         abc = foo(abc) :: zya :: {1,2,43};
#         }
#         """
#         expect = """Error on line 3 col 30: ::"""
#         self.assertTrue(TestParser.test(input, expect, 273))
#     def test274(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             fooo(2) = a;
#         }
#         """
#         expect = """Error on line 3 col 20: ="""
#         self.assertTrue(TestParser.test(input, expect, 274))
#     def test275(self):
#         input = """
#         main : function void (abc : array [2] of float){
#             a[2], a[3] = foo(3,4);
#         }
#         """
#         expect = """Error on line 3 col 16: ,"""
#         self.assertTrue(TestParser.test(input, expect, 275))
#     def test276(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         abc = // \n 5;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 276))
#     def test277(self):
#         input = """
#         // abcd = 2 \n;
#         """
#         expect = """Error on line 3 col 0: ;"""
#         self.assertTrue(TestParser.test(input, expect, 277))
#     def test278(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         mystr = "queainstr\\h";
#         }
#         """
#         expect = """queainstr\h"""
#         self.assertTrue(TestParser.test(input, expect, 278))
#     def test279(self):
#         input = """
#         main : function void (abc : array [2] of float){
#         do {
#             if (a > b) return true;
#             if(a < b) return false;
#         } while(2+3+3+3+4+4/2%356)
#         }
#         """
#         expect = """Error on line 7 col 8: }"""
#         self.assertTrue(TestParser.test(input, expect, 279))
#     def test280(self):
#         input = """
#         bine : function void (int : integer){
#             readInteger();
#             readFloat();
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 280))
#     def test281(self):
#         input = """
#         bine : function void (int : integer){
#         if (a > 2) int : function void (int : integer){
#             return {1,2,3};
#         }
#         else int : function void (int : float){
#             return {1e2, 1., 2e3};
#         }
#         }
#         """
#         expect = """Error on line 3 col 23: :"""
#         self.assertTrue(TestParser.test(input, expect, 281))
#     def test282(self):
#         input = """
#         bine : function void (int : integer){
#         if (a > 2) fooo(2,4);
#         else fooo(2,4);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 282))
#     def test283(self):
#         input = """
#         bine : function void (int : integer){
#         printMystr("abcbbd\\a");
#         }
#         """
#         expect = """abcbbd\\a"""
#         self.assertTrue(TestParser.test(input, expect, 283))
#     def test284(self):
#         input = """
#         bine : function void (int : integer){
#         abc = {a[1]};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 284))
#     def test285(self):
#         input = """
#         bine : function void (int : integer){
#         a = b + v == c + d == abd;
#         }
#         """
#         expect = """Error on line 3 col 27: =="""
#         self.assertTrue(TestParser.test(input, expect, 285))
#     def test286(self):
#         input = """
#         bine : function void (int : integer){
#         a = (b + v) == (c + d == abd);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 286))
#     def test287(self):
#         input = """auto : integer = 1;"""
#         expect = """Error on line 1 col 0: auto"""
#         self.assertTrue(TestParser.test(input, expect, 287))
#     def test288(self):
#         input = """ 
#         bine : function void (int : integer){
#         cba + cba = 2;
#         }
#         """
#         expect = """Error on line 3 col 12: +"""
#         self.assertTrue(TestParser.test(input, expect, 288))
#     def test289(self):
#         input = """
#         bine : function void (int : integer){
#         whatisdonem = {{lomg}, {bine}};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 289))
#     def test290(self):
#         input = """
#         bine : function void (int : integer){
#         auto : integer = 1;
#         bala : auto = 2;
#         }
#         """
#         expect = """Error on line 3 col 8: auto"""
#         self.assertTrue(TestParser.test(input, expect, 290))
#     def test291(self):
#         input = """
        
#         mynameis : string = printMyName(yourName);
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 291))
#     def test292(self):
#         input = """
#         bine : function void (int : integer){
#         _ = 55;
#         abcb = 56;
#         a = {1,2,3, {_}};
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 292))
#     def test293(self):
#         input = """
#                 str : string = "tai sao thay doi de vao ngay deadline huhu";
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 293))
#     def test294(self):
#         input = """
#         bine : function void (int : integer){
#             aloalo(1234);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 294))
#     def test295(self):
#         input = """
#         bine : function void (int : integer){
#         print(a || b || c  + 2);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 295))
#     def test296(self):
#         input = """
#         /* 
#         a : array [2] of float;
#         */
#         """
#         expect = """Error on line 5 col 8: <EOF>"""
#         self.assertTrue(TestParser.test(input, expect, 296))
#     def test297(self):
#         input = """
#         /* 
#         a : array [2] of float;
#         */
#         bine : function void (int : integer){
#         a = 2;
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 297))
#     def test298(self):
#         input = """
        
#         main : function void (){
#             return ;
#         }
#         bine : function void (int : integer){
#         main();
#         main(1);
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 298))
#     def test299(self):
#         input = """
#         bine : function void (int : integer){
#         areuok = "i am not ok";
#         tired = "i am so tied";
#         for (tired = 2, tired < 33, tired + 2){
#             print({1,2,4});
#         }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 299))
#     def test300(self):
#         input = """
#         /* a = abc;*/
#         """
#         expect = """Error on line 3 col 8: <EOF>"""
#         self.assertTrue(TestParser.test(input, expect, 300))
    
    
# import unittest
# from TestUtils import TestParser


# class ParserSuite(unittest.TestCase):
#     def test_parser_201(self):
#         input = """main: function integer() {}"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))

#     def test_parser_202(self):
#         input = """a: integer;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))
    
#     def test_parser_203(self):
#         input = """a: integer = 1;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 203))

#     def test_parser_204(self):
#         input = """a: array[10, 2] of integer = {};"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 204))
        
#     def test_parser_205(self):
#         input = """a: array[10, 2] of integer = {1, 2};"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 205))
    
#     def test_parser_206(self):
#         input = """a: array[10, 2] of integer = {1, 2};
#                     /* This is comment */
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 206))

#     def test_parser_207(self):
#         input = """a: array[10, 2] of integer = {1, 2};
#                     /* This is comment */
#                    b: boolean = (a >= b) && c;
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 207))
    
#     def test_parser_208(self):
#         input = """a: array[10, 2] of integer = true;
#                     /* This is comment */
#                    b: boolean = true;
#                    c: string = "abc \\n";
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))
    
#     def test_parser_209(self):
#         input = """a: array[10, 2] of integer = {1, 2};
#                     /* This is comment */
#                    b: boolean = true;
#                    c: string = "abc \\n";
#                    d: string = "abc \\"";
#                    e: integer = a();
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 209))
        
#     def test_parser_210(self):
#         input = """a: array[10, 2] of integer = {1, 2};
#                     /* This is comment */
#                    b: boolean = true;
#                    c: string = "abc \\n";
#                    d: string = "abc";
#                    e: float = 1.4e10;
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 210))
    
#     def test_parser_211(self):
#         input = """ a: integer = (1 + 2) * 3;
#                     _aa: function integer() {
#                         break;
#                         return;
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 211))
    
#     def test_parser_212(self):
#         input = """ a: integer = (1 + 2) * 3;
#                     _aa: function integer(inherit a: integer) {
#                         break;
#                         return;
#                         while(a > b) {
#                             continue;
#                         }
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 212))
    
#     def test_parser_213(self):
#         input = """ a: integer = (1 + 2) * 3;
#                     _aa: function integer(inherit out a: float, b: integer) {
#                         break;
#                         return;
#                         for(a[0] = 5, a < 10, a + 1)
#                            break;
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 213))
    
#     def test_parser_214(self):
#         input = """ a: integer = (1 + 2) * 3;
#                     _aa: function integer(inherit out a: float, b: integer) inherit b {
#                         return;
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 214))
        
#     def test_parser_215(self):
#         input = """ a: void = (1 + 2) * 3;
#                     fact: function integer (n: string) {
#                         if(n == 0) return 1;
#                         else return n * fact(n - 1);
#                     }
#                 """
#         expect = "Error on line 1 col 4: void"
#         self.assertTrue(TestParser.test(input, expect, 215))
        
#     def test_parser_216(self):
#         input = """ a: boolean = (1 + 2) * 3;
#                     fact: function integer (out inherit n: string) {
#                         if(n == 0) return 1;
#                         else return n * fact(n - 1);
#                     }
#                 """
#         expect = "Error on line 2 col 48: inherit"
#         self.assertTrue(TestParser.test(input, expect, 216))
        
#     def test_parser_217(self):
#         input = """ a: boolean = (1 + 2) * 3;
#                     fact: function integer (inherit n: string) {
#                         do {
#                             a[0] = 5;
#                         }
#                         while(n <= 5);
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 217))
    
#     def test_parser_218(self):
#         input = """ a: boolean = (1 + 2) * 3;
#                     fact: function void (inherit n: string) {
#                         do {
#                             a[] = 5;
#                         }
#                         while(n <= 5);
#                     }
#                 """
#         expect = "Error on line 4 col 30: ]"
#         self.assertTrue(TestParser.test(input, expect, 218))
    
#     def test_parser_219(self):
#         input = """ a: boolean = "(1 + 2) * 3 \\" abc \\"";
#                     fact: function void (out n: string) {
#                         do {
#                             b = 3;
#                         }
#                         while(n <= 5);
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 219))
        
#     def test_parser_220(self):
#         input = """ a: boolean = "(1 + 2) * 3 \\" abc \\"";
#                     fact: function void (out n: string) {
#                         a: string = a :: b;
#                         return;
#                     }
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 220))
    
#     def test_parser_221(self):
#         input = """ a: integer = (1 + 2) * 3;
#                     fact: function integer (n: void) {
#                         if(n == 0) return 1;
#                         else return n * fact(n - 1);
#                     }
#                 """
#         expect = "Error on line 2 col 47: void"
#         self.assertTrue(TestParser.test(input, expect, 221))
        
#     def test_parser_222(self):
#         input = """ a: integer = a + b - c * 2;
#                     b: float = a % b + !c && d;
#                     c: string = a || b == (c != d);
#                     d: boolean = a < (((b <= c) > d) >= e) :: f;
#                 """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 222))
    
#     def test_parser_223(self):
#         input = """ a: array [1, 2, 3] of integer = {{1, 2, 3}, 2, 3}; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 223))
        
#     def test_parser_224(self):
#         input = """ a: array [1, 2, 3] of integer = ""; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 224))
        
#     def test_parser_225(self):
#         input = """ a: array [1, 2, 3] of integer = "";
#                     fact: function integer (n: auto) {
#                         while(a < 10)
#                     }
#         """
#         expect = "Error on line 4 col 20: }"
#         self.assertTrue(TestParser.test(input, expect, 225))
    
#     def test_parser_226(self):
#         input = """ a: array [1, 2, 3] of integer = "";
#                     fact: function integer (n: auto) {
#                         while(a)
#                             if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 226))
        
#     def test_parser_227(self):
#         input = """ a: array [1, 2, 3] of integer = "";
#                     fact: function integer (n: auto) {
#                         while(a)
#                             if(a < 10) a = a + 1
#                     }
#         """
#         expect = "Error on line 5 col 20: }"
#         self.assertTrue(TestParser.test(input, expect, 227))
        
#     def test_parser_228(self):
#         input = """ a: array [1, 2, 3] of integer = "";
#                     fact: integer (n: auto) ;
#         """
#         expect = "Error on line 2 col 36: :"
#         self.assertTrue(TestParser.test(input, expect, 228))
        
#     def test_parser_229(self):
#         input = """ a: array [1, 2, 3] of integer = "";
#                     fact: function integer (n: auto) {
#                         while(a)
#                             if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 229))
        
#     def test_parser_230(self):
#         input = """ a: array [1, 2, 3] of array [1, 2, 3] = "";
#                     fact: function integer (n: auto) {
#                         if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "Error on line 1 col 23: array"
#         self.assertTrue(TestParser.test(input, expect, 230))
        
#     def test_parser_231(self):
#         input = """ a: integer = a || b;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 231))
        
#     def test_parser_232(self):
#         input = """ a: integer = a >= b;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 232))
        
#     def test_parser_233(self):
#         input = """ a: integer = a < (b < c);"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 233))
        
#     def test_parser_234(self):
#         input = """ a: integer = a >= b;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 234))
        
#     def test_parser_235(self):
#         input = """ a: integer = a > b > c;"""
#         expect = "Error on line 1 col 20: >"
#         self.assertTrue(TestParser.test(input, expect, 235))
        
#     def test_parser_236(self):
#         input = """ a: integer = a < b;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 236))
        
#     def test_parser_237(self):
#         input = """ a: integer = a < b < c;"""
#         expect = "Error on line 1 col 20: <"
#         self.assertTrue(TestParser.test(input, expect, 237))
        
#     def test_parser_238(self):
#         input = """ a: integer = a >= b;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 238))
        
#     def test_parser_239(self):
#         input = """ a: integer = a >= b >= c;"""
#         expect = "Error on line 1 col 21: >="
#         self.assertTrue(TestParser.test(input, expect, 239))
        
#     def test_parser_240(self):
#         input = """ a: integer = a <= b;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 240))
        
#     def test_parser_241(self):
#         input = """ a: integer = a <= b <= c;"""
#         expect = "Error on line 1 col 21: <="
#         self.assertTrue(TestParser.test(input, expect, 241))
        
#     def test_parser_242(self):
#         input = """ a: integer = a <= b; 
#                     fact: function integer (n: auto) {
#                         if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 242))
        
#     def test_parser_243(self):
#         input = """ a: integer = a <= b
#                     fact: function integer (n: auto) {
#                         if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "Error on line 2 col 20: fact"
#         self.assertTrue(TestParser.test(input, expect, 243))
        
#     def test_parser_244(self):
#         input = """ a: = a <= b;
#                     fact: function integer (n: auto) {
#                         if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "Error on line 1 col 4: ="
#         self.assertTrue(TestParser.test(input, expect, 244))
        
#     def test_parser_245(self):
#         input = """ a integer = a <= b;
#                     fact: function integer (n: auto) {
#                         if(a < 10) a = a + 1;
#                     }
#         """
#         expect = "Error on line 1 col 3: integer"
#         self.assertTrue(TestParser.test(input, expect, 245))
        
#     def test_parser_246(self):
#         input = """ a: integer = a(10) + _a(); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 246))
        
#     def test_parser_247(self):
#         input = """ a: integer = true + _a(); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 247))
        
#     def test_parser_248(self):
#         input = """ a: integer = true + _a(); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 248))
        
#     def test_parser_249(self):
#         input = """ a: integer = true + 123_213; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 249))
        
#     def test_parser_250(self):
#         input = """ a: integer = 1.234 + 123_213; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 250))
        
#     def test_parser_251(self):
#         input = """ a: integer = 123_12 + 12; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 251))
        
#     def test_parser_252(self):
#         input = """ a: float = 1.23 + 1.2e-10; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 252))
        
#     def test_parser_253(self):
#         input = """ a: string = "abc" :: "bcd"; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 253))
        
#     def test_parser_254(self):
#         input = """ a: string = a[10] :: "bcd"; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 254))
        
#     def test_parser_255(self):
#         input = """ a: string = a[10] + "bcd"; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 255))
        
#     def test_parser_256(self):
#         input = """ a: string = a[10] + b[0]; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 256))
        
#     def test_parser_257(self):
#         input = """ a: string = 123_123 + "sad"; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 257))
        
#     def test_parser_258(self):
#         input = """ a: string = 123_123 + "sad" + func(2); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 258))
        
#     def test_parser_259(self):
#         input = """ a: string = a[20] + "sad" + func(2); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 259))
        
#     def test_parser_260(self):
#         input = """ a: string = func(func(5))+ func(2); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 260))
        
#     def test_parser_261(self):
#         input = """ a: string = func(func(5))+ func(func()); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 261))
        
#     def test_parser_262(self):
#         input = """ a: string = func(func(5 + 3, true)); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 262))
        
#     def test_parser_263(self):
#         input = """ a: string = func(func(5 + 3, true, 2_3223.3223e10)); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 263))
        
#     def test_parser_264(self):
#         input = """ a: string = a[a[a[0]]]; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 264))
        
#     def test_parser_265(self):
#         input = """ a: string = a[a[a[0]]]; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 265))
        
#     def test_parser_266(self):
#         input = """ a: string = a[a[a[true]]]; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 266))
    
#     def test_parser_267(self):
#         input = """ a: string = a == b + c; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 267))
        
#     def test_parser_268(self):
#         input = """ a: string = a == b + c - d; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 268))
        
#     def test_parser_269(self):
#         input = """ a: string = -5 + 10;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 269))
        
#     def test_parser_270(self):
#         input = """ a: string = 10 * 5 - (-5); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 270))
        
#     def test_parser_271(self):
#         input = """ a: string = 10 * 5 - (-5) """
#         expect = "Error on line 1 col 27: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 271))
        
#     def test_parser_272(self):
#         input = """ a: string = -10 * -5 - (-5); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 272))
        
#     def test_parser_273(self):
#         input = """ a: string = -10 * -5 - (-5) + a["123"]; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 273))
        
#     def test_parser_274(self):
#         input = """ a: string = a["123"] + fc(_aa); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 274))
        
#     def test_parser_275(self):
#         input = """ a: string = function(a["123"]); """
#         expect = "Error on line 1 col 13: function"
#         self.assertTrue(TestParser.test(input, expect, 275))
        
#     def test_parser_276(self):
#         input = """ a: boolean = fc({1, 2, 3}); """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 276))
        
#     def test_parser_277(self):
#         input = """ a: boolean = fc(fc({1, 2, 3})) + {1, 2, "a"}; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 277))
        
#     def test_parser_278(self):
#         input = """ a: boolean = fc(fc({1, 2, 3})) + abc; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 278))
        
#     def test_parser_279(self):
#         input = """ a: boolean = {{fc(fc({1, 2, 3}))}} + {1, 2, "a"}; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 279))
        
#     def test_parser_280(self):
#         input = """ a: boolean = a[fc(fc({1, 2, 3}))] + {1, 2, "a"}; """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 280))
        
#     def test_parser_281(self):
#         input = """"""
#         expect = "Error on line 1 col 0: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 281))
        
#     def test_parser_282(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         print("tuimetquaroi");
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 282))
        
#     def test_parser_283(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         print("tuimetquaroi");
#                         a[0] = "brrr";
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 283))
    
#     def test_parser_284(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         print("tuimetquaroi");
#                         br = brrr;
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 284))
        
#     def test_parser_285(self):
#         input = """ quametmoi: function string (inherit out n: string) {
#                         print("tuimetquaroi");
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 285))
        
#     def test_parser_286(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         if(a > 10 + 1 * 3 :: (!y)) cout(getout);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 286))
        
#     def test_parser_287(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         for(a = 5, 5 > 3, a > 5)
#                             writeInt();
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 287))
        
#     def test_parser_288(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         while(a > 10 + 1 * 3 :: (!y)) 
#                             cout(getout);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 288))
        
#     def test_parser_289(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         do {
#                             cout(brrrr);
#                         }
#                         while(a > 10);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 289))
        
#     def test_parser_290(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                         }
#                         while(a > 10);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 290))
        
#     def test_parser_291(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         do {
#                             continue;
#                         }
#                         while(a > 10);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 291))
    
#     def test_parser_292(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                             {
#                                 break;
#                             }
#                         }
#                         while(a > 10);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 292))
        
#     def test_parser_293(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                             continue;
#                             for(i = 5, i < 10, i + 1) {
#                                 continue;
#                             }
#                         }
#                         while(a > 10);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 293))
        
#     def test_parser_294(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         return 5;
#                         while(a > 10)
#                             break;
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 294))
        
#     def test_parser_295(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         quametmoi(n + 100);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 295))
        
#     def test_parser_296(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         for(i = 5; i < 10, i + 1) {
#                             continue;
#                         }
#                     }
#         """
#         expect = "Error on line 2 col 33: ;"
#         self.assertTrue(TestParser.test(input, expect, 296))
        
#     def test_parser_297(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         for(i = 5, i < 10, i++) {
#                             continue;
#                         }
#                     }
#         """
#         expect = "Error on line 2 col 45: +"
#         self.assertTrue(TestParser.test(input, expect, 297))
        
#     def test_parser_298(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         for(, i < 10, i + 1) {
#                             continue;
#                         }
#                     }
#         """
#         expect = "Error on line 2 col 28: ,"
#         self.assertTrue(TestParser.test(input, expect, 298))
        
#     def test_parser_299(self):
#         input = """ quametmoi: function string (inherit n: string) {
#                         for(,,,) {
#                             continue;
#                         }
#                     }
#         """
#         expect = "Error on line 2 col 28: ,"
#         self.assertTrue(TestParser.test(input, expect, 299))
        
#     def test_parser_300(self):
#         input = """ a: string = "Chuc mung ban da pass BTL1";
#                     quametmoi: function string (inherit n: string) {
#                         ketthuccuoochoi(123);
#                     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 300))

import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """
            x : integer = 6_5;
        fact : function integer (n : integer) {
            if (n == 0) 
                while (n > 0) {}
            else return n * fact (n - 1);
        }
        inc : function void (out n : integer, delta: integer) {
            n = n + delta ;
        }
        main : function void () {
            delta: integer = fact(3);
            inc(x, delta) ;
            printInteger( x ) ;
        }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = """x,y: array [2+2,3] of auto;
                """
        expect = "Error on line 1 col 13: +"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """x: integer = 1, 2;
                """
        expect = "Error on line 1 col 14: ,"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """x: void;
                """
        expect = "Error on line 1 col 3: void"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """x,y: float = 2*3.0;
                """
        expect = "Error on line 1 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = """
                foo: function integer () inherit foo1 {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = """
                foo: function float (inherit out n: integer, out b: auto, temp: string) {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = """
                foo: function void (inherit out n: integer, out b: auto, temp: string) {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = """
                foo: function array [2,3] of string (n: integer, str: string) {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = """
                foo: function array [2,3] of string (inherit out arr: array[3,4,5] of string) {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        input = """
                main: function void () {
                    x: integer = 0;
                    x = (x + 1) * 3.0 + foo() / 23;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        input = """
                main: function void () {
                    x: array[] of integer;
                }
                """
        expect = "Error on line 3 col 29: ]"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        input = """
                main: function void () {
                    x: array[3] of integer = {};
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        input = """
                main: function void () {
                    x: array[1+t] of integer = {};
                }
                """
        expect = "Error on line 3 col 30: +"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_214(self):
        input = """
                main: function void () {
                    x: array[34] of integer = {1, 1+2, 3+foo()};
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        input = """
                main: function void () {
                    x: array[3,4,5] of integer = {{12,2},{23,34}};
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_215(self):
        input = """
                arr: array[2,3] of integer;
                main: function void () {
                    x: integer = arr[1,2] + 23 * foo();
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        input = """
                arr: array[2,3] of integer;
                main: function void () {
                    x: integer = arr[1,2] + 23 * foo();
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = """
                main: function void () {
                    x: integer;
                    x = 1 + -foo() * arr[1,2];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = """
                main: function void () {
                    x: boolean;
                    x = true && false || true ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = """
                main: function void () {
                    x: boolean;
                    x = (a < b) && (c >= d);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        input = """
                main: function void () {
                    x: integer;
                    x = -!foo();
                }
                """
        expect = "Error on line 4 col 25: !"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = """
                main: function void () {
                    x: integer;
                    x = foo()[2,3];
                }
                """
        expect = "Error on line 4 col 29: ["
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = """
                main: function void () {
                    x: integer;
                    x = !arr[2,3];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = """
                main: function void () {
                    x: integer;
                    x = readInteger() + 23;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = """
                main: function void () {
                    x: boolean;
                    x = -(readInteger() + 23) == foo();
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = """
                main: function void () {
                    // x: boolean;
                    x[1,2] = "hihi"::12::"23";
                }
                """
        expect = "Error on line 4 col 39: ::"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = """
                x: integer = 1;
                main: function void () {
                    if (x < 0) x = -x;
                    else x = x * 2 + 3;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = """
                main: function void () {
                    if (x < 10) res = 2.0*x;
                    else if (x < 100) res = 2.5*x + 35;
                    else res = x * 5.5 + 3;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """
                main: function void () {
                    if (x >= 10) {
                        x = x + 10;
                        {}
                    } 
                    else {
                        x = x - 10;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))   

    def test_229(self):
        input = """
                main: function void () {
                    if (!(foo() && foo1())) x = x * 2;
                    else {
                        x = x - 10;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))   

    def test_230(self):
        input = """
                main: function void () {
                    if (!a[1]) {
                        x = x / 2;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230)) 

    def test_231(self):
        input = """
                main: function void () {
                    for (i = 1, i < 100, 1) 
                        x = x + 1;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231)) 

    def test_232(self):
        input = """
                main: function void () {
                    for (i = foo(), !i, -1) 
                        x = x + i;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232)) 

    def test_233(self):
        input = """
                main: function void () {
                    for (i = foo(), , -i) 
                        x += i;
                }
                """
        expect = "Error on line 3 col 36: ,"
        self.assertTrue(TestParser.test(input, expect, 233)) 

    def test_234(self):
        input = """
                main: function void () {
                    for (i = foo(), !i, -i) 
                }
                """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = """
                main: function void () {
                    for (i = foo(); !i; -i) 
                        x += i;
                }
                """
        expect = "Error on line 3 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """
                main: function void () {
                    while (x >= 10)
                        x = x + 1;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """
                main: function void () {
                    while (x >= 10) ;
                }
                """
        expect = "Error on line 3 col 36: ;"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """
                main: function void () {
                    while (x + 1 > y * 2) {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """
                main: function void () {
                    while () {}
                }
                """
        expect = "Error on line 3 col 27: )"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """
                main: function void () {
                    while (!a) ;
                }
                """
        expect = "Error on line 3 col 31: ;"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """
                main: function void () {
                    do
                        {}
                    while (x < 100) ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """
                main: function void () {
                    do
                        {}
                    while (x < 100) 
                }
                """
        expect = "Error on line 6 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """
                main: function void () {
                    do
                        {}
                    while (x < 100;) ;
                }
                """
        expect = "Error on line 5 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """
                main: function void () {
                    do {
                        x = x + 1;
                    }
                    while (x < 100) ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """
                main: function void () {
                    do
                    {}
                    while (true) ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """
                main: function void () {
                    break;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """
                main: function void () {
                    for (i = 1, i < 10, 1) {
                        break;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """
                main: function void () {
                    while (true) break;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """
                main: function void () {
                    do
                        {
                            break;
                        }
                    while (true) ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """
                main: function void () {
                    break
                }
                """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = """
                main: function void () {
                    continue;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = """
                main: function void () {
                    for (i = 1, i < 10, 1) {
                        continue;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = """
                main: function void () {
                    while (true) continue;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = """
                main: function void () {
                    do
                        {
                            continue;
                        }
                    while (true) ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = """
                main: function void () {
                    continue
                }
                """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = """
                main: function void () {
                    return;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = """
                main: function void () {
                    return 1 + x * 3 - 2;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = """
                main: function void () {
                    return
                }
                """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = """
                main: function void () {
                    main();
                    foo({1,2,3,4}, "s"::"tring");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = """
                main: function void () {
                    -foo();
                }
                """
        expect = "Error on line 3 col 20: -"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = """
                main: function void () {
                    {{{}}}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = """
                main: function void () {
                    {
                        a, b: integer;
                        if (a == b) return;
                        for (i = a, i != b, 1) a = a + 1;
                    }
                    return ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """
                main: function void () {
                    x = readInteger() + 1;
                    printInteger(x, y);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """
                main: function void () {
                    x = readFloat() + 1;
                    printFloat(x);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """
                main: function void () {
                    x = readString()::"12";
                    printString(x);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """
                fact: function integer (n: integer) {
                    if (n <= 1) return 1;
                    else return n * fact(n-1);
                }
                main: function void () {
                    x: integer = fact(34);
                    printInteger(x);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """
                fact: function integer (n: integer) {
                    if (n <= 1) return 1;
                    i, res: integer = 0, 1;
                    for (i = 2, i <= 2, 1) {
                        res = res * i;
                    }    
                    return res;
                }
                main: function void () {
                    printInteger(fact(2*3));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """
                arr: array[10] of float = {0,1,2,3,4,5,6,7,8,9};
                recSumArr: function float (arr: array [10] of float, idx: integer) {
                    if (idx == 9) return arr[9];
                    else return arr[idx] + recSumArr(arr, idx+1);
                }
                sumArr: function float (arr: array [10] of float) {
                    return recSumArr(arr, 0);
                }
                main: function void () {
                    printFloat(sumArr(arr));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """
                arr: array[10] of float = {0,1,2,3,4,5,6,7,8,9};
                sumArr: function float (arr: array [10] of float) {
                    res: float = 0;
                    i: integer = 0;
                    while (i < 10) {
                        res = res + arr[i];
                        i = i + 1;
                    }
                }
                main: function void () {
                    printFloat(sumArr(arr));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """
                gcdRec: function integer (n: integer, m: integer) {
                    if (m == 0) return n;
                    return gcdRec(m, n % m);
                }
                main: function void () {
                    printInteger(gcdRec(340, 23));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """
                gcd: function integer (n: integer, m: integer) {
                    while (m != 0) {
                        n = n % m;
                        tmp: integer = n;
                        n = m;
                        m = tmp;
                    }
                    return n;
                }
                main: function void () {
                    printInteger(gcd(340, 23));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """
                printRec: function void (n: integer) {
                    if (n < 0) printInteger(n);
                    else {
                        printInteger(n);
                        printRec(n-5);
                        printInteger(n);
                    }
                }
                main: function void () {
                    printRec();
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """
                checkUniq: function boolean (arr: array [1000] of integer) {
                    i, j: integer;
                    for (i = 0, i < 999, 1) {
                        for (j = i + 1, j < 1000, 1) {
                            if (arr[i] == arr[j]) return false;
                        }
                    }
                    return true;
                }
                main: function void () {
                    checkUniq({1,2,3,4,5,6,6,7,8,8,8});
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """
                sort: function void (arr: array [10] of integer) {
                    i, j: integer;
                    flag: boolean;
                    for (i = 0, i < 9, 1) {
                        flag = false;
                        for (j = i, j < 9, 1) {
                            if (arr[j] > arr[j+1]) {
                                tmp: integer = arr[j];
                                arr[j] = arr[j+1];
                                arr[j+1] = tmp;
                                flag = true; 
                            }
                        }
                        if (!flag) break;
                    }
                    return ;
                }
                main: function void () {
                    arr: array [10] of integer = {1,2,4,3,5,7,6,8,9,10};
                    sort(arr);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """
                sumOfGtNum: function integer(arr: array [10] of integer, n: integer) {
                    i, res: integer = 0, 0;
                    for (i = 0, i < 10, 1) {
                        if (arr[i] <= n) continue;
                        res = res + arr[i];
                    }
                }
                main: function void () {
                    arr: array [10] of integer = {1,2,4,3,5,7,6,8,9,10};
                    sort(arr);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """
                checkPrime: function boolean (n: integer) {
                    if (n < 2) return false;
                    i: integer;
                    for (i = 2, i < n , 1) {
                        if (n % i == 0) return false;
                    }
                    return true;
                }
                main: function void () {
                    checkPrime(123);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """
                checkPrime: function boolean (n: integer) {
                    if (n < 2) return false;
                    i: integer;
                    for (i = 2, i < n / 2 , 1) {
                        if (n % i == 0) return false;
                    }
                    return true;
                }
                main: function void () {
                    checkPrime(123);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """
                main: function void () {
                    x: integer = readInteger();
                    res: integer = 0;
                    for (x = x, x > 0, -1) {
                        res = res + x;
                    }
                    printInteger(res);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = """
                main: function void () {
                    x, res: float = readFloat(), 0.;
                    if (x < 10) res = x*10;
                    else if (x < 100) res = x*11;
                    else res = x*100 + 12;
                    printFloat(res);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = """
                main: function void () {
                    if (x < 10) 
                        if (x < 5) x = x + 5;
                    else x = x + 10;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = """
                addDigits: function integer (num: integer) {
                    if (num < 10) return num;
                    res: integer = 0;
                    while (num != 0) {
                        res = res + num % 10;
                        num = num / 10;
                    }
                    return addDigits(res);
                }
                main: function void () {
                    printInteger(addDigits(12));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = """
                pow: function integer (num: integer, exp: integer) {
                    if (exp == 0) return 1;
                    tmp: integer = pow(num, exp/2);
                    if (exp % 2 == 1) return tmp*tmp*num;
                    else return tmp*tmp;
                }
                main: function void () {
                    printInteger(pow(12,2));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """
                concatNString: function string (arr: array [1000000] of string, n: integer) {
                    i: integer;
                    res: string = "";
                    for (i = 0, i < n, 1) {
                        res = res :: arr[i];
                    }
                    return res;
                }
                main: function void () {
                    arr: array [5] of string = {"Hello ", "World, ", "Coding ", "With ", "MT22 Language!"};
                    printString(concatNString(arr, 5));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """
                out: integer = 1;
                """
        expect = "Error on line 2 col 16: out"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """
                readInteger: integer = 1;
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = """
                countPrime: function integer (n: integer) {
                    if (n < 3) return 0;
                    prime: array [1000000] of boolean;
                    for (i = 2, i < 999999, 1) prime[i] = true;
                    res: integer = 0;
                    for (i = 2, i < n, 1) {
                        if (prime[i]) {
                            res = res + 1;
                            j: integer = i * 2;
                            while (j < n) {
                                prime[j] = false;
                                j = j + i;
                            }
                        }
                    }
                    return res;
                }
                main: function void () {
                    printInteger(countPrime(100));
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """
                
                """
        expect = "Error on line 3 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = """
                main: function void () {
                    x = !foo() && !arr[10*x] || arr[10.];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = """
                linearSearch: function integer (arr: array [1000000] of integer, size: integer, val: integer) {
                    i: integer;
                    for (i = 0, i < size, 1) {
                        if (arr[i] == val) return i;
                    }
                    return -1;
                }
                arr: array [5] of integer = {4,2,6,100,34};
                main: function void () {
                    linearSearch(arr, 5, 100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """
                binarySearch: function integer (arr: array [1000000] of integer, size: integer, val: integer) {
                    l, r: integer = 0, size;
                    while (l <= r) {
                        mid: integer = (l + r) / 2;
                        if (arr[mid] == val) return mid;
                        else if (arr[mid] < val) l = mid + 1;
                        else r = mid - 1;
                    }
                    return -1;
                }
                arr: array [5] of integer = {4,2,6,100,34};
                main: function void () {
                    binarySearch(arr, 5, 100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """
                binarySearch: function integer (arr: array [1000000] of integer, l: integer, r: integer, val: integer) {
                    if (l > r) return -1;
                    mid: integer = (l + r) / 2;
                    if (arr[mid] == val) return mid;
                    else if (arr[mid] < val) binarySearch(arr, mid+1, r, 100);
                    else binarySearch(arr, l, mid-1, 100);
                }
                arr: array [5] of integer = {4,2,6,100,34};
                main: function void () {
                    binarySearch(arr, 0, 4, 100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """
                main: function void () {
                    for (i = 0, !i, 1) {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """
                sumTo: function integer (n: integer) {
                    if (n == 0) return 0;
                    else return n + sumTo(n-1);
                }
                main: function void () {
                    sumTo(100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """
                sumTo: function integer (n: integer) {
                    res: integer = 0;
                    for (n = n, n > 0, -1) res = res + n;
                }
                main: function void () {
                    sumTo(100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """
                fibo: function integer (n: integer) {
                    if (n < 2) return 1;
                    else return fibo(n-1) + fibo(n-2);
                }
                main: function void () {
                    fibo(100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """
                fibo: function integer (n: integer) {
                    if (n < 2) return 1;
                    f1, f2: integer = 1, 1;
                    for (i = 2, i <= n, 1) {
                        f1 = f2 + f2 + f1;
                        f2 = f1 - f2;
                        f1 = f1 - f2;
                    }
                    return f2;
                }
                main: function void () {
                    fibo(100);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """
                main: function void () {
                    x = "Hello \\a ";
                }
                """
        expect = "Hello \\a"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """
                main: function void () {
                    x = ..e34;
                }
                """
        expect = "Error on line 3 col 24: ."
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """
                main: function void () {
                    x = "Hello" ;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    # def test_300(self):
    #     input = """
    #             main: function void () {
    #                 while (x) {
    #                     if (x) 
    #                     do
    #                         x();
    #                     while (x);
    #                 }
    #             }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 300))
