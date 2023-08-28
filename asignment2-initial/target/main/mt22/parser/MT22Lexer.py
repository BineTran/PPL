# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\7\2\u0089\n\2\f\2\16\2\u008c\13\2\5\2\u008e\n")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u009a\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a3\n\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00b5\n\3\3\4\3\4\3\5\3\5\3\6\6\6\u00bc\n\6\r\6\16")
        buf.write("\6\u00bd\3\7\3\7\5\7\u00c2\n\7\3\7\6\7\u00c5\n\7\r\7\16")
        buf.write("\7\u00c6\3\b\3\b\5\b\u00cb\n\b\3\t\3\t\7\t\u00cf\n\t\f")
        buf.write("\t\16\t\u00d2\13\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00da\n")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\38\38\38\39\39\39\39\39\39\3:\3:\7:\u0194\n:\f")
        buf.write(":\16:\u0197\13:\3;\3;\3;\3;\7;\u019d\n;\f;\16;\u01a0\13")
        buf.write(";\3;\3;\3<\3<\3<\3<\7<\u01a8\n<\f<\16<\u01ab\13<\3<\3")
        buf.write("<\3<\3<\3<\3=\6=\u01b3\n=\r=\16=\u01b4\3=\3=\3>\3>\7>")
        buf.write("\u01bb\n>\f>\16>\u01be\13>\3>\5>\u01c1\n>\3>\5>\u01c4")
        buf.write("\n>\3>\3>\3?\3?\7?\u01ca\n?\f?\16?\u01cd\13?\3?\3?\3?")
        buf.write("\3@\3@\3@\5@\u01d5\n@\3A\3A\3A\3\u01a9\2B\3\3\5\4\7\2")
        buf.write("\t\2\13\2\r\2\17\5\21\6\23\2\25\7\27\b\31\t\33\n\35\13")
        buf.write("\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27")
        buf.write("\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W")
        buf.write("(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{:")
        buf.write("};\177\2\u0081<\3\2\f\3\2\63;\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17\"\"\2\u01ea\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\u0081\3\2\2\2\3\u008d\3\2\2\2\5\u00b4\3")
        buf.write("\2\2\2\7\u00b6\3\2\2\2\t\u00b8\3\2\2\2\13\u00bb\3\2\2")
        buf.write("\2\r\u00bf\3\2\2\2\17\u00ca\3\2\2\2\21\u00cc\3\2\2\2\23")
        buf.write("\u00d9\3\2\2\2\25\u00db\3\2\2\2\27\u00dd\3\2\2\2\31\u00df")
        buf.write("\3\2\2\2\33\u00e1\3\2\2\2\35\u00e3\3\2\2\2\37\u00e5\3")
        buf.write("\2\2\2!\u00e7\3\2\2\2#\u00e9\3\2\2\2%\u00eb\3\2\2\2\'")
        buf.write("\u00ed\3\2\2\2)\u00ef\3\2\2\2+\u00f1\3\2\2\2-\u00f3\3")
        buf.write("\2\2\2/\u00f5\3\2\2\2\61\u00f7\3\2\2\2\63\u00f9\3\2\2")
        buf.write("\2\65\u00fb\3\2\2\2\67\u00fd\3\2\2\29\u0100\3\2\2\2;\u0103")
        buf.write("\3\2\2\2=\u0106\3\2\2\2?\u0109\3\2\2\2A\u010b\3\2\2\2")
        buf.write("C\u010e\3\2\2\2E\u0110\3\2\2\2G\u0113\3\2\2\2I\u0116\3")
        buf.write("\2\2\2K\u011b\3\2\2\2M\u0121\3\2\2\2O\u0129\3\2\2\2Q\u012c")
        buf.write("\3\2\2\2S\u0131\3\2\2\2U\u0137\3\2\2\2W\u013d\3\2\2\2")
        buf.write("Y\u0141\3\2\2\2[\u014a\3\2\2\2]\u014d\3\2\2\2_\u0155\3")
        buf.write("\2\2\2a\u015c\3\2\2\2c\u0163\3\2\2\2e\u0168\3\2\2\2g\u016e")
        buf.write("\3\2\2\2i\u0173\3\2\2\2k\u0177\3\2\2\2m\u0180\3\2\2\2")
        buf.write("o\u0183\3\2\2\2q\u018b\3\2\2\2s\u0191\3\2\2\2u\u0198\3")
        buf.write("\2\2\2w\u01a3\3\2\2\2y\u01b2\3\2\2\2{\u01b8\3\2\2\2}\u01c7")
        buf.write("\3\2\2\2\177\u01d4\3\2\2\2\u0081\u01d6\3\2\2\2\u0083\u008e")
        buf.write("\7\62\2\2\u0084\u008a\t\2\2\2\u0085\u0089\t\3\2\2\u0086")
        buf.write("\u0087\7a\2\2\u0087\u0089\t\3\2\2\u0088\u0085\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3")
        buf.write("\2\2\2\u008a\u008b\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a")
        buf.write("\3\2\2\2\u008d\u0083\3\2\2\2\u008d\u0084\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0090\b\2\2\2\u0090\4\3\2\2\2\u0091")
        buf.write("\u0099\5\7\4\2\u0092\u0093\5\t\5\2\u0093\u0094\5\13\6")
        buf.write("\2\u0094\u0095\5\r\7\2\u0095\u009a\3\2\2\2\u0096\u0097")
        buf.write("\5\t\5\2\u0097\u0098\5\r\7\2\u0098\u009a\3\2\2\2\u0099")
        buf.write("\u0092\3\2\2\2\u0099\u0096\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009c\b\3\3\2\u009c\u00b5\3\2\2\2\u009d\u00a2\5")
        buf.write("\7\4\2\u009e\u00a3\5\t\5\2\u009f\u00a0\5\t\5\2\u00a0\u00a1")
        buf.write("\5\13\6\2\u00a1\u00a3\3\2\2\2\u00a2\u009e\3\2\2\2\u00a2")
        buf.write("\u009f\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\b\3\4\2")
        buf.write("\u00a5\u00b5\3\2\2\2\u00a6\u00a7\5\7\4\2\u00a7\u00a8\5")
        buf.write("\r\7\2\u00a8\u00a9\b\3\5\2\u00a9\u00b5\3\2\2\2\u00aa\u00ab")
        buf.write("\5\t\5\2\u00ab\u00ac\5\13\6\2\u00ac\u00ad\5\r\7\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00af\b\3\6\2\u00af\u00b5\3\2\2\2")
        buf.write("\u00b0\u00b1\5\t\5\2\u00b1\u00b2\5\r\7\2\u00b2\u00b3\b")
        buf.write("\3\7\2\u00b3\u00b5\3\2\2\2\u00b4\u0091\3\2\2\2\u00b4\u009d")
        buf.write("\3\2\2\2\u00b4\u00a6\3\2\2\2\u00b4\u00aa\3\2\2\2\u00b4")
        buf.write("\u00b0\3\2\2\2\u00b5\6\3\2\2\2\u00b6\u00b7\5\3\2\2\u00b7")
        buf.write("\b\3\2\2\2\u00b8\u00b9\5!\21\2\u00b9\n\3\2\2\2\u00ba\u00bc")
        buf.write("\t\3\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\f\3\2\2\2\u00bf")
        buf.write("\u00c1\t\4\2\2\u00c0\u00c2\t\5\2\2\u00c1\u00c0\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c5\t")
        buf.write("\3\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\16\3\2\2\2\u00c8\u00cb")
        buf.write("\5c\62\2\u00c9\u00cb\5S*\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00cb\20\3\2\2\2\u00cc\u00d0\7$\2\2\u00cd\u00cf")
        buf.write("\5\23\n\2\u00ce\u00cd\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d3\u00d4\7$\2\2\u00d4\u00d5\b")
        buf.write("\t\b\2\u00d5\22\3\2\2\2\u00d6\u00da\n\6\2\2\u00d7\u00d8")
        buf.write("\7^\2\2\u00d8\u00da\t\7\2\2\u00d9\u00d6\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\24\3\2\2\2\u00db\u00dc\7*\2\2\u00dc")
        buf.write("\26\3\2\2\2\u00dd\u00de\7+\2\2\u00de\30\3\2\2\2\u00df")
        buf.write("\u00e0\7}\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7\177\2\2\u00e2")
        buf.write("\34\3\2\2\2\u00e3\u00e4\7]\2\2\u00e4\36\3\2\2\2\u00e5")
        buf.write("\u00e6\7_\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7\60\2\2\u00e8")
        buf.write("\"\3\2\2\2\u00e9\u00ea\7.\2\2\u00ea$\3\2\2\2\u00eb\u00ec")
        buf.write("\7=\2\2\u00ec&\3\2\2\2\u00ed\u00ee\7<\2\2\u00ee(\3\2\2")
        buf.write("\2\u00ef\u00f0\7?\2\2\u00f0*\3\2\2\2\u00f1\u00f2\7-\2")
        buf.write("\2\u00f2,\3\2\2\2\u00f3\u00f4\7/\2\2\u00f4.\3\2\2\2\u00f5")
        buf.write("\u00f6\7,\2\2\u00f6\60\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8")
        buf.write("\62\3\2\2\2\u00f9\u00fa\7\'\2\2\u00fa\64\3\2\2\2\u00fb")
        buf.write("\u00fc\7#\2\2\u00fc\66\3\2\2\2\u00fd\u00fe\7(\2\2\u00fe")
        buf.write("\u00ff\7(\2\2\u00ff8\3\2\2\2\u0100\u0101\7~\2\2\u0101")
        buf.write("\u0102\7~\2\2\u0102:\3\2\2\2\u0103\u0104\7?\2\2\u0104")
        buf.write("\u0105\7?\2\2\u0105<\3\2\2\2\u0106\u0107\7#\2\2\u0107")
        buf.write("\u0108\7?\2\2\u0108>\3\2\2\2\u0109\u010a\7>\2\2\u010a")
        buf.write("@\3\2\2\2\u010b\u010c\7>\2\2\u010c\u010d\7?\2\2\u010d")
        buf.write("B\3\2\2\2\u010e\u010f\7@\2\2\u010fD\3\2\2\2\u0110\u0111")
        buf.write("\7@\2\2\u0111\u0112\7?\2\2\u0112F\3\2\2\2\u0113\u0114")
        buf.write("\7<\2\2\u0114\u0115\7<\2\2\u0115H\3\2\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7w\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7q\2\2\u011aJ\3\2\2\2\u011b\u011c\7d\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7g\2\2\u011e\u011f\7c\2\2\u011f\u0120")
        buf.write("\7m\2\2\u0120L\3\2\2\2\u0121\u0122\7d\2\2\u0122\u0123")
        buf.write("\7q\2\2\u0123\u0124\7q\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7g\2\2\u0126\u0127\7c\2\2\u0127\u0128\7p\2\2\u0128N\3")
        buf.write("\2\2\2\u0129\u012a\7f\2\2\u012a\u012b\7q\2\2\u012bP\3")
        buf.write("\2\2\2\u012c\u012d\7g\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7u\2\2\u012f\u0130\7g\2\2\u0130R\3\2\2\2\u0131\u0132")
        buf.write("\7h\2\2\u0132\u0133\7c\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7u\2\2\u0135\u0136\7g\2\2\u0136T\3\2\2\2\u0137\u0138")
        buf.write("\7h\2\2\u0138\u0139\7n\2\2\u0139\u013a\7q\2\2\u013a\u013b")
        buf.write("\7c\2\2\u013b\u013c\7v\2\2\u013cV\3\2\2\2\u013d\u013e")
        buf.write("\7h\2\2\u013e\u013f\7q\2\2\u013f\u0140\7t\2\2\u0140X\3")
        buf.write("\2\2\2\u0141\u0142\7h\2\2\u0142\u0143\7w\2\2\u0143\u0144")
        buf.write("\7p\2\2\u0144\u0145\7e\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7q\2\2\u0148\u0149\7p\2\2\u0149Z\3")
        buf.write("\2\2\2\u014a\u014b\7k\2\2\u014b\u014c\7h\2\2\u014c\\\3")
        buf.write("\2\2\2\u014d\u014e\7k\2\2\u014e\u014f\7p\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7g\2\2\u0151\u0152\7i\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153\u0154\7t\2\2\u0154^\3\2\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\u0157\7g\2\2\u0157\u0158\7v\2\2\u0158\u0159")
        buf.write("\7w\2\2\u0159\u015a\7t\2\2\u015a\u015b\7p\2\2\u015b`\3")
        buf.write("\2\2\2\u015c\u015d\7u\2\2\u015d\u015e\7v\2\2\u015e\u015f")
        buf.write("\7t\2\2\u015f\u0160\7k\2\2\u0160\u0161\7p\2\2\u0161\u0162")
        buf.write("\7i\2\2\u0162b\3\2\2\2\u0163\u0164\7v\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\u0166\7w\2\2\u0166\u0167\7g\2\2\u0167d\3")
        buf.write("\2\2\2\u0168\u0169\7y\2\2\u0169\u016a\7j\2\2\u016a\u016b")
        buf.write("\7k\2\2\u016b\u016c\7n\2\2\u016c\u016d\7g\2\2\u016df\3")
        buf.write("\2\2\2\u016e\u016f\7x\2\2\u016f\u0170\7q\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7f\2\2\u0172h\3\2\2\2\u0173\u0174")
        buf.write("\7q\2\2\u0174\u0175\7w\2\2\u0175\u0176\7v\2\2\u0176j\3")
        buf.write("\2\2\2\u0177\u0178\7e\2\2\u0178\u0179\7q\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a\u017b\7v\2\2\u017b\u017c\7k\2\2\u017c\u017d")
        buf.write("\7p\2\2\u017d\u017e\7w\2\2\u017e\u017f\7g\2\2\u017fl\3")
        buf.write("\2\2\2\u0180\u0181\7q\2\2\u0181\u0182\7h\2\2\u0182n\3")
        buf.write("\2\2\2\u0183\u0184\7k\2\2\u0184\u0185\7p\2\2\u0185\u0186")
        buf.write("\7j\2\2\u0186\u0187\7g\2\2\u0187\u0188\7t\2\2\u0188\u0189")
        buf.write("\7k\2\2\u0189\u018a\7v\2\2\u018ap\3\2\2\2\u018b\u018c")
        buf.write("\7c\2\2\u018c\u018d\7t\2\2\u018d\u018e\7t\2\2\u018e\u018f")
        buf.write("\7c\2\2\u018f\u0190\7{\2\2\u0190r\3\2\2\2\u0191\u0195")
        buf.write("\t\b\2\2\u0192\u0194\t\t\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196t\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\7\61\2")
        buf.write("\2\u0199\u019a\7\61\2\2\u019a\u019e\3\2\2\2\u019b\u019d")
        buf.write("\n\n\2\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1\u01a2\b;\t\2\u01a2v\3\2\2\2")
        buf.write("\u01a3\u01a4\7\61\2\2\u01a4\u01a5\7,\2\2\u01a5\u01a9\3")
        buf.write("\2\2\2\u01a6\u01a8\13\2\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("\u01ab\3\2\2\2\u01a9\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\7")
        buf.write(",\2\2\u01ad\u01ae\7\61\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0")
        buf.write("\b<\t\2\u01b0x\3\2\2\2\u01b1\u01b3\t\13\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\b=\t\2")
        buf.write("\u01b7z\3\2\2\2\u01b8\u01bc\7$\2\2\u01b9\u01bb\5\23\n")
        buf.write("\2\u01ba\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be")
        buf.write("\u01bc\3\2\2\2\u01bf\u01c1\t\n\2\2\u01c0\u01bf\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01c4\7")
        buf.write("\2\2\3\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5")
        buf.write("\3\2\2\2\u01c5\u01c6\b>\n\2\u01c6|\3\2\2\2\u01c7\u01cb")
        buf.write("\7$\2\2\u01c8\u01ca\5\23\n\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\5")
        buf.write("\177@\2\u01cf\u01d0\b?\13\2\u01d0~\3\2\2\2\u01d1\u01d2")
        buf.write("\7^\2\2\u01d2\u01d5\n\7\2\2\u01d3\u01d5\7^\2\2\u01d4\u01d1")
        buf.write("\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u0080\3\2\2\2\u01d6")
        buf.write("\u01d7\13\2\2\2\u01d7\u01d8\bA\f\2\u01d8\u0082\3\2\2\2")
        buf.write("\30\2\u0088\u008a\u008d\u0099\u00a2\u00b4\u00bd\u00c1")
        buf.write("\u00c6\u00ca\u00d0\u00d9\u0195\u019e\u01a9\u01b4\u01bc")
        buf.write("\u01c0\u01c3\u01cb\u01d4\r\3\2\2\3\3\3\3\3\4\3\3\5\3\3")
        buf.write("\6\3\3\7\3\t\b\b\2\2\3>\t\3?\n\3A\13")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLLIT = 3
    STRINGLIT = 4
    LP = 5
    RP = 6
    LCURB = 7
    RCURB = 8
    LSQAB = 9
    RSQAB = 10
    DOT = 11
    COMMA = 12
    SEMICOL = 13
    COLON = 14
    EQUAL = 15
    ADD = 16
    SUBTRAC = 17
    MULTI = 18
    DIVIS = 19
    MODUL = 20
    NOT = 21
    AND = 22
    OR = 23
    ISEQUAL = 24
    NOTEQUAL = 25
    LESSTHAN = 26
    LESSTHANOREQ = 27
    GREATERTHAN = 28
    GREATERTHANOREQ = 29
    STRINGCON = 30
    AUTO = 31
    BREAK = 32
    BOOLEAN = 33
    DO = 34
    ELSE = 35
    FALSE = 36
    FLOAT = 37
    FOR = 38
    FUNCTION = 39
    IF = 40
    INTERGER = 41
    RETURN = 42
    STRING = 43
    TRUE = 44
    WHILE = 45
    VOID = 46
    OUT = 47
    CONTINUE = 48
    OF = 49
    INHERIT = 50
    ARRAY = 51
    ID = 52
    CMSINGLE = 53
    CMMULTI = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", "','", "';'", 
            "':'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "LP", "RP", "LCURB", 
            "RCURB", "LSQAB", "RSQAB", "DOT", "COMMA", "SEMICOL", "COLON", 
            "EQUAL", "ADD", "SUBTRAC", "MULTI", "DIVIS", "MODUL", "NOT", 
            "AND", "OR", "ISEQUAL", "NOTEQUAL", "LESSTHAN", "LESSTHANOREQ", 
            "GREATERTHAN", "GREATERTHANOREQ", "STRINGCON", "AUTO", "BREAK", 
            "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTERGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ID", "CMSINGLE", 
            "CMMULTI", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "INTPART", "DOT_FLOAT", "DECPART", 
                  "EXPPART", "BOOLLIT", "STRINGLIT", "CHARINSTR", "LP", 
                  "RP", "LCURB", "RCURB", "LSQAB", "RSQAB", "DOT", "COMMA", 
                  "SEMICOL", "COLON", "EQUAL", "ADD", "SUBTRAC", "MULTI", 
                  "DIVIS", "MODUL", "NOT", "AND", "OR", "ISEQUAL", "NOTEQUAL", 
                  "LESSTHAN", "LESSTHANOREQ", "GREATERTHAN", "GREATERTHANOREQ", 
                  "STRINGCON", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTERGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ID", "CMSINGLE", "CMMULTI", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_PART", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTLIT_action 
            actions[1] = self.FLOATLIT_action 
            actions[7] = self.STRINGLIT_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','');
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace('_',''); 
     

        if actionIndex == 2:
             self.text = self.text.replace('_',''); 
     

        if actionIndex == 3:
             self.text = self.text.replace('_',''); 
     

        if actionIndex == 4:
             self.text = self.text.replace('_',''); 
     

        if actionIndex == 5:
             self.text = self.text.replace('_',''); 
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
            raise ErrorToken(self.text)
     


