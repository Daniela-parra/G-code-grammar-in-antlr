// Generated from c://Users//dparr//OneDrive - Universidad de los andes//UNIVERSIDAD//9 SEMESTRE//Moviles//G-code//gcode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gcodeParser}.
 */
public interface gcodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gcodeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(gcodeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link gcodeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(gcodeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link gcodeParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(gcodeParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link gcodeParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(gcodeParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link gcodeParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(gcodeParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link gcodeParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(gcodeParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link gcodeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(gcodeParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link gcodeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(gcodeParser.ParameterContext ctx);
}