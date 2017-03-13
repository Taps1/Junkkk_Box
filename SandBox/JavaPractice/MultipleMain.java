class MultipleMain
	{
		public static void main(String str1, String str2)
			{
				System.out.println("hello, this is string main method");
			}
		public static void main(int n1, int n2)
			{
				System.out.println("hello, this is integer main method");
			}
		public static void main(String args[])
			{
				main("hey Buddy", "How you doing");
				main(123, 456);
			}
	}
