public class BankAccount{
  private double balance;
  private String ownerName;
  private String accountNumber;


  public BankAccount(double balance1, String ownerName1, String accountNumber1){
    balance = balance1;
    ownerName = ownerName1;
    accountNumber = accountNumber1;
  }

  public double withdraw(){
    balance - withdrawAmount = balance;
  }

  public double deposit(){
    balance + depositAmount = balance;
  }

  public double compoundInterest(int numYears, double Rate, int numCompounds){
    return balance * (1 + rate/numCompounds)**(numYears*numCompounds);
  }

  public simpleInterest(int numYears, double rate){
    return balance * (1 +numYears*rate);
  }
  public static void main(String[] args) {
    BankAccount c = new BankAccount;
  }
  }
