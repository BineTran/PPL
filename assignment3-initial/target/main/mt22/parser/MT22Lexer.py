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
        buf.write("\u01c5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\7\2\u0087\n\2\f\2\16\2\u008a\13\2\5\2\u008c\n\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3\u00a1\n\3\3\4\3\4\3\5\3\5\7\5\u00a7")
        buf.write("\n\5\f\5\16\5\u00aa\13\5\3\6\3\6\5\6\u00ae\n\6\3\6\6\6")
        buf.write("\u00b1\n\6\r\6\16\6\u00b2\3\7\3\7\5\7\u00b7\n\7\3\b\3")
        buf.write("\b\7\b\u00bb\n\b\f\b\16\b\u00be\13\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\5\t\u00c6\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\39\39\79\u0180\n9\f9\169\u0183\139\3:\3:\3:\3:\7:\u0189")
        buf.write("\n:\f:\16:\u018c\13:\3:\3:\3;\3;\3;\3;\7;\u0194\n;\f;")
        buf.write("\16;\u0197\13;\3;\3;\3;\3;\3;\3<\6<\u019f\n<\r<\16<\u01a0")
        buf.write("\3<\3<\3=\3=\7=\u01a7\n=\f=\16=\u01aa\13=\3=\5=\u01ad")
        buf.write("\n=\3=\5=\u01b0\n=\3=\3=\3>\3>\7>\u01b6\n>\f>\16>\u01b9")
        buf.write("\13>\3>\3>\3>\3?\3?\3?\5?\u01c1\n?\3@\3@\3@\3\u0195\2")
        buf.write("A\3\3\5\4\7\2\t\2\13\2\r\5\17\6\21\2\23\7\25\b\27\t\31")
        buf.write("\n\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61")
        buf.write("\26\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K")
        buf.write("#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66")
        buf.write("s\67u8w9y:{;}\2\177<\3\2\f\3\2\63;\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\f\16\17\"\"\2\u01d4")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2\177\3\2\2\2\3\u008b\3\2\2\2\5\u00a0\3")
        buf.write("\2\2\2\7\u00a2\3\2\2\2\t\u00a4\3\2\2\2\13\u00ab\3\2\2")
        buf.write("\2\r\u00b6\3\2\2\2\17\u00b8\3\2\2\2\21\u00c5\3\2\2\2\23")
        buf.write("\u00c7\3\2\2\2\25\u00c9\3\2\2\2\27\u00cb\3\2\2\2\31\u00cd")
        buf.write("\3\2\2\2\33\u00cf\3\2\2\2\35\u00d1\3\2\2\2\37\u00d3\3")
        buf.write("\2\2\2!\u00d5\3\2\2\2#\u00d7\3\2\2\2%\u00d9\3\2\2\2\'")
        buf.write("\u00db\3\2\2\2)\u00dd\3\2\2\2+\u00df\3\2\2\2-\u00e1\3")
        buf.write("\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2\2\63\u00e7\3\2\2")
        buf.write("\2\65\u00e9\3\2\2\2\67\u00ec\3\2\2\29\u00ef\3\2\2\2;\u00f2")
        buf.write("\3\2\2\2=\u00f5\3\2\2\2?\u00f7\3\2\2\2A\u00fa\3\2\2\2")
        buf.write("C\u00fc\3\2\2\2E\u00ff\3\2\2\2G\u0102\3\2\2\2I\u0107\3")
        buf.write("\2\2\2K\u010d\3\2\2\2M\u0115\3\2\2\2O\u0118\3\2\2\2Q\u011d")
        buf.write("\3\2\2\2S\u0123\3\2\2\2U\u0129\3\2\2\2W\u012d\3\2\2\2")
        buf.write("Y\u0136\3\2\2\2[\u0139\3\2\2\2]\u0141\3\2\2\2_\u0148\3")
        buf.write("\2\2\2a\u014f\3\2\2\2c\u0154\3\2\2\2e\u015a\3\2\2\2g\u015f")
        buf.write("\3\2\2\2i\u0163\3\2\2\2k\u016c\3\2\2\2m\u016f\3\2\2\2")
        buf.write("o\u0177\3\2\2\2q\u017d\3\2\2\2s\u0184\3\2\2\2u\u018f\3")
        buf.write("\2\2\2w\u019e\3\2\2\2y\u01a4\3\2\2\2{\u01b3\3\2\2\2}\u01c0")
        buf.write("\3\2\2\2\177\u01c2\3\2\2\2\u0081\u008c\7\62\2\2\u0082")
        buf.write("\u0088\t\2\2\2\u0083\u0087\t\3\2\2\u0084\u0085\7a\2\2")
        buf.write("\u0085\u0087\t\3\2\2\u0086\u0083\3\2\2\2\u0086\u0084\3")
        buf.write("\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008b")
        buf.write("\u0081\3\2\2\2\u008b\u0082\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\b\2\2\2\u008e\4\3\2\2\2\u008f\u0090\5\7\4")
        buf.write("\2\u0090\u0091\5\t\5\2\u0091\u0092\5\13\6\2\u0092\u0093")
        buf.write("\b\3\3\2\u0093\u00a1\3\2\2\2\u0094\u0095\5\7\4\2\u0095")
        buf.write("\u0096\5\t\5\2\u0096\u0097\b\3\4\2\u0097\u00a1\3\2\2\2")
        buf.write("\u0098\u0099\5\7\4\2\u0099\u009a\5\13\6\2\u009a\u009b")
        buf.write("\b\3\5\2\u009b\u00a1\3\2\2\2\u009c\u009d\5\t\5\2\u009d")
        buf.write("\u009e\5\13\6\2\u009e\u009f\b\3\6\2\u009f\u00a1\3\2\2")
        buf.write("\2\u00a0\u008f\3\2\2\2\u00a0\u0094\3\2\2\2\u00a0\u0098")
        buf.write("\3\2\2\2\u00a0\u009c\3\2\2\2\u00a1\6\3\2\2\2\u00a2\u00a3")
        buf.write("\5\3\2\2\u00a3\b\3\2\2\2\u00a4\u00a8\7\60\2\2\u00a5\u00a7")
        buf.write("\t\3\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\n\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00ab\u00ad\t\4\2\2\u00ac\u00ae\t\5\2\2")
        buf.write("\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3")
        buf.write("\2\2\2\u00af\u00b1\t\3\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\f\3\2\2\2\u00b4\u00b7\5a\61\2\u00b5\u00b7\5Q)\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\16\3\2\2\2\u00b8")
        buf.write("\u00bc\7$\2\2\u00b9\u00bb\5\21\t\2\u00ba\u00b9\3\2\2\2")
        buf.write("\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3")
        buf.write("\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0")
        buf.write("\7$\2\2\u00c0\u00c1\b\b\7\2\u00c1\20\3\2\2\2\u00c2\u00c6")
        buf.write("\n\6\2\2\u00c3\u00c4\7^\2\2\u00c4\u00c6\t\7\2\2\u00c5")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\22\3\2\2\2\u00c7")
        buf.write("\u00c8\7*\2\2\u00c8\24\3\2\2\2\u00c9\u00ca\7+\2\2\u00ca")
        buf.write("\26\3\2\2\2\u00cb\u00cc\7}\2\2\u00cc\30\3\2\2\2\u00cd")
        buf.write("\u00ce\7\177\2\2\u00ce\32\3\2\2\2\u00cf\u00d0\7]\2\2\u00d0")
        buf.write("\34\3\2\2\2\u00d1\u00d2\7_\2\2\u00d2\36\3\2\2\2\u00d3")
        buf.write("\u00d4\7\60\2\2\u00d4 \3\2\2\2\u00d5\u00d6\7.\2\2\u00d6")
        buf.write("\"\3\2\2\2\u00d7\u00d8\7=\2\2\u00d8$\3\2\2\2\u00d9\u00da")
        buf.write("\7<\2\2\u00da&\3\2\2\2\u00db\u00dc\7?\2\2\u00dc(\3\2\2")
        buf.write("\2\u00dd\u00de\7-\2\2\u00de*\3\2\2\2\u00df\u00e0\7/\2")
        buf.write("\2\u00e0,\3\2\2\2\u00e1\u00e2\7,\2\2\u00e2.\3\2\2\2\u00e3")
        buf.write("\u00e4\7\61\2\2\u00e4\60\3\2\2\2\u00e5\u00e6\7\'\2\2\u00e6")
        buf.write("\62\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8\64\3\2\2\2\u00e9")
        buf.write("\u00ea\7(\2\2\u00ea\u00eb\7(\2\2\u00eb\66\3\2\2\2\u00ec")
        buf.write("\u00ed\7~\2\2\u00ed\u00ee\7~\2\2\u00ee8\3\2\2\2\u00ef")
        buf.write("\u00f0\7?\2\2\u00f0\u00f1\7?\2\2\u00f1:\3\2\2\2\u00f2")
        buf.write("\u00f3\7#\2\2\u00f3\u00f4\7?\2\2\u00f4<\3\2\2\2\u00f5")
        buf.write("\u00f6\7>\2\2\u00f6>\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8")
        buf.write("\u00f9\7?\2\2\u00f9@\3\2\2\2\u00fa\u00fb\7@\2\2\u00fb")
        buf.write("B\3\2\2\2\u00fc\u00fd\7@\2\2\u00fd\u00fe\7?\2\2\u00fe")
        buf.write("D\3\2\2\2\u00ff\u0100\7<\2\2\u0100\u0101\7<\2\2\u0101")
        buf.write("F\3\2\2\2\u0102\u0103\7c\2\2\u0103\u0104\7w\2\2\u0104")
        buf.write("\u0105\7v\2\2\u0105\u0106\7q\2\2\u0106H\3\2\2\2\u0107")
        buf.write("\u0108\7d\2\2\u0108\u0109\7t\2\2\u0109\u010a\7g\2\2\u010a")
        buf.write("\u010b\7c\2\2\u010b\u010c\7m\2\2\u010cJ\3\2\2\2\u010d")
        buf.write("\u010e\7d\2\2\u010e\u010f\7q\2\2\u010f\u0110\7q\2\2\u0110")
        buf.write("\u0111\7n\2\2\u0111\u0112\7g\2\2\u0112\u0113\7c\2\2\u0113")
        buf.write("\u0114\7p\2\2\u0114L\3\2\2\2\u0115\u0116\7f\2\2\u0116")
        buf.write("\u0117\7q\2\2\u0117N\3\2\2\2\u0118\u0119\7g\2\2\u0119")
        buf.write("\u011a\7n\2\2\u011a\u011b\7u\2\2\u011b\u011c\7g\2\2\u011c")
        buf.write("P\3\2\2\2\u011d\u011e\7h\2\2\u011e\u011f\7c\2\2\u011f")
        buf.write("\u0120\7n\2\2\u0120\u0121\7u\2\2\u0121\u0122\7g\2\2\u0122")
        buf.write("R\3\2\2\2\u0123\u0124\7h\2\2\u0124\u0125\7n\2\2\u0125")
        buf.write("\u0126\7q\2\2\u0126\u0127\7c\2\2\u0127\u0128\7v\2\2\u0128")
        buf.write("T\3\2\2\2\u0129\u012a\7h\2\2\u012a\u012b\7q\2\2\u012b")
        buf.write("\u012c\7t\2\2\u012cV\3\2\2\2\u012d\u012e\7h\2\2\u012e")
        buf.write("\u012f\7w\2\2\u012f\u0130\7p\2\2\u0130\u0131\7e\2\2\u0131")
        buf.write("\u0132\7v\2\2\u0132\u0133\7k\2\2\u0133\u0134\7q\2\2\u0134")
        buf.write("\u0135\7p\2\2\u0135X\3\2\2\2\u0136\u0137\7k\2\2\u0137")
        buf.write("\u0138\7h\2\2\u0138Z\3\2\2\2\u0139\u013a\7k\2\2\u013a")
        buf.write("\u013b\7p\2\2\u013b\u013c\7v\2\2\u013c\u013d\7g\2\2\u013d")
        buf.write("\u013e\7i\2\2\u013e\u013f\7g\2\2\u013f\u0140\7t\2\2\u0140")
        buf.write("\\\3\2\2\2\u0141\u0142\7t\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\u0144\7v\2\2\u0144\u0145\7w\2\2\u0145\u0146\7t\2\2\u0146")
        buf.write("\u0147\7p\2\2\u0147^\3\2\2\2\u0148\u0149\7u\2\2\u0149")
        buf.write("\u014a\7v\2\2\u014a\u014b\7t\2\2\u014b\u014c\7k\2\2\u014c")
        buf.write("\u014d\7p\2\2\u014d\u014e\7i\2\2\u014e`\3\2\2\2\u014f")
        buf.write("\u0150\7v\2\2\u0150\u0151\7t\2\2\u0151\u0152\7w\2\2\u0152")
        buf.write("\u0153\7g\2\2\u0153b\3\2\2\2\u0154\u0155\7y\2\2\u0155")
        buf.write("\u0156\7j\2\2\u0156\u0157\7k\2\2\u0157\u0158\7n\2\2\u0158")
        buf.write("\u0159\7g\2\2\u0159d\3\2\2\2\u015a\u015b\7x\2\2\u015b")
        buf.write("\u015c\7q\2\2\u015c\u015d\7k\2\2\u015d\u015e\7f\2\2\u015e")
        buf.write("f\3\2\2\2\u015f\u0160\7q\2\2\u0160\u0161\7w\2\2\u0161")
        buf.write("\u0162\7v\2\2\u0162h\3\2\2\2\u0163\u0164\7e\2\2\u0164")
        buf.write("\u0165\7q\2\2\u0165\u0166\7p\2\2\u0166\u0167\7v\2\2\u0167")
        buf.write("\u0168\7k\2\2\u0168\u0169\7p\2\2\u0169\u016a\7w\2\2\u016a")
        buf.write("\u016b\7g\2\2\u016bj\3\2\2\2\u016c\u016d\7q\2\2\u016d")
        buf.write("\u016e\7h\2\2\u016el\3\2\2\2\u016f\u0170\7k\2\2\u0170")
        buf.write("\u0171\7p\2\2\u0171\u0172\7j\2\2\u0172\u0173\7g\2\2\u0173")
        buf.write("\u0174\7t\2\2\u0174\u0175\7k\2\2\u0175\u0176\7v\2\2\u0176")
        buf.write("n\3\2\2\2\u0177\u0178\7c\2\2\u0178\u0179\7t\2\2\u0179")
        buf.write("\u017a\7t\2\2\u017a\u017b\7c\2\2\u017b\u017c\7{\2\2\u017c")
        buf.write("p\3\2\2\2\u017d\u0181\t\b\2\2\u017e\u0180\t\t\2\2\u017f")
        buf.write("\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182r\3\2\2\2\u0183\u0181\3\2\2")
        buf.write("\2\u0184\u0185\7\61\2\2\u0185\u0186\7\61\2\2\u0186\u018a")
        buf.write("\3\2\2\2\u0187\u0189\n\n\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\b")
        buf.write(":\b\2\u018et\3\2\2\2\u018f\u0190\7\61\2\2\u0190\u0191")
        buf.write("\7,\2\2\u0191\u0195\3\2\2\2\u0192\u0194\13\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0198\u0199\7,\2\2\u0199\u019a\7\61\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u019c\b;\b\2\u019cv\3\2\2\2\u019d\u019f")
        buf.write("\t\13\2\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a3\b<\b\2\u01a3x\3\2\2\2\u01a4\u01a8\7$\2\2")
        buf.write("\u01a5\u01a7\5\21\t\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ad\t\n\2\2")
        buf.write("\u01ac\u01ab\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af\3")
        buf.write("\2\2\2\u01ae\u01b0\7\2\2\3\u01af\u01ae\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\b=\t\2\u01b2")
        buf.write("z\3\2\2\2\u01b3\u01b7\7$\2\2\u01b4\u01b6\5\21\t\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3")
        buf.write("\2\2\2\u01ba\u01bb\5}?\2\u01bb\u01bc\b>\n\2\u01bc|\3\2")
        buf.write("\2\2\u01bd\u01be\7^\2\2\u01be\u01c1\n\7\2\2\u01bf\u01c1")
        buf.write("\7^\2\2\u01c0\u01bd\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("~\3\2\2\2\u01c2\u01c3\13\2\2\2\u01c3\u01c4\b@\13\2\u01c4")
        buf.write("\u0080\3\2\2\2\26\2\u0086\u0088\u008b\u00a0\u00a8\u00ad")
        buf.write("\u00b2\u00b6\u00bc\u00c5\u0181\u018a\u0195\u01a0\u01a8")
        buf.write("\u01ac\u01af\u01b7\u01c0\f\3\2\2\3\3\3\3\3\4\3\3\5\3\3")
        buf.write("\6\3\b\7\b\2\2\3=\b\3>\t\3@\n")
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

    ruleNames = [ "INTLIT", "FLOATLIT", "INTPART", "DECPART", "EXPPART", 
                  "BOOLLIT", "STRINGLIT", "CHARINSTR", "LP", "RP", "LCURB", 
                  "RCURB", "LSQAB", "RSQAB", "DOT", "COMMA", "SEMICOL", 
                  "COLON", "EQUAL", "ADD", "SUBTRAC", "MULTI", "DIVIS", 
                  "MODUL", "NOT", "AND", "OR", "ISEQUAL", "NOTEQUAL", "LESSTHAN", 
                  "LESSTHANOREQ", "GREATERTHAN", "GREATERTHANOREQ", "STRINGCON", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTERGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ID", "CMSINGLE", "CMMULTI", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_PART", "ERROR_CHAR" ]

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
            actions[6] = self.STRINGLIT_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
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
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise ErrorToken(self.text)
     


