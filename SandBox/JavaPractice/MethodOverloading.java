class Test
{
	public static void add(String s1, String s2)
		{
			String sum_of_string = s1 + s2;
			System.out.println("Sum of "+s1+" & "+s2+" is: "+sum_of_string);
		}
	public static void add(int num1, int num2)
		{
			int result_of_sum = num1 + num2;
			System.out.println("Sum of "+num1+" & "+num2+" is "+result_of_sum);
		}
	}
	
public class MethodOverloading
{
public static void main(String args[])
{

Test.add(1,2);
Test.add("Talat", "Parwez");
}
}
