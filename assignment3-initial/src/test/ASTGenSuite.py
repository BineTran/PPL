import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """
                main : function integer()
                {
                   if (5 > 3){
                           
                   }
                   else {
                           
                   }
                }
                """
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

#     def test_full_vardecl(self):
#         input = """func: function integer() {
#             for (a[true] = 1, a < b, a + 1){
#                 if (x<5) 
#                     if (y>4){
#                         y = y-1;
#                     } else while (z>3) if (r>4) {
#                         r = 1 + r;
#                     }
#                 else return y; 
#             } 
#             a: integer = 5;
#         } """
#         expect = """Program([
# 	FuncDecl(func, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [BooleanLit(True)]), IntegerLit(1)), BinExpr(<, Id(a), Id(b)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(x), IntegerLit(5)), IfStmt(BinExpr(>, Id(y), IntegerLit(4)), BlockStmt([AssignStmt(Id(y), BinExpr(-, Id(y), IntegerLit(1)))]), WhileStmt(BinExpr(>, Id(z), IntegerLit(3)), IfStmt(BinExpr(>, Id(r), IntegerLit(4)), BlockStmt([AssignStmt(Id(r), BinExpr(+, IntegerLit(1), Id(r)))])))), ReturnStmt(Id(y)))])), VarDecl(a, IntegerType, IntegerLit(5))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_vardecls(self):
#         input = """x, y, z: integer = 1, 2, .E12;
#         a, b: float;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, FloatLit(0.0))
# 	VarDecl(a, FloatType)
# 	VarDecl(b, FloatType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 302))

#     def test_simple_program(self):
#         """Simple program"""
#         input = """
#                 main: function integer () {
#                     }
#                 a: integer = 1;
#                 b: auto = a + 1;
#                 c: auto = a + main();
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))

#     def test305(self):
#         """More complex program"""
#         input = """main: function integer() {}"""
#         expect = """Program([
# 	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))
    
#     def test306(self):
#         """More complex program"""
#         input = """a: integer;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 306))
        
#     def test307(self):
#         """More complex program"""
#         input = """a: integer = 2E31;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, FloatLit(2e+31))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 307))
        
#     def test308(self):
#         """More complex program"""
#         input = """a: array[10, 2] of integer = b[2,3];"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 308))
        
#     def test309(self):
#         """More complex program"""
#         input = """a: array[10, 2] of integer = {1, 2};
#                     /* This is comment */
#                    b: boolean = (a >= b) && c;"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
# 	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(>=, Id(a), Id(b)), Id(c)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 309))
    
# #     def test310(self):
# #         """More complex program"""
# #         input = """a: array[10, 2] of integer = {1, 2};
# #                     /* This is comment */
# #                    b: boolean = true;
# #                    c: string = "abc \\n";
# #                    d: string = "abc";
# #                    e: float = 1.4e10;"""
# #         expect = """Program([
# # 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
# # 	VarDecl(b, BooleanType, BooleanLit(True))
# # 	VarDecl(c, StringType, StringLit(abc \n))
# # 	VarDecl(d, StringType, StringLit(abc))
# # 	VarDecl(e, FloatType, FloatLit(14000000000.0))
# # ])"""
# #         self.assertTrue(TestAST.test(input, expect, 310))

#     def test310(self):
#         """More complex program"""
#         input = """a: array[10, 2] of integer = {1, 2};
#                     /* This is comment */
#                    b: boolean = true;
#                    c: string = 1;
#                    d: string = 2;
#                    e: float = 1.4e10;"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
# 	VarDecl(b, BooleanType, BooleanLit(True))
# 	VarDecl(c, StringType, IntegerLit(1))
# 	VarDecl(d, StringType, IntegerLit(2))
# 	VarDecl(e, FloatType, FloatLit(14000000000.0))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 310))

#     def test311(self):
#         """More complex program"""
#         input = """a: integer = (1 + 2) * 3;
#                     _aa: function integer() {
#                         break;
#                         return;
#                     };"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
# 	FuncDecl(_aa, IntegerType, [], None, BlockStmt([BreakStmt(), ReturnStmt()]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 311))

#     def test312(self):
#         """More complex program"""
#         input = """a: integer = (1 + 2) * 3;
#                     _aa: function integer(inherit a: integer) {
#                         break;
#                         return;
#                         while(a > b) {
#                             continue;
#                         }
#                     }"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
# 	FuncDecl(_aa, IntegerType, [InheritParam(a, IntegerType)], None, BlockStmt([BreakStmt(), ReturnStmt(), WhileStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([ContinueStmt()]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 312))
    
#     def test313(self):
#         """More complex program"""
#         input = """a: integer = (1 + 2) * 3;
#                     _aa: function integer(inherit out a: float, b: integer) {
#                         break;
#                         return;
#                         for(a[0] = 5, a < 10, a + 1)
#                            break;
#                     }"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
# 	FuncDecl(_aa, IntegerType, [InheritOutParam(a, FloatType), Param(b, IntegerType)], None, BlockStmt([BreakStmt(), ReturnStmt(), ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(5)), BinExpr(<, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BreakStmt())]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 313))
        
# #     def test314(self):
# #         """More complex program"""
# #         input = """a: integer = (1 + 2) * 3;
# #                     _aa: function integer(inherit out a: float, b: integer) inherit b {
# #                         return;
# #                     }"""
# #         expect = """Program([
# # 	VarDecl(a, IntegerType, BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
# # 	FuncDecl(_aa, IntegerType, [InheritOutParam(a, FloatType), Param(b, IntegerType)], b, BlockStmt([ReturnStmt()]))
# # ])"""
#         # self.assertTrue(TestAST.test(input, expect, 314))
        
#     def test_full_vardecl_expr_5(self):
#         input = """x: string = ("thanh" :: "vip") :: "max";"""
#         expect = str(Program([
#             VarDecl('x', StringType(), BinExpr('::', BinExpr('::', StringLit('thanh'), StringLit('vip')), StringLit('max')))
#         ]))
#         self.assertTrue(TestAST.test(input, expect, 314))
    
#     def test315(self):
#         """More complex program"""
#         input = """a: integer = (1 + 2) * 3;
#                     fact: function integer (n: string) {
#                         if(n == 0) return 1;
#                         else return n * fact(n - 1);
#                     }"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
# 	FuncDecl(fact, IntegerType, [Param(n, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 315))
    
#     def test316(self):
#         """More complex program"""
#         input = """a: boolean = (1 + 2) * 3;
#                     fact: function integer (inherit n: string) {
#                         do {
#                             a[0] = 5;
#                         }
#                         while(n <= 5);
#                     }"""
#         expect = """Program([
# 	VarDecl(a, BooleanType, BinExpr(*, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
# 	FuncDecl(fact, IntegerType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(<=, Id(n), IntegerLit(5)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(5))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 316))
        
#     def test317(self):
#         """More complex program"""
#         input = """a: integer = a + b - c * 2;
#                     b: float = a % b + !c && d;
#                     c: string = a || b == (c != d);
#                     d: boolean = a < (((b <= c) > d) >= e) :: f;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, Id(a), Id(b)), BinExpr(*, Id(c), IntegerLit(2))))
# 	VarDecl(b, FloatType, BinExpr(&&, BinExpr(+, BinExpr(%, Id(a), Id(b)), UnExpr(!, Id(c))), Id(d)))
# 	VarDecl(c, StringType, BinExpr(==, BinExpr(||, Id(a), Id(b)), BinExpr(!=, Id(c), Id(d))))
# 	VarDecl(d, BooleanType, BinExpr(::, BinExpr(<, Id(a), BinExpr(>=, BinExpr(>, BinExpr(<=, Id(b), Id(c)), Id(d)), Id(e))), Id(f)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 317))
        
#     def test318(self):
#         """More complex program"""
#         input = """a: array [1, 2, 3] of integer = ""; """
#         expect = """Program([
# 	VarDecl(a, ArrayType([1, 2, 3], IntegerType), StringLit())
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 318))
    
#     def test319(self):
#         """More complex program"""
#         input = """a: array [1, 2, 3] of integer = "";
#                     fact: function integer (n: auto) {
#                         while(a < 10) {}
#                     }"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([1, 2, 3], IntegerType), StringLit())
# 	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 319))
    
#     def test320(self):
#         """More complex program"""
#         input = """a: array [1, 2, 3] of integer = "";
#                     fact: function integer (n: auto) {
#                         while(a)
#                             if(a < 10) a = a + 1;
#                     }"""
#         expect = """Program([
# 	VarDecl(a, ArrayType([1, 2, 3], IntegerType), StringLit())
# 	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([WhileStmt(Id(a), IfStmt(BinExpr(<, Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 320))
    
#     def test321(self):
#         """More complex program"""
#         input = """a: integer = a || b;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(||, Id(a), Id(b)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 321))
    
#     def test322(self):
#         """More complex program"""
#         input = """a: integer = a >= b;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(>=, Id(a), Id(b)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 322))

#     def test323(self):
#         """More complex program"""
#         input = """a: integer = a >= b;"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(>=, Id(a), Id(b)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 323))
    
#     def test324(self):
#         """More complex program"""
#         input = """a: integer = a <= b; 
#                     fact: function integer (n: auto) {
#                         if(a < 10) a = a + 1;
#                     }"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(<=, Id(a), Id(b)))
# 	FuncDecl(fact, IntegerType, [Param(n, AutoType)], None, BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 324))

#     def test325(self):
#         """More complex program"""
#         input = """ a: integer = a(10) + _a(); """
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(+, FuncCall(a, [IntegerLit(10)]), FuncCall(_a, [])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 325))
    
#     def test326(self):
#         """More complex program"""
#         input = """ a: integer = true + 123_213; """
#         expect = """Program([
# 	VarDecl(a, IntegerType, BinExpr(+, BooleanLit(True), IntegerLit(123213)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 326))
    
#     def test327(self):
#         """More complex program"""
#         input = """ a: float = 1.23 + 1.2e-10; """
#         expect = """Program([
# 	VarDecl(a, FloatType, BinExpr(+, FloatLit(1.23), FloatLit(1.2e-10)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 327))
    
#     def test328(self):
#         """More complex program"""
#         input = """ a: string = a[10] :: "bcd"; """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(::, ArrayCell(a, [IntegerLit(10)]), StringLit(bcd)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 328))
    
#     def test329(self):
#         """More complex program"""
#         input = """ a: string = a[10] + "bcd"; """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, ArrayCell(a, [IntegerLit(10)]), StringLit(bcd)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 329))
        
#     def test330(self):
#         """More complex program"""
#         input = """a: string = a[10] + b[0]; """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, ArrayCell(a, [IntegerLit(10)]), ArrayCell(b, [IntegerLit(0)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 330))
    
#     def test331(self):
#         """More complex program"""
#         input = """a: string = 123_123 + "sad"; """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, IntegerLit(123123), StringLit(sad)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 331))
    
#     def test332(self):
#         """More complex program"""
#         input = """ a: string = 123_123 + "sad" + func(2); """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, BinExpr(+, IntegerLit(123123), StringLit(sad)), FuncCall(func, [IntegerLit(2)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 332))
    
#     def test333(self):
#         """More complex program"""
#         input = """a: string = func(func(5))+ func(2); """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, FuncCall(func, [FuncCall(func, [IntegerLit(5)])]), FuncCall(func, [IntegerLit(2)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 333))
    
#     def test334(self):
#         """More complex program"""
#         input = """a: string = func(func(5))+ func(func()); """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, FuncCall(func, [FuncCall(func, [IntegerLit(5)])]), FuncCall(func, [FuncCall(func, [])])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 334))

#     def test335(self):
#         """More complex program"""
#         input = """a: string = func(func(5 + 3, true)); """
#         expect = """Program([
# 	VarDecl(a, StringType, FuncCall(func, [FuncCall(func, [BinExpr(+, IntegerLit(5), IntegerLit(3)), BooleanLit(True)])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 335))
    
#     def test336(self):
#         """More complex program"""
#         input = """ a: string = func(func(5 + 3, true, 2_3223.3223e10));"""
#         expect = """Program([
# 	VarDecl(a, StringType, FuncCall(func, [FuncCall(func, [BinExpr(+, IntegerLit(5), IntegerLit(3)), BooleanLit(True), FloatLit(232233223000000.0)])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 336))
    
#     def test337(self):
#         """More complex program"""
#         input = """a: string = a[a[a[0]]];"""
#         expect = """Program([
# 	VarDecl(a, StringType, ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(0)])])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 337))
    
#     def test338(self):
#         """More complex program"""
#         input = """a: string = a[a[a[true]]];"""
#         expect = """Program([
# 	VarDecl(a, StringType, ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [BooleanLit(True)])])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 338))
    
#     def test339(self):
#         """More complex program"""
#         input = """a: string = a == b + c;"""
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(==, Id(a), BinExpr(+, Id(b), Id(c))))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 339))
    
#     def test340(self):
#         """More complex program"""
#         input = """a: string = a == b + c - d; """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(==, Id(a), BinExpr(-, BinExpr(+, Id(b), Id(c)), Id(d))))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 340))

#     def test341(self):
#         """More complex program"""
#         input = """a: string = 10 * 5 - (-5);"""
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(-, BinExpr(*, IntegerLit(10), IntegerLit(5)), UnExpr(-, IntegerLit(5))))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 341))
    
#     def test342(self):
#         """More complex program"""
#         input = """main: function void () {
#                     if (x < 10) res = 2.0*x;
#                     else if (x < 100) res = 2.5*x + 35;
#                     else res = x * 5.5 + 3;
                    
#                     if (x < 10)
#                     if (x == 3) x = x + 3;
#                     else x = 5;
#                     else if (x == 5) x = x + 4;

                    
#                 }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(x), IntegerLit(10)), AssignStmt(Id(res), BinExpr(*, FloatLit(2.0), Id(x))), IfStmt(BinExpr(<, Id(x), IntegerLit(100)), AssignStmt(Id(res), BinExpr(+, BinExpr(*, FloatLit(2.5), Id(x)), IntegerLit(35))), AssignStmt(Id(res), BinExpr(+, BinExpr(*, Id(x), FloatLit(5.5)), IntegerLit(3))))), IfStmt(BinExpr(<, Id(x), IntegerLit(10)), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(3))), AssignStmt(Id(x), IntegerLit(5))), IfStmt(BinExpr(==, Id(x), IntegerLit(5)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(4)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 342))

#     def test343(self):
#         """More complex program"""
#         input = """a: string = -10 * -5 - (-5) + a["123"];"""
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, BinExpr(-, BinExpr(*, UnExpr(-, IntegerLit(10)), UnExpr(-, IntegerLit(5))), UnExpr(-, IntegerLit(5))), ArrayCell(a, [StringLit(123)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 343))

#     def test344(self):
#         """More complex program"""
#         input = """a: string = a["123"] + fc(_aa);"""
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, ArrayCell(a, [StringLit(123)]), FuncCall(fc, [Id(_aa)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 344))
    
#     def test345(self):
#         """More complex program"""
#         input = """a: string = functio(a["123"]);"""
#         expect = """Program([
# 	VarDecl(a, StringType, FuncCall(functio, [ArrayCell(a, [StringLit(123)])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 345))

#     def test345(self):
#         """More complex program"""
#         input = """a: string = functio(a["123"]);"""
#         expect = """Program([
# 	VarDecl(a, StringType, FuncCall(functio, [ArrayCell(a, [StringLit(123)])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 345))

#     def test346(self):
#         """More complex program"""
#         input = """ a: boolean = fc(fc({1, 2, 3})) + {1, 2, "a"}; """
#         expect = """Program([
# 	VarDecl(a, BooleanType, BinExpr(+, FuncCall(fc, [FuncCall(fc, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])]), ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(a)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 346))

#     def test347(self):
#         """More complex program"""
#         input = """ a: boolean = fc(fc({1, 2, 3})) + abc; """
#         expect = """Program([
# 	VarDecl(a, BooleanType, BinExpr(+, FuncCall(fc, [FuncCall(fc, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])]), Id(abc)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 347))
    
#     def test348(self):
#         """More complex program"""
#         input = """a: boolean = {{fc(fc({1, 2, 3}))}} + {1, 2, "a"};"""
#         expect = """Program([
# 	VarDecl(a, BooleanType, BinExpr(+, ArrayLit([ArrayLit([FuncCall(fc, [FuncCall(fc, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])])])]), ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(a)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 348))

#     def test349(self):
#         """More complex program"""
#         input = """a: boolean = a[fc(fc({1, 2, 3}))] + {1, 2, "a"};"""
#         expect = """Program([
# 	VarDecl(a, BooleanType, BinExpr(+, ArrayCell(a, [FuncCall(fc, [FuncCall(fc, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])])]), ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(a)])))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 349))

#     def test350(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         print("tuimetquaroi");
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([CallStmt(print, StringLit(tuimetquaroi))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 350))

#     def test351(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         print("tuimetquaroi");
#                         a[0] = "brrr";
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([CallStmt(print, StringLit(tuimetquaroi)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), StringLit(brrr))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 351))
    
#     def test352(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         if(a > 10 + 1 * 3 :: (!y)) cout(getout);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([IfStmt(BinExpr(::, BinExpr(>, Id(a), BinExpr(+, IntegerLit(10), BinExpr(*, IntegerLit(1), IntegerLit(3)))), UnExpr(!, Id(y))), CallStmt(cout, Id(getout)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 352))

#     def test353(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         for(a = 5, 5 > 3, a > 5)
#                             writeInt();
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(5)), BinExpr(>, IntegerLit(5), IntegerLit(3)), BinExpr(>, Id(a), IntegerLit(5)), CallStmt(writeInt, ))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 353))
    
#     def test354(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         while(a > 10 + 1 * 3 :: (!y)) 
#                             cout(getout);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(>, Id(a), BinExpr(+, IntegerLit(10), BinExpr(*, IntegerLit(1), IntegerLit(3)))), UnExpr(!, Id(y))), CallStmt(cout, Id(getout)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 354))

#     def test355(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         while(a > 10 + 1 * 3 :: (!y)) 
#                             cout(getout);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([WhileStmt(BinExpr(::, BinExpr(>, Id(a), BinExpr(+, IntegerLit(10), BinExpr(*, IntegerLit(1), IntegerLit(3)))), UnExpr(!, Id(y))), CallStmt(cout, Id(getout)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 355))

#     def test356(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         do {
#                             cout(brrrr);
#                         }
#                         while(a > 10);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([CallStmt(cout, Id(brrrr))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 356))
    
#     def test357(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                         }
#                         while(a > 10);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([CallStmt(cout, Id(brrrr))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 357))
    
#     def test357(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                         }
#                         while(a > 10);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([BreakStmt()]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 357))

#     def test358(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         do {
#                             continue;
#                         }
#                         while(a > 10);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([ContinueStmt()]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 358))

#     def test359(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                             {
#                                 break;
#                             }
#                         }
#                         while(a > 10);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([BreakStmt(), BlockStmt([BreakStmt()])]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 359))

#     def test360(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         do {
#                             break;
#                             continue;
#                             for(i = 5, i < 10, i + 1) {
#                                 continue;
#                             }
#                         }
#                         while(a > 10);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([BreakStmt(), ContinueStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 360))

#     def test361(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         return 5;
#                         while(a > 10)
#                             break;
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(5)), WhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BreakStmt())]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 361))

#     def test362(self):
#         """More complex program"""
#         input = """quametmoi: function string (inherit n: string) {
#                         quametmoi(n + 100);
#                     }"""
#         expect = """Program([
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([CallStmt(quametmoi, BinExpr(+, Id(n), IntegerLit(100)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 362))

#     def test363(self):
#         """More complex program"""
#         input = """a: string = "Chuc mung ban da pass BTL1";
#                     quametmoi: function string (inherit n: string) {
#                         ketthuccuoochoi(123);
#                     }"""
#         expect = """Program([
# 	VarDecl(a, StringType, StringLit(Chuc mung ban da pass BTL1))
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([CallStmt(ketthuccuoochoi, IntegerLit(123))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 363))

# #     def test364(self):
# #         """More complex program"""
# #         input = """main : function void (abc : array [2] of float){
# #         for (i = 2, i < 10, i + 1){
# #             if (a < b) return {a, b};
# #             if (b < a) return {b, a};
# #             while(1){
# #             }
# #         }
# #         }"""
# #         expect = """Program([
# # 	FuncDecl(main, VoidType, [Param(abc, ArrayType([2], FloatType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), ReturnStmt(ArrayLit([Id(a), Id(b)]))), IfStmt(BinExpr(<, Id(b), Id(a)), ReturnStmt(ArrayLit([Id(b), Id(a)]))), WhileStmt(IntegerLit(1), BlockStmt([]))]))]))
# # ])"""
# #         self.assertTrue(TestAST.test(input, expect, 364))

#     def test_simple_program_60(self):
#         """Simple program: int main() {} """
#         input = """ func: function integer() {
#                     for (a[true] = 1, a < b, a + 1){
#                         if (x<5) 
#                             if (y>4){
#                                 y = y-1;
#                             } else while (z>3) if (r>4) {
#                                 r = 1 + r;
#                             } else return y; 
#                         else return y; 
#                     } 
#                     a: integer = 5;
#                 } """
#         expect = """Program([
# 	FuncDecl(func, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [BooleanLit(True)]), IntegerLit(1)), BinExpr(<, Id(a), Id(b)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, Id(x), IntegerLit(5)), IfStmt(BinExpr(>, Id(y), IntegerLit(4)), BlockStmt([AssignStmt(Id(y), BinExpr(-, Id(y), IntegerLit(1)))]), WhileStmt(BinExpr(>, Id(z), IntegerLit(3)), IfStmt(BinExpr(>, Id(r), IntegerLit(4)), BlockStmt([AssignStmt(Id(r), BinExpr(+, IntegerLit(1), Id(r)))]), ReturnStmt(Id(y))))), ReturnStmt(Id(y)))])), VarDecl(a, IntegerType, IntegerLit(5))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 364))

#     def test365(self):
#         """More complex program"""
#         input = """main : function void (abc : array [2] of float){
#         a = inputStr();
#         if (a == 2) return main();
#        }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(abc, ArrayType([2], FloatType))], None, BlockStmt([AssignStmt(Id(a), FuncCall(inputStr, [])), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(FuncCall(main, [])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 365))

#     def test366(self):
#         """More complex program"""
#         input = """main : function void (abc : array [2] of float){
#             sum = 0;
#              for (i = 0, i < length(arr), i + 2){
#                  sum = sum + arr[i];
#              }
#              print(sum);
#          }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(abc, ArrayType([2], FloatType))], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), CallStmt(print, Id(sum))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 366))

#     def test367(self):
#         """More complex program"""
#         input = """main : function void (abc : array [2] of float){
#          abc = 2.3 * 3E2 / 3.E6;
#          }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(abc, ArrayType([2], FloatType))], None, BlockStmt([AssignStmt(Id(abc), BinExpr(/, BinExpr(*, FloatLit(2.3), FloatLit(300.0)), FloatLit(3000000.0)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 367))

#     def test368(self):
#         """More complex program"""
#         input = """main : function void (abc : array [2] of float){
#              for(int = 2, int < int, int + int){
#                  return int + int;
#              }
#          }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [Param(abc, ArrayType([2], FloatType))], None, BlockStmt([ForStmt(AssignStmt(Id(int), IntegerLit(2)), BinExpr(<, Id(int), Id(int)), BinExpr(+, Id(int), Id(int)), BlockStmt([ReturnStmt(BinExpr(+, Id(int), Id(int)))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 368))

#     def test369(self):
#         """More complex program"""
#         input = """sumTo: function integer (n: integer) {
#                     if (n == 0) return 0;
#                     else return n + sumTo(n-1);
#                 }
#                 main: function void () {
#                     sumTo(100);
#                 }"""
#         expect = """Program([
# 	FuncDecl(sumTo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(0)), ReturnStmt(BinExpr(+, Id(n), FuncCall(sumTo, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(sumTo, IntegerLit(100))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 369))

#     def test370(self):
#         """More complex program"""
#         input = """sumTo: function integer (n: integer) {
#                     res: integer = 0;
#                     for (n = n, n > 0, -1) res = res + n;
                    
#                 }"""
#         expect = """Program([
# 	FuncDecl(sumTo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(res, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(n), Id(n)), BinExpr(>, Id(n), IntegerLit(0)), UnExpr(-, IntegerLit(1)), AssignStmt(Id(res), BinExpr(+, Id(res), Id(n))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 370))
    
#     def test371(self):
#         """More complex program"""
#         input = """linearSearch: function integer (arr: array [1000000] of integer, size: integer, val: integer) {
#                     i: integer;
#                     for (i = 0, i < size, 1) {
#                         if (arr[i] == val) return i;
#                     }
#                     return -1;
#                 }
#                 arr: array [5] of integer = {4,2,6,100,34};
#                 main: function void () {
#                     linearSearch(arr, 5, 100);
#                 }"""
#         expect = """Program([
# 	FuncDecl(linearSearch, IntegerType, [Param(arr, ArrayType([1000000], IntegerType)), Param(size, IntegerType), Param(val, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(val)), ReturnStmt(Id(i)))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
# 	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(4), IntegerLit(2), IntegerLit(6), IntegerLit(100), IntegerLit(34)]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(linearSearch, Id(arr), IntegerLit(5), IntegerLit(100))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 371))

#     def test372(self):
#         """More complex program"""
#         input = """binarySearch: function integer (arr: array [1000000] of integer, size: integer, val: integer) {
#                     l, r: integer = 0, size;
#                     while (l <= r) {
#                         mid: integer = (l + r) / 2;
#                         if (arr[mid] == val) return mid;
#                         else if (arr[mid] < val) l = mid + 1;
#                         else r = mid - 1;
#                     }
#                     return -1;
#                 }
#                 arr: array [5] of integer = {4,2,6,100,34};
#                 main: function void () {
#                     binarySearch(arr, 4, 100);
#                 }"""
#         expect = """Program([
# 	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([1000000], IntegerType)), Param(size, IntegerType), Param(val, IntegerType)], None, BlockStmt([VarDecl(l, IntegerType, IntegerLit(0)), VarDecl(r, IntegerType, Id(size)), WhileStmt(BinExpr(<=, Id(l), Id(r)), BlockStmt([VarDecl(mid, IntegerType, BinExpr(/, BinExpr(+, Id(l), Id(r)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(mid)]), Id(val)), ReturnStmt(Id(mid)), IfStmt(BinExpr(<, ArrayCell(arr, [Id(mid)]), Id(val)), AssignStmt(Id(l), BinExpr(+, Id(mid), IntegerLit(1))), AssignStmt(Id(r), BinExpr(-, Id(mid), IntegerLit(1)))))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
# 	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(4), IntegerLit(2), IntegerLit(6), IntegerLit(100), IntegerLit(34)]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(binarySearch, Id(arr), IntegerLit(4), IntegerLit(100))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 372))

#     def test373(self):
#         """More complex program"""
#         input = """checkPrime: function boolean (n: integer) {
#                     if (n < 2) return false;
#                     i: integer;
#                     for (i = 2, i < n / 2 , 1) {
#                         if (n % i == 0) return false;
#                     }
#                     return true;
#                 }
#                 main: function void () {
#                     checkPrime(123);
#                 }"""
#         expect = """Program([
# 	FuncDecl(checkPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(False))), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), BinExpr(/, Id(n), IntegerLit(2))), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(checkPrime, IntegerLit(123))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 373))
    
#     def test374(self):
#         """More complex program"""
#         input = """
#                 a : integer = foo();
#                 pow: function integer (num: integer, exp: integer) {
#                     if (exp == 0) return 1;
#                     tmp: integer = pow(num, exp/2);
#                     if (exp % 2 == 1) return tmp*tmp*num;
#                     else return tmp*tmp;
#                 }
#                 addDigits: function integer (num: integer) {
#                     if (num < 10) return num;
#                     res: integer = 0;
#                     while (num != 0) {
#                         res = res + num % 10;
#                         num = num / 10;
#                     }
#                     return addDigits(res);
#                 }
#                 main: function void () {
#                     printInteger(addDigits(12));
#                 }"""
#         expect = """Program([
# 	VarDecl(a, IntegerType, FuncCall(foo, []))
# 	FuncDecl(pow, IntegerType, [Param(num, IntegerType), Param(exp, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(exp), IntegerLit(0)), ReturnStmt(IntegerLit(1))), VarDecl(tmp, IntegerType, FuncCall(pow, [Id(num), BinExpr(/, Id(exp), IntegerLit(2))])), IfStmt(BinExpr(==, BinExpr(%, Id(exp), IntegerLit(2)), IntegerLit(1)), ReturnStmt(BinExpr(*, BinExpr(*, Id(tmp), Id(tmp)), Id(num))), ReturnStmt(BinExpr(*, Id(tmp), Id(tmp))))]))
# 	FuncDecl(addDigits, IntegerType, [Param(num, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(num), IntegerLit(10)), ReturnStmt(Id(num))), VarDecl(res, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(!=, Id(num), IntegerLit(0)), BlockStmt([AssignStmt(Id(res), BinExpr(+, Id(res), BinExpr(%, Id(num), IntegerLit(10)))), AssignStmt(Id(num), BinExpr(/, Id(num), IntegerLit(10)))])), ReturnStmt(FuncCall(addDigits, [Id(res)]))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(addDigits, [IntegerLit(12)]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 374))

#     def test375(self):
#         """More complex program"""
#         input = """fibo: function integer (n: integer) {
#                     if (n < 2) return 1;
#                     f1, f2: integer = 1, 1;
#                     for (i = 2, i <= n, 1) {
#                         f1 = f2 + f2 + f1;
#                         f2 = f1 - f2;
#                         f1 = f1 - f2;
#                     }
#                     return f2;
#                 }
#                 main: function void () {
#                     fibo(100);
#                 }"""
#         expect = """Program([
# 	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(IntegerLit(1))), VarDecl(f1, IntegerType, IntegerLit(1)), VarDecl(f2, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), IntegerLit(1), BlockStmt([AssignStmt(Id(f1), BinExpr(+, BinExpr(+, Id(f2), Id(f2)), Id(f1))), AssignStmt(Id(f2), BinExpr(-, Id(f1), Id(f2))), AssignStmt(Id(f1), BinExpr(-, Id(f1), Id(f2)))])), ReturnStmt(Id(f2))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(fibo, IntegerLit(100))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 375))

#     def test376(self):
#         """More complex program"""
#         input = """
#         main: function void () {
#                     if (x < 10) res = 2.0*x;
#                     else if (x < 100) res = 2.5*x + 35;
#                     else res = x * 5.5 + 3;
#                 }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(x), IntegerLit(10)), AssignStmt(Id(res), BinExpr(*, FloatLit(2.0), Id(x))), IfStmt(BinExpr(<, Id(x), IntegerLit(100)), AssignStmt(Id(res), BinExpr(+, BinExpr(*, FloatLit(2.5), Id(x)), IntegerLit(35))), AssignStmt(Id(res), BinExpr(+, BinExpr(*, Id(x), FloatLit(5.5)), IntegerLit(3)))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 376))

#     def test377(self):
#         """More complex program"""
#         input = """
#         a: string = a["123"] + fc(_aa);
#         a: boolean = fc(fc({1, 2, 3})) + {1, 2, "a"};
#         a: boolean = fc(fc({1, 2, 3})) + abc;
#         quametmoi: function string (inherit n: string) {
#                         return 5;
#                         while(a > 10)
#                              break;
#                      }
#         foo: function array [2,3] of string (n: integer, str: string) {}
#         """
#         expect = """Program([
# 	VarDecl(a, StringType, BinExpr(+, ArrayCell(a, [StringLit(123)]), FuncCall(fc, [Id(_aa)])))
# 	VarDecl(a, BooleanType, BinExpr(+, FuncCall(fc, [FuncCall(fc, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])]), ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(a)])))
# 	VarDecl(a, BooleanType, BinExpr(+, FuncCall(fc, [FuncCall(fc, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])]), Id(abc)))
# 	FuncDecl(quametmoi, StringType, [InheritParam(n, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(5)), WhileStmt(BinExpr(>, Id(a), IntegerLit(10)), BreakStmt())]))
# 	FuncDecl(foo, ArrayType([2, 3], StringType), [Param(n, IntegerType), Param(str, StringType)], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 377))

#     def test378(self):
#         """More complex program"""
#         input = """
#         main : function void (){
#              printBoolean(anArg);
#          }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, Id(anArg))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 378))

#     def test379(self):
#         """More complex program"""
#         input = """
#         main : function void (){
#              printBoolean(anArg);
#              readInteger();
#              printInteger(anArg);
#              readFloat();
#              writeFloat(anAr);
#             readBoolean();
#             printBoolean(anArg);
#             readString() ;
#             a,b,c : string = 1, 2, 3;
#          }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBoolean, Id(anArg)), CallStmt(readInteger, ), CallStmt(printInteger, Id(anArg)), CallStmt(readFloat, ), CallStmt(writeFloat, Id(anAr)), CallStmt(readBoolean, ), CallStmt(printBoolean, Id(anArg)), CallStmt(readString, ), VarDecl(a, StringType, IntegerLit(1)), VarDecl(b, StringType, IntegerLit(2)), VarDecl(c, StringType, IntegerLit(3))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 379))

#     def test380(self):
#         """More complex program"""
#         input = """
#         main : function void (){
#              a : array [2] of boolean = {true, false};
#              print(a[2]);
#               mynameis : string  = 2;
#          }
#           mynameis : string  = 2;
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], BooleanType), ArrayLit([BooleanLit(True), BooleanLit(False)])), CallStmt(print, ArrayCell(a, [IntegerLit(2)])), VarDecl(mynameis, StringType, IntegerLit(2))]))
# 	VarDecl(mynameis, StringType, IntegerLit(2))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 380))

#     def test381(self):
#         """More complex program"""
#         input = """
#         main : function void () {
#              myStr = 123455E-102 + { {1,2}, {2,3,4}, {5,6,7}};
#          }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(myStr), BinExpr(+, FloatLit(1.23455e-97), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7)])])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 381))

#     def test382(self):
#         """More complex program"""
#         input = """
#                  x : integer = 65;
#          fact : function integer (n : integer){
#              if (n == 0) return 1;
#              else return n * fact (n - 1);
#          }
#          inc : function void (out n : integer, delta : integer){
#              n = n + delta;
#          }         main : function void (){
#              delta: integer = fact(3);
#              inc(x, delta);
#              printInteger(x);
#          }
#         """
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(65))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# 	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 382))

#     def test383(self):
#         """More complex program"""
#         input = """
#                          funcAboutArray : function array [2] of integer (a: integer, del: float){
#              for (i = 2, i < 10, i + 2) while(1){
#                  b = {1,2,4,"abc"};
#             }
#          }
#         """
#         expect = """Program([
# 	FuncDecl(funcAboutArray, ArrayType([2], IntegerType), [Param(a, IntegerType), Param(del, FloatType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), WhileStmt(IntegerLit(1), BlockStmt([AssignStmt(Id(b), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4), StringLit(abc)]))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 383))

#     def test384(self):
#         """More complex program"""
#         input = """
#             gcd : function integer (a : integer, b : integer){
#              if (a > b) gcd(a-b,b);
#              if (b > a) gcd (a, b - a);
#              return a;
#          }
#         """
#         expect = """Program([
# 	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), CallStmt(gcd, BinExpr(-, Id(a), Id(b)), Id(b))), IfStmt(BinExpr(>, Id(b), Id(a)), CallStmt(gcd, Id(a), BinExpr(-, Id(b), Id(a)))), ReturnStmt(Id(a))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 384))

#     def test385(self):
#         """More complex program"""
#         input = """
#                      main: function void (){
#              while (1) {
#                  do {
#                      while (1) do {
#                          return;
#                      } while (1);
#                  } while (1);
#              }
#          }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(IntegerLit(1), BlockStmt([DoWhileStmt(IntegerLit(1), BlockStmt([WhileStmt(IntegerLit(1), DoWhileStmt(IntegerLit(1), BlockStmt([ReturnStmt()])))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 385))

#     def test386(self):
#         """More complex program"""
#         input = """
#                               x : integer = 65;
#          fact : function integer (n : integer){
#              if (n == 0) return 1;
#              else return n * fact (n - 1);
#          }
#          inc : function void (out n : integer, delta : integer){
#              n = n + delta;         }
#          main : function void (){
#              delta: integer = fact(3);
#              inc(x, delta);
#              printInteger(x);
#          }
#         """
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(65))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# 	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 386))
        
#     def test387(self):
#         """More complex program"""
#         input = """
#          funcAboutArray : function array [2] of integer (a: integer, del: float){
#              for (i = 2, i < 10, i + 2) while(1){
#                  b = {1,2,4,"abc"};             }
#          }
#         """
#         expect = """Program([
# 	FuncDecl(funcAboutArray, ArrayType([2], IntegerType), [Param(a, IntegerType), Param(del, FloatType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), WhileStmt(IntegerLit(1), BlockStmt([AssignStmt(Id(b), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4), StringLit(abc)]))])))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 387))

#     def test388(self):
#         """More complex program"""
#         input = """
#                  bine : function void (int : integer){
#          whatisdonem = {{lomg}, {bine}};
#          }
#         """
#         expect = """Program([
# 	FuncDecl(bine, VoidType, [Param(int, IntegerType)], None, BlockStmt([AssignStmt(Id(whatisdonem), ArrayLit([ArrayLit([Id(lomg)]), ArrayLit([Id(bine)])]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 388))

#     def test389(self):
#         """More complex program"""
#         input = """
#                 bine : function void (int : integer){
#              aloalo(1234);
#          }
#         """
#         expect = """Program([
# 	FuncDecl(bine, VoidType, [Param(int, IntegerType)], None, BlockStmt([CallStmt(aloalo, IntegerLit(1234))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 389))

#     def test390(self):
#         """More complex program"""
#         input = """
#                /* 
#          a : array [2] of float;        */
#          bine : function void (int : integer){
#          a = 2;
#          }
#         """
#         expect = """Program([
# 	FuncDecl(bine, VoidType, [Param(int, IntegerType)], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 390))

#     def test391(self):
#         """More complex program"""
#         input = """
#                bine : function void (int : integer){
#          areuok = "i am not ok";
#          tired = "i am so tied";
#          for (tired = 2, tired < 33, tired + 2){
#              print({1,2,4});
#          }
#          }
#         """
#         expect = """Program([
# 	FuncDecl(bine, VoidType, [Param(int, IntegerType)], None, BlockStmt([AssignStmt(Id(areuok), StringLit(i am not ok)), AssignStmt(Id(tired), StringLit(i am so tied)), ForStmt(AssignStmt(Id(tired), IntegerLit(2)), BinExpr(<, Id(tired), IntegerLit(33)), BinExpr(+, Id(tired), IntegerLit(2)), BlockStmt([CallStmt(print, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 391))

#     def test392(self):
#         """More complex program"""
#         input = """
#                a: integer = 1;
#                a: array[10, 2] of integer = {};
#                a: array[10, 2] of integer = {1, 2};
#                a: array[10, 2] of integer = {1, 2};
#                      /* This is comment */
#                     b: boolean = (a >= b) && c;
#         """
#         expect = """Program([
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([]))
# 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
# 	VarDecl(a, ArrayType([10, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
# 	VarDecl(b, BooleanType, BinExpr(&&, BinExpr(>=, Id(a), Id(b)), Id(c)))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 392))

#     def test393(self):
#         """More complex program"""
#         input = """
#                listNumber : array [2,3] of integer = {{1,2,3}, {4,5,6}, {7,8,9}};
#         """
#         expect = """Program([
# 	VarDecl(listNumber, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 393))

#     def test394(self):
#         """More complex program"""
#         input = """
#               main : function void () {
#          do {                 abc =  12344 * 2345 / 2345 % 4567 ;
#                  for (abc = 0, abc < 100000, abc*12){
#                      do {
#                          abc = abc1234;
#                      } while(abc < 100000);                 }
#              } while(1);        }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(IntegerLit(1), BlockStmt([AssignStmt(Id(abc), BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(12344), IntegerLit(2345)), IntegerLit(2345)), IntegerLit(4567))), ForStmt(AssignStmt(Id(abc), IntegerLit(0)), BinExpr(<, Id(abc), IntegerLit(100000)), BinExpr(*, Id(abc), IntegerLit(12)), BlockStmt([DoWhileStmt(BinExpr(<, Id(abc), IntegerLit(100000)), BlockStmt([AssignStmt(Id(abc), Id(abc1234))]))]))]))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 394))

#     def test395(self):
#         """More complex program"""
#         input = """
#               main : function void () {
#              if (! a % 3) abc = 2;
#              else abc = 3;
#          }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(%, UnExpr(!, Id(a)), IntegerLit(3)), AssignStmt(Id(abc), IntegerLit(2)), AssignStmt(Id(abc), IntegerLit(3)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 395))

#     def test396(self):
#         """More complex program"""
#         input = """
#              main : function void () {
#              areuready = "abcb2" + 12345 + {1,2,3} + foo(2,3,4) + _;
#          }
#         """
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(areuready), BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, StringLit(abcb2), IntegerLit(12345)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), FuncCall(foo, [IntegerLit(2), IntegerLit(3), IntegerLit(4)])), Id(_)))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 396))

#     def test397(self):
#         """More complex program"""
#         input = """
#                     inc : function void (out n : integer, delta : integer){
#              n = n + delta;
#          }
#          main : function void (){
#              delta: integer = fact(3);
#              inc(x, delta);
#              printInteger(x);
#          }
#         """
#         expect = """Program([
# 	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
# 	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 397))

#     def test398(self):
#         """More complex program"""
#         input = """
#                     a: integer = 1;
#                      a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1; a: integer = 1;
#                      fact: function integer (n: integer) {
#                          if(n == 0) return 1;
#                          else return n * fact(n - 1);
#                      }
#                      fact: function integer (n: integer) {
#                          if(n == 0) return 1;
#                          else return n * fact(n - 1);
#                      }
#                      fact: function integer (n: integer) {
#                          if(n == 0) return 1;
#                          else return n * fact(n - 1);
#                      }
#                      fact: function integer (n: integer) {
#                          if(n == 0) return 1;
#                          else return n * fact(n - 1);
#                      }
#         """
#         expect = """Program([
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	VarDecl(a, IntegerType, IntegerLit(1))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# 	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 398))

#     def test399(self):
#         """More complex program"""
#         input = """
#                     a: array [1, 2, 3] of integer = arr[a];
#         """
#         expect = """Program([
# 	VarDecl(a, ArrayType([1, 2, 3], IntegerType), ArrayCell(arr, [Id(a)]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 399))