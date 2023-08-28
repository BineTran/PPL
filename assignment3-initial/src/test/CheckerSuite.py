import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """ a: integer = 1;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_401(self):
        input = """ a: integer = 1;
                    b: auto = c + 1;
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_402(self):
        input = """ a: float = 1 + 2.0;
                    b: auto = a + 1;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_403(self):
        input = """ main1: function integer () {
                    }
                    a: integer = 1;
                    b: auto = a + 1;
                    c: auto = a + main1();
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """ alo: function float () {
                    }
                    a: integer = 1;
                    b: auto = 1.0;
                    c: auto = b + alo();
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_405(self):
        input = """ 
                    a: array [1, 2, 3] of integer = {1,2,3};
                    b: integer = a[2];
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """ alo: function float (b: string, c: string) {
                        a: integer = b;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_407(self):
        input = """ alo: function float (b: string, c: string) {
                        a = b;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_408(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_410(self):
        input = """ alo: function float (b: string, b: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Redeclared Parameter: b"""
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_411(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 > 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """ main1: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 > 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """ alo: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 + 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in statement: IfStmt(BinExpr(+, IntegerLit(3), IntegerLit(2)), BlockStmt([VarDecl(a, BooleanType, BooleanLit(True))]), BlockStmt([VarDecl(a, BooleanType, BooleanLit(True))]))"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """ alo: function float (b: string, c: boolean) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c < 3, c + 1){
                           c = c + 1; 
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(0)), BinExpr(<, Id(c), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """ main1: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c + 3, c + 1){
                           c = c + 1; 
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """ alo: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c < 3, c + 1){
                           c = c + 1; 
                        }
                        break;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """ 
                    alo: function float (c: integer){
                        
                    }
                    a: float = alo(7.4) + 5;
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in expression: FuncCall(alo, [FloatLit(7.4)])"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """ 
                    a: integer = main1(7) + 5;
                    main1: function integer (c: integer){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """ 
                    a: float = main1(7) + 5;
                    foo: function integer(c: float){
                        
                    }
                    main1: function float (c: integer){
                        foo(6.5);
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """ 
                    a: float = main1(7) + 5;
                    main1: function float (c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """ 
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        boo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Function: boo"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """ 
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main2: function integer () inherit main1 {
                        c = c + 1;
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
                    main2: function integer () inherit main1 {
                        c = c + 1;
                    }
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
                    main2: function integer () inherit main1 {
                        d = d + 1;
                    }
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer, d: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
                    main2: function integer () inherit main1 {
                        d = c + 1;
                    }
                    
                    a: float = main1(7,8) + 5;
                    
                    main1: function float (inherit c: integer, inherit d: integer){
                        foo(6.5);
                    }
                    
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    a: float = foo(1,2);
                    c: float = a + 2;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    a: float = foo(1,2);
                    b: integer = foo(1,2) + 1;
                    c: float = a + 2;
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: integer = foo(1,2) + 1;
                    a: integer = foo(1,2);
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: float = (foo(1,2) + 1.0) * (foo(1,2) + 1);
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: integer = (foo(1,2) + 1) * (foo(1,2) + 1.0);
                    main: function void () {
                        
                    }
                    
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(*, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)), BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), FloatLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_431(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: integer = (foo(1,2) + 1) * (foo(1,2) + 1.0);
                    main: function void () {
                        
                    }
                    
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(*, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)), BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), FloatLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    boo: function void (){
                        foo(2,3);
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_433(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22];
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22];
                """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2.4];
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in expression: ArrayCell(a, [FloatLit(2.4)])"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    main: function void () {
                        c: array[3] of integer = {1, 2.3};
                    }
                """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.3)])"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2.0;
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2.0;
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function float () {
                        return 2.0;
                    }
                    main: function void(){
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function auto () {
                        return 2.0;
                    }
                    main: function void(){
                        a: integer = boo();
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(boo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function auto () {
                        return 2.0;
                    }
                    main: function void(){
                        a: float = boo();
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function auto (a: integer) {
                        return 2.0;
                    }
                    main: function void(){
                        a: float = boo(2.0);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(boo, [FloatLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
                    b: auto = main();
                    main: function void(){
                        
                    }
                """
        expect = """Type mismatch in expression: FuncCall(main, [])"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    b: integer;
                    main: function void(){
                        c: integer = a[1];
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    b: integer;
                    main: function void(){
                        b: array[5] of integer = {1,2,3,4,5};
                        c: integer = b[1];
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    b: integer;
                    main: function void(){
                        b: array[5] of integer = {1,2,3,4,5};
                        c: integer = b[1];
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
                    a: function integer(c: integer){
                        
                    }
                    main: function void(){
                        b: integer = a(1,2);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(a, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
                    a: function integer(c: integer){
                        
                    }
                    c: integer = a(1,2);
                    main: function void(){
                        b: integer = a(1,2);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(a, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
                    main1: function float (inherit c: integer){
                        
                    }
                    a: function integer (c: integer) inherit main1{
                        
                    }
                """
        expect = """Invalid Parameter: c"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
                    main1: function float (c: integer){
                        
                    }
                    a: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Invalid statement in function: a"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
                    main1: function float (){
                        
                    }
                    a: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
                    main1: function float (){
                        
                    }
                    main1: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Redeclared Function: main1"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
                    a: integer = 1;
                    a: float = 1.0;
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    foo: integer = 2;
                    
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
                    foo: integer = 2;
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    
                """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 457))


    def test_458(self):
        input = """
                    foo: integer = 2;
                    iden : integer = 5;
                    main: function void (){
                        while (foo < -3){
                            if (iden % 2 == 1) {
                                iden = iden + 1;
                            }
                            else {
                                iden = iden + 2;
                            }
                            foo = foo - 1;
                        }
                    }
                    
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
                    foo: integer = 2;
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    
                """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
                    
                    foo: function auto(a: integer){
                        
                    }
                    main: function void (){
                        
                    }
                    a: auto = foo(2);
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
                    
                    foo: function float(a: integer){
                        return a;
                    }
                    main: function void (){
                        
                    }
                    a: auto = foo(2);
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """
                    
                    foo: function integer(a: float){
                        return a;
                    }
                    main: function void (){
                        
                    }
                    a: auto = foo(2);
                """
        expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
                    foo: function float (a: float){
                        return a;
                    }
                    foo1: function integer(){
                        foo(2);
                    }
                    main: function void (){
                        
                    }
                    c: auto = foo(2);
                    a: auto = foo1();
                    b: float = foo1();
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
                    y: function void (a: string) {}
                    x: function void (a: auto) {
                        y(a);
                        b: string = a :: "Hello";
                    }
                    main: function void () {
                        x(5);
                    }
                """
        expect = """Type mismatch in statement: CallStmt(x, IntegerLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """
                    
                    x: function void (a: auto) {}
                    main: function void () {
                        x("a");
                        x(2);
                    }
                """
        expect = """Type mismatch in statement: CallStmt(x, IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = """
                    y: function auto (a: string) {}
                    x: function string (a: string) {}
                    main: function void () {
                        x(y("abc"));
                        a: integer = y("a");
                    } 
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(y, [StringLit(a)]))"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """
                    y: function string (a: auto) {}
                    x: function string (a: string) {}
                    main: function void () {
                        a: string = y("a");
                        b: string = y(2);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(y, [IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
                    y: function auto (a: integer) {
                        
                    }
                    x: function string (a: string) {
                        
                    }
                    main: function void () {
                        a: string = x(y(5));
                        b: integer = y(5);
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FuncCall(y, [IntegerLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
                    y: function auto (a: auto) {
                        
                    }
                    x: function string (a: string) {
                        
                    }
                    z: function integer (a: integer) {
                        
                    }
                    main: function void () {
                        x(y(5));
                        a: string = y(6);
                        z(y(6));
                    }
                """
        expect = """Type mismatch in statement: CallStmt(z, FuncCall(y, [IntegerLit(6)]))"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
                    a: integer = 5;
                    b: integer = 5 + a;
                    main: function void () {
                        if (2 > 3.56) 
                        {
                            c : integer = 1;
                            if (3 < 4){
                                if (5.6 >= 7.8){
                                    
                                } 
                                if (5 != true){
                                    
                                }
                                if ( 1 == false)
                                if ( b <= a) {
                                    b = c + a;
                                    for (c = 2, c < 5, c + 1){
                                        a = a + b;
                                    }
                                }
                            }
                        }
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
                    binarySearch: function integer (a: integer, l: integer, r: integer, x: integer) {
                        arr: array [6] of integer = {1, 2, 3, 4, 5};
                        while (l <= r) {
                            m: integer = l + (r - 1)/2;
                            if (arr[m] == x) return m;
                            if (arr[m] < x) l = m + 1;
                            else r = m - 1;
                        }
                        return -1;
                    }
                    main: function void () {
                        arr: array [6] of integer = {1, 2, 3, 4, 5};
                        n: integer = 5;
                        x: integer = 10;
                        result: integer = binarySearch(6, 0, n-1, x-1);
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([6], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
                    boo: function auto (n: integer) {
                        
                    }
                    main: function void () {
                        a: integer = boo(2) + 4;
                        b: string = boo(3);
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, StringType, FuncCall(boo, [IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
                    boo: function auto (n: integer) {
                        
                    }
                    main: function void () {
                        a: integer = boo(2) + boo(3);
                        b: string = boo(3);
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 473))


    def test_475(self):
        input = """
                    foo: function void (inherit a: integer, a: float) inherit bar {}
                """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 475))
        

    def test_476(self):
        input = """
                    a: integer;
                    foo: function integer (p: boolean) {}
                    bar: function integer () inherit foo {
                        a = foo(1);
                    }
                """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
                    foo: function void(){
                        
                    }
                    main: function void() {
                        foo: integer = 1; 
                        x: integer = foo();
                        x = foo;
                    }
                """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """
                    main : function void() inherit foo{
                        super(1.0, 2.0, 3.0);
                        z: integer = foo(1,2,3) + 1;
                        x = 1;
                        y = true;
                    }
                    foo : function auto(inherit x : auto, inherit y : auto, z : auto){
                        x = true;
                        return x + y + z;
                    }
                """
        expect = """Type mismatch in statement: AssignStmt(Id(y), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
                    foo: function auto (a: string, b: string){
                        return a :: b;
                    }
                    a: float = foo("hello", "Hi");
                    // Chu y
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, FloatType, FuncCall(foo, [StringLit(hello), StringLit(Hi)]))"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
                    a: float = foo(1, 2) + 1.5;
                    foo: function auto (a: integer, b: integer) {
                        return a + b;
                    }
                    b: integer = foo(2,3);
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FuncCall(foo, [IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_482(self):
        input = """
                    foo: function auto (a: integer, b: integer) {
                        return a + b;
                    }
                    b: integer = foo(2,3);
                """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_481(self):
        input = """
                    foo: function integer(){
                        
                    }
                    main: function void(){

                        foo: integer = 3;

                        a: integer = foo(); // line 5

                    }
                """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_477(self):
        input = """
                    foo: function void(){
                        
                    }
                    main: function void() {
                        foo: integer = 1; 
                        x: integer = foo();
                        x = foo;
                    }
                """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_483(self):
        input = """
                        
                    foo: function integer (a: integer) {
                        
                    }
                    a: integer = foo(1,2);  
                """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test_484(self):
        input = """  
                    foo: function integer (a: integer) {
                        foo(1,2); 
                    }
                """
        expect = """Type mismatch in expression: CallStmt(foo, IntegerLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_474(self):
        input = """
                    // a: array[2,2] of integer = { {{1}, {3}}, {1,3} };
                    c: array[2,2] of integer = { {1,2.0}, {2,1} };
                """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_485(self):
        input = """
                    a: array[2,2] of integer = { {1,3}, {1,4} }; 
                    c: array[2,2] of integer = { {1,2}, {2,1} };
                    b: integer = a[2.0];
                """
        expect = """Type mismatch in expression: ArrayCell(a, [FloatLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
                    a: array[2,2] of integer = { {1,3}, {1,4} };
                    c: array[2,2] of integer = { {1,2}, {2,1} };
                    d: integer = 3;
                    b: integer = a[d];
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [Id(d)]))"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
                    test1 : function string(y : auto) {
                        y = 2; // line 2
                        return "1";
                    }
                    main: function void () {
                        test1(true); // line 6
                    }
                """
        expect = """Type mismatch in statement: CallStmt(test1, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 487))
    
    def test_488(self):
        input = """ 
                    main1: function float (inherit c: integer){
                        
                    }
                    foo: function integer (a: float) inherit main1{
                        
                    }
                """
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """ 
                    main1: function float (inherit c: integer){
                        
                    }
                    foo: function integer (a: float) inherit main1{
                        super();
                    }
                """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """ 
                    main1: function float (inherit c: integer){
                        
                    }
                    foo: function integer (a: float) inherit main1{
                        super(1,2);
                    }
                """
        expect = """Type mismatch in expression: IntegerLit(2)"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """ 
                    main1: function float (inherit c: integer){
                        
                    }
                    foo: function integer (a: float) inherit main1{
                        preventDefault(1,2);
                    }
                """
        expect = """Type mismatch in statement: CallStmt(preventDefault, IntegerLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """ 
                    foo: function auto (c: integer){
                        if (5 > 3) {
                            return "a";
                        }
                        else 
                        {   
                            return 1;
                        }
                    }
                    a: integer = foo(1);
                    
                """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """ 
                    foo: function auto (c: integer){
                        return "a";
                        return 1;
                    }
                    a: integer = foo(1);
                    
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, [IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """ 
                    y: function auto() {}
                    x: function void (a: auto) {
                        i: integer;
                        for (i = a, i < 5, i + 1) {
                            printBoolean(5 == a);
                        }
                        i = y; 
                    }
                    main: function void () {}        
                """
        expect = """Undeclared Identifier: y"""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """ 
                    alo: function integer  (a: integer){
                        
                    }
                    main: function void () {
                        readInteger();
                    }       
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """ 
                    alo: function integer  (a: integer){
                        return;
                    }
                    main: function void () {
                        readInteger();
                    }       
                """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """ a: integer = 1;
                    b: auto = c + 1;
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """ a: integer = 1;
                    b: auto = c + 1;
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """ a: float = 1 + 2.0;
                    b: auto = a + 1;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_500(self):
        input = """ main1: function integer () {
                    }
                    a: integer = 1;
                    b: auto = a + 1;
                    c: auto = a + main1();
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 500))
