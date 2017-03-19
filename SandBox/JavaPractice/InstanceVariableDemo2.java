class Student
	{
		private String studentName;
		int studentMarks;
        public void display()
		{
			System.out.println(studentName);
			System.out.println(studentMarks);
		}
	}

public class InstanceVariableDemo2
	{
		public static void main(String args[])
		{
			Student st1 = new Student();
			st1.studentName = "Suraj";
			st1.studentMarks = 60;

			Student st2 = new Student();
			st2.studentName = "Ravi";
			st2.studentMarks = 70;
			System.out.println("from Main Class - St1: "+st1.studentName+' '+st1.studentMarks);
			System.out.println("from Main Class - St2: "+st2.studentName+' '+st2.studentMarks);
                        st1.display();
			st2.display();
			
		}
}
