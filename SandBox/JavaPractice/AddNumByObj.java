class Test
	{
		public int add(int x, int y)
		{
			int sum = x + y;
			return sum;
		}
	}

public class AddNumByObj
	{	
		public static void main(String args[])
		{
			System.out.println(args.length);
                        String str1 = args[0];
			String str2 = args[1];
			int num1 = Integer.parseInt(str1);
			int num2 = Integer.parseInt(str2);
			Test t = new Test();
			int result_of_sum = t.add(num1, num2);
			System.out.println("The sum is: "+result_of_sum);
			
		}
	}
