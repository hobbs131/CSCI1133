public class Calculator {
  private double value1;
  private double value2;

  public Calculator(double v1, double v2) {
      value1 = v1;
      value2 = v2;
  }
  public void setValue(double v1, double v2) {
      value1 = v1;
      value2 = v2;
  }
  public double sum() {
    return value1 + value2;
  }
  public double difference() {
    return value1 - value2;
  }

  public double product(){
    return value1 * value2;
  }

  public double quotient(){
    return (double)(value1 / value2);
  }

  public static void main(String[] args) {
      for (int i = 0; i<=20; i++){

      Calculator c = new Calculator(0,0);
      c.setValue(i,i);
      System.out.println("sum " + c.sum());
      System.out.println("difference " + c.difference());
      System.out.println("product " + c.product());
      System.out.println("quotient " + c.quotient());
      System.out.println();

    }
  }
}
