# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stm.
    def visitStm(self, ctx:MT22Parser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#matchStm.
    def visitMatchStm(self, ctx:MT22Parser.MatchStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unmatchStm.
    def visitUnmatchStm(self, ctx:MT22Parser.UnmatchStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#otherStm.
    def visitOtherStm(self, ctx:MT22Parser.OtherStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stm.
    def visitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_vardecl_stm.
    def visitList_vardecl_stm(self, ctx:MT22Parser.List_vardecl_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_vardecl_stmprime.
    def visitList_vardecl_stmprime(self, ctx:MT22Parser.List_vardecl_stmprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_stmprime.
    def visitVardecl_stmprime(self, ctx:MT22Parser.Vardecl_stmprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functiondecl.
    def visitFunctiondecl(self, ctx:MT22Parser.FunctiondeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listparams.
    def visitListparams(self, ctx:MT22Parser.ListparamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listparamsprime.
    def visitListparamsprime(self, ctx:MT22Parser.ListparamsprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stm.
    def visitCall_stm(self, ctx:MT22Parser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stm.
    def visitReturn_stm(self, ctx:MT22Parser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stm.
    def visitContinue_stm(self, ctx:MT22Parser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stm.
    def visitBreak_stm(self, ctx:MT22Parser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stm.
    def visitDo_while_stm(self, ctx:MT22Parser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stm.
    def visitWhile_stm(self, ctx:MT22Parser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stm.
    def visitFor_stm(self, ctx:MT22Parser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stm.
    def visitAssign_stm(self, ctx:MT22Parser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdecl.
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variablesdecl.
    def visitVariablesdecl(self, ctx:MT22Parser.VariablesdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_id.
    def visitList_id(self, ctx:MT22Parser.List_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#recursion_assi.
    def visitRecursion_assi(self, ctx:MT22Parser.Recursion_assiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assi_components.
    def visitAssi_components(self, ctx:MT22Parser.Assi_componentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assi_components_EQ.
    def visitAssi_components_EQ(self, ctx:MT22Parser.Assi_components_EQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_types.
    def visitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_types_for_param.
    def visitAtomic_types_for_param(self, ctx:MT22Parser.Atomic_types_for_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_type.
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listexps.
    def visitListexps(self, ctx:MT22Parser.ListexpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listexpsprime.
    def visitListexpsprime(self, ctx:MT22Parser.ListexpsprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        return self.visitChildren(ctx)



del MT22Parser