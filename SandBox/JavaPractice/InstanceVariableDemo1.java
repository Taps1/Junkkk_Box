public class InstanceVariableDemo1
    {
        int i;
	byte b;
	boolean bool;
	short sh;
	char ch;
	float fl;
	long ln;
	double dbl;
    	public static void main(String args[])
		{
      			InstanceVariableDemo1 demo = new InstanceVariableDemo1();
			demo.show();
		}
        public void show()
		{
			System.out.println("The value if integer is: "+i);
			System.out.println("The value if byte is: "+b);
			System.out.println("The value if boolean is: "+bool);
			System.out.println("The value if short is: "+sh);
			System.out.println("The value if char is: "+ch);
			System.out.println("The value if float is: "+fl);
			System.out.println("The value if long is: "+ln);
			System.out.println("The value if double is: "+dbl);
	    }
}	
