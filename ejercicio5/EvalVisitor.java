import generated.*;

public class EvalVisitor extends MacLaurinBaseVisitor<Double> {

    @Override
    public Double visitProg(MacLaurinParser.ProgContext ctx) {

        int n = Integer.parseInt(ctx.INT().getText());
        double x = Double.parseDouble(ctx.NUMBER().getText());

        double result = 0;

        for(int i = 0; i <= n; i++){
            result += Math.pow(x, i) / factorial(i);
        }

        System.out.println("Resultado: " + result);

        return result;
    }

    private double factorial(int n){
        double f = 1;
        for(int i = 1; i <= n; i++){
            f *= i;
        }
        return f;
    }
}
