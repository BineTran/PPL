// Generated from /Users/bientran/Downloads/BTL PPL/assignment1-initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MT22Parser}.
 */
public interface MT22Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MT22Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MT22Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MT22Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#decls}.
	 * @param ctx the parse tree
	 */
	void enterDecls(MT22Parser.DeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#decls}.
	 * @param ctx the parse tree
	 */
	void exitDecls(MT22Parser.DeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(MT22Parser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(MT22Parser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#stm}.
	 * @param ctx the parse tree
	 */
	void enterStm(MT22Parser.StmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#stm}.
	 * @param ctx the parse tree
	 */
	void exitStm(MT22Parser.StmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#matchStm}.
	 * @param ctx the parse tree
	 */
	void enterMatchStm(MT22Parser.MatchStmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#matchStm}.
	 * @param ctx the parse tree
	 */
	void exitMatchStm(MT22Parser.MatchStmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#unmatchStm}.
	 * @param ctx the parse tree
	 */
	void enterUnmatchStm(MT22Parser.UnmatchStmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#unmatchStm}.
	 * @param ctx the parse tree
	 */
	void exitUnmatchStm(MT22Parser.UnmatchStmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#otherStm}.
	 * @param ctx the parse tree
	 */
	void enterOtherStm(MT22Parser.OtherStmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#otherStm}.
	 * @param ctx the parse tree
	 */
	void exitOtherStm(MT22Parser.OtherStmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#block_stm}.
	 * @param ctx the parse tree
	 */
	void enterBlock_stm(MT22Parser.Block_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#block_stm}.
	 * @param ctx the parse tree
	 */
	void exitBlock_stm(MT22Parser.Block_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#list_vardecl_stm}.
	 * @param ctx the parse tree
	 */
	void enterList_vardecl_stm(MT22Parser.List_vardecl_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#list_vardecl_stm}.
	 * @param ctx the parse tree
	 */
	void exitList_vardecl_stm(MT22Parser.List_vardecl_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#list_vardecl_stmprime}.
	 * @param ctx the parse tree
	 */
	void enterList_vardecl_stmprime(MT22Parser.List_vardecl_stmprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#list_vardecl_stmprime}.
	 * @param ctx the parse tree
	 */
	void exitList_vardecl_stmprime(MT22Parser.List_vardecl_stmprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#vardecl_stmprime}.
	 * @param ctx the parse tree
	 */
	void enterVardecl_stmprime(MT22Parser.Vardecl_stmprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#vardecl_stmprime}.
	 * @param ctx the parse tree
	 */
	void exitVardecl_stmprime(MT22Parser.Vardecl_stmprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#functiondecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctiondecl(MT22Parser.FunctiondeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#functiondecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctiondecl(MT22Parser.FunctiondeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#listparams}.
	 * @param ctx the parse tree
	 */
	void enterListparams(MT22Parser.ListparamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#listparams}.
	 * @param ctx the parse tree
	 */
	void exitListparams(MT22Parser.ListparamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#listparamsprime}.
	 * @param ctx the parse tree
	 */
	void enterListparamsprime(MT22Parser.ListparamsprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#listparamsprime}.
	 * @param ctx the parse tree
	 */
	void exitListparamsprime(MT22Parser.ListparamsprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#call_stm}.
	 * @param ctx the parse tree
	 */
	void enterCall_stm(MT22Parser.Call_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#call_stm}.
	 * @param ctx the parse tree
	 */
	void exitCall_stm(MT22Parser.Call_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#return_stm}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stm(MT22Parser.Return_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#return_stm}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stm(MT22Parser.Return_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#continue_stm}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stm(MT22Parser.Continue_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#continue_stm}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stm(MT22Parser.Continue_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#break_stm}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stm(MT22Parser.Break_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#break_stm}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stm(MT22Parser.Break_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#do_while_stm}.
	 * @param ctx the parse tree
	 */
	void enterDo_while_stm(MT22Parser.Do_while_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#do_while_stm}.
	 * @param ctx the parse tree
	 */
	void exitDo_while_stm(MT22Parser.Do_while_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#while_stm}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stm(MT22Parser.While_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#while_stm}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stm(MT22Parser.While_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#for_stm}.
	 * @param ctx the parse tree
	 */
	void enterFor_stm(MT22Parser.For_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#for_stm}.
	 * @param ctx the parse tree
	 */
	void exitFor_stm(MT22Parser.For_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#assign_stm}.
	 * @param ctx the parse tree
	 */
	void enterAssign_stm(MT22Parser.Assign_stmContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#assign_stm}.
	 * @param ctx the parse tree
	 */
	void exitAssign_stm(MT22Parser.Assign_stmContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(MT22Parser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(MT22Parser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#paramdecl}.
	 * @param ctx the parse tree
	 */
	void enterParamdecl(MT22Parser.ParamdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#paramdecl}.
	 * @param ctx the parse tree
	 */
	void exitParamdecl(MT22Parser.ParamdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#variablesdecl}.
	 * @param ctx the parse tree
	 */
	void enterVariablesdecl(MT22Parser.VariablesdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#variablesdecl}.
	 * @param ctx the parse tree
	 */
	void exitVariablesdecl(MT22Parser.VariablesdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#list_id}.
	 * @param ctx the parse tree
	 */
	void enterList_id(MT22Parser.List_idContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#list_id}.
	 * @param ctx the parse tree
	 */
	void exitList_id(MT22Parser.List_idContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#recursion_assi}.
	 * @param ctx the parse tree
	 */
	void enterRecursion_assi(MT22Parser.Recursion_assiContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#recursion_assi}.
	 * @param ctx the parse tree
	 */
	void exitRecursion_assi(MT22Parser.Recursion_assiContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#assi_components}.
	 * @param ctx the parse tree
	 */
	void enterAssi_components(MT22Parser.Assi_componentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#assi_components}.
	 * @param ctx the parse tree
	 */
	void exitAssi_components(MT22Parser.Assi_componentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#assi_components_EQ}.
	 * @param ctx the parse tree
	 */
	void enterAssi_components_EQ(MT22Parser.Assi_components_EQContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#assi_components_EQ}.
	 * @param ctx the parse tree
	 */
	void exitAssi_components_EQ(MT22Parser.Assi_components_EQContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#atomic_types}.
	 * @param ctx the parse tree
	 */
	void enterAtomic_types(MT22Parser.Atomic_typesContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#atomic_types}.
	 * @param ctx the parse tree
	 */
	void exitAtomic_types(MT22Parser.Atomic_typesContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#atomic_types_for_param}.
	 * @param ctx the parse tree
	 */
	void enterAtomic_types_for_param(MT22Parser.Atomic_types_for_paramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#atomic_types_for_param}.
	 * @param ctx the parse tree
	 */
	void exitAtomic_types_for_param(MT22Parser.Atomic_types_for_paramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#array_type}.
	 * @param ctx the parse tree
	 */
	void enterArray_type(MT22Parser.Array_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#array_type}.
	 * @param ctx the parse tree
	 */
	void exitArray_type(MT22Parser.Array_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#dimensions}.
	 * @param ctx the parse tree
	 */
	void enterDimensions(MT22Parser.DimensionsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#dimensions}.
	 * @param ctx the parse tree
	 */
	void exitDimensions(MT22Parser.DimensionsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#element_type}.
	 * @param ctx the parse tree
	 */
	void enterElement_type(MT22Parser.Element_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#element_type}.
	 * @param ctx the parse tree
	 */
	void exitElement_type(MT22Parser.Element_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#arraylit}.
	 * @param ctx the parse tree
	 */
	void enterArraylit(MT22Parser.ArraylitContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#arraylit}.
	 * @param ctx the parse tree
	 */
	void exitArraylit(MT22Parser.ArraylitContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#listexps}.
	 * @param ctx the parse tree
	 */
	void enterListexps(MT22Parser.ListexpsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#listexps}.
	 * @param ctx the parse tree
	 */
	void exitListexps(MT22Parser.ListexpsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#listexpsprime}.
	 * @param ctx the parse tree
	 */
	void enterListexpsprime(MT22Parser.ListexpsprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#listexpsprime}.
	 * @param ctx the parse tree
	 */
	void exitListexpsprime(MT22Parser.ListexpsprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MT22Parser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MT22Parser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr1}.
	 * @param ctx the parse tree
	 */
	void enterExpr1(MT22Parser.Expr1Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr1}.
	 * @param ctx the parse tree
	 */
	void exitExpr1(MT22Parser.Expr1Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterExpr2(MT22Parser.Expr2Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitExpr2(MT22Parser.Expr2Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr3}.
	 * @param ctx the parse tree
	 */
	void enterExpr3(MT22Parser.Expr3Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr3}.
	 * @param ctx the parse tree
	 */
	void exitExpr3(MT22Parser.Expr3Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr4}.
	 * @param ctx the parse tree
	 */
	void enterExpr4(MT22Parser.Expr4Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr4}.
	 * @param ctx the parse tree
	 */
	void exitExpr4(MT22Parser.Expr4Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr5}.
	 * @param ctx the parse tree
	 */
	void enterExpr5(MT22Parser.Expr5Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr5}.
	 * @param ctx the parse tree
	 */
	void exitExpr5(MT22Parser.Expr5Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr6}.
	 * @param ctx the parse tree
	 */
	void enterExpr6(MT22Parser.Expr6Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr6}.
	 * @param ctx the parse tree
	 */
	void exitExpr6(MT22Parser.Expr6Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr7}.
	 * @param ctx the parse tree
	 */
	void enterExpr7(MT22Parser.Expr7Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr7}.
	 * @param ctx the parse tree
	 */
	void exitExpr7(MT22Parser.Expr7Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#expr8}.
	 * @param ctx the parse tree
	 */
	void enterExpr8(MT22Parser.Expr8Context ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#expr8}.
	 * @param ctx the parse tree
	 */
	void exitExpr8(MT22Parser.Expr8Context ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#subexpr}.
	 * @param ctx the parse tree
	 */
	void enterSubexpr(MT22Parser.SubexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#subexpr}.
	 * @param ctx the parse tree
	 */
	void exitSubexpr(MT22Parser.SubexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MT22Parser#callexpr}.
	 * @param ctx the parse tree
	 */
	void enterCallexpr(MT22Parser.CallexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MT22Parser#callexpr}.
	 * @param ctx the parse tree
	 */
	void exitCallexpr(MT22Parser.CallexprContext ctx);
}