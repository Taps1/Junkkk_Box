public class AutoConversionDemo{
public static void main(String args[]){
byte num1 = 10;
int num2 = num1;
// byte num3 = num2; Not valid
byte num3 = (byte)num2;
System.out.println(num1+" "+num2+" "+num3);
}
}
