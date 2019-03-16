import java.util.Scanner;

public class Pet {
		public static String pet() {
			int [][] c=new int[5][4];
			Scanner kb=new Scanner(System.in);
			for(int i=0;i<c.length;i++)
				for(int j=0;j<c[0].length;j++) 
					c[i][j]=kb.nextInt();
			int[] sums=new int[5];
			for(int r=0; r<5;r++)
				for(int i=0;i<c[0].length;i++)
					sums[r]=sums[r]+c[r][i];			
			int max=sums[0];
			int maxpos=0;
			for(int i=1;i<sums.length;i++)
				if(sums[i]>=max) {
					max=sums[i];
					maxpos=i;
				}
			maxpos++;
			return maxpos+" "+max;
	}	
		public static void main(String[] args) {
			System.out.println(pet());
				}
		}
