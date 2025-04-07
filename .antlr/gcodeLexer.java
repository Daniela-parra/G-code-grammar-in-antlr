// Generated from c://Users//dparr//OneDrive - Universidad de los andes//UNIVERSIDAD//9 SEMESTRE//Moviles//G-code//gcode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class gcodeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMENT=1, GCODE=2, MCODE=3, TCODE=4, FCODE=5, SCODE=6, AXIS=7, LETTER=8, 
		NUMBER=9, DIGIT=10, NEWLINE=11, WHITESPACE=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"COMMENT", "GCODE", "MCODE", "TCODE", "FCODE", "SCODE", "AXIS", "LETTER", 
			"NUMBER", "DIGIT", "NEWLINE", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMENT", "GCODE", "MCODE", "TCODE", "FCODE", "SCODE", "AXIS", 
			"LETTER", "NUMBER", "DIGIT", "NEWLINE", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public gcodeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "gcode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\fd\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0005\u0000\u001c\b\u0000\n\u0000"+
		"\f\u0000\u001f\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0004\u0001%\b\u0001\u000b\u0001\f\u0001&\u0001\u0002\u0001\u0002\u0004"+
		"\u0002+\b\u0002\u000b\u0002\f\u0002,\u0001\u0003\u0001\u0003\u0004\u0003"+
		"1\b\u0003\u000b\u0003\f\u00032\u0001\u0004\u0001\u0004\u0004\u00047\b"+
		"\u0004\u000b\u0004\f\u00048\u0001\u0005\u0001\u0005\u0004\u0005=\b\u0005"+
		"\u000b\u0005\f\u0005>\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0003\bF\b\b\u0001\b\u0004\bI\b\b\u000b\b\f\bJ\u0001\b\u0001"+
		"\b\u0004\bO\b\b\u000b\b\f\bP\u0003\bS\b\b\u0001\t\u0001\t\u0001\n\u0003"+
		"\nX\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0004\u000b_\b\u000b"+
		"\u000b\u000b\f\u000b`\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0001\u0000\u0005\u0002\u0000\n"+
		"\n\r\r\u0002\u0000EEXZ\u0005\u0000ADFIKNPRTW\u0001\u000009\u0002\u0000"+
		"\t\t  o\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0001"+
		"\u0019\u0001\u0000\u0000\u0000\u0003\"\u0001\u0000\u0000\u0000\u0005("+
		"\u0001\u0000\u0000\u0000\u0007.\u0001\u0000\u0000\u0000\t4\u0001\u0000"+
		"\u0000\u0000\u000b:\u0001\u0000\u0000\u0000\r@\u0001\u0000\u0000\u0000"+
		"\u000fB\u0001\u0000\u0000\u0000\u0011E\u0001\u0000\u0000\u0000\u0013T"+
		"\u0001\u0000\u0000\u0000\u0015W\u0001\u0000\u0000\u0000\u0017^\u0001\u0000"+
		"\u0000\u0000\u0019\u001d\u0005;\u0000\u0000\u001a\u001c\b\u0000\u0000"+
		"\u0000\u001b\u001a\u0001\u0000\u0000\u0000\u001c\u001f\u0001\u0000\u0000"+
		"\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000"+
		"\u0000\u001e \u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000"+
		" !\u0006\u0000\u0000\u0000!\u0002\u0001\u0000\u0000\u0000\"$\u0005G\u0000"+
		"\u0000#%\u0003\u0013\t\u0000$#\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000"+
		"\u0000&$\u0001\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\'\u0004\u0001"+
		"\u0000\u0000\u0000(*\u0005M\u0000\u0000)+\u0003\u0013\t\u0000*)\u0001"+
		"\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-\u0006\u0001\u0000\u0000\u0000.0\u0005T\u0000"+
		"\u0000/1\u0003\u0013\t\u00000/\u0001\u0000\u0000\u000012\u0001\u0000\u0000"+
		"\u000020\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u00003\b\u0001\u0000"+
		"\u0000\u000046\u0005F\u0000\u000057\u0003\u0013\t\u000065\u0001\u0000"+
		"\u0000\u000078\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001"+
		"\u0000\u0000\u00009\n\u0001\u0000\u0000\u0000:<\u0005S\u0000\u0000;=\u0003"+
		"\u0013\t\u0000<;\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000><\u0001"+
		"\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?\f\u0001\u0000\u0000\u0000"+
		"@A\u0007\u0001\u0000\u0000A\u000e\u0001\u0000\u0000\u0000BC\u0007\u0002"+
		"\u0000\u0000C\u0010\u0001\u0000\u0000\u0000DF\u0005-\u0000\u0000ED\u0001"+
		"\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001\u0000\u0000\u0000"+
		"GI\u0003\u0013\t\u0000HG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"JH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KR\u0001\u0000\u0000"+
		"\u0000LN\u0005.\u0000\u0000MO\u0003\u0013\t\u0000NM\u0001\u0000\u0000"+
		"\u0000OP\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PQ\u0001\u0000"+
		"\u0000\u0000QS\u0001\u0000\u0000\u0000RL\u0001\u0000\u0000\u0000RS\u0001"+
		"\u0000\u0000\u0000S\u0012\u0001\u0000\u0000\u0000TU\u0007\u0003\u0000"+
		"\u0000U\u0014\u0001\u0000\u0000\u0000VX\u0005\r\u0000\u0000WV\u0001\u0000"+
		"\u0000\u0000WX\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0005"+
		"\n\u0000\u0000Z[\u0001\u0000\u0000\u0000[\\\u0006\n\u0000\u0000\\\u0016"+
		"\u0001\u0000\u0000\u0000]_\u0007\u0004\u0000\u0000^]\u0001\u0000\u0000"+
		"\u0000_`\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000"+
		"\u0000\u0000ab\u0001\u0000\u0000\u0000bc\u0006\u000b\u0000\u0000c\u0018"+
		"\u0001\u0000\u0000\u0000\r\u0000\u001d&,28>EJPRW`\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}