from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):

    # program: decls EOF ;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))



    # decls: decl decls | decl;
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decls())



    # decl: variablesdecl | functiondecl ;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.variablesdecl():
            return self.visit(ctx.variablesdecl())
        return self.visit(ctx.functiondecl())

    # stm: matchStm | unmatchStm;
    def visitStm(self, ctx:MT22Parser.StmContext):
        if ctx.matchStm():
            return self.visit(ctx.matchStm())
        return self.visit(ctx.unmatchStm())

    # matchStm: IF LP expr RP matchStm ELSE matchStm
	# 	      | otherStm;
    
    def visitMatchStm(self, ctx:MT22Parser.MatchStmContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.otherStm())
        cond = self.visit(ctx.expr())
        matchStm0 = self.visit(ctx.matchStm(0))
        matchStm1 = self.visit(ctx.matchStm(1))
        return IfStmt(cond,matchStm0,matchStm1)
    
    # unmatchStm: IF LP expr RP stm
	# 	        | IF LP expr RP matchStm ELSE unmatchStm;
    def visitUnmatchStm(self, ctx:MT22Parser.UnmatchStmContext):
        if ctx.ELSE():
            cond = self.visit(ctx.expr())
            matchStm0 = self.visit(ctx.matchStm())
            unmatchStm0 = self.visit(ctx.unmatchStm())
            return IfStmt(cond,matchStm0,unmatchStm0)
        cond = self.visit(ctx.expr())
        stm0 = self.visit(ctx.stm())
        return IfStmt(cond,stm0)
    
    # otherStm: block_stm 
    # 		  | call_stm 
    # 		  | return_stm 
    # 		  | continue_stm 
    # 		  | break_stm 
    # 		  | do_while_stm 
    #         | while_stm 
    # 		  | for_stm 
    # 		  | assign_stm;   
    def visitOtherStm(self, ctx:MT22Parser.OtherStmContext):
        if ctx.block_stm():
                return self.visit(ctx.block_stm())
        if ctx.call_stm():
            return self.visit(ctx.call_stm())
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        if ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        if ctx.break_stm():
            return self.visit(ctx.break_stm())
        if ctx.do_while_stm():
            return self.visit(ctx.do_while_stm())
        if ctx.while_stm():
            return self.visit(ctx.while_stm())
        if ctx.for_stm():
            return self.visit(ctx.for_stm())
        if ctx.assign_stm():
            return self.visit(ctx.assign_stm())
    
    # stm: block_stm 
	# | call_stm 
	# | return_stm 
	# | continue_stm 
	# | break_stm 
	# | do_while_stm 
	# | while_stm 
	# | for_stm | if_stm | assign_stm;
    # def visitStm(self, ctx:MT22Parser.StmContext):
    #     if ctx.block_stm():
    #         return self.visit(ctx.block_stm())
    #     if ctx.call_stm():
    #         return self.visit(ctx.call_stm())
    #     if ctx.return_stm():
    #         return self.visit(ctx.return_stm())
    #     if ctx.continue_stm():
    #         return self.visit(ctx.continue_stm())
    #     if ctx.break_stm():
    #         return self.visit(ctx.break_stm())
    #     if ctx.do_while_stm():
    #         return self.visit(ctx.do_while_stm())
    #     if ctx.while_stm():
    #         return self.visit(ctx.while_stm())
    #     if ctx.for_stm():
    #         return self.visit(ctx.for_stm())
    #     if ctx.if_stm():
    #         return self.visit(ctx.if_stm())
    #     if ctx.assign_stm():
    #         return self.visit(ctx.assign_stm())
    
    # block_stm: LCURB list_vardecl_stm RCURB;
    def visitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        return BlockStmt(self.visit(ctx.list_vardecl_stm()))


    # list_vardecl_stm: list_vardecl_stmprime | ;
    def visitList_vardecl_stm(self, ctx:MT22Parser.List_vardecl_stmContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_vardecl_stmprime())
        

    # list_vardecl_stmprime: vardecl_stmprime list_vardecl_stmprime | vardecl_stmprime;
    def visitList_vardecl_stmprime(self, ctx:MT22Parser.List_vardecl_stmprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.vardecl_stmprime())
        return self.visit(ctx.vardecl_stmprime()) + self.visit(ctx.list_vardecl_stmprime())


    # vardecl_stmprime: variablesdecl | stm;
    def visitVardecl_stmprime(self, ctx:MT22Parser.Vardecl_stmprimeContext):
        if ctx.stm():
            return [self.visit(ctx.stm())]
        return self.visit(ctx.variablesdecl())
        


    # functiondecl: ID COLON FUNCTION (array_type | atomic_types) LP listparams RP (INHERIT ID)? block_stm;
    def visitFunctiondecl(self, ctx:MT22Parser.FunctiondeclContext):
        if ctx.array_type():
            if ctx.INHERIT():
                return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.array_type()), self.visit(ctx.listparams()), ctx.ID(1).getText(), self.visit(ctx.block_stm()))]
            return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.array_type()), self.visit(ctx.listparams()),None,self.visit(ctx.block_stm()))]
        if ctx.INHERIT():
            return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.atomic_types()), self.visit(ctx.listparams()), ctx.ID(1).getText(), self.visit(ctx.block_stm()))]
        return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.atomic_types()), self.visit(ctx.listparams()),None,self.visit(ctx.block_stm()))]

    # listparams: listparamsprime | ;
    def visitListparams(self, ctx:MT22Parser.ListparamsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.listparamsprime())


    # listparamsprime: paramdecl COMMA listparamsprime | paramdecl;
    def visitListparamsprime(self, ctx:MT22Parser.ListparamsprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramdecl())]
        return [self.visit(ctx.paramdecl())] + self.visit(ctx.listparamsprime())


    # call_stm: ID LP listexps RP SEMICOL;
    def visitCall_stm(self, ctx:MT22Parser.Call_stmContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.listexps()))


    # return_stm: RETURN (expr | ) SEMICOL;
    def visitReturn_stm(self, ctx:MT22Parser.Return_stmContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()


    # continue_stm: CONTINUE SEMICOL;
    def visitContinue_stm(self, ctx:MT22Parser.Continue_stmContext):
        return ContinueStmt()

    # break_stm: BREAK SEMICOL;
    def visitBreak_stm(self, ctx:MT22Parser.Break_stmContext):
        return BreakStmt()


    # do_while_stm: DO block_stm WHILE LP expr RP SEMICOL;
    def visitDo_while_stm(self, ctx:MT22Parser.Do_while_stmContext):
        return DoWhileStmt(self.visit(ctx.expr()),self.visit(ctx.block_stm()))


    # while_stm: WHILE LP expr RP stm;
    def visitWhile_stm(self, ctx:MT22Parser.While_stmContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stm()))


    # for_stm: FOR LP lhs EQUAL expr COMMA expr COMMA expr RP stm;
    def visitFor_stm(self, ctx:MT22Parser.For_stmContext):
        init = AssignStmt(self.visit(ctx.lhs()),self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        upd = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stm())
        return ForStmt(init,cond,upd,stmt)


    # # if_stm: IF LP expr RP stm (ELSE stm)?;
    # def visitIf_stm(self, ctx:MT22Parser.If_stmContext):
    #     cond = self.visit(ctx.expr())
    #     stmt0 = self.visit(ctx.stm(0))
    #     if ctx.ELSE():
    #         stmt1 = self.visit(ctx.stm(1))
    #         return IfStmt(cond,stmt0,stmt1)
    #     return IfStmt(cond,stmt0)
            
            

    # assign_stm: lhs EQUAL expr SEMICOL;
    def visitAssign_stm(self, ctx:MT22Parser.Assign_stmContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs,rhs)


    # # lhs: ID | ID LSQAB listexpsprime RSQAB;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText());
        return ArrayCell(ctx.getChild(0).getText(),self.visit(ctx.listexpsprime()))


    # # paramdecl: INHERIT ? OUT ? ID COLON (array_type | atomic_types_for_param);
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        if ctx.array_type():
            typeParam = self.visit(ctx.array_type())
        else :
            typeParam = self.visit(ctx.atomic_types_for_param())
        if ctx.INHERIT():
            if ctx.OUT():
                return ParamDecl(ctx.ID().getText(),typeParam, True, True)
            return ParamDecl(ctx.ID().getText(),typeParam, False, True)
        if ctx.OUT():
            return ParamDecl(ctx.ID().getText(),typeParam, True, False)
        return ParamDecl(ctx.ID().getText(),typeParam, False, False)
        


    # variablesdecl: list_id assi_components SEMICOL | ID recursion_assi expr SEMICOL;
    def visitVariablesdecl(self, ctx:MT22Parser.VariablesdeclContext):
        if ctx.expr():
            # [abc|234] 0 1 2   3   4 5 6
            
            listIDVal = [ctx.ID().getText()] + self.visit(ctx.recursion_assi()) + [self.visit(ctx.expr())]
        
            listID = listIDVal[0 : int(len(listIDVal)/2)]
            
            listVal = listIDVal[int(len(listIDVal)/2) + 1:]
            
            typeVar = listIDVal[int(len(listIDVal)/2)]
            
            
            return list(map(lambda x,y: VarDecl(x, typeVar, y), listID, listVal))
            
        typeVar = self.visit(ctx.assi_components())
        listID = self.visit(ctx.list_id())
        return list(map(lambda x: VarDecl(x, typeVar, None), listID))
        
    
    # list_id: ID COMMA list_id | ID;
    def visitList_id(self, ctx:MT22Parser.List_idContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.list_id())

    # recursion_assi: COMMA ID recursion_assi expr COMMA | assi_components_EQ;
    def visitRecursion_assi(self, ctx:MT22Parser.Recursion_assiContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.assi_components_EQ())]
        return [ctx.ID().getText()] + self.visit(ctx.recursion_assi()) + [self.visit(ctx.expr())]
        

    # assi_components: COLON (atomic_types_for_param | array_type);
    def visitAssi_components(self, ctx:MT22Parser.Assi_componentsContext):
        return self.visit(ctx.atomic_types_for_param()) if ctx.atomic_types_for_param() else self.visit(ctx.array_type())
    
    # assi_components_EQ: COLON (atomic_types_for_param | array_type) EQUAL;
    def visitAssi_components_EQ(self, ctx:MT22Parser.Assi_components_EQContext):
        return self.visit(ctx.atomic_types_for_param()) if ctx.atomic_types_for_param() else self.visit(ctx.array_type())

    # atomic_types: BOOLEAN | INTERGER | FLOAT | STRING | VOID | AUTO;
    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.INTERGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.VOID():
            return VoidType()
        if ctx.AUTO():
            return AutoType()

    # atomic_types_for_param: BOOLEAN | INTERGER | FLOAT | STRING | AUTO;
    def visitAtomic_types_for_param(self, ctx:MT22Parser.Atomic_types_for_paramContext):
        if ctx.BOOLEAN():
            return BooleanType()
        if ctx.INTERGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.AUTO():
            return AutoType()

    # array_type: ARRAY LSQAB dimensions RSQAB OF element_type;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        dimen = self.visit(ctx.dimensions())
        typ = self.visit(ctx.element_type())
        return ArrayType(dimen,typ)


    # dimensions: INTLIT COMMA dimensions | INTLIT;
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())

    # element_type: atomic_types;
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        return self.visit(ctx.atomic_types())


    # arraylit: LCURB listexps RCURB;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.listexps()))


    # listexps: listexpsprime | ;
    def visitListexps(self, ctx:MT22Parser.ListexpsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.listexpsprime())


    # listexpsprime: expr COMMA listexpsprime | expr;
    def visitListexpsprime(self, ctx:MT22Parser.ListexpsprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.listexpsprime())


    # expr: expr1 STRINGCON expr1 | expr1;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.STRINGCON().getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))


    # expr1: expr2 (ISEQUAL | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSTHANOREQ | GREATERTHANOREQ) expr2 | expr2;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
 

    # expr2: expr2 (AND | OR ) expr3 | expr3;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))


    # expr3: expr3 (ADD | SUBTRAC) expr4 | expr4;
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))


    # expr4: expr4 (MULTI | DIVIS | MODUL) expr5 | expr5;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))


    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
           return self.visit(ctx.getChild(0))
        return UnExpr(ctx.getChild(0).getText(),self.visit(ctx.getChild(1)))


    # expr6: SUBTRAC expr6 | expr7;
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnExpr(ctx.getChild(0).getText(),self.visit(ctx.getChild(1)))


    # expr7: ID LSQAB listexpsprime RSQAB | expr8;
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.getChildCount() == 1:
           return self.visit(ctx.getChild(0))
        return ArrayCell(ctx.getChild(0).getText(),self.visit(ctx.listexpsprime()))


    # expr8: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | ID | arraylit | subexpr | callexpr;
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            if ctx.FLOATLIT().getText()[0:2] == '.e':
                return FloatLit(float(0.0))
            if ctx.FLOATLIT().getText()[0:2] == '.E':
                return FloatLit(float(0.0))
            return FloatLit(float(ctx.FLOATLIT().getText()))
        if ctx.BOOLLIT():
            if ctx.BOOLLIT().getText() == "true":
                return BooleanLit(True)
            return BooleanLit(False) 
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.arraylit():
            return self.visit(ctx.arraylit())
        if ctx.subexpr():
            return self.visit(ctx.subexpr())
        if ctx.callexpr():
            return self.visit(ctx.callexpr())
            

    # subexpr: LP expr RP;
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visit(ctx.expr())


    # callexpr: ID LP listexps RP;
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        return FuncCall(ctx.ID().getText(),self.visit(ctx.listexps()))
