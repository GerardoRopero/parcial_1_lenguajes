import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import generated.*;

public class Main {

    public static void main(String[] args) throws Exception {

        CharStream input = CharStreams.fromStream(System.in);

        MacLaurinLexer lexer = new MacLaurinLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        MacLaurinParser parser = new MacLaurinParser(tokens);
        ParseTree tree = parser.prog();

        EvalVisitor visitor = new EvalVisitor();
        visitor.visit(tree);
    }
}
